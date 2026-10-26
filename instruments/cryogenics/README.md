# Cryogenics, vacuum and sample environment

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Temperature controllers, cryostat systems, dilution refrigerators and vacuum gauges.

## Temperature controllers and monitors

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Cryo-con Model 24C cryogenic temperature controller](temperature-controller/cryocon-24c) | no card | LAN, RS-232, GPIB, USB | [support](https://qd-europe.com/de/en/news/product-application-news-spectrum/find-the-right-temperature-monitor-and-controller-for-your-cryogenic-experiments) |
| [Lake Shore Model 218 temperature monitor](temperature-controller/lakeshore-218) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/218_manual.pdf) |
| [Lake Shore Model 335 / 336 temperature controller](temperature-controller/lakeshore-336) | [community](temperature-controller/lakeshore-336/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/336manual.pdf?sfvrsn=fa4e3a80_12) |
| [Lake Shore Model 340 cryogenic temperature controller](temperature-controller/lakeshore-340) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/340_manual.pdf) |
| [Lake Shore Model 350 temperature controller](temperature-controller/lakeshore-350) | [community](temperature-controller/lakeshore-350/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/software/manuals/350_manual.pdf?sfvrsn=501e9331_5) |
| [Oxford Instruments Mercury iTC temperature controller](temperature-controller/oxford-mercury-itc) | [community](temperature-controller/oxford-mercury-itc/card.yaml) | USB, LAN, RS-232, GPIB | [manual](https://www.mymercurysupport.com/sites/default/files/59_UMC0071_EN_02.pdf) |

## Cryostat systems

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [attocube attoDRY closed-cycle cryostats](cryostat/attocube-attodry) | [draft](cryostat/attocube-attodry/card.yaml) | USB |  |
| [Montana Instruments Cryostation s-series closed-cycle optical cryostat](cryostat/montana-cryostation) | no card | LAN | [manual](https://cdn.prod.website-files.com/6118466f5c775b56d53d49e9/695d7ffcee2d9010efc7f5a4_4100-1-DOC002_1.2%20(User%20Manual%20-%20Cryostation%20s-series%20-%20SHI%20Configuration%20MI75%20VCM).pdf) |
| [Quantum Design PPMS, DynaCool, VersaLab and MPMS3 through MultiVu](cryostat/qd-multivu) | [community](cryostat/qd-multivu/card.yaml) | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) |
| [Quantum Design OptiCool magneto-optical cryostat](cryostat/qd-opticool) | no card | LAN | [manual](https://qdusa.com/siteDocs/appNotes/1070-220.pdf) |

## Dilution refrigerators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Bluefors dilution refrigerators (Control Software, temperature controller, gas handling system)](dilution-refrigerator/bluefors-dilution-refrigerator) | no card | LAN, web API | [manual](https://github.com/BlueforsOy/Control_Software_gen2_API_examples/blob/main/README.md) |
| [Oxford Instruments Triton dilution refrigerator](dilution-refrigerator/oxford-triton) | no card | LAN | [support](https://qd-oxford.com/services/legacy_product_support.html) |

## Vacuum gauges and controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Pfeiffer Vacuum TPG 361 / TPG 362 SingleGauge / DualGauge vacuum gauge controllers](vacuum-gauge/pfeiffer-tpg36x) | no card | RS-485, USB, LAN | [manual](https://www.shop.buschgroup.com/api/empolis/resource/environment/project1_p/documents/pfeifferSharepointProd/2181-bg5510ben_d.pdf) |

## Also used here

- [Lake Shore Model 372 AC resistance bridge and temperature controller](../electronics/resistance-bridge/lakeshore-372), in electronics
