# Electronics and electrical measurement

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Sources, meters, lock-ins, preamplifiers, generators and data acquisition, the core of transport measurements.

## Source-measure units

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 2400-series SourceMeter](source-meter/keithley-2400) | [community](source-meter/keithley-2400/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2400S-900-01_K-Sep2011_User.pdf) |
| [Keithley 2450 / 2460 / 2461 / 2470 SourceMeter](source-meter/keithley-2450) | [community](source-meter/keithley-2450/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://download.tek.com/manual/2450-901-01E_Sept_2019_Ref.pdf) |
| [Keithley 2636B System SourceMeter SMU (2600B series)](source-meter/keithley-2636b) | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/2600BS-901-01F_2600B_Reference_Aug2021.pdf) |
| [Keithley 6430 sub-femtoamp remote SourceMeter](source-meter/keithley-6430) | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6430-901-01G_Jan_2021_Ref-2.pdf) |
| [Keysight B2900A/B series precision source-measure units](source-meter/keysight-b2900) | [community](source-meter/keysight-b2900/card.yaml) | USB-TMC, LAN, GPIB |  |

## DC voltage sources and low-noise DACs

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Basel Precision Instruments LNHR DAC II (SP1060) 12/24-channel low-noise DAC](voltage-source/basel-lnhr-dac) | no card | LAN, RS-232 | [manual](https://www.baspi.ch/_files/ugd/68eb62_ed0cc567cc26466382f596cf9190b4ac.pdf) |
| [QDevil QDAC-II 24-channel low-noise DAC](voltage-source/qdevil-qdac-ii) | no card | USB, LAN | [manual](https://docs.quantum-machines.co/latest/docs/Hardware/assets/QDAC-II%20Compact%20Command%20Reference.pdf) |
| [SRS SIM928 isolated voltage source](voltage-source/srs-sim928) | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM928m.pdf) |
| [Yokogawa 7651 programmable DC source](voltage-source/yokogawa-7651) | no card | GPIB | [manual](https://cdn.tmi.yokogawa.com/IM7651-01E.is.pdf) |
| [Yokogawa GS200 / GS210 DC voltage and current source](voltage-source/yokogawa-gs200) | [community](voltage-source/yokogawa-gs200/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://web-material3.yokogawa.com/IMGS210-01EN.pdf) |

## Precision AC and DC current sources

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 6221 AC and DC current source](current-source/keithley-6221) | no card | GPIB, RS-232, LAN | [manual](https://download.tek.com/manual/622x-901-01%20(C%20-%20Oct%202008)(Ref).pdf) |

## Digital multimeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [HP / Agilent / Keysight 34401A 6.5-digit multimeter](multimeter/hp-34401a) | no card | GPIB, RS-232 | [manual](https://www.keysight.com/us/en/assets/9018-01063/user-manuals/9018-01063.pdf) |
| [Keithley 2000 6½-digit multimeter](multimeter/keithley-2000) | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/2000-900_J-Aug2010_User.pdf) |
| [Keithley 2700 / 2701 / 2750 multimeter and data acquisition systems](multimeter/keithley-2700) | no card | GPIB, RS-232, LAN | [manual](https://download.tek.com/manual/2700-900-01K_Feb_2016.pdf) |
| [Keithley DMM6500 6½-digit bench multimeter](multimeter/keithley-dmm6500) | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/DMM6500-901-01C_April_2026_Ref.pdf) |
| [Keysight Truevolt 34460A / 34461A / 34465A / 34470A multimeters](multimeter/keysight-34465a) | [community](multimeter/keysight-34465a/card.yaml) | USB-TMC, LAN, GPIB |  |
| [SRS SIM970 quad digital voltmeter](multimeter/srs-sim970) | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM970m.pdf) |

## Nanovoltmeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 2182A nanovoltmeter](nanovoltmeter/keithley-2182a) | [community](nanovoltmeter/keithley-2182a/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2182A-900-01C_July_2022_User.pdf) |

## Electrometers and picoammeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 6485 / 6487 picoammeters](electrometer/keithley-6485) | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6487-900-01(C-Mar2011)(User).pdf) |
| [Keithley 6517B electrometer / high-resistance meter](electrometer/keithley-6517b) | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6517B-901-01F_Jan2024_Ref.pdf) |

