# BiquadOneHalf



## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Stable |

## Description

an interleaved biquad filter like Biquad

## Detailed Overview

BiquadOneHalf is tech that’s going into my future plugins. You have to set the frequency twice as high as you would using Biquad, and it can only go up to 1/4 Nyquist, but the way it interacts with the sampling frequency is special and works very well for some types of filtering. You’ll be getting more developed plugins of that nature soon, and all through January, but for now I got this: working version of the new Biquad filter variation, that you can use on stuff.

It’s the first version, not the ‘sweepable’ version, because this is going to find its way into fixed-frequency EQs, ‘head bump’ etc… compare it to Biquad remembering to use twice the frequency you otherwise would. It’s happiest on bass or midrange: much like regular Biquad, trying to force it to get real close to its high frequency limit can get messy.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BiquadOneHalf processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BiquadOneHalf)

**Categories**: Biquads

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Biquads](../categories/biquads.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
