# Optics, detection and spectroscopy

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Detectors, spectrometers, cameras, modulators, shutters, light shaping and fiber optics.

## Optical power and energy meters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Newport 2936-R / 1936-R optical power meters](power-meter/newport-2936-r) | no card | USB, RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/npresources/hc4/h06/10082698067998/19xx-29xx-R-Power-Meter-Commands_Ver01/19xx-29xx-R-Power-Meter-Commands-Ver01.pdf) |
| [Thorlabs PM100D / PM100USB / PM400 optical power meters](power-meter/thorlabs-pm100) | [community](power-meter/thorlabs-pm100/card.yaml) | USB-TMC | [manual](https://media.thorlabs.com/globalassets/items/p/pm/pm1/pm100d/17654-d02.pdf) |

## Spectrometers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [HORIBA iHR320 / iHR550 imaging spectrometers](spectrometer/horiba-ihr) | no card | USB | [manual](https://horiba-python-sdk.readthedocs.io/en/latest/icl_api/) |
| [Ocean Insight USB spectrometers (Flame, HR, QE Pro, USB2000+)](spectrometer/ocean-spectrometer) | [community](spectrometer/ocean-spectrometer/card.yaml) | USB |  |

## Monochromators and imaging spectrographs

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Andor Shamrock and Kymera spectrographs](monochromator/andor-shamrock) | [community](monochromator/andor-shamrock/card.yaml) | USB |  |
| [Newport Oriel Cornerstone 130 and 260 monochromators](monochromator/newport-cornerstone) | no card | RS-232, USB, GPIB | [manual](https://api.p1.mks.com/medias/sys_master/software/software/h30/hb7/9358972125214/90088262B-MCS130B-Manual.pdf) |
| [Princeton Instruments (Acton) SpectraPro monochromators](monochromator/princeton-spectrapro) | [community](monochromator/princeton-spectrapro/card.yaml) | RS-232, USB |  |

## Optical spectrum analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Anritsu MS9740A optical spectrum analyzer](optical-spectrum-analyzer/anritsu-ms9740) | no card | GPIB, LAN | [manual](https://dl.cdn-anritsu.com/en-au/test-measurement/files/Manuals/Operation-Manual/MS9740A/MS9740A_Remote_Operation_Manual_SCPI_e_5_0.pdf) |
| [Yokogawa AQ6370D optical spectrum analyzer](optical-spectrum-analyzer/yokogawa-aq6370) | no card | GPIB, LAN, RS-232 | [manual](https://cdn.tmi.yokogawa.com/1/6057/files/IMAQ6370C-17EN.pdf) |

## Scientific cameras

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Andor CCD and EMCCD cameras (iXon, Newton, iDus)](camera/andor-ccd) | [draft](camera/andor-ccd/card.yaml) | USB, PCIe |  |
| [Andor sCMOS cameras (Zyla, Neo, Sona, Marana)](camera/andor-scmos) | [draft](camera/andor-scmos/card.yaml) | USB, PCIe |  |
| [Basler industrial cameras (pylon)](camera/basler-camera) | [community](camera/basler-camera/card.yaml) | USB, LAN |  |
| [Hamamatsu ORCA-Flash4.0 / ORCA-Quest scientific CMOS cameras (DCAM-API)](camera/hamamatsu-orca) | no card | USB, PCIe | [support](https://www.hamamatsu.com/us/en/product/cameras/software/driver-software/dcam-sdk4.html) |
| [Nüvü Camēras HNü EMCCD cameras](camera/nuvu-hnu) | no card | LAN | [support](https://www.nuvucameras.com/products/hnu-512/) |
| [Teledyne Photometrics Kinetix sCMOS camera (PVCAM SDK)](camera/teledyne-kinetix) | no card | PCIe, USB | [manual](https://docs.teledynevisionsolutions.com/pvcam-sdk/) |
| [Teledyne Princeton Instruments cameras through PICam](camera/princeton-picam) | [community](camera/princeton-picam/card.yaml) | USB, LAN |  |
| [Thorlabs Kiralux / Quantalux / Zelux scientific cameras (Scientific Camera SDK)](camera/thorlabs-scientific-camera) | no card | USB | [support](https://www.thorlabs.com/item/CS165MU) |

## Photodiodes, APDs, PMTs and quadrant detectors

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs PDQ80A quadrant detector with KPA101 K-Cube position aligner](photodetector/thorlabs-pdq80a) | no card | USB, analog | [manual](https://media.thorlabs.com/contentassets/e92d618c92c94cea9096b3f231859611/etn033528-d02.pdf) |

## Beam profilers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs BP209 slit-scanning beam profiler](beam-profiler/thorlabs-bp209) | no card | USB | [manual](https://media.thorlabs.com/globalassets/items/b/bp/bp2/bp209-ir2_m/doc-104056.pdf) |

## Polarimeters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs PAX1000 polarimeter](polarimeter/thorlabs-pax1000) | no card | USB-TMC | [manual](https://github.com/Thorlabs/Light_Analysis_Examples/blob/main/Python/Thorlabs%20PAX1000%20Polarimeters/SCPI_command_docu/pax1000.html) |

## Autocorrelators and pulse characterization

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [APE pulseCheck autocorrelator](autocorrelator/ape-pulsecheck) | no card | USB, LAN | [support](https://www.ape-berlin.de/en/autocorrelator/pulsecheck/) |

## Optical choppers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs MC2000B optical chopper](chopper/thorlabs-mc2000b) | no card | USB | [manual](https://media.thorlabs.com/globalassets/items/m/mc/mc2/mc2000b/ttn102010-d02.pdf) |

## Photoelastic and electro-optic modulators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Hinds Instruments PEM-200 photoelastic modulator controller (and PEM-100)](modulator/hinds-pem) | no card | USB, LAN, RS-232 | [manual](https://www.hindsinstruments.com/wp-content/uploads/PEM-200-User-Manual.pdf) |

## Shutters, filter wheels and flip mounts

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs FW102C six-position motorized filter wheel](shutter/thorlabs-fw102c) | no card | RS-232, USB |  |
| [Thorlabs MFF101 motorized filter flip mount](shutter/thorlabs-mff101) | no card | USB | [manual](https://media.thorlabs.com/contentassets/e92d618c92c94cea9096b3f231859611/etn012604-d02.pdf) |
| [Thorlabs SC10 optical beam shutter controller](shutter/thorlabs-sc10) | no card | RS-232 | [support](https://media.thorlabs.com/contentassets/e92d618c92c94cea9096b3f231859611/etn017648-d02.pdf) |
| [Uniblitz VMM-D3 three-channel shutter driver](shutter/uniblitz-vmm-d3) | no card | RS-232, analog | [manual](https://www.uniblitz.com/wp-content/uploads/2021/08/VMM_D3_D4-User-Manual-2.10_Rev_B.pdf) |

## Spatial light modulators and DMDs

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Hamamatsu X13138 series LCOS-SLM phase spatial light modulator](spatial-light-modulator/hamamatsu-lcos-slm) | no card |  | [support](https://www.hamamatsu.com/us/en/product/optical-components/lcos-slm.html) |
| [HOLOEYE PLUTO-2.1 and GAEA-2 spatial light modulators (SLM Display SDK)](spatial-light-modulator/holoeye-slm) | no card | USB | [sign-in](https://customers.holoeye.com/) |
| [Meadowlark Optics liquid-crystal spatial light modulators (1920x1152, 1920x1200, 1024x1024 and 1536x1536 formats)](spatial-light-modulator/meadowlark-slm) | no card | PCIe | [support](https://www.meadowlark.com/shop/slms/1536-x-1536-spatial-light-modulator/) |
| [santec SLM-200 spatial light modulator](spatial-light-modulator/santec-slm-200) | no card | USB | [sign-in](https://aoc.santec.com/en/support/usermanuals/slm/) |
| [ViALUX V-7000 DMD module with the ALP-4.3 API](spatial-light-modulator/vialux-dmd) | no card | USB | [sign-in](https://www.vialux.de/ViALUX-Website/registration-for-download.html) |

## Fiber switches, attenuators and polarization controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [DiCon GP700 programmable fiber optic switch](fiber-optics/dicon-gp700) | no card |  | [support](https://www.diconfiberoptics.com/resources/legacy-products.php) |
| [Keysight 8164B lightwave measurement system](fiber-optics/keysight-8164b) | no card | GPIB, LAN | [support](https://www.keysight.com/us/en/product/8164B/lightwave-measurement-system.html) |
| [Thorlabs MPC320 motorized fiber polarization controller](fiber-optics/thorlabs-mpc320) | no card | USB | [support](https://media.thorlabs.com/contentassets/5f57e82e38004e2aa5dfd0071bcf0732/kinesis_with_c_quick_start_guide.pdf) |

## Broadband lamps and LED drivers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Energetiq EQ-99X laser-driven light source](light-source/energetiq-eq-99x) | no card |  | [manual](https://www.energetiq.com/hubfs/Product%20Manuals/LDLS/EQ-99X%20LDLS%20Operation%20Maintenance%20Manual.pdf) |
| [Newport (Oriel) 69911 arc lamp power supply](light-source/newport-69911) | no card | RS-232 | [manual](https://api.p1.mks.com/medias/sys_master/root/h70/hc3/9574045974558/90073995B-M69911-Arc-Lamp-Power-Supply-Manual.pdf) |
| [Thorlabs DC4100 four-channel LED driver](light-source/thorlabs-dc4100) | no card |  |  |

## Also used here

- [Montana Instruments Cryostation s-series closed-cycle optical cryostat](../cryogenics/cryostat/montana-cryostation), in cryogenics
- [Quantum Design OptiCool magneto-optical cryostat](../cryogenics/cryostat/qd-opticool), in cryogenics
