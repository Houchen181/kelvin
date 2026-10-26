# Cryogenics, vacuum and sample environment

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Temperature control, cryostats and dilution refrigerators, compressors, vacuum, strain and pressure.

## Temperature controllers and monitors

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Cryo-con Model 24C cryogenic temperature controller](temperature-controller/cryocon-24c) | no card | LAN, RS-232, GPIB, USB | [support](https://qd-europe.com/de/en/news/product-application-news-spectrum/find-the-right-temperature-monitor-and-controller-for-your-cryogenic-experiments) |
| [Lake Shore Model 218 temperature monitor](temperature-controller/lakeshore-218) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/218_manual.pdf) |
| [Lake Shore Model 331 and 332 cryogenic temperature controllers](temperature-controller/lakeshore-331) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/331_manual.pdf) |
| [Lake Shore Model 335 / 336 temperature controller](temperature-controller/lakeshore-336) | [community](temperature-controller/lakeshore-336/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/336manual.pdf?sfvrsn=fa4e3a80_12) |
| [Lake Shore Model 340 cryogenic temperature controller](temperature-controller/lakeshore-340) | no card | GPIB, RS-232 | [manual](https://www.lakeshore.com/docs/default-source/product-downloads/manuals/340_manual.pdf) |
| [Lake Shore Model 350 temperature controller](temperature-controller/lakeshore-350) | [community](temperature-controller/lakeshore-350/card.yaml) | USB, LAN, GPIB | [manual](https://www.lakeshore.com/docs/default-source/software/manuals/350_manual.pdf?sfvrsn=501e9331_5) |
| [Oxford Instruments ITC503 intelligent temperature controller](temperature-controller/oxford-itc503) | no card | RS-232, GPIB | [support](https://qd-oxford.com/services/legacy_product_support.html) |
| [Oxford Instruments Mercury iTC temperature controller](temperature-controller/oxford-mercury-itc) | [community](temperature-controller/oxford-mercury-itc/card.yaml) | USB, LAN, RS-232, GPIB | [manual](https://www.mymercurysupport.com/sites/default/files/59_UMC0071_EN_02.pdf) |
| [SRS SIM922 diode temperature monitor](temperature-controller/srs-sim922) | no card | RS-232, GPIB | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SIM922m.pdf) |

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

## Cryocooler compressors

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Cryomech CPA helium compressors (remote monitoring)](compressor/cryomech-cpa) | no card |  | [support](https://bluefors.com/support/) |
| [Sumitomo F-70 helium compressor](compressor/sumitomo-f-70) | no card | RS-232 | [support](https://shicryogenics.com/product/f-70-indoor-water-cooled-compressor-series/) |

## Cryogen level meters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [AMI Model 1700 liquid level instrument](level-meter/ami-1700) | no card | LAN, RS-232 | [manual](https://www.americanmagnetics.com/support/manuals/Model1700-Rev6.pdf) |
| [Cryomagnetics LM-510 liquid cryogen level monitor](level-meter/cryomagnetics-lm-510) | no card | USB, LAN, GPIB, RS-232 | [manual](https://cryomagnetics.com/wp-content/uploads/2022/05/LM_510_Rev1_3.pdf) |
| [Oxford Instruments ILM200 helium level meter](level-meter/oxford-ilm200) | no card | RS-232 | [support](https://qd-oxford.com/services/legacy_product_support.html) |

## Heating and cooling stages

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Instec mK2000 temperature controller for heating and cooling stages](heating-stage/instec-mk2000) | no card | USB, LAN | [support](https://instec.com/TCA/46.html) |
| [Linkam T96 controller with THMS600 heating and cooling stage](heating-stage/linkam-t96) | no card | USB | [support](https://www.linkam.co.uk/t96) |

## Chillers and circulators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [JULABO circulators and recirculating coolers](chiller/julabo-circulator) | no card | USB, RS-232, RS-485, LAN | [manual](https://dbyt75tph3sip.cloudfront.net/asset/512030579289/document_qr637chm0l11lekorrrhucvk57/1.950.2823.en.V08.pdf) |

## Vacuum gauges and controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Pfeiffer Vacuum TPG 361 / TPG 362 SingleGauge / DualGauge vacuum gauge controllers](vacuum-gauge/pfeiffer-tpg36x) | no card | RS-485, USB, LAN | [manual](https://www.shop.buschgroup.com/api/empolis/resource/environment/project1_p/documents/pfeifferSharepointProd/2181-bg5510ben_d.pdf) |

## Vacuum pump controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Agilent 4UHV ion pump controller](vacuum-pump/agilent-4uhv) | no card |  |  |
| [Edwards TIC turbo and instrument controller](vacuum-pump/edwards-tic) | no card | RS-232 | [support](https://www.edwardsvacuum.com/content/dam/brands/edwards-vacuum/general-vacuum/downloads/measurement-and-control/vacuum-gauge-and-pump-controllers/3601-0654-01-TIC-Turbo-and-Instr-Controller-Datasheet.pdf) |
| [Gamma Vacuum SPCe ion pump controller](vacuum-pump/gamma-vacuum-spce) | no card | RS-232, RS-485, LAN | [support](https://www.gammavacuum.com/products/digital-spc-ion) |
| [Pfeiffer Vacuum HiCube pumping stations and TC 400 turbo drive unit](vacuum-pump/pfeiffer-hicube) | no card | RS-485 | [manual](https://www.shop.buschgroup.com/api/empolis/resource/environment/project1_p/documents/pfeifferSharepointProd/1548-pt0265ben_f.pdf) |
| [SAES NEXTorr NEG-ion pumps with the NIOPS controller](vacuum-pump/saes-nextorr) | no card |  |  |

## Residual gas analyzers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [SRS RGA100 / RGA200 / RGA300 residual gas analyzers](rga/srs-rga) | no card | RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/RGAm.pdf) |

## Uniaxial strain cells

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Razorbill RP100 power supply for CS100 / CS130 uniaxial strain cells](strain-cell/razorbill-rp100) | no card | USB | [manual](https://razorbillinstruments.com/wp-content/uploads/2023/06/RP100-Manual-v6-9-Web.pdf) |

## Pressure-cell controllers

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Almax easyLab Diacell iGM gas-membrane pressure controller](pressure-controller/almax-easylab-membrane) | no card | RS-232, GPIB, LAN, USB | [support](https://www.almax-easylab.com/product/diacell-igm-controller/) |

## Also used here

- [Lake Shore Model 370 AC resistance bridge](../electronics/resistance-bridge/lakeshore-370), in electronics
- [Lake Shore Model 372 AC resistance bridge and temperature controller](../electronics/resistance-bridge/lakeshore-372), in electronics
- [Picowatt AVS-47B AC resistance bridge](../electronics/resistance-bridge/picowatt-avs-47), in electronics
- [SRS SIM921 AC resistance bridge](../electronics/resistance-bridge/srs-sim921), in electronics
