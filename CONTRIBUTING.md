# Contributing

Thank you for adding to the collection. Everything here is checked by `python tools/kic.py validate` (it needs
PyYAML), and the catalog is rebuilt by `python tools/kic.py index`. Run both before opening a pull request; the
same checks run on every pull request.

If you have Kelvin installed from source in the same Python, `validate` also runs Kelvin's own card, lab-config and
plan parsers.

## Add an instrument

Instruments are sorted by category, then kind: `instruments/<category>/<kind>/<maker>-<model>/instrument.yaml`.
The kind decides the category (see `collection.yaml`), so a new source-meter from ACME goes in
`instruments/electronics/source-meter/acme-sm-2000/`. Its id is `maker/model` in lowercase letters, digits, `-`
and `.` (use the maker slugs already in use, such as `keithley`, `srs`, `lakeshore`, `zhinst`); `validate` says
where an instrument belongs if it is in the wrong folder.

```yaml
schema: 1
id: acme/sm-2000
maker: ACME Instruments
model: SM-2000
name: ACME SM-2000 source-measure unit
covers: [SM-2001]                       # other models with the same command set
kind: source-meter                      # one of the kinds in collection.yaml
categories: []                          # extra categories, only if it clearly belongs to more than its kind's
interfaces: [gpib, usb-tmc, lan]
control: scpi                           # scpi, text, library, web-api or none
identify:                               # only when there is no card: the *IDN? reply, as a regex
  idn: "^ACME,SM-200[01],"
  example: "ACME,SM-2000,12345,1.02"
  usb: ["1234:5678"]                    # the USB IDs it reports, VID:PID in hex (see USB IDs below)
manuals:
  - title: SM-2000 Programming Manual
    url: https://www.acme.example/manuals/sm-2000-programming.pdf
    covers: "Chapter 6: SCPI command reference"
    access: public                      # public, sign-in or owners
software:
  - name: PyMeasure
    kind: python-driver                 # python-driver, vendor-sdk or vendor-software
    ref: pymeasure.instruments.acme.SM2000
    url: https://github.com/pymeasure/pymeasure/blob/master/pymeasure/instruments/acme/sm2000.py
notes:
  - One or two sentences of practical advice. No marketing.
```

- **Links:** only the maker's own pages (or its official GitHub or PyPI), opened by you. Never link third-party
  manual mirrors, and never commit a manual's PDF.
- **Drivers:** only ones you have seen in the project's docs or source.

### USB IDs

An instrument that doesn't answer `*IDN?` (a maker's USB device driven through its SDK, a USB-serial instrument
with a protocol of its own, a USB-TMC instrument that ignores `*IDN?`) is named by its USB ID instead: VID:PID in
hex, such as `1313:8078`. Kelvin names a plugged-in instrument by it (its scan, and its list of what is plugged
in), with the manual listed here.

- **Where it goes:** `identify.usb`, a list: in the card when there is one, otherwise in `instrument.yaml`. List
  every ID the model reports, and only IDs you have seen on the instrument or in its maker's documentation.
- **Finding it:** plug the instrument in, then
  - Windows: Device Manager, the device, Properties, Details, **Hardware Ids**: `USB\VID_1313&PID_8078` is
    `1313:8078`.
  - Linux: `lsusb`, which prints `ID 1313:8078` before the device's name.
  - Mac: System Information, USB, the device: its **Vendor ID** (`0x1313`) and **Product ID** (`0x8078`).
