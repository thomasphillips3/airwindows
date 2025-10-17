# Hull2

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

a very clear three-band EQ

## Detailed Overview

We ended up using the Hull algorithm in something! It's what makes the high band of ConsoleLA work. Hull2 is taking the guts of that code and giving it to you as a pristine, no-saturation, no analog mojo, pure EQ.

Note that I didn't say 'normal' ;)

The idea here is that it's very, very simple algorithms that combine to produce complicated results. When I describe what happens here, keep that in mind: the code that produces it is incredibly pure and simple, and the tone of these odd and complicated effects is very transparent and hangs onto expressiveness instead of degrading the tone.

You've got a treble, mid, and bass control. If you move them all together, you get a simple gain control that's roughly as good as PurestGain. It's very close to PurestGain, if you've moved all three controls exactly together, and that's how transparent Hull2 can be.

If you boost treble relative to mid (at any position), you get the 10k-centered boost from ConsoleLA, but without any harmonics or other alterations. It's an even clearer effect. It centers on 10k and falls off slightly above that (remembering that, flat, it's a perfect bypass).

If you cut treble relative to mid, you get at first a soft notch, then increasingly steep. And then, the notch gets shallower again, and then it becomes a very steep roll-off slightly higher than that.

If you boost lows relative to mid (at any position) you begin to lift the lows, while subtly cutting around 700 hz causing the sensation that the bass region is shifting lower while boosting.

If you cut lows relative to mid, it'll subtly lift those same lower-mids, so again it's like shifting the voicing of the track rather than just 'adding and removing exact frequencies'. It's very broad-stroke EQ, like two tilt-EQs with a hinge in the middle, if that makes any sense.

All this is designed in, but it's not done by banks of EQs doing elaborate (and unaccountable) things. It comes out of how very simple algorithms interact with each other, so the behaviors are somewhat designable but it's kind of unavoidable. It's the cost of using these crossovers at these steepnesses, and the trick is to design it so the weirdnesses do musically useful things. And then, the other trick is to construct the three-band EQ by deconstructing the input in such a way that you can just add it together again and get the input back.

You could have the craziest, wildest crossover behavior, with all sorts of pre-ring or whatever (Hull2 doesn't, but you could have this) and subtract it from the highs to get a mid band. If you do that, both the bands will have exactly matching pre-ripple, if there's pre-ring (same with phase issues, etc).

And then if you put 'em back together you have the original back: no more ripple, phase or anything.

And of course if you apply only a tiny amount, you get only a tiny amount of whatever character is part of the crossover. And that's the principle in ConsoleLA, and in ConsoleMC (and MD), and now it's in Hull2, where ConsoleLA's treble crossover was developed.

Hope you find some use for it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Filter Stage]
    B --> C[Resonance]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Hull2 shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Hull2)

**Categories**: Filter

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Filter](../categories/filter.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
