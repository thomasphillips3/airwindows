# Isolator3

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

Isolator2, but on one slider, with a band-narrower control

## Detailed Overview

Isolator3 is basically a request. I got asked for an isolator filter 'on one knob', which I've seen around but I've not used myself. Basically it means middle is full-range, to the left you're lowpassing and to the right you're highpassing.

Turns out you need to run it as two filters because it's impossible to 'switch' the biquads inside it, from one role to the other. So you constantly run two filters one of which you can't hear the effect of.

Except then there's the Q control, which does not actually control the Q of the filters. They're still steep, stacked-up filters without special resonances of their own. But when you turn up the Q slider, the cutoffs approach each other, turn into something like a bandpass on the fly. Full up, it should act a little like a resonance. To go back to full range, turn Q back down to zero and Iso to 0.5 (the middle).

Lastly, this is lots and lots of filter stages all of which are smoothed for better modulation… but it's made of biquad filters, which don't like being modulated, and then it's two types of filter run into each other. I've put in safety clipping because it turns out that if you yank the control around real crazy, it's easy to get Isolator to glitch out. The glitches aren't always useful sounding but now and then it emits really weird synthetic burps and frills and so I've just made sure it can't blow up the output too bad, and then left it to its own devices. So, use Isolator3 with smooth intentional motions for traditional effects, yank it around madly if you want it to spit digits and sparks at you, have fun is the most important instruction.

Hope it works as I got COVID returning from my vacation and it is heavily still with me so I've lost a bunch of steps. Not ideas, it's just that this is a good time for me to work through the backlog a bit. May or may not livestream in the upcoming week and if I do I won't be talking for eight hours at a stretch: probably won't need to go to the hospital but will check with a doctor. I'm in my space, Chris's 'hunting for ideas mountaintop' and it's no biggie for me to hole up for a few weeks. See ya again next week with something else from the backlog! :)

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

Isolator3 shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Isolator3)

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
