# Catalog

<!-- Written by `python tools/kic.py index` from the files in this repository; edit those, not this. -->

280 instruments, 49 of them with a Kelvin card; 29 experiments; 10 lab configs.

**Card status.** *community*: written from the maker's manual, not yet checked on hardware. *lab-verified*: checked on hardware by a lab (see the instrument's `verified` list). *draft*: Kelvin keeps its outputs simulated until someone checks it. *no card*: Kelvin writes one from the manual when it finds the instrument.

- [Instruments by category](#instruments-by-category)
- [Experiments](#experiments)
- [Lab configs](#lab-configs)
- [Wanted cards](#wanted-cards)
- [Makers](#makers)

## Instruments by category

- [Electronics and electrical measurement](#electronics-and-electrical-measurement) (70)
- [RF and microwave](#rf-and-microwave) (29)
- [Timing, pulses and photon counting](#timing-pulses-and-photon-counting) (16)
- [Lasers and laser control](#lasers-and-laser-control) (31)
- [Optics, detection and spectroscopy](#optics-detection-and-spectroscopy) (40)
- [Quantum optics and single photons](#quantum-optics-and-single-photons) (15)
- [Motion and positioning](#motion-and-positioning) (16)
- [Cryogenics, vacuum and sample environment](#cryogenics-vacuum-and-sample-environment) (36)
- [Magnets and field measurement](#magnets-and-field-measurement) (11)
- [Microscopy and diffraction](#microscopy-and-diffraction) (15)
- [Spectroscopy systems](#spectroscopy-systems) (7)
- [Materials synthesis and fabrication](#materials-synthesis-and-fabrication) (8)

### Electronics and electrical measurement

Sources, meters, lock-ins, preamplifiers, generators and data acquisition, the core of transport measurements.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Keithley 2400-series SourceMeter](instruments/electronics/source-meter/keithley-2400/instrument.yaml) | source-meter | [community](instruments/electronics/source-meter/keithley-2400/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2400S-900-01_K-Sep2011_User.pdf) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) +3 |
| [Keithley 2450 / 2460 / 2461 / 2470 SourceMeter](instruments/electronics/source-meter/keithley-2450/instrument.yaml) | source-meter | [community](instruments/electronics/source-meter/keithley-2450/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://download.tek.com/manual/2450-901-01E_Sept_2019_Ref.pdf) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml) +3 |
| [Keithley 2636B System SourceMeter SMU (2600B series)](instruments/electronics/source-meter/keithley-2636b/instrument.yaml) | source-meter | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/2600BS-901-01F_2600B_Reference_Aug2021.pdf) | [Current-voltage characteristics](experiments/transport/iv-curve.yaml) |
| [Keithley 6430 sub-femtoamp remote SourceMeter](instruments/electronics/source-meter/keithley-6430/instrument.yaml) | source-meter | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6430-901-01G_Jan_2021_Ref-2.pdf) |  |
| [Keysight B2900A/B series precision source-measure units](instruments/electronics/source-meter/keysight-b2900/instrument.yaml) | source-meter | [community](instruments/electronics/source-meter/keysight-b2900/card.yaml) | USB-TMC, LAN, GPIB |  | [Field-effect gate sweep](experiments/transport/gate-sweep.yaml), [Current-voltage characteristics](experiments/transport/iv-curve.yaml) |
| [Basel Precision Instruments LNHR DAC II (SP1060) 12/24-channel low-noise DAC](instruments/electronics/voltage-source/basel-lnhr-dac/instrument.yaml) | voltage-source | no card | LAN, RS-232 | [manual](https://www.baspi.ch/_files/ugd/68eb62_ed0cc567cc26466382f596cf9190b4ac.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [QDevil QDAC-II 24-channel low-noise DAC](instruments/electronics/voltage-source/qdevil-qdac-ii/instrument.yaml) | voltage-source | no card | USB, LAN | [manual](https://docs.quantum-machines.co/latest/docs/Hardware/assets/QDAC-II%20Compact%20Command%20Reference.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml), [Field-effect gate sweep](experiments/transport/gate-sweep.yaml) +1 |
| [SRS SIM928 isolated voltage source](instruments/electronics/voltage-source/srs-sim928/instrument.yaml) | voltage-source | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM928m.pdf) |  |
| [Yokogawa 7651 programmable DC source](instruments/electronics/voltage-source/yokogawa-7651/instrument.yaml) | voltage-source | no card | GPIB | [manual](https://cdn.tmi.yokogawa.com/IM7651-01E.is.pdf) |  |
| [Yokogawa GS200 / GS210 DC voltage and current source](instruments/electronics/voltage-source/yokogawa-gs200/instrument.yaml) | voltage-source | [community](instruments/electronics/voltage-source/yokogawa-gs200/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://web-material3.yokogawa.com/IMGS210-01EN.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Keithley 6221 AC and DC current source](instruments/electronics/current-source/keithley-6221/instrument.yaml) | current-source | no card | GPIB, RS-232, LAN | [manual](https://download.tek.com/manual/622x-901-01%20(C%20-%20Oct%202008)(Ref).pdf) | [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml) |
| [HP / Agilent / Keysight 34401A 6.5-digit multimeter](instruments/electronics/multimeter/hp-34401a/instrument.yaml) | multimeter | no card | GPIB, RS-232 | [manual](https://www.keysight.com/us/en/assets/9018-01063/user-manuals/9018-01063.pdf) |  |
| [Keithley 2000 6½-digit multimeter](instruments/electronics/multimeter/keithley-2000/instrument.yaml) | multimeter | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/2000-900_J-Aug2010_User.pdf) | [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Keithley 2700 / 2701 / 2750 multimeter and data acquisition systems](instruments/electronics/multimeter/keithley-2700/instrument.yaml) | multimeter | no card | GPIB, RS-232, LAN | [manual](https://download.tek.com/manual/2700-900-01K_Feb_2016.pdf) |  |
| [Keithley DMM6500 6½-digit bench multimeter](instruments/electronics/multimeter/keithley-dmm6500/instrument.yaml) | multimeter | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/DMM6500-901-01C_April_2026_Ref.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Keysight Truevolt 34460A / 34461A / 34465A / 34470A multimeters](instruments/electronics/multimeter/keysight-34465a/instrument.yaml) | multimeter | [community](instruments/electronics/multimeter/keysight-34465a/card.yaml) | USB-TMC, LAN, GPIB |  | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) +1 |
| [SRS SIM970 quad digital voltmeter](instruments/electronics/multimeter/srs-sim970/instrument.yaml) | multimeter | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM970m.pdf) |  |
| [Keithley 2182A nanovoltmeter](instruments/electronics/nanovoltmeter/keithley-2182a/instrument.yaml) | nanovoltmeter | [community](instruments/electronics/nanovoltmeter/keithley-2182a/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2182A-900-01C_July_2022_User.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml), [Current-voltage characteristics](experiments/transport/iv-curve.yaml) |
| [Keithley 6485 / 6487 picoammeters](instruments/electronics/electrometer/keithley-6485/instrument.yaml) | electrometer | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6487-900-01(C-Mar2011)(User).pdf) |  |
| [Keithley 6517B electrometer / high-resistance meter](instruments/electronics/electrometer/keithley-6517b/instrument.yaml) | electrometer | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6517B-901-01F_Jan2024_Ref.pdf) |  |
| [NF Corporation LI5650 / LI5660 digital lock-in amplifiers](instruments/electronics/lock-in/nf-li5660/instrument.yaml) | lock-in | no card | USB, GPIB, RS-232, LAN | [manual](https://www.nfcorp.co.jp/english/doc_portal/download/pdf/manual/mi/EN_LI5655_LI5660_RemoteControl.pdf) |  |
| [Signal Recovery 7270 DSP lock-in amplifier](instruments/electronics/lock-in/signal-recovery-7270/instrument.yaml) | lock-in | no card | LAN, USB, RS-232 | [sign-in](https://www.ameteksi.com/-/media/ameteksi/download_links/documentations/supportcenter/signalrecovery/instruction_manuals/197852-a-mnl-f.pdf) | [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [Stanford Research SR830 DSP lock-in amplifier](instruments/electronics/lock-in/srs-sr830/instrument.yaml) | lock-in | [community](instruments/electronics/lock-in/srs-sr830/card.yaml) | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR830m.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml) +11 |
| [Stanford Research Systems SR844 RF lock-in amplifier](instruments/electronics/lock-in/srs-sr844/instrument.yaml) | lock-in | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf) |  |
| [SRS SR850 DSP lock-in amplifier](instruments/electronics/lock-in/srs-sr850/instrument.yaml) | lock-in | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR850m.pdf) |  |
| [Stanford Research SR860 / SR865A lock-in amplifiers](instruments/electronics/lock-in/srs-sr860/instrument.yaml) | lock-in | [community](instruments/electronics/lock-in/srs-sr860/card.yaml) | GPIB, RS-232, USB-TMC, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR860m.pdf) | [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) +8 |
| [SynkTek MCL1-540 multichannel lock-in amplifier](instruments/electronics/lock-in/synktek-mcl1-540/instrument.yaml) | lock-in | no card | LAN, USB | [manual](https://www.synktek.com/wp-content/uploads/2023/01/manual.pdf) |  |
| [Zurich Instruments HF2LI 50 MHz lock-in amplifier](instruments/electronics/lock-in/zhinst-hf2li/instrument.yaml) | lock-in | no card | USB | [manual](https://docs.zhinst.com/hf2_user_manual/programming.html) |  |
| [Zurich Instruments MFLI 500 kHz / 5 MHz lock-in amplifier](instruments/electronics/lock-in/zhinst-mfli/instrument.yaml) | lock-in | [community](instruments/electronics/lock-in/zhinst-mfli/card.yaml) | USB, LAN | [manual](https://docs.zhinst.com/pdf/ziMFLI_UserManual.pdf) | [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) +7 |
| [Zurich Instruments UHFLI 600 MHz lock-in amplifier](instruments/electronics/lock-in/zhinst-uhfli/instrument.yaml) | lock-in | no card | USB, LAN | [manual](https://docs.zhinst.com/uhf_user_manual/nodedoc.html) |  |
| [FEMTO DLPCA-200 variable-gain current amplifier (with LUCI-10 USB interface)](instruments/electronics/preamp/femto-dlpca-200/instrument.yaml) | preamp | no card | USB, analog | [manual](https://www.femto.de/images/pdf-dokumente/de-dlpca-200.pdf) |  |
| [NF Corporation CA5351 programmable current amplifier](instruments/electronics/preamp/nf-ca5351/instrument.yaml) | preamp | no card | LAN, GPIB, USB | [manual](https://www.nfcorp.co.jp/english/doc_portal/download/pdf/manual/mi/EN_CA5351_InstructionManual_001.pdf) |  |
| [Stanford Research SR560 low-noise voltage preamplifier](instruments/electronics/preamp/srs-sr560/instrument.yaml) | preamp | [community](instruments/electronics/preamp/srs-sr560/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR560m.pdf) | [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [Stanford Research SR570 low-noise current preamplifier](instruments/electronics/preamp/srs-sr570/instrument.yaml) | preamp | [community](instruments/electronics/preamp/srs-sr570/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR570m.pdf) | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Lake Shore Model 370 AC resistance bridge](instruments/electronics/resistance-bridge/lakeshore-370/instrument.yaml) | resistance-bridge | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/370_manual.pdf) |  |
| [Lake Shore Model 372 AC resistance bridge and temperature controller](instruments/electronics/resistance-bridge/lakeshore-372/instrument.yaml) | resistance-bridge | no card | GPIB, USB, LAN | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/372_manual.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) |
| [Picowatt AVS-47B AC resistance bridge](instruments/electronics/resistance-bridge/picowatt-avs-47/instrument.yaml) | resistance-bridge | no card | GPIB, RS-232, USB | [manual](https://www.picowatt.fi/support/avs47bmanual_20180424_1101_1110.pdf) |  |
| [SRS SIM921 AC resistance bridge](instruments/electronics/resistance-bridge/srs-sim921/instrument.yaml) | resistance-bridge | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM921m.pdf) |  |
| [Agilent / Keysight 33220A function / arbitrary waveform generator](instruments/electronics/function-generator/keysight-33220a/instrument.yaml) | function-generator | no card | GPIB, USB-TMC, LAN | [manual](https://www.keysight.com/us/en/assets/9018-04437/user-manuals/9018-04437.pdf) |  |
| [Keysight 33500B / 33600A waveform generators](instruments/electronics/function-generator/keysight-33500b/instrument.yaml) | function-generator | [community](instruments/electronics/function-generator/keysight-33500b/card.yaml) | USB-TMC, LAN, GPIB |  | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) |
| [SRS DS345 function generator](instruments/electronics/function-generator/srs-ds345/instrument.yaml) | function-generator | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DS345m.pdf) |  |
| [Keysight M3202A PXIe arbitrary waveform generator](instruments/electronics/awg/keysight-m3202a/instrument.yaml) | awg | no card | PXIe | [sign-in](https://www.keysight.com/us/en/assets/9018-04448/user-manuals/9018-04448.pdf) |  |
| [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](instruments/electronics/awg/qick-rfsoc/instrument.yaml) | awg | [community](instruments/electronics/awg/qick-rfsoc/card.yaml) | LAN |  | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Rigol DG1000Z function and arbitrary waveform generators](instruments/electronics/awg/rigol-dg1000z/instrument.yaml) | awg | [community](instruments/electronics/awg/rigol-dg1000z/card.yaml) | USB-TMC, LAN | [manual](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0493/1/-/-/-/-/DG1000Z%20Programming%20Guide.pdf) |  |
| [Spectrum Instrumentation M4i.66xx arbitrary waveform generator cards](instruments/electronics/awg/spectrum-m4i-66xx/instrument.yaml) | awg | no card | PCIe | [manual](https://spectrum-instrumentation.com/dl/m4i_m4x_66xx_96xx_manual_english.pdf) |  |
| [Tektronix AWG5200 series arbitrary waveform generator](instruments/electronics/awg/tektronix-awg5200/instrument.yaml) | awg | no card | LAN, USB-TMC, GPIB | [manual](https://download.tek.com/manual/AWG5200-Programmer-Manual-077133700-RevA.pdf) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [Zurich Instruments HDAWG arbitrary waveform generator](instruments/electronics/awg/zhinst-hdawg/instrument.yaml) | awg | no card | USB, LAN | [manual](https://docs.zhinst.com/hdawg_user_manual/index.html) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [AlazarTech ATS9870 8-bit 1 GS/s PCIe waveform digitizer](instruments/electronics/oscilloscope/alazartech-ats9870/instrument.yaml) | oscilloscope | no card | PCIe | [manual](https://docs.alazartech.com/ats-sdk-user-guide/latest/) |  |
| [Keysight InfiniiVision 3000 X-Series oscilloscopes](instruments/electronics/oscilloscope/keysight-dsox3000/instrument.yaml) | oscilloscope | no card | LAN, USB-TMC, GPIB | [manual](https://www.keysight.com/us/en/assets/9018-06894/programming-guides/9018-06894.pdf) |  |
| [Pico Technology PicoScope USB oscilloscopes](instruments/electronics/oscilloscope/pico-picoscope/instrument.yaml) | oscilloscope | no card | USB | [manual](https://www.picotech.com/download/manuals/picoscope-6000-series-a-api-programmers-guide.pdf) |  |
| [Tektronix 5 Series MSO mixed signal oscilloscopes](instruments/electronics/oscilloscope/tektronix-mso5/instrument.yaml) | oscilloscope | no card | LAN, USB-TMC | [manual](https://download.tek.com/manual/4-5-6-Series-MSO_Programmer_077189805.pdf) |  |
| [NI DAQ devices through NI-DAQmx (USB-600x, USB-62xx, PCIe/PXIe-63xx, cDAQ)](instruments/electronics/daq/ni-daqmx/instrument.yaml) | daq | [community](instruments/electronics/daq/ni-daqmx/card.yaml) | USB, PCIe, PXIe |  |  |
| [Keysight E4980A precision LCR meter](instruments/electronics/lcr-meter/keysight-e4980a/instrument.yaml) | lcr-meter | no card | GPIB, USB-TMC, LAN | [manual](https://www.keysight.com/us/en/assets/9018-05655/user-manuals/9018-05655.pdf) |  |
| [Solartron 1260A impedance/gain-phase analyzer](instruments/electronics/lcr-meter/solartron-1260/instrument.yaml) | lcr-meter | no card | GPIB | [sign-in](https://www.ameteksi.com/-/media/ameteksi/download_links/documentations/supportcenter/solartonanalytical/product-manuals/1260a-impedance-analyzer-ea.pdf) |  |
| [Zurich Instruments MFIA impedance analyzer](instruments/electronics/lcr-meter/zhinst-mfia/instrument.yaml) | lcr-meter | no card | USB, LAN | [manual](https://docs.zhinst.com/mfia_user_manual/) |  |
| [Andeen-Hagerling AH 2700A ultra-precision capacitance bridge](instruments/electronics/capacitance-bridge/andeen-hagerling-ah2700a/instrument.yaml) | capacitance-bridge | no card | GPIB, RS-232 | [support](https://www.andeen-hagerling.com/ah2700a.htm) |  |
| [Delta Elektronika SM series programmable DC power supplies](instruments/electronics/power-supply/delta-elektronika-sm/instrument.yaml) | power-supply | no card | analog, RS-232, LAN, GPIB | [manual](https://www.deltaelektronika.com/sites/default/files/2025-05/PSC-232_prod-manual_V202503.pdf) |  |
| [Keysight E36300 series triple-output programmable DC power supplies](instruments/electronics/power-supply/keysight-e36300/instrument.yaml) | power-supply | no card | USB-TMC, LAN, GPIB | [manual](https://www.keysight.com/us/en/assets/9018-04577/programming-guides/9018-04577.pdf) |  |
| [TDK-Lambda Genesys programmable DC power supplies](instruments/electronics/power-supply/tdk-lambda-genesys/instrument.yaml) | power-supply | no card | RS-232, RS-485, GPIB, USB, LAN |  |  |
| [Keithley 4200A-SCS parameter analyzer](instruments/electronics/parameter-analyzer/keithley-4200a/instrument.yaml) | parameter-analyzer | no card | GPIB, LAN | [manual](https://download.tek.com/manual/4200A-KXCI-907-01F_Sept2026.pdf) |  |
| [Keysight B1500A semiconductor device parameter analyzer](instruments/electronics/parameter-analyzer/keysight-b1500a/instrument.yaml) | parameter-analyzer | no card | GPIB | [manual](https://www.keysight.com/us/en/assets/9018-01851/programming-guides/9018-01851.pdf) |  |
| [Keithley 707B / 708B switching matrix](instruments/electronics/switch-matrix/keithley-707b/instrument.yaml) | switch-matrix | no card | GPIB, LAN, RS-232 | [manual](https://download.tek.com/manual/707B-901-01C_Jan_2025_Ref.pdf) |  |
| [SRS SR1 audio analyzer](instruments/electronics/signal-analyzer/srs-sr1/instrument.yaml) | signal-analyzer | no card | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR1bm.pdf) |  |
| [SRS SR785 dynamic signal analyzer](instruments/electronics/signal-analyzer/srs-sr785/instrument.yaml) | signal-analyzer | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR785m.pdf) |  |
| [aixACCT TF Analyzer ferroelectric and piezoelectric testers](instruments/electronics/ferroelectric-tester/aixacct-tf-analyzer/instrument.yaml) | ferroelectric-tester | no card |  | [support](https://www.aixacct.com/en/testsysteme/tf-analyzer-family/) |  |
| [Radiant Technologies Precision ferroelectric testers](instruments/electronics/ferroelectric-tester/radiant-precision/instrument.yaml) | ferroelectric-tester | no card |  | [support](https://www.ferrodevices.com/) |  |
| [SRS SIM960 analog PID controller](instruments/electronics/pid-controller/srs-sim960/instrument.yaml) | pid-controller | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM960m.pdf) |  |
| [Liquid Instruments Moku:Pro, Moku:Lab and Moku:Go](instruments/electronics/fpga-instrument/liquid-instruments-moku/instrument.yaml) | fpga-instrument | no card | USB, LAN, web API | [manual](https://apis.liquidinstruments.com/api/) |  |
| [Red Pitaya STEMlab boards (SCPI server) and the PyRPL lock software](instruments/electronics/fpga-instrument/red-pitaya-stemlab/instrument.yaml) | fpga-instrument | no card | LAN | [manual](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/scpi.html) |  |
| [SRS SIM900 mainframe](instruments/electronics/mainframe/srs-sim900/instrument.yaml) | mainframe | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM900m.pdf) |  |

### RF and microwave

Signal generators, network and spectrum analyzers, acousto-optic drivers and qubit controllers.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Keysight E8257D PSG analog signal generator](instruments/rf-microwave/microwave-source/keysight-e8257d/instrument.yaml) | microwave-source | no card | GPIB, LAN, RS-232 | [manual](https://www.keysight.com/us/en/assets/9018-04961/installation-guides/9018-04961.pdf) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [Keysight MXG N5183B microwave signal generator](instruments/rf-microwave/microwave-source/keysight-n5183b/instrument.yaml) | microwave-source | [community](instruments/rf-microwave/microwave-source/keysight-n5183b/card.yaml) | USB-TMC, LAN, GPIB | [manual](https://www.keysight.com/content/dam/keysight/en/doc/gate/programming-guides/9018-03690.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Rohde & Schwarz SGS100A SGMA RF source](instruments/rf-microwave/microwave-source/rs-sgs100a/instrument.yaml) | microwave-source | no card | LAN, USB-TMC, PCIe | [manual](https://www.rohde-schwarz.com/webhelp/SGS100A_HTML_UserManual_en/SGS100A_HTML_UserManual_en.htm) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Rohde & Schwarz SMB100A RF and microwave signal generator](instruments/rf-microwave/microwave-source/rs-smb100a/instrument.yaml) | microwave-source | [community](instruments/rf-microwave/microwave-source/rs-smb100a/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_manuals/dl_user_manual/SMB100A_OperatingManual_en_23.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml), [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml) +1 |
| [SignalCore SC5511A 20 GHz RF signal source](instruments/rf-microwave/microwave-source/signalcore-sc5511a/instrument.yaml) | microwave-source | no card | USB | [manual](https://www.signalcore.com/downloads/sc5510x_11x/SC5511A_Manual.pdf) |  |
| [Stanford Research SG380-series RF signal generators](instruments/rf-microwave/microwave-source/srs-sg384/instrument.yaml) | microwave-source | [community](instruments/rf-microwave/microwave-source/srs-sg384/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SG380m.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) +2 |
| [Valon Technology 5015 and 5019 frequency synthesizers](instruments/rf-microwave/microwave-source/valon-5019/instrument.yaml) | microwave-source | no card | USB | [manual](https://valontechnology.com/5015users/Valon_5015-5019_opman.pdf) |  |
| [Windfreak SynthHD dual-channel microwave generator](instruments/rf-microwave/microwave-source/windfreak-synthhd/instrument.yaml) | microwave-source | [draft](instruments/rf-microwave/microwave-source/windfreak-synthhd/card.yaml) | USB | [manual](https://windfreaktech.com/wp-content/uploads/2016/12/WFT_SerialProgramming_API_10b.pdf) | [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Copper Mountain 2-port USB VNAs (S5048, S5065, M5180 and similar) via the S2VNA software](instruments/rf-microwave/vna/copper-mountain-s2vna/instrument.yaml) | vna | no card | USB, LAN | [manual](https://coppermountaintech.com/wp-content/uploads/2025/04/S2VNA-Operating-and-Programming-Manual.pdf) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Keysight E5071C ENA vector network analyzer](instruments/rf-microwave/vna/keysight-e5071c/instrument.yaml) | vna | no card | GPIB, USB-TMC, LAN | [manual](https://helpfiles.keysight.com/csg/e5071c/programming/remote_control/remote_control.htm) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Keysight E5080B ENA vector network analyzer](instruments/rf-microwave/vna/keysight-e5080b/instrument.yaml) | vna | no card | GPIB, USB-TMC, LAN | [manual](https://helpfiles.keysight.com/csg/e5080b/Programming/Programming_Guide.htm) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml) |
| [Rohde & Schwarz ZNB vector network analyzer](instruments/rf-microwave/vna/rs-znb/instrument.yaml) | vna | no card | GPIB, USB-TMC, LAN | [manual](https://www.rohde-schwarz.com/webhelp/ZNB_HTML_UserManual_en/ZNB_HTML_UserManual_en.htm) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Keysight N9020B MXA signal analyzer (X-Series)](instruments/rf-microwave/spectrum-analyzer/keysight-n9020b/instrument.yaml) | spectrum-analyzer | no card | GPIB, USB-TMC, LAN | [sign-in](https://www.keysight.com/us/en/assets/9018-02192/programming-guides/9018-02192.pdf) |  |
| [Signal Hound BB60C and BB60D spectrum analyzers](instruments/rf-microwave/spectrum-analyzer/signalhound-bb60/instrument.yaml) | spectrum-analyzer | no card | USB | [manual](https://signalhound.com/sigdownloads/SDK/online_docs/bb_api/index.html) |  |
| [MOGLabs XRF / ARF / QRF agile RF synthesizers](instruments/rf-microwave/aom-driver/moglabs-xrf/instrument.yaml) | aom-driver | [community](instruments/rf-microwave/aom-driver/moglabs-xrf/card.yaml) | USB, LAN | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/RF-generators-synthesizers/MOGLabs_XRF_manual.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Novatech 409B four-channel DDS signal generator](instruments/rf-microwave/aom-driver/novatech-409b/instrument.yaml) | aom-driver | [community](instruments/rf-microwave/aom-driver/novatech-409b/card.yaml) | RS-232 | [manual](https://www.novatechsales.com/docs/409b_man.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Intermodulation Products Presto](instruments/rf-microwave/quantum-controller/intermod-presto/instrument.yaml) | quantum-controller | no card | LAN | [manual](https://intermod.pro/manuals/presto/) |  |
| [Qblox Cluster qubit control system](instruments/rf-microwave/quantum-controller/qblox-cluster/instrument.yaml) | quantum-controller | no card | LAN | [manual](https://docs.qblox.com/en/main/products/qblox_instruments/api/index.html) |  |
| [Quantum Machines OPX+ / OPX1000 quantum controller (QUA)](instruments/rf-microwave/quantum-controller/quantum-machines-opx/instrument.yaml) | quantum-controller | no card | LAN | [manual](https://docs.quantum-machines.co/latest/) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [Zurich Instruments SHFQC qubit controller](instruments/rf-microwave/quantum-controller/zhinst-shfqc/instrument.yaml) | quantum-controller | no card | USB, LAN | [manual](https://docs.zhinst.com/shfqc_user_manual/index.html) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Quantum Machines Octave up- and down-converter](instruments/rf-microwave/frequency-converter/quantum-machines-octave/instrument.yaml) | frequency-converter | no card | LAN | [manual](https://docs.quantum-machines.co/latest/docs/Guides/octave/) |  |
| [Mini-Circuits USB and Ethernet programmable RF switches (RC, USB and ZTRC series)](instruments/rf-microwave/rf-switch/minicircuits-rf-switch/instrument.yaml) | rf-switch | no card | USB, LAN | [manual](https://www.minicircuits.com/softwaredownload/Prog_Manual-2-Switch.pdf) |  |
| [Mini-Circuits RCDAT USB and Ethernet programmable attenuators](instruments/rf-microwave/rf-attenuator/minicircuits-rcdat/instrument.yaml) | rf-attenuator | no card | USB, LAN | [manual](https://www.minicircuits.com/softwaredownload/Prog_Manual-6-Programmable_Attenuator.pdf) |  |
| [Vaunix Lab Brick LDA digital attenuators](instruments/rf-microwave/rf-attenuator/vaunix-lda/instrument.yaml) | rf-attenuator | no card | USB | [support](https://vaunix.com/software/) |  |
| [Keysight U2000 series USB power sensors](instruments/rf-microwave/rf-power-meter/keysight-u2000/instrument.yaml) | rf-power-meter | no card | USB-TMC | [sign-in](https://www.keysight.com/us/en/assets/9018-01701/programming-guides/9018-01701.pdf) |  |
| [Rohde & Schwarz NRP power sensors (NRPxxS(N), NRPxxA(N), NRPxxP and NRP-Z series)](instruments/rf-microwave/rf-power-meter/rs-nrp/instrument.yaml) | rf-power-meter | no card | USB-TMC, USB, LAN | [manual](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/pdm/cl_manuals/user_manual/1177_5079_01/NRPxSN_UserManual_en_26.pdf) |  |
| [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](instruments/electronics/awg/qick-rfsoc/instrument.yaml) | awg | [community](instruments/electronics/awg/qick-rfsoc/card.yaml) | LAN |  | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Spectrum Instrumentation M4i.66xx arbitrary waveform generator cards](instruments/electronics/awg/spectrum-m4i-66xx/instrument.yaml) | awg | no card | PCIe | [manual](https://spectrum-instrumentation.com/dl/m4i_m4x_66xx_96xx_manual_english.pdf) |  |
| [Stanford Research Systems SR844 RF lock-in amplifier](instruments/electronics/lock-in/srs-sr844/instrument.yaml) | lock-in | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf) |  |

### Timing, pulses and photon counting

Pulse and delay generators, experiment sequencers, photon counters, counters and clocks.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Avtech -B series high-speed pulse generators (rise time 1 ns and below)](instruments/timing/pulse-generator/avtech-pulse-generator/instrument.yaml) | pulse-generator | no card | GPIB, RS-232, LAN | [manual](https://www.avtechpulse.com/manuals/programming/programming.pdf) |  |
| [Keysight 81150A and 81160A pulse function arbitrary noise generators](instruments/timing/pulse-generator/keysight-81160a/instrument.yaml) | pulse-generator | no card | GPIB, USB-TMC, LAN | [sign-in](https://www.keysight.com/us/en/assets/9018-03445/user-manuals/9018-03445.pdf) |  |
| [SpinCore PulseBlaster pulse generators](instruments/timing/pulse-generator/spincore-pulseblaster/instrument.yaml) | pulse-generator | [community](instruments/timing/pulse-generator/spincore-pulseblaster/card.yaml) | USB, PCIe |  | [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Swabian Instruments Pulse Streamer 8/2](instruments/timing/pulse-generator/swabian-pulse-streamer/instrument.yaml) | pulse-generator | [community](instruments/timing/pulse-generator/swabian-pulse-streamer/card.yaml) | LAN | [manual](https://www.swabianinstruments.com/static/documentation/pulse-streamer/v2.1/sections/api-doc.html) | [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Berkeley Nucleonics Model 575 and 577 digital delay and pulse generators](instruments/timing/delay-generator/bnc-577/instrument.yaml) | delay-generator | no card | USB, RS-232, LAN, GPIB | [manual](https://www.berkeleynucleonics.com/docs/bnc-model-577-user-manual.html) |  |
| [Stanford Research DG645 digital delay generator](instruments/timing/delay-generator/srs-dg645/instrument.yaml) | delay-generator | [community](instruments/timing/delay-generator/srs-dg645/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DG645m.pdf) |  |
| [ARTIQ and Sinara hardware (Kasli, Urukul, Zotino, Sampler, Phaser, Mirny)](instruments/timing/sequencer/m-labs-artiq-sinara/instrument.yaml) | sequencer | no card | LAN | [manual](https://m-labs.hk/artiq/manual/) |  |
| [ID Quantique ID900 and ID1000 Time Controllers](instruments/timing/photon-counter/idquantique-id900/instrument.yaml) | photon-counter | no card | LAN | [support](https://www.idquantique.com/quantum-detection-systems/products/id1000-time-controller/) |  |
| [PicoQuant HydraHarp 400 TCSPC / time tagger](instruments/timing/photon-counter/picoquant-hydraharp-400/instrument.yaml) | photon-counter | no card | USB | [manual](https://downloads.picoquant.com/manuals/discontinued/HydraHarp400_DLL_Manual.pdf) |  |
| [PicoQuant MultiHarp 150 time tagger](instruments/timing/photon-counter/picoquant-multiharp-150/instrument.yaml) | photon-counter | no card | USB | [manual](https://downloads.picoquant.com/manuals/MultiHarp150_160_DLL_Manual.pdf) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [qutools quTAG time-to-digital converter](instruments/timing/photon-counter/qutools-qutag/instrument.yaml) | photon-counter | no card | USB | [manual](https://www.qutools.com/files/quTAG/documentation/) |  |
| [Stanford Research Systems SR400 gated photon counter](instruments/timing/photon-counter/srs-sr400/instrument.yaml) | photon-counter | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR400m.pdf) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Swabian Instruments Time Tagger (20, Ultra, X)](instruments/timing/photon-counter/swabian-time-tagger/instrument.yaml) | photon-counter | [community](instruments/timing/photon-counter/swabian-time-tagger/card.yaml) | USB | [manual](https://www.swabianinstruments.com/static/documentation/TimeTagger/api/measurements/event_counting.html) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Keysight 53230A universal frequency counter/timer](instruments/timing/frequency-counter/keysight-53230a/instrument.yaml) | frequency-counter | no card | GPIB, USB-TMC, LAN | [support](https://www.keysight.com/us/en/assets/7018-02642/data-sheets/5990-6283.pdf) |  |
| [Stanford Research Systems SR620 universal time interval counter](instruments/timing/frequency-counter/srs-sr620/instrument.yaml) | frequency-counter | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR620m.pdf) |  |
| [Stanford Research Systems FS725 rubidium frequency standard](instruments/timing/frequency-reference/srs-fs725/instrument.yaml) | frequency-reference | no card | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/FS725m.pdf) |  |

### Lasers and laser control

CW, tunable and ultrafast lasers, parametric sources, combs, diode controllers, locks and wavelength meters.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Azurlight Systems ALS fiber lasers and amplifiers](instruments/lasers/laser/azurlight-als/instrument.yaml) | laser | no card | analog | [support](https://azurlight-systems.com/high-power-fiber-lasers-low-noise-single-mode-single-frequency/) |  |
| [Coherent Chameleon Ultra / Discovery ultrafast Ti:sapphire lasers](instruments/lasers/laser/coherent-chameleon/instrument.yaml) | laser | no card | RS-232, USB | [support](https://www.coherent.com/lasers/oscillators/chameleon-ultra) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Coherent COMPexPro excimer lasers (COMPex series)](instruments/lasers/laser/coherent-compex/instrument.yaml) | laser | no card |  | [support](https://www.coherent.com/lasers/excimer/compex) |  |
| [Coherent Mephisto NPRO lasers](instruments/lasers/laser/coherent-mephisto/instrument.yaml) | laser | no card |  | [support](https://www.coherent.com/lasers/cw-solid-state/mephisto) |  |
| [Coherent OBIS LX/LS lasers](instruments/lasers/laser/coherent-obis/instrument.yaml) | laser | [community](instruments/lasers/laser/coherent-obis/card.yaml) | USB, RS-232 | [manual](https://www.coherent.com/content/dam/coherent/site/en/resources/manuals/lasers/obis-lx-ls-operators-manual.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) +5 |
| [Coherent Verdi DPSS lasers (G, V and C series)](instruments/lasers/laser/coherent-verdi/instrument.yaml) | laser | no card |  | [support](https://www.coherent.com/lasers/cw-solid-state/verdi) |  |
| [HÜBNER Photonics Cobolt 04-01 / 06-01 / 08-01 series lasers](instruments/lasers/laser/hubner-cobolt/instrument.yaml) | laser | no card | USB, RS-232 | [manual](https://hubner-photonics.com/wp-content/uploads/2023/11/D0136-P_Manual-Cobolt-06-01-Series_October_2023-1.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) +3 |
| [IPG Photonics YLR fiber lasers](instruments/lasers/laser/ipg-ylr/instrument.yaml) | laser | no card |  | [manual](https://stipgpkenticoprod.blob.core.windows.net/ipgpsoftware/YLR/YLR%20Laser%20Fieldbus%20Interface/Documents/DOCOXISCOMXX0002_IPG_YLR-YLPP_Series_Fieldbus_Spec.pdf) |  |
| [Light Conversion PHAROS femtosecond laser](instruments/lasers/laser/lightcon-pharos/instrument.yaml) | laser | [community](instruments/lasers/laser/lightcon-pharos/card.yaml) | LAN, web API |  | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [M Squared SolsTiS Ti:sapphire laser (ICE-BLOC)](instruments/lasers/laser/m2-solstis/instrument.yaml) | laser | [community](instruments/lasers/laser/m2-solstis/card.yaml) | LAN |  | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) |
| [NKT Photonics SuperK EXTREME / FIANIUM supercontinuum lasers](instruments/lasers/laser/nkt-superk/instrument.yaml) | laser | no card | USB, LAN, RS-232 | [manual](https://lf.hamamatsu.com/wp-json/nktphotonics/v1/download/SuperK-EXTREME/SuperK%20EXTREME%20Product%20Guide.pdf) |  |
| [Spectra-Physics Mai Tai Ti:sapphire ultrafast laser](instruments/lasers/laser/spectra-physics-mai-tai/instrument.yaml) | laser | no card | RS-232 | [manual](https://api.p1.mks.com/mam/celum/celum_assets/sp/resources/284A_Rev_G_Mai_Tai_Users_Manual.pdf) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Vexlum VALO VECSEL lasers (VALO SF and VALO SHG)](instruments/lasers/laser/vexlum-vecsel/instrument.yaml) | laser | no card |  | [support](https://vexlum.com/products/) |  |
| [HÜBNER Photonics C-WAVE tunable CW OPO](instruments/lasers/parametric-source/hubner-c-wave/instrument.yaml) | parametric-source | no card |  | [support](https://hubner-photonics.com/products/lasers/tunable-lasers/c-wave/) |  |
| [Light Conversion ORPHEUS optical parametric amplifiers](instruments/lasers/parametric-source/lightcon-orpheus/instrument.yaml) | parametric-source | no card | USB, LAN, web API | [manual](https://lightconupdater.blob.core.windows.net/documentation/WinTopas4/index.html) |  |
| [Light Conversion TOPAS optical parametric amplifiers (TOPAS-Prime)](instruments/lasers/parametric-source/lightcon-topas/instrument.yaml) | parametric-source | no card | USB, LAN, web API | [manual](https://lightconupdater.blob.core.windows.net/documentation/WinTopas4/index.html) |  |
| [Menlo Systems FC1500 optical frequency combs](instruments/lasers/frequency-comb/menlo-fc1500/instrument.yaml) | frequency-comb | no card |  | [support](https://www.menlosystems.com/products/optical-frequency-combs/fc1500-uln-nova/) |  |
| [TOPTICA DFC difference frequency combs (DFC CORE and DFC CORE+)](instruments/lasers/frequency-comb/toptica-dfc/instrument.yaml) | frequency-comb | no card | LAN | [support](https://www.toptica.com/products/frequency-combs/dfc) |  |
| [MOGLabs DLC-202 diode laser controller](instruments/lasers/laser-driver/moglabs-dlc-202/instrument.yaml) | laser-driver | no card | USB, LAN | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/Laser-Electronics/MOGLabs_DLC_manual.pdf) |  |
| [PicoQuant PDL 800-D pulsed diode laser driver](instruments/lasers/laser-driver/picoquant-pdl-800/instrument.yaml) | laser-driver | no card |  | [manual](https://downloads.picoquant.com/manuals/PDL800-D_Manual.pdf) |  |
| [Thorlabs CLD1010 compact laser diode and TEC controller](instruments/lasers/laser-driver/thorlabs-cld1010/instrument.yaml) | laser-driver | no card | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/c/cl/cld/cld1015/doc-104674.pdf) |  |
| [Thorlabs ITC4000-series laser diode and TEC controllers](instruments/lasers/laser-driver/thorlabs-itc4000/instrument.yaml) | laser-driver | [community](instruments/lasers/laser-driver/thorlabs-itc4000/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/t/te/ted/ted4015/16407-d03.pdf) |  |
| [TOPTICA DLC pro diode laser controller](instruments/lasers/laser-driver/toptica-dlc-pro/instrument.yaml) | laser-driver | [draft](instruments/lasers/laser-driver/toptica-dlc-pro/card.yaml) | LAN, USB |  | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |
| [MOGLabs FSC fast servo controller](instruments/lasers/laser-lock/moglabs-fsc/instrument.yaml) | laser-lock | no card |  | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/Laser-Electronics/MOGLabs_FSC_manual.pdf) |  |
| [TOPTICA DigiLock 110 digital laser lock](instruments/lasers/laser-lock/toptica-digilock/instrument.yaml) | laser-lock | no card | USB, LAN | [manual](https://www.toptica.com/fileadmin/Editors_English/03_products/03_tunable_diode_lasers/04_control_electronics/02_laser_locking_electronics/04_DigiLock_110/toptica_digilock_manual.pdf) |  |
| [TOPTICA FALC pro fast analog laser lock (the FALC 110 has no computer control)](instruments/lasers/laser-lock/toptica-falc/instrument.yaml) | laser-lock | no card |  | [support](https://www.toptica.com/products/locking-driving-electronics/falc-pro) |  |
| [Vescent D2-125 laser servo](instruments/lasers/laser-lock/vescent-d2-125/instrument.yaml) | laser-lock | no card | analog | [manual](https://vescent-production-media.s3.us-west-2.amazonaws.com/files/67117c0f2897eecc14f41d25.pdf) |  |
| [Bristol Instruments 671 / 771 / 871 wavelength meters](instruments/lasers/wavemeter/bristol-wavemeter/instrument.yaml) | wavemeter | no card | USB, LAN | [support](https://www.bristol-inst.com/wp-content/uploads/2023/09/Bristol-671-Series-Laser-Wavelength-Meter-Specifications.pdf) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |
| [HighFinesse WS6 / WS7 / WS8 wavelength meters](instruments/lasers/wavemeter/highfinesse-wavemeter/instrument.yaml) | wavemeter | no card | USB | [support](https://www.highfinesse.com/en/support/downloads.html) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |
| [Liquid Instruments Moku:Pro, Moku:Lab and Moku:Go](instruments/electronics/fpga-instrument/liquid-instruments-moku/instrument.yaml) | fpga-instrument | no card | USB, LAN, web API | [manual](https://apis.liquidinstruments.com/api/) |  |
| [Red Pitaya STEMlab boards (SCPI server) and the PyRPL lock software](instruments/electronics/fpga-instrument/red-pitaya-stemlab/instrument.yaml) | fpga-instrument | no card | LAN | [manual](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/scpi.html) |  |

### Optics, detection and spectroscopy

Detectors, spectrometers, cameras, modulators, shutters, light shaping and fiber optics.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Newport 2936-R / 1936-R optical power meters](instruments/optics/power-meter/newport-2936-r/instrument.yaml) | power-meter | no card | USB, RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/npresources/hc4/h06/10082698067998/19xx-29xx-R-Power-Meter-Commands_Ver01/19xx-29xx-R-Power-Meter-Commands-Ver01.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) |
| [Thorlabs PM100D / PM100USB / PM400 optical power meters](instruments/optics/power-meter/thorlabs-pm100/instrument.yaml) | power-meter | [community](instruments/optics/power-meter/thorlabs-pm100/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/p/pm/pm1/pm100d/17654-d02.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml) +2 |
| [HORIBA iHR320 / iHR550 imaging spectrometers](instruments/optics/spectrometer/horiba-ihr/instrument.yaml) | spectrometer | no card | USB | [manual](https://horiba-python-sdk.readthedocs.io/en/latest/icl_api/) | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) |
| [Ocean Insight USB spectrometers (Flame, HR, QE Pro, USB2000+)](instruments/optics/spectrometer/ocean-spectrometer/instrument.yaml) | spectrometer | [community](instruments/optics/spectrometer/ocean-spectrometer/card.yaml) | USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [Andor Shamrock and Kymera spectrographs](instruments/optics/monochromator/andor-shamrock/instrument.yaml) | monochromator | [community](instruments/optics/monochromator/andor-shamrock/card.yaml) | USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +1 |
| [Newport Oriel Cornerstone 130 and 260 monochromators](instruments/optics/monochromator/newport-cornerstone/instrument.yaml) | monochromator | no card | RS-232, USB, GPIB | [manual](https://api.p1.mks.com/medias/sys_master/software/software/h30/hb7/9358972125214/90088262B-MCS130B-Manual.pdf) |  |
| [Princeton Instruments (Acton) SpectraPro monochromators](instruments/optics/monochromator/princeton-spectrapro/instrument.yaml) | monochromator | [community](instruments/optics/monochromator/princeton-spectrapro/card.yaml) | RS-232, USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +1 |
| [Anritsu MS9740A optical spectrum analyzer](instruments/optics/optical-spectrum-analyzer/anritsu-ms9740/instrument.yaml) | optical-spectrum-analyzer | no card | GPIB, LAN | [manual](https://dl.cdn-anritsu.com/en-au/test-measurement/files/Manuals/Operation-Manual/MS9740A/MS9740A_Remote_Operation_Manual_SCPI_e_5_0.pdf) |  |
| [Yokogawa AQ6370D optical spectrum analyzer](instruments/optics/optical-spectrum-analyzer/yokogawa-aq6370/instrument.yaml) | optical-spectrum-analyzer | no card | GPIB, LAN, RS-232 | [manual](https://cdn.tmi.yokogawa.com/1/6057/files/IMAQ6370C-17EN.pdf) |  |
| [Andor CCD and EMCCD cameras (iXon, Newton, iDus)](instruments/optics/camera/andor-ccd/instrument.yaml) | camera | [draft](instruments/optics/camera/andor-ccd/card.yaml) | USB, PCIe |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +2 |
| [Andor sCMOS cameras (Zyla, Neo, Sona, Marana)](instruments/optics/camera/andor-scmos/instrument.yaml) | camera | [draft](instruments/optics/camera/andor-scmos/card.yaml) | USB, PCIe |  |  |
| [Basler industrial cameras (pylon)](instruments/optics/camera/basler-camera/instrument.yaml) | camera | [community](instruments/optics/camera/basler-camera/card.yaml) | USB, LAN |  |  |
| [Hamamatsu ORCA-Flash4.0 / ORCA-Quest scientific CMOS cameras (DCAM-API)](instruments/optics/camera/hamamatsu-orca/instrument.yaml) | camera | no card | USB, PCIe | [support](https://www.hamamatsu.com/us/en/product/cameras/software/driver-software/dcam-sdk4.html) |  |
| [Nüvü Camēras HNü EMCCD cameras](instruments/optics/camera/nuvu-hnu/instrument.yaml) | camera | no card | LAN | [support](https://www.nuvucameras.com/products/hnu-512/) |  |
| [Teledyne Photometrics Kinetix sCMOS camera (PVCAM SDK)](instruments/optics/camera/teledyne-kinetix/instrument.yaml) | camera | no card | PCIe, USB | [manual](https://docs.teledynevisionsolutions.com/pvcam-sdk/) |  |
| [Teledyne Princeton Instruments cameras through PICam](instruments/optics/camera/princeton-picam/instrument.yaml) | camera | [community](instruments/optics/camera/princeton-picam/card.yaml) | USB, LAN |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +1 |
| [Thorlabs Kiralux / Quantalux / Zelux scientific cameras (Scientific Camera SDK)](instruments/optics/camera/thorlabs-scientific-camera/instrument.yaml) | camera | no card | USB | [support](https://www.thorlabs.com/item/CS165MU) |  |
| [Thorlabs PDQ80A quadrant detector with KPA101 K-Cube position aligner](instruments/optics/photodetector/thorlabs-pdq80a/instrument.yaml) | photodetector | no card | USB, analog | [manual](https://media.thorlabs.com/contentassets/e92d618c92c94cea9096b3f231859611/etn033528-d02.pdf) |  |
| [Thorlabs BP209 slit-scanning beam profiler](instruments/optics/beam-profiler/thorlabs-bp209/instrument.yaml) | beam-profiler | no card | USB | [manual](https://media.thorlabs.com/globalassets/items/b/bp/bp2/bp209-ir2_m/doc-104056.pdf) |  |
| [Thorlabs PAX1000 polarimeter](instruments/optics/polarimeter/thorlabs-pax1000/instrument.yaml) | polarimeter | no card | USB-TMC | [manual](https://github.com/Thorlabs/Light_Analysis_Examples/blob/main/Python/Thorlabs%20PAX1000%20Polarimeters/SCPI_command_docu/pax1000.html) |  |
| [APE pulseCheck autocorrelator](instruments/optics/autocorrelator/ape-pulsecheck/instrument.yaml) | autocorrelator | no card | USB, LAN | [support](https://www.ape-berlin.de/en/autocorrelator/pulsecheck/) |  |
| [Thorlabs MC2000B optical chopper](instruments/optics/chopper/thorlabs-mc2000b/instrument.yaml) | chopper | no card | USB | [manual](https://media.thorlabs.com/globalassets/items/m/mc/mc2/mc2000b/ttn102010-d02.pdf) | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Hinds Instruments PEM-200 photoelastic modulator controller (and PEM-100)](instruments/optics/modulator/hinds-pem/instrument.yaml) | modulator | no card | USB, LAN, RS-232 | [manual](https://www.hindsinstruments.com/wp-content/uploads/PEM-200-User-Manual.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |
| [Thorlabs FW102C six-position motorized filter wheel](instruments/optics/shutter/thorlabs-fw102c/instrument.yaml) | shutter | no card | RS-232, USB |  |  |
| [Thorlabs MFF101 motorized filter flip mount](instruments/optics/shutter/thorlabs-mff101/instrument.yaml) | shutter | no card | USB | [manual](https://media.thorlabs.com/contentassets/e92d618c92c94cea9096b3f231859611/etn012604-d02.pdf) |  |
| [Thorlabs SC10 optical beam shutter controller](instruments/optics/shutter/thorlabs-sc10/instrument.yaml) | shutter | no card | RS-232 | [support](https://media.thorlabs.com/contentassets/e92d618c92c94cea9096b3f231859611/etn017648-d02.pdf) |  |
| [Uniblitz VMM-D3 three-channel shutter driver](instruments/optics/shutter/uniblitz-vmm-d3/instrument.yaml) | shutter | no card | RS-232, analog | [manual](https://www.uniblitz.com/wp-content/uploads/2021/08/VMM_D3_D4-User-Manual-2.10_Rev_B.pdf) |  |
| [Hamamatsu X13138 series LCOS-SLM phase spatial light modulator](instruments/optics/spatial-light-modulator/hamamatsu-lcos-slm/instrument.yaml) | spatial-light-modulator | no card |  | [support](https://www.hamamatsu.com/us/en/product/optical-components/lcos-slm.html) |  |
| [HOLOEYE PLUTO-2.1 and GAEA-2 spatial light modulators (SLM Display SDK)](instruments/optics/spatial-light-modulator/holoeye-slm/instrument.yaml) | spatial-light-modulator | no card | USB | [sign-in](https://customers.holoeye.com/) |  |
| [Meadowlark Optics liquid-crystal spatial light modulators (1920x1152, 1920x1200, 1024x1024 and 1536x1536 formats)](instruments/optics/spatial-light-modulator/meadowlark-slm/instrument.yaml) | spatial-light-modulator | no card | PCIe | [support](https://www.meadowlark.com/shop/slms/1536-x-1536-spatial-light-modulator/) |  |
| [santec SLM-200 spatial light modulator](instruments/optics/spatial-light-modulator/santec-slm-200/instrument.yaml) | spatial-light-modulator | no card | USB | [sign-in](https://aoc.santec.com/en/support/usermanuals/slm/) |  |
| [ViALUX V-7000 DMD module with the ALP-4.3 API](instruments/optics/spatial-light-modulator/vialux-dmd/instrument.yaml) | spatial-light-modulator | no card | USB | [sign-in](https://www.vialux.de/ViALUX-Website/registration-for-download.html) |  |
| [DiCon GP700 programmable fiber optic switch](instruments/optics/fiber-optics/dicon-gp700/instrument.yaml) | fiber-optics | no card |  | [support](https://www.diconfiberoptics.com/resources/legacy-products.php) |  |
| [Keysight 8164B lightwave measurement system](instruments/optics/fiber-optics/keysight-8164b/instrument.yaml) | fiber-optics | no card | GPIB, LAN | [support](https://www.keysight.com/us/en/product/8164B/lightwave-measurement-system.html) |  |
| [Thorlabs MPC320 motorized fiber polarization controller](instruments/optics/fiber-optics/thorlabs-mpc320/instrument.yaml) | fiber-optics | no card | USB | [support](https://media.thorlabs.com/contentassets/5f57e82e38004e2aa5dfd0071bcf0732/kinesis_with_c_quick_start_guide.pdf) |  |
| [Energetiq EQ-99X laser-driven light source](instruments/optics/light-source/energetiq-eq-99x/instrument.yaml) | light-source | no card |  | [manual](https://www.energetiq.com/hubfs/Product%20Manuals/LDLS/EQ-99X%20LDLS%20Operation%20Maintenance%20Manual.pdf) |  |
| [Newport (Oriel) 69911 arc lamp power supply](instruments/optics/light-source/newport-69911/instrument.yaml) | light-source | no card | RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/root/h70/hc3/9574045974558/90073995B-M69911-Arc-Lamp-Power-Supply-Manual.pdf) |  |
| [Thorlabs DC4100 four-channel LED driver](instruments/optics/light-source/thorlabs-dc4100/instrument.yaml) | light-source | no card |  |  |  |
| [Montana Instruments Cryostation s-series closed-cycle optical cryostat](instruments/cryogenics/cryostat/montana-cryostation/instrument.yaml) | cryostat | no card | LAN | [manual](https://cdn.prod.website-files.com/6118466f5c775b56d53d49e9/695d7ffcee2d9010efc7f5a4_4100-1-DOC002_1.2%20(User%20Manual%20-%20Cryostation%20s-series%20-%20SHI%20Configuration%20MI75%20VCM).pdf) | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Raman spectroscopy](experiments/optics/raman.yaml), [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) +1 |
| [Quantum Design OptiCool magneto-optical cryostat](instruments/cryogenics/cryostat/qd-opticool/instrument.yaml) | cryostat | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |

### Quantum optics and single photons

Single-photon detectors, photon-pair and single-photon sources, and ovens that phase-match their crystals.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [ID Quantique ID281 SNSPD system](instruments/quantum-optics/snspd/idquantique-id281/instrument.yaml) | snspd | no card | LAN, web API | [support](https://www.idquantique.com/quantum-detection-systems/products/id281-snspd-system/) |  |
| [Photon Spot SNSPD systems (Cryospot cryostats with SNSPDs)](instruments/quantum-optics/snspd/photon-spot-snspd/instrument.yaml) | snspd | no card |  | [support](https://www.photonspot.com/cryogenics) |  |
| [Pixel Photonics Dena waveguide-integrated SNSPD systems](instruments/quantum-optics/snspd/pixel-photonics-snspd/instrument.yaml) | snspd | no card | LAN | [support](https://www.pixelphotonics.com/en/single-photon-detector-products/rack-snspd-system/) |  |
| [Quantum Opus Opus One SNSPD system](instruments/quantum-optics/snspd/quantum-opus-opus-one/instrument.yaml) | snspd | no card | USB | [manual](https://www.quantumopus.com/documentation/detector-operation) |  |
| [Single Quantum Eos SNSPD system](instruments/quantum-optics/snspd/single-quantum-eos/instrument.yaml) | snspd | no card | LAN, web API | [manual](https://docs.singlequantum.com/general/index.html) |  |
| [Excelitas SPCM-AQRH single-photon counting module](instruments/quantum-optics/single-photon-detector/excelitas-spcm-aqrh/instrument.yaml) | single-photon-detector | no card | analog | [manual](https://www.excelitas.com/sites/default/files/assets/product/document/27464.pdf) |  |
| [ID Quantique ID100 visible single-photon detector](instruments/quantum-optics/single-photon-detector/idquantique-id100/instrument.yaml) | single-photon-detector | no card |  | [support](https://www.idquantique.com/quantum-detection-systems/products/id100/) |  |
| [Micro Photon Devices PDM series SPAD modules](instruments/quantum-optics/single-photon-detector/mpd-pdm/instrument.yaml) | single-photon-detector | no card | analog | [manual](https://www.micro-photon-devices.com/user-manuals/MPD_PDM_Usermanual.pdf) |  |
| [OZ Optics polarization-entangled photon sources (EPS-1000, EPG-1000, EPG-2000)](instruments/quantum-optics/photon-source/ozoptics-entangled-source/instrument.yaml) | photon-source | no card |  | [owners](https://www.ozoptics.com/ALLNEW_PDF/OI-EPS_1000_Rev0_BC73898.pdf) |  |
| [Quandela Prometheus quantum-dot single-photon source](instruments/quantum-optics/photon-source/quandela-prometheus/instrument.yaml) | photon-source | no card |  | [support](https://www.quandela.com/products-and-services/prometheus/) |  |
| [Qubitekk entangled photon-pair source](instruments/quantum-optics/photon-source/qubitekk-entangled-source/instrument.yaml) | photon-source | no card |  | [support](https://ionq.com/news/ionq-completes-acquisition-of-qubitekk-solidifying-leadership-in-quantum) |  |
| [qutools quED entanglement demonstrator](instruments/quantum-optics/photon-source/qutools-qued/instrument.yaml) | photon-source | no card |  | [manual](https://www.qutools.com/files/quED/quED_manual.pdf) |  |
| [Sparrow Quantum Sparrow Nest rack-mounted single-photon source (built around the Sparrow Core chip)](instruments/quantum-optics/photon-source/sparrow-quantum-sparrow/instrument.yaml) | photon-source | no card | LAN, web API | [support](https://sparrowquantum.com/sparrow-nest) |  |
| [Covesion PPLN crystal ovens (PV10, PV20, PV40, PV50) with OC2 and OC3 temperature controllers](instruments/quantum-optics/crystal-oven/covesion-oven/instrument.yaml) | crystal-oven | no card |  | [support](https://covesion.com/solutions/temperature-controllers/) |  |
| [Thorlabs TC200 and TC300 heater controllers](instruments/quantum-optics/crystal-oven/thorlabs-tc300/instrument.yaml) | crystal-oven | no card | USB, RS-232 |  |  |

### Motion and positioning

Piezo positioners and scanners, motorized stages, delay lines and rotation mounts.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [attocube AMC300 / AMC100 piezo positioner controller](instruments/motion/positioner/attocube-amc/instrument.yaml) | positioner | no card | LAN, USB | [manual](https://raw.githubusercontent.com/attocube-systems/AMC-APIs/master/AMC_Interface_Manual_v1.5.1.pdf) |  |
| [attocube ANC300 piezo positioner controller](instruments/motion/positioner/attocube-anc300/instrument.yaml) | positioner | [community](instruments/motion/positioner/attocube-anc300/card.yaml) | USB, LAN |  |  |
| [attocube ANC350 closed-loop positioner controller](instruments/motion/positioner/attocube-anc350/instrument.yaml) | positioner | [community](instruments/motion/positioner/attocube-anc350/card.yaml) | USB |  | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [Mad City Labs Nano-Drive piezo nanopositioning controller](instruments/motion/positioner/mcl-nano-drive/instrument.yaml) | positioner | no card | USB, analog | [support](https://www.madcitylabs.com/nanodrive.html) | [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml) |
| [PI piezo controllers with the GCS command set](instruments/motion/positioner/pi-gcs-piezo/instrument.yaml) | positioner | [community](instruments/motion/positioner/pi-gcs-piezo/card.yaml) | USB, LAN, RS-232 |  | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [SmarAct MCS2 modular positioning controller](instruments/motion/positioner/smaract-mcs2/instrument.yaml) | positioner | no card | USB, LAN | [owners](https://www.smaract.com/en/motion/products/control-systems-and-software-working/control-systems/mcs2) | [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml) |
| [Thorlabs MDT693A / MDT694A piezo controllers](instruments/motion/positioner/thorlabs-mdt69xa/instrument.yaml) | positioner | [community](instruments/motion/positioner/thorlabs-mdt69xa/card.yaml) | USB |  |  |
| [ASI MS-2000 and Tiger stage controllers](instruments/motion/motion-stage/asi-ms-2000/instrument.yaml) | motion-stage | no card | RS-232, USB | [manual](https://docs.asiimaging.com/command_quick_start) |  |
| [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](instruments/motion/motion-stage/newport-conex-cc/instrument.yaml) | motion-stage | no card | USB | [manual](https://api.p1.mks.com/medias/sys_master/npresources/h91/hf3/10219689345054/CONEX-CC%20-%20Controller%20Documentation/CONEX-CC-Controller-Documentation.pdf) | [Raman spectroscopy](experiments/optics/raman.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Newport ESP301 three-axis motion controller](instruments/motion/motion-stage/newport-esp301/instrument.yaml) | motion-stage | no card | GPIB, USB, RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/images/images/hda/h3e/9117547069470/ESP301-User-s-Manual.pdf) |  |
| [Newport SMC100CC / SMC100PP single-axis motion controller](instruments/motion/motion-stage/newport-smc100/instrument.yaml) | motion-stage | no card | RS-232, RS-485, USB | [manual](https://api.p1.mks.com/medias/sys_master/resources/hec/h2b/10211813294110/SMC100CC_and_SMC100PP_-_User_Manual/SMC100CC-and-SMC100PP-User-Manual.pdf) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Newport XPS-D / XPS-RL universal high-performance motion controller](instruments/motion/motion-stage/newport-xps/instrument.yaml) | motion-stage | no card | LAN | [manual](https://api.p1.mks.com/medias/sys_master/npresources/h3e/h82/10211812802590/XPS_Unified_-_Programmer_s_Manual/XPS-Unified-Programmer-s-Manual.pdf) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) |
| [Physik Instrumente C-863 Mercury DC motor controller](instruments/motion/motion-stage/pi-c-863/instrument.yaml) | motion-stage | no card | USB, RS-232 | [sign-in](https://www.physikinstrumente.com/en/products/controllers-and-drivers/motion-controllers-drivers-for-linear-torque-stepper-dc-servo-motors/c-863-mercury-servo-controller-900606/) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) |
| [Prior ProScan III microscope stage controller](instruments/motion/motion-stage/prior-proscan/instrument.yaml) | motion-stage | no card | RS-232, USB | [manual](https://www.prior.com/wp-content/uploads/2026/08/ProScanIII_EN_UK_Manual.pdf) |  |
| [Thorlabs K10CR1 motorized rotation mount](instruments/motion/motion-stage/thorlabs-k10cr1/instrument.yaml) | motion-stage | no card | USB |  | [Raman spectroscopy](experiments/optics/raman.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Thorlabs KDC101 K-Cube brushed DC servo motor controller](instruments/motion/motion-stage/thorlabs-kdc101/instrument.yaml) | motion-stage | no card | USB |  | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) |

### Cryogenics, vacuum and sample environment

Temperature control, cryostats and dilution refrigerators, compressors, vacuum, strain and pressure.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Cryo-con Model 24C cryogenic temperature controller](instruments/cryogenics/temperature-controller/cryocon-24c/instrument.yaml) | temperature-controller | no card | LAN, RS-232, GPIB, USB | [support](https://qd-europe.com/de/en/news/product-application-news-spectrum/find-the-right-temperature-monitor-and-controller-for-your-cryogenic-experiments) |  |
| [Lake Shore Model 218 temperature monitor](instruments/cryogenics/temperature-controller/lakeshore-218/instrument.yaml) | temperature-controller | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/218_manual.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml) |
| [Lake Shore Model 331 and 332 cryogenic temperature controllers](instruments/cryogenics/temperature-controller/lakeshore-331/instrument.yaml) | temperature-controller | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/331_manual.pdf) |  |
| [Lake Shore Model 335 / 336 temperature controller](instruments/cryogenics/temperature-controller/lakeshore-336/instrument.yaml) | temperature-controller | [community](instruments/cryogenics/temperature-controller/lakeshore-336/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/336manual.pdf?sfvrsn=fa4e3a80_12) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) +8 |
| [Lake Shore Model 340 cryogenic temperature controller](instruments/cryogenics/temperature-controller/lakeshore-340/instrument.yaml) | temperature-controller | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/340_manual.pdf) |  |
| [Lake Shore Model 350 temperature controller](instruments/cryogenics/temperature-controller/lakeshore-350/instrument.yaml) | temperature-controller | [community](instruments/cryogenics/temperature-controller/lakeshore-350/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/software/manuals/350_manual.pdf?sfvrsn=501e9331_5) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [Oxford Instruments ITC503 intelligent temperature controller](instruments/cryogenics/temperature-controller/oxford-itc503/instrument.yaml) | temperature-controller | no card | RS-232, GPIB | [support](https://qd-oxford.com/services/legacy_product_support.html) |  |
| [Oxford Instruments Mercury iTC temperature controller](instruments/cryogenics/temperature-controller/oxford-mercury-itc/instrument.yaml) | temperature-controller | [community](instruments/cryogenics/temperature-controller/oxford-mercury-itc/card.yaml) | USB, LAN, RS-232, GPIB | [manual](https://www.mymercurysupport.com/sites/default/files/59_UMC0071_EN_02.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [SRS SIM922 diode temperature monitor](instruments/cryogenics/temperature-controller/srs-sim922/instrument.yaml) | temperature-controller | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM922m.pdf) |  |
| [attocube attoDRY closed-cycle cryostats](instruments/cryogenics/cryostat/attocube-attodry/instrument.yaml) | cryostat | [draft](instruments/cryogenics/cryostat/attocube-attodry/card.yaml) | USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hall effect and magnetoresistance](experiments/transport/hall-magnetoresistance.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Montana Instruments Cryostation s-series closed-cycle optical cryostat](instruments/cryogenics/cryostat/montana-cryostation/instrument.yaml) | cryostat | no card | LAN | [manual](https://cdn.prod.website-files.com/6118466f5c775b56d53d49e9/695d7ffcee2d9010efc7f5a4_4100-1-DOC002_1.2%20(User%20Manual%20-%20Cryostation%20s-series%20-%20SHI%20Configuration%20MI75%20VCM).pdf) | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Raman spectroscopy](experiments/optics/raman.yaml), [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) +1 |
| [Quantum Design PPMS, DynaCool, VersaLab and MPMS3 through MultiVu](instruments/cryogenics/cryostat/qd-multivu/instrument.yaml) | cryostat | [community](instruments/cryogenics/cryostat/qd-multivu/card.yaml) | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [SQUID magnetometry (M-T and M-H)](experiments/magnetometry/squid-magnetometry.yaml) +10 |
| [Quantum Design OptiCool magneto-optical cryostat](instruments/cryogenics/cryostat/qd-opticool/instrument.yaml) | cryostat | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |
| [Bluefors dilution refrigerators (Control Software, temperature controller, gas handling system)](instruments/cryogenics/dilution-refrigerator/bluefors-dilution-refrigerator/instrument.yaml) | dilution-refrigerator | no card | LAN, web API | [manual](https://github.com/BlueforsOy/Control_Software_gen2_API_examples/blob/main/README.md) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) +1 |
| [Oxford Instruments Triton dilution refrigerator](instruments/cryogenics/dilution-refrigerator/oxford-triton/instrument.yaml) | dilution-refrigerator | no card | LAN | [support](https://qd-oxford.com/services/legacy_product_support.html) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Cryomech CPA helium compressors (remote monitoring)](instruments/cryogenics/compressor/cryomech-cpa/instrument.yaml) | compressor | no card |  | [support](https://bluefors.com/support/) |  |
| [Sumitomo F-70 helium compressor](instruments/cryogenics/compressor/sumitomo-f-70/instrument.yaml) | compressor | no card | RS-232 | [support](https://shicryogenics.com/product/f-70-indoor-water-cooled-compressor-series/) |  |
| [AMI Model 1700 liquid level instrument](instruments/cryogenics/level-meter/ami-1700/instrument.yaml) | level-meter | no card | LAN, RS-232 | [manual](https://www.americanmagnetics.com/support/manuals/Model1700-Rev6.pdf) |  |
| [Cryomagnetics LM-510 liquid cryogen level monitor](instruments/cryogenics/level-meter/cryomagnetics-lm-510/instrument.yaml) | level-meter | no card | USB, LAN, GPIB, RS-232 | [manual](https://cryomagnetics.com/wp-content/uploads/2022/05/LM_510_Rev1_3.pdf) |  |
| [Oxford Instruments ILM200 helium level meter](instruments/cryogenics/level-meter/oxford-ilm200/instrument.yaml) | level-meter | no card | RS-232 | [support](https://qd-oxford.com/services/legacy_product_support.html) |  |
| [Instec mK2000 temperature controller for heating and cooling stages](instruments/cryogenics/heating-stage/instec-mk2000/instrument.yaml) | heating-stage | no card | USB, LAN | [support](https://instec.com/TCA/46.html) |  |
| [Linkam T96 controller with THMS600 heating and cooling stage](instruments/cryogenics/heating-stage/linkam-t96/instrument.yaml) | heating-stage | no card | USB | [support](https://www.linkam.co.uk/t96) |  |
| [JULABO circulators and recirculating coolers](instruments/cryogenics/chiller/julabo-circulator/instrument.yaml) | chiller | no card | USB, RS-232, RS-485, LAN | [manual](https://dbyt75tph3sip.cloudfront.net/asset/512030579289/document_qr637chm0l11lekorrrhucvk57/1.950.2823.en.V08.pdf) |  |
| [Pfeiffer Vacuum TPG 361 / TPG 362 SingleGauge / DualGauge vacuum gauge controllers](instruments/cryogenics/vacuum-gauge/pfeiffer-tpg36x/instrument.yaml) | vacuum-gauge | no card | RS-485, USB, LAN | [manual](https://www.shop.buschgroup.com/api/empolis/resource/environment/project1_p/documents/pfeifferSharepointProd/2181-bg5510ben_d.pdf) |  |
| [Agilent 4UHV ion pump controller](instruments/cryogenics/vacuum-pump/agilent-4uhv/instrument.yaml) | vacuum-pump | no card |  |  |  |
| [Edwards TIC turbo and instrument controller](instruments/cryogenics/vacuum-pump/edwards-tic/instrument.yaml) | vacuum-pump | no card | RS-232 | [support](https://www.edwardsvacuum.com/content/dam/brands/edwards-vacuum/general-vacuum/downloads/measurement-and-control/vacuum-gauge-and-pump-controllers/3601-0654-01-TIC-Turbo-and-Instr-Controller-Datasheet.pdf) |  |
| [Gamma Vacuum SPCe ion pump controller](instruments/cryogenics/vacuum-pump/gamma-vacuum-spce/instrument.yaml) | vacuum-pump | no card | RS-232, RS-485, LAN | [support](https://www.gammavacuum.com/products/digital-spc-ion) |  |
| [Pfeiffer Vacuum HiCube pumping stations and TC 400 turbo drive unit](instruments/cryogenics/vacuum-pump/pfeiffer-hicube/instrument.yaml) | vacuum-pump | no card | RS-485 | [manual](https://www.shop.buschgroup.com/api/empolis/resource/environment/project1_p/documents/pfeifferSharepointProd/1548-pt0265ben_f.pdf) |  |
| [SAES NEXTorr NEG-ion pumps with the NIOPS controller](instruments/cryogenics/vacuum-pump/saes-nextorr/instrument.yaml) | vacuum-pump | no card |  |  |  |
| [SRS RGA100 / RGA200 / RGA300 residual gas analyzers](instruments/cryogenics/rga/srs-rga/instrument.yaml) | rga | no card | RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/RGAm.pdf) |  |
| [Razorbill RP100 power supply for CS100 / CS130 uniaxial strain cells](instruments/cryogenics/strain-cell/razorbill-rp100/instrument.yaml) | strain-cell | no card | USB | [manual](https://razorbillinstruments.com/wp-content/uploads/2023/06/RP100-Manual-v6-9-Web.pdf) |  |
| [Almax easyLab Diacell iGM gas-membrane pressure controller](instruments/cryogenics/pressure-controller/almax-easylab-membrane/instrument.yaml) | pressure-controller | no card | RS-232, GPIB, LAN, USB | [support](https://www.almax-easylab.com/product/diacell-igm-controller/) |  |
| [Lake Shore Model 370 AC resistance bridge](instruments/electronics/resistance-bridge/lakeshore-370/instrument.yaml) | resistance-bridge | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/370_manual.pdf) |  |
| [Lake Shore Model 372 AC resistance bridge and temperature controller](instruments/electronics/resistance-bridge/lakeshore-372/instrument.yaml) | resistance-bridge | no card | GPIB, USB, LAN | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/372_manual.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) |
| [Picowatt AVS-47B AC resistance bridge](instruments/electronics/resistance-bridge/picowatt-avs-47/instrument.yaml) | resistance-bridge | no card | GPIB, RS-232, USB | [manual](https://www.picowatt.fi/support/avs47bmanual_20180424_1101_1110.pdf) |  |
| [SRS SIM921 AC resistance bridge](instruments/electronics/resistance-bridge/srs-sim921/instrument.yaml) | resistance-bridge | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM921m.pdf) |  |

### Magnets and field measurement

Magnet power supplies, magnetometers, gaussmeters and teslameters.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [American Magnetics Model 430 magnet power supply programmer](instruments/magnets/magnet-supply/ami-430/instrument.yaml) | magnet-supply | [community](instruments/magnets/magnet-supply/ami-430/card.yaml) | RS-232, LAN | [manual](https://www.americanmagnetics.com/support/manuals/mn-430-rev14.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) +3 |
| [Cryomagnetics Model 4G superconducting magnet power supply](instruments/magnets/magnet-supply/cryomagnetics-4g/instrument.yaml) | magnet-supply | no card | USB, LAN, GPIB | [manual](https://cryomagnetics.com/wp-content/uploads/2022/05/4G-Rev-9_3.pdf) | [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Kepco BOP bipolar operational power supplies](instruments/magnets/magnet-supply/kepco-bop/instrument.yaml) | magnet-supply | no card | GPIB, RS-232, LAN, analog |  |  |
| [Lake Shore Model 625 superconducting magnet power supply](instruments/magnets/magnet-supply/lakeshore-625/instrument.yaml) | magnet-supply | [community](instruments/magnets/magnet-supply/lakeshore-625/card.yaml) | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/625_manual.pdf?sfvrsn=2d9f6b7_1) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml), [Hall effect and magnetoresistance](experiments/transport/hall-magnetoresistance.yaml) |
| [Oxford Instruments IPS120-10 superconducting magnet power supply](instruments/magnets/magnet-supply/oxford-ips120/instrument.yaml) | magnet-supply | no card | RS-232, GPIB | [support](https://qd-oxford.com/services/legacy_product_support.html) |  |
| [Oxford Instruments Mercury iPS superconducting magnet power supply](instruments/magnets/magnet-supply/oxford-mercury-ips/instrument.yaml) | magnet-supply | no card | LAN, RS-232, USB, GPIB | [manual](https://mymercurysupport.com/sites/default/files/59_UMC0072_01.pdf) | [Landau fan and quantum oscillations](experiments/transport/landau-fan.yaml) |
| [Bartington Mag-03 three-axis fluxgate magnetometer](instruments/magnets/magnetometer/bartington-mag-03/instrument.yaml) | magnetometer | no card | analog | [manual](https://www.bartingtondownloads.com/wp-content/uploads/OM1004.pdf) |  |
| [Lake Shore 8600 Series VSM](instruments/magnets/magnetometer/lakeshore-8600/instrument.yaml) | magnetometer | no card |  | [support](https://www.lakeshore.com/products/categories/overview/discontinued-products/discontinued-products/8600-series-vsm) |  |
| [Lake Shore Model 475 DSP gaussmeter](instruments/magnets/gaussmeter/lakeshore-475/instrument.yaml) | gaussmeter | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/475_manual.pdf) |  |
| [Lake Shore F71 / F41 teslameters](instruments/magnets/gaussmeter/lakeshore-f71/instrument.yaml) | gaussmeter | no card | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/f41_f71manual.pdf) |  |
| [Quantum Design OptiCool magneto-optical cryostat](instruments/cryogenics/cryostat/qd-opticool/instrument.yaml) | cryostat | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |

### Microscopy and diffraction

Scanning probe and electron microscopes, optical tweezers and X-ray diffraction.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Asylum Research (Oxford Instruments) AFMs](instruments/microscopy/spm-controller/asylum-afm/instrument.yaml) | spm-controller | no card | USB | [manual](https://afm.oxinst.com/assets/uploads/products/asylum/documents/MacroBuilder-Automating-AFM.pdf) |  |
| [Bruker Dimension AFMs (NanoScope software and NanoScope API)](instruments/microscopy/spm-controller/bruker-afm/instrument.yaml) | spm-controller | no card | LAN | [support](https://www.bruker.com/en/products-and-solutions/microscopes/materials-afm/nanoscope-api.html) |  |
| [RHK Technology R9 SPM controller](instruments/microscopy/spm-controller/rhk-r9/instrument.yaml) | spm-controller | no card | USB | [manual](https://rhk-tech.com/wp-content/uploads/2025/06/AN-7-RHK_R9_MATLAB_Scripting.pdf) |  |
| [SPECS Nanonis SPM controller (TCP programming interface)](instruments/microscopy/spm-controller/specs-nanonis/instrument.yaml) | spm-controller | no card | LAN | [manual](https://raw.githubusercontent.com/SPECS-Zurich-GmbH/nanonis_spm/main/TCPProtocol_SPM.pdf) |  |
| [TESCAN SEM and FIB-SEM systems (SharkSEM remote-control API, Automation SDK)](instruments/microscopy/electron-microscope/tescan-sharksem/instrument.yaml) | electron-microscope | no card | LAN | [support](https://tescan.com/product-portfolio/add-ons/fib-sem-expert-pi-visualcoder) |  |
| [Thermo Fisher SEM and DualBeam (FIB-SEM) systems automated with AutoScript](instruments/microscopy/electron-microscope/thermofisher-autoscript/instrument.yaml) | electron-microscope | no card | LAN | [support](https://documents.thermofisher.com/TFS-Assets/MSD/Datasheets/autoscript-4-datasheet.pdf) |  |
| [ZEISS SEM and FIB-SEM systems (SmartSEM, Python scripting API)](instruments/microscopy/electron-microscope/zeiss-sem/instrument.yaml) | electron-microscope | no card | LAN | [support](https://www.zeiss.com/microscopy/en/products/sem-fib-sem/sem/geminisem-family.html) |  |
| [JPK (Bruker) NanoTracker optical tweezers](instruments/microscopy/optical-tweezers/jpk-nanotracker/instrument.yaml) | optical-tweezers | no card | analog | [support](https://www.bruker.com/en/products-and-solutions/microscopes/optical-tweezers/jpk-nanotracker-2.html) |  |
| [Impetux SENSOCELL optical tweezers](instruments/microscopy/optical-tweezers/impetux-sensocell/instrument.yaml) | optical-tweezers | no card | USB | [support](https://impetux.com/sensocell-optical-tweezers/) |  |
| [LUMICKS C-Trap optical tweezers](instruments/microscopy/optical-tweezers/lumicks-c-trap/instrument.yaml) | optical-tweezers | no card |  | [sign-in](https://help.lumicks.com/bluelake-api/) |  |
| [Bruker D8 X-ray diffractometers (DIFFRAC.SUITE)](instruments/microscopy/x-ray-diffractometer/bruker-d8/instrument.yaml) | x-ray-diffractometer | no card | LAN | [support](https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/diffrac-suite-software/diffrac-measurement-center.html) |  |
| [Photonic Science Laue crystal orientation system](instruments/microscopy/x-ray-diffractometer/photonic-science-laue/instrument.yaml) | x-ray-diffractometer | no card | LAN | [support](https://photonicscience.com/products/laue-single-crystal-orientation-system-laue-family/) |  |
| [Rigaku SmartLab X-ray diffractometer (SmartLab Studio II, RAI)](instruments/microscopy/x-ray-diffractometer/rigaku-smartlab/instrument.yaml) | x-ray-diffractometer | no card | LAN | [support](https://rigaku.com/products/lablinc-studio/rai) |  |
| [ASI MS-2000 and Tiger stage controllers](instruments/motion/motion-stage/asi-ms-2000/instrument.yaml) | motion-stage | no card | RS-232, USB | [manual](https://docs.asiimaging.com/command_quick_start) |  |
| [Prior ProScan III microscope stage controller](instruments/motion/motion-stage/prior-proscan/instrument.yaml) | motion-stage | no card | RS-232, USB | [manual](https://www.prior.com/wp-content/uploads/2026/08/ProScanIII_EN_UK_Manual.pdf) |  |

### Spectroscopy systems

Complete spectrometers for infrared, terahertz, ellipsometry, photoemission and magnetic resonance.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Bruker INVENIO and VERTEX FTIR spectrometers (OPUS)](instruments/spectroscopy/ftir-spectrometer/bruker-ftir/instrument.yaml) | ftir-spectrometer | no card | LAN | [support](https://www.bruker.com/en/products-and-solutions/infrared-and-raman/opus-spectroscopy-software/base-package.html) |  |
| [TOPTICA TeraFlash pro terahertz time-domain spectrometer](instruments/spectroscopy/thz-spectrometer/toptica-teraflash/instrument.yaml) | thz-spectrometer | no card | LAN | [support](https://www.toptica.com/products/terahertz/teraflash-pro) |  |
| [J.A. Woollam spectroscopic ellipsometers (CompleteEASE)](instruments/spectroscopy/ellipsometer/woollam-ellipsometer/instrument.yaml) | ellipsometer | no card | USB, LAN | [support](https://www.jawoollam.com/ellipsometry-software/completeease) |  |
| [Scienta Omicron DA30-L electron analyser for ARPES](instruments/spectroscopy/electron-analyzer/scienta-omicron-da30/instrument.yaml) | electron-analyzer | no card | LAN | [support](https://scientaomicron.com/en/Instruments/Electron-Analysers/DA30-L) |  |
| [SPECS PHOIBOS electron analyzers (SpecsLab Prodigy)](instruments/spectroscopy/electron-analyzer/specs-phoibos/instrument.yaml) | electron-analyzer | no card | LAN | [support](https://www.specs-group.com/specs/products/detail/remote-in/) |  |
| [Tecmag Redstone NMR console (TNMR)](instruments/spectroscopy/nmr-spectrometer/tecmag-redstone/instrument.yaml) | nmr-spectrometer | no card | USB | [support](https://tecmag.com/redstone/) |  |
| [Bruker EMX and ELEXSYS EPR spectrometers (Xepr)](instruments/spectroscopy/epr-spectrometer/bruker-epr/instrument.yaml) | epr-spectrometer | no card | LAN | [support](https://www.bruker.com/en/products-and-solutions/mr/epr-instruments/epr-research-instruments/xepr-software.html) |  |

### Materials synthesis and fabrication

Furnace and process controllers, mass-flow controllers, deposition monitors and lithography.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Eurotherm 3200, 3500 and 2400 controllers](instruments/synthesis/process-controller/eurotherm-3200/instrument.yaml) | process-controller | no card | RS-232, RS-485, LAN | [manual](https://www.eurotherm.com/?wpdmdl=27913) |  |
| [Watlow F4T controllers](instruments/synthesis/process-controller/watlow-f4t/instrument.yaml) | process-controller | no card | LAN, RS-485 | [manual](https://www.watlow.com/-/media/documents/software-and-demos/f4t-register-list-2025-05-15.ashx) |  |
| [Alicat mass flow controllers](instruments/synthesis/flow-controller/alicat-mfc/instrument.yaml) | flow-controller | no card | RS-232, RS-485, LAN, analog | [manual](https://documents.alicat.com/Alicat-Serial-Primer.pdf) |  |
| [Bronkhorst EL-FLOW mass flow controllers](instruments/synthesis/flow-controller/bronkhorst-el-flow/instrument.yaml) | flow-controller | no card | RS-232, RS-485, USB, LAN, analog | [manual](https://products.bronkhorst.com/media/rskkdfei/917027-manual-rs232-interface.pdf) |  |
| [MKS G-Series mass flow controllers](instruments/synthesis/flow-controller/mks-mfc/instrument.yaml) | flow-controller | no card | RS-485, analog | [sign-in](https://www.mks.com/f/ge50a-mass-flow-controller) |  |
| [INFICON SQC-310 and SQM-160 deposition controllers](instruments/synthesis/deposition-monitor/inficon-sqc-310/instrument.yaml) | deposition-monitor | no card | RS-232, USB, LAN | [support](https://www.inficon.com/en/products/thin-film-technology/sqc-310) |  |
| [JC Nabity NPGS lithography system](instruments/synthesis/lithography/nabity-npgs/instrument.yaml) | lithography | no card | PCIe, analog | [support](https://www.jcnabity.com/sysdesc.htm) |  |
| [Raith ELPHY lithography attachment](instruments/synthesis/lithography/raith-elphy/instrument.yaml) | lithography | no card | analog | [support](https://raith.com/products/elphy/) |  |

## Experiments

### Electrical transport

Resistance, Hall effect, gating, tunneling and superconductivity, DC and with lock-ins.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml) | source, voltmeter, cryostat | [ppms-transport](labs/ppms-transport.yaml) | 2 |
| [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) | bias, lockin, iamp, dmm, temperature | [cryostat-electrical](labs/cryostat-electrical.yaml) | 2 |
| [Field-effect gate sweep](experiments/transport/gate-sweep.yaml) | gate, lockin, cryostat (optional) | [ppms-transport](labs/ppms-transport.yaml) | 1 |
| [Hall effect and magnetoresistance](experiments/transport/hall-magnetoresistance.yaml) | cryostat, lockin_xx, lockin_xy | [ppms-transport](labs/ppms-transport.yaml) | 2 |
| [Current-voltage characteristics](experiments/transport/iv-curve.yaml) | smu, voltmeter (optional), temperature (optional) | [cryostat-electrical](labs/cryostat-electrical.yaml) | 1 |
| [Landau fan and quantum oscillations](experiments/transport/landau-fan.yaml) | cryostat, gate, lockin_xx, lockin_xy | [ppms-transport](labs/ppms-transport.yaml) | 1 |
| [Nonlinear Hall effect (second harmonic)](experiments/transport/nonlinear-hall.yaml) | lockin_drive, lockin_2w, cryostat | [ppms-transport](labs/ppms-transport.yaml) | 3 |
| [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) | lockin, temperature, preamp (optional) | [cryostat-electrical](labs/cryostat-electrical.yaml) | 2 |

### Magnetometry

Magnetization and susceptibility.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml) | lockin, temperature | [cryostat-electrical](labs/cryostat-electrical.yaml) | 2 |
| [SQUID magnetometry (M-T and M-H)](experiments/magnetometry/squid-magnetometry.yaml) | magnetometer |  |  |

### Optical spectroscopy and imaging

Photoluminescence, Raman, reflectance, photocurrent and magneto-optics.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Magneto-optical Kerr effect](experiments/optics/moke.yaml) | laser, modulation, lockin, magnet | [magneto-optics](labs/magneto-optics.yaml) | 1 |
| [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) | laser, modulation, lockin, iamp, scanner, gate (optional) | [confocal-optics](labs/confocal-optics.yaml) | 2 |
| [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) | laser, spectrograph, camera, power_meter, temperature (optional) | [confocal-optics](labs/confocal-optics.yaml) | 2 |
| [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml) | laser, scanner, spectrograph, camera | [confocal-optics](labs/confocal-optics.yaml) | 1 |
| [Raman spectroscopy](experiments/optics/raman.yaml) | laser, spectrograph, camera, temperature (optional), polarizer (optional) | [confocal-optics](labs/confocal-optics.yaml) | 1 |
| [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) | spectrograph, camera, scanner | [confocal-optics](labs/confocal-optics.yaml) | 1 |

### Ultrafast and nonlinear optics

Second-harmonic generation and pump-probe spectroscopy.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) | laser, delay, chopper, lockin, cryostat (optional) |  | needs a card: motion-stage, chopper |
| [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) | laser, polarization, detector, chopper (optional), cryostat (optional) |  | needs a card: motion-stage |

### Spin resonance and quantum sensing

NV-center ODMR and coherence, ferromagnetic resonance.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) | magnet, microwave, lockin, vna (optional) | [fmr](labs/fmr.yaml) | 2 |
| [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml) | pulses, microwave, counter, aom, laser | [nv-odmr](labs/nv-odmr.yaml) | 4 |
| [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) | pulses, microwave, counter, aom, laser | [nv-odmr](labs/nv-odmr.yaml) | 2 |

### Quantum devices

Superconducting resonators and qubits, quantum dots.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) | gate, bias, iamp, dmm, lockin (optional), fridge | [cryostat-electrical](labs/cryostat-electrical.yaml) | 1 |
| [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) | controller, sources (optional), fridge |  | needs a card: quantum-controller |
| [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) | readout, fridge | [qick-resonator](labs/qick-resonator.yaml) | 2 |

### Acoustics and phononics

Surface acoustic waves, acoustoelectric and magnetoacoustic effects.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml) | rf, voltmeter, cryostat | [saw](labs/saw.yaml) | 2 |
| [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml) | vna, cryostat, gate (optional) |  | needs a card: vna |

### Atomic, molecular and optical control

AOMs, tunable lasers and wavelength scans.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml) | aom, power_meter | [aom-bench](labs/aom-bench.yaml) | 2 |
| [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) | laser, counter, power_meter, wavemeter (optional) | [tunable-laser](labs/tunable-laser.yaml) | 1 |

### Sample environment

Cooldowns, temperature steps and field ramps.

| Experiment | Instruments | Lab config | Plans |
|---|---|---|---|
| [Cooldown log](experiments/environment/cooldown-log.yaml) | temperature, lockin (optional) | [cryostat-electrical](labs/cryostat-electrical.yaml) | 1 |

## Lab configs

Copy one to `~/Kelvin/lab.yaml` (or open it in **Lab → Set up…**), then give each instrument its address. Without addresses every instrument is simulated.

| Lab config | Instruments | Used by |
|---|---|---|
| [AOM bench](labs/aom-bench.yaml) | aom (moglabs/xrf), pm (thorlabs/pm100) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml) |
| [Confocal optics](labs/confocal-optics.yaml) | laser (coherent/obis), fg (keysight/33500b), lockin (srs/sr830), iamp (srs/sr570), gate (keithley/2450), scan_x (pi/gcs-piezo), scan_y (pi/gcs-piezo), spectrograph (princeton/spectrapro), camera (princeton/picam), pm (thorlabs/pm100), tc (lakeshore/336) | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [Cryostat electrical bench](labs/cryostat-electrical.yaml) | tc (lakeshore/336), lockin (srs/sr830), smu (keithley/2450), gate (keithley/2400), bias (yokogawa/gs200), iamp (srs/sr570), dmm (keysight/34465a) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml), [Current-voltage characteristics](experiments/transport/iv-curve.yaml), [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [FMR](labs/fmr.yaml) | magnet (ami/430), mw (rs/smb100a), lockin (srs/sr830) | [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Magneto-optics](labs/magneto-optics.yaml) | cryo (qd/multivu), laser (coherent/obis), fg (keysight/33500b), lockin (srs/sr830), pm (thorlabs/pm100) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |
| [NV ODMR](labs/nv-odmr.yaml) | pg (swabian/pulse-streamer), mw (srs/sg384), counter (swabian/time-tagger), aom (moglabs/xrf), laser (coherent/obis) | [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [PPMS transport](labs/ppms-transport.yaml) | cryo (qd/multivu), lockin_xx (srs/sr830), lockin_xy (srs/sr830), gate (keithley/2400), source (yokogawa/gs200), nvm (keithley/2182a) | [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml), [Field-effect gate sweep](experiments/transport/gate-sweep.yaml), [Hall effect and magnetoresistance](experiments/transport/hall-magnetoresistance.yaml), [Landau fan and quantum oscillations](experiments/transport/landau-fan.yaml), [Nonlinear Hall effect (second harmonic)](experiments/transport/nonlinear-hall.yaml) |
| [QICK resonator readout](labs/qick-resonator.yaml) | rfsoc (qick/rfsoc) | [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [SAW](labs/saw.yaml) | cryo (qd/multivu), rf (srs/sg384), nvm (keithley/2182a) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml) |
| [Tunable laser](labs/tunable-laser.yaml) | laser (m2/solstis), counter (swabian/time-tagger), pm (thorlabs/pm100) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |

## Wanted cards

Experiments that need an instrument no card covers yet, and the catalogued models that would fill the gap. Kelvin can draft these cards from the manuals listed here.

- **vna** for [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml): [Copper Mountain 2-port USB VNAs (S5048, S5065, M5180 and similar) via the S2VNA software](instruments/rf-microwave/vna/copper-mountain-s2vna/instrument.yaml), [Keysight E5071C ENA vector network analyzer](instruments/rf-microwave/vna/keysight-e5071c/instrument.yaml), [Keysight E5080B ENA vector network analyzer](instruments/rf-microwave/vna/keysight-e5080b/instrument.yaml), [Rohde & Schwarz ZNB vector network analyzer](instruments/rf-microwave/vna/rs-znb/instrument.yaml)
- **quantum-controller** for [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml): [Intermodulation Products Presto](instruments/rf-microwave/quantum-controller/intermod-presto/instrument.yaml), [Qblox Cluster qubit control system](instruments/rf-microwave/quantum-controller/qblox-cluster/instrument.yaml), [Quantum Machines OPX+ / OPX1000 quantum controller (QUA)](instruments/rf-microwave/quantum-controller/quantum-machines-opx/instrument.yaml), [Zurich Instruments SHFQC qubit controller](instruments/rf-microwave/quantum-controller/zhinst-shfqc/instrument.yaml)
- **motion-stage** for [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml): [ASI MS-2000 and Tiger stage controllers](instruments/motion/motion-stage/asi-ms-2000/instrument.yaml), [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](instruments/motion/motion-stage/newport-conex-cc/instrument.yaml), [Newport ESP301 three-axis motion controller](instruments/motion/motion-stage/newport-esp301/instrument.yaml), [Newport SMC100CC / SMC100PP single-axis motion controller](instruments/motion/motion-stage/newport-smc100/instrument.yaml), [Newport XPS-D / XPS-RL universal high-performance motion controller](instruments/motion/motion-stage/newport-xps/instrument.yaml), [Physik Instrumente C-863 Mercury DC motor controller](instruments/motion/motion-stage/pi-c-863/instrument.yaml), [Prior ProScan III microscope stage controller](instruments/motion/motion-stage/prior-proscan/instrument.yaml), [Thorlabs K10CR1 motorized rotation mount](instruments/motion/motion-stage/thorlabs-k10cr1/instrument.yaml), [Thorlabs KDC101 K-Cube brushed DC servo motor controller](instruments/motion/motion-stage/thorlabs-kdc101/instrument.yaml)
- **chopper** for [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml): [Thorlabs MC2000B optical chopper](instruments/optics/chopper/thorlabs-mc2000b/instrument.yaml)
- **motion-stage** for [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml): [ASI MS-2000 and Tiger stage controllers](instruments/motion/motion-stage/asi-ms-2000/instrument.yaml), [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](instruments/motion/motion-stage/newport-conex-cc/instrument.yaml), [Newport ESP301 three-axis motion controller](instruments/motion/motion-stage/newport-esp301/instrument.yaml), [Newport SMC100CC / SMC100PP single-axis motion controller](instruments/motion/motion-stage/newport-smc100/instrument.yaml), [Newport XPS-D / XPS-RL universal high-performance motion controller](instruments/motion/motion-stage/newport-xps/instrument.yaml), [Physik Instrumente C-863 Mercury DC motor controller](instruments/motion/motion-stage/pi-c-863/instrument.yaml), [Prior ProScan III microscope stage controller](instruments/motion/motion-stage/prior-proscan/instrument.yaml), [Thorlabs K10CR1 motorized rotation mount](instruments/motion/motion-stage/thorlabs-k10cr1/instrument.yaml), [Thorlabs KDC101 K-Cube brushed DC servo motor controller](instruments/motion/motion-stage/thorlabs-kdc101/instrument.yaml)

## Makers

- **Agilent:** [4UHV](instruments/cryogenics/vacuum-pump/agilent-4uhv/instrument.yaml)
- **aixACCT Systems:** [TF Analyzer](instruments/electronics/ferroelectric-tester/aixacct-tf-analyzer/instrument.yaml)
- **AlazarTech:** [ATS9870](instruments/electronics/oscilloscope/alazartech-ats9870/instrument.yaml)
- **Alicat Scientific:** [MC series](instruments/synthesis/flow-controller/alicat-mfc/instrument.yaml)
- **Almax easyLab:** [iGM](instruments/cryogenics/pressure-controller/almax-easylab-membrane/instrument.yaml)
- **American Magnetics:** [1700](instruments/cryogenics/level-meter/ami-1700/instrument.yaml), [430](instruments/magnets/magnet-supply/ami-430/instrument.yaml)
- **Andeen-Hagerling:** [AH 2700A](instruments/electronics/capacitance-bridge/andeen-hagerling-ah2700a/instrument.yaml)
- **Andor (Oxford Instruments):** [CCD and EMCCD](instruments/optics/camera/andor-ccd/instrument.yaml), [sCMOS](instruments/optics/camera/andor-scmos/instrument.yaml), [Shamrock / Kymera](instruments/optics/monochromator/andor-shamrock/instrument.yaml)
- **Anritsu:** [MS9740A](instruments/optics/optical-spectrum-analyzer/anritsu-ms9740/instrument.yaml)
- **APE Angewandte Physik und Elektronik:** [pulseCheck](instruments/optics/autocorrelator/ape-pulsecheck/instrument.yaml)
- **Applied Scientific Instrumentation:** [MS-2000](instruments/motion/motion-stage/asi-ms-2000/instrument.yaml)
- **Asylum Research:** [MFP-3D / Cypher / Jupiter](instruments/microscopy/spm-controller/asylum-afm/instrument.yaml)
- **attocube:** [attoDRY](instruments/cryogenics/cryostat/attocube-attodry/instrument.yaml), [AMC300](instruments/motion/positioner/attocube-amc/instrument.yaml), [ANC300](instruments/motion/positioner/attocube-anc300/instrument.yaml), [ANC350](instruments/motion/positioner/attocube-anc350/instrument.yaml)
- **Avtech Electrosystems:** [-B series](instruments/timing/pulse-generator/avtech-pulse-generator/instrument.yaml)
- **Azurlight Systems:** [ALS](instruments/lasers/laser/azurlight-als/instrument.yaml)
- **Bartington Instruments:** [Mag-03](instruments/magnets/magnetometer/bartington-mag-03/instrument.yaml)
- **Basel Precision Instruments:** [SP1060](instruments/electronics/voltage-source/basel-lnhr-dac/instrument.yaml)
- **Basler:** [ace / dart](instruments/optics/camera/basler-camera/instrument.yaml)
- **Berkeley Nucleonics:** [577](instruments/timing/delay-generator/bnc-577/instrument.yaml)
- **Bluefors:** [LD / XLD / SD / LH series](instruments/cryogenics/dilution-refrigerator/bluefors-dilution-refrigerator/instrument.yaml)
- **Bristol Instruments:** [671](instruments/lasers/wavemeter/bristol-wavemeter/instrument.yaml)
- **Bronkhorst:** [EL-FLOW Select](instruments/synthesis/flow-controller/bronkhorst-el-flow/instrument.yaml)
- **Bruker:** [NanoScope 6 / Dimension](instruments/microscopy/spm-controller/bruker-afm/instrument.yaml), [D8 ADVANCE / D8 DISCOVER](instruments/microscopy/x-ray-diffractometer/bruker-d8/instrument.yaml), [EMX / ELEXSYS](instruments/spectroscopy/epr-spectrometer/bruker-epr/instrument.yaml), [INVENIO / VERTEX](instruments/spectroscopy/ftir-spectrometer/bruker-ftir/instrument.yaml)
- **Bruker (JPK):** [NanoTracker 2](instruments/microscopy/optical-tweezers/jpk-nanotracker/instrument.yaml)
- **Coherent:** [Chameleon Ultra](instruments/lasers/laser/coherent-chameleon/instrument.yaml), [COMPexPro](instruments/lasers/laser/coherent-compex/instrument.yaml), [Mephisto](instruments/lasers/laser/coherent-mephisto/instrument.yaml), [OBIS](instruments/lasers/laser/coherent-obis/instrument.yaml), [Verdi](instruments/lasers/laser/coherent-verdi/instrument.yaml)
- **Copper Mountain:** [S2VNA](instruments/rf-microwave/vna/copper-mountain-s2vna/instrument.yaml)
- **Covesion (Hawthorn Photonics):** [OC2 / OC3](instruments/quantum-optics/crystal-oven/covesion-oven/instrument.yaml)
- **Cryo-con:** [24C](instruments/cryogenics/temperature-controller/cryocon-24c/instrument.yaml)
- **Cryomagnetics:** [LM-510](instruments/cryogenics/level-meter/cryomagnetics-lm-510/instrument.yaml), [4G](instruments/magnets/magnet-supply/cryomagnetics-4g/instrument.yaml)
- **Cryomech (Bluefors):** [CPA](instruments/cryogenics/compressor/cryomech-cpa/instrument.yaml)
- **Delta Elektronika:** [SM series](instruments/electronics/power-supply/delta-elektronika-sm/instrument.yaml)
- **DiCon Fiberoptics:** [GP700](instruments/optics/fiber-optics/dicon-gp700/instrument.yaml)
- **Edwards Vacuum (Atlas Copco):** [TIC](instruments/cryogenics/vacuum-pump/edwards-tic/instrument.yaml)
- **Energetiq (Hamamatsu):** [EQ-99X](instruments/optics/light-source/energetiq-eq-99x/instrument.yaml)
- **Eurotherm (Watlow):** [3200 series](instruments/synthesis/process-controller/eurotherm-3200/instrument.yaml)
- **Excelitas:** [SPCM-AQRH](instruments/quantum-optics/single-photon-detector/excelitas-spcm-aqrh/instrument.yaml)
- **FEMTO:** [DLPCA-200](instruments/electronics/preamp/femto-dlpca-200/instrument.yaml)
- **Gamma Vacuum:** [SPCe](instruments/cryogenics/vacuum-pump/gamma-vacuum-spce/instrument.yaml)
- **Hamamatsu:** [ORCA-Flash4.0 V3](instruments/optics/camera/hamamatsu-orca/instrument.yaml), [X13138](instruments/optics/spatial-light-modulator/hamamatsu-lcos-slm/instrument.yaml)
- **HighFinesse:** [WS7](instruments/lasers/wavemeter/highfinesse-wavemeter/instrument.yaml)
- **Hinds Instruments:** [PEM-200](instruments/optics/modulator/hinds-pem/instrument.yaml)
- **HOLOEYE Photonics:** [PLUTO-2.1](instruments/optics/spatial-light-modulator/holoeye-slm/instrument.yaml)
- **HORIBA:** [iHR320](instruments/optics/spectrometer/horiba-ihr/instrument.yaml)
- **HP / Agilent:** [34401A](instruments/electronics/multimeter/hp-34401a/instrument.yaml)
- **HÜBNER Photonics:** [06-01](instruments/lasers/laser/hubner-cobolt/instrument.yaml), [C-WAVE](instruments/lasers/parametric-source/hubner-c-wave/instrument.yaml)
- **ID Quantique:** [ID100](instruments/quantum-optics/single-photon-detector/idquantique-id100/instrument.yaml), [ID281](instruments/quantum-optics/snspd/idquantique-id281/instrument.yaml), [ID900](instruments/timing/photon-counter/idquantique-id900/instrument.yaml)
- **Impetux Optics:** [SENSOCELL](instruments/microscopy/optical-tweezers/impetux-sensocell/instrument.yaml)
- **INFICON:** [SQC-310](instruments/synthesis/deposition-monitor/inficon-sqc-310/instrument.yaml)
- **Instec:** [mK2000](instruments/cryogenics/heating-stage/instec-mk2000/instrument.yaml)
- **Intermodulation Products:** [Presto](instruments/rf-microwave/quantum-controller/intermod-presto/instrument.yaml)
- **IPG Photonics:** [YLR](instruments/lasers/laser/ipg-ylr/instrument.yaml)
- **J.A. Woollam:** [RC2 / M-2000 / alpha 2.0](instruments/spectroscopy/ellipsometer/woollam-ellipsometer/instrument.yaml)
- **J.C. Nabity Lithography Systems:** [NPGS](instruments/synthesis/lithography/nabity-npgs/instrument.yaml)
- **JULABO:** [Circulators](instruments/cryogenics/chiller/julabo-circulator/instrument.yaml)
- **Keithley (Tektronix):** [6221](instruments/electronics/current-source/keithley-6221/instrument.yaml), [6485](instruments/electronics/electrometer/keithley-6485/instrument.yaml), [6517B](instruments/electronics/electrometer/keithley-6517b/instrument.yaml), [2000](instruments/electronics/multimeter/keithley-2000/instrument.yaml), [2700](instruments/electronics/multimeter/keithley-2700/instrument.yaml), [DMM6500](instruments/electronics/multimeter/keithley-dmm6500/instrument.yaml), [2182A](instruments/electronics/nanovoltmeter/keithley-2182a/instrument.yaml), [4200A-SCS](instruments/electronics/parameter-analyzer/keithley-4200a/instrument.yaml), [2400](instruments/electronics/source-meter/keithley-2400/instrument.yaml), [2450](instruments/electronics/source-meter/keithley-2450/instrument.yaml), [2636B](instruments/electronics/source-meter/keithley-2636b/instrument.yaml), [6430](instruments/electronics/source-meter/keithley-6430/instrument.yaml), [707B](instruments/electronics/switch-matrix/keithley-707b/instrument.yaml)
- **Kepco:** [BOP](instruments/magnets/magnet-supply/kepco-bop/instrument.yaml)
- **Keysight:** [M3202A](instruments/electronics/awg/keysight-m3202a/instrument.yaml), [33220A](instruments/electronics/function-generator/keysight-33220a/instrument.yaml), [33500B](instruments/electronics/function-generator/keysight-33500b/instrument.yaml), [E4980A](instruments/electronics/lcr-meter/keysight-e4980a/instrument.yaml), [34465A](instruments/electronics/multimeter/keysight-34465a/instrument.yaml), [InfiniiVision 3000 X-Series](instruments/electronics/oscilloscope/keysight-dsox3000/instrument.yaml), [B1500A](instruments/electronics/parameter-analyzer/keysight-b1500a/instrument.yaml), [E36312A](instruments/electronics/power-supply/keysight-e36300/instrument.yaml), [B2900](instruments/electronics/source-meter/keysight-b2900/instrument.yaml), [8164B](instruments/optics/fiber-optics/keysight-8164b/instrument.yaml), [E8257D](instruments/rf-microwave/microwave-source/keysight-e8257d/instrument.yaml), [N5183B](instruments/rf-microwave/microwave-source/keysight-n5183b/instrument.yaml), [U2000A](instruments/rf-microwave/rf-power-meter/keysight-u2000/instrument.yaml), [N9020B](instruments/rf-microwave/spectrum-analyzer/keysight-n9020b/instrument.yaml), [E5071C](instruments/rf-microwave/vna/keysight-e5071c/instrument.yaml), [E5080B](instruments/rf-microwave/vna/keysight-e5080b/instrument.yaml), [53230A](instruments/timing/frequency-counter/keysight-53230a/instrument.yaml), [81160A](instruments/timing/pulse-generator/keysight-81160a/instrument.yaml)
- **Lake Shore Cryotronics:** [218](instruments/cryogenics/temperature-controller/lakeshore-218/instrument.yaml), [331](instruments/cryogenics/temperature-controller/lakeshore-331/instrument.yaml), [336](instruments/cryogenics/temperature-controller/lakeshore-336/instrument.yaml), [340](instruments/cryogenics/temperature-controller/lakeshore-340/instrument.yaml), [350](instruments/cryogenics/temperature-controller/lakeshore-350/instrument.yaml), [370](instruments/electronics/resistance-bridge/lakeshore-370/instrument.yaml), [372](instruments/electronics/resistance-bridge/lakeshore-372/instrument.yaml), [475](instruments/magnets/gaussmeter/lakeshore-475/instrument.yaml), [F71](instruments/magnets/gaussmeter/lakeshore-f71/instrument.yaml), [625](instruments/magnets/magnet-supply/lakeshore-625/instrument.yaml), [8600](instruments/magnets/magnetometer/lakeshore-8600/instrument.yaml)
- **Light Conversion:** [PHAROS](instruments/lasers/laser/lightcon-pharos/instrument.yaml), [ORPHEUS](instruments/lasers/parametric-source/lightcon-orpheus/instrument.yaml), [TOPAS](instruments/lasers/parametric-source/lightcon-topas/instrument.yaml)
- **Linkam Scientific Instruments:** [T96](instruments/cryogenics/heating-stage/linkam-t96/instrument.yaml)
- **Liquid Instruments:** [Moku:Pro](instruments/electronics/fpga-instrument/liquid-instruments-moku/instrument.yaml)
- **LUMICKS:** [C-Trap](instruments/microscopy/optical-tweezers/lumicks-c-trap/instrument.yaml)
- **M Squared:** [SolsTiS](instruments/lasers/laser/m2-solstis/instrument.yaml)
- **M-Labs:** [Kasli](instruments/timing/sequencer/m-labs-artiq-sinara/instrument.yaml)
- **Mad City Labs:** [Nano-Drive](instruments/motion/positioner/mcl-nano-drive/instrument.yaml)
- **Meadowlark Optics:** [SLM](instruments/optics/spatial-light-modulator/meadowlark-slm/instrument.yaml)
- **Menlo Systems:** [FC1500](instruments/lasers/frequency-comb/menlo-fc1500/instrument.yaml)
- **Micro Photon Devices:** [PDM](instruments/quantum-optics/single-photon-detector/mpd-pdm/instrument.yaml)
- **Mini-Circuits:** [RCDAT](instruments/rf-microwave/rf-attenuator/minicircuits-rcdat/instrument.yaml), [RC series](instruments/rf-microwave/rf-switch/minicircuits-rf-switch/instrument.yaml)
- **MKS Instruments:** [GE50A](instruments/synthesis/flow-controller/mks-mfc/instrument.yaml)
- **MOGLabs:** [DLC-202](instruments/lasers/laser-driver/moglabs-dlc-202/instrument.yaml), [FSC](instruments/lasers/laser-lock/moglabs-fsc/instrument.yaml), [XRF](instruments/rf-microwave/aom-driver/moglabs-xrf/instrument.yaml)
- **Montana Instruments:** [Cryostation s-series](instruments/cryogenics/cryostat/montana-cryostation/instrument.yaml)
- **Newport (MKS):** [CONEX-CC](instruments/motion/motion-stage/newport-conex-cc/instrument.yaml), [ESP301](instruments/motion/motion-stage/newport-esp301/instrument.yaml), [SMC100CC](instruments/motion/motion-stage/newport-smc100/instrument.yaml), [XPS-D](instruments/motion/motion-stage/newport-xps/instrument.yaml), [69911](instruments/optics/light-source/newport-69911/instrument.yaml), [Cornerstone 130](instruments/optics/monochromator/newport-cornerstone/instrument.yaml), [2936-R](instruments/optics/power-meter/newport-2936-r/instrument.yaml)
- **NF Corporation:** [LI5660](instruments/electronics/lock-in/nf-li5660/instrument.yaml), [CA5351](instruments/electronics/preamp/nf-ca5351/instrument.yaml)
- **NI (National Instruments):** [DAQmx devices](instruments/electronics/daq/ni-daqmx/instrument.yaml)
- **NKT Photonics:** [SuperK EXTREME](instruments/lasers/laser/nkt-superk/instrument.yaml)
- **Novatech:** [409B](instruments/rf-microwave/aom-driver/novatech-409b/instrument.yaml)
- **Nüvü Camēras:** [HNü 512](instruments/optics/camera/nuvu-hnu/instrument.yaml)
- **Ocean Insight:** [USB spectrometers](instruments/optics/spectrometer/ocean-spectrometer/instrument.yaml)
- **Oxford Instruments:** [Triton](instruments/cryogenics/dilution-refrigerator/oxford-triton/instrument.yaml), [ILM200](instruments/cryogenics/level-meter/oxford-ilm200/instrument.yaml), [ITC503](instruments/cryogenics/temperature-controller/oxford-itc503/instrument.yaml), [Mercury iTC](instruments/cryogenics/temperature-controller/oxford-mercury-itc/instrument.yaml), [IPS120-10](instruments/magnets/magnet-supply/oxford-ips120/instrument.yaml), [Mercury iPS](instruments/magnets/magnet-supply/oxford-mercury-ips/instrument.yaml)
- **OZ Optics:** [EPS-1000](instruments/quantum-optics/photon-source/ozoptics-entangled-source/instrument.yaml)
- **Pfeiffer Vacuum:** [TPG 362](instruments/cryogenics/vacuum-gauge/pfeiffer-tpg36x/instrument.yaml), [HiCube](instruments/cryogenics/vacuum-pump/pfeiffer-hicube/instrument.yaml)
- **Photon Spot:** [Cryospot](instruments/quantum-optics/snspd/photon-spot-snspd/instrument.yaml)
- **Photonic Science:** [Laue crystal orientation system](instruments/microscopy/x-ray-diffractometer/photonic-science-laue/instrument.yaml)
- **Physik Instrumente (PI):** [C-863](instruments/motion/motion-stage/pi-c-863/instrument.yaml), [E-727 / E-709 / E-712](instruments/motion/positioner/pi-gcs-piezo/instrument.yaml)
- **Pico Technology:** [PicoScope](instruments/electronics/oscilloscope/pico-picoscope/instrument.yaml)
- **PicoQuant:** [PDL 800-D](instruments/lasers/laser-driver/picoquant-pdl-800/instrument.yaml), [HydraHarp 400](instruments/timing/photon-counter/picoquant-hydraharp-400/instrument.yaml), [MultiHarp 150](instruments/timing/photon-counter/picoquant-multiharp-150/instrument.yaml)
- **Picowatt (RV-Elektroniikka):** [AVS-47B](instruments/electronics/resistance-bridge/picowatt-avs-47/instrument.yaml)
- **Pixel Photonics:** [Dena](instruments/quantum-optics/snspd/pixel-photonics-snspd/instrument.yaml)
- **Prior Scientific:** [ProScan III](instruments/motion/motion-stage/prior-proscan/instrument.yaml)
- **Qblox:** [Cluster](instruments/rf-microwave/quantum-controller/qblox-cluster/instrument.yaml)
- **QDevil (Quantum Machines):** [QDAC-II](instruments/electronics/voltage-source/qdevil-qdac-ii/instrument.yaml)
- **QICK (open source):** [RFSoC boards](instruments/electronics/awg/qick-rfsoc/instrument.yaml)
- **Quandela:** [Prometheus](instruments/quantum-optics/photon-source/quandela-prometheus/instrument.yaml)
- **Quantum Design:** [MultiVu systems](instruments/cryogenics/cryostat/qd-multivu/instrument.yaml), [OptiCool](instruments/cryogenics/cryostat/qd-opticool/instrument.yaml)
- **Quantum Machines:** [Octave](instruments/rf-microwave/frequency-converter/quantum-machines-octave/instrument.yaml), [OPX+](instruments/rf-microwave/quantum-controller/quantum-machines-opx/instrument.yaml)
- **Quantum Opus:** [Opus One](instruments/quantum-optics/snspd/quantum-opus-opus-one/instrument.yaml)
- **Qubitekk (IonQ):** [Entangled photon source](instruments/quantum-optics/photon-source/qubitekk-entangled-source/instrument.yaml)
- **qutools:** [quED](instruments/quantum-optics/photon-source/qutools-qued/instrument.yaml), [quTAG](instruments/timing/photon-counter/qutools-qutag/instrument.yaml)
- **Radiant Technologies:** [Precision](instruments/electronics/ferroelectric-tester/radiant-precision/instrument.yaml)
- **Raith:** [ELPHY](instruments/synthesis/lithography/raith-elphy/instrument.yaml)
- **Razorbill Instruments:** [RP100](instruments/cryogenics/strain-cell/razorbill-rp100/instrument.yaml)
- **Red Pitaya:** [STEMlab](instruments/electronics/fpga-instrument/red-pitaya-stemlab/instrument.yaml)
- **RHK Technology:** [R9 / R9 Plus](instruments/microscopy/spm-controller/rhk-r9/instrument.yaml)
- **Rigaku:** [SmartLab](instruments/microscopy/x-ray-diffractometer/rigaku-smartlab/instrument.yaml)
- **Rigol:** [DG1000Z](instruments/electronics/awg/rigol-dg1000z/instrument.yaml)
- **Rohde & Schwarz:** [SGS100A](instruments/rf-microwave/microwave-source/rs-sgs100a/instrument.yaml), [SMB100A](instruments/rf-microwave/microwave-source/rs-smb100a/instrument.yaml), [NRP](instruments/rf-microwave/rf-power-meter/rs-nrp/instrument.yaml), [ZNB](instruments/rf-microwave/vna/rs-znb/instrument.yaml)
- **SAES Getters:** [NEXTorr](instruments/cryogenics/vacuum-pump/saes-nextorr/instrument.yaml)
- **santec:** [SLM-200](instruments/optics/spatial-light-modulator/santec-slm-200/instrument.yaml)
- **Scienta Omicron:** [DA30-L](instruments/spectroscopy/electron-analyzer/scienta-omicron-da30/instrument.yaml)
- **Signal Hound:** [BB60C](instruments/rf-microwave/spectrum-analyzer/signalhound-bb60/instrument.yaml)
- **Signal Recovery (AMETEK):** [7270](instruments/electronics/lock-in/signal-recovery-7270/instrument.yaml)
- **SignalCore:** [SC5511A](instruments/rf-microwave/microwave-source/signalcore-sc5511a/instrument.yaml)
- **Single Quantum:** [Eos](instruments/quantum-optics/snspd/single-quantum-eos/instrument.yaml)
- **SmarAct:** [MCS2](instruments/motion/positioner/smaract-mcs2/instrument.yaml)
- **Solartron Analytical (AMETEK):** [1260A](instruments/electronics/lcr-meter/solartron-1260/instrument.yaml)
- **Sparrow Quantum:** [Sparrow Nest](instruments/quantum-optics/photon-source/sparrow-quantum-sparrow/instrument.yaml)
- **SPECS Zurich:** [Nanonis SPM Controller](instruments/microscopy/spm-controller/specs-nanonis/instrument.yaml), [PHOIBOS 150 / SpecsLab Prodigy](instruments/spectroscopy/electron-analyzer/specs-phoibos/instrument.yaml)
- **Spectra-Physics (MKS):** [Mai Tai](instruments/lasers/laser/spectra-physics-mai-tai/instrument.yaml)
- **Spectrum Instrumentation:** [M4i.66xx](instruments/electronics/awg/spectrum-m4i-66xx/instrument.yaml)
- **SpinCore:** [PulseBlaster](instruments/timing/pulse-generator/spincore-pulseblaster/instrument.yaml)
- **Stanford Research Systems:** [RGA100](instruments/cryogenics/rga/srs-rga/instrument.yaml), [SIM922](instruments/cryogenics/temperature-controller/srs-sim922/instrument.yaml), [DS345](instruments/electronics/function-generator/srs-ds345/instrument.yaml), [SR830](instruments/electronics/lock-in/srs-sr830/instrument.yaml), [SR844](instruments/electronics/lock-in/srs-sr844/instrument.yaml), [SR850](instruments/electronics/lock-in/srs-sr850/instrument.yaml), [SR860](instruments/electronics/lock-in/srs-sr860/instrument.yaml), [SIM900](instruments/electronics/mainframe/srs-sim900/instrument.yaml), [SIM970](instruments/electronics/multimeter/srs-sim970/instrument.yaml), [SIM960](instruments/electronics/pid-controller/srs-sim960/instrument.yaml), [SR560](instruments/electronics/preamp/srs-sr560/instrument.yaml), [SR570](instruments/electronics/preamp/srs-sr570/instrument.yaml), [SIM921](instruments/electronics/resistance-bridge/srs-sim921/instrument.yaml), [SR1](instruments/electronics/signal-analyzer/srs-sr1/instrument.yaml), [SR785](instruments/electronics/signal-analyzer/srs-sr785/instrument.yaml), [SIM928](instruments/electronics/voltage-source/srs-sim928/instrument.yaml), [SG384](instruments/rf-microwave/microwave-source/srs-sg384/instrument.yaml), [DG645](instruments/timing/delay-generator/srs-dg645/instrument.yaml), [SR620](instruments/timing/frequency-counter/srs-sr620/instrument.yaml), [FS725](instruments/timing/frequency-reference/srs-fs725/instrument.yaml), [SR400](instruments/timing/photon-counter/srs-sr400/instrument.yaml)
- **Sumitomo (SHI) Cryogenics:** [F-70](instruments/cryogenics/compressor/sumitomo-f-70/instrument.yaml)
- **Swabian Instruments:** [Time Tagger](instruments/timing/photon-counter/swabian-time-tagger/instrument.yaml), [Pulse Streamer 8/2](instruments/timing/pulse-generator/swabian-pulse-streamer/instrument.yaml)
- **SynkTek:** [MCL1-540](instruments/electronics/lock-in/synktek-mcl1-540/instrument.yaml)
- **TDK-Lambda:** [Genesys](instruments/electronics/power-supply/tdk-lambda-genesys/instrument.yaml)
- **Tecmag:** [Redstone](instruments/spectroscopy/nmr-spectrometer/tecmag-redstone/instrument.yaml)
- **Tektronix:** [AWG5200](instruments/electronics/awg/tektronix-awg5200/instrument.yaml), [5 Series MSO](instruments/electronics/oscilloscope/tektronix-mso5/instrument.yaml)
- **Teledyne Photometrics:** [Kinetix](instruments/optics/camera/teledyne-kinetix/instrument.yaml)
- **Teledyne Princeton Instruments:** [PICam cameras](instruments/optics/camera/princeton-picam/instrument.yaml), [SpectraPro](instruments/optics/monochromator/princeton-spectrapro/instrument.yaml)
- **TESCAN:** [SharkSEM / FIB-SEM Expert PI](instruments/microscopy/electron-microscope/tescan-sharksem/instrument.yaml)
- **Thermo Fisher Scientific:** [AutoScript 4](instruments/microscopy/electron-microscope/thermofisher-autoscript/instrument.yaml)
- **Thorlabs:** [CLD1010LP](instruments/lasers/laser-driver/thorlabs-cld1010/instrument.yaml), [ITC4000](instruments/lasers/laser-driver/thorlabs-itc4000/instrument.yaml), [K10CR1](instruments/motion/motion-stage/thorlabs-k10cr1/instrument.yaml), [KDC101](instruments/motion/motion-stage/thorlabs-kdc101/instrument.yaml), [MDT69xA](instruments/motion/positioner/thorlabs-mdt69xa/instrument.yaml), [BP209](instruments/optics/beam-profiler/thorlabs-bp209/instrument.yaml), [CS165MU](instruments/optics/camera/thorlabs-scientific-camera/instrument.yaml), [MC2000B](instruments/optics/chopper/thorlabs-mc2000b/instrument.yaml), [MPC320](instruments/optics/fiber-optics/thorlabs-mpc320/instrument.yaml), [DC4100](instruments/optics/light-source/thorlabs-dc4100/instrument.yaml), [PDQ80A](instruments/optics/photodetector/thorlabs-pdq80a/instrument.yaml), [PAX1000](instruments/optics/polarimeter/thorlabs-pax1000/instrument.yaml), [PM100](instruments/optics/power-meter/thorlabs-pm100/instrument.yaml), [FW102C](instruments/optics/shutter/thorlabs-fw102c/instrument.yaml), [MFF101](instruments/optics/shutter/thorlabs-mff101/instrument.yaml), [SC10](instruments/optics/shutter/thorlabs-sc10/instrument.yaml), [TC300](instruments/quantum-optics/crystal-oven/thorlabs-tc300/instrument.yaml)
- **TOPTICA Photonics:** [DFC CORE+](instruments/lasers/frequency-comb/toptica-dfc/instrument.yaml), [DLC pro](instruments/lasers/laser-driver/toptica-dlc-pro/instrument.yaml), [DigiLock 110](instruments/lasers/laser-lock/toptica-digilock/instrument.yaml), [FALC pro](instruments/lasers/laser-lock/toptica-falc/instrument.yaml), [TeraFlash pro](instruments/spectroscopy/thz-spectrometer/toptica-teraflash/instrument.yaml)
- **Uniblitz (Vincent Associates):** [VMM-D3](instruments/optics/shutter/uniblitz-vmm-d3/instrument.yaml)
- **Valon Technology:** [5019](instruments/rf-microwave/microwave-source/valon-5019/instrument.yaml)
- **Vaunix Technology Corporation:** [LDA](instruments/rf-microwave/rf-attenuator/vaunix-lda/instrument.yaml)
- **Vescent Photonics:** [D2-125](instruments/lasers/laser-lock/vescent-d2-125/instrument.yaml)
- **Vexlum:** [VALO SF](instruments/lasers/laser/vexlum-vecsel/instrument.yaml)
- **ViALUX:** [V-7000](instruments/optics/spatial-light-modulator/vialux-dmd/instrument.yaml)
- **Watlow:** [F4T](instruments/synthesis/process-controller/watlow-f4t/instrument.yaml)
- **Windfreak Technologies:** [SynthHD](instruments/rf-microwave/microwave-source/windfreak-synthhd/instrument.yaml)
- **Yokogawa:** [7651](instruments/electronics/voltage-source/yokogawa-7651/instrument.yaml), [GS200](instruments/electronics/voltage-source/yokogawa-gs200/instrument.yaml), [AQ6370D](instruments/optics/optical-spectrum-analyzer/yokogawa-aq6370/instrument.yaml)
- **ZEISS:** [SmartSEM (GeminiSEM / Sigma / EVO / Crossbeam)](instruments/microscopy/electron-microscope/zeiss-sem/instrument.yaml)
- **Zurich Instruments:** [HDAWG](instruments/electronics/awg/zhinst-hdawg/instrument.yaml), [MFIA](instruments/electronics/lcr-meter/zhinst-mfia/instrument.yaml), [HF2LI](instruments/electronics/lock-in/zhinst-hf2li/instrument.yaml), [MFLI](instruments/electronics/lock-in/zhinst-mfli/instrument.yaml), [UHFLI](instruments/electronics/lock-in/zhinst-uhfli/instrument.yaml), [SHFQC](instruments/rf-microwave/quantum-controller/zhinst-shfqc/instrument.yaml)
