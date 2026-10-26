# Optics, detection and spectroscopy

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Power meters, spectrometers, spectrographs, scientific cameras, detectors and modulators.

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
| [Princeton Instruments (Acton) SpectraPro monochromators](monochromator/princeton-spectrapro) | [community](monochromator/princeton-spectrapro/card.yaml) | RS-232, USB |  |

## Scientific cameras

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Andor CCD and EMCCD cameras (iXon, Newton, iDus)](camera/andor-ccd) | [draft](camera/andor-ccd/card.yaml) | USB, PCIe |  |
| [Andor sCMOS cameras (Zyla, Neo, Sona, Marana)](camera/andor-scmos) | [draft](camera/andor-scmos/card.yaml) | USB, PCIe |  |
| [Basler industrial cameras (pylon)](camera/basler-camera) | [community](camera/basler-camera/card.yaml) | USB, LAN |  |
| [Hamamatsu ORCA-Flash4.0 / ORCA-Quest scientific CMOS cameras (DCAM-API)](camera/hamamatsu-orca) | no card | USB, PCIe | [support](https://www.hamamatsu.com/us/en/product/cameras/software/driver-software/dcam-sdk4.html) |
| [Teledyne Princeton Instruments cameras through PICam](camera/princeton-picam) | [community](camera/princeton-picam/card.yaml) | USB, LAN |  |
| [Thorlabs Kiralux / Quantalux / Zelux scientific cameras (Scientific Camera SDK)](camera/thorlabs-scientific-camera) | no card | USB | [support](https://www.thorlabs.com/item/CS165MU) |

## Optical choppers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Thorlabs MC2000B optical chopper](chopper/thorlabs-mc2000b) | no card | USB | [manual](https://media.thorlabs.com/globalassets/items/m/mc/mc2/mc2000b/ttn102010-d02.pdf) |

## Photoelastic and electro-optic modulators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Hinds Instruments PEM-200 photoelastic modulator controller (and PEM-100)](modulator/hinds-pem) | no card | USB, LAN, RS-232 | [manual](https://www.hindsinstruments.com/wp-content/uploads/PEM-200-User-Manual.pdf) |

## Also used here

- [Montana Instruments Cryostation s-series closed-cycle optical cryostat](../cryogenics/cryostat/montana-cryostation), in cryogenics
- [Quantum Design OptiCool magneto-optical cryostat](../cryogenics/cryostat/qd-opticool), in cryogenics
