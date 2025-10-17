# Energy



## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Stable |

## Description

electrifying fixed-frequency treble boosts

## Detailed Overview

In the continuing series of ‘weird algorithms other people can’t give you’, here’s Energy. What’s the matter with Energy that only Airwindows can/will do it? Pretty simple. It’s a bizarre algorithm which acts like half a super-high-Q boost and can’t be tuned in the normal way. It can only work on integer multiples of the sample rate. So the labels only relate to 44.1K, they’re colorfully named rather than specifying frequencies, and at different sample rates any frequency labels would be lies anyhow… and they can’t be tuned, and the Q can’t be altered. Literally all it does is slam huge amounts of super-aggressive treble on.

But what a treble it is! Energy accentuates the attack transient like no other high frequency EQ (especially linear phase, and ‘DSP cookbook’ biquad EQs). The principle of operation is totally different. It didn’t catch on because it’s a weird idea to start with, and it’s completely not adaptable to anything. It’s not even that great at cuts, though you can try it for cuts if you like. It’s really just about slamming a bunch of punchy brightness on at 22K, 15K, 11K, 9K and so on: or, Hiss Glitter Rat Fizz Scrape Chug Yowr Snarl, as the labelling goes.

The lower ones extend down into high-mids as you’d imagine (at high sample rates they’d work as high-boosts) but that’s another reason I can’t simply label them as frequency controls. These are nasty. They won’t give you clean tidy boosts, not even ‘analog style’ clean tidy boosts. They’re interacting with the sample rate in a nasty way and produce a bunch of extra overtones and skronk so it’s better to leave them as adjectives to avoid even the suggestion that they would give you polite EQ shaping.

But if you are looking for brutal, raw electrifying ENERGY I think it’s hard to do better than Energy. The only thing that’s new on this old school super secret weapon, besides denormalization and the noise shaping to the floating point buss and higher resolution internal processing, is the InvDryWet control, which was an obvious call. Since the different sliders can get into strange interactions, since you can play them off against each other, that means you could try to isolate high frequency stuff you don’t want and accentuate it as much as possible… and then, return to dry, and give it just a bit of inverted effect. That’s one way to tame nasty highs (such as from a bad condenser mic). I accept no responsibility if the bad mic, combined with Energy boosts, kills you with treble. That’s kind of Energy’s job :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Energy processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Energy)

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
