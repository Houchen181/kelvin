"""tools/kic.py from-issue: a card sent from Kelvin as an issue (the new-card form) becomes the files of a pull request.
Each test runs it on a copy of the collection, as the card-from-issue workflow does on its checkout."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

yaml = pytest.importorskip("yaml")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
import kic  # noqa: E402

# the form's field ids, which Kelvin fills the form in by (labharness/contribute.py FIELDS): the two must agree
FIELDS = ["instrument", "maker", "model", "kind", "interfaces", "idn", "usb", "firmware", "checked", "credit", "card"]

NEW_CARD = """\
# Drafted by Kelvin on 2026-11-16 from https://www.acmex.example/manuals/sm-2000.pdf with a model.
card: 1
id: acmex/sm-2000
model: ACMEX SM-2000 source-measure unit
vendor: ACMEX Instruments
kind: source-meter
status: lab-verified
manual: SM-2000 Programming Manual, chapter 6
manual_url: https://www.acmex.example/manuals/sm-2000.pdf
identify:
  idn: "^ACMEX,SM-2000,"
  example: "ACMEX,SM-2000,<serial number>,1.02"
error_query: "SYST:ERR?"
parameters:
  V:
    label: Voltage
    kind: drive
    unit: V
    set: "SOUR:VOLT {value}"
    get: "SOUR:VOLT?"
    limits: [-21, 21]
    safe: 0
    ramp: gate
    max_rate: 1
  I:
    label: Current
    kind: measure
    unit: A
    get: "SENS:CURR?"
"""

SR844_CARD = """\
card: 1
id: stanford/sr844
model: Stanford Research Systems SR844 RF lock-in amplifier
vendor: Stanford Research Systems
kind: lock-in-amplifier
status: lab-verified
manual: SR844 manual, chapter 5 (remote programming)
manual_url: https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf
identify:
  idn: "^Stanford_Research_Systems,SR844,"
  example: "Stanford_Research_Systems,SR844,<serial number>,ver1.006"
parameters:
  X:
    label: X
    kind: measure
    unit: V
    get: "OUTP? 1"
  frequency:
    label: Reference frequency
    kind: measure
    unit: Hz
    get: "FREQ?"
"""


def copy(tmp_path: Path) -> Path:
    root = tmp_path / "collection"
    shutil.copytree(REPO, root, ignore=shutil.ignore_patterns("." + "git", "__pycache__", ".pytest_cache", "manuals"))
    return root


def body(**answers: str) -> str:
    """An issue's body as GitHub writes it from the form: each field's label as a heading, then its answer (the card in
    a yaml code block, an empty field as _No response_)."""
    out = []
    for fid, label in kic.form_fields(REPO / ".github" / "ISSUE_TEMPLATE" / "new-card.yml"):
        value = answers.get(fid, "")
        if fid == "card" and value:
            value = "```yaml\n%s\n```" % value.strip("\n")
        out += ["### " + label, "", value or "_No response_", ""]
    return "\n".join(out)


def run(root: Path, text: str, *more: str) -> "tuple[subprocess.CompletedProcess, Path]":
    issue, report = root.parent / "issue.md", root.parent / "report"
    issue.write_text(text, encoding="utf-8")
    p = subprocess.run([sys.executable, str(root / "tools" / "kic.py"), "from-issue", str(issue), "--issue", "7",
                        "--author", "octo-lab", "--author-id", "123", "--date", "2026-11-17", "--report", str(report),
                        "--no-kelvin"] + list(more), capture_output=True, text=True, encoding="utf-8")
    return p, report


def snapshot(root: Path) -> dict:
    """Every file's SHA-256 and every folder, by path."""
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else "folder"
            for p in sorted(root.rglob("*")) if "__pycache__" not in p.parts}


def validates(root: Path) -> bool:
    return subprocess.run([sys.executable, str(root / "tools" / "kic.py"), "validate", "--no-kelvin"],
                          capture_output=True, text=True).returncode == 0


