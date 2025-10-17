# CrunchyGrooveWear

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Lo-Fi |
| **Type** | Lo-Fi |
| **Status** | Latest Release |

## Description

a version of GrooveWear for more edge and distortion

## Detailed Overview

GrooveWear began as a feature on ToVinyl. It defaulted to ‘on a tiny bit’ and gave a slight treble lift and sculpting of the highs, following its working principle: averaging/smoothing the rate of change of the signal, something that’s not normally present in audio processing. This would cause the output to try and ‘keep going’ at the speed it was moving, like a phono cartridge needle that had weight and inertia.

The thing is, it was also implemented with a bug (or possibly just an unwitting choice). It’d overshoot, and bring on a kind of treble zing that was distorted and didn’t always work for everybody. When I split this feature out into a dedicated plugin, GrooveWear, I found out through trying to incorporate a dry/wet control that I could apply half the effect and then the ‘groove wear’ wouldn’t overshoot. And it produced a treble-eroding plugin with a different operating principle than normal EQs, with the same ‘glue’ effect but none of the tizz or distortion. And that’s GrooveWear, and I considered it a good bugfix and came up with a way to run the dry/wet control in four stages so you could have the new ‘glue’ over an even wider frequency range, from a ‘purest’ one stage to twice the intensity of the original thing in ToVinyl. I still see that as the ‘groove wear’ to have, for realistically getting a ‘vinyl warmth’ effect, and I stand by that version.

And yet… some folks missed the zing. So, this is for them.

I’ve experimented and I think this is the optimal algorithm for doing that original ‘energy boost’ up top, except now you can apply it, too, at a wider range, and you can also get up to four stages of the effect. Adjusting the dry/wet will dial in a wide range of tones because of the way the effect kicks in (halfway engaged stages give that treble-eroded quality, so the effect is most striking at 0.25, 0.5, 0.75, and 1.0). And if you fully crank it out, you can get a really intense sort of treble hype that’s not like traditional EQs. It’s more exciter-like, and has no pre-echo even though it seems like it’s a very high Q filter with lots of resonance. It’s crunchy and adds zing and character and if you’re actually seeking fake zip of an interesting color, CrunchyGrooveWear has lots of potential. Remember, if you’re looking for the most extreme crunch, use 0.25, 0.5, 0.75 or 1.0 as intermediate settings actively take highs away again (GrooveWear functions linearly so it doesn’t have this behavior). But you’ve got the full range of adjustments, because sometimes it’s nice to let a plugin into the wild that’s extremely weird and untame. This one’s born to be a secret weapon because it’s strange and unpredictable.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

CrunchyGrooveWear processes audio in the Lo-Fi category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Lo-Fi](../categories/lo-fi.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/CrunchyGrooveWear)

**Categories**: Lo-Fi

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Lo-Fi](../categories/lo-fi.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
