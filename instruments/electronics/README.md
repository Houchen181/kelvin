# Electronics and electrical measurement

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Sources, meters, lock-ins, preamplifiers, generators and data acquisition, the core of transport measurements.

## Source-measure units

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 2400-series SourceMeter](source-meter/keithley-2400) | [community](source-meter/keithley-2400/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2400S-900-01_K-Sep2011_User.pdf) |
| [Keithley 2450 / 2460 / 2461 / 2470 SourceMeter](source-meter/keithley-2450) | [community](source-meter/keithley-2450/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://download.tek.com/manual/2450-901-01E_Sept_2019_Ref.pdf) |
| [Keithley 2636B System SourceMeter SMU (2600B series)](source-meter/keithley-2636b) | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/2600BS-901-01F_2600B_Reference_Aug2021.pdf) |
| [Keysight B2900A/B series precision source-measure units](source-meter/keysight-b2900) | [community](source-meter/keysight-b2900/card.yaml) | USB-TMC, LAN, GPIB |  |

## DC voltage sources and low-noise DACs

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Basel Precision Instruments LNHR DAC II (SP1060) 12/24-channel low-noise DAC](voltage-source/basel-lnhr-dac) | no card | LAN, RS-232 | [manual](https://www.baspi.ch/_files/ugd/68eb62_ed0cc567cc26466382f596cf9190b4ac.pdf) |
| [QDevil QDAC-II 24-channel low-noise DAC](voltage-source/qdevil-qdac-ii) | no card | USB, LAN | [manual](https://docs.quantum-machines.co/latest/docs/Hardware/assets/QDAC-II%20Compact%20Command%20Reference.pdf) |
| [Yokogawa GS200 / GS210 DC voltage and current source](voltage-source/yokogawa-gs200) | [community](voltage-source/yokogawa-gs200/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://web-material3.yokogawa.com/IMGS210-01EN.pdf) |

## Precision AC and DC current sources

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 6221 AC and DC current source](current-source/keithley-6221) | no card | GPIB, RS-232, LAN | [manual](https://download.tek.com/manual/622x-901-01%20(C%20-%20Oct%202008)(Ref).pdf) |

## Digital multimeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 2000 6½-digit multimeter](multimeter/keithley-2000) | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/2000-900_J-Aug2010_User.pdf) |
| [Keithley DMM6500 6½-digit bench multimeter](multimeter/keithley-dmm6500) | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/DMM6500-901-01C_April_2026_Ref.pdf) |
| [Keysight Truevolt 34460A / 34461A / 34465A / 34470A multimeters](multimeter/keysight-34465a) | [community](multimeter/keysight-34465a/card.yaml) | USB-TMC, LAN, GPIB |  |

## Nanovoltmeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 2182A nanovoltmeter](nanovoltmeter/keithley-2182a) | [community](nanovoltmeter/keithley-2182a/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2182A-900-01C_July_2022_User.pdf) |

## Electrometers and picoammeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keithley 6517B electrometer / high-resistance meter](electrometer/keithley-6517b) | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6517B-901-01F_Jan2024_Ref.pdf) |

## Lock-in amplifiers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Signal Recovery 7270 DSP lock-in amplifier](lock-in/signal-recovery-7270) | no card | LAN, USB, RS-232 | [sign-in](https://www.ameteksi.com/-/media/ameteksi/download_links/documentations/supportcenter/signalrecovery/instruction_manuals/197852-a-mnl-f.pdf) |
| [Stanford Research SR830 DSP lock-in amplifier](lock-in/srs-sr830) | [community](lock-in/srs-sr830/card.yaml) | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR830m.pdf) |
| [Stanford Research Systems SR844 RF lock-in amplifier](lock-in/srs-sr844) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf) |
| [Stanford Research SR860 / SR865A lock-in amplifiers](lock-in/srs-sr860) | [community](lock-in/srs-sr860/card.yaml) | GPIB, RS-232, USB-TMC, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR860m.pdf) |
| [Zurich Instruments HF2LI 50 MHz lock-in amplifier](lock-in/zhinst-hf2li) | no card | USB | [manual](https://docs.zhinst.com/hf2_user_manual/programming.html) |
| [Zurich Instruments MFLI 500 kHz / 5 MHz lock-in amplifier](lock-in/zhinst-mfli) | [community](lock-in/zhinst-mfli/card.yaml) | USB, LAN | [manual](https://docs.zhinst.com/pdf/ziMFLI_UserManual.pdf) |
| [Zurich Instruments UHFLI 600 MHz lock-in amplifier](lock-in/zhinst-uhfli) | no card | USB, LAN | [manual](https://docs.zhinst.com/uhf_user_manual/nodedoc.html) |

## Voltage and current preamplifiers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Stanford Research SR560 low-noise voltage preamplifier](preamp/srs-sr560) | [community](preamp/srs-sr560/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR560m.pdf) |
| [Stanford Research SR570 low-noise current preamplifier](preamp/srs-sr570) | [community](preamp/srs-sr570/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR570m.pdf) |

## AC resistance bridges

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Lake Shore Model 372 AC resistance bridge and temperature controller](resistance-bridge/lakeshore-372) | no card | GPIB, USB, LAN | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/372_manual.pdf) |

## Function generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight 33500B / 33600A waveform generators](function-generator/keysight-33500b) | [community](function-generator/keysight-33500b/card.yaml) | USB-TMC, LAN, GPIB |  |

## Arbitrary waveform generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](awg/qick-rfsoc) | [community](awg/qick-rfsoc/card.yaml) | LAN |  |
| [Rigol DG1000Z function and arbitrary waveform generators](awg/rigol-dg1000z) | [community](awg/rigol-dg1000z/card.yaml) | USB-TMC, LAN | [manual](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0493/1/-/-/-/-/DG1000Z%20Programming%20Guide.pdf) |
| [Tektronix AWG5200 series arbitrary waveform generator](awg/tektronix-awg5200) | no card | LAN, USB-TMC, GPIB | [manual](https://download.tek.com/manual/AWG5200-Programmer-Manual-077133700-RevA.pdf) |
| [Zurich Instruments HDAWG arbitrary waveform generator](awg/zhinst-hdawg) | no card | USB, LAN | [manual](https://docs.zhinst.com/hdawg_user_manual/index.html) |

## Data acquisition devices

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [NI DAQ devices through NI-DAQmx (USB-600x, USB-62xx, PCIe/PXIe-63xx, cDAQ)](daq/ni-daqmx) | [community](daq/ni-daqmx/card.yaml) | USB, PCIe, PXIe |  |

## Semiconductor parameter analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight B1500A semiconductor device parameter analyzer](parameter-analyzer/keysight-b1500a) | no card | GPIB | [manual](https://www.keysight.com/us/en/assets/9018-01851/programming-guides/9018-01851.pdf) |