def test_the_form_and_from_issue_agree_on_the_fields():
    form = yaml.safe_load((REPO / ".github" / "ISSUE_TEMPLATE" / "new-card.yml").read_text(encoding="utf-8"))
    fields = kic.form_fields(REPO / ".github" / "ISSUE_TEMPLATE" / "new-card.yml")
    assert [fid for fid, _ in fields] == FIELDS
    assert len({label for _, label in fields}) == len(fields)          # each answer found by its own heading
    assert form["labels"] == ["new-card"]                               # what the workflow runs for
    card = next(item for item in form["body"] if item.get("id") == "card")
    assert card["type"] == "textarea" and card["attributes"]["render"] == "yaml" and card["validations"]["required"]
    assert all(item["type"] in ("input", "textarea") for item in form["body"] if item.get("id"))   # prefilled by URL


def test_a_new_instrument_gets_its_folder_its_card_and_the_check_on_hardware(tmp_path):
    root = copy(tmp_path)
    checked = ("- Read on the instrument: V, I\n- Set on the instrument: V (0 V to 5 V)\n"
               "- Compared with the front panel.")
    p, report = run(root, body(maker="ACMEX Instruments", model="SM-2000", kind="source-meter",
                               interfaces="gpib, usb-tmc", idn="ACMEX,SM-2000,<serial number>,1.02",
                               usb="abcd:1234, 0403:6001", firmware="1.02", checked=checked,
                               credit="Example Lab, Example University", card=NEW_CARD))
    assert p.returncode == 0, p.stdout + p.stderr
    folder = root / "instruments" / "electronics" / "source-meter" / "acmex-sm-2000"
    inst = kic.load_yaml(folder / "instrument.yaml")
    assert inst["id"] == "acmex/sm-2000" and inst["maker"] == "ACMEX Instruments" and inst["model"] == "SM-2000"
    assert inst["name"] == "ACMEX SM-2000 source-measure unit" and inst["kind"] == "source-meter"
    assert inst["interfaces"] == ["gpib", "usb-tmc"] and inst["control"] == "scpi" and inst["card"] == "card.yaml"
    assert inst["manuals"] == [{"title": "SM-2000 Programming Manual, chapter 6",
                                "url": "https://www.acmex.example/manuals/sm-2000.pdf", "access": "public"}]
    check = inst["verified"][0]
    assert check["lab"] == "Example Lab, Example University" and check["by"] == "octo-lab"
    assert str(check["date"]) == "2026-11-17" and check["firmware"] == "1.02"
    assert check["summary"].startswith("Read on the instrument: V, I; Set on the instrument")
    card_text = (folder / "card.yaml").read_text(encoding="utf-8")
    assert card_text.startswith("# Drafted by Kelvin")                  # the card as sent, its comments too
    card = kic.load_yaml(folder / "card.yaml")
    assert card["identify"]["usb"] == ["abcd:1234"]                      # the generic FTDI chip's ID left out
    index = json.loads((root / "index.json").read_text(encoding="utf-8"))
    entry = next(i for i in index["instruments"] if i["id"] == "acmex/sm-2000")
    assert entry["usb"] == ["abcd:1234"] and entry["card"]["status"] == "lab-verified"
    assert "acmex-sm-2000" in (root / "CATALOG.md").read_text(encoding="utf-8")
    assert validates(root)
    pr = (report / "pr.md").read_text(encoding="utf-8")
    assert pr.startswith("Closes #7") and "@octo-lab sent this card from Kelvin: a new instrument" in pr
    assert "`0403:6001`: generic USB-serial chips' IDs" in pr and "Compared with the front panel." in pr
    assert (report / "title.txt").read_text(encoding="utf-8").strip() == "Card for acmex/sm-2000 (#7)"
    assert "Co-authored-by: octo-lab <123+octo-lab@users.noreply.github.com>" in (report / "commit.txt").read_text(
        encoding="utf-8")


