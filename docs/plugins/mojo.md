# Mojo

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Latest Release |

## Description

a biggenator that also works as a loudenator

## Detailed Overview

Happy accidents! What I was trying to do was add a blend control to Spiral, so I could make a Channel that let you go between the original, ‘fatter’ sound and the cleaner, more transparent but less fat Spiral sound.

Instead, I got this (and another, complementary plugin to be revealed later). I coded up a refinement to the algorithm, where the ‘curve factor’ of Spiral got modified by powers of itself, or powers of powers of itself… up to the fourth power, which turned out to sort of have MAGICAL powers, or at least that’s how it seemed when I worked out what was happening to my test sine waves.

Mojo’s the result. It’s a neat little algorithm that doesn’t sound anything like Density, or Spiral. Instead, it sounds like concentrated HUGE. Even at no added boost, it makes the sound a lot fatter (much like what was asked: a more refined algorithm that still gets the fatness of Density). But then there’s more… when you start slamming it.

Turns out this simple little algorithm, one single transfer function without extra parts or switches or added tricks, soaks up input gain like nothing I’ve seen.

Understand, it’s not ‘clean’. It thickens and fattens the sound without any real EQ change, by where it puts the energy and how it rounds off peaks. It’s got a weirdly effective way of being able to round stuff off and then turn it into a mostly flat-topped output, like full-on digital clipping style loudness, but with neatly sculpted little curves going in and out of the flat stuff. It’s also such a nonintuitive algorithm that I wasn’t able to find an ideal spot to just straight clip it… so, like original Spiral, if you push beyond its limits it’ll start wavefolding on you (which can be an indication of too much slam). But the sweet spot is unusually wide and forgiving, and it sounds really loud while you explore that maximum limit.

Mojo is an accident, but it’s also an obvious ‘popular’ plugin. Check to see if you’re okay with the extreme fattening effect it has, since it does really have a sound and isn’t what you’d call clean, even in the absence of extra boost. But if you were already looking for some ‘mojo’ to be added, this Mojo might be just the type… and, like the original Density algorithm, this one is likely to show up in other plugins as an added saturation element, because it’s got a distinct flavor that will help certain plugins do their thing.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Mojo processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Mojo)

**Categories**: Saturation

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Saturation](../categories/saturation.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
