# Air2



## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Stable |

## Description

a different bright EQ with silk tone and high sample rate support

## Detailed Overview

Here’s what you get: Air2 has three treble-boost bands, Hiss, Glitter and Air. The first two are very like what’s in Energy2, but Air2 is NOT the same: it’s a different algorithm, not done the samw way Energy2’s ‘Rat’ band is done, and it has a broader, softer air band that’s less ‘raw harsh energy injection’ and more ‘bright and pretty’.

And then, they all run through a ‘Silk’ control… inspired by but NOT the same as the Neve Portico Silk circuit. That is a real hardware transformer biased into second harmonic creation by a DC current. Air2’s Silk control is the same thing as Single Ended Triode (which you can download and use already) but only applied to the highs out of Air2, so it’s the same general concept but is not a clone of the Portico preamp. Plus if they freak out I will rename it to ‘Sow’s Ear’: it’s part of a treble brightener and the same basic functionality and as far as I’m concerned, nothing is stopping me from asymmetrically distorting highs, and Silk is the best general term for what that does. Except with mine you can push it too far for effect, because of course you can :)

And finally, unlike Energy2, the Dry/Wet control for Air2 strikes a new balance between the Energy style of increasing the effect, and the traditional Dry/Wet control. New with Air2, you can now turn it to full-wet and get ONLY the output of the brightener bands. They’re not exactly filters but they act like it, and by adjusting them against each other you can produce insanely treble-boosted sounds and wipe out everything else using Dry/Wet. The way it works is, up to 75% (0.75) you still have full volume Dry. It won’t re-balance your track, just add whatever Air2 highs you’re looking for. Then, between 0.75 and 1 (full Wet) the dry goes away, so if you crank it up all the way you get the fullest extreme, but for most normal use it’s like Energy2, taking an unvarying dry signal (which is NOT undersampled) and adding however much of the effect you like.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Air2 processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Air2)

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
