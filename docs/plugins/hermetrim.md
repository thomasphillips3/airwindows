# HermeTrim

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

Very Fine Adjustments, otherwise just like EveryTrim

## Detailed Overview

If you’ve seen EveryTrim, you know how this works: it’s the all-possible-trims trim. +- 12dB of left, right, mid, side, and master volume. By request, and a handy little tool for all manner of stereo tweaking. It’s very nearly as clear and accurate as PurestGain, which itself is very nearly as accurate as BitShiftGain (and most people will find any of these more than acceptable, because this is uber-pickiness land and none of you are likely to be able to tell these from your standard utility gain plugin from your DAW, ten out of ten. I just know I’ve implemented mine with extra rigorousness)

Thing is, the person who’d requested this is the same one who requested Hermepass… and in this case, I fumbled it a bit. On many DAWs, and all my Mac Audio Unit stuff, you can hold option to get tiny fine adjustments. But my user with the enlightening (and accessible) requests isn’t using a host that can do that… and needed to have much, much finer adjustments on tap.

So, now Hermepass has a companion, HermeTrim. This is exactly the same as EveryTrim, only it’s 1.5 dB plus and minus. It’s more a mastering tool: make tiny little tweaks to get the master just right. EveryTrim will sound just as good, but this one’s geared towards non-mixing purposes. Hope you like it.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

HermeTrim processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/HermeTrim)

**Categories**: Utility

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Utility](../categories/utility.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
