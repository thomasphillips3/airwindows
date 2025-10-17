# Zoom

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Distortion |
| **Type** | Distortion |
| **Status** | Latest Release |

## Description

a bank of Density-like waveshapers for subtly modulating peak energy

## Detailed Overview

This is a little piece of what could become a new Mastering plugin, but I've got a lot of testing to do to work out whether that should happen. Zoom is waveshapers: as many as five stacked up for high gain levels, and most settings will use at least a couple. They're applied sort of in parallel: the basic idea is a lot like Density, but handled very differently.

The purpose is to try and alter, very strongly, the peak energy and only the peak energy of the sound, while leaving the loudness more or less alone. That's why the 'negative' settings, below 0.5, don't get as much quieter as those in Density. It's taking the hottest peaks and further boosting them while cutting back quieter stuff. Boosts still work as in Density, except the character will be a little different.

So, you might find the sounds of this interesting, or find that it's an amazing overdrive or 'weird expander', or whatever, but those are all obvious changes that you can hear because they're modifying the RMS loudness of the signal. And that's fine too. I'm just saying, for the last month I've been on a deep dive into Meter and the concepts around it, and I'm working towards something specific. I would like to see whether you can take an already good track and make it significantly better by heavily modifying just the PEAK energy and getting that exactly the way I want it. A new version of Meter is coming out and I'll be doing more 'vinyl hit record videos' to demonstrate what I'm talking about, and to do that I have to write new plugins that specifically master audio to work with Meter and work on the stuff I 'can't hear'… at least, not directly. If I'm right, perfecting this stuff will cause tracks to sound inexplicably amazing (and they will have to start out with the potential for amazing: some don't need help, and for others it's very obvious what must happen.)

For instance, I might have various 80s hit records where, due to the taste in mixing and mastering, there's constantly stray peaks 6 to 12 dB hotter than everything else, and I'd need to remap them to be a more continuous range of peak energy. Or, the area is too dense and could use being opened up subtly, allowing the hottest peaks to 'un-saturate' slightly without it being really audible, again to get me an area of peak energy that's as evenly distributed as possible.

And that's what Zoom was coded to do, and why it's hard to hear what it's doing until you crank it up to the point of obviousness. It is also a simple waveshaper so you can do that while oversampling it in the DAW, which of course I won't be doing because used normally it'll barely create any harmonics at all. It's a 'zoom lens' for audio: everything is still in focus and looks the same, but the presentation has shifted in the desired direction, probably only discernable by Meter.

I might still be working on Meter and far from ready to put out a Mastering that's entirely based on my untested theories, but the new Meter should be coming up just next week, and if you wanted to experiment as I am experimenting (or just slam stuff, I'm not your Mom) then here is Zoom. Have fun!

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

Zoom adds harmonics and edge through distortion. Use it for adding grit, warmth, or aggressive processing.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Distortion](../categories/distortion.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Zoom)

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
