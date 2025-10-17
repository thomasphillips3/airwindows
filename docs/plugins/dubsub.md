# DubSub



## Quick Info

| | |
|---|---|
| **Category** | Bass |
| **Type** | Bass |
| **Status** | Stable |

## Description

a fully featured bass doctor

## Detailed Overview

Be careful what you wish for. I like making plugins with very few controls, but when you have to use ALL the controls…

Here’s how it works. The top section, Treble Grind, is like a bass guitar presence circuit. You shouldn’t use that for hi-fi purposes, if you want clean pass-through use the Dry/Wet. Treble Grind works like a distortion, and has an Inverse/Out control allowing you to subtract it as well as add it. ‘zero’ is in the middle.

Crossover determines what goes to the Treble Grind, and what goes to the bass sections. To make it track bass better, set the crossover low.

Bass Drive is how hard you’re pushing the main bass section. It’s essentially an adjustable Head Bump control like in ToTape. Bass Voicing controls the depth of the bass boost: setting it higher up sounds more like overdriving a bass amp. Bass Inv/Out is the same as in the Treble Grind section, an ‘attenuverter’ like in certain Eurorack modules: it lets you subtract the bass, not just add it.

Sub Drive, Sub Voicing, and Sub Inv/Out are much like the bass section, except they work on an octave-divided version of the bass section. This helps it get good octave-down sounds some of the time, but it’s not anything like a digital suboctave synthesizer: it’s working crudely like an analog octave divider, which means it can make horrible noises if it doesn’t have clean signal to work with. This is of course intentional :) if you want it to do a recognizable sub-note, feed it a carefully controlled signal off a single track. Or, you can set it very deep and not mix in all that much of it, and get an interesting effect sound. For cleaner deep bass, work with the main bass section, or voice both of them very deep in hopes of cleaning up the sub-bass section a little by refusing to let it have more complicated signals.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DubSub processes audio in the Bass category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Bass](../categories/bass.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DubSub)

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
