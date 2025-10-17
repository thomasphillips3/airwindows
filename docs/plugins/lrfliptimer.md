# LRFlipTimer

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

a utility that swaps Left with Right every few (1-10) minutes

## Detailed Overview

I don’t know how useful this’ll be for you: a person asked me for it, and I was able to do it. This just does one thing.

Every few minutes (as in, one minute to ten minutes) it swaps the L and R channels. It sweeps them across in about a tenth of a second, to prevent any sort of pop or anything. When it’s in LR or RL mode, it is 100% direct pass-through of the audio data word, so this is as clean as stuff like LeftToMono: it’s one of those ones that just copies the data over, not even touching it. That said, this doesn’t belong in your mix: the idea is that if you’re mixing and you do stuff asymmetrically, it’s like visual arts: you might need to flip the canvas left-to-right to see if things are off balance. That’s all this plugin does. You set how many minutes will elapse before it flips or re-flips.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

LRFlipTimer processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/LRFlipTimer)

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
