# XLowpass

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | XYZ Filters |
| **Type** | XYZ Filters |
| **Status** | Latest Release |

## Description

a distorted digital EQ, inspired by retro sampler DSP

## Detailed Overview

Welcome to the Airwindows journey into vintage sampler land! This might prove to be a long journey, but every journey starts with a first step.

Maybe the first step was Mackity and MackEQ: hardware mixer emulations. (that’s not necessarily done, either: it’s the 1202, beloved to French House music, that I did, but the DnB-hounds liked the 8-buss.) But the follow-up is just the sort of thing I might want to look into: certain of the E-mu Z-plane filters. Apparently not even the really fancy stuff… but the way that the simple lowpasses and highpasses would distort when you abused them. And it seems nobody’s that interested in exploring that, because these are not analog filters or particularly sought-after, except by those in the know.

And we know some stuff about them, because the information is out there… but a lot of devs don’t think of them as interesting. They’re biquads, with hard clipping inside the EQ code, and implemented in certain ways for efficiency: and if you can have properly made stock DAW filters, why would you want lower-bit calculation or clipping or stuff like that?

XLowpass… is NOT the end destination. There will be more like it but the X series of Airwindows filters (handy to look up in the plugin list) are NOT the carefully tailored E-mu emulation (or at least tone-alike, to the best of my ability?) XLowpass is getting familiar with the CONCEPT, an internally distorted multi-stage biquad and how I can manipulate it to get sounds out of it. It’s not meant to itself sound like an E-mu e6400 (that being the sampler I have, so far), but it’s a plugin that can dial in a whole range of the craziness people had to go to a lot of trouble to do in the real sampler (internal distorting and so on). And you can run it into Mackity and see whether you’re within striking distance of some of the more gnarly DnB tones that belonged to the 90s, seemingly lost to time.

And when the Y series comes out, things will be even more off the hook, because Y stands for “WHY would you DO that?!?” and it means I do the same thing, except with wavefolding on the internal distortion. So those should get GNARLY.

And then when I get to work on the eventual ZLowpass etc, and stack them up against real Z-plane hardware (note, however, I will not be cloning the algorithms, I am just going to try and get the tone the same), then I’ll have some practice under my belt.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

XLowpass processes audio in the XYZ Filters category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [XYZ Filters](../categories/xyz-filters.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/XLowpass)

**Categories**: XYZ Filters

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: XYZ Filters](../categories/xyz-filters.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
