#!/usr/bin/env python3
"""kic: tools for the Kelvin instrument collection.

    python tools/kic.py validate               check every instrument, card, experiment and lab config
    python tools/kic.py index [--check]        rebuild index.json, CATALOG.md and the instruments/ READMEs
    python tools/kic.py find TEXT              look up instruments, experiments and labs (--idn "<*IDN? reply>")
    python tools/kic.py install [--dry-run]    put the cards Kelvin doesn't have into ~/Kelvin/cards
    python tools/kic.py manuals [ID ...]       download manuals, e.g. for a lab PC that is offline
    python tools/kic.py links                  check that every manual and link still answers
    python tools/kic.py probe ID ADDRESS       ask an instrument who it is and read its settings (sets nothing)

find, install, manuals and links need only Python 3.9 or later. validate, index, manuals --pin and probe also need
PyYAML (pip install pyyaml), and probe needs PyVISA (pip install pyvisa pyvisa-py).
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"
CATALOG = ROOT / "CATALOG.md"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) kelvin-instruments"

ID = re.compile(r"^[a-z0-9][a-z0-9.-]*/[a-z0-9][a-z0-9.-]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ACCESS = ("public", "sign-in", "owners")
SOFTWARE_KINDS = ("python-driver", "other-driver", "vendor-sdk", "vendor-software")   # other: Micro-Manager, LabVIEW, MATLAB

# The card format, as Kelvin reads it (docs/instruments.md in Kelvin, "Writing a card").
CARD_PARAM_KINDS = ("measure", "drive")
CARD_TYPES = ("float", "int", "bool", "enum", "str", "trace", "image")
RAMPS = ("gate", "instrument", "none")
STATUSES = ("community", "lab-verified", "draft")
CONNECTION = {"read_termination": str, "write_termination": str, "baud_rate": int, "data_bits": int,
              "stop_bits": (int, float), "parity": str, "timeout_ms": int, "query_delay": (int, float),
              "write_only": bool, "echo": bool, "ack": str, "set_reply": str}
VAR_NAME = re.compile(r"^[a-z][a-z0-9_]{0,30}$")
VAR_VALUE = re.compile(r"^[A-Za-z0-9_.+-]{1,40}$")
LIB_DENY = {"os", "sys", "subprocess", "shutil", "builtins", "importlib", "runpy", "ctypes", "socket", "pathlib",
            "pickle", "marshal", "multiprocessing", "code", "codeop", "webbrowser", "urllib", "http", "asyncio"}
PLAN_KEYS = {"plan", "description", "device", "requires", "preconditions", "setup", "sweep", "repeat", "time",
             "settle", "measure", "after", "on_abort"}
LAB_INSTRUMENT_KEYS = {"card", "address", "trust", "limits", "rates", "guards", "auto", "connection", "vars"}
CONDITION = re.compile(r"^\s*([A-Za-z_]\w*)\.([A-Za-z_]\w*)\s*(<=|>=|==|!=|<|>)\s*(\S+)\s*$")
# Reads that can start something on the instrument (a measurement that switches an output on, a self-test);
# probe never sends them, as Kelvin's own "Try it" doesn't.
RISKY_READ = re.compile(r"^:?(MEAS|READ|INIT|\*TST|\*CAL|\*RST|\*TRG|TRIG|\*SAV|\*RCL)", re.I)

INSTRUMENT_KEYS = ["schema", "id", "maker", "model", "name", "covers", "kind", "categories", "interfaces", "control",
                   "identify", "card", "manuals", "links", "software", "examples", "notes", "verified"]
EXPERIMENT_KEYS = ["schema", "id", "area", "title", "summary", "roles", "lab", "needs_cards", "setup", "procedure",
                   "plans", "analysis", "pitfalls", "safety", "references"]


class Problems:
    """Errors fail validation; warnings are printed and let it pass."""

    def __init__(self) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append("%s: %s" % (where, msg))


_LOADER: Any = None


def load_yaml(path: Path) -> Any:
    """YAML as Kelvin reads it: YAML 1.2 number rules, so 1e7 and 1.0e7 are numbers (PyYAML alone follows
    YAML 1.1, where an exponent needs a sign and "1.0e7" is a string)."""
    global _LOADER
    try:
        import yaml
    except ImportError:
        sys.exit("This command reads YAML: pip install pyyaml")
    if _LOADER is None:
        class Loader(yaml.SafeLoader):
            pass
        Loader.add_implicit_resolver("tag:yaml.org,2002:float",
                                     re.compile(r"^[-+]?(?:[0-9][0-9_]*)?\.?[0-9_]*[eE][-+]?[0-9]+$"),
                                     list("-+0123456789."))
        _LOADER = Loader
    with open(path, encoding="utf-8") as f:
        return yaml.load(f, Loader=_LOADER)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def kelvin_file(card_id: str) -> str:
    """The name Kelvin gives a card in ~/Kelvin/cards (so its own save and replace find it)."""
    return re.sub(r"[^\w.-]+", "_", card_id).strip("_") + ".yaml"


def is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def https(url: Any) -> bool:
    return isinstance(url, str) and re.match(r"^https://[^\s/]+\.[^\s/]+(/\S*)?$", url) is not None


def strings(x: Any) -> bool:
    return isinstance(x, list) and all(isinstance(s, str) and s.strip() for s in x)


def scpi_header(cmd: str) -> str:
    """A command's header in short form (SOURce:VOLTage[:LEVel] {value} -> SOUR:VOLT), to compare commands.
    Library and web-API cards name the call after the verb (SET output {value} -> SET OUTPUT)."""
    words = cmd.strip().split()
    if len(words) > 1 and words[0].upper() in ("SET", "GET", "PUT", "POST", "PATCH"):
        return "%s %s" % (words[0].upper(), re.split(r"[{=]", words[1], maxsplit=1)[0].upper())
    head = re.split(r"[\s{]", cmd.strip(), maxsplit=1)[0]
    while True:
        shorter = re.sub(r"\[[^\[\]]*\]", "", head)
        if shorter == head:
            break
        head = shorter
    nodes = []
    for node in head.strip(":").split(":"):
        caps = re.match(r"^([A-Z*]+)[a-z]", node)
        nodes.append((caps.group(1) if caps else node).upper().rstrip("?"))
    return ":".join(nodes)


def expand(cmd: str, values: Dict[str, str]) -> str:
    """A card command as sent: optional [:PARTS] left out, {vars} filled in."""
    while True:
        shorter = re.sub(r"\[[^\[\]]*\]", "", cmd)
        if shorter == cmd:
            break
        cmd = shorter
    for k, v in values.items():
        cmd = cmd.replace("{%s}" % k, v)
    return cmd


# ---------------------------------------------------------------- the collection, read from its files

class Collection:
    def __init__(self, problems: Problems) -> None:
        self.p = problems
        self.meta: Dict[str, Any] = load_yaml(ROOT / "collection.yaml")
        self.kind_category: Dict[str, str] = {}
        for cat, c in self.meta["categories"].items():
            for kind in c["kinds"]:
                if kind in self.kind_category:
                    self.p.error("collection.yaml", "kind %s is in two categories" % kind)
                self.kind_category[kind] = cat
        self.instruments: Dict[str, Dict[str, Any]] = {}
        self.paths: Dict[str, Path] = {}          # id -> its folder, instruments/<category>/<kind>/<maker>-<model>
        self.cards: Dict[str, Dict[str, Any]] = {}
        self.experiments: Dict[str, Dict[str, Any]] = {}
        self.labs: Dict[str, Dict[str, Any]] = {}
        self._read()

    def _read(self) -> None:
        shelf = ROOT / "instruments"
        for path in sorted(shelf.glob("*/*/*/instrument.yaml")):
            data = self._load(path)
            if not isinstance(data, dict):
                continue
            iid = str(data.get("id") or rel(path.parent))
            if iid in self.paths:
                self.p.error(rel(path), "id %s is also used in %s" % (iid, rel(self.paths[iid])))
                continue
            self.instruments[iid] = data
            self.paths[iid] = path.parent
            card = path.parent / "card.yaml"
            if card.exists():
                cdata = self._load(card)
                if isinstance(cdata, dict):
                    self.cards[iid] = cdata
        for path in sorted(shelf.rglob("*.yaml")):
            if len(path.relative_to(shelf).parts) != 4 or path.name not in ("instrument.yaml", "card.yaml"):
                self.p.error(rel(path), "instruments live in instruments/<category>/<kind>/<maker>-<model>/")
            elif path.name == "card.yaml" and not (path.parent / "instrument.yaml").exists():
                self.p.error(rel(path), "a card needs an instrument.yaml next to it")
        for path in sorted((ROOT / "experiments").glob("*/*.yaml")):
            data = self._load(path)
            if isinstance(data, dict):
                self.experiments[path.relative_to(ROOT / "experiments").with_suffix("").as_posix()] = data
        for path in sorted((ROOT / "labs").glob("*.yaml")):
            data = self._load(path)
            if isinstance(data, dict):
                self.labs[path.stem] = data

    def _load(self, path: Path) -> Any:
        try:
            data = load_yaml(path)
        except Exception as e:   # a YAML syntax error: say where, keep checking the rest
            self.p.error(rel(path), "not valid YAML: %s" % str(e).replace("\n", " "))
            return None
        if not isinstance(data, dict):
            self.p.error(rel(path), "must be a mapping")
        return data

    def category(self, iid: str) -> str:
        return self.kind_category.get(self.instruments[iid].get("kind", ""), "")

    def folder_for(self, iid: str, kind: Any) -> str:
        """Where an instrument belongs: its kind's category, its kind, then maker-model."""
        return "instruments/%s/%s/%s" % (self.kind_category.get(str(kind), "?"), kind, iid.replace("/", "-"))

    def params(self, card_id: str) -> Dict[str, Dict[str, Any]]:
        card = self.cards.get(card_id) or {}
        ps = card.get("parameters")
        return ps if isinstance(ps, dict) else {}


