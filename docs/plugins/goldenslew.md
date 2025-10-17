# GoldenSlew



## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Stable |

## Description

a multistage slew clipper based on the Golden Ratio

## Detailed Overview

Slew clipping is a fairly uncommon effect: it takes the bright off sounds, but replaces it with a distorty edge. You've already got Slew to do slew clipping with, and if you like Channel part of what you like is its built-in slew clipping… but what if you could expand on what slew clipping does?

GoldenSlew is a chain of slew clippers becoming increasingly restrictive as they go, each one scaled by a factor related to the Golden Ratio (if it was applied to the 'slew' control). You would think this would produce a simple result: the sound would always be restricted to the smallest amount in the chain, and it'd sound just like Slew.

Except it SO doesn't… because each new value's working from what the previous one was clipped to. And so, when you apply slew clipping as a chain, you get a completely different effect. And what it sounds like… is distant, roaring, big, loud, powerful in a way you just don't get from slew clipping alone.

Be warned: for this plugin, like Slew, if you have audio going through it and you crank the slew clipping ALL the way to 1.0, what you're telling it is 'stop slewing completely, don't budge' which means sample and hold which means you're stuck on a DC voltage. There are reasons why you might do this, for instance if you're in VCV Rack and using it on a control voltage and you want to do sample and hold on that voltage. Don't crank it up to 1.0 on audio signals or you might hurt your speakers if they're DC coupled.

This is one of a series of plugins starting with Slew and continuing with GoldenSlew, where they're refinements of a tone I like using for analog emulation. When used for that, you typically want to keep the setting fairly low, less than 0.5 certainly. It's for controlling the digital-ness of the highs without apparently making them quieter: remember this is a clipper, not an EQ, and it'll kick in only on LOUD treble. There will be more explorations of this concept because I'll need a really good test-bed to use for when I start dialing in sounds of actual classic analog consoles: it's not just the maximum restriction of slew (like in the Channel plugins), it's about the sound character as we hit that limit.

You can use GoldenSlew on things like drums, final mixes: anywhere you want the effect of extreme loudness, but don't want the treble coming forward and poking at you. Hope you like GoldenSlew!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

GoldenSlew processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/GoldenSlew)

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
