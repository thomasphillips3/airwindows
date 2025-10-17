# Channel5



## Quick Info

| | |
|---|---|
| **Category** | Tone Color |
| **Type** | Tone Color |
| **Status** | Stable |

## Description

Channel for 2018, with new subtleties

## Detailed Overview

Channel has long been a sort of test-bed of mine, and so when I started working with new methods for some of my stuff it was an obvious choice. I’ve been asked for an extra Output level control, which it has (for those of you who are really into level matching, can’t fault you for that though sometimes I think it’s not relevant) but if you set Output to 1.0 it bypasses itself and becomes exactly, exactly the same as Channel4.

Except for two things, which first appeared in Atmosphere: this lets you A/B them with the original versions, using Channel 4 and 5.

One, I introduced the concept of live air denormalizing: before this (and on plugins I think are suited to it), Airwindows plugins watched for total digital black silence, and if it was present, produced an impossibly faint hiss sound, at around 300 dB down. If there was any audio at all that wasn’t digital black, this got switched off. With Atmosphere, it’s different: the denormalizing signal is always there, and if the result WITH the signal is digital black, then the signal’s subtracted again. Same result, but there’s a permanent noise hundreds of times quieter than typical ‘noise adding plugins’. The idea is that there can be no ‘dead’ silence, only ‘alive’ silence: you can’t save the file in normal formats and retain it (24 bit audio saving will simply turn this noise to digital black again), you most likely can’t hear it ever no matter what you do, but I wanted the deepest darkest silence to be alive rather than dead black nothingness.

Two, it noise shapes to the floating point buss differently, and on the one hand I bet you can’t consistently hear it but on the other, I think it matters. Before, I used an interleaving technique much like I often use in IIR filters and plugs such as Capacitor. It related to the sample rate by forcing everything to be considered as the interaction between two or more samples, and the energy being brought back into the output audio provided corrections at high frequencies. What began with Atmosphere, and what you’ll (maybe) hear with Channel5, is a completely different and more radical approach. These plugins noise shape ALL the error energy back into the audio. It accumulates, sticks around, and so it can contribute to bass energy in tiny amounts because it persists over thousands and thousands of samples. There’s a ‘pull-back’ in the form of multiplying the amount by something like 0.999999, which will bleed built-up energy away, but this multiply doesn’t happen on a per-sample basis. It happens per BUFFER. So, in the world of noise shaping floating point error, this is the one that stores up every tiniest bit of error and applies it, not interleaved but very smoothly, to the audio.

What should happen as a result of this is, there’s a sense of ease from switching from interleaved to the smooth way. It might seem a little less lively, and I’ll have some plugins that retain the other way. But due to the greatly increased time during which the error is held, plugins that use the new noise shaping will be crazy good at presenting analog-like, seamless bass and mids. So, more soothing, possibly less exciting, but a huge jump in depth and naturalness.

…in RELATIVE terms to what was there before. That’s the thing. I feel it’s possible that when you get used to it the change can be dimly sensed as a good thing. I don’t think you, or I, or anyone would be able to pick this out double blind. I can think of a mastering guy or two that MIGHT, but they’d struggle: these are people who take pains to dither to 24 bit and say that they sense something wrong if they don’t. It’s on the order of that, or even more subtle.

But I do feel that one eventually senses the full range of a sound one works with, and more importantly if I can make something better I will do so, without hesitating.

Have fun playing with Channel5. And if anyone needs to sound the alarm and say HEY! You need to stop using the new stuff! That noise is driving me crazy, and your noise shaping sounds awful now!

…well, that’d be pretty funny :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Channel5 processes audio in the Tone Color category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tone Color](../categories/tone-color.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Channel5)

**Categories**: Tone Color

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Tone Color](../categories/tone-color.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
