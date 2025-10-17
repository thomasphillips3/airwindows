# UltrasonX

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Latest Release |

## Description

a method for rolling your own Console-type systems with total control over your ultrasonic filtering

## Detailed Overview

A little while back, I made a simpler ‘Ultrasonic’ filter, with the intention of making a lighter-weight utility that could be used where Ultrasonic might go. The idea was, Ultrasonic (which is already available) was too heavy: it uses five stages of biquad filtering and I thought doing the same thing with just one or two stages would be better.

Turns out you can do that, but if you stack them up you start losing the super-highs. The one or two-stage versions weren’t steep enough: didn’t bring out the super highs close enough to the ultrasonic zone. But, the five stage version is still just too much processing to put all over the mix. What do?

UltrasonX solves this problem (that maybe nobody but me had :) ).

This is a plugin that does any one of the five stages in Ultrasonic, one at a time. It’s got settings for A, B, C, D and E stages. Each of these are a carefully calibrated resonance value, that add up to nice and flat and clear all the way up to the supersonic region.

Console7Cascade does something like this, internally, and gets a particular tone because its ‘more resonant A stage filter) is before distortion, and the softer unresonant filters that compensate for this are after the distortions.

But here’s the thing: if you want to make a Console topology where the channels aren’t overly brightening, but you’re feeding a submix buss that is more crunchy and shouldn’t be hit too hard, you can do that too. This is likely going to end up my problem but now you can experiment!

To do that, construct a Console system, using an earlier Console or PurestConsole (the original) and see to it that there are exactly five instances of UltrasonX in each signal path. Maybe two on each channel, two on the submix, one on the 2-buss! Or, one on each channel before hitting the PurestConsoleChannel, one on the 2-buss before the PurestConsoleBuss, and then three more sprinkled between your 2-buss processing. And any of these can be the ‘pre-brightening’ or ‘complementary darkening’ ones, meaning you could have the brightness boost after summing for a bit of air in between your instruments, or early on for softening saturation and adding glue.

Or, you could use it anywhere, or on one single channel (that didn’t have ultrasonic filtering) as long as you’ve got room to fit five individual filter plugins. Bottom line is, if your audio goes through ABCDE and comes out the other end, it should be correct. The rest is up to you :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

UltrasonX processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/UltrasonX)

**Categories**: Brightness

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Brightness](../categories/brightness.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
