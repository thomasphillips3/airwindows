# BiquadDouble



## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Stable |

## Description

a handy Airwindows cascaded biquad filter: steeper roll-off before resonance

## Detailed Overview

So it’s a boring old biquad.

Except, if you’re into the details of how stuff works, it’s not THAT boring. It’s two biquad filters stacked, which means you can get twice as much cutoff steepness before resonance. Since it’s Airwindows, you can have any possible resonance setting anyway, from ‘impossibly high’ to so wide that it’s basically full bandwidth. That interacts interestingly with the stacked filters: some of the weird effects with super-wide filters will act different here. On top of that, it’s two stacked filters inside an internal Console mixing system: so the tone of the filter itself is ‘expanded’ in a way not common to boring old biquad filters. And it’s the most efficient (but least cooperative) biquad, meaning that it runs and sounds great but doesn’t always cooperate with rapid automation, so that might get interesting if you’re not careful.

Why do this at all?

Because I sometimes like mocking up effects and plugins out of component parts. And if I was to use a stacked biquad filter as part of something else, it’s just more convenient to dial in the correct settings and get the tone exactly right: I could use two ‘Biquad’ instances, but remember that BiquadDouble stacks its filters INSIDE the Console processing, so it might not be as good to fake it, plus I’d have to set both the Biquad instances the same…

The real answer is ‘because that’s how I roll’. Nobody asked for this. But maybe you reach for a biquad filter for simple tone shaping, and you keep trying to find a butter zone between too shallow, and too resonant. This might become your go-to basic filter. I can’t predict what will take off: for all I know, this is THE basic digital filter everyone’s been waiting for, the one that just sounds right for every purpose. Or not. But you can’t know until you try :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BiquadDouble processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BiquadDouble)

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
