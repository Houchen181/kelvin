# Lasers and laser control

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

CW, tunable and ultrafast lasers, diode and TEC controllers, wavelength meters.

## Lasers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Coherent Chameleon Ultra / Discovery ultrafast Ti:sapphire lasers](laser/coherent-chameleon) | no card | RS-232, USB | [support](https://www.coherent.com/lasers/oscillators/chameleon-ultra) |
| [Coherent OBIS LX/LS lasers](laser/coherent-obis) | [community](laser/coherent-obis/card.yaml) | USB, RS-232 | [manual](https://www.coherent.com/content/dam/coherent/site/en/resources/manuals/lasers/obis-lx-ls-operators-manual.pdf) |
| [HÜBNER Photonics Cobolt 04-01 / 06-01 / 08-01 series lasers](laser/hubner-cobolt) | no card | USB, RS-232 | [manual](https://hubner-photonics.com/wp-content/uploads/2023/11/D0136-P_Manual-Cobolt-06-01-Series_October_2023-1.pdf) |
| [Light Conversion PHAROS femtosecond laser](laser/lightcon-pharos) | [community](laser/lightcon-pharos/card.yaml) | LAN, web API |  |
| [M Squared SolsTiS Ti:sapphire laser (ICE-BLOC)](laser/m2-solstis) | [community](laser/m2-solstis/card.yaml) | LAN |  |
| [NKT Photonics SuperK EXTREME / FIANIUM supercontinuum lasers](laser/nkt-superk) | no card | USB, LAN, RS-232 | [manual](https://lf.hamamatsu.com/wp-json/nktphotonics/v1/download/SuperK-EXTREME/SuperK%20EXTREME%20Product%20Guide.pdf) |
| [Spectra-Physics Mai Tai Ti:sapphire ultrafast laser](laser/spectra-physics-mai-tai) | no card | RS-232 | [manual](https://api.p1.mks.com/mam/celum/celum_assets/sp/resources/284A_Rev_G_Mai_Tai_Users_Manual.pdf) |

## Laser diode and TEC controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs CLD1010 compact laser diode and TEC controller](laser-driver/thorlabs-cld1010) | no card | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/c/cl/cld/cld1015/doc-104674.pdf) |
| [Thorlabs ITC4000-series laser diode and TEC controllers](laser-driver/thorlabs-itc4000) | [community](laser-driver/thorlabs-itc4000/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/t/te/ted/ted4015/16407-d03.pdf) |
| [TOPTICA DLC pro diode laser controller](laser-driver/toptica-dlc-pro) | [draft](laser-driver/toptica-dlc-pro/card.yaml) | LAN, USB |  |

## Wavelength meters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Bristol Instruments 671 / 771 / 871 wavelength meters](wavemeter/bristol-wavemeter) | no card | USB, LAN | [support](https://www.bristol-inst.com/wp-content/uploads/2023/09/Bristol-671-Series-Laser-Wavelength-Meter-Specifications.pdf) |
| [HighFinesse WS6 / WS7 / WS8 wavelength meters](wavemeter/highfinesse-wavemeter) | no card | USB | [support](https://www.highfinesse.com/en/support/downloads.html) |