- **Never a generic adapter's IDs.** When the instrument shows up as a USB-serial cable or the chip inside it does
  (an FTDI, Prolific, Silicon Labs CP210x, WCH CH340 or CH9102, Microchip MCP2200, an ATEN or Moxa adapter, with the
  chip's own IDs such as `0403:6001` or `1a86:7523`), leave `usb` out: those IDs only say which chip is inside, and
  any maker's product built on that chip has them. `validate` refuses them. A maker's own product ID on such a chip,
  such as Thorlabs' `0403:faf0`, is the maker's and belongs here.

## Add or update a card

The easiest way to write a card is with Kelvin: **Lab → Set up → Make a card for it from its manual or example
scripts**, then **Try it** on the instrument until the readings match the front panel. Kelvin saves it as
`~/Kelvin/cards/<maker>_<model>.yaml`; copy it as `card.yaml` into the instrument's folder
(`instruments/<category>/<kind>/<maker>-<model>/`) and add `card: card.yaml` to the `instrument.yaml` next to it.

- A card nobody has checked is `status: draft`. Kelvin keeps a draft's outputs simulated on real hardware.
- `community` means a person has read the card against the manual: every drive and its safe value, the limits,
  and the blocked commands.
- `lab-verified` means it has been checked on hardware. Add the check to `instrument.yaml`:

  ```yaml
  verified:
    - lab: Example Lab, Example University
      by: github-handle
      date: 2026-10-26
      firmware: "1.07"
      summary: Readings match the front panel; output, V and compliance checked into a 1 MΩ load.
  ```

### Review checklist for cards

Cards decide what Kelvin treats as safe, so every card change gets a second look:

- [ ] Every parameter that changes what reaches the sample (voltage, current, field, temperature, laser or RF
      power, output on/off) is a `drive`, with a `safe` value and the vendor's `limits`.
- [ ] Readings that switch an output on or start a measurement are marked (`read_when`, `acquires`).
- [ ] Commands that change what readings mean or bypass the instrument's own protection are under `raw.blocked`:
      calibration, firmware, sensor curves, coil constants, persistent-switch heaters, current limits.
- [ ] `on_connect` only sets up the connection (terminations, headers, listen mode); it never sets a parameter.
- [ ] `identify.idn` matches this model and no other.
- [ ] `identify.usb`, if given, lists only the IDs this model reports, never a USB-serial chip's own.
- [ ] `manual` names the manual and chapter the card follows; its `manual_url` is listed under `manuals`.

## Send a card from Kelvin

A card your lab reviewed in Kelvin can come here without copying files: **Send to the collection** next to it in
**Lab → Cards…** (or ask Kelvin in a chat to send it). Kelvin first shows exactly what goes, then opens the **Send a
card from Kelvin** issue form in your browser, filled in: the card, its maker, model, kind and interfaces, its id here
when the collection has it, an identity reply and USB IDs with the serial numbers taken out, and a summary of the
check on hardware from your lab's record for you to edit. Kelvin leaves out addresses, serial numbers, host names, file
paths and names; the **Credit** field is yours to fill in. A card too long for the link is copied for you to paste.
Nothing is sent until you submit the form from your own GitHub account, and Kelvin needs no GitHub token.

The workflow `.github/workflows/card-from-issue.yml` then runs `python tools/kic.py from-issue` on the issue. It puts
the card into its instrument's folder as `card.yaml` (or makes the folder of an instrument the collection lacks),
brings `instrument.yaml` up to date (`card: card.yaml`, the card's manual, a `verified` entry for the check on
hardware), runs `validate` and `index`, and opens a pull request crediting you. It comments on the issue with the
pull request's link, or with what to fix: edit the issue and it runs again. The maintainer reviews the pull request
like any card change; nothing is merged without that review.

## Report a hardware check

Open an issue with the **Hardware verification** form, or a pull request that adds a `verified` entry. Say which
firmware you checked and what you compared.

## Add an experiment

Create `experiments/<area>/<name>.yaml`, with an area from `collection.yaml`. Name the instruments it needs by
`roles` (with kinds, and suggested instruments from the collection), and write `plans` in Kelvin's plan format for
one of the lab configs in `labs/`. `validate` checks that every plan only names instruments and parameters of that
lab. If the experiment needs an instrument no card covers yet, list its kind under `needs_cards` instead of writing
plans; it then shows up under **Wanted cards** in the catalog.

Keep the physics right and the advice concrete: what to wire, what to check first, how to analyze, what goes wrong.
Give references with a DOI where there is one.

## Add a lab config

A lab config in `labs/` is a Kelvin `lab.yaml` for a common setup. Leave the addresses as comments (an instrument
without one is simulated), keep the limits conservative, and include each drive's safe value in its limits (Kelvin
refuses to run otherwise).

## Style

Plain words, SI units, no marketing. Say what something does, not that it is great.
