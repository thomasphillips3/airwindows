# Wider

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

Airwindows stereo space shaping

## Detailed Overview

Here’s a nice little building block. It’s stereo-only for obvious reasons (in AU, you won’t see it available on mono tracks): it’s a stereo space adjuster.

It works like this: you’ve got mid and side channels, but taken up several notches. Instead of being adjusted by level controls, the sliders use the Density algorithm. That means if you’re boosting, they get fattened up, and if you cut, they retain some of the edge and definition. This technique from Density has a way of moving audio’s position in space: boost comes forward, and cut moves backward. It turns out that’s perfect for manipulating the shape of a stereo space.

But that’s not all: as a final space-manipulating technique, Wider applies an itty-bitty time delay and interpolation (it can be as small as sub-sample) to whichever is the least forward, mid or side. That causes a delicate roll-off and sits the relevant part just a tiny bit back, spatially… and then the audio’s recombined into stereo again. It’s a bold thing to try, but it’s done very subtly so you wouldn’t know it was happening except I’ve just told you, so my secret is out :)

The result is this: you can kinda-sorta use Wider to produce extreme stereo effects (look for StereoFX, coming soon, as a better way to get aggressive with space) but it really comes into its own when used to redesign stereo soundfields. With tiny, small adjustments, you can get hugely effective results that sound totally natural. This is the mastering-grade one, where you can transform the source in a convincing and musical way, and not lose anything in the process. The effectiveness and transparency, especially when used for tiny corrections, will make this a go-to plugin for real stereo work.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Wider processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Wider)

**Categories**: Stereo

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Stereo](../categories/stereo.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
