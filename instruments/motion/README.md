# Motion and positioning

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Piezo positioners and scanners, motorized stages, delay lines and rotation mounts.

## Piezo positioners and scanners

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [attocube AMC300 / AMC100 piezo positioner controller](positioner/attocube-amc) | no card | LAN, USB | [manual](https://raw.githubusercontent.com/attocube-systems/AMC-APIs/master/AMC_Interface_Manual_v1.5.1.pdf) |
| [attocube ANC300 piezo positioner controller](positioner/attocube-anc300) | [community](positioner/attocube-anc300/card.yaml) | USB, LAN |  |
| [attocube ANC350 closed-loop positioner controller](positioner/attocube-anc350) | [community](positioner/attocube-anc350/card.yaml) | USB |  |
| [Mad City Labs Nano-Drive piezo nanopositioning controller](positioner/mcl-nano-drive) | no card | USB, analog | [support](https://www.madcitylabs.com/nanodrive.html) |
| [PI piezo controllers with the GCS command set](positioner/pi-gcs-piezo) | [community](positioner/pi-gcs-piezo/card.yaml) | USB, LAN, RS-232 |  |
| [SmarAct MCS2 modular positioning controller](positioner/smaract-mcs2) | no card | USB, LAN | [owners](https://www.smaract.com/en/motion/products/control-systems-and-software-working/control-systems/mcs2) |
| [Thorlabs MDT693A / MDT694A piezo controllers](positioner/thorlabs-mdt69xa) | [community](positioner/thorlabs-mdt69xa/card.yaml) | USB |  |

## Motorized stages, delay lines and rotation mounts

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [ASI MS-2000 and Tiger stage controllers](motion-stage/asi-ms-2000) | no card | RS-232, USB | [manual](https://docs.asiimaging.com/command_quick_start) |
| [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](motion-stage/newport-conex-cc) | no card | USB | [manual](https://api.p1.mks.com/medias/sys_master/npresources/h91/hf3/10219689345054/CONEX-CC%20-%20Controller%20Documentation/CONEX-CC-Controller-Documentation.pdf) |
| [Newport ESP301 three-axis motion controller](motion-stage/newport-esp301) | no card | GPIB, USB, RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/images/images/hda/h3e/9117547069470/ESP301-User-s-Manual.pdf) |
| [Newport SMC100CC / SMC100PP single-axis motion controller](motion-stage/newport-smc100) | no card | RS-232, RS-485, USB | [manual](https://api.p1.mks.com/medias/sys_master/resources/hec/h2b/10211813294110/SMC100CC_and_SMC100PP_-_User_Manual/SMC100CC-and-SMC100PP-User-Manual.pdf) |
| [Newport XPS-D / XPS-RL universal high-performance motion controller](motion-stage/newport-xps) | no card | LAN | [manual](https://api.p1.mks.com/medias/sys_master/npresources/h3e/h82/10211812802590/XPS_Unified_-_Programmer_s_Manual/XPS-Unified-Programmer-s-Manual.pdf) |
| [Physik Instrumente C-863 Mercury DC motor controller](motion-stage/pi-c-863) | no card | USB, RS-232 | [sign-in](https://www.physikinstrumente.com/en/products/controllers-and-drivers/motion-controllers-drivers-for-linear-torque-stepper-dc-servo-motors/c-863-mercury-servo-controller-900606/) |
| [Prior ProScan III microscope stage controller](motion-stage/prior-proscan) | no card | RS-232, USB | [manual](https://www.prior.com/wp-content/uploads/2026/08/ProScanIII_EN_UK_Manual.pdf) |
| [Thorlabs K10CR1 motorized rotation mount](motion-stage/thorlabs-k10cr1) | no card | USB |  |
| [Thorlabs KDC101 K-Cube brushed DC servo motor controller](motion-stage/thorlabs-kdc101) | no card | USB |  |
