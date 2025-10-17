# TPDFDither

![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

TPDF dither. With 16/24 bit output and a DeRez control

## Detailed Overview

TPDF is the industry standard technically correct boring dither. It does nothing strange or interesting, makes no effort to optimize the sound in any way (generally if you make it better for something it’s worse for something else: even Naturalize only has a limited amount of output bits to work with.)

TPDF uses two sources of noise to make what’s called a Triangular Probability Density Function, which gives it its name. If you had only one noise source, you’d get what’s called flat dither (I’m not offering that, but it’s in Ditherbox, along with truncation.) When you only have one noise source (at the correct volume, which is one bit wide) you get dithering and sounds correctly transition into silence instead of going insane with grating gnarlyness (which is what happens with truncation, anywhere and everywhere it happens) but with only the one noise source you get an effect where the noise level flutters and shifts depending on what the audio’s doing. I demonstrate this in the video, it’s quite noticeable.

With the two noise sources, TPDF transitions sounds into silence, and still keeps a totally unvarying noise profile. In a very real way, this is more analog-like. All analog circuits get some noise, and all analog circuits let sounds drop beneath that noise exactly like TPDF dither does.

That’s not to say it’s the only choice you can have for dithering: I’ll be offering up different ways to dither for weeks, each with their own interesting sound signature. I’m just saying, for what it is, TPDF dither works extremely well. If you don’t have good reasons to use something fancier, or you want something guaranteed to work on everything in any situation, TPDF dither’s the one for you. Airwindows TPDF dither is a nice high-resolution well-coded implementation, one that does the truncating for you so you can compare it (for instance, with BitShiftGain like in the video) but it’s also exactly the same as any other properly done TPDF dither out there. There’s no fancy tricks, it’s just the boring but useful TPDF dither.

I guess there are a few Airwindowsy things about it but they’re not sound quality related. If you’re using the AU on Macs, it’s ‘N to N’ meaning it works on quad and 5.1 channels automatically, and is more efficient on mono channels. And just like all the Airwindows dithers that are coming out, it is 24 bit only and has no controls. That means if you want 16 bit you could get the AU Ditherbox, wait for it to be ported to VST, or use two copies of BitShiftGain that I just released. (I’m discouraging emphasis on 16 bit because I think it’s obsolete and should be deprecated.) This also means if you’re using TPDFDither as intended, it’s a ‘non-fiddly’ plugin that won’t distract you. There’s no window, no GUI, no reason ever to open it in the DAW: if you’ve placed it in the correct spot you can see it there (clearly marked TPDFDither) and that’s all you need to know.

Making plugins that simple and self-effacing is a very ‘Patreon-supported‘ thing to do. When you have to sell plugins to stay alive as a company, you’ve got to keep them in your users’ faces and distract people to make them think about you, lest you be forgotten. This competes with the creative urge and gets in the way. Making plugins that are ruthlessly minimalistic to the point of being almost not there, is the opposite. Your music has to be the focus, so the plugin has to have the goods sonically but also be non-fiddly, because it’s sort of ugly and boring and not fun to play with.

I continue to delight in the latter. Let your music be the focus. Hope you enjoy TPDF Dither, and expect a lot more plugins of this nature, as fast as I can reasonably release them :)

This got a Redux edition, meaning some added controls. Not only 16/24 bit TPDF with a DeRez control (and a clamp for how loud it gets so it doesn’t blow up your ears at super low bit depths), it’s also the Airwindows TPDF algorithm. Which is to say it’s not exactly like everyone else’s TPDF algorithm, even though it adds exactly two noise sources each one bit in loudness.

That’s because when I made it, I added one and then subtracted the other and thought that gave me zero. But of course, it doesn’t… it gives me TPDF (triangular probability density function, or ‘the correct kind of dither when done by-the-book’ which decorrelates two moments of quantization noise blah blah blah technical :) )

But it also gives exactly half a bit, on average, of DC offset. This is enough to make measurements weird. It’s not enough to do any harm to anything (less than a least significant bit: it’s literally in the noise floor). But it is enough to have the noise floor sit across THREE bit values instead of only two. And that is enough to make it sound nice. (it’s possible there are other values, like 0.382… that would sound better still, but I’ve not done that experiment yet, and it’d be more complicated to implement… guess I know what I’ll be doing NEXT week)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

TPDFDither processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/TPDFDither)

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
