# PurestGain

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

a high-res noise shaped gain, with smoothed fader

## Detailed Overview

Marking the 200th plugin in Airwindows’ ‘AU’ category (not perfectly accurate, but yay anyhow) is PurestGain, in VST-enabled form!

What’s to explain? It’s a gain utility. :D

No, seriously, that’s what it is. Here’s why some folks are a fan of this plugin anyway, even though every DAW has this as a utility plugin, plus the DAW faders built in.

Firstly, gain is processing. When you apply even a simple gain change, it expands the word length of your digital audio out to arbitrary size. PurestGain comes from a set of plugins I did to experiment with the extremes of digital audio accuracy. You might think digital audio is automatically accurate, but that’s far from the truth. We hear degradation in the resolution domain as flatness, cardboardy-ness, and it’s cumulative. I don’t think anybody can hear the difference between PurestGain and a DAW utility gain plugin, when just a single plugin is in the signal path… but it’s cumulative.

Also, you can’t be sure that a gain plugin is truly minimalist. If a plugin takes in floating-point audio of great quietness, and multiplies it by 1.0… that’s a math operation that can force the result into the same floating-point ‘level of resolution’ as the 1.0. Floating-point is treacherous, and the damage done is still very subtle but again is cumulative.

PurestGain takes the input audio and does the gain processing at ‘long double’ resolution. It then noise shapes the result back into the DAW audio buss, whether that’s a 32 bit buss for normal VST and AU, or a double-precision 64 bit VST buss, if available. The result is an ultra-high-precision gain plugin that refuses to lose any audio quality. It’s the plugin equivalent of using switched attenuators with precision resistors in a mastering console, rather than potentiometers.

There’s one more trick PurestGain has up its sleeve: a second control especially for fades. The trouble with DAW faders is that they must serve two masters: they’ve got to adjust smoothly and avoid zipper noise (crackling while you move the control, most clearly audible if you get a low-frequency sine wave going and then manipulate the control) but they’ve also got to snap instantly to a position if asked. The second slider in PurestGain runs in series with the dB gain control, but it functions very differently. One way to resist zipper noise is to have the gain smoothly ramp between volume settings, and that second control is designed for human-performed gain rides. Map the fader on a control surface to it, do your active mixing, and PurestGain will smooth every fader motion until it’s as fluid as any real-world analog console: try it with sinewaves and see how flawless the result can be.

That’s a surprising amount to say about a gain plugin, but that’s Airwindows for you :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PurestGain processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PurestGain)

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
