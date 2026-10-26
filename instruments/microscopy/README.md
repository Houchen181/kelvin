# Microscopy and diffraction

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Scanning probe and electron microscopes, optical tweezers and X-ray diffraction.

## SPM controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Asylum Research (Oxford Instruments) AFMs](spm-controller/asylum-afm) | no card | USB | [manual](https://afm.oxinst.com/assets/uploads/products/asylum/documents/MacroBuilder-Automating-AFM.pdf) |
| [Bruker Dimension AFMs (NanoScope software and NanoScope API)](spm-controller/bruker-afm) | no card | LAN | [support](https://www.bruker.com/en/products-and-solutions/microscopes/materials-afm/nanoscope-api.html) |
| [RHK Technology R9 SPM controller](spm-controller/rhk-r9) | no card | USB | [manual](https://rhk-tech.com/wp-content/uploads/2025/06/AN-7-RHK_R9_MATLAB_Scripting.pdf) |
| [SPECS Nanonis SPM controller (TCP programming interface)](spm-controller/specs-nanonis) | no card | LAN | [manual](https://raw.githubusercontent.com/SPECS-Zurich-GmbH/nanonis_spm/main/TCPProtocol_SPM.pdf) |

## Electron and ion microscopes

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [TESCAN SEM and FIB-SEM systems (SharkSEM remote-control API, Automation SDK)](electron-microscope/tescan-sharksem) | no card | LAN | [support](https://tescan.com/product-portfolio/add-ons/fib-sem-expert-pi-visualcoder) |
| [Thermo Fisher SEM and DualBeam (FIB-SEM) systems automated with AutoScript](electron-microscope/thermofisher-autoscript) | no card | LAN | [support](https://documents.thermofisher.com/TFS-Assets/MSD/Datasheets/autoscript-4-datasheet.pdf) |
| [ZEISS SEM and FIB-SEM systems (SmartSEM, Python scripting API)](electron-microscope/zeiss-sem) | no card | LAN | [support](https://www.zeiss.com/microscopy/en/products/sem-fib-sem/sem/geminisem-family.html) |

## Optical tweezers systems

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [JPK (Bruker) NanoTracker optical tweezers](optical-tweezers/jpk-nanotracker) | no card | analog | [support](https://www.bruker.com/en/products-and-solutions/microscopes/optical-tweezers/jpk-nanotracker-2.html) |
| [Impetux SENSOCELL optical tweezers](optical-tweezers/impetux-sensocell) | no card | USB | [support](https://impetux.com/sensocell-optical-tweezers/) |
| [LUMICKS C-Trap optical tweezers](optical-tweezers/lumicks-c-trap) | no card |  | [sign-in](https://help.lumicks.com/bluelake-api/) |

## X-ray diffractometers and Laue cameras

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Bruker D8 X-ray diffractometers (DIFFRAC.SUITE)](x-ray-diffractometer/bruker-d8) | no card | LAN | [support](https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/diffrac-suite-software/diffrac-measurement-center.html) |
| [Photonic Science Laue crystal orientation system](x-ray-diffractometer/photonic-science-laue) | no card | LAN | [support](https://photonicscience.com/products/laue-single-crystal-orientation-system-laue-family/) |
| [Rigaku SmartLab X-ray diffractometer (SmartLab Studio II, RAI)](x-ray-diffractometer/rigaku-smartlab) | no card | LAN | [support](https://rigaku.com/products/lablinc-studio/rai) |

## Also used here

- [ASI MS-2000 and Tiger stage controllers](../motion/motion-stage/asi-ms-2000), in motion
- [Prior ProScan III microscope stage controller](../motion/motion-stage/prior-proscan), in motion
