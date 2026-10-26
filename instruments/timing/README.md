# Timing, pulses and photon counting

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Pulse and delay generators, experiment sequencers, photon counters, counters and clocks.

## Pulse pattern generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Avtech -B series high-speed pulse generators (rise time 1 ns and below)](pulse-generator/avtech-pulse-generator) | no card | GPIB, RS-232, LAN | [manual](https://www.avtechpulse.com/manuals/programming/programming.pdf) |
| [Keysight 81150A and 81160A pulse function arbitrary noise generators](pulse-generator/keysight-81160a) | no card | GPIB, USB-TMC, LAN | [sign-in](https://www.keysight.com/us/en/assets/9018-03445/user-manuals/9018-03445.pdf) |
| [SpinCore PulseBlaster pulse generators](pulse-generator/spincore-pulseblaster) | [community](pulse-generator/spincore-pulseblaster/card.yaml) | USB, PCIe |  |
| [Swabian Instruments Pulse Streamer 8/2](pulse-generator/swabian-pulse-streamer) | [community](pulse-generator/swabian-pulse-streamer/card.yaml) | LAN | [manual](https://www.swabianinstruments.com/static/documentation/pulse-streamer/v2.1/sections/api-doc.html) |

## Digital delay generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Berkeley Nucleonics Model 575 and 577 digital delay and pulse generators](delay-generator/bnc-577) | no card | USB, RS-232, LAN, GPIB | [manual](https://www.berkeleynucleonics.com/docs/bnc-model-577-user-manual.html) |
| [Stanford Research DG645 digital delay generator](delay-generator/srs-dg645) | [community](delay-generator/srs-dg645/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DG645m.pdf) |

## Experiment sequencers and control systems

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [ARTIQ and Sinara hardware (Kasli, Urukul, Zotino, Sampler, Phaser, Mirny)](sequencer/m-labs-artiq-sinara) | no card | LAN | [manual](https://m-labs.hk/artiq/manual/) |

## Photon counters, time taggers and TCSPC

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [ID Quantique ID900 and ID1000 Time Controllers](photon-counter/idquantique-id900) | no card | LAN | [support](https://www.idquantique.com/quantum-detection-systems/products/id1000-time-controller/) |
| [PicoQuant HydraHarp 400 TCSPC / time tagger](photon-counter/picoquant-hydraharp-400) | no card | USB | [manual](https://downloads.picoquant.com/manuals/discontinued/HydraHarp400_DLL_Manual.pdf) |
| [PicoQuant MultiHarp 150 time tagger](photon-counter/picoquant-multiharp-150) | no card | USB | [manual](https://downloads.picoquant.com/manuals/MultiHarp150_160_DLL_Manual.pdf) |
| [qutools quTAG time-to-digital converter](photon-counter/qutools-qutag) | no card | USB | [manual](https://www.qutools.com/files/quTAG/documentation/) |
| [Stanford Research Systems SR400 gated photon counter](photon-counter/srs-sr400) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR400m.pdf) |
| [Swabian Instruments Time Tagger (20, Ultra, X)](photon-counter/swabian-time-tagger) | [community](photon-counter/swabian-time-tagger/card.yaml) | USB | [manual](https://www.swabianinstruments.com/static/documentation/TimeTagger/api/measurements/event_counting.html) |

## Frequency and time-interval counters

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Keysight 53230A universal frequency counter/timer](frequency-counter/keysight-53230a) | no card | GPIB, USB-TMC, LAN | [support](https://www.keysight.com/us/en/assets/7018-02642/data-sheets/5990-6283.pdf) |
| [Stanford Research Systems SR620 universal time interval counter](frequency-counter/srs-sr620) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR620m.pdf) |

## Frequency references and clocks

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Stanford Research Systems FS725 rubidium frequency standard](frequency-reference/srs-fs725) | no card | RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/FS725m.pdf) |
