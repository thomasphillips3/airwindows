# BassAmp

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

an old plugin with new tweaks, that gives some bass guitar tones

## Detailed Overview

This is BassAmp. (I’ve been asked to do amp sim type plugins, so it’s a start). Back in the day I experimented with some of these things, though I’ve always been more interested in wiring up physical hardware, especially for guitar distortions and things. I’ve brought this one up to date in some ways, debugging a problem with the ‘dub’ channel and using my modern techniques for dithering to the floating point bus, and so on.

It’s got basically a bright channel, midrange (which is just dry, as a slider), a bass channel with a characteristic woolly tone that has a kind of noisy blur on the small amount of treble it does have, and a ‘sub’ channel that really doesn’t work, so use it as a crazy special effect. BassKit might get you a cleaner sub-octave, but this will give you a trashy sub-octave that’s mostly garbage, even on a single-note line. So you’ll be leaving it off, I think.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BassAmp processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BassAmp)

**Categories**: Amp Sims

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Amp Sims](../categories/amp-sims.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
