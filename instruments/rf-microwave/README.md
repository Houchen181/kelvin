# RF and microwave

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Signal generators, network and spectrum analyzers, acousto-optic drivers and qubit controllers.

## RF and microwave signal generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight E8257D PSG analog signal generator](microwave-source/keysight-e8257d) | no card | GPIB, LAN, RS-232 | [manual](https://www.keysight.com/us/en/assets/9018-04961/installation-guides/9018-04961.pdf) |
| [Keysight MXG N5183B microwave signal generator](microwave-source/keysight-n5183b) | [community](microwave-source/keysight-n5183b/card.yaml) | USB-TMC, LAN, GPIB | [manual](https://www.keysight.com/content/dam/keysight/en/doc/gate/programming-guides/9018-03690.pdf) |
| [Rohde & Schwarz SGS100A SGMA RF source](microwave-source/rs-sgs100a) | no card | LAN, USB-TMC, PCIe | [manual](https://www.rohde-schwarz.com/webhelp/SGS100A_HTML_UserManual_en/SGS100A_HTML_UserManual_en.htm) |
| [Rohde & Schwarz SMB100A RF and microwave signal generator](microwave-source/rs-smb100a) | [community](microwave-source/rs-smb100a/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_manuals/dl_user_manual/SMB100A_OperatingManual_en_23.pdf) |
| [Stanford Research SG380-series RF signal generators](microwave-source/srs-sg384) | [community](microwave-source/srs-sg384/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SG380m.pdf) |
| [Windfreak SynthHD dual-channel microwave generator](microwave-source/windfreak-synthhd) | [draft](microwave-source/windfreak-synthhd/card.yaml) | USB | [manual](https://windfreaktech.com/wp-content/uploads/2016/12/WFT_SerialProgramming_API_10b.pdf) |

## Vector network analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Copper Mountain 2-port USB VNAs (S5048, S5065, M5180 and similar) via the S2VNA software](vna/copper-mountain-s2vna) | no card | USB, LAN | [manual](https://coppermountaintech.com/wp-content/uploads/2025/04/S2VNA-Operating-and-Programming-Manual.pdf) |
| [Keysight E5071C ENA vector network analyzer](vna/keysight-e5071c) | no card | GPIB, USB-TMC, LAN | [manual](https://helpfiles.keysight.com/csg/e5071c/programming/remote_control/remote_control.htm) |
| [Keysight E5080B ENA vector network analyzer](vna/keysight-e5080b) | no card | GPIB, USB-TMC, LAN | [manual](https://helpfiles.keysight.com/csg/e5080b/Programming/Programming_Guide.htm) |
| [Rohde & Schwarz ZNB vector network analyzer](vna/rs-znb) | no card | GPIB, USB-TMC, LAN | [manual](https://www.rohde-schwarz.com/webhelp/ZNB_HTML_UserManual_en/ZNB_HTML_UserManual_en.htm) |

## Spectrum and signal analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight N9020B MXA signal analyzer (X-Series)](spectrum-analyzer/keysight-n9020b) | no card | GPIB, USB-TMC, LAN | [sign-in](https://www.keysight.com/us/en/assets/9018-02192/programming-guides/9018-02192.pdf) |

## AOM and EOM drivers, DDS synthesizers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [MOGLabs XRF / ARF / QRF agile RF synthesizers](aom-driver/moglabs-xrf) | [community](aom-driver/moglabs-xrf/card.yaml) | USB, LAN | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/RF-generators-synthesizers/MOGLabs_XRF_manual.pdf) |
| [Novatech 409B four-channel DDS signal generator](aom-driver/novatech-409b) | [community](aom-driver/novatech-409b/card.yaml) | RS-232 | [manual](https://www.novatechsales.com/docs/409b_man.pdf) |

## Qubit control systems

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Quantum Machines OPX+ / OPX1000 quantum controller (QUA)](quantum-controller/quantum-machines-opx) | no card | LAN | [manual](https://docs.quantum-machines.co/latest/) |
| [Zurich Instruments SHFQC qubit controller](quantum-controller/zhinst-shfqc) | no card | USB, LAN | [manual](https://docs.zhinst.com/shfqc_user_manual/index.html) |

## Also used here

- [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](../electronics/awg/qick-rfsoc), in electronics
- [Stanford Research Systems SR844 RF lock-in amplifier](../electronics/lock-in/srs-sr844), in electronics
