# FathomFive



## Quick Info

| | |
|---|---|
| **Category** | Bass |
| **Type** | Bass |
| **Status** | Stable |

## Description

a way of supplementing extreme bass that’s not just EQ

## Detailed Overview

FathomFive introduces a special Airwindows algorithm that acts like a combination between an EQ and a bass amp. This plugin can be used in sound design or on isolated tracks, but it’s also part of an Airwindows DAW workflow I outline in the video I’ve made. The idea is this: rather than blur and damage your sound by running through lots of ‘fake analog’ effects on your buss to impart deepness and analog-like tone, use the Airwindows plugins Console4 and FathomFive to get a big-sounding mix while letting most mix elements through with minimal processing. You can run the ‘bass bloom’ behavior on an aux, and feed it with only the elements you want, and then integrate it into the sound with Console4 which both works the way Console wants to be used, and addresses limitations that Console has when used all by itself.

It’s all in the rather long video, and of course you can simply download and use the plugin if you prefer making up your own rules. There are no rules, I’m only explaining one very specific use case where FathomFive works symbiotically with Console.

(followup: this is a very old plugin. Newer ones that do this type of thing with increasing ease and friendliness are DubSub, DubCenter, and BassKit. FathomFive is wilder, and you probably want to keep an eye on whether it is spitting out excessive DC offsets, as the algorithm these plugins use for the bass is tricky to manage)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

FathomFive processes audio in the Bass category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Bass](../categories/bass.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/FathomFive)

**Categories**: Bass

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Bass](../categories/bass.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
