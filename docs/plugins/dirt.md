# Dirt

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Distortion |
| **Type** | Distortion |
| **Status** | Latest Release |

## Description

a soft-clip distortion in the spirit of Edge

## Detailed Overview

In the event that you’d like a softer, tubier Edge… I’ve got you covered.

If you liked Airwindows Edge, this is a variation. It doesn’t go nearly as high gain but it’s got a much softer clip to it, and the same controls set up the same way (so highpass/lowpass settings ought to match if you want them to). My intent with it was to have a companion plugin to Edge for use with ITB guitars: I’d be using it with Cabs, but folks who need full-on IRs might try that too, or sandwiching your IR between Dirt and Cabs as a final tone/presentation tweak.

I hope you like it… and not just on guitars. In line with my current ultrasonic filtering approach, you’ll get more mileage out of this and Edge at high sample rates, but the lowpass will let you get some space between you and aliasing no matter what sample rate you’re at.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Drive]
    B --> C[Waveshaping]
    C --> D[Filtering]
    D --> E[Output]
    style C fill:#f59e0b
```

## How It Works

Dirt adds harmonics and edge through distortion. Use it for adding grit, warmth, or aggressive processing.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Distortion](../categories/distortion.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Dirt)

**Categories**: Distortion

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Distortion](../categories/distortion.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
