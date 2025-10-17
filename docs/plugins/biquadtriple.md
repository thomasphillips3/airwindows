# BiquadTriple



## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Stable |

## Description

a handy Airwindows cascaded biquad filter: steeper roll-off before resonance

## Detailed Overview

Here’s another utility plugin! This is the same as BiquadDouble, except it’s three stacked biquads. Otherwise the same: you get to set the frequency, Q etc. for all the filters in parallel. This saves time over doing three instances of Biquad, plus they’re run in series inside Console inside the plugin, so there will be a deeper tone out of this one.

It’s for if you wanted to get steeper filter slopes without the cutoff going resonant. This, like BiquadDouble, is very much ‘tools to make tools’, for if you’re mocking up some kind of effect and know you’re going to be using filters. You can test out what you’ll use in your effect, this way. Note: seems like the inv/dry/wet is really just wet/dry/wet, and I have too many new and more worthwhile plugins to put out to fuss over it so I’d advise just taking BiquadTriple as it is. I’d be using it as full-wet anyway though you can bleed in dry for more of a shelf effect if you’re doing a steep rolloff of some kind.

I expect to be doing some more variations on this as there are known ways to stack filters where the Q factors are very specific and staggered: however, those will be more aimed at the mixer/end user, and probably will be called isolators (that being a common term for this type of steep crossover-like filter). And again, I’ve got other things to put out that are more interesting, so more will be revealed as I do those experiments. I think an Airwindows isolator-style effect would be good. Bear in mind the biquads can be fussy about extreme settings and moving the sliders abruptly.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BiquadTriple processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BiquadTriple)

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
