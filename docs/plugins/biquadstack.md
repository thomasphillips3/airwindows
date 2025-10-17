# BiquadStack

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Latest Release |

## Description

a way of making a parametric EQ out of stacked biquad filters

## Detailed Overview

There's already a plugin called BiquadTriple, and it's three biquads simply cascaded to do what they do with steeper roll-offs before resonance. I'd said 'this is to let you mock up effects where you're going to be using filters' and mentioned 'ways to make the Q factors more specific and staggered' but didn't really go there, at the time.

That time arrived in a hurry when I started really trying to work out what was so special about SSL channel strips, so I could use similar parametric bands in ConsoleX.

So, BiquadStack is out to let you use this right away, without waiting, and see how that goes. The way it works is, it has the same technique used to make very steep Butterworth filters. This is using specific Q factors in combination, so they end up doing a very accurate highpass or lowpass without resonance or irregularities. Typically, when you find this stuff it's carefully designed to behave correctly, and you can make steep Butterworth filters of whatever order you like, this way.

Using it for bandpasses instead, and adding nonlinearity, gives you a really interesting response: it's not a narrowing spike as a normal resonant filter would be, instead it's a little region of intensity that you can bring in or remove. The nonlinearity increases as you add more boost, or stays subtle at lower settings. The edges of the region develop little 'moats' to accentuate the effect: some sort of phase interference.

The result is what I wanted: tight and effective parametric EQ which is not 'analog modeled', it's designed to do what I'd WANT to do with analog modeling. It's about letting through the energy and sonority (or suppressing energy you don't want) rather than trying to duplicate tone colors of some hardware and muddying things up. This one is full-range, and smoothed, because there's only one of it: if you want to do sweepy automation things keep it around. There will be more, like a three-band that can fit in Airwindows Consolidated, and the full SSL-style four-band that goes in ConsoleX.

If you want to get a head start on what that will bring you, play with BiquadStack. If you want four bands of it on every channel in your whole mix… well so do I, and I'm working on it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BiquadStack processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BiquadStack)

**Categories**: Biquads

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Biquads](../categories/biquads.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
