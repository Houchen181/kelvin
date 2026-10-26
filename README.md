<p align="center">
  <img src=".github/kelvin.svg" width="112" alt="Kelvin: a sleeping cat beside a snowflake">
</p>

<h1 align="center">Kelvin</h1>
<p align="center"><b>The coolest cat in the lab.</b><br>An AI lab assistant for experimental physicists that plans, measures and logs, and asks before it drives your sample harder.</p>

<p align="center"><a href="../../releases/latest/download/Kelvin-Setup.exe"><b>⬇ Download Kelvin for Windows</b></a> (Windows 10/11)<br><a href="../../releases/latest/download/Kelvin-macOS.zip">macOS</a> (Apple silicon) · <a href="../../releases">what's new</a> · <a href="CATALOG.md">instrument collection</a></p>

---

You ask in plain words. Kelvin turns the request into a measurement plan for your instruments, asks you before anything drives the sample harder, runs it, and fits the result. Every command and approval is logged.

```text
You     Sweep the gate from 0 to 5 V and record the lock-in signal.
Kelvin  Plan gate_sweep: smu.V from 0 to 5 V in 0.1 V steps; read lockin.X and smu.I; back to 0 V after.
        Approve?  51 points.  smu.output off → on,  smu.V 0 → 5 V (your limit ±10 V), ramped.
You     Approve
Kelvin  Done. lockin.X has a peak at 2.41 ± 0.02 V, FWHM 0.38 ± 0.05 V.
        Plot, data and fit in runs/20261018-153012-gate_sweep/
```

It works with Claude, GPT, Gemini, your ChatGPT plan or a local model, and keeps everything on your computer.

This repository holds Kelvin's **releases** and its **instrument collection**: cards for the instruments Kelvin talks
to, links to the makers' manuals, experiments with plans ready to run, and lab configs for common setups.

## Install

- **Windows 10/11:** run `Kelvin-Setup.exe` from the [latest release](../../releases/latest). No admin rights are
  needed. It isn't code-signed yet: if Windows warns you, choose **More info → Run anyway**.
- **macOS (Apple silicon):** unzip `Kelvin-macOS.zip` and move `Kelvin.app` to Applications. It isn't signed yet:
  the first time, right-click it and choose **Open**.

Kelvin opens on a simulated lab with a demo model, so you can try it right away; add an API key in Settings to use a
real model. It keeps itself up to date from this repository's releases, and installs a download only if it matches
the checksum GitHub gives for it.

## Safety

Every command goes through one gate, whether it comes from Kelvin, another AI agent, or you in the terminal.

| Command | What happens |
|---|---|
| Measure or configure | Runs, and is logged |
| Drive toward safe | Runs, ramped |
| Drive away from safe | Checked against your limits, approved by a person, ramped and watched |
| Beyond the limits, or blocked | Refused |

Only people can change the lab config, the approval mode or which lab Kelvin controls.

## Instrument collection

Every lab PC needs the same things before the first measurement: a card that says how to talk to each instrument
safely, the maker's manual, and a starting point for the experiment. They are collected here, so a new computer
(or a new lab) is set up in minutes.

| Folder | What is in it |
|---|---|
| [`instruments/`](instruments) | One folder per instrument model, `instruments/<maker>/<model>/`: who makes it, how it talks, where its manuals and drivers are, and its **Kelvin card** when there is one |
| [`experiments/`](experiments) | What to measure and how, by area: roles, wiring, procedure, analysis, pitfalls, and **Kelvin plans** ready to run |
| [`labs/`](labs) | **Lab configs** for common setups (a PPMS transport rack, a confocal microscope, an NV setup...) |
| [`CATALOG.md`](CATALOG.md) | Everything above, by category, experiment and maker |
| [`index.json`](index.json) | The same, for Kelvin and other programs |
| [`tools/kic.py`](tools/kic.py) | Install cards, find an instrument, fetch manuals, probe an instrument, check the collection |

**[Browse the catalog →](CATALOG.md)**

