# MSFlipTimer

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

a utility that swaps stereo with mono every few (1-10) minutes

## Detailed Overview

Here's a request I got, a variation on one that's in the utility category. While I ramp up to more interesting stuff I can do some of the background work while putting out the thing that someone asked me to make :)

Every few minutes (as in, one minute to ten minutes) MSFlipTimer switches from stereo to mono. It does this in about a tenth of a second, to prevent any sort of pop or anything. When it’s in stereo it is 100% direct pass-through of the audio data word, so this is as clean as stuff like LeftToMono: it’s one of those ones that just copies the data over, not even touching it. That said, this doesn’t belong in your mix: the idea is that if you’re mixing and you tend to screw up the mono mix by doing too much crazy stuff with stereo, this'll repeatedly force you to grapple with it in its mono form.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

MSFlipTimer processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/MSFlipTimer)

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
