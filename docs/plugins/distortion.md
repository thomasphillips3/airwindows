# Distortion

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Distortion |
| **Type** | Distortion |
| **Status** | Latest Release |

## Description

a slightly dark analog-style distortion with several presets, like Focus

## Detailed Overview

I think this one ought to go over well. People often want ‘analog-style distortion’. Here’s a collection of Airwindows distortion algorithms in a handy plugin with a new twist: it’s optimized for high sample rate in an innovative way.

What does that mean? Distortion is a slightly ‘dark’ distortion plugin. Not only are the algorithms pretty smooth (with some exceptions: check the end of the video for one!), it uses sample averaging to stop extreme highs from getting through. At 44.1k, there’s an averaging stage before the distortion, darkening the output but also interfering with aliasing. Averaging also has some tonal benefits to midrange and bass, so this gives the plugin more of a ‘voice’. That’s at 44.1k, CD quality.

But, if you use higher rates like 96k or 192k, Distortion begins to use more ‘poles’ of simple averaging. It’ll bring in averaging after the distortion, softening the tone. It’ll use more and more stages of this treble-softening, still always on just the most recent two samples, even though that becomes more and more finely grained as the sample rate goes up. Because of how averaging works, this never brings in weird notches or cancellations (like broader averages) but it does produce a sort of bleed-off of highs. Run at 44.1k this would give you an increasingly wide roll-off.

At the high sample rates this was designed for, what you get instead is exactly the same ‘dark distortion’ tonality, but increasingly better aliasing rejection as the sample rate goes up. I think 96k is a sweet spot for this: at 96k, still a basically normal sample rate, you get extremely warm and fluid distortion, even when pushed to extremes.

If you like extremes, look into the final two distortion modes. In Distortion, the modes Mojo and Dyno operate in their purest form, where the distortion shape can curl around again to produce strange effects if you slam them ruthlessly. In the video you see me discovering this on Mojo, running a simple DI bass at far too high a volume into Mojo, and then doubling it up to make crazy organic synth-like effects. Other modes like Density, Drive or Spiral will just go to ultra-clipping normally.

Distortion will give you truly warm overdrive effects, especially at high sample rates, without a bunch of fake analog modeling. I don’t recommend using it on everything (because maybe some sounds are good WITH extended high-end, especially if you’re working at 96k and all) but as always, I’m not the boss of you.

Again, the notable thing about this relative to other cascaded aliasing-suppressed distortions like Console7Cascade is that Distortion is doing it all with simple averaging filters. That will give you a distinct, softer sound without the clarity you get from multi-pole biquad rolloffs. Distortion is for when you want warm, warm, warm and are OK with letting the highs soften, plus if you want to pick different sorts of crunch edge (not often a feature on Airwindows plugins).

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

Distortion adds harmonics and edge through distortion. Use it for adding grit, warmth, or aggressive processing.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Distortion](../categories/distortion.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Distortion)

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
