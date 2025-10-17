# MidSide

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

the other side of the EdIsDim mid/side conversion utility plugin

## Detailed Overview

It’s always nice to expand one’s horizons! You don’t have to run the latest Logic to be able to use any plugin in mid/side mode… though you might need to do a little fiddling with settings.

EdIsDim comes in two plugs: first use MidSide to convert your stereo track into mid/side (on left and right channels). Then apply your processing (there’s a control with which you can balance the mid/side balance, which also means you can gain stage the M/S content into your plugin), then, go into EdIsDim (read it backwards) to convert back to stereo. The same control is present, and can reverse the gain staging you applied.

Some good techniques include using it with Density to saturate the center and leave the stereo width lively, or getting a fresh take on a stereo reverb that’s much wider than usual. But the real purpose is opening up funky routing techniques in your DAW: send the L and R to separate busses, do all manner of things with plugins that don’t even have to be the same, or to line up (sample delay on just mid or side, anyone?) and merge them back to a stereo buss with EdIsDim on it. Or design weird synth patches that are heavy on the left with a lot of odd stereo behaviors, just to run into EdIsDim as an intentional part of the synth sound. Sky’s the limit :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

MidSide processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/MidSide)

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
