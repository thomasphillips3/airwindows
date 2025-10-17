# SampleUndelay

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

the original AU SampleDelay that declares lots of latency to do 'negative delay'

## Detailed Overview

By request, here's something from the retro bin, brought up to date as well as I could :)

The original SampleDelay offered millisecond, sample and subsample delays, but it also offered negative delay. The thing is, it did that through declaring a bunch of latency and then delaying to match it. There's a couple problems with that. Firstly, it kills your ability to track into the mixing system: everything gets the maximum added latency, and then more delay to get to whatever the target delay time is. So you're always getting thousands of samples delay no matter what: it's only OK for mixing. Even recording automation that will interfere with you being able to interact with the mix.

Secondly, I've had trouble making it work reliably with different programs. Generally at 44.1k it does what it means to do. I've seen 96k recordings mysteriously try to use 88.1k for a latency, throwing off the calibration of the ms control. Never mind trying to do a VST port: I've not seen documentation on how that's meant to be done though I understand the JUCE folks try to make it work, yet even they seem to sometimes run into incompatibilities. I'm running into incompatibilities even just on Audio Unit. For the time being I am not liking the results of trying to declare latency, even just on AU where it's part of the basic plugin format.

But I was asked to bring this back anyhow… so here it is, as-is. It's January and I'm mostly trying to get other stuff up to speed, such as the reverbs: in my video I asked whether people are interested in a 'redux' of kCathedral, because I'm interested in revising it to address criticisms (I'd keep the original one available, but replace it with a newer version) and to take advantage of a lot of woodshedding I've been doing on the subject of reverbs.

I've got a lot of things coming out in February, I just wanted to drop a thing or two that are not as big as full plugin releases, or things like this where there's a couple people who want it, and limited scope for it. For VST users (of which I'm one, on Mac Reaper, because it runs a 64-bit buss) or indeed anybody, I'd also recommend just sliding the track earlier in the DAW, and then if you want a plugin, finetune it with the regular SampleDelay which will do exactly the same thing in the end, except you can track into it because you're running a zero latency system (outside of whatever your DAW and converters impose).

For those of you that asked for exactly this, hope it will do :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

SampleUndelay processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/SampleUndelay)

**Categories**: Utility

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Utility](../categories/utility.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
