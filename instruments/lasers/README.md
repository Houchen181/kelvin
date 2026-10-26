# Lasers and laser control

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

CW, tunable and ultrafast lasers, parametric sources, combs, diode controllers, locks and wavelength meters.

## Lasers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Azurlight Systems ALS fiber lasers and amplifiers](laser/azurlight-als) | no card | analog | [support](https://azurlight-systems.com/high-power-fiber-lasers-low-noise-single-mode-single-frequency/) |
| [Coherent Chameleon Ultra / Discovery ultrafast Ti:sapphire lasers](laser/coherent-chameleon) | no card | RS-232, USB | [support](https://www.coherent.com/lasers/oscillators/chameleon-ultra) |
| [Coherent COMPexPro excimer lasers (COMPex series)](laser/coherent-compex) | no card |  | [support](https://www.coherent.com/lasers/excimer/compex) |
| [Coherent Mephisto NPRO lasers](laser/coherent-mephisto) | no card |  | [support](https://www.coherent.com/lasers/cw-solid-state/mephisto) |
| [Coherent OBIS LX/LS lasers](laser/coherent-obis) | [community](laser/coherent-obis/card.yaml) | USB, RS-232 | [manual](https://www.coherent.com/content/dam/coherent/site/en/resources/manuals/lasers/obis-lx-ls-operators-manual.pdf) |
| [Coherent Verdi DPSS lasers (G, V and C series)](laser/coherent-verdi) | no card |  | [support](https://www.coherent.com/lasers/cw-solid-state/verdi) |
| [HÜBNER Photonics Cobolt 04-01 / 06-01 / 08-01 series lasers](laser/hubner-cobolt) | no card | USB, RS-232 | [manual](https://hubner-photonics.com/wp-content/uploads/2023/11/D0136-P_Manual-Cobolt-06-01-Series_October_2023-1.pdf) |
| [IPG Photonics YLR fiber lasers](laser/ipg-ylr) | no card |  | [manual](https://stipgpkenticoprod.blob.core.windows.net/ipgpsoftware/YLR/YLR%20Laser%20Fieldbus%20Interface/Documents/DOCOXISCOMXX0002_IPG_YLR-YLPP_Series_Fieldbus_Spec.pdf) |
| [Light Conversion PHAROS femtosecond laser](laser/lightcon-pharos) | [community](laser/lightcon-pharos/card.yaml) | LAN, web API |  |
| [M Squared SolsTiS Ti:sapphire laser (ICE-BLOC)](laser/m2-solstis) | [community](laser/m2-solstis/card.yaml) | LAN |  |
| [NKT Photonics SuperK EXTREME / FIANIUM supercontinuum lasers](laser/nkt-superk) | no card | USB, LAN, RS-232 | [manual](https://lf.hamamatsu.com/wp-json/nktphotonics/v1/download/SuperK-EXTREME/SuperK%20EXTREME%20Product%20Guide.pdf) |
| [Spectra-Physics Mai Tai Ti:sapphire ultrafast laser](laser/spectra-physics-mai-tai) | no card | RS-232 | [manual](https://api.p1.mks.com/mam/celum/celum_assets/sp/resources/284A_Rev_G_Mai_Tai_Users_Manual.pdf) |
| [Vexlum VALO VECSEL lasers (VALO SF and VALO SHG)](laser/vexlum-vecsel) | no card |  | [support](https://vexlum.com/products/) |

## OPOs and OPAs

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [HÜBNER Photonics C-WAVE tunable CW OPO](parametric-source/hubner-c-wave) | no card |  | [support](https://hubner-photonics.com/products/lasers/tunable-lasers/c-wave/) |
| [Light Conversion ORPHEUS optical parametric amplifiers](parametric-source/lightcon-orpheus) | no card | USB, LAN, web API | [manual](https://lightconupdater.blob.core.windows.net/documentation/WinTopas4/index.html) |
| [Light Conversion TOPAS optical parametric amplifiers (TOPAS-Prime)](parametric-source/lightcon-topas) | no card | USB, LAN, web API | [manual](https://lightconupdater.blob.core.windows.net/documentation/WinTopas4/index.html) |

## Optical frequency combs

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Menlo Systems FC1500 optical frequency combs](frequency-comb/menlo-fc1500) | no card |  | [support](https://www.menlosystems.com/products/optical-frequency-combs/fc1500-uln-nova/) |
| [TOPTICA DFC difference frequency combs (DFC CORE and DFC CORE+)](frequency-comb/toptica-dfc) | no card | LAN | [support](https://www.toptica.com/products/frequency-combs/dfc) |

## Laser diode and TEC controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [MOGLabs DLC-202 diode laser controller](laser-driver/moglabs-dlc-202) | no card | USB, LAN | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/Laser-Electronics/MOGLabs_DLC_manual.pdf) |
| [PicoQuant PDL 800-D pulsed diode laser driver](laser-driver/picoquant-pdl-800) | no card |  | [manual](https://downloads.picoquant.com/manuals/PDL800-D_Manual.pdf) |
| [Thorlabs CLD1010 compact laser diode and TEC controller](laser-driver/thorlabs-cld1010) | no card | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/c/cl/cld/cld1015/doc-104674.pdf) |
| [Thorlabs ITC4000-series laser diode and TEC controllers](laser-driver/thorlabs-itc4000) | [community](laser-driver/thorlabs-itc4000/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/t/te/ted/ted4015/16407-d03.pdf) |
| [TOPTICA DLC pro diode laser controller](laser-driver/toptica-dlc-pro) | [draft](laser-driver/toptica-dlc-pro/card.yaml) | LAN, USB |  |

## Laser locking and stabilization

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [MOGLabs FSC fast servo controller](laser-lock/moglabs-fsc) | no card |  | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/Laser-Electronics/MOGLabs_FSC_manual.pdf) |
| [TOPTICA DigiLock 110 digital laser lock](laser-lock/toptica-digilock) | no card | USB, LAN | [manual](https://www.toptica.com/fileadmin/Editors_English/03_products/03_tunable_diode_lasers/04_control_electronics/02_laser_locking_electronics/04_DigiLock_110/toptica_digilock_manual.pdf) |
| [TOPTICA FALC pro fast analog laser lock (the FALC 110 has no computer control)](laser-lock/toptica-falc) | no card |  | [support](https://www.toptica.com/products/locking-driving-electronics/falc-pro) |
| [Vescent D2-125 laser servo](laser-lock/vescent-d2-125) | no card | analog | [manual](https://vescent-production-media.s3.us-west-2.amazonaws.com/files/67117c0f2897eecc14f41d25.pdf) |

## Wavelength meters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Bristol Instruments 671 / 771 / 871 wavelength meters](wavemeter/bristol-wavemeter) | no card | USB, LAN | [support](https://www.bristol-inst.com/wp-content/uploads/2023/09/Bristol-671-Series-Laser-Wavelength-Meter-Specifications.pdf) |
| [HighFinesse WS6 / WS7 / WS8 wavelength meters](wavemeter/highfinesse-wavemeter) | no card | USB | [support](https://www.highfinesse.com/en/support/downloads.html) |

## Also used here

- [Liquid Instruments Moku:Pro, Moku:Lab and Moku:Go](../electronics/fpga-instrument/liquid-instruments-moku), in electronics
- [Red Pitaya STEMlab boards (SCPI server) and the PyRPL lock software](../electronics/fpga-instrument/red-pitaya-stemlab), in electronics