# ---------------------------------------------------------------- validate

def check_card(where: str, card: Dict[str, Any], p: Problems) -> None:
    """The card format Kelvin reads, checked here so a broken card never reaches a lab."""
    if card.get("card") != 1:
        p.error(where, "card: 1 (the schema version) is required")
    for key in ("id", "model", "kind"):
        if not card.get(key):
            p.error(where, "%s is required" % key)
    if card.get("status") not in STATUSES:
        p.error(where, "status must be one of %s" % ", ".join(STATUSES))
    vars_ = card.get("vars") or {}
    values: Dict[str, str] = {}
    if not isinstance(vars_, dict):
        p.error(where, "vars must be a mapping of name: {default, label}")
        vars_ = {}
    for name, v in vars_.items():
        default = v.get("default") if isinstance(v, dict) else v
        if not VAR_NAME.match(str(name)):
            p.error(where, "vars.%s: names are lowercase letters, digits and _" % name)
        elif default is None or not VAR_VALUE.match(str(default)):
            p.error(where, "vars.%s: a default of letters, digits and . _ + - is required" % name)
        else:
            values[str(name)] = str(default)
    commands = json.dumps({k: v for k, v in card.items() if k != "vars"})
    used = set(re.findall(r"\{([a-z_][a-z0-9_]*)\}", commands)) - {"value", "address"}
    for name in sorted(used - set(values)):
        p.error(where, "the commands use {%s}, which vars does not declare" % name)

    params = card.get("parameters")
    if not isinstance(params, dict) or not params:
        p.error(where, "parameters: at least one is required")
        params = {}
    for name, spec in params.items():
        check_param(where, str(name), spec, params, p)

    identify = card.get("identify") or {}
    check_identify(where, identify, p)
    for u in identify.get("usb") or []:
        if not re.match(r"^[0-9a-fA-F]{4}:[0-9a-fA-F]{4}$", str(u)):
            p.error(where, "identify.usb: %r is not VID:PID in hex" % u)
    for key, value in (card.get("connection") or {}).items():
        kind = CONNECTION.get(key)
        if kind is None:
            p.error(where, "connection.%s is not a setting Kelvin knows (%s)" % (key, ", ".join(sorted(CONNECTION))))
        elif kind is bool and not isinstance(value, bool):
            p.error(where, "connection.%s must be true or false" % key)
        elif kind is not bool and not isinstance(value, kind if isinstance(kind, tuple) else (kind,)):
            p.error(where, "connection.%s has the wrong type" % key)
    on_connect = card.get("on_connect") or []
    setters = {scpi_header(str(s["set"])): n for n, s in params.items() if isinstance(s, dict) and s.get("set")}
    for c in on_connect:
        name = setters.get(scpi_header(str(c)))
        if name:
            p.error(where, "on_connect %r would set %s; connecting must leave every setting as it is" % (c, name))
    if card.get("library"):
        check_library(where, card["library"], p)
        if on_connect:
            p.error(where, "a card with a library connects through library.open, not on_connect")
    if card.get("manual_url") and not https(card["manual_url"]):
        p.error(where, "manual_url must be an https:// address of the maker's manual")
    headline = (card.get("display") or {}).get("headline")
    if headline is not None and not (isinstance(params.get(headline), dict) and params[headline].get("get")):
        p.error(where, "display.headline %r is not a readable parameter" % headline)
    for i, h in enumerate(card.get("health") or []):
        if isinstance(h, dict) and h.get("query"):
            continue
        if isinstance(h, dict) and h.get("read") in params and isinstance(h.get("range"), list) \
                and len(h["range"]) == 2 and all(is_number(x) for x in h["range"]):
            continue
        p.error(where, "health[%d] needs query (+ expect) or read + range: [low, high]" % i)
    raw = card.get("raw") or {}
    for key in ("reset", "blocked"):
        if raw.get(key) is not None and not strings(raw[key]):
            p.error(where, "raw.%s must be a list of commands" % key)
    listen_only = bool((card.get("connection") or {}).get("write_only"))
    if not card.get("library") and not listen_only and not str((card.get("identify") or {}).get("idn") or ""):
        p.warn(where, "no identify.idn: a scan cannot recognise this instrument")
    if not card.get("manual") and not card.get("manual_url"):
        p.warn(where, "say which manual (and chapter) the card follows, under manual:")


def check_param(where: str, name: str, spec: Any, params: Dict[str, Any], p: Problems) -> None:
    at = "%s: parameters.%s" % (where, name)
    if not isinstance(spec, dict):
        p.errors.append(at + ": must be a mapping")
        return
    kind, typ = spec.get("kind"), spec.get("type", "float")
    numeric = typ in ("float", "int")
    if kind not in CARD_PARAM_KINDS:
        p.errors.append(at + ": kind must be measure or drive")
    if typ not in CARD_TYPES:
        p.errors.append(at + ": type must be one of " + ", ".join(CARD_TYPES))
    if not spec.get("get") and not spec.get("set"):
        p.errors.append(at + ": needs a get or set command")
    if spec.get("set") and "{value}" not in str(spec["set"]):
        p.errors.append(at + ": the set command needs {value}")
    if spec.get("get") and "{value}" in str(spec["get"]):
        p.errors.append(at + ": the get command must not contain {value}")
    if typ == "enum" and not (isinstance(spec.get("values"), (list, dict)) and spec["values"]):
        p.errors.append(at + ": an enum needs a list or mapping of values")
    limits = spec.get("limits")
    if limits is not None:
        if not numeric:
            p.errors.append(at + ": only numbers have limits")
        elif not (isinstance(limits, list) and len(limits) == 2 and all(is_number(x) for x in limits)
                  and limits[0] < limits[1]):
            p.errors.append(at + ": limits must be [low, high] with low < high")
            limits = None
    ramp = spec.get("ramp", "none")
    if ramp not in RAMPS:
        p.errors.append(at + ": ramp must be gate, instrument or none")
    if ramp == "gate" and (not numeric or not is_number(spec.get("max_rate")) or spec["max_rate"] <= 0):
        p.errors.append(at + ": a gate-ramped parameter is a number with max_rate > 0")
    if kind == "drive":
        if not spec.get("set"):
            p.errors.append(at + ": a drive needs a set command")
        if typ not in ("float", "int", "bool", "enum"):
            p.errors.append(at + ": a drive is a float, int, bool or enum")
        if spec.get("safe") is None:
            p.errors.append(at + ": a drive needs a safe value")
        if numeric and limits is None:
            p.errors.append(at + ": a numeric drive needs limits")
    for key in ("safe", "default"):
        v = spec.get(key)
        if numeric and v is not None and limits is not None and is_number(v) and not limits[0] <= v <= limits[1]:
            p.errors.append(at + ": %s %s is outside the limits" % (key, v))
    if any(isinstance(x, bool) for x in spec.get("bool_text") or ()):
        p.errors.append(at + ': quote bool_text words, e.g. ["ON", "OFF"] (YAML reads a bare ON as true)')
    if spec.get("acquires") is not None and not isinstance(spec["acquires"], bool):
        p.errors.append(at + ": acquires must be true or false")

    def ref(key: str, ok: bool, what: str) -> None:
        if spec.get(key) is not None and not ok:
            p.errors.append(at + ": %s %r is not %s" % (key, spec[key], what))

    rb = params.get(spec.get("readback"))
    ref("readback", isinstance(rb, dict) and bool(rb.get("get")), "a readable parameter")
    ref("rate_param", spec.get("rate_param") in params, "a parameter of this card")
    for dep in spec.get("enables") or []:
        if not (isinstance(params.get(dep), dict) and params[dep].get("kind") == "drive"):
            p.errors.append(at + ": enables %r, which is not a drive on this card" % dep)
    when = params.get(spec.get("applies_when"))
    ref("applies_when", isinstance(when, dict) and when.get("kind") == "drive" and bool(when.get("get")),
        "a readable drive")
    rw = params.get(spec.get("read_when"))
    ref("read_when", isinstance(rw, dict) and rw.get("type") == "bool", "an on/off parameter")


