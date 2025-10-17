# kCosmos

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Latest Release |

## Description

infinite space ambient, or titanic hall

## Detailed Overview

It's not the first time I've tried to make a space ambient type reverb, but there are a number of firsts here nevertheless.

kCosmos uses the 5x5 Householder matrix design I've used in recent reverbs like kGuitarHall, but rather than just finding a new arrangement of delays, it's riding a wave of new developments in reverb development. Rather than taking days to evaluate ten or a hundred thousand possible reverbs before critical listening, I revamped the program I was using, to hundreds of MILLIONS per night. Since the method is not unlike the genetic algorithm in that it's trying variations against fitness functions, this wildly improved tone quality.

I went from evaluating recurring delay lengths based on where they were in the reverb tail, to mapping out spacings between echo returns, and evaluating the distribution of these spacings. This changed the whole texture of the reverbs from 'artifical' to more of a natural, invisible spaciousness that blends in better.

And I went from running an extra 3x3 matrix just for early reflections, to running no early reflections at all, to running a whole other parallel unfiltered 5x5 matrix… JUST for early reflections. That's the EarlyRF slider, which can be used in conjuction with Dry/Wet, predelay, and the Filter control, to help transition from the raw sounds to the deep reverb space.

I've added an FIR brickwall filter for the main regenerating section (though not inside the regeneration) and worked out my own sinc interpolation, and have a plugin coming along those lines, and used it for the regenerating filter section. I've included a simple averaging for non-full-crank settings of this filter, so kCosmos can switch on the fly between extended highs at infinite sustain, and a maximal-depth version that gradually loses highs in a way that sounds like distance.

And I've refined the concept of 'gradually restraining the infinite sustain when new audio is coming in', so that in normal use as an infinite verb, you can layer stuff all day without the reverb running away with you. It's so effective that subtle noises can have a slight feedback bias: when you start with very quiet layers, they will creep up in volume to about -18 dB total, at which point they'll balance. So it's an infinite reverb specifically designed for live performace as an ambient musician doing deep space explorations, and it'll adapt to the way you play audio into it.

And lastly it has both CreamCoat style undersampling, and CrunchCoat style, at the same time. Meaning, set to full crank it uses the CreamCoat method for applying Bezier undersampling without artifacts, and as soon as you go away from Derez of 1.0, it switches to the continuous adjustment range of CrunchCoat, sometimes described as 'cursed digital derezzing'. Except this time, the Derez control is control-smoothed, and use of the filter tends to mask the 'cursed' quality completely. It's just that the giant reverbing space can be cleanly pitched up and down as you go, or dropped to an eerie rumble and murmur.

There will be further experiments, but kCosmos stakes out a position as the most epic (and playable) Airwindows reverb. I hope you like it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Early Reflections]
    A --> C[Diffusion]
    C --> D[Feedback]
    D --> C
    B --> E[Mix]
    C --> E
    A --> E
    E --> F[Output]
    style C fill:#6366f1
    style D fill:#8b5cf6
```

## How It Works

kCosmos creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/kCosmos)

**Categories**: Reverb

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Reverb](../categories/reverb.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