| Instruments | | Experiments | |
|---|---|---|---|
| Electronics | source-meters, lock-ins, preamps, DMMs, DACs, generators, DAQ | Transport | R(T), Hall, gating, Landau fans, nonlinear Hall, dI/dV, critical current |
| RF and microwave | signal generators, VNAs, spectrum analyzers, AOM drivers, qubit controllers | Magnetometry | SQUID M(T) and M(H), AC susceptibility |
| Timing | pulse and delay generators, photon counters, time taggers | Optics | PL, Raman, mapping, photocurrent, reflectance, MOKE |
| Lasers | CW, tunable and ultrafast lasers, diode controllers, wavemeters | Ultrafast and nonlinear | SHG rotational anisotropy, pump-probe |
| Optics | spectrometers, spectrographs, cameras, power meters, choppers, PEMs | Spin resonance | NV ODMR, Rabi, Ramsey, echo, T1, FMR |
| Motion | piezo positioners, scanners, stages, delay lines, rotation mounts | Quantum devices | Coulomb diamonds, resonators, qubits |
| Cryogenics | temperature controllers, PPMS/MPMS, dilution refrigerators, vacuum | Acoustics | SAW transmission, acoustoelectric |
| Magnets | magnet supplies, gaussmeters | AMO | AOM calibration, PLE scans |
| Scanning probe | SPM controllers | Environment | cooldown logs |

The categories, kinds and areas are defined in [`collection.yaml`](collection.yaml).

### Set up a lab computer

On the computer the instruments are plugged into, with Kelvin installed and started once:

```bash
git clone https://github.com/Houchen181/kelvin-instruments
cd kelvin-instruments
python tools/kic.py install
```

`install` copies the collection's cards into `~/Kelvin/cards`, where Kelvin finds them at its next start. It leaves
out the cards Kelvin brings itself, and never overwrites a card that was changed or reviewed on this computer.
Run it again after `git pull` to update. It needs nothing but Python 3.9.

Then start from a lab config: copy one from [`labs/`](labs) to `~/Kelvin/lab.yaml` (or open it in **Lab → Set up…**),
give each instrument its address (**Scan** finds them) and set the limits for your sample. Until it has addresses,
every instrument in it is simulated, so the experiments' plans can be tried first.

```bash
python tools/kic.py find lock-in                                   # look something up
python tools/kic.py find --idn "Stanford_Research_Systems,SR830,s/n1,ver1.07"   # which instrument is this?
python tools/kic.py manuals --lab ppms-transport --out D:/manuals  # fetch the manuals, e.g. for an offline PC
python tools/kic.py probe srs/sr830 GPIB0::8::INSTR                # ask an instrument who it is and read its settings
```

`probe` (which needs PyVISA) only reads: it checks the instrument's identity first and stops if it is not the
model the card describes, and it skips readings that could start a measurement. For an offline PC, put each manual
into `~/Kelvin/instruments/<name>/manual.pdf`, where Kelvin looks for it.

### Cards and trust

A card tags every parameter as *measure* or *drive* and gives each drive a safe value; Kelvin's safety gate guards
every move away from it. Card status says how far to trust one:

| Status | Meaning | In Kelvin |
|---|---|---|
| `community` | Written from the maker's manual and reviewed, not yet checked on hardware | Works; watch the first runs |
| `lab-verified` | Checked on hardware by a lab, recorded under `verified` in its `instrument.yaml` | Works |
| `draft` | Not reviewed by a person | Readings work; outputs stay simulated until someone checks it |
| *no card* | Catalogued with its manual | Kelvin writes a draft card from the manual when it finds the instrument |

Cards never replace hardware interlocks. Keep the limits in your lab config tighter than the card's.

### Manuals and example scripts

Manuals are linked, not copied: they belong to their makers, and most may not be redistributed. Each entry gives
the maker's own URL, what part covers remote control, and whether it is public, behind a sign-in, or only for
owners. `kic manuals --pin` records a manual's SHA-256, so a changed edition is noticed, and a weekly check reports
links that have moved.

The runnable examples are Kelvin plans, inside each experiment, checked against their lab config. Each instrument
also lists open-source drivers (PyMeasure, QCoDeS, pylablib), the maker's SDK, and the maker's example repositories
with their licenses.

## Contributing

New instruments, cards, hardware checks, experiments and lab configs are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).
`python tools/kic.py validate` checks everything (with PyYAML), and `python tools/kic.py index` rebuilds the catalog.
Kelvin's own issues and feature requests are welcome in [Issues](../../issues) too.

## License

The instrument collection, everything in this repository's files, is MIT licensed ([LICENSE](LICENSE)). Kelvin itself
is distributed as the installers under [Releases](../../releases). Manuals, software and trademarks linked from the
collection belong to their owners.