def check_identify(where: str, identify: Any, p: Problems) -> None:
    if not isinstance(identify, dict):
        p.error(where, "identify must be a mapping {idn, example}")
        return
    idn = identify.get("idn")
    if idn is None:
        return
    try:
        pattern = re.compile(str(idn), re.I)   # Kelvin matches identity replies ignoring case
    except re.error as e:
        p.error(where, "identify.idn is not a valid regex: %s" % e)
        return
    example = identify.get("example")
    if example is not None and not pattern.search(str(example)):
        p.error(where, "identify.example %r does not match identify.idn" % example)


def check_library(where: str, lib: Any, p: Problems) -> None:
    if not isinstance(lib, dict):
        p.error(where, "library must be a mapping")
        return
    if bool(lib.get("module")) == bool(lib.get("dll")):
        p.error(where, "library names either module (a Python module) or dll (a DLL file)")
    if lib.get("module"):
        mod = str(lib["module"])
        if not all(re.match(r"^[A-Za-z][A-Za-z0-9_]*$", part) for part in mod.split(".")) or mod.split(".")[0] in LIB_DENY:
            p.error(where, "library.module %r is not a maker's module" % mod)
    if lib.get("dll") and not re.match(r"^[A-Za-z0-9_.+-]+\.(dll|so|dylib)$", str(lib["dll"]), re.I):
        p.error(where, "library.dll must be a file name such as attoDRYLib.dll")