## Lock-in amplifiers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [NF Corporation LI5650 / LI5660 digital lock-in amplifiers](lock-in/nf-li5660) | no card | USB, GPIB, RS-232, LAN | [manual](https://www.nfcorp.co.jp/english/doc_portal/download/pdf/manual/mi/EN_LI5655_LI5660_RemoteControl.pdf) |
| [Signal Recovery 7270 DSP lock-in amplifier](lock-in/signal-recovery-7270) | no card | LAN, USB, RS-232 | [sign-in](https://www.ameteksi.com/-/media/ameteksi/download_links/documentations/supportcenter/signalrecovery/instruction_manuals/197852-a-mnl-f.pdf) |
| [Stanford Research SR830 DSP lock-in amplifier](lock-in/srs-sr830) | [community](lock-in/srs-sr830/card.yaml) | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR830m.pdf) |
| [Stanford Research Systems SR844 RF lock-in amplifier](lock-in/srs-sr844) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf) |
| [SRS SR850 DSP lock-in amplifier](lock-in/srs-sr850) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR850m.pdf) |
| [Stanford Research SR860 / SR865A lock-in amplifiers](lock-in/srs-sr860) | [community](lock-in/srs-sr860/card.yaml) | GPIB, RS-232, USB-TMC, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR860m.pdf) |
| [SynkTek MCL1-540 multichannel lock-in amplifier](lock-in/synktek-mcl1-540) | no card | LAN, USB | [manual](https://www.synktek.com/wp-content/uploads/2023/01/manual.pdf) |
| [Zurich Instruments HF2LI 50 MHz lock-in amplifier](lock-in/zhinst-hf2li) | no card | USB | [manual](https://docs.zhinst.com/hf2_user_manual/programming.html) |
| [Zurich Instruments MFLI 500 kHz / 5 MHz lock-in amplifier](lock-in/zhinst-mfli) | [community](lock-in/zhinst-mfli/card.yaml) | USB, LAN | [manual](https://docs.zhinst.com/pdf/ziMFLI_UserManual.pdf) |
| [Zurich Instruments UHFLI 600 MHz lock-in amplifier](lock-in/zhinst-uhfli) | no card | USB, LAN | [manual](https://docs.zhinst.com/uhf_user_manual/nodedoc.html) |

## Voltage and current preamplifiers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [FEMTO DLPCA-200 variable-gain current amplifier (with LUCI-10 USB interface)](preamp/femto-dlpca-200) | no card | USB, analog | [manual](https://www.femto.de/images/pdf-dokumente/de-dlpca-200.pdf) |
| [NF Corporation CA5351 programmable current amplifier](preamp/nf-ca5351) | no card | LAN, GPIB, USB | [manual](https://www.nfcorp.co.jp/english/doc_portal/download/pdf/manual/mi/EN_CA5351_InstructionManual_001.pdf) |
| [Stanford Research SR560 low-noise voltage preamplifier](preamp/srs-sr560) | [community](preamp/srs-sr560/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR560m.pdf) |
| [Stanford Research SR570 low-noise current preamplifier](preamp/srs-sr570) | [community](preamp/srs-sr570/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR570m.pdf) |

## AC resistance bridges

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Lake Shore Model 370 AC resistance bridge](resistance-bridge/lakeshore-370) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/370_manual.pdf) |
| [Lake Shore Model 372 AC resistance bridge and temperature controller](resistance-bridge/lakeshore-372) | no card | GPIB, USB, LAN | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/372_manual.pdf) |
| [Picowatt AVS-47B AC resistance bridge](resistance-bridge/picowatt-avs-47) | no card | GPIB, RS-232, USB | [manual](https://www.picowatt.fi/support/avs47bmanual_20180424_1101_1110.pdf) |
| [SRS SIM921 AC resistance bridge](resistance-bridge/srs-sim921) | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM921m.pdf) |

## Function generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Agilent / Keysight 33220A function / arbitrary waveform generator](function-generator/keysight-33220a) | no card | GPIB, USB-TMC, LAN | [manual](https://www.keysight.com/us/en/assets/9018-04437/user-manuals/9018-04437.pdf) |
| [Keysight 33500B / 33600A waveform generators](function-generator/keysight-33500b) | [community](function-generator/keysight-33500b/card.yaml) | USB-TMC, LAN, GPIB |  |
| [SRS DS345 function generator](function-generator/srs-ds345) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DS345m.pdf) |

## Arbitrary waveform generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight M3202A PXIe arbitrary waveform generator](awg/keysight-m3202a) | no card | PXIe | [sign-in](https://www.keysight.com/us/en/assets/9018-04448/user-manuals/9018-04448.pdf) |
| [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](awg/qick-rfsoc) | [community](awg/qick-rfsoc/card.yaml) | LAN |  |
| [Rigol DG1000Z function and arbitrary waveform generators](awg/rigol-dg1000z) | [community](awg/rigol-dg1000z/card.yaml) | USB-TMC, LAN | [manual](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0493/1/-/-/-/-/DG1000Z%20Programming%20Guide.pdf) |
| [Spectrum Instrumentation M4i.66xx arbitrary waveform generator cards](awg/spectrum-m4i-66xx) | no card | PCIe | [manual](https://spectrum-instrumentation.com/dl/m4i_m4x_66xx_96xx_manual_english.pdf) |
| [Tektronix AWG5200 series arbitrary waveform generator](awg/tektronix-awg5200) | no card | LAN, USB-TMC, GPIB | [manual](https://download.tek.com/manual/AWG5200-Programmer-Manual-077133700-RevA.pdf) |
| [Zurich Instruments HDAWG arbitrary waveform generator](awg/zhinst-hdawg) | no card | USB, LAN | [manual](https://docs.zhinst.com/hdawg_user_manual/index.html) |

## Oscilloscopes and digitizers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [AlazarTech ATS9870 8-bit 1 GS/s PCIe waveform digitizer](oscilloscope/alazartech-ats9870) | no card | PCIe | [manual](https://docs.alazartech.com/ats-sdk-user-guide/latest/) |
| [Keysight InfiniiVision 3000 X-Series oscilloscopes](oscilloscope/keysight-dsox3000) | no card | LAN, USB-TMC, GPIB | [manual](https://www.keysight.com/us/en/assets/9018-06894/programming-guides/9018-06894.pdf) |
| [Pico Technology PicoScope USB oscilloscopes](oscilloscope/pico-picoscope) | no card | USB | [manual](https://www.picotech.com/download/manuals/picoscope-6000-series-a-api-programmers-guide.pdf) |
| [Tektronix 5 Series MSO mixed signal oscilloscopes](oscilloscope/tektronix-mso5) | no card | LAN, USB-TMC | [manual](https://download.tek.com/manual/4-5-6-Series-MSO_Programmer_077189805.pdf) |

## Data acquisition devices

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [NI DAQ devices through NI-DAQmx (USB-600x, USB-62xx, PCIe/PXIe-63xx, cDAQ)](daq/ni-daqmx) | [community](daq/ni-daqmx/card.yaml) | USB, PCIe, PXIe |  |

## LCR meters and impedance analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight E4980A precision LCR meter](lcr-meter/keysight-e4980a) | no card | GPIB, USB-TMC, LAN | [manual](https://www.keysight.com/us/en/assets/9018-05655/user-manuals/9018-05655.pdf) |
| [Solartron 1260A impedance/gain-phase analyzer](lcr-meter/solartron-1260) | no card | GPIB | [sign-in](https://www.ameteksi.com/-/media/ameteksi/download_links/documentations/supportcenter/solartonanalytical/product-manuals/1260a-impedance-analyzer-ea.pdf) |
| [Zurich Instruments MFIA impedance analyzer](lcr-meter/zhinst-mfia) | no card | USB, LAN | [manual](https://docs.zhinst.com/mfia_user_manual/) |

## Capacitance bridges

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Andeen-Hagerling AH 2700A ultra-precision capacitance bridge](capacitance-bridge/andeen-hagerling-ah2700a) | no card | GPIB, RS-232 | [support](https://www.andeen-hagerling.com/ah2700a.htm) |

## DC power supplies

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Delta Elektronika SM series programmable DC power supplies](power-supply/delta-elektronika-sm) | no card | analog, RS-232, LAN, GPIB | [manual](https://www.deltaelektronika.com/sites/default/files/2025-05/PSC-232_prod-manual_V202503.pdf) |
| [Keysight E36300 series triple-output programmable DC power supplies](power-supply/keysight-e36300) | no card | USB-TMC, LAN, GPIB | [manual](https://www.keysight.com/us/en/assets/9018-04577/programming-guides/9018-04577.pdf) |
| [TDK-Lambda Genesys programmable DC power supplies](power-supply/tdk-lambda-genesys) | no card | RS-232, RS-485, GPIB, USB, LAN |  |

## Semiconductor parameter analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 4200A-SCS parameter analyzer](parameter-analyzer/keithley-4200a) | no card | GPIB, LAN | [manual](https://download.tek.com/manual/4200A-KXCI-907-01F_Sept2026.pdf) |
| [Keysight B1500A semiconductor device parameter analyzer](parameter-analyzer/keysight-b1500a) | no card | GPIB | [manual](https://www.keysight.com/us/en/assets/9018-01851/programming-guides/9018-01851.pdf) |

## Switch matrices and multiplexers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 707B / 708B switching matrix](switch-matrix/keithley-707b) | no card | GPIB, LAN, RS-232 | [manual](https://download.tek.com/manual/707B-901-01C_Jan_2025_Ref.pdf) |

## FFT and dynamic signal analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [SRS SR1 audio analyzer](signal-analyzer/srs-sr1) | no card | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR1bm.pdf) |
| [SRS SR785 dynamic signal analyzer](signal-analyzer/srs-sr785) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR785m.pdf) |

## Ferroelectric testers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [aixACCT TF Analyzer ferroelectric and piezoelectric testers](ferroelectric-tester/aixacct-tf-analyzer) | no card |  | [support](https://www.aixacct.com/en/testsysteme/tf-analyzer-family/) |
| [Radiant Technologies Precision ferroelectric testers](ferroelectric-tester/radiant-precision) | no card |  | [support](https://www.ferrodevices.com/) |

## PID and servo controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [SRS SIM960 analog PID controller](pid-controller/srs-sim960) | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM960m.pdf) |

## FPGA multi-instruments

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Liquid Instruments Moku:Pro, Moku:Lab and Moku:Go](fpga-instrument/liquid-instruments-moku) | no card | USB, LAN, web API | [manual](https://apis.liquidinstruments.com/api/) |
| [Red Pitaya STEMlab boards (SCPI server) and the PyRPL lock software](fpga-instrument/red-pitaya-stemlab) | no card | LAN | [manual](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/scpi.html) |

## Instrument mainframes

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [SRS SIM900 mainframe](mainframe/srs-sim900) | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM900m.pdf) |
