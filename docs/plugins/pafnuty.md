# Pafnuty



## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Stable |

## Description

a Chebyshev filter, that adds harmonics

## Detailed Overview

Pafnuty is a Chebyshev filter. What are those? Well, it’s not much like your usual filter: you don’t use this to roll off highs or lows (though under some conditions you might be able to do any of those things). A Chebyshev filter is like a mathematical formula. It works like this: if you feed it a sine wave (at exactly 0dB, or barely-clipping) it can generate entirely new sine waves to add to your sine wave. Which ones? Harmonically related ones. You can have twice, three, four times the frequency, all the way up to thirteenth harmonic.

Pafnuty’s been rearranged in such a way that when you move the sliders to the right, the harmonics add. (The old version used simpler math but gave a slightly weirder arrangement: you’d have to do 1.0 third harmonic, -1.0 fifth, 1.0 seventh and so on for them to add up in phase.) There’s also an attenuverter (which is what you get with a dry-wet control when it also allows for inverse-dry-wet: something out of Eurorack-land, which also existed on the Delta Labs Effectron. Side note about the funky old Effectron: it’s a delta-sigma converter like SACDs but cruder, and I’d been wanting someone to make a DIY-able delay like that. It exists! The Princeton PT2399 chip, which is in lots of current synths and pedals such as the Dreadbox Erebus)

Back to Pafnuty. What do you get when you run music into this sine-multiplying filter? If your audio has no frequencies that, multiplied, go higher than the sampling rate, you get perfect aliasing-free harmonic enhancement. The way the filter works, it absolutely doesn’t generate anything higher than the multipliers it works with. It’s a sort of color-adding harmonic enhancement where you can pick what kind of coloration you add (or subtract, since all the controls go both ways). If the frequencies do go higher than the sampling rate then they do alias, but the way Pafnuty resists adding extra harmonics helps it to resist aliasing and if you don’t add lots of higher harmonics you can go very high in frequency, cleanly.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Pafnuty processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Pafnuty)

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
