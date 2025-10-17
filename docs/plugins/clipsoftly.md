# ClipSoftly

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Clipping |
| **Type** | Clipping |
| **Status** | Latest Release |

## Description

ClipOnly2 but as a softclipper: a very handy building block

## Detailed Overview

What more needs be said? ClipSoftly is ultimate softclipping, using the techniques used on ClipOnly2 for softening the edge of the hard clipping, but on the softest possible clipping. Where ClipOnly2 manipulates the onsets of the brightest transients to give you pure hard-clipping without digital grit, ClipSoftly is doing that without even hardclipping.

So what we have here, basically, is a control-less (like ClipOnly and ClipOnly2) safety clipper, but it's a saturation effect. It's also a building block I (or others) can use inside larger plugins or new versions of Console, much like the recent Pop2 uses ClipOnly2 on the output, to give you the ability for really aggressive attacks.

You'd use something like ClipOnly2 in mastering specifically because it won't touch the values of any unclipped samples. ClipSoftly is different: it will touch the values of ALL samples, reshaping the whole sound to make it bigger, fatter, tubier.

I hope you like it, and the way it'll affect my plugins going forward :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ClipSoftly controls peaks and maximizes loudness through peak limiting. Use it as a mastering tool or creative effect.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Clipping](../categories/clipping.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ClipSoftly)

**Categories**: Clipping

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Clipping](../categories/clipping.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
