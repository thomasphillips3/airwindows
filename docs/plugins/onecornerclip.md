# OneCornerClip

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Clipping |
| **Type** | Clipping |
| **Status** | Latest Release |

## Description

an ultimate full-bandwidth clipper

## Detailed Overview

OneCornerClip works like this: it’s like ADClip, except it spreads out the onset to clipping over possibly many samples. They converge upon the maximum possible output, which means the front edge of a clip takes on a continuous curve, moving its energy down into lower frequencies where the clippage is less bright and gritty, and more brutal and ballsy.

Then, on departing the clip, the waveform just snaps instantly to the next unclipped value, with no attempt to soften: so your waveshaping ends up getting one corner (on departing the clip) and one rounded onset (entering the clip).

What this means is, you can smash this with bass and it’ll remain bassy. Smash it with midrange and it’ll be middy. It shapes itself to the needs of your track, the distortion taking on the character of what you’re putting in. And that means, you can slam stuff absurdly hard through this while retaining character… and you can retain size and scale and depth.

I didn’t really design it for 2-buss mastering duties though I’m sure it’ll find some use there. It’s more a technical experiment that came to life and ate Tokyo. I think it’ll do great for nasty industrial noise, for obliterating drum room tracks, just a whole bunch of uses: because this isn’t a special purpose effect. It’s a big fat dirty distortion, and that makes it more flexible than bright gritty distortions, in that it can wear your frequency balance like a mask. It IS still distortion, so you won’t be using it for clean things. But it’s also very good at soaking up brief clips without revealing itself, so it’s not an insane choice for subtler use. I keep it at 0.618 for general use: that gets a good range of tones.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

OneCornerClip controls peaks and maximizes loudness through peak limiting. Use it as a mastering tool or creative effect.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Clipping](../categories/clipping.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/OneCornerClip)

**Categories**: Clipping

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Clipping](../categories/clipping.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
