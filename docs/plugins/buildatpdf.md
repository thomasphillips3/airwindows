# BuildATPDF



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

a dither-making toolkit

## Detailed Overview

I've explained how DoublePaul was made: taking a TPDF highpass dither, and including additional nearby samples to cause the tone of the noise to be more high-pitched.

Wouldn’t be fair if I didn’t give you a chance to play with it yourself :)

To use BuildATPDF the way I used it, set the middle sliders to -1 and +1. Then adjust the other sliders until you’ve tailored the sound of the noise in a way you like. With the other sliders at 0, you have PaulDither. If the surrounding sliders ‘oscillate’ (going minus, plus, minus, plus) you have more of what DoublePaul is. Tailor the highpass in ways gentle or obvious, or even darken the highpass while leaving its dither functionality intact! It’s the combination of a -1 and +1 tap that gives you highpassed TPDF. (This won’t work with +1 and +1, because it’s the same random noise passing through the plugin: it needs to play a positive node against a negative node)

Or, you can set up the -1 and +1 taps, and then just play with the sliders to see what it sounds like!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BuildATPDF processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BuildATPDF)

**Categories**: Dithers

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Dithers](../categories/dithers.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
