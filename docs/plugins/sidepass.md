# Sidepass

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

a simple utility plugin, a highpass on the side channel. Mono-maker

## Detailed Overview

This one was by request. It’s not very fancy, but I hope it’ll come in handy. If it is, spread the word!

I’ve got a plugin called ToVinyl, which is rather fancy. It’s the Airwindows attempt at a vinyl mastering suite: elliptical EQ, highpass on the mid to help get levels, an acceleration limiter to tame sudden energy spikes without really cutting brightness otherwise, and even a groove wear modeler that was the precursor to Airwindows Aura. That’s one of the Kagi for-pay plugins, number 9 on the list when I reach $800 a month and begin doing those.

But, I got asked for something much simpler. A highpass filter on just the side channel, and one that would go up the full range from subs to highs, so at full crank it’d be purely mono.

Well, I’ve altered that a teeny bit: Sidepass is aware of sample rates, so if you’re at a 0.1 setting at 44.1K, it ought to be doing the same thing at 0.1 at 96K. But apart from that, here’s a little utility for AU, Mac and PC VST that just highpasses the side, from DC to 22K. It’s an Airwindows filter, same as what’s in Density and Drive as a highpass, and it ought to do nicely.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Sidepass processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Sidepass)

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
