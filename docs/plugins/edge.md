# Edge

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Distortion |
| **Type** | Distortion |
| **Status** | Latest Release |

## Description

a seven-stage distortion with Hypersonic filtering and tone shaping controls

## Detailed Overview

With all the talk I’ve done about Hypersonic (composite filtering making very steep Butterworth slopes from sets of biquads), one must ask: what if you just made a distortion out of it?

This is Edge. It’s seven stages of hard clipping with Hypersonic-style filtering between each one. It’s real bright and has silly high gain, and it’s going to become real useful.

That’s because it’s one piece in the DI Guitar system I’m devising: a set of plugins that combine my style of aliasing reduction (using biquads, so zero latency) with guitar-grade distortion and a reissue of a classic old plugin of mine that’s totally revitalized for the modern day, Cabs. (it can also be run into the Airwindows amp sims, of course)

Suffice to say Edge is the high-gain distortion stage of such a system. It should run pretty efficiently, and it’s got a carefully designed set of controls. The gain of course is obvious.

Lowpass is basically your cutoff frequency: this isn’t designed to be swept (though you could if you’re OK with some crackles) but is a very efficient Hypersonic-style lowpass that you can set from 25k right down into the deep bass. Since it doubles as the ultrasonic filter, dialing back on the extreme highs will give you even better aliasing performance (run at elevated sample rates to use this properly) and also gives you an interesting tonality at the cutoff which isn’t exactly resonance, but it’s a bit like it. The way the phase shifts going into successive stages of gain boost and clipping produces a distinctive tone.

Highpass is your secret weapon for when you use it as a guitar amp: get the rest of the system huge and beefy, and then dial in the lows using this input highpass, for maximum texture.

Output and Dry/Wet are for use when you’re just making it be a hard clipper. It’s never going to be exactly a hard clip because of all the stages and the way the EQ interacts with the sound, but between the highpass, lowpass and the gain on tap you’ll get many sounds out of this one. Unlike stuff like ‘Tube’ this is never intended to be smooth. It’s just edgy in a distinctive way that might come in handy.

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

Edge adds harmonics and edge through distortion. Use it for adding grit, warmth, or aggressive processing.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Distortion](../categories/distortion.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Edge)

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
