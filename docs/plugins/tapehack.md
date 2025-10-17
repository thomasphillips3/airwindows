# TapeHack

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Tape |
| **Type** | Tape |
| **Status** | Latest Release |

## Description

a new dimension in tape realism, abstracted to software

## Detailed Overview

It started with a paper by Spencer Walters, on this subject: what's the role of hysteresis in magnetic tape recording? We tend to assume that's fine, we're making it linear, apart from all the soft saturation of course. Even then, that's not quite where it starts: it's research on Dolby HX-Pro that got Spencer thinking. I'm not sure the Dolby people quite understood the implications of what they had, as that was an era of 'remove all distortions'.

Gradually, Spencer started to figure out what he had, and there's analog hardware coming out from Walters Audio that I frankly covet. And Spencer wrote a paper, talking of magnetic flux and relative coercivity and hysteresis loops. I frankly don't have the math he does, but I worked with analog tape growing up, and have a good idea of how it responds. And there was this set of diagrams, of a 1kHz wave magnetizing tape, and what you actually get out of it without and with tape bias…

It showed there was a dead spot, if you didn't bias. Well, I knew that: I'd coded something like it into ToTape 7 and 8, letting you dial in a section of Type AB distortion if it was 'underbiased'. But look again: that dead spot is still there, if you bias. The recording is sweeping back and forth across it at 100 kHz, but it doesn't stop that dead spot, where magnetic tape's coercivity hasn't kicked in, from still existing. You're just keeping it way busier than before, but a 100k wave still has to sweep through zero each cycle.

What if this dead spot was central to tape sound as we know it? What if there's always a hint of it, a bit of antisaturation in there at the opposite dynamic extreme from TAEP PHAT, as shown in Spencer's diagrams? More importantly, could I code something like that?

Sure could :)

TapeHack does a number of interesting things due to what I came up with. First, it's very efficient: it's a simpler, lower-CPU form of a sin() function, so it has the softclip nature. It's made to have this 'extra zone' by manipulating how an approximation of sin() is made, so I can also do variations on it and asin() and combinations of them, for the purposes of future Console versions. Doing that tends to take away the saturation effects, so there would be additional layers of TapeHack for making 'vintage consoles' sound as we experienced them.

The differences in waveform can be described. Unlike sin(), TapeHack hits a soft saturation point and then takes the flat top and begins to extend it, while turning the 'quiet part' of the wave into more of a trapezoid shape that's remarkably persistent in its slope. The steepening curve of the soft-clip gets sharper and sharper while these other factors stay relatively consistent.

As a result, TapeHack does 'tape compression' better than anything I've ever made, full stop. Turns out you can make sharp softclip corners, but we hear 'brighter' as a function of how much more steeply that center part of the waveform slopes. This is likely to be exactly the same in the Walters T805 (patent pending) even though that's fully analog: you can see it showing up in oscilloscope traces in Spencer's paper. It's heard as a shockingly believable 'tape bark' on things like drums, it's heard plainly when you run a heavy guitar sound hot to 'tape' to make it sit more up-front, but just as importantly, it livens up a more quietly 'recorded' track by giving it that characteristic dynamism and optimal distribution of peak energy.

A side note: I've posted classic vinyl records and measured them, tracking peak vs. RMS energy, as that's been my own parallel pursuit of what went on in those very sonic Seventies, when things just sounded better to me. A common factor is WAY more emphasis on peak energy and crest factor, with it persistently sitting much better dynamically than digital accuracy gives you. Well, this lines up with that observation exactly. Applying this hysteresis (or, like with TapeHack, just using the transfer function directly) produces both the peak distribution and the desired sound.

There will be more about this: and yeah, Spencer's aware of what I'm doing and cool with it. In fact he'd like to know if my testimonial (in his thread on the matter) can go on his website. My work on TapeHack suggested to me that he's really on to something with this, I'm happy to say so, and my more abstracted version is something we can all enjoy. (oh: it's also perfectly suited to oversampling for folks with something like Reaper where you can just do that. I won't be, because I think it gains more from the immediacy of direct processing than you lose from what little aliasing it'll produce)

I'll be saving up for the hardware Spencer makes, and I'll be using what I learned in TapeHack for many things. Hope you like it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Bias]
    B --> C[Saturation]
    C --> D[Head Bump]
    D --> E[Flutter]
    E --> F[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

TapeHack emulates magnetic tape characteristics including specific tape behaviors. Use it to add warmth and analog character.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tape](../categories/tape.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/TapeHack)

**Categories**: Tape

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Tape](../categories/tape.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
