# ToVinyl4

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

a vinyl-mastering simulator bringing several vinyl-type colors

## Detailed Overview

ToVinyl has several uses. You can use it to reshape the bass in your track, making it more mono or tightening up the center. It’s a special multipole IIR filter that acts almost like a ‘mega-bass’ plugin: it doesn’t just take away, it rearranges (so don’t expect it to act like a normal digital cut, you might see increased peak energy down low.)

Then, there’s the acceleration limiter. This algorithm is unlike any other Airwindows treble-reducer: it zeroes in on just the sorts of transients that’d burn up a cutting head, and zaps them ruthlessly. (if you own a cutting head you’re responsible for checking this, but some of you folks are still using Spitfish, and I’m pretty sure this will way outperform Spitfish.) The effect is treble softening without any obvious treble reduction, and it’ll make stuff sound like classic vinyl grooves very effectively.

But that’s nothing compared to the next control, Groove Wear. This one analyzes the virtual groove, and then sets up an imaginary stylus going down that groove, and gives it a tiny bit of inertia. It’s more slew mojo (and not tied to any particular frequency, it doesn’t even know what a frequency is) and the effect (should you choose to use it) is a very characteristic darkening and slight trashening of the most extreme highs. You can shut it off entirely, or turn it up, and you can combine it with the acceleration limiter to get pretty much any ‘vinyl LP high end’ you want. Some settings even bring a touch of moving-coil sparkle: it’s not all darken, in fact Groove Wear is very much its own thing distortion-wise.

Combine it all together and you’ve got ToVinyl4, the up-to-date version of a classic Airwindows for-pay plugin.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ToVinyl4 processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ToVinyl4)

**Categories**: Stereo

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Stereo](../categories/stereo.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
