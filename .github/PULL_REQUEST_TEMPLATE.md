## What this adds or changes

<!-- An instrument, a card, a hardware check, an experiment, a lab config... -->

## Checks

- [ ] `python tools/kic.py validate` passes
- [ ] `python tools/kic.py index` was run (index.json and CATALOG.md are in this pull request)
- [ ] Every link is the maker's own (or its official GitHub or PyPI) and I opened it
- [ ] No manual PDFs are committed

## For a card

- [ ] Drives, safe values and vendor limits checked against the manual (chapter: )
- [ ] Readings that switch an output on or start a measurement are marked (`read_when`, `acquires`)
- [ ] Calibration, firmware and protection-bypassing commands are under `raw.blocked`
- [ ] `on_connect` sets nothing but the connection
- [ ] Tried on hardware? Model, firmware and what was compared:
