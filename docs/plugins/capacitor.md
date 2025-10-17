# Capacitor



## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

a lowpass/highpass filter of a new type

## Detailed Overview

Sometimes half the fun is just inventing :)

People say all filter plugins are just biquads with different GUIs. It’s not true… or at least it’s not true at Airwindows. (actually I have to see what I can get out of biquads: I generally don’t even use ’em at all)

This is a new filter. When I say new, I mean that you don’t have it. I can demonstrate that, because due to the way it works it has a little characteristic response quirk at 1/3 the sampling rate: nothing that hurts the sound, just an odd little notch under some circumstances.

Because it’s a typically Airwindowsy, not-normal EQ algorithm, nobody has tried it, and because of the little quirk, if anybody did try it they knew they had to reject it, because it wasn’t perfect. It had a quirk! And even if they experimented, they probably weren’t that invested in concepts like the sequence of operations on stuff that, in theory, could be done in any order. Why care so much about the implementation details of an idea that had a quirk anyhow and was therefore useless?

More fools they :)

Because musically, this filter has tone for DAYS.

There’s almost an analog-synth-like effect to it: though it doesn’t accentuate the rolloff point, it behaves almost like a DJ ‘isolator’ in the obviousness of its filtering. It has a highpass, a lowpass, and dry/wet, and the high and lowpass are melded into each other as part of the algorithm to get the sound more fluid. It’s also got new experiments in rejecting zipper noise and clicks, because I’m figuring people will want to automate this one. But, even though it’ll work for crazy effects and ‘isolator’ madness, the fullness of the tone will also let you use it in mastering: if you need to tighten bass or roll off just a hint of brightness, you’ll pay no penalty in the body of the music. And the dry/wet is there to let you treat it as a shelf… or to create a presence boost by isolating an area of interest, and then leaving it mostly dry with a hint of the clarified zone.

I’m thrilled with this filter, and nobody else has it: nobody else would be allowed to do this one, because it has a quirk at 1/3 the sampling rate, and typical commercial developers are not allowed DSP quirks. But, since I’m supported by Patreon, I am.

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

Capacitor shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Capacitor)

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
