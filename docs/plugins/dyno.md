# Dyno

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Latest Release |

## Description

a lot like Mojo, but for intensity instead of loudness

## Detailed Overview

Dyno is similar in some ways to Mojo, but Dyno has a completely different character. Instead of loudenating, it ‘intensenates’. It’s a little bit like Remap in that way, but it’s not the same as Remap. You won’t get a volume boost out of it really, nor will it let you slam it for fatter peaks.

Instead, it brings fire and intensity to the audio and reshapes the waveform in a Mojo-like ‘evolution of Spiral’ way. Because it doesn’t take to slamming in the same way, it’s going to be a more subtle effect, but for those who got excited by Remap, this one deserves your attention.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Dyno processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Dyno)

**Categories**: Saturation

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Saturation](../categories/saturation.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
