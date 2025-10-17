# Srsly3

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

Srsly2, with a Nonlin control to analogify the filters

## Detailed Overview

Those who are familiar with Airwindows know that Srsly is a sort of take on a famous stereo processor, the Hughes SRS. The first version, Srsly, uses a bank of very tight resonant filters to adjust space psychoacoustically and simulate the sound of ambience around human ears (based on illustrations that ran in Popular Mechanics). The second, Srsly2, took that and added aggressive mid/side processing to more closely resemble existing SRS boxes, thanks to a Crate SRS box I was able to get by way of example.

Srsly3 is the same thing as Srsly2, except all those filters are replaced with the kinds of biquad filter found in Airwindows BiquadNonlin. That's the one where I figured out how to apply the filter modulating used in Capacitor2, which simulates nonlinearity in cutoff frequency of ceramic capacitors (specifically Murata capacitors made of barium titanate), but applied to biquad filters which are a lot more adaptable than Capacitor was.

You don't have to understand any of that, it's just the way I got to this result.

It means you get a Nonlin control, where setting it to 0 means you have Srsly2 again. And then when you turn it up, especially when you have your filters at a higher Q setting (sharper resonances), the filters get modulated by the voltage pressures they themselves see from the signal passing through. And it fuzzes them out in a way that makes Srsly3 sound more analog than it's ever sounded before, with more of a vibe and texture to the vivid stereo sounds it can make.

I would say play with it and see what kinds of settings sound good to you. And if you liked Srsly2 and found it useful, now you've got this which starts where Srsly2 left off, and then takes it to new places. BiquadNonLin really sounds most interesting on tight resonant peaks, which is what Srsly is made out of, so with a bit of luck this will really click for Srsly enjoyers. Hope you like it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Srsly3 processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Srsly3)

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
