# Fracture2

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

a wavefolder that allows more extreme disruption

## Detailed Overview

Fracture2 is straight up a West Coast wavefolder, in a plugin. You've got Drive, Fracture, Threshold, Output and Dry/Wet controls. Drive is basically overdrive like in Mackity, and you can get unity gain at a setting of 0.1, and Output and Dry/Wet are what you'd expect.

Fracture makes the signal go exponential before folding. What this means is, if it's at zero you'll get a simple wavefold. With a sine, that'll create a distinct overtone (stronger than the original Fracture) which will slow down as it nears the top, then reverse. As you increase Fracture, the pitch of the wavefold increases because the wave you feed in will start folding faster and faster the more it folds: it will also open up the unfolded part of the wave, making it more dynamic. On non-tonal sounds, this makes the effect dryer and punchier and more aggressive.

Threshold is by request from a fan who asked in Youtube comments, and whom I've got some things in common with. The idea is basically, can you make the folding part only take up a certain amount of space, like back to the zero point but not past? Turns out you can! And what this does is, it lets you have a volume control on the fold part. So, at zero threshold, you have a soft clip (or, with Fracture, a weird expando-clip like High Impact). As you increase it, the wavefold comes out of the clipping, expanding down (or up) from the flat-top of the wave, with 0.5 going to the center of the waveform and 1.0 doing a full-amplitude wavefold.

Because this effect lends itself to the Rack port of my plugins (where you can feed audio rates into any controls), all the controls except Fracture are smoothed for better automation. I don't do this all the time, but it just seems to be the kind of effect where you might be sending sine waves into it (revealing zipper noises) and then modulating it like crazy, so it's using the same smoothing that's in the Z2-series filters.

Hope you like it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Fracture2 processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Fracture2)

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
