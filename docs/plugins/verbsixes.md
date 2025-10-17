# VerbSixes

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Latest Release |

## Description

a calibrated reference reverb plugin for Householder matrices

## Detailed Overview

The only thing small about this is the interface, and there's a reason for that.

VerbSixes applies Householder matrices to produce reverb, and it's named VerbSixes because it escalates things up to the point of 6x6 matrices. Normally you get 4x4 matrices in conjuction with allpass filters which smear out the sound (example: my CloudCoat plugin is made up entirely out of allpass filters, as is MV). There's a reason other matrix sizes aren't popular: firstly, you can use multiple 4x4 matrices, and secondly the math is messier with other sizes. With the 4x4 you can feed all the delays into all the other delays at unity gain, just flipping the polarity.

A 3x3 matrix gives you 27 distinct echoes out of 9 different delay lines.

A 4x4 matrix gives you 256 distinct echoes out of 16 different delay lines, only 7 more, and the math is quite straightforward.

A 5x5 matrix, which I've been doing for all the kVerbs I've made, uses only 9 more delays to get 3125 distinct echoes… which is an impressive jump from 256, especially when you're using the ability of a Householder matrix to feed back into the input again. That'll quickly get you lots of echo density, though it'll sound repetitive with smaller matrices like 3x3 or 4x4. 3125 with regen is a lot, though the math requires multiplications by -2 and 3.

A 6x6 matrix gives you 46,656 distinct echoes BEFORE regen. And all the math is either unity gain or times 2… which of course we know as BitShiftGain, a math operation that only changes the exponent and doesn't alter the mantissa of the floating point number in any way (one of the secrets of the old Midiverb, which didn't have floating point math capable of complicated multiplication).

VerbSixes comes with a built-in 6x6 matrix with a calibrated amount of regeneration, so it's the most recent generation of Householder matrices, prepared to produce extremely lush fluid reverb, in spite of having no filtering or allpasses whatsoever. In fact it has no controls either: it gives exactly one RT60 no matter what the reverb is.

That's because VerbSixes is also set up to demonstrate 5x5 reverbs. And 4x4. And 3x3… and ANY COMBINATION of those things.

So if you're making a 4x4 matrix, generating variations on them with my program IntoTheMatrix, you can compare the results knowing they're going to be consistent. They're also pretty consistent with the other matrix sizes (to the best of my ability) and a full range of delay lengths (smaller spaces will tend to get louder). It's a reference reverb maker, running all wet, and you can put it on an aux or just wallow in depth, and if you can get the VerbSixes code to compile and also run IntoTheMatrix, you can generate anything and try it.

Or you can use it just as a plugin, which is a 6x6 giant hall… times an entirely separate 4x4 matrix, so call it 256 giant halls laid end to end.

Just short of 12 MILLION echoes, even without regen. And they both have regen.

I'll give you more reverbs based on this technique, but enjoy the new bigger-than-Cosmos space :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Early Reflections]
    A --> C[Diffusion]
    C --> D[Feedback]
    D --> C
    B --> E[Mix]
    C --> E
    A --> E
    E --> F[Output]
    style C fill:#6366f1
    style D fill:#8b5cf6
```

## How It Works

VerbSixes creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/VerbSixes)

**Categories**: Reverb

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Reverb](../categories/reverb.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
