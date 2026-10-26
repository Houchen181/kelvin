# Contributing

Thank you for adding to the collection. Everything here is checked by `python tools/kic.py validate` (it needs
PyYAML), and the catalog is rebuilt by `python tools/kic.py index`. Run both before opening a pull request; the
same checks run on every pull request.

If you have Kelvin installed from source in the same Python, `validate` also runs Kelvin's own card, lab-config and
plan parsers.

## Add an instrument

Create `instruments/<maker>/<model>/instrument.yaml`, with lowercase letters, digits, `-` and `.` in both names
(use the maker slugs already in use, such as `keithley`, `srs`, `lakeshore`, `zhinst`):

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

## Add or update a card

The easiest way to write a card is with Kelvin: **Lab → Set up → Make a card for it from its manual or example
scripts**, then **Try it** on the instrument until the readings match the front panel. Kelvin saves it as
`~/Kelvin/cards/<maker>_<model>.yaml`; copy it to `instruments/<maker>/<model>/card.yaml` and add `card: card.yaml`
to the `instrument.yaml` next to it.

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
- [ ] `manual` names the manual and chapter the card follows; its `manual_url` is listed under `manuals`.

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
