# PurestWarm



## Quick Info

| | |
|---|---|
| **Category** | Subtlety |
| **Type** | Subtlety |
| **Status** | Stable |

## Description

a subtle tone shaper and warmth adder

## Detailed Overview

PurestWarm is a little bit like PurestDrive (anxiously awaited by quite a few people) but not quite as sophisticated… however, in its simplicity is part of its usefulness. It applies an Airwindows softest-possible-saturation effect (like what you can get out of Density, or Channel) but it’s polarized: you pick which side of the waveform the saturation applies to. For the other half of the waveform, it’ll pass through the exact bits that came in. So it’s half a plugin: I’m not sure there’s ever been anything quite like that, on one half of the wave a full Airwindows (noise shaped to floating point) ultra-quality saturation, and on the other half of the wave, ‘bypass’ and literal bit-identical pass-through. I made sure even the noise shaping wasn’t applying for the ‘bypass’ half.

The result is this: waveforms that need a little sweetening, can have that texture (not frequency or EQ, texture) subtly added to the track, in a way that utterly and totally maintains the integrity of the signal. In some ways this is ‘purer’ than any of the other Purest line, since by its nature it’s true bypass for literally half the time. It’s also one of the minimal ones, with just a switch: there’s no way to get the perfect integration of bypass and effected halves (they switch off like a push-pull power amp) otherwise, and it produces an obvious enough effect but one that’s harmonious and doesn’t get in the way. In some circumstances it hints at being like a ‘bass optimizer’ since it’ll push some second harmonic by its nature. You’ll probably find that for any given sound (especially an electric bass guitar) there’ll be one polarity that’s clearly better: I think for basses where the string swings near the pickup and produces extra voltage on that side of the wave, PurestWarm will saturate that side of the wave really well and it’ll give you an ideal bass tone with no extra fiddling or processing required.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PurestWarm processes audio in the Subtlety category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Subtlety](../categories/subtlety.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PurestWarm)

**Categories**: Subtlety

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Subtlety](../categories/subtlety.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