def test_an_instrument_the_collection_has_gets_the_card_under_its_own_id_and_kind(tmp_path):
    root = copy(tmp_path)
    p, report = run(root, body(instrument="srs/sr844", maker="Stanford Research Systems", model="SR844",
                               kind="lock-in", interfaces="gpib", card=SR844_CARD))
    assert p.returncode == 0, p.stdout + p.stderr
    folder = root / "instruments" / "electronics" / "lock-in" / "srs-sr844"
    card = kic.load_yaml(folder / "card.yaml")
    assert card["id"] == "srs/sr844" and card["kind"] == "lock-in"          # the instrument's, not the card's
    inst = kic.load_yaml(folder / "instrument.yaml")
    assert inst["card"] == "card.yaml" and "identify" not in inst        # identify lives in the card now
    assert "verified" not in inst                                         # nothing was checked on hardware
    assert len(inst["manuals"]) == 1                                      # its manual was listed already
    text = (folder / "instrument.yaml").read_text(encoding="utf-8")
    assert text.index("card: card.yaml") < text.index("manuals:")         # in the collection's order
    assert validates(root)
    pr = (report / "pr.md").read_text(encoding="utf-8")
    assert "The card's id was `stanford/sr844`; it is filed under the instrument's id, `srs/sr844`." in pr
    assert "The card's kind was `lock-in-amplifier`" in pr and "instrument.yaml had identify" in pr
    assert "which had none" in pr


def test_a_card_the_collection_has_is_replaced_and_the_check_added(tmp_path):
    root = copy(tmp_path)
    folder = root / "instruments" / "optics" / "modulator" / "hinds-pem200"
    sent = (folder / "card.yaml").read_text(encoding="utf-8").replace("status: community", "status: lab-verified")
    p, report = run(root, body(maker="Hinds Instruments", model="PEM-200", kind="modulator", interfaces="usb",
                               checked="Amplitude and frequency read against the controller's display.",
                               firmware="V01", card=sent))
    assert p.returncode == 0, p.stdout + p.stderr
    assert (folder / "card.yaml").read_text(encoding="utf-8") == sent
    inst = kic.load_yaml(folder / "instrument.yaml")
    assert inst["verified"] == [{"lab": "not named", "by": "octo-lab", "date": inst["verified"][0]["date"],
                                 "firmware": "V01",
                                 "summary": "Amplitude and frequency read against the controller's display."}]
    assert "replacing its community card" in (report / "pr.md").read_text(encoding="utf-8")
    assert validates(root)
    p, _ = run(root, body(card=sent, checked="Amplitude and frequency read against the controller's display.",
                          firmware="V01"))
    assert p.returncode == 0                                              # a second check is a second entry
    assert len(kic.load_yaml(folder / "instrument.yaml")["verified"]) == 2


@pytest.mark.parametrize("card, said", [
    ("card: 1\nid: [unclosed\n", "not valid YAML"),
    ("card: 1\nid: &a acmex/x\nmodel: *a\n", "anchors or aliases"),
    ("!!python/object/apply:os.system ['echo pwned']\n", "not valid YAML"),
    (NEW_CARD.replace("id: acmex/sm-2000", "id: ../../tools/x"), "is not maker/model"),
    (NEW_CARD.replace("    safe: 0\n", ""), "a drive needs a safe value"),
    ("", "The card is empty"),
])
def test_an_issue_that_cant_go_in_says_why_and_changes_nothing(tmp_path, card, said):
    root = copy(tmp_path)
    before = snapshot(root)
    p, report = run(root, body(maker="ACMEX Instruments", model="SM-2000", kind="source-meter", interfaces="gpib",
                               card=card))
    assert p.returncode == 1 and said in p.stdout, p.stdout + p.stderr
    assert said in (report / "comment.md").read_text(encoding="utf-8")
    assert snapshot(root) == before                                       # every file as it was, no folder left


def test_ids_kinds_and_usb_ids_from_an_issue_are_checked(tmp_path):
    root = copy(tmp_path)
    before = snapshot(root)
    p, _ = run(root, body(instrument="nobody/nothing", card=NEW_CARD))
    assert p.returncode == 1 and "the collection has no instrument nobody/nothing" in p.stdout
    p, _ = run(root, body(instrument="../../etc", card=NEW_CARD))
    assert p.returncode == 1 and "is not an id such as srs/sr830" in p.stdout
    p, _ = run(root, body(maker="ACMEX", model="SM-2000", kind="gadget", interfaces="gpib", card=NEW_CARD))
    assert p.returncode == 1 and "Kind 'gadget' is not one of the collection's kinds" in p.stdout
    p, _ = run(root, body(maker="ACMEX", model="SM-2000", kind="source-meter", interfaces="carrier-pigeon",
                          card=NEW_CARD))
    assert p.returncode == 1 and "not carrier-pigeon" in p.stdout
    p, _ = run(root, body(maker="ACMEX", model="SM-2000", kind="source-meter", interfaces="gpib", usb="12:34",
                          card=NEW_CARD))
    assert p.returncode == 1 and "'12:34' is not VID:PID in hex" in p.stdout
    lockin = NEW_CARD.replace('idn: "^ACMEX,SM-2000,"', 'idn: "^Stanford_Research_Systems,SR844,"').replace(
        '"ACMEX,SM-2000,<serial number>,1.02"', '"Stanford_Research_Systems,SR844,<serial number>,ver1.006"')
    p, _ = run(root, body(maker="ACMEX", model="SM-2000", kind="source-meter", interfaces="gpib", card=lockin))
    assert p.returncode == 1 and "the collection has this instrument already, as srs/sr844" in p.stdout
    assert snapshot(root) == before


