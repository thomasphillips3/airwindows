# YNotLowpass



## Quick Info

| | |
|---|---|
| **Category** | XYZ Filters |
| **Type** | XYZ Filters |
| **Status** | Stable |

## Description

soft and smooth to nasty, edgy texture-varying filtering, no control smoothing

## Detailed Overview

YNotLowpass introduces a new way to internally distort filters, and a new control… Resonant Edge! The ‘normal’ position for this is around 0.1 on the control. If you make it less, you get a slightly asymmetrical distortion that lets you get really warm analog filter sounds, even when they’re resonant. If you crank it up, the Resonant Edge lets you go to very aggressive, glitchy sounds that are a lot more like circuit bending than bit-banging.

This is the alternate version of YLowpass, except without control smoothing. That means it'll be slightly less CPU-hungry, and might be preferable for situations like use in VCV Rack at very small buffer sizes. These are also buying me some time to work on the upcoming ConsoleMC, which is beginning to take shape… and on a new update for ToTape, for which I've got an idea for a bias control. So, use YNotLowpass if you'd like slightly more CPU efficiency, if you run tiny buffers, if you are using it as a fixed filter sound, or if you want that 'neuro' glitchy zipper-noise sound, at which it'll be really good since it already has an aggressively unnatural filter tone :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

YNotLowpass processes audio in the XYZ Filters category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [XYZ Filters](../categories/xyz-filters.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/YNotLowpass)

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
