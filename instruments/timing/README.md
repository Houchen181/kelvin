# Timing, pulses and photon counting

<!-- Written by `python tools/kic.py index` from the instrument.yaml files; edit those, not this. -->

Pulse pattern and delay generators, photon counters and time taggers.

## Pulse pattern generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [SpinCore PulseBlaster pulse generators](pulse-generator/spincore-pulseblaster) | [community](pulse-generator/spincore-pulseblaster/card.yaml) | USB, PCIe |  |
| [Swabian Instruments Pulse Streamer 8/2](pulse-generator/swabian-pulse-streamer) | [community](pulse-generator/swabian-pulse-streamer/card.yaml) | LAN | [manual](https://www.swabianinstruments.com/static/documentation/pulse-streamer/v2.1/sections/api-doc.html) |

## Digital delay generators

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [Stanford Research DG645 digital delay generator](delay-generator/srs-dg645) | [community](delay-generator/srs-dg645/card.yaml) | GPIB, RS-232, LAN | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/DG645m.pdf) |

## Photon counters, time taggers and TCSPC

| Instrument | Card | Talks over | Manual |
|---|---|---|---|
| [PicoQuant HydraHarp 400 TCSPC / time tagger](photon-counter/picoquant-hydraharp-400) | no card | USB | [manual](https://downloads.picoquant.com/manuals/discontinued/HydraHarp400_DLL_Manual.pdf) |
| [PicoQuant MultiHarp 150 time tagger](photon-counter/picoquant-multiharp-150) | no card | USB | [manual](https://downloads.picoquant.com/manuals/MultiHarp150_160_DLL_Manual.pdf) |
| [Stanford Research Systems SR400 gated photon counter](photon-counter/srs-sr400) | no card | GPIB, RS-232 | [manual](https://www.thinksrs.com/downloads/pdfs/manuals/SR400m.pdf) |
| [Swabian Instruments Time Tagger (20, Ultra, X)](photon-counter/swabian-time-tagger) | [community](photon-counter/swabian-time-tagger/card.yaml) | USB | [manual](https://www.swabianinstruments.com/static/documentation/TimeTagger/api/measurements/event_counting.html) |
