# Channel9

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Tone Color |
| **Type** | Tone Color |
| **Status** | Latest Release |

## Description

Channel8 with ultrasonic filtering, and new Teac and Mackie 'low end' settings

## Detailed Overview

Channel9 retains everything it had—the two-stage drive control, the newly improved highpass, the slew clipping—the same calibrated Airwindows algorithms to not clone, but give you the general sense of various fancy name brand consoles in a cleaner, less ’emulated’ way which lets the music through…

But now, Channel9 has the same ultrasonic aliasing-filtering that’s come to Console and other recent Airwindows plugins. In a new way! Because Channel9 isn’t just sticking to ’20k’ as its definition of supersonic. Instead, Channel9 steepens its filter with a teeny resonant peak at this cutoff point… and then selects it in keeping with what the real console would be doing, if you had it! The Neve is the most extended, well beyond 20k. The SSL cuts off tighter, gives more audible sparkle (due to the additional gain stages in a really huge SSL desk, the cutoff will be steeper over the entire desk). API is between the two. The lift at the peak comes before the saturation stage, for better smoothness when the console is being driven.

And then I went and added two MUCH more affordable ‘models’, with their own usefulness.

The new settings are ‘Teac’ and ‘Mackie’. That’s right, old school house/techno classic basement mixers! The Teac, I was able to reference recordings of a real unit. I didn’t get it perfect as the real board had a noticeable high-mids peak that doesn’t belong in Channel, but it’s the correct kind of dark and vibey. And the Mackie’s my take on what you get out of the classic vintage 1202: A hair leaner than the Teac, but brighter. They both grind a bit harder than any of the big expensive desks, they both have slightly more exaggerated reshaping of the deep bass (using the Capacitor2 algorithm, like the others), they both control the brightest highs much like you’d get in a classic old low end mixer. It’s two new settings that follow entirely different rules than the big guns, for folks who know how to use an actual mixer much like metal guitarists use a Tube Screamer.

You can still have your fancy desk models (only better: the ultrasonic filtering brings just the right additional distinction to the models) but now you can go cheap and get the tone and vibe of some house music warhorses. The sonic reshaping these low end models do is just the ticket for sculpting relentlessly synthetic sounds into an appealing result. And since it’s Channel… it won’t have the noise of the real ones, it won’t have weird extra colorations, it’ll honor more of your real mix as it reshapes it: sort of best of both worlds! You can always add funky colorations or noise to your digital mix, but you can’t remove that stuff from the real mixers. Channel9 will shape your sound in ‘classic’ ways but along Airwindows lines: getting out of the way so your sound is interfered with as little as possible.

Channel9 can be used anywhere you like. If you’re doing a Console mix, I’d put it after ConsoleBuss. If you’re not doing a Console mix, you can literally do anything you want with it: it’s a subtle distortion/fattener combined with a set of careful tone shaping algorithms. Hope you like it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Channel9 processes audio in the Tone Color category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tone Color](../categories/tone-color.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Channel9)

**Categories**: Tone Color

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Tone Color](../categories/tone-color.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
