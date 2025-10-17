# ZRegion2

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | XYZ Filters |
| **Type** | XYZ Filters |
| **Status** | Latest Release |

## Description

an Emu e6400 style Airwindows Region filter, with control smoothing

## Detailed Overview

ZRegion2 comes out at the same time as ZRegion, but note that I'm still putting out ZRegion. This is because ZRegion will always run at lower CPU than ZRegion2, because the first plugin doesn't do coefficient smoothing. It's for if you have a fixed tone setting to use, OR if you want to have a slight glitchy/zipper-noise quality on some audio and you're moving the controls.

If you're going for automation, the Z2 filters are the ones that interpolate the coefficients across the sample buffer, meaning they'll make control changes smooth. No crackling! This eats more CPU, but a lot of the fun with these filters comes from actively manipulating them. The original sampler never had a Region filter type, but now you can make believe it did, and produce aggressive and textural bandpass-y effects across a broader range than the original sampler's ZBandpass. Hope you like it!


This concludes the AirwindowsPedia. Expect this file to be expanded as new plugins come in. Might end up needing one of these for the Free Studio sample instruments, eventually…

-chris

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ZRegion2 processes audio in the XYZ Filters category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [XYZ Filters](../categories/xyz-filters.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ZRegion2)

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