def check_instrument(iid: str, data: Dict[str, Any], c: Collection) -> None:
    folder = rel(c.paths[iid])
    p, where = c.p, folder + "/instrument.yaml"
    for key in data:
        if key not in INSTRUMENT_KEYS:
            p.error(where, "unknown key %r (known: %s)" % (key, ", ".join(INSTRUMENT_KEYS)))
    if data.get("schema") != 1:
        p.error(where, "schema: 1 is required")
    if data.get("id") != iid or not ID.match(iid):
        p.error(where, "id must be maker/model in lowercase letters, digits, '-' and '.', such as srs/sr830")
    elif data.get("kind") in c.kind_category and folder != c.folder_for(iid, data["kind"]):
        p.error(where, "move it to %s/ (its kind's category, its kind, then maker-model)"
                % c.folder_for(iid, data["kind"]))
    for key in ("maker", "model", "kind", "control"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            p.error(where, "%s is required (quote a numeric model name)" % key)
    if data.get("kind") not in c.kind_category:
        p.error(where, "kind %r is not in collection.yaml" % data.get("kind"))
    for cat in data.get("categories") or []:
        if cat not in c.meta["categories"]:
            p.error(where, "category %r is not in collection.yaml" % cat)
    if data.get("covers") is not None and not strings(data["covers"]):
        p.error(where, "covers is a list of model names")
    interfaces = data.get("interfaces")
    if not strings(interfaces) or any(i not in c.meta["interfaces"] for i in interfaces):
        p.error(where, "interfaces must be a list from: %s" % ", ".join(c.meta["interfaces"]))
    if data.get("control") not in c.meta["controls"]:
        p.error(where, "control must be one of %s" % ", ".join(c.meta["controls"]))
    for i, m in enumerate(data.get("manuals") or []):
        at = "%s: manuals[%d]" % (where, i)
        if not isinstance(m, dict) or not m.get("title") or not https(m.get("url")):
            p.errors.append(at + ": needs title and an https url")
            continue
        if m.get("access", "public") not in ACCESS:
            p.errors.append(at + ": access must be one of " + ", ".join(ACCESS))
        if m.get("sha256") is not None and not SHA256.match(str(m["sha256"])):
            p.errors.append(at + ": sha256 must be 64 lowercase hex digits")
    for key in ("links", "examples", "software"):
        for i, item in enumerate(data.get(key) or []):
            at = "%s: %s[%d]" % (where, key, i)
            if not isinstance(item, dict) or not (item.get("title") or item.get("name")) or not https(item.get("url")):
                p.errors.append(at + ": needs a title (or name) and an https url")
            elif key == "software" and item.get("kind") not in SOFTWARE_KINDS:
                p.errors.append(at + ": kind must be one of " + ", ".join(SOFTWARE_KINDS))
    if data.get("notes") is not None and not strings(data["notes"]):
        p.error(where, "notes is a list of sentences")
    card = c.cards.get(iid)
    if data.get("card") is not None and data["card"] != "card.yaml":
        p.error(where, "card: card.yaml (the file next to this one) is the only value")
    if (data.get("card") == "card.yaml") != (card is not None):
        p.error(where, "card: card.yaml must be said exactly when the folder has a card.yaml")
    if card is not None:
        cwhere = folder + "/card.yaml"
        check_card(cwhere, card, p)
        if card.get("id") != iid:
            p.error(cwhere, "id must be %r, the id in the instrument.yaml next to it" % iid)
        if card.get("kind") != data.get("kind"):
            p.error(where, "kind %r differs from the card's %r" % (data.get("kind"), card.get("kind")))
        if data.get("identify"):
            p.error(where, "identify lives in the card when there is one")
        urls = [m.get("url") for m in data.get("manuals") or [] if isinstance(m, dict)]
        if card.get("manual_url") and card["manual_url"] not in urls:
            p.error(where, "list the card's manual_url under manuals")
    else:
        check_identify(where, data.get("identify") or {}, p)
        if data.get("verified"):
            p.error(where, "verified reports belong to instruments with a card")
    for i, v in enumerate(data.get("verified") or []):
        at = "%s: verified[%d]" % (where, i)
        if not isinstance(v, dict) or not v.get("lab") or not v.get("by") or not DATE.match(str(v.get("date", ""))):
            p.errors.append(at + ": needs lab, by and date (YYYY-MM-DD)")
    if card is not None and card.get("status") == "lab-verified" and not data.get("verified"):
        p.warn(where, "the card is lab-verified: add who checked it under verified")


def check_lab(name: str, data: Dict[str, Any], c: Collection) -> None:
    """A lab config, as Kelvin's Set up would accept it (limits nest inside the card's, guards read readings)."""
    p, where = c.p, "labs/%s.yaml" % name
    if not isinstance(data.get("lab"), str) or not data["lab"].strip():
        p.error(where, "lab: the lab's name is required")
    instruments = data.get("instruments")
    if not isinstance(instruments, dict) or not instruments:
        p.error(where, "instruments: at least one is required")
        return
    for iname, d in instruments.items():
        at = "%s: instruments.%s" % (where, iname)
        if not str(iname).isidentifier():
            p.errors.append(at + ": names are simple identifiers")
        if not isinstance(d, dict):
            p.errors.append(at + ": must be a mapping")
            continue
        for key in d:
            if key not in LAB_INSTRUMENT_KEYS:
                p.errors.append(at + ": unknown key %r" % key)
        card_id = d.get("card")
        if card_id not in c.cards:
            p.errors.append(at + ": card %r is not in the collection" % card_id)
            continue
        params = c.params(card_id)
        if d.get("trust", "ask") not in ("ask", "envelope"):
            p.errors.append(at + ": trust must be ask or envelope")
        for param, lim in (d.get("limits") or {}).items():
            spec = params.get(param) or {}
            vendor = spec.get("limits")
            if spec.get("type", "float") not in ("float", "int"):
                p.errors.append(at + ".limits.%s: not a numeric parameter of %s" % (param, card_id))
            elif not (isinstance(lim, list) and len(lim) == 2 and all(is_number(x) for x in lim) and lim[0] < lim[1]):
                p.errors.append(at + ".limits.%s: must be [low, high]" % param)
            elif vendor and (lim[0] < vendor[0] or lim[1] > vendor[1]):
                p.errors.append(at + ".limits.%s: %s exceeds the card's limits %s" % (param, lim, vendor))
            elif is_number(spec.get("safe")) and not lim[0] <= spec["safe"] <= lim[1]:
                p.errors.append(at + ".limits.%s: %s leaves out the safe value %s, so Kelvin's preflight would refuse "
                                     "every run" % (param, lim, spec["safe"]))
        for param, rate in (d.get("rates") or {}).items():
            spec = params.get(param) or {}
            if spec.get("ramp") != "gate":
                p.errors.append(at + ".rates.%s: only gate-ramped parameters have rates" % param)
            elif not is_number(rate) or rate <= 0 or rate > spec.get("max_rate", float("inf")):
                p.errors.append(at + ".rates.%s: must be > 0 and at most the card's max_rate" % param)
        for param, guards in (d.get("guards") or {}).items():
            if (params.get(param) or {}).get("kind") != "drive":
                p.errors.append(at + ".guards.%s: guards belong to drives" % param)
            for g in guards if isinstance(guards, list) else [guards]:
                key = str(g.get("read", "")) if isinstance(g, dict) else ""
                key = key if "." in key else "%s.%s" % (iname, key)
                if not isinstance(g, dict) or "max_abs" not in g or not lab_readable(key, instruments, c):
                    p.errors.append(at + ".guards.%s: a guard needs read (a reading in this lab) and max_abs" % param)
        auto = d.get("auto")
        if isinstance(auto, dict):
            for param, rule in auto.items():
                if (params.get(param) or {}).get("kind") != "drive":
                    p.errors.append(at + ".auto.%s: auto rules belong to drives" % param)
        elif auto not in (None, "never"):
            p.errors.append(at + ".auto: never, or a mapping of drive: never | [low, high]")
        card_vars = c.cards[card_id].get("vars") or {}
        for var, value in (d.get("vars") or {}).items():
            if var not in card_vars:
                p.errors.append(at + ".vars.%s: %s has no such variable" % (var, card_id))
            elif not VAR_VALUE.match(str(value)):
                p.errors.append(at + ".vars.%s: letters, digits and . _ + - only" % var)
        for key in d.get("connection") or {}:
            if key not in CONNECTION:
                p.errors.append(at + ".connection.%s: not a setting Kelvin knows" % key)
    for i, lock in enumerate(data.get("interlocks") or []):
        if not lab_drive(str(lock.get("drive")), instruments, c) or not lab_condition(lock.get("require"), instruments, c):
            p.error(where, "interlocks[%d]: drive must be a drive and require a condition on a reading" % i)
    for key, action in (data.get("safe_actions") or {}).items():
        if not lab_drive(key, instruments, c) or action not in ("hold", "safe"):
            p.error(where, "safe_actions.%s: a drive, with hold or safe" % key)
    for i, w in enumerate(data.get("watch") or []):
        if not isinstance(w, dict) or not lab_readable(str(w.get("read")), instruments, c) \
                or (w.get("above") is None and w.get("below") is None):
            p.error(where, "watch[%d]: needs read (a reading in this lab) and above or below" % i)
            continue
        for key, value in (w.get("then") or {}).items():
            spec = lab_spec(key, instruments, c) or {}
            if spec.get("kind") != "drive" or not same_value(value, spec.get("safe")):
                p.error(where, "watch[%d].then.%s: a watch may only send a drive to its safe value" % (i, key))


def lab_spec(key: str, instruments: Dict[str, Any], c: Collection) -> Optional[Dict[str, Any]]:
    instr, _, param = str(key).partition(".")
    d = instruments.get(instr)
    if not isinstance(d, dict):
        return None
    return c.params(str(d.get("card"))).get(param)


def lab_readable(key: str, instruments: Dict[str, Any], c: Collection) -> bool:
    spec = lab_spec(key, instruments, c)
    return isinstance(spec, dict) and bool(spec.get("get"))


def lab_drive(key: str, instruments: Dict[str, Any], c: Collection) -> bool:
    spec = lab_spec(key, instruments, c)
    return isinstance(spec, dict) and spec.get("kind") == "drive"


def lab_condition(text: Any, instruments: Dict[str, Any], c: Collection) -> bool:
    m = CONDITION.match(str(text or ""))
    return bool(m) and lab_readable("%s.%s" % (m.group(1), m.group(2)), instruments, c)


def same_value(a: Any, b: Any) -> bool:
    words = {"on": True, "true": True, "1": True, "off": False, "false": False, "0": False}
    a2, b2 = words.get(str(a).lower(), a), words.get(str(b).lower(), b)
    if is_number(a2) and is_number(b2):
        return abs(float(a2) - float(b2)) < 1e-12
    return str(a2).lower() == str(b2).lower()


def check_plan(where: str, plan: Any, instruments: Dict[str, Any], c: Collection) -> None:
    """A plan in Kelvin's format, against the lab config it is written for."""
    p = c.p
    if not isinstance(plan, dict):
        p.error(where, "a plan is a mapping")
        return
    for key in plan:
        if key not in PLAN_KEYS:
            p.error(where, "unknown plan key %r (Kelvin knows %s)" % (key, ", ".join(sorted(PLAN_KEYS))))
    if not plan.get("plan"):
        p.error(where, "plan: a name is required")

    def known(key: Any, settable: bool = False) -> None:
        spec = lab_spec(str(key), instruments, c)
        if spec is None:
            p.error(where, "%s is not an instrument.parameter in the lab config" % key)
        elif settable and not spec.get("set"):
            p.error(where, "%s cannot be set" % key)
        elif not settable and not spec.get("get"):
            p.error(where, "%s cannot be read" % key)

    for section in ("setup", "after", "on_abort"):
        for key in (plan.get(section) or {}):
            known(key, settable=True)
    for key, axis in (plan.get("sweep") or {}).items():
        known(key, settable=True)
        if not isinstance(axis, dict):
            p.error(where, "sweep.%s: {from, to, step | points} or {values: [...]}" % key)
            continue
        if "values" not in axis and not ("from" in axis and "to" in axis and ("step" in axis or "points" in axis)):
            p.error(where, "sweep.%s: {from, to, step | points} or {values: [...]}" % key)
        stab = axis.get("stabilize")
        if stab is not None and not (isinstance(stab, dict) and lab_readable(str(stab.get("read")), instruments, c)
                                     and is_number(stab.get("within")) and is_number(stab.get("for"))):
            p.error(where, "sweep.%s.stabilize: {read, within, for} with a reading in this lab" % key)
    measure = plan.get("measure")
    if not strings(measure):
        p.error(where, "measure: a list of readings is required")
    for key in measure or []:
        known(key)
    for cond in plan.get("preconditions") or []:
        if not lab_condition(cond, instruments, c):
            p.error(where, "precondition %r: instrument.reading <op> value, with a reading in this lab" % cond)
    for name in plan.get("requires") or []:
        if name not in instruments:
            p.error(where, "requires %r, which is not in the lab config" % name)


def check_experiment(eid: str, data: Dict[str, Any], c: Collection) -> None:
    p, where = c.p, "experiments/%s.yaml" % eid
    for key in data:
        if key not in EXPERIMENT_KEYS:
            p.error(where, "unknown key %r (known: %s)" % (key, ", ".join(EXPERIMENT_KEYS)))
    if data.get("schema") != 1:
        p.error(where, "schema: 1 is required")
    area = eid.split("/")[0]
    if data.get("id") != eid:
        p.error(where, "id must be %r (area/file name)" % eid)
    if data.get("area") != area or area not in c.meta["areas"]:
        p.error(where, "area must be %r, the folder it is in, and listed in collection.yaml" % area)
    for key in ("title", "summary"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            p.error(where, "%s is required" % key)
    roles = data.get("roles")
    if not isinstance(roles, dict) or not roles:
        p.error(where, "roles: which instruments the experiment needs")
        roles = {}
    for role, r in roles.items():
        at = "%s: roles.%s" % (where, role)
        if not isinstance(r, dict):
            p.errors.append(at + ": must be a mapping {kind, does, suggested}")
            continue
        kinds = r.get("kind") if isinstance(r.get("kind"), list) else [r.get("kind")]
        for k in kinds:
            if k not in c.kind_category:
                p.errors.append(at + ": kind %r is not in collection.yaml" % k)
        for iid in r.get("suggested") or []:
            if iid not in c.instruments:
                p.errors.append(at + ": suggested %r is not in the collection" % iid)
            elif c.instruments[iid].get("kind") not in kinds:
                p.warn(where, "roles.%s suggests %s, a %s" % (role, iid, c.instruments[iid].get("kind")))
    for k in data.get("needs_cards") or []:
        if k not in c.kind_category:
            p.error(where, "needs_cards: %r is not a kind in collection.yaml" % k)
    for key in ("setup", "procedure", "analysis", "pitfalls", "safety"):
        if data.get(key) is not None and not strings(data[key]):
            p.error(where, "%s is a list of sentences" % key)
    for i, ref in enumerate(data.get("references") or []):
        if not isinstance(ref, dict) or not ref.get("title") or (ref.get("url") is not None and not https(ref["url"])) \
                or (ref.get("doi") is not None and not re.match(r"^10\.\d{4,9}/\S+$", str(ref["doi"]))):
            p.error(where, "references[%d]: needs a title, and a doi (10.xxxx/...) or https url if given" % i)
    lab = data.get("lab")
    instruments: Dict[str, Any] = {}
    if lab is not None:
        m = re.match(r"^labs/([a-z0-9-]+)\.yaml$", str(lab))
        if not m or m.group(1) not in c.labs:
            p.error(where, "lab %r is not one of labs/*.yaml" % lab)
        else:
            instruments = c.labs[m.group(1)].get("instruments") or {}
    plans = data.get("plans") or []
    if plans and lab is None:
        p.error(where, "plans are written for a lab config: name it under lab")
    for i, item in enumerate(plans):
        at = "%s: plans[%d]" % (where, i)
        if not isinstance(item, dict) or not item.get("title") or "plan" not in item:
            p.errors.append(at + ": needs title and plan")
            continue
        if instruments:
            check_plan(at, item["plan"], instruments, c)


def kelvin_crosscheck(c: Collection) -> Optional[str]:
    """When Kelvin itself is installed in this Python (from source), its own parsers read every card,
    lab config and plan too. Returns what was checked, or None when Kelvin isn't here."""
    try:
        from labharness.cards import CardRegistry, load_card
        from labharness.labconfig import load_lab_config
        from labharness.plans import load_plan
    except ImportError:
        return None
    registry = CardRegistry()
    for iid in c.cards:
        try:
            registry.add(load_card(c.paths[iid] / "card.yaml"))
        except Exception as e:
            c.p.error(rel(c.paths[iid] / "card.yaml"), "Kelvin: %s" % e)
    for name in c.labs:
        try:
            load_lab_config(ROOT / "labs" / (name + ".yaml"), registry)
        except Exception as e:
            c.p.error("labs/%s.yaml" % name, "Kelvin: %s" % e)
    for eid, data in c.experiments.items():
        for i, item in enumerate(data.get("plans") or []):
            try:
                load_plan(item.get("plan"))
            except Exception as e:
                c.p.error("experiments/%s.yaml: plans[%d]" % (eid, i), "Kelvin: %s" % e)
    return "Kelvin's own card, lab and plan parsers"


def cmd_validate(args: argparse.Namespace) -> int:
    p = Problems()
    c = Collection(p)
    for iid, data in c.instruments.items():
        check_instrument(iid, data, c)
    for name, data in c.labs.items():
        check_lab(name, data, c)
    for eid, data in c.experiments.items():
        check_experiment(eid, data, c)
    also = None if args.no_kelvin else kelvin_crosscheck(c)
    for w in p.warnings if args.warnings else []:
        print("warning: " + w)
    for e in p.errors:
        print("error: " + e)
    cards = len(c.cards)
    print("%d instruments (%d with a card), %d experiments, %d lab configs: %s%s" % (
        len(c.instruments), cards, len(c.experiments), len(c.labs),
        "%d problems" % len(p.errors) if p.errors else "all good",
        "" if not p.warnings or args.warnings else " (%d warnings, --warnings shows them)" % len(p.warnings)))
    if also:
        print("Also checked with " + also + ".")
    return 1 if p.errors else 0


# ---------------------------------------------------------------- index.json and CATALOG.md

def build_index(c: Collection) -> Dict[str, Any]:
    used_by: Dict[str, List[str]] = {}
    lab_users: Dict[str, List[str]] = {}

    def use(iid: Any, eid: str) -> None:
        users = used_by.setdefault(str(iid), [])
        if eid not in users:
            users.append(eid)

    for eid, e in c.experiments.items():
        for r in (e.get("roles") or {}).values():
            for iid in (r or {}).get("suggested") or []:
                use(iid, eid)
        if e.get("lab"):
            lab = Path(e["lab"]).stem
            lab_users.setdefault(lab, []).append(eid)
            instruments = (c.labs.get(lab) or {}).get("instruments") or {}
            for item in e.get("plans") or []:
                for name in plan_instruments(item.get("plan") or {}):
                    if isinstance(instruments.get(name), dict):
                        use(instruments[name].get("card"), eid)

    instruments = []
    for iid, d in c.instruments.items():
        card = c.cards.get(iid)
        identify = (card or d).get("identify") or {}
        path = c.paths[iid]
        instruments.append({
            "id": iid, "maker": d["maker"], "model": d["model"], "name": display_name(d),
            "covers": d.get("covers") or [], "kind": d["kind"], "category": c.category(iid),
            "categories": [c.category(iid)] + [x for x in d.get("categories") or [] if x != c.category(iid)],
            "interfaces": d.get("interfaces") or [], "control": d["control"],
            "identify": {k: identify[k] for k in ("idn", "example", "query") if identify.get(k)} or None,
            "usb": [str(u).lower() for u in identify.get("usb") or []],
            "card": None if card is None else {
                "path": rel(path / "card.yaml"), "sha256": sha256(path / "card.yaml"), "status": card["status"],
                "kelvin_file": kelvin_file(iid), "model": card["model"]},
            "manuals": d.get("manuals") or [], "links": d.get("links") or [], "software": d.get("software") or [],
            "examples": d.get("examples") or [], "notes": d.get("notes") or [],
            "verified": d.get("verified") or [], "experiments": sorted(used_by.get(iid, [])),
            "path": rel(path),
        })
    experiments = []
    for eid, e in c.experiments.items():
        path = ROOT / "experiments" / (eid + ".yaml")
        roles = {}
        for role, r in (e.get("roles") or {}).items():
            kinds = r.get("kind") if isinstance(r.get("kind"), list) else [r.get("kind")]
            roles[role] = {"kind": kinds, "does": r.get("does", ""), "optional": bool(r.get("optional")),
                           "suggested": r.get("suggested") or []}
        experiments.append({
            "id": eid, "area": e["area"], "title": e["title"], "summary": e["summary"].strip(), "roles": roles,
            "lab": e.get("lab"), "plans": [pl["title"] for pl in e.get("plans") or []],
            "needs_cards": e.get("needs_cards") or [], "path": rel(path), "sha256": sha256(path)})
    labs = []
    for name, lab in c.labs.items():
        path = ROOT / "labs" / (name + ".yaml")
        labs.append({"id": name, "name": lab["lab"], "path": rel(path), "sha256": sha256(path),
                     "instruments": {k: v.get("card") for k, v in (lab.get("instruments") or {}).items()},
                     "experiments": sorted(lab_users.get(name, []))})
    categories = []
    for cat, m in c.meta["categories"].items():
        members = [i for i in instruments if cat in i["categories"]]
        categories.append({"id": cat, "title": m["title"], "description": m["description"],
                           "kinds": [{"id": k, "title": t, "count": sum(1 for i in instruments if i["kind"] == k)}
                                     for k, t in m["kinds"].items()],
                           "count": len(members)})
    areas = [{"id": a, "title": m["title"], "description": m["description"],
              "count": sum(1 for e in experiments if e["area"] == a)} for a, m in c.meta["areas"].items()]
    return {
        "schema": 1, "name": c.meta["name"], "repository": c.meta["repository"],
        "counts": {"instruments": len(instruments), "cards": sum(1 for i in instruments if i["card"]),
                   "experiments": len(experiments), "labs": len(labs)},
        "categories": categories, "areas": areas, "kelvin": c.meta.get("kelvin") or {},
        "instruments": instruments, "experiments": experiments, "labs": labs,
    }


def plan_instruments(plan: Dict[str, Any]) -> Set[str]:
    """The lab instruments a plan sets, sweeps or reads."""
    keys: List[str] = []
    for section in ("setup", "sweep", "after", "on_abort"):
        keys += [str(k) for k in plan.get(section) or {}]
    keys += [str(k) for k in plan.get("measure") or []]
    keys += [str((axis or {}).get("stabilize", {}).get("read", "")) for axis in (plan.get("sweep") or {}).values()
             if isinstance(axis, dict) and isinstance(axis.get("stabilize"), dict)]
    for cond in plan.get("preconditions") or []:
        m = CONDITION.match(str(cond))
        if m:
            keys.append(m.group(1))
    return {k.split(".")[0] for k in keys if k} | {str(n) for n in plan.get("requires") or []}


INTERFACE_NAMES = {"gpib": "GPIB", "usb-tmc": "USB-TMC", "usb": "USB", "lan": "LAN", "rs-232": "RS-232",
                   "rs-485": "RS-485", "pcie": "PCIe", "pxie": "PXIe", "analog": "analog", "web-api": "web API"}


def display_name(d: Dict[str, Any]) -> str:
    return d.get("name") or "%s %s" % (d["maker"], d["model"])


def anchor(title: str) -> str:
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")


def md(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def build_catalog(index: Dict[str, Any]) -> str:
    ins = index["instruments"]
    exps = {e["id"]: e for e in index["experiments"]}
    n = index["counts"]
    out = ["# Catalog", "",
           "<!-- Written by `python tools/kic.py index` from the files in this repository; edit those, not this. -->",
           "",
           "%d instruments, %d of them with a Kelvin card; %d experiments; %d lab configs." % (
               n["instruments"], n["cards"], n["experiments"], n["labs"]),
           "",
           "**Card status.** *community*: written from the maker's manual, not yet checked on hardware. "
           "*lab-verified*: checked on hardware by a lab (see the instrument's `verified` list). "
           "*draft*: Kelvin keeps its outputs simulated until someone checks it. "
           "*no card*: Kelvin writes one from the manual when it finds the instrument.",
           "",
           "- [Instruments by category](#instruments-by-category)",
           "- [Experiments](#experiments)",
           "- [Lab configs](#lab-configs)",
           "- [Wanted cards](#wanted-cards)",
           "- [Makers](#makers)",
           "", "## Instruments by category", ""]
    for cat in index["categories"]:
        out.append("- [%s](#%s) (%d)" % (cat["title"], anchor(cat["title"]), cat["count"]))
    for cat in index["categories"]:
        members = [i for i in ins if cat["id"] in i["categories"]]
        out += ["", "### " + cat["title"], "", cat["description"], "",
                "| Instrument | Kind | Card | Talks over | Manual | Used in |", "|---|---|---|---|---|---|"]
        order = {k["id"]: n for n, k in enumerate(cat["kinds"])}
        for i in sorted(members, key=lambda i: (order.get(i["kind"], 99), i["maker"].lower(), i["model"].lower())):
            used = [exps[e] for e in i["experiments"] if e in exps]
            used_md = ", ".join("[%s](%s)" % (md(e["title"]), e["path"]) for e in used[:3])
            if len(used) > 3:
                used_md += " +%d" % (len(used) - 3)
            out.append("| [%s](%s/instrument.yaml) | %s | %s | %s | %s | %s |" % (
                md(i["name"]), i["path"], i["kind"],
                "[%s](%s)" % (i["card"]["status"], i["card"]["path"]) if i["card"] else "no card",
                md(", ".join(INTERFACE_NAMES.get(x, x) for x in i["interfaces"])),
                manual_cell(i), used_md or ""))
    out += ["", "## Experiments", ""]
    for area in index["areas"]:
        members = [e for e in index["experiments"] if e["area"] == area["id"]]
        if not members:
            continue
        out += ["### " + area["title"], "", area["description"], "",
                "| Experiment | Instruments | Lab config | Plans |", "|---|---|---|---|"]
        for e in members:
            roles = ", ".join("%s%s" % (r, " (optional)" if v["optional"] else "") for r, v in e["roles"].items())
            out.append("| [%s](%s) | %s | %s | %s |" % (
                md(e["title"]), e["path"], md(roles),
                "[%s](%s)" % (Path(e["lab"]).stem, e["lab"]) if e["lab"] else "",
                len(e["plans"]) or ("needs a card: " + ", ".join(e["needs_cards"]) if e["needs_cards"] else "")))
        out.append("")
    out += ["## Lab configs", "",
            "Copy one to `~/Kelvin/lab.yaml` (or open it in **Lab → Set up…**), then give each instrument its "
            "address. Without addresses every instrument is simulated.", "",
            "| Lab config | Instruments | Used by |", "|---|---|---|"]
    for lab in index["labs"]:
        out.append("| [%s](%s) | %s | %s |" % (
            md(lab["name"]), lab["path"],
            ", ".join("%s (%s)" % (k, v) for k, v in lab["instruments"].items()),
            ", ".join("[%s](%s)" % (md(exps[e]["title"]), exps[e]["path"]) for e in lab["experiments"] if e in exps)))
    out += ["", "## Wanted cards", "",
            "Experiments that need an instrument no card covers yet, and the catalogued models that would fill "
            "the gap. Kelvin can draft these cards from the manuals listed here.", ""]
    for e in index["experiments"]:
        for kind in e["needs_cards"]:
            options = [i for i in ins if i["kind"] == kind and not i["card"]]
            out.append("- **%s** for [%s](%s): %s" % (kind, md(e["title"]), e["path"], ", ".join(
                "[%s](%s/instrument.yaml)" % (md(i["name"]), i["path"]) for i in options) or "none catalogued yet"))
    out += ["", "## Makers", ""]
    makers: Dict[str, List[Dict[str, Any]]] = {}
    for i in ins:
        makers.setdefault(i["maker"], []).append(i)
    for maker in sorted(makers, key=str.lower):
        out.append("- **%s:** %s" % (md(maker), ", ".join(
            "[%s](%s/instrument.yaml)" % (md(i["model"]), i["path"]) for i in makers[maker])))
    return "\n".join(out) + "\n"


def manual_cell(i: Dict[str, Any]) -> str:
    for m in i["manuals"]:
        if m.get("access", "public") == "public":
            return "[manual](%s)" % m["url"]
    for m in i["manuals"]:
        return "[%s](%s)" % (m.get("access"), m["url"])
    for link in i["links"]:
        return "[support](%s)" % link["url"]
    return ""


def build_shelf(index: Dict[str, Any]) -> Dict[str, str]:
    """A README for instruments/ and for each category folder in it, so the folders read well on GitHub."""
    ins = index["instruments"]
    note = "<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->"
    top = ["# Instruments", "", note, "",
           "Sorted by category, then kind: `<category>/<kind>/<maker>-<model>/`. Each folder has the instrument's "
           "`instrument.yaml` (maker, interfaces, manuals, drivers) and its Kelvin `card.yaml` when there is one. "
           "[CATALOG.md](../CATALOG.md) lists them all, with the experiments that use them.", "",
           "| Category | Instruments | With a card |", "|---|---|---|"]
    pages: Dict[str, str] = {}
    for cat in index["categories"]:
        here = [i for i in ins if i["category"] == cat["id"]]
        top.append("| [%s](%s) | %d | %d |" % (cat["title"], cat["id"], len(here), sum(1 for i in here if i["card"])))
        out = ["# " + cat["title"], "", note, "", cat["description"], ""]
        for kind in cat["kinds"]:
            members = sorted((i for i in here if i["kind"] == kind["id"]),
                             key=lambda i: (i["maker"].lower(), i["model"].lower()))
            if not members:
                continue
            out += ["## %s" % kind["title"], "", "| Instrument | Card | Talks over | Manual |", "|---|---|---|---|"]
            for i in members:
                folder = i["path"].split("/", 2)[2]
                out.append("| [%s](%s) | %s | %s | %s |" % (
                    md(i["name"]), folder,
                    "[%s](%s/card.yaml)" % (i["card"]["status"], folder) if i["card"] else "no card",
                    md(", ".join(INTERFACE_NAMES.get(x, x) for x in i["interfaces"])), manual_cell(i)))
            out.append("")
        also = [i for i in ins if cat["id"] in i["categories"] and i["category"] != cat["id"]]
        if also:
            out += ["## Also used here", ""] + ["- [%s](../%s), in %s" % (md(i["name"]), i["path"].split("/", 1)[1],
                                                                        i["category"]) for i in also] + [""]
        pages["instruments/%s/README.md" % cat["id"]] = "\n".join(out).rstrip("\n") + "\n"
    pages["instruments/README.md"] = "\n".join(top) + "\n"
    return pages


def cmd_index(args: argparse.Namespace) -> int:
    p = Problems()
    c = Collection(p)
    if p.errors:
        print("\n".join("error: " + e for e in p.errors))
        return 1
    index = build_index(c)
    files = {"index.json": json.dumps(index, indent=1, ensure_ascii=False) + "\n", "CATALOG.md": build_catalog(index)}
    files.update(build_shelf(index))
    if args.check:
        stale = [name for name, new in files.items()
                 if not (ROOT / name).exists() or (ROOT / name).read_text(encoding="utf-8") != new]
        if stale:
            print("%s out of date: run python tools/kic.py index" % ", ".join(stale))
            return 1
        print("index.json, CATALOG.md and the instruments/ READMEs are up to date")
        return 0
    for name, text in files.items():
        (ROOT / name).write_text(text, encoding="utf-8", newline="\n")
    print("Wrote index.json, CATALOG.md and the instruments/ READMEs: %(instruments)d instruments (%(cards)d cards), "
          "%(experiments)d experiments, %(labs)d lab configs" % index["counts"])
    return 0


def read_index() -> Dict[str, Any]:
    if not INDEX.exists():
        sys.exit("No index.json: run python tools/kic.py index first")
    return json.loads(INDEX.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- find

def cmd_find(args: argparse.Namespace) -> int:
    index = read_index()
    found = 0
    if args.idn:
        for i in index["instruments"]:
            idn = (i.get("identify") or {}).get("idn")
            if idn and re.search(idn, args.idn, re.I):
                found += 1
                print("%-28s %s (%s)" % (i["id"], i["name"], "card: " + i["card"]["status"] if i["card"] else "no card"))
        if not found:
            print("No instrument in the collection answers like that. Kelvin can write a card from its manual.")
        return 0 if found else 1
    words = [w.lower() for w in args.text]
    for i in index["instruments"]:
        hay = " ".join([i["id"], i["maker"], i["model"], i["name"], i["kind"], " ".join(i["categories"]),
                        " ".join(i["covers"])]).lower()
        if all(w in hay for w in words):
            found += 1
            manual = next((m["url"] for m in i["manuals"] if m.get("access", "public") == "public"), "")
            print("%-28s %-48s %-20s %-12s %s" % (i["id"], i["name"][:48], i["kind"],
                                                   i["card"]["status"] if i["card"] else "no card", manual))
    for e in index["experiments"]:
        if all(w in " ".join([e["id"], e["title"], e["summary"]]).lower() for w in words):
            found += 1
            print("%-28s %s" % ("experiment " + e["id"], e["title"]))
    for lab in index["labs"]:
        if all(w in " ".join([lab["id"], lab["name"]] + list(lab["instruments"].values())).lower() for w in words):
            found += 1
            print("%-28s %s" % ("lab " + lab["id"], lab["name"]))
    if not found:
        print("Nothing matches %s" % " ".join(args.text))
    return 0 if found else 1


# ---------------------------------------------------------------- install

def kelvin_bundled(index: Dict[str, Any], app: Optional[str]) -> Tuple[Set[str], str]:
    """The card ids this computer's Kelvin brings itself, read from the installed app when it can be found."""
    places = [Path(app)] if app else []
    if os.name == "nt" and os.environ.get("LOCALAPPDATA"):
        places.append(Path(os.environ["LOCALAPPDATA"]) / "Programs" / "Kelvin")
    if sys.platform == "darwin":
        places.append(Path("/Applications/Kelvin.app"))
    try:
        import importlib.util
        spec = importlib.util.find_spec("labharness")
        if spec and spec.origin:
            places.append(Path(spec.origin).parent)
    except (ImportError, ValueError):
        pass
    for place in places:
        if not place.is_dir():
            continue
        for cards in place.rglob("cards"):
            if cards.parent.name == "data" and cards.parent.parent.name == "labharness":
                ids = set()
                for f in cards.rglob("*.yaml"):
                    m = re.search(r"(?m)^id:\s*['\"]?([^\s'\"]+)", f.read_text(encoding="utf-8", errors="ignore"))
                    if m:
                        ids.add(m.group(1))
                if ids:
                    return ids, "the Kelvin installed in %s" % place
    bundled = (index.get("kelvin") or {}).get("bundled") or {}
    return set(bundled.get("cards") or []), "collection.yaml (Kelvin %s)" % bundled.get("version", "?")


def cmd_install(args: argparse.Namespace) -> int:
    index = read_index()
    home = Path(args.kelvin_home).expanduser() if args.kelvin_home else Path.home() / "Kelvin"
    if not home.is_dir():
        sys.exit("No Kelvin folder at %s. Start Kelvin once on this computer, or give --kelvin-home." % home)
    cards_dir = home / "cards"
    bundled, source = kelvin_bundled(index, args.kelvin_app)
    manifest_path = cards_dir / ".kelvin-instruments.json"   # what this tool put there, so it can update it later
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        manifest = {}
    installed: Dict[str, str] = dict(manifest.get("installed") or {})
    chosen = [i for i in index["instruments"] if i["card"]]
    if args.ids:
        unknown = sorted(set(args.ids) - {i["id"] for i in chosen})
        if unknown:
            sys.exit("No card in the collection for %s" % ", ".join(unknown))
        chosen = [i for i in chosen if i["id"] in args.ids]
    if args.category:
        chosen = [i for i in chosen if args.category in i["categories"]]
    report: Dict[str, List[str]] = {"new": [], "updated": [], "same": [], "kept": [], "kelvin": []}
    for i in chosen:
        if i["id"] in bundled:
            report["kelvin"].append(i["id"])
            continue
        src = ROOT / i["card"]["path"]
        if sha256(src) != i["card"]["sha256"]:
            sys.exit("%s changed since index.json was written: run python tools/kic.py index" % i["card"]["path"])
        dst = cards_dir / i["card"]["kelvin_file"]
        if dst.exists():
            current = sha256(dst)
            if current == i["card"]["sha256"]:
                report["same"].append(i["id"])
                continue
            if installed.get(dst.name) != current:   # edited or reviewed on this computer: theirs stays
                report["kept"].append(i["id"])
                continue
            report["updated"].append(i["id"])
        else:
            report["new"].append(i["id"])
        if not args.dry_run:
            cards_dir.mkdir(parents=True, exist_ok=True)
            tmp = dst.with_suffix(".tmp")
            tmp.write_bytes(src.read_bytes())
            tmp.replace(dst)
            installed[dst.name] = i["card"]["sha256"]
    if not args.dry_run and (report["new"] or report["updated"]):
        manifest_path.write_text(json.dumps({"from": index["repository"], "installed": installed}, indent=1) + "\n",
                                 encoding="utf-8")
    verb = "Would add" if args.dry_run else "Added"
    print("%s %d cards to %s, updated %d, %d already there." % (
        verb, len(report["new"]), cards_dir, len(report["updated"]), len(report["same"])))
    for key, text in (("new", "  new: "), ("updated", "  updated: "),
                      ("kept", "  kept yours (changed on this computer): ")):
        if report[key]:
            print(text + ", ".join(report[key]))
    print("Left out %d that Kelvin brings itself (from %s)." % (len(report["kelvin"]), source))
    if report["new"] or report["updated"]:
        print("Restart Kelvin to use them; they are listed under Lab -> Set up -> Cards.")
    return 0


# ---------------------------------------------------------------- manuals

def fetch(url: str, limit: int = 80 * 1024 * 1024) -> Tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read(limit + 1)
        if len(data) > limit:
            raise ValueError("larger than %d MB" % (limit >> 20))
        return data, r.headers.get("Content-Type", "")


def cmd_manuals(args: argparse.Namespace) -> int:
    index = read_index()
    by_id = {i["id"]: i for i in index["instruments"]}
    ids = list(args.ids)
    if args.lab:
        lab = next((x for x in index["labs"] if x["id"] == Path(args.lab).stem), None)
        if lab is None:
            sys.exit("No lab config %s in labs/" % args.lab)
        ids += [cid for cid in lab["instruments"].values() if cid not in ids]
    if not ids:
        sys.exit("Name instruments (e.g. srs/sr830) or a lab config (--lab ppms-transport)")
    out = Path(args.out)
    failed = 0
    for iid in ids:
        i = by_id.get(iid)
        if i is None:
            print("%s: not in the collection" % iid)
            failed += 1
            continue
        for n, m in enumerate(i["manuals"]):
            if m.get("access", "public") != "public":
                print("%s: %s is %s only, get it from %s" % (iid, m["title"], m["access"], m["url"]))
                continue
            last = urllib.parse.unquote(m["url"].split("?")[0].rstrip("/").rsplit("/", 1)[-1])
            name = re.sub(r"[^\w.-]+", "_", last).strip("_") or "manual"
            target = out / iid / (name if name.lower().endswith(".pdf") else "%s-%d.pdf" % (iid.split("/")[1], n))
            if target.exists() and m.get("sha256") and sha256(target) == m["sha256"]:
                print("%s: %s already here" % (iid, target))
                continue
            try:
                data, ctype = fetch(m["url"])
            except (urllib.error.URLError, OSError, ValueError) as e:
                print("%s: could not fetch %s (%s)" % (iid, m["url"], e))
                failed += 1
                continue
            if not data.startswith(b"%PDF"):
                print("%s: %s is not a PDF (a web page or a sign-in?); open it in a browser" % (iid, m["url"]))
                continue
            digest = hashlib.sha256(data).hexdigest()
            if m.get("sha256") and digest != m["sha256"] and not args.pin:
                print("%s: %s has changed since it was pinned (the maker may have a new edition); "
                      "check it, then run with --pin" % (iid, m["url"]))
                failed += 1
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            print("%s: %s (%d kB)" % (iid, target, len(data) >> 10))
            if args.pin and m.get("sha256") != digest:
                pin(ROOT / i["path"] / "instrument.yaml", m["url"], digest)
    return 1 if failed else 0


def pin(path: Path, url: str, digest: str) -> None:
    """Record a manual's SHA-256 under its url in instrument.yaml, leaving the rest of the file as written."""
    lines = path.read_text(encoding="utf-8").split("\n")
    for n, line in enumerate(lines):
        m = re.match(r"^(\s*)(- )?url: ['\"]?(\S+?)['\"]?\s*$", line)
        if m and m.group(3) == url:
            indent = m.group(1) + ("  " if m.group(2) else "")
            end = n + 1
            while end < len(lines) and lines[end].startswith(indent) and not lines[end].strip().startswith("- "):
                if lines[end].strip().startswith("sha256:"):
                    lines[end] = "%ssha256: %s" % (indent, digest)
                    break
                end += 1
            else:
                lines.insert(n + 1, "%ssha256: %s" % (indent, digest))
            path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
            print("  pinned in %s" % rel(path))
            return
    print("  could not find %s in %s to pin it" % (url, rel(path)))


# ---------------------------------------------------------------- links

def check_url(url: str, want_pdf: bool) -> Tuple[str, str]:
    """('ok' | 'moved' | 'html' | 'blocked' | 'broken', detail). Only 'broken' is certain."""
    for method, headers in (("HEAD", {}), ("GET", {"Range": "bytes=0-2047"})):
        req = urllib.request.Request(url, method=method, headers=dict(headers, **{"User-Agent": UA}))
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                ctype = r.headers.get("Content-Type", "")
                final = r.geturl()
                head = r.read(2048) if method == "GET" else b""
            if want_pdf and "pdf" not in ctype and "octet-stream" not in ctype and not head.startswith(b"%PDF"):
                if method == "HEAD":
                    continue          # some servers answer HEAD loosely: look at the first bytes
                return "html", ctype
            return ("moved", final) if final.rstrip("/") != url.rstrip("/") else ("ok", ctype)
        except urllib.error.HTTPError as e:
            if method == "GET":       # some servers answer HEAD with 404 and GET with the page
                return ("broken" if e.code in (404, 410) else "blocked"), "HTTP %d" % e.code
        except (urllib.error.URLError, OSError) as e:
            if method == "GET":
                reason = str(getattr(e, "reason", e))
                return ("broken" if "getaddrinfo" in reason or "Name or service" in reason else "blocked"), reason
    return "blocked", "no answer"


def cmd_links(args: argparse.Namespace) -> int:
    index = read_index()
    todo = []
    for i in index["instruments"]:
        if args.ids and i["id"] not in args.ids:
            continue
        for m in i["manuals"]:
            todo.append((i["id"], "manual", m["url"], m.get("access", "public") == "public" and
                         m["url"].lower().split("?")[0].endswith(".pdf")))
        if not args.manuals_only:
            for key in ("links", "software", "examples"):
                for item in i[key]:
                    todo.append((i["id"], key, item["url"], False))
    seen: Dict[str, Tuple[str, str]] = {}
    urls = sorted({(u, pdf) for _, _, u, pdf in todo})
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for (u, _), result in zip(urls, pool.map(lambda x: check_url(*x), urls)):
            seen[u] = result
    broken = 0
    counts: Dict[str, int] = {}
    for iid, key, url, _ in todo:
        status, detail = seen[url]
        counts[status] = counts.get(status, 0) + 1
        if status == "broken" and key == "manual":
            broken += 1
        if status != "ok" and (args.verbose or status in ("broken", "html")):
            print("%-8s %-28s %-9s %s  %s" % (status, iid, key, url, detail))
    print("%d links: %s" % (len(todo), ", ".join("%d %s" % (n, s) for s, n in sorted(counts.items()))))
    if counts.get("blocked"):
        print("'blocked' means the site refused an automated check (403, 429, a bot wall); check those in a browser.")
    return 1 if broken else 0


# ---------------------------------------------------------------- probe

def visa_resource(address: str) -> str:
    if address.startswith("serial://"):
        port = address[len("serial://"):]
        m = re.match(r"^COM(\d+)$", port, re.I)
        return "ASRL%s::INSTR" % (m.group(1) if m else port)
    if re.match(r"^(GPIB|TCPIP|USB|ASRL|VXI|PXI)\d*::", address, re.I):
        return address
    sys.exit("probe talks VISA (GPIB, USB, LAN, serial). For %s, use Try it in Kelvin's Lab -> Set up." % address)


def cmd_probe(args: argparse.Namespace) -> int:
    if args.card.endswith(".yaml"):
        path = Path(args.card)
    else:   # a card id: instruments/<category>/<kind>/<maker>-<model>/card.yaml
        hits = sorted((ROOT / "instruments").glob("*/*/%s/card.yaml" % args.card.replace("/", "-")))
        path = hits[0] if hits else ROOT / "instruments" / args.card
    if not path.exists():
        sys.exit("No card %s" % args.card)
    card = load_yaml(path)
    params = card.get("parameters") or {}
    if card.get("library") or any(str(s.get("get", "")).startswith("GET ") for s in params.values()):
        sys.exit("%s talks through its maker's library or web API; use Try it in Kelvin's Lab -> Set up." % card["id"])
    if (card.get("connection") or {}).get("write_only"):
        sys.exit("%s only listens; it has nothing to read back. Check it from its front panel." % card["id"])
    values = {k: str(v.get("default") if isinstance(v, dict) else v) for k, v in (card.get("vars") or {}).items()}
    for item in args.var or []:
        k, _, v = item.partition("=")
        if k not in values or not VAR_VALUE.match(v):
            sys.exit("--var %s: the card's variables are %s" % (item, ", ".join(values) or "none"))
        values[k] = v
    try:
        import pyvisa
        from pyvisa import constants
    except ImportError:
        sys.exit("probe needs PyVISA: pip install pyvisa pyvisa-py")
    conn = card.get("connection") or {}
    rm = pyvisa.ResourceManager(args.backend) if args.backend else pyvisa.ResourceManager()
    inst = rm.open_resource(visa_resource(args.address))
    inst.timeout = conn.get("timeout_ms", 3000)
    inst.read_termination = conn.get("read_termination", "\n")
    inst.write_termination = conn.get("write_termination", "\n")
    if args.address.startswith("serial://") or args.address.upper().startswith("ASRL"):
        inst.baud_rate = conn.get("baud_rate", 9600)
        inst.data_bits = conn.get("data_bits", 8)
        inst.parity = getattr(constants.Parity, conn.get("parity", "none"))
        inst.stop_bits = {1: constants.StopBits.one, 1.5: constants.StopBits.one_and_a_half,
                          2: constants.StopBits.two}[conn.get("stop_bits", 1)]

    def ask(cmd: str) -> str:
        inst.write(cmd)
        reply = inst.read()
        if conn.get("echo") and reply.strip() == cmd.strip():
            reply = inst.read()
        if conn.get("ack"):
            inst.read()
        return reply.strip()

    identify = card.get("identify") or {}
    query = identify.get("query") or "*IDN?"
    try:
        who = ask(query)
    except Exception as e:
        sys.exit("%s did not answer %s (%s). Check the address and the connection settings." % (args.address, query, e))
    print("%-22s %-34s %s" % ("identity", query, who))
    if identify.get("idn") and not re.search(identify["idn"], who, re.I):
        print("This is not a %s (its card expects %s). Nothing else was sent." % (card["model"], identify["idn"]))
        return 2
    misses = 0
    for name, spec in params.items():
        cmd = spec.get("get")
        if not cmd:
            continue
        cmd = expand(str(cmd), values)
        why = ("a %s" % spec.get("type") if spec.get("type") in ("trace", "image") else
               "it starts an acquisition" if spec.get("acquires") else
               "read only while %s is on" % spec["read_when"] if spec.get("read_when") else
               "it could start a measurement" if RISKY_READ.match(cmd) else "")
        if why:
            print("%-22s %-34s skipped: %s" % (name, cmd, why))
            continue
        try:
            reply = ask(cmd)
            misses = 0
        except Exception as e:
            reply = "no answer (%s)" % type(e).__name__
            misses += 1
        print("%-22s %-34s %s %s" % (name, cmd, reply, spec.get("unit", "")))
        if misses >= 3:
            print("Three readings in a row went unanswered; stopping.")
            break
    if card.get("error_query"):
        try:
            print("%-22s %-34s %s" % ("errors", card["error_query"], ask(expand(card["error_query"], values))))
        except Exception:
            pass
    inst.close()
    print("Compare these with the front panel. Nothing was set.")
    return 0


# ---------------------------------------------------------------- command line

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="kic", description="Tools for the Kelvin instrument collection.")
    sub = ap.add_subparsers(dest="command", required=True)
    v = sub.add_parser("validate", help="check every instrument, card, experiment and lab config")
    v.add_argument("--warnings", action="store_true", help="also show warnings")
    v.add_argument("--no-kelvin", action="store_true", help="skip Kelvin's own parsers even if Kelvin is installed")
    v.set_defaults(func=cmd_validate)
    x = sub.add_parser("index", help="rebuild index.json and CATALOG.md")
    x.add_argument("--check", action="store_true", help="only say whether they are up to date")
    x.set_defaults(func=cmd_index)
    f = sub.add_parser("find", help="look up instruments, experiments and lab configs")
    f.add_argument("text", nargs="*", help="words to look for, e.g. lock-in srs")
    f.add_argument("--idn", help="an instrument's *IDN? reply: which entry is it?")
    f.set_defaults(func=cmd_find)
    i = sub.add_parser("install", help="put the collection's cards into ~/Kelvin/cards")
    i.add_argument("ids", nargs="*", help="only these cards (e.g. srs/sr844)")
    i.add_argument("--category", help="only this category, e.g. optics")
    i.add_argument("--kelvin-home", help="Kelvin's folder (default ~/Kelvin)")
    i.add_argument("--kelvin-app", help="where Kelvin is installed, to see which cards it brings")
    i.add_argument("--dry-run", action="store_true", help="say what would change, change nothing")
    i.set_defaults(func=cmd_install)
    m = sub.add_parser("manuals", help="download public manuals")
    m.add_argument("ids", nargs="*", help="instruments, e.g. srs/sr830 lakeshore/336")
    m.add_argument("--lab", help="every instrument in a lab config, e.g. ppms-transport")
    m.add_argument("--out", default=str(ROOT / "manuals"), help="where to put them (default ./manuals)")
    m.add_argument("--pin", action="store_true", help="record each manual's SHA-256 in its instrument.yaml")
    m.set_defaults(func=cmd_manuals)
    lk = sub.add_parser("links", help="check that manuals and links still answer")
    lk.add_argument("ids", nargs="*", help="only these instruments")
    lk.add_argument("--manuals-only", action="store_true", help="check manuals only")
    lk.add_argument("--verbose", action="store_true", help="also list moved and blocked links")
    lk.set_defaults(func=cmd_links)
    pr = sub.add_parser("probe", help="ask an instrument who it is and read its settings (sets nothing)")
    pr.add_argument("card", help="a card id (srs/sr830) or a card file")
    pr.add_argument("address", help="GPIB0::8::INSTR, TCPIP0::10.0.0.5::INSTR, serial://COM3, ...")
    pr.add_argument("--var", action="append", help="a card variable, e.g. --var axis=2")
    pr.add_argument("--backend", help="PyVISA backend, e.g. @py for pyvisa-py")
    pr.set_defaults(func=cmd_probe)
    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
