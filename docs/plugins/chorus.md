# Chorus

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Ambience |
| **Type** | Ambience |
| **Status** | Latest Release |

## Description

a mono chorus, also works as a vibrato

## Detailed Overview

Here’s the start of some modulation plugins: Chorus will give you a nice basic mono chorusing effect, sweeping one moving delay tap against the dry signal. What makes it unusual is a pile of odd Airwindows things to adjust it this way and that.

The sweep is done with a peculiar Airwindows interpolation which both applies a bit of an averaging function, and also a subtle lift to highs to compensate for that. The idea is to have the moving part be totally fluid, analog-like, even though it’s digital.

To drive that, there’s a treble boost going into this smoothing delay tap, and it’s based on the Airwindows Energy algorithms: that means this plugin interacts with the raw sample rate in two different ways. It’s designed to make it so, whatever the sample rate, the sounds project through to the most extreme highs without edge or dullness. That means Chorus won’t sound exactly the same at 44.1K, 96K and so on: it will try to deliver the most finely tuned treble for each sample rate, whatever that is, and the tonality might be different. Also, since it’s running a delay buffer, it’s giving you full use of the buffer at all times: the broader settings might be more useful at high sample rates.

In general, this should be pretty approachable. Hope you like the tone: there’s more where that came from.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Chorus processes audio in the Ambience category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Ambience](../categories/ambience.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Chorus)

**Categories**: Ambience

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Ambience](../categories/ambience.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
