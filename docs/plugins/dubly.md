# Dubly



## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Stable |

## Description

a retro vibe and atmosphere maker

## Detailed Overview

Some people will recognize this instantly… even if you don't do heavy metal in Dubly, you know :)

Here's what this is. There's a famous sort of noise reduction, with variations, that's based around the idea of taking the audio, filtering it, compressing it 2:1 and adding that TO the signal. You then record that to tape. And when you play it back, you take that combination, compress it and filter it AGAIN, but this time subtract it from the signal. And hey presto, perfect sound!

Well… nope. Doesn't add up. Changes the sound. The thing is… that changed sound is sort of magical.

How come? For starters, when you distort tape you get harmonics. If you do that to the sound you start getting harmonics a lot sooner, over a broader range of sounds… but then you're taking the added harmonics you just made, and you're subtracting them again. You're turning them down. You're making the dynamics of your sound come with dynamically varying harmonics, a real color adder, but without the dynamic squashing of just plain saturating. And that's not even getting into when you've got the machines misaligned… or tuned by ear to bring out a particular magical sparkliness and ambience that's NOT really accurate, but maybe is the special sauce for a particular studio's recording machines… we may never know, we know only that these old noise reduction things were fiddly beasts…

So what if you strip all that down, Airwindows-style, to only the basic principle?

Meet Dubly. It uses uLaw technology (really!) for good, not evil! It does the most general form of that processing, NOT like any specific very proprietary tech, and uses a simple distortion inside rather than any tricky tape emulation (that can come later!). It defaults to 0.5, where it will just bring a delicate aura of retro magic to the sound. But, the way it's calibrated (very tricky, by nature) you can crank it out and mis-calibrate it. And when you do, you'll get more and more into a crazy, hyped, intensified zone that adds a lot of treble energy. But this doesn't make it into a 'single ended' version of the processing (even though that's a known secret weapon). It remains the double-ended, full chain, noise-reducing system (that is, if the single distortion stage was adding noise, which it isn't). Just… twisted.

There will obviously be more of this, but for now, you can do your heavy metal in Dubly, you know. It will get a little lighter and spacier and more atmospheric, which is probably why this is Not Done. But who knows, maybe you'll like a little Dubly on your record. Hope you like it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Dubly processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Dubly)

**Categories**: Effects

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Effects](../categories/effects.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
