# YNotNotch



## Quick Info

| | |
|---|---|
| **Category** | XYZ Filters |
| **Type** | XYZ Filters |
| **Status** | Stable |

## Description

soft and smooth to nasty, edgy texture-varying filtering, no control smoothing

## Detailed Overview

YNotNotch is the final incarnation of the Y series plugins, done to give me more experience with smoothing plugin controls. It’s got a biquad filter with more than a little extra: the Y filters all have a ResEdge control. This defaults to 0.1 (like the gain control) but it can be lowered to 0 for a softer, somewhat more organic tone… or, turned up and up and up until the filter begins to distort and act weird in very unusual ways.

This is NOT like a sampler model. It’s a whole other algorithm, putting weird edges on the way the filter resonates when the Resonance is turned up. You can basically dial in the sharpness of the edge, like with the other Y filters. But unlike the other Y filters, the Resonance control goes a little further. Not in sharpness, but in dullness… you can drop resonance down to where it’s basically an ultra-shallow slope cut, put the frequency to either extreme, and use the very first hints of the Resonance control to dial in an extreme low or high cut.

And then either soften or sharpen the hell out of the edge, to get tones that don’t really exist anywhere else. This is the alternate version of YNotch, except without control smoothing. That means it'll be slightly less CPU-hungry, and might be preferable for situations like use in VCV Rack at very small buffer sizes. So, use YNotNotch if you'd like slightly more CPU efficiency, if you run tiny buffers, if you are using it as a fixed filter sound, or if you want that 'neuro' glitchy zipper-noise sound, at which it'll be really good since it already has an aggressively unnatural filter tone :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

YNotNotch processes audio in the XYZ Filters category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [XYZ Filters](../categories/xyz-filters.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/YNotNotch)

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
