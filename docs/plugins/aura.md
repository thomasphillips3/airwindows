# Aura

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

a new kind of resonant lowpass EQ

## Detailed Overview

So this turned out to be a bear to bring up to date, because the original code was insane. I’m not quite sure how I got there, and I was still bugfixing long after the demo video was made. You’ll find the actual version of Aura has a slightly wider range, better adjustability in the low range, and the Dry/Wet control gets a touch of added functionality: as you go full wet, the resonant quality gets enhanced, so be sure and explore the half-wet or barely-wet settings. If it’s too scary-resonant, just pull it back a teeny bit and it should cooperate.

And this one is a bit scary as it seems to be channeling analog filters. I agree that it would be great to have this principle work as a full-range, synth-style filter that goes all the way into the bass. I can’t do it, though: it freaks out when I try, and it took endless hacking just to expand it a bit from what you see in the video. This is the algorithm derived from GrooveWear, which averages the rate of change OF the rate of change of the waveform. It’s not even slightly normal. You get what you get.

But what you get, is a lowpass with a striking resonant edge that’s implemented in a totally new way, and which has no pre-ring at all… and the way it gets its sound gives it an extraordinary sonority. Pretty much anything in audio that you’d want to project loudly as if from an acoustic space, can be given a sheen and glisten and sonority with Aura. I’ve got it extending down fairly low into the midrange if you’re at 44.1K or so: that should help if you need to use it at high sample rates, because the technique for doing it is not exactly cooperative and I found no way to simply tune it down: everything’s so geared to slew rate between samples that it’s best used for treble effects. I think it’s got a useful tonality for its treble manipulations, and I’ve spent a lot of time coming up with interesting ways to cut or enhance treble. This one’s good at what it does. You can really do stuff with the texture of your mix by aggressively using Aura on suitable elements.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Aura processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Aura)

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
