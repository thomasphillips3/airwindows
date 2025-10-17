# kCathedral3



## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Stable |

## Description

a giant cathedral-like space using Bezier undersampling

## Detailed Overview

From the mad scientist's lab, bigtime!

This is the third kCathedral, and probably the final one before I launch into lots of other types of reverbs. I've got three lined up already, but this is where I figure out what the kReverbs are about.

The first one was like this: one knob, dry/wet (a 'wetness' knob, in that the center is full volume for both) and a 5x5 Householder matrix. Put it out, people had fun but it was kind of metallic. Not really ready. So I kept working.

The second one was one knob, dry/wet as before, greatly improved sonics. I designed new ways to generate and test the reverb algorithms, churned through millions of possibilities, measured and tested and cooked up a new and unique Cathedral algorithm. Also, tried a different sort of early reflections. Still a one-knob, but sounded a lot better.

Then… I did even more algorithm testing. And invented CrunchCoat. And then DeRez3. And then CreamCoat, a method for using that technique while keeping the downsample 'gears' from seeming unrealistic. And explored the usefulness of varying regeneration. And found that when varying downsampling it's useful to adjust regen. And discovered Discontinuity! And tried using it in the feedback loop of the reverb, to dial in realistic huge-space sustain at synthetic loudnesses.

So basically this ought to work for the genre going forward. If you thought CreamCoat sounded cool, that's the very primitive version compared with this, still a 5x5 Householder (already an unusual choice) but this time selected from more millions of options with new metrics for analyzing them. This time there's a predelay, a Discontinuity (says Top dB), a wide ranging Regen control (for realistic RT60s: this one happens to not go infinite). And that DeRez control you saw on CreamCoat, but this time it's on a BIG reverb.

I feel this ought to work really well for many purposes: just listen to it. It's still trying to be an Airwindows-style reverb rather than 'front and center instrument for making all possible sounds', but within the context of cathedral-style deep verb, I think this obliterates the first two AND completely abandons the 'over-simplified' thing I tried valiantly to make work.

Hope you like it, let me know what you think.

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

kCathedral3 creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/kCathedral3)

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
