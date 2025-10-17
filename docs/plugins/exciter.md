# Exciter

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

an Aural Exciter plugin that can be both subtle and extreme

## Detailed Overview

This plugin isn't my usual jam, but I've been listening to this type of effect all my life. The Steely Dan album 'The Royal Scam' wouldn't be the same without the Exciter effect. And now it's a free Airwindows plugin!

Note that this is NOT a clone of hardware, or any particular brand. As I usually do, I've extracted the guts of the effect and then adapted it so it can be used normally or exaggerated. You'll find that as you apply the effect, it'll start off sounding like it does nothing, gets more and more intense and then suddenly blows up into crazy distortion. To use it like a normal exciter, fine-tune it so that it's just barely making transients 'pop'. If you're hearing obvious crunch, you've already got it cranked up higher than real-world examples would let you do.

The effect works like this: get a sharp band filter going to extract certain kinds of information. Distort it with a soft clip (I use a sin() function, and some real-world examples used a 4049 hex inverter chip, which does a very similar super soft distort when used as an audio effect: it's the chip that made up Craig Anderton's 'Tube Sound Fuzz' circuit back in the day, and I still have lots of these chips to play with :D ) Then, once you've distorted this bandpass, add just only the distortion elements back into the full bandwidth signal, by subtracting the bandpass again.

Exciter lets you adjust the frequency you're using, and dial in the amount of effect you want. I'm pretty sure it'll consistently sound good (not quite natural, but this is 'late seventies heightened detail' tone here, it doesn't have to sound natural) if you're careful to not crank it too much. And of course this is Airwindows, you can crank it on stuff that doesn't have much to excite, and blast it on bright stuff to make a distinct form of gritty evil distortion for effect.

A lot of the stuff I like in analog is when transistors and chips are misused and freaking out. You can get tones like that out of Exciter, if you like. You can put it in the middle of uLaw, if you like. I've not tried that so you can be the first. I hope you enjoy Exciter :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Exciter processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Exciter)

**Categories**: Effects

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Effects](../categories/effects.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
