# Safety and security

Cards and lab configs decide what Kelvin treats as safe: which parameters are drives, their safe values and limits,
and which commands are blocked. A wrong card can let an instrument do more than its owner intended.

**If you find a card that could drive an instrument unsafely** (a drive marked as a measurement, a missing or wrong
safe value, limits beyond the vendor's, an unblocked calibration or firmware command, a reading that switches an
output on), please report it privately: use **Security → Report a vulnerability** on this repository. For problems
that are not urgent, an issue with the **Card problem** form is fine.

Things this repository does to keep cards trustworthy:

- Every card is checked by `tools/kic.py validate` on each pull request: drives need safe values and limits,
  `on_connect` may not set parameters, a library card may only name its maker's module.
- Card changes need a maintainer's review (see `.github/CODEOWNERS`) against the checklist in CONTRIBUTING.md.
- `kic install` never overwrites a card that was changed or reviewed on the lab computer, and Kelvin keeps a draft
  card's outputs simulated until a person checks it.

Software limits add to hardware interlocks; they never replace them.
