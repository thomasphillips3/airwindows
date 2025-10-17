# Console0Channel

![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Stable |

## Description

a radical, minimalist Console system

## Detailed Overview

If the weirdness of Airwindows Console systems tends to throw you, it's probably good to skip this one. You'll either hear what it's about… or you won't. This is sort of an extreme position of a line of inquiry that not everybody buys into. It's really quite clear what's going on and why, but people disagree very intensely on whether it matters. Rather than make allowances, I thought I'd push it to the most radical extreme possible to see what happened.

Meet Console Zero.

There will probably never be anything that goes farther in this direction… not in the purely digital domain, anyway. Not as free open source plugins that everyone can have. It's easy to get external hardware to do some of these things, but that's costly. Console Zero can be used by everybody… if, that is, you can deal with the demands it makes.

Console Zero is the Airwindows Console concept, crossed with the BitShiftGain concept, and pushed literally as far as it can possibly go. It has built-in gain and pan… kinda. It has aliasing-suppression filtering… kinda. It does the saturate on channels and then anti-saturate on the buss… kinda.

Everything, everything is sacrificed to the Mantissa Gods. The idea is, with many analog-to-digital converters, with even fairly humble ones you can get quite a lot out of them if you just pass the audio straight through. Analog to digital straight to analog again? Often, it'll capture a really good sound. It all goes to hell when you start trying to work with it in the box.

Even on a system like Console8, with NO other processing, there might be hundreds of mathematical operations on every channel, thousands. Things like sine and arcsine functions do a lot of processing to be accurate. Biquad filters can get you nice accurate filtering, but require lots of math operations to function. The stuff modern mix topologies get up to could be tens of thousands of calculations, PER sample, PER channel on the way to the final mix. We take this for granted and nobody tries to make the opposite approach work, certainly not while including filtering and analog emulation.

Console Zero does maybe eight math operations, per sample, per channel, between input and the final mix output, that touch the mantissa of the input values. INCLUDING the actual mix. Including the Console saturation/antisaturation system. Including the aliasing-suppresion filtering. Eight, if I remember correctly… for the ENTIRE chain.

How? By leaning on bit shifting, to an insane, excessive degree. It's a giant trade-off. All level and pan is done with built-in BitShiftPan. (even on the buss, and you shouldn't touch it… but why not? The point is that it doesn't alter any mantissas). That is mixing in 6 dB increments, 3 if you count moving stuff one notch to the side to make it quieter. The filtering is strictly simple averaging. One operation, and a bit shift to get back the original gain: the bit shift doesn't touch the tone. The Console system is simplified so much that it's just one calculation and another bit shift. Everything is traded off for minimalism. The saturation produces slightly more harmonics than something like PurestConsole, but almost without calculation.

You get a mix together in Console Zero through arrangement, through broad strokes. You CANNOT fuss with it. It's almost LCR panning, except there are obvious left-center and right-center points included, and a range of pannings nearer the edges. All these points sound exactly like unprocessed raw digital audio, all of them pass through the unaltered mantissa from the input sample. The entire mix, with all its levels and pannings, puts through every single track as if it was the untouched raw signal without even a gain change… because there is not a single mantissa change to any track on any channel, going into the Console processing.

This may mean NOTHING to you. If you got here and that's you, thank you for the great patience. And… does it sound good? All of this is in pursuit of a particular KIND of sound, very unlike typical DAW sound. Do you hear that in my example, do you hear it if you attempt a Console Zero mix? If you hear nothing unusual, move on, this is not for you.

Some of you are going to lose your minds over how good this can sound. This is for you :)

Wait, it gets worse! You have to run 96k this time, 192k if you really want extended highs. If you're at 44.1k, the averaging will still work. It will be REAL DARK. Sorry! That means some people could do mixes at 44.1k with some of the desirable qualities we're seeking here, just so long as it's meant to be dark. Plenty of genres that can do that. But you should be running 96k. These plugins are SO lightweight, it's hard to even express how light they are: again, eight operations across the entire mix buss, not thousands or hundreds of thousands, per sample. That's from input to mix output. That will stand up to a lot of tracks… and the other secret is, Console Zero LOVES high track counts. The more stuff you have layered, the more freedom you have to do subtle loudness adjustments: a 3 dB nudge on one layer of one track made of four layers means the total loudness of those doubles, is the same as adjusting all of them by 0.75 dB. It will nudge one of the layers sideways in the stereo picture. And? The task becomes managing aggregates of tracks, thinking only of the big picture, letting some stuff be buried in the mix because you simply can't nudge it up in volume to balance.

And it can all come together and work, better than you'd ever imagine, and quicker… and sound like life, not like a DAW.

Either this will work for you, or it absolutely won't. Either it'll blow away anything you've tried, or completely frustrate you. This one's gonna be polarizing. It goes so far in the directions I try to achieve, that I'm certain it'll blow some of you away, and it's gonna make other people really mad. What price is an untouched mantissa? How much can you hear the inevitable digital erosion of overprocessing… and just how little processing can you do in a mix and still have a mix at all?

Console Zero… if you dare :) I will return to more accessible stuff, analog emulations etc, now. There will be no beating Console Zero for what it does. The rest is doing interesting tone colors, which I promise I'll bring you… but if this is your jam, you're done. There won't be any better from me or anybody else. It will beat many external summing busses. Console Zero is yours now.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Encode]
    B --> C[Summing]
    C --> D[Decode]
    D --> E[Output]
    style B fill:#6366f1
    style D fill:#f59e0b
```

## How It Works

Console0Channel is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Console0Channel)

**Categories**: Consoles

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Consoles](../categories/consoles.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