def test_a_card_as_the_collection_has_it_is_nothing_to_change(tmp_path):
    root = copy(tmp_path)
    folder = root / "instruments" / "optics" / "modulator" / "hinds-pem200"
    p, _ = run(root, body(card=(folder / "card.yaml").read_text(encoding="utf-8")))
    assert p.returncode == 1 and "Nothing to change" in p.stdout


@pytest.mark.parametrize("text", [
    "card: 1\nidentify:\n  idn: x\n  example: x1\n\nparameters: {}\n",
    "card: 1\nidentify: {idn: x, example: x1}\nparameters: {}\n",
    'card: 1\nidentify:\n  idn: x\n  usb:\n  - "0403:6001"\n  example: x1\nparameters: {}\n',
    "card: 1\nparameters: {}\n",
])
def test_usb_ids_go_into_the_cards_identify_block_and_nothing_else_changes(text):
    out = kic.with_usb(text, ["abcd:1234"])
    data, before = kic.load_yaml_text(out), kic.load_yaml_text(text)
    assert data["identify"]["usb"] == ["abcd:1234"] and data["parameters"] == {} and data["card"] == 1
    assert {k: v for k, v in data["identify"].items() if k != "usb"} == \
        {k: v for k, v in (before.get("identify") or {}).items() if k != "usb"}


def test_a_heading_inside_the_card_is_the_cards_text(tmp_path):
    fields = kic.form_fields(REPO / ".github" / "ISSUE_TEMPLATE" / "new-card.yml")
    text = body(maker="ACMEX", card="# ### Maker\ncard: 1\n### Credit\n")
    answers = kic.issue_answers(text, fields)
    assert answers["maker"] == "ACMEX" and answers["credit"] == ""
    assert kic.unfenced(answers["card"]) == "# ### Maker\ncard: 1\n### Credit\n"
    assert answers["usb"] == ""                                           # _No response_ is no answer


def test_the_workflow_hands_over_the_event_file(tmp_path):
    root = copy(tmp_path)
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"action": "opened", "issue": {
        "number": 12, "body": body(maker="ACMEX Instruments", model="SM-2000", kind="source-meter", interfaces="gpib",
                                   card=NEW_CARD),
        "created_at": "2026-11-17T09:30:00Z", "user": {"login": "lab-person", "id": 4567}}}), encoding="utf-8")
    report = tmp_path / "out"
    p = subprocess.run([sys.executable, str(root / "tools" / "kic.py"), "from-issue", "--event", str(event),
                        "--report", str(report), "--no-kelvin"], capture_output=True, text=True, encoding="utf-8")
    assert p.returncode == 0, p.stdout + p.stderr
    assert (report / "pr.md").read_text(encoding="utf-8").startswith("Closes #12\n\n@lab-person sent this card")
    assert "4567+lab-person@users.noreply" in (report / "commit.txt").read_text(encoding="utf-8")


def test_the_workflow_never_puts_the_issues_text_in_a_script():
    flow = (REPO / ".github" / "workflows" / "card-from-issue.yml").read_text(encoding="utf-8")
    assert "github.event.issue.body" not in flow and "github.event.issue.title" not in flow
    assert '--event "$GITHUB_EVENT_PATH"' in flow and "gh pr merge" not in flow
    data = yaml.safe_load(flow)
    assert data["permissions"] == {"contents": "write", "pull-requests": "write", "issues": "write"}
    assert data[True]["issues"]["types"] == ["opened", "edited"]          # YAML 1.1 reads the key on as True
