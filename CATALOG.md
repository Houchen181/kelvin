# Catalog

<!-- Written by `python tools/kic.py index` from the files in this repository; edit those, not this. -->

111 instruments, 49 of them with a Kelvin card; 29 experiments; 10 lab configs.

**Card status.** *community*: written from the maker's manual, not yet checked on hardware. *lab-verified*: checked on hardware by a lab (see the instrument's `verified` list). *draft*: Kelvin keeps its outputs simulated until someone checks it. *no card*: Kelvin writes one from the manual when it finds the instrument.

- [Instruments by category](#instruments-by-category)
- [Experiments](#experiments)
- [Lab configs](#lab-configs)
- [Wanted cards](#wanted-cards)
- [Makers](#makers)

## Instruments by category

- [Electronics and electrical measurement](#electronics-and-electrical-measurement) (30)
- [RF and microwave](#rf-and-microwave) (17)
- [Timing, pulses and photon counting](#timing-pulses-and-photon-counting) (7)
- [Lasers and laser control](#lasers-and-laser-control) (12)
- [Optics, detection and spectroscopy](#optics-detection-and-spectroscopy) (16)
- [Motion and positioning](#motion-and-positioning) (14)
- [Cryogenics, vacuum and sample environment](#cryogenics-vacuum-and-sample-environment) (14)
- [Magnets and field measurement](#magnets-and-field-measurement) (6)
- [Scanning probe microscopy](#scanning-probe-microscopy) (1)

### Electronics and electrical measurement

Sources, meters, lock-ins, preamplifiers, generators and data acquisition, the core of transport measurements.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Keithley 2400-series SourceMeter](instruments/keithley/2400/instrument.yaml) | source-meter | [community](instruments/keithley/2400/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2400S-900-01_K-Sep2011_User.pdf) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) +3 |
| [Keithley 2450 / 2460 / 2461 / 2470 SourceMeter](instruments/keithley/2450/instrument.yaml) | source-meter | [community](instruments/keithley/2450/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://download.tek.com/manual/2450-901-01E_Sept_2019_Ref.pdf) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml) +3 |
| [Keithley 2636B System SourceMeter SMU (2600B series)](instruments/keithley/2636b/instrument.yaml) | source-meter | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/2600BS-901-01F_2600B_Reference_Aug2021.pdf) | [Current-voltage characteristics](experiments/transport/iv-curve.yaml) |
| [Keysight B2900A/B series precision source-measure units](instruments/keysight/b2900/instrument.yaml) | source-meter | [community](instruments/keysight/b2900/card.yaml) | USB-TMC, LAN, GPIB |  | [Field-effect gate sweep](experiments/transport/gate-sweep.yaml), [Current-voltage characteristics](experiments/transport/iv-curve.yaml) |
| [Basel Precision Instruments LNHR DAC II (SP1060) 12/24-channel low-noise DAC](instruments/basel/lnhr-dac/instrument.yaml) | voltage-source | no card | LAN, RS-232 | [manual](https://www.baspi.ch/_files/ugd/68eb62_ed0cc567cc26466382f596cf9190b4ac.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [QDevil QDAC-II 24-channel low-noise DAC](instruments/qdevil/qdac-ii/instrument.yaml) | voltage-source | no card | USB, LAN | [manual](https://docs.quantum-machines.co/latest/docs/Hardware/assets/QDAC-II%20Compact%20Command%20Reference.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml), [Field-effect gate sweep](experiments/transport/gate-sweep.yaml) +1 |
| [Yokogawa GS200 / GS210 DC voltage and current source](instruments/yokogawa/gs200/instrument.yaml) | voltage-source | [community](instruments/yokogawa/gs200/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://web-material3.yokogawa.com/IMGS210-01EN.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Keithley 6221 AC and DC current source](instruments/keithley/6221/instrument.yaml) | current-source | no card | GPIB, RS-232, LAN | [manual](https://download.tek.com/manual/622x-901-01%20(C%20-%20Oct%202008)(Ref).pdf) | [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml) |
| [Keithley 2000 6½-digit multimeter](instruments/keithley/2000/instrument.yaml) | multimeter | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/2000-900_J-Aug2010_User.pdf) | [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Keithley DMM6500 6½-digit bench multimeter](instruments/keithley/dmm6500/instrument.yaml) | multimeter | no card | USB-TMC, LAN, GPIB, RS-232 | [manual](https://download.tek.com/manual/DMM6500-901-01C_April_2026_Ref.pdf) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Keysight Truevolt 34460A / 34461A / 34465A / 34470A multimeters](instruments/keysight/34465a/instrument.yaml) | multimeter | [community](instruments/keysight/34465a/card.yaml) | USB-TMC, LAN, GPIB |  | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) +1 |
| [Keithley 2182A nanovoltmeter](instruments/keithley/2182a/instrument.yaml) | nanovoltmeter | [community](instruments/keithley/2182a/card.yaml) | GPIB, RS-232 | [manual](https://download.tek.com/manual/2182A-900-01C_July_2022_User.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Critical current and Fraunhofer pattern](experiments/transport/critical-current.yaml), [Current-voltage characteristics](experiments/transport/iv-curve.yaml) |
| [Keithley 6517B electrometer / high-resistance meter](instruments/keithley/6517b/instrument.yaml) | electrometer | no card | GPIB, RS-232 | [manual](https://download.tek.com/manual/6517B-901-01F_Jan2024_Ref.pdf) |  |
| [Signal Recovery 7270 DSP lock-in amplifier](instruments/signal-recovery/7270/instrument.yaml) | lock-in | no card | LAN, USB, RS-232 | [sign-in](https://www.ameteksi.com/-/media/ameteksi/download_links/documentations/supportcenter/signalrecovery/instruction_manuals/197852-a-mnl-f.pdf) | [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [Stanford Research SR830 DSP lock-in amplifier](instruments/srs/sr830/instrument.yaml) | lock-in | [community](instruments/srs/sr830/card.yaml) | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR830m.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml) +11 |
| [Stanford Research Systems SR844 RF lock-in amplifier](instruments/srs/sr844/instrument.yaml) | lock-in | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf) |  |
| [Stanford Research SR860 / SR865A lock-in amplifiers](instruments/srs/sr860/instrument.yaml) | lock-in | [community](instruments/srs/sr860/card.yaml) | GPIB, RS-232, USB-TMC, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR860m.pdf) | [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) +8 |
| [Zurich Instruments HF2LI 50 MHz lock-in amplifier](instruments/zhinst/hf2li/instrument.yaml) | lock-in | no card | USB | [manual](https://docs.zhinst.com/hf2_user_manual/programming.html) |  |
| [Zurich Instruments MFLI 500 kHz / 5 MHz lock-in amplifier](instruments/zhinst/mfli/instrument.yaml) | lock-in | [community](instruments/zhinst/mfli/card.yaml) | USB, LAN | [manual](https://docs.zhinst.com/pdf/ziMFLI_UserManual.pdf) | [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) +7 |
| [Zurich Instruments UHFLI 600 MHz lock-in amplifier](instruments/zhinst/uhfli/instrument.yaml) | lock-in | no card | USB, LAN | [manual](https://docs.zhinst.com/uhf_user_manual/nodedoc.html) |  |
| [Stanford Research SR560 low-noise voltage preamplifier](instruments/srs/sr560/instrument.yaml) | preamp | [community](instruments/srs/sr560/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR560m.pdf) | [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [Stanford Research SR570 low-noise current preamplifier](instruments/srs/sr570/instrument.yaml) | preamp | [community](instruments/srs/sr570/card.yaml) | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR570m.pdf) | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Tunneling spectroscopy (dI/dV)](experiments/transport/differential-conductance.yaml) |
| [Lake Shore Model 372 AC resistance bridge and temperature controller](instruments/lakeshore/372/instrument.yaml) | resistance-bridge | no card | GPIB, USB, LAN | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/372_manual.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) |
| [Keysight 33500B / 33600A waveform generators](instruments/keysight/33500b/instrument.yaml) | function-generator | [community](instruments/keysight/33500b/card.yaml) | USB-TMC, LAN, GPIB |  | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml) |
| [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](instruments/qick/rfsoc/instrument.yaml) | awg | [community](instruments/qick/rfsoc/card.yaml) | LAN |  | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Rigol DG1000Z function and arbitrary waveform generators](instruments/rigol/dg1000z/instrument.yaml) | awg | [community](instruments/rigol/dg1000z/card.yaml) | USB-TMC, LAN | [manual](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0493/1/-/-/-/-/DG1000Z%20Programming%20Guide.pdf) |  |
| [Tektronix AWG5200 series arbitrary waveform generator](instruments/tektronix/awg5200/instrument.yaml) | awg | no card | LAN, USB-TMC, GPIB | [manual](https://download.tek.com/manual/AWG5200-Programmer-Manual-077133700-RevA.pdf) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [Zurich Instruments HDAWG arbitrary waveform generator](instruments/zhinst/hdawg/instrument.yaml) | awg | no card | USB, LAN | [manual](https://docs.zhinst.com/hdawg_user_manual/index.html) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [NI DAQ devices through NI-DAQmx (USB-600x, USB-62xx, PCIe/PXIe-63xx, cDAQ)](instruments/ni/daqmx/instrument.yaml) | daq | [community](instruments/ni/daqmx/card.yaml) | USB, PCIe, PXIe |  |  |
| [Keysight B1500A semiconductor device parameter analyzer](instruments/keysight/b1500a/instrument.yaml) | parameter-analyzer | no card | GPIB | [manual](https://www.keysight.com/us/en/assets/9018-01851/programming-guides/9018-01851.pdf) |  |

### RF and microwave

Signal generators, network and spectrum analyzers, acousto-optic drivers and qubit controllers.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Keysight E8257D PSG analog signal generator](instruments/keysight/e8257d/instrument.yaml) | microwave-source | no card | GPIB, LAN, RS-232 | [manual](https://www.keysight.com/us/en/assets/9018-04961/installation-guides/9018-04961.pdf) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [Keysight MXG N5183B microwave signal generator](instruments/keysight/n5183b/instrument.yaml) | microwave-source | [community](instruments/keysight/n5183b/card.yaml) | USB-TMC, LAN, GPIB | [manual](https://www.keysight.com/content/dam/keysight/en/doc/gate/programming-guides/9018-03690.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Rohde & Schwarz SGS100A SGMA RF source](instruments/rs/sgs100a/instrument.yaml) | microwave-source | no card | LAN, USB-TMC, PCIe | [manual](https://www.rohde-schwarz.com/webhelp/SGS100A_HTML_UserManual_en/SGS100A_HTML_UserManual_en.htm) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Rohde & Schwarz SMB100A RF and microwave signal generator](instruments/rs/smb100a/instrument.yaml) | microwave-source | [community](instruments/rs/smb100a/card.yaml) | GPIB, USB-TMC, LAN | [manual](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_manuals/dl_user_manual/SMB100A_OperatingManual_en_23.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml), [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml) +1 |
| [Stanford Research SG380-series RF signal generators](instruments/srs/sg384/instrument.yaml) | microwave-source | [community](instruments/srs/sg384/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SG380m.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) +2 |
| [Windfreak SynthHD dual-channel microwave generator](instruments/windfreak/synthhd/instrument.yaml) | microwave-source | [draft](instruments/windfreak/synthhd/card.yaml) | USB | [manual](https://windfreaktech.com/wp-content/uploads/2016/12/WFT_SerialProgramming_API_10b.pdf) | [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Copper Mountain 2-port USB VNAs (S5048, S5065, M5180 and similar) via the S2VNA software](instruments/copper-mountain/s2vna/instrument.yaml) | vna | no card | USB, LAN | [manual](https://coppermountaintech.com/wp-content/uploads/2025/04/S2VNA-Operating-and-Programming-Manual.pdf) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Keysight E5071C ENA vector network analyzer](instruments/keysight/e5071c/instrument.yaml) | vna | no card | GPIB, USB-TMC, LAN | [manual](https://helpfiles.keysight.com/csg/e5071c/programming/remote_control/remote_control.htm) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Keysight E5080B ENA vector network analyzer](instruments/keysight/e5080b/instrument.yaml) | vna | no card | GPIB, USB-TMC, LAN | [manual](https://helpfiles.keysight.com/csg/e5080b/Programming/Programming_Guide.htm) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml) |
| [Rohde & Schwarz ZNB vector network analyzer](instruments/rs/znb/instrument.yaml) | vna | no card | GPIB, USB-TMC, LAN | [manual](https://www.rohde-schwarz.com/webhelp/ZNB_HTML_UserManual_en/ZNB_HTML_UserManual_en.htm) | [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Keysight N9020B MXA signal analyzer (X-Series)](instruments/keysight/n9020b/instrument.yaml) | spectrum-analyzer | no card | GPIB, USB-TMC, LAN | [sign-in](https://www.keysight.com/us/en/assets/9018-02192/programming-guides/9018-02192.pdf) |  |
| [MOGLabs XRF / ARF / QRF agile RF synthesizers](instruments/moglabs/xrf/instrument.yaml) | aom-driver | [community](instruments/moglabs/xrf/card.yaml) | USB, LAN | [manual](https://santec-inst.files.svdcdn.com/production/Files/Tutorials/RF-generators-synthesizers/MOGLabs_XRF_manual.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Novatech 409B four-channel DDS signal generator](instruments/novatech/409b/instrument.yaml) | aom-driver | [community](instruments/novatech/409b/card.yaml) | RS-232 | [manual](https://www.novatechsales.com/docs/409b_man.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Quantum Machines OPX+ / OPX1000 quantum controller (QUA)](instruments/quantum-machines/opx/instrument.yaml) | quantum-controller | no card | LAN | [manual](https://docs.quantum-machines.co/latest/) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml) |
| [Zurich Instruments SHFQC qubit controller](instruments/zhinst/shfqc/instrument.yaml) | quantum-controller | no card | USB, LAN | [manual](https://docs.zhinst.com/shfqc_user_manual/index.html) | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [RFSoC boards running QICK (ZCU111, ZCU216, RFSoC 4x2)](instruments/qick/rfsoc/instrument.yaml) | awg | [community](instruments/qick/rfsoc/card.yaml) | LAN |  | [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Stanford Research Systems SR844 RF lock-in amplifier](instruments/srs/sr844/instrument.yaml) | lock-in | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR844m.pdf) |  |

### Timing, pulses and photon counting

Pulse pattern and delay generators, photon counters and time taggers.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [SpinCore PulseBlaster pulse generators](instruments/spincore/pulseblaster/instrument.yaml) | pulse-generator | [community](instruments/spincore/pulseblaster/card.yaml) | USB, PCIe |  | [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Swabian Instruments Pulse Streamer 8/2](instruments/swabian/pulse-streamer/instrument.yaml) | pulse-generator | [community](instruments/swabian/pulse-streamer/card.yaml) | LAN | [manual](https://www.swabianinstruments.com/static/documentation/pulse-streamer/v2.1/sections/api-doc.html) | [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |
| [Stanford Research DG645 digital delay generator](instruments/srs/dg645/instrument.yaml) | delay-generator | [community](instruments/srs/dg645/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DG645m.pdf) |  |
| [PicoQuant HydraHarp 400 TCSPC / time tagger](instruments/picoquant/hydraharp-400/instrument.yaml) | photon-counter | no card | USB | [manual](https://downloads.picoquant.com/manuals/discontinued/HydraHarp400_DLL_Manual.pdf) |  |
| [PicoQuant MultiHarp 150 time tagger](instruments/picoquant/multiharp-150/instrument.yaml) | photon-counter | no card | USB | [manual](https://downloads.picoquant.com/manuals/MultiHarp150_160_DLL_Manual.pdf) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Stanford Research Systems SR400 gated photon counter](instruments/srs/sr400/instrument.yaml) | photon-counter | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR400m.pdf) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Swabian Instruments Time Tagger (20, Ultra, X)](instruments/swabian/time-tagger/instrument.yaml) | photon-counter | [community](instruments/swabian/time-tagger/card.yaml) | USB | [manual](https://www.swabianinstruments.com/static/documentation/TimeTagger/api/measurements/event_counting.html) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [NV-center Rabi, Ramsey, Hahn echo and T1](experiments/spin-resonance/nv-coherence.yaml), [NV-center ODMR (CW and pulsed)](experiments/spin-resonance/nv-odmr.yaml) |

### Lasers and laser control

CW, tunable and ultrafast lasers, diode and TEC controllers, wavelength meters.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Coherent Chameleon Ultra / Discovery ultrafast Ti:sapphire lasers](instruments/coherent/chameleon/instrument.yaml) | laser | no card | RS-232, USB | [support](https://www.coherent.com/lasers/oscillators/chameleon-ultra) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Coherent OBIS LX/LS lasers](instruments/coherent/obis/instrument.yaml) | laser | [community](instruments/coherent/obis/card.yaml) | USB, RS-232 | [manual](https://www.coherent.com/content/dam/coherent/site/en/resources/manuals/lasers/obis-lx-ls-operators-manual.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) +5 |
| [HÜBNER Photonics Cobolt 04-01 / 06-01 / 08-01 series lasers](instruments/hubner/cobolt/instrument.yaml) | laser | no card | USB, RS-232 | [manual](https://hubner-photonics.com/wp-content/uploads/2023/11/D0136-P_Manual-Cobolt-06-01-Series_October_2023-1.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) +3 |
| [Light Conversion PHAROS femtosecond laser](instruments/lightcon/pharos/instrument.yaml) | laser | [community](instruments/lightcon/pharos/card.yaml) | LAN, web API |  | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [M Squared SolsTiS Ti:sapphire laser (ICE-BLOC)](instruments/m2/solstis/instrument.yaml) | laser | [community](instruments/m2/solstis/card.yaml) | LAN |  | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) |
| [NKT Photonics SuperK EXTREME / FIANIUM supercontinuum lasers](instruments/nkt/superk/instrument.yaml) | laser | no card | USB, LAN, RS-232 | [manual](https://lf.hamamatsu.com/wp-json/nktphotonics/v1/download/SuperK-EXTREME/SuperK%20EXTREME%20Product%20Guide.pdf) |  |
| [Spectra-Physics Mai Tai Ti:sapphire ultrafast laser](instruments/spectra-physics/mai-tai/instrument.yaml) | laser | no card | RS-232 | [manual](https://api.p1.mks.com/mam/celum/celum_assets/sp/resources/284A_Rev_G_Mai_Tai_Users_Manual.pdf) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Thorlabs CLD1010 compact laser diode and TEC controller](instruments/thorlabs/cld1010/instrument.yaml) | laser-driver | no card | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/c/cl/cld/cld1015/doc-104674.pdf) |  |
| [Thorlabs ITC4000-series laser diode and TEC controllers](instruments/thorlabs/itc4000/instrument.yaml) | laser-driver | [community](instruments/thorlabs/itc4000/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/t/te/ted/ted4015/16407-d03.pdf) |  |
| [TOPTICA DLC pro diode laser controller](instruments/toptica/dlc-pro/instrument.yaml) | laser-driver | [draft](instruments/toptica/dlc-pro/card.yaml) | LAN, USB |  | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |
| [Bristol Instruments 671 / 771 / 871 wavelength meters](instruments/bristol/wavemeter/instrument.yaml) | wavemeter | no card | USB, LAN | [support](https://www.bristol-inst.com/wp-content/uploads/2023/09/Bristol-671-Series-Laser-Wavelength-Meter-Specifications.pdf) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |
| [HighFinesse WS6 / WS7 / WS8 wavelength meters](instruments/highfinesse/wavemeter/instrument.yaml) | wavemeter | no card | USB | [support](https://www.highfinesse.com/en/support/downloads.html) | [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml) |

### Optics, detection and spectroscopy

Power meters, spectrometers, spectrographs, scientific cameras, detectors and modulators.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Newport 2936-R / 1936-R optical power meters](instruments/newport/2936-r/instrument.yaml) | power-meter | no card | USB, RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/npresources/hc4/h06/10082698067998/19xx-29xx-R-Power-Meter-Commands_Ver01/19xx-29xx-R-Power-Meter-Commands-Ver01.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) |
| [Thorlabs PM100D / PM100USB / PM400 optical power meters](instruments/thorlabs/pm100/instrument.yaml) | power-meter | [community](instruments/thorlabs/pm100/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/p/pm/pm1/pm100d/17654-d02.pdf) | [AOM diffraction efficiency](experiments/amo/aom-calibration.yaml), [Photoluminescence excitation (PLE) wavelength scan](experiments/amo/ple-scan.yaml), [Magneto-optical Kerr effect](experiments/optics/moke.yaml) +2 |
| [HORIBA iHR320 / iHR550 imaging spectrometers](instruments/horiba/ihr/instrument.yaml) | spectrometer | no card | USB | [manual](https://horiba-python-sdk.readthedocs.io/en/latest/icl_api/) | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) |
| [Ocean Insight USB spectrometers (Flame, HR, QE Pro, USB2000+)](instruments/ocean/spectrometer/instrument.yaml) | spectrometer | [community](instruments/ocean/spectrometer/card.yaml) | USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [Andor Shamrock and Kymera spectrographs](instruments/andor/shamrock/instrument.yaml) | monochromator | [community](instruments/andor/shamrock/card.yaml) | USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +1 |
| [Princeton Instruments (Acton) SpectraPro monochromators](instruments/princeton/spectrapro/instrument.yaml) | monochromator | [community](instruments/princeton/spectrapro/card.yaml) | RS-232, USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +1 |
| [Andor CCD and EMCCD cameras (iXon, Newton, iDus)](instruments/andor/ccd/instrument.yaml) | camera | [draft](instruments/andor/ccd/card.yaml) | USB, PCIe |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +2 |
| [Andor sCMOS cameras (Zyla, Neo, Sona, Marana)](instruments/andor/scmos/instrument.yaml) | camera | [draft](instruments/andor/scmos/card.yaml) | USB, PCIe |  |  |
| [Basler industrial cameras (pylon)](instruments/basler/camera/instrument.yaml) | camera | [community](instruments/basler/camera/card.yaml) | USB, LAN |  |  |
| [Hamamatsu ORCA-Flash4.0 / ORCA-Quest scientific CMOS cameras (DCAM-API)](instruments/hamamatsu/orca/instrument.yaml) | camera | no card | USB, PCIe | [support](https://www.hamamatsu.com/us/en/product/cameras/software/driver-software/dcam-sdk4.html) |  |
| [Teledyne Princeton Instruments cameras through PICam](instruments/princeton/picam/instrument.yaml) | camera | [community](instruments/princeton/picam/card.yaml) | USB, LAN |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Raman spectroscopy](experiments/optics/raman.yaml) +1 |
| [Thorlabs Kiralux / Quantalux / Zelux scientific cameras (Scientific Camera SDK)](instruments/thorlabs/scientific-camera/instrument.yaml) | camera | no card | USB | [support](https://www.thorlabs.com/item/CS165MU) |  |
| [Thorlabs MC2000B optical chopper](instruments/thorlabs/mc2000b/instrument.yaml) | chopper | no card | USB | [manual](https://media.thorlabs.com/globalassets/items/m/mc/mc2/mc2000b/ttn102010-d02.pdf) | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Hinds Instruments PEM-200 photoelastic modulator controller (and PEM-100)](instruments/hinds/pem/instrument.yaml) | modulator | no card | USB, LAN, RS-232 | [manual](https://www.hindsinstruments.com/wp-content/uploads/PEM-200-User-Manual.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |
| [Montana Instruments Cryostation s-series closed-cycle optical cryostat](instruments/montana/cryostation/instrument.yaml) | cryostat | no card | LAN | [manual](https://cdn.prod.website-files.com/6118466f5c775b56d53d49e9/695d7ffcee2d9010efc7f5a4_4100-1-DOC002_1.2%20(User%20Manual%20-%20Cryostation%20s-series%20-%20SHI%20Configuration%20MI75%20VCM).pdf) | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Raman spectroscopy](experiments/optics/raman.yaml), [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) +1 |
| [Quantum Design OptiCool magneto-optical cryostat](instruments/qd/opticool/instrument.yaml) | cryostat | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |

### Motion and positioning

Piezo positioners and scanners, motorized stages, delay lines and rotation mounts.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [attocube AMC300 / AMC100 piezo positioner controller](instruments/attocube/amc/instrument.yaml) | positioner | no card | LAN, USB | [manual](https://raw.githubusercontent.com/attocube-systems/AMC-APIs/master/AMC_Interface_Manual_v1.5.1.pdf) |  |
| [attocube ANC300 piezo positioner controller](instruments/attocube/anc300/instrument.yaml) | positioner | [community](instruments/attocube/anc300/card.yaml) | USB, LAN |  |  |
| [attocube ANC350 closed-loop positioner controller](instruments/attocube/anc350/instrument.yaml) | positioner | [community](instruments/attocube/anc350/card.yaml) | USB |  | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [Mad City Labs Nano-Drive piezo nanopositioning controller](instruments/mcl/nano-drive/instrument.yaml) | positioner | no card | USB, analog | [support](https://www.madcitylabs.com/nanodrive.html) | [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml) |
| [PI piezo controllers with the GCS command set](instruments/pi/gcs-piezo/instrument.yaml) | positioner | [community](instruments/pi/gcs-piezo/card.yaml) | USB, LAN, RS-232 |  | [Scanning photocurrent microscopy](experiments/optics/photocurrent-mapping.yaml), [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml), [Reflectance contrast spectroscopy](experiments/optics/reflectance-contrast.yaml) |
| [SmarAct MCS2 modular positioning controller](instruments/smaract/mcs2/instrument.yaml) | positioner | no card | USB, LAN | [owners](https://www.smaract.com/en/motion/products/control-systems-and-software-working/control-systems/mcs2) | [Hyperspectral PL and Raman mapping](experiments/optics/pl-mapping.yaml) |
| [Thorlabs MDT693A / MDT694A piezo controllers](instruments/thorlabs/mdt69xa/instrument.yaml) | positioner | [community](instruments/thorlabs/mdt69xa/card.yaml) | USB |  |  |
| [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](instruments/newport/conex-cc/instrument.yaml) | motion-stage | no card | USB | [manual](https://api.p1.mks.com/medias/sys_master/npresources/h91/hf3/10219689345054/CONEX-CC%20-%20Controller%20Documentation/CONEX-CC-Controller-Documentation.pdf) | [Raman spectroscopy](experiments/optics/raman.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Newport ESP301 three-axis motion controller](instruments/newport/esp301/instrument.yaml) | motion-stage | no card | GPIB, USB, RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/images/images/hda/h3e/9117547069470/ESP301-User-s-Manual.pdf) |  |
| [Newport SMC100CC / SMC100PP single-axis motion controller](instruments/newport/smc100/instrument.yaml) | motion-stage | no card | RS-232, RS-485, USB | [manual](https://api.p1.mks.com/medias/sys_master/resources/hec/h2b/10211813294110/SMC100CC_and_SMC100PP_-_User_Manual/SMC100CC-and-SMC100PP-User-Manual.pdf) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Newport XPS-D / XPS-RL universal high-performance motion controller](instruments/newport/xps/instrument.yaml) | motion-stage | no card | LAN | [manual](https://api.p1.mks.com/medias/sys_master/npresources/h3e/h82/10211812802590/XPS_Unified_-_Programmer_s_Manual/XPS-Unified-Programmer-s-Manual.pdf) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) |
| [Physik Instrumente C-863 Mercury DC motor controller](instruments/pi/c-863/instrument.yaml) | motion-stage | no card | USB, RS-232 | [sign-in](https://www.physikinstrumente.com/en/products/controllers-and-drivers/motion-controllers-drivers-for-linear-torque-stepper-dc-servo-motors/c-863-mercury-servo-controller-900606/) | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) |
| [Thorlabs K10CR1 motorized rotation mount](instruments/thorlabs/k10cr1/instrument.yaml) | motion-stage | no card | USB |  | [Raman spectroscopy](experiments/optics/raman.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Thorlabs KDC101 K-Cube brushed DC servo motor controller](instruments/thorlabs/kdc101/instrument.yaml) | motion-stage | no card | USB |  | [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) |

### Cryogenics, vacuum and sample environment

Temperature controllers, cryostat systems, dilution refrigerators and vacuum gauges.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [Cryo-con Model 24C cryogenic temperature controller](instruments/cryocon/24c/instrument.yaml) | temperature-controller | no card | LAN, RS-232, GPIB, USB | [support](https://qd-europe.com/de/en/news/product-application-news-spectrum/find-the-right-temperature-monitor-and-controller-for-your-cryogenic-experiments) |  |
| [Lake Shore Model 218 temperature monitor](instruments/lakeshore/218/instrument.yaml) | temperature-controller | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/218_manual.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml) |
| [Lake Shore Model 335 / 336 temperature controller](instruments/lakeshore/336/instrument.yaml) | temperature-controller | [community](instruments/lakeshore/336/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/336manual.pdf?sfvrsn=fa4e3a80_12) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml) +8 |
| [Lake Shore Model 340 cryogenic temperature controller](instruments/lakeshore/340/instrument.yaml) | temperature-controller | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/340_manual.pdf) |  |
| [Lake Shore Model 350 temperature controller](instruments/lakeshore/350/instrument.yaml) | temperature-controller | [community](instruments/lakeshore/350/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/software/manuals/350_manual.pdf?sfvrsn=501e9331_5) | [Cooldown log](experiments/environment/cooldown-log.yaml), [AC susceptibility with a lock-in](experiments/magnetometry/ac-susceptibility.yaml), [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [Oxford Instruments Mercury iTC temperature controller](instruments/oxford/mercury-itc/instrument.yaml) | temperature-controller | [community](instruments/oxford/mercury-itc/card.yaml) | USB, LAN, RS-232, GPIB | [manual](https://www.mymercurysupport.com/sites/default/files/59_UMC0071_EN_02.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [Resistance against temperature](experiments/transport/resistance-vs-temperature.yaml) |
| [attocube attoDRY closed-cycle cryostats](instruments/attocube/attodry/instrument.yaml) | cryostat | [draft](instruments/attocube/attodry/card.yaml) | USB |  | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Hall effect and magnetoresistance](experiments/transport/hall-magnetoresistance.yaml), [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml) |
| [Montana Instruments Cryostation s-series closed-cycle optical cryostat](instruments/montana/cryostation/instrument.yaml) | cryostat | no card | LAN | [manual](https://cdn.prod.website-files.com/6118466f5c775b56d53d49e9/695d7ffcee2d9010efc7f5a4_4100-1-DOC002_1.2%20(User%20Manual%20-%20Cryostation%20s-series%20-%20SHI%20Configuration%20MI75%20VCM).pdf) | [Photoluminescence spectroscopy](experiments/optics/photoluminescence.yaml), [Raman spectroscopy](experiments/optics/raman.yaml), [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml) +1 |
| [Quantum Design PPMS, DynaCool, VersaLab and MPMS3 through MultiVu](instruments/qd/multivu/instrument.yaml) | cryostat | [community](instruments/qd/multivu/card.yaml) | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [SQUID magnetometry (M-T and M-H)](experiments/magnetometry/squid-magnetometry.yaml) +10 |
| [Quantum Design OptiCool magneto-optical cryostat](instruments/qd/opticool/instrument.yaml) | cryostat | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |
| [Bluefors dilution refrigerators (Control Software, temperature controller, gas handling system)](instruments/bluefors/dilution-refrigerator/instrument.yaml) | dilution-refrigerator | no card | LAN, web API | [manual](https://github.com/BlueforsOy/Control_Software_gen2_API_examples/blob/main/README.md) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) +1 |
| [Oxford Instruments Triton dilution refrigerator](instruments/oxford/triton/instrument.yaml) | dilution-refrigerator | no card | LAN | [support](https://qd-oxford.com/services/legacy_product_support.html) | [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml), [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml), [Superconducting resonator spectroscopy](experiments/quantum-devices/resonator-spectroscopy.yaml) |
| [Pfeiffer Vacuum TPG 361 / TPG 362 SingleGauge / DualGauge vacuum gauge controllers](instruments/pfeiffer/tpg36x/instrument.yaml) | vacuum-gauge | no card | RS-485, USB, LAN | [manual](https://www.shop.buschgroup.com/api/empolis/resource/environment/project1_p/documents/pfeifferSharepointProd/2181-bg5510ben_d.pdf) |  |
| [Lake Shore Model 372 AC resistance bridge and temperature controller](instruments/lakeshore/372/instrument.yaml) | resistance-bridge | no card | GPIB, USB, LAN | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/372_manual.pdf) | [Cooldown log](experiments/environment/cooldown-log.yaml), [Coulomb diamonds in quantum dots](experiments/quantum-devices/coulomb-diamonds.yaml) |

### Magnets and field measurement

Superconducting magnet supplies, gaussmeters and teslameters.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [American Magnetics Model 430 magnet power supply programmer](instruments/ami/430/instrument.yaml) | magnet-supply | [community](instruments/ami/430/card.yaml) | RS-232, LAN | [manual](https://www.americanmagnetics.com/support/manuals/mn-430-rev14.pdf) | [Acoustoelectric effect](experiments/acoustics/acoustoelectric.yaml), [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) +3 |
| [Cryomagnetics Model 4G superconducting magnet power supply](instruments/cryomagnetics/4g/instrument.yaml) | magnet-supply | no card | USB, LAN, GPIB | [manual](https://cryomagnetics.com/wp-content/uploads/2022/05/4G-Rev-9_3.pdf) | [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml) |
| [Lake Shore Model 625 superconducting magnet power supply](instruments/lakeshore/625/instrument.yaml) | magnet-supply | [community](instruments/lakeshore/625/card.yaml) | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/625_manual.pdf?sfvrsn=2d9f6b7_1) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml), [Ferromagnetic resonance (field-modulated)](experiments/spin-resonance/fmr.yaml), [Hall effect and magnetoresistance](experiments/transport/hall-magnetoresistance.yaml) |
| [Oxford Instruments Mercury iPS superconducting magnet power supply](instruments/oxford/mercury-ips/instrument.yaml) | magnet-supply | no card | LAN, RS-232, USB, GPIB | [manual](https://mymercurysupport.com/sites/default/files/59_UMC0072_01.pdf) | [Landau fan and quantum oscillations](experiments/transport/landau-fan.yaml) |
| [Lake Shore Model 475 DSP gaussmeter](instruments/lakeshore/475/instrument.yaml) | gaussmeter | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/475_manual.pdf) |  |
| [Quantum Design OptiCool magneto-optical cryostat](instruments/qd/opticool/instrument.yaml) | cryostat | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) | [Magneto-optical Kerr effect](experiments/optics/moke.yaml) |

### Scanning probe microscopy

Controllers for STM, AFM and scanning sensors.

| Instrument | Kind | Card | Talks over | Manual | Used in |
|---|---|---|---|---|---|
| [SPECS Nanonis SPM controller (TCP programming interface)](instruments/specs/nanonis/instrument.yaml) | spm-controller | no card | LAN | [manual](https://raw.githubusercontent.com/SPECS-Zurich-GmbH/nanonis_spm/main/TCPProtocol_SPM.pdf) |  |

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

- **vna** for [Surface acoustic wave transmission and magnetoacoustics](experiments/acoustics/saw-transmission.yaml): [Copper Mountain 2-port USB VNAs (S5048, S5065, M5180 and similar) via the S2VNA software](instruments/copper-mountain/s2vna/instrument.yaml), [Keysight E5071C ENA vector network analyzer](instruments/keysight/e5071c/instrument.yaml), [Keysight E5080B ENA vector network analyzer](instruments/keysight/e5080b/instrument.yaml), [Rohde & Schwarz ZNB vector network analyzer](instruments/rs/znb/instrument.yaml)
- **quantum-controller** for [Superconducting qubit characterization](experiments/quantum-devices/qubit-time-domain.yaml): [Quantum Machines OPX+ / OPX1000 quantum controller (QUA)](instruments/quantum-machines/opx/instrument.yaml), [Zurich Instruments SHFQC qubit controller](instruments/zhinst/shfqc/instrument.yaml)
- **motion-stage** for [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml): [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](instruments/newport/conex-cc/instrument.yaml), [Newport ESP301 three-axis motion controller](instruments/newport/esp301/instrument.yaml), [Newport SMC100CC / SMC100PP single-axis motion controller](instruments/newport/smc100/instrument.yaml), [Newport XPS-D / XPS-RL universal high-performance motion controller](instruments/newport/xps/instrument.yaml), [Physik Instrumente C-863 Mercury DC motor controller](instruments/pi/c-863/instrument.yaml), [Thorlabs K10CR1 motorized rotation mount](instruments/thorlabs/k10cr1/instrument.yaml), [Thorlabs KDC101 K-Cube brushed DC servo motor controller](instruments/thorlabs/kdc101/instrument.yaml)
- **chopper** for [Pump-probe transient reflectivity](experiments/ultrafast-nonlinear/pump-probe.yaml): [Thorlabs MC2000B optical chopper](instruments/thorlabs/mc2000b/instrument.yaml)
- **motion-stage** for [Rotational-anisotropy second-harmonic generation](experiments/ultrafast-nonlinear/shg-rotational-anisotropy.yaml): [Newport CONEX-CC / CONEX-AGP integrated single-axis controller](instruments/newport/conex-cc/instrument.yaml), [Newport ESP301 three-axis motion controller](instruments/newport/esp301/instrument.yaml), [Newport SMC100CC / SMC100PP single-axis motion controller](instruments/newport/smc100/instrument.yaml), [Newport XPS-D / XPS-RL universal high-performance motion controller](instruments/newport/xps/instrument.yaml), [Physik Instrumente C-863 Mercury DC motor controller](instruments/pi/c-863/instrument.yaml), [Thorlabs K10CR1 motorized rotation mount](instruments/thorlabs/k10cr1/instrument.yaml), [Thorlabs KDC101 K-Cube brushed DC servo motor controller](instruments/thorlabs/kdc101/instrument.yaml)

## Makers

- **American Magnetics:** [430](instruments/ami/430/instrument.yaml)
- **Andor (Oxford Instruments):** [CCD and EMCCD](instruments/andor/ccd/instrument.yaml), [sCMOS](instruments/andor/scmos/instrument.yaml), [Shamrock / Kymera](instruments/andor/shamrock/instrument.yaml)
- **attocube:** [AMC300](instruments/attocube/amc/instrument.yaml), [ANC300](instruments/attocube/anc300/instrument.yaml), [ANC350](instruments/attocube/anc350/instrument.yaml), [attoDRY](instruments/attocube/attodry/instrument.yaml)
- **Basel Precision Instruments:** [SP1060](instruments/basel/lnhr-dac/instrument.yaml)
- **Basler:** [ace / dart](instruments/basler/camera/instrument.yaml)
- **Bluefors:** [LD / XLD / SD / LH series](instruments/bluefors/dilution-refrigerator/instrument.yaml)
- **Bristol Instruments:** [671](instruments/bristol/wavemeter/instrument.yaml)
- **Coherent:** [Chameleon Ultra](instruments/coherent/chameleon/instrument.yaml), [OBIS](instruments/coherent/obis/instrument.yaml)
- **Copper Mountain:** [S2VNA](instruments/copper-mountain/s2vna/instrument.yaml)
- **Cryo-con:** [24C](instruments/cryocon/24c/instrument.yaml)
- **Cryomagnetics:** [4G](instruments/cryomagnetics/4g/instrument.yaml)
- **Hamamatsu:** [ORCA-Flash4.0 V3](instruments/hamamatsu/orca/instrument.yaml)
- **HighFinesse:** [WS7](instruments/highfinesse/wavemeter/instrument.yaml)
- **Hinds Instruments:** [PEM-200](instruments/hinds/pem/instrument.yaml)
- **HORIBA:** [iHR320](instruments/horiba/ihr/instrument.yaml)
- **HÜBNER Photonics (Cobolt):** [06-01](instruments/hubner/cobolt/instrument.yaml)
- **Keithley (Tektronix):** [2000](instruments/keithley/2000/instrument.yaml), [2182A](instruments/keithley/2182a/instrument.yaml), [2400](instruments/keithley/2400/instrument.yaml), [2450](instruments/keithley/2450/instrument.yaml), [2636B](instruments/keithley/2636b/instrument.yaml), [6221](instruments/keithley/6221/instrument.yaml), [6517B](instruments/keithley/6517b/instrument.yaml), [DMM6500](instruments/keithley/dmm6500/instrument.yaml)
- **Keysight:** [33500B](instruments/keysight/33500b/instrument.yaml), [34465A](instruments/keysight/34465a/instrument.yaml), [B1500A](instruments/keysight/b1500a/instrument.yaml), [B2900](instruments/keysight/b2900/instrument.yaml), [E5071C](instruments/keysight/e5071c/instrument.yaml), [E5080B](instruments/keysight/e5080b/instrument.yaml), [E8257D](instruments/keysight/e8257d/instrument.yaml), [N5183B](instruments/keysight/n5183b/instrument.yaml), [N9020B](instruments/keysight/n9020b/instrument.yaml)
- **Lake Shore Cryotronics:** [218](instruments/lakeshore/218/instrument.yaml), [336](instruments/lakeshore/336/instrument.yaml), [340](instruments/lakeshore/340/instrument.yaml), [350](instruments/lakeshore/350/instrument.yaml), [372](instruments/lakeshore/372/instrument.yaml), [475](instruments/lakeshore/475/instrument.yaml), [625](instruments/lakeshore/625/instrument.yaml)
- **Light Conversion:** [PHAROS](instruments/lightcon/pharos/instrument.yaml)
- **M Squared:** [SolsTiS](instruments/m2/solstis/instrument.yaml)
- **Mad City Labs:** [Nano-Drive](instruments/mcl/nano-drive/instrument.yaml)
- **MOGLabs:** [XRF](instruments/moglabs/xrf/instrument.yaml)
- **Montana Instruments:** [Cryostation s-series](instruments/montana/cryostation/instrument.yaml)
- **Newport (MKS):** [2936-R](instruments/newport/2936-r/instrument.yaml), [CONEX-CC](instruments/newport/conex-cc/instrument.yaml), [ESP301](instruments/newport/esp301/instrument.yaml), [SMC100CC](instruments/newport/smc100/instrument.yaml), [XPS-D](instruments/newport/xps/instrument.yaml)
- **NI (National Instruments):** [DAQmx devices](instruments/ni/daqmx/instrument.yaml)
- **NKT Photonics:** [SuperK EXTREME](instruments/nkt/superk/instrument.yaml)
- **Novatech:** [409B](instruments/novatech/409b/instrument.yaml)
- **Ocean Insight:** [USB spectrometers](instruments/ocean/spectrometer/instrument.yaml)
- **Oxford Instruments:** [Mercury iPS](instruments/oxford/mercury-ips/instrument.yaml), [Mercury iTC](instruments/oxford/mercury-itc/instrument.yaml), [Triton](instruments/oxford/triton/instrument.yaml)
- **Pfeiffer Vacuum:** [TPG 362](instruments/pfeiffer/tpg36x/instrument.yaml)
- **Physik Instrumente (PI):** [C-863](instruments/pi/c-863/instrument.yaml), [E-727 / E-709 / E-712](instruments/pi/gcs-piezo/instrument.yaml)
- **PicoQuant:** [HydraHarp 400](instruments/picoquant/hydraharp-400/instrument.yaml), [MultiHarp 150](instruments/picoquant/multiharp-150/instrument.yaml)
- **QDevil (Quantum Machines):** [QDAC-II](instruments/qdevil/qdac-ii/instrument.yaml)
- **QICK (open source):** [RFSoC boards](instruments/qick/rfsoc/instrument.yaml)
- **Quantum Design:** [MultiVu systems](instruments/qd/multivu/instrument.yaml), [OptiCool](instruments/qd/opticool/instrument.yaml)
- **Quantum Machines:** [OPX+](instruments/quantum-machines/opx/instrument.yaml)
- **Rigol:** [DG1000Z](instruments/rigol/dg1000z/instrument.yaml)
- **Rohde & Schwarz:** [SGS100A](instruments/rs/sgs100a/instrument.yaml), [SMB100A](instruments/rs/smb100a/instrument.yaml), [ZNB](instruments/rs/znb/instrument.yaml)
- **Signal Recovery (AMETEK):** [7270](instruments/signal-recovery/7270/instrument.yaml)
- **SmarAct:** [MCS2](instruments/smaract/mcs2/instrument.yaml)
- **SPECS Zurich:** [Nanonis SPM Controller](instruments/specs/nanonis/instrument.yaml)
- **Spectra-Physics (MKS):** [Mai Tai](instruments/spectra-physics/mai-tai/instrument.yaml)
- **SpinCore:** [PulseBlaster](instruments/spincore/pulseblaster/instrument.yaml)
- **Stanford Research Systems:** [DG645](instruments/srs/dg645/instrument.yaml), [SG384](instruments/srs/sg384/instrument.yaml), [SR400](instruments/srs/sr400/instrument.yaml), [SR560](instruments/srs/sr560/instrument.yaml), [SR570](instruments/srs/sr570/instrument.yaml), [SR830](instruments/srs/sr830/instrument.yaml), [SR844](instruments/srs/sr844/instrument.yaml), [SR860](instruments/srs/sr860/instrument.yaml)
- **Swabian Instruments:** [Pulse Streamer 8/2](instruments/swabian/pulse-streamer/instrument.yaml), [Time Tagger](instruments/swabian/time-tagger/instrument.yaml)
- **Tektronix:** [AWG5200](instruments/tektronix/awg5200/instrument.yaml)
- **Teledyne Princeton Instruments:** [PICam cameras](instruments/princeton/picam/instrument.yaml), [SpectraPro](instruments/princeton/spectrapro/instrument.yaml)
- **Thorlabs:** [CLD1010LP](instruments/thorlabs/cld1010/instrument.yaml), [ITC4000](instruments/thorlabs/itc4000/instrument.yaml), [K10CR1](instruments/thorlabs/k10cr1/instrument.yaml), [KDC101](instruments/thorlabs/kdc101/instrument.yaml), [MC2000B](instruments/thorlabs/mc2000b/instrument.yaml), [MDT69xA](instruments/thorlabs/mdt69xa/instrument.yaml), [PM100](instruments/thorlabs/pm100/instrument.yaml), [CS165MU](instruments/thorlabs/scientific-camera/instrument.yaml)
- **TOPTICA Photonics:** [DLC pro](instruments/toptica/dlc-pro/instrument.yaml)
- **Windfreak Technologies:** [SynthHD](instruments/windfreak/synthhd/instrument.yaml)
- **Yokogawa:** [GS200](instruments/yokogawa/gs200/instrument.yaml)
- **Zurich Instruments:** [HDAWG](instruments/zhinst/hdawg/instrument.yaml), [HF2LI](instruments/zhinst/hf2li/instrument.yaml), [MFLI](instruments/zhinst/mfli/instrument.yaml), [SHFQC](instruments/zhinst/shfqc/instrument.yaml), [UHFLI](instruments/zhinst/uhfli/instrument.yaml)
