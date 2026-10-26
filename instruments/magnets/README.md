# Magnets and field measurement

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Superconducting magnet supplies, gaussmeters and teslameters.

## Magnet power supplies

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [American Magnetics Model 430 magnet power supply programmer](magnet-supply/ami-430) | [community](magnet-supply/ami-430/card.yaml) | RS-232, LAN | [manual](https://www.americanmagnetics.com/support/manuals/mn-430-rev14.pdf) |
| [Cryomagnetics Model 4G superconducting magnet power supply](magnet-supply/cryomagnetics-4g) | no card | USB, LAN, GPIB | [manual](https://cryomagnetics.com/wp-content/uploads/2022/05/4G-Rev-9_3.pdf) |
| [Lake Shore Model 625 superconducting magnet power supply](magnet-supply/lakeshore-625) | [community](magnet-supply/lakeshore-625/card.yaml) | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/625_manual.pdf?sfvrsn=2d9f6b7_1) |
| [Oxford Instruments Mercury iPS superconducting magnet power supply](magnet-supply/oxford-mercury-ips) | no card | LAN, RS-232, USB, GPIB | [manual](https://mymercurysupport.com/sites/default/files/59_UMC0072_01.pdf) |

## Gaussmeters and teslameters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Lake Shore Model 475 DSP gaussmeter](gaussmeter/lakeshore-475) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/475_manual.pdf) |

## Also used here

- [Quantum Design OptiCool magneto-optical cryostat](../cryogenics/cryostat/qd-opticool), in cryogenics
