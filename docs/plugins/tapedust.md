# TapeDust

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Noise |
| **Type** | Noise |
| **Status** | Latest Release |

## Description

just a special treble-erode noise, a ‘slew noise’ plugin

## Detailed Overview

Sometimes it’s good to have just a little specialty plugin that does a useful thing. Hard to do that in the commercial plugin biz, where everything has to be the biggest hype to date: but hey! Thanks to Patreon I’m free of all that, and can follow my vision.

It helps that I put out a lot of plugins: it’d be weird to do this as my only plugin for the month. But, while I work on Desk4 and StarChild from the greatest-hits list, I thought I’d sprinkle a little TapeDust for you.

This is slightly different from the tape noise in Iron Oxide, though it’s the same general principle. It is a slew noise plugin. What that means is, the noise ONLY hits high frequencies or anywhere the signal’s moving rapidly (there’s a teeny bit of other noise added at high settings, but it’s mostly that).

Note the ‘or anywhere the signal’s moving rapidly’. This isn’t a crossover. If you put in a sine wave that’s low and loud, you’ll get very obvious noise only as it crosses through zero, and that’ll sound odd. In general, cranking this up is weird. It’ll depend hugely on what kind of signal you’ve got… but that’s the beauty of it if you can master where to use this plugin.

Basses? Probably no way. Full mix? Getouttahere, no chance outside very low settings. Guitar? Hmmm. Drums, loops? A pattern emerges.

TapeDust can convert ugly sharp treble attacks on pointy percussive atonal sounds to pretty much any degree of dense, noisy, natural-sounding crunch. It’s a type of noise, so it also gives analog-style variance to repeated samples that might sound over-digital. And the less tonal, or the less ‘pure clear note’ the signal is, the more TapeDust you can get away with. Since it’s a slew noise, it hits the treble of your signal HARD, but since it’s a noise, it’s not filtering or softening the sound as much as it’s just eroding it, weathering it, making it more natural. Anywhere you’ve got bright highs on a nonpure sound, you can grind them off with TapeDust.

Of course, if you’re cool with using super-low settings, you can do that anywhere: it’s just important to register that this very specialized and dedicated tool is super picky about what it likes to work on. It’s a beautiful example of taking your production skills deeper: use something that can sound horrible and wrong, and find places where it’s in its element. You can do outlandish textural things, taking something like a clean electro mix with deep clean bass, and sticking heavy TapeDust on just one element in the mix to contrast with the un-grungy elements. I hope you like TapeDust. It’s the kind of plugin I love to make.

(note: there has been a bug in this plugin causing it to sound different than intended)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

TapeDust processes audio in the Noise category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Noise](../categories/noise.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/TapeDust)

**Categories**: Noise

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Noise](../categories/noise.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
