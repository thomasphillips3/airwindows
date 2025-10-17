# Righteous4

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Latest Release |

## Description

a final output stage for targeting dynamic range

## Detailed Overview

This one’s pretty eagerly awaited by some… all the more since I’ve incorporated all the latest tech, such as the changes in denormalization and noise shaping to the floating point buss (it uses the ‘more warmth, ease and depth’ version when set to 32 bit) and even the Spiral algorithm in its overdrive section.

But you might not end up using that noise shaping, because Righteous4 has NotJustAnotherDither (and the CD version) built right into it, along with an optimized ADClip and code from an old strange experiment I did called ShortBuss. Yep! Righteous4 is your all-purpose final output stage, which handles final clipping, saturating and even the dither to let you output 24 or 16 bit fixed point in the purest, most optimized way. It doesn’t even return to the DAW buss between these stages: everything is ‘long double’, so you put in your mix audio (from conservative levels to peaks that would clip a normal output file: it’ll soak up the peaks) and you get out literally the data you burn to the CD or upload to Bandcamp etc. as hi-res HD audio.

But it’s a little more complicated than that. Bear with me. Righteous4 will clog up and audibly distort under some circumstances, and it’s for a reason that might interest you.

Many music services these days (possibly all?) incorporate RMS loudness targets. They’ll turn up your stuff and limit it (maybe) which is awful but outside your control… but if you’re doing the loudness wars thing, they will turn you DOWN. And all your efforts to make loud masters will be wasted. Apple will cut stuff back to around -17 LUFS. YouTube goes for -13 LUFS. Spotify and Tidal do -14 LUFS. That’s loudness units short of full scale (similar to how many dB down from clipping your average (root-mean-square, or RMS) loudness is). Loudness war folks often push to -8 LUFS or even more, and that means YouTube will turn you down (and Apple will turn you WAY DOWN) to fit in with their playlists.

Here’s the thing: you can have all the peak energy you want (caveat: Apple doesn’t want your bright treble peaking over -0.4 LUFS in any case, so don’t go too bonkers with brightness when aiming for Apple music services). Peak is not RMS. In fact, music sounds great with lots of peak energy pervading it: this is one of the reasons old vinyl records sounded so great! I’ve measured RMS loudness behavior like -27 LUFS off old hit records. The energy pouring out of those old grooves is due to the way peaks and compression were handled: it was a different kind of limiting, handled differently, back then. Peak energy makes the music sound better. Righteous4 handles peak energy by clipping it with ADClip, so you can throw more at it in safety. This is not the audible clipping I’m talking about (at least, not if you’re talking percussive peaks etc. which are pretty cleanly clipped, especially by ADClip)

The audible clipping happens when you push your LUFS levels beyond the target. As you mix and set levels, you simply have to listen for whether Righteous4 sounds big and open, or whether it’s getting a little intense, or whether it’s obviously being pushed too far and breaking up (especially on bass, and mix fullness).

What’s happening is, the saturation from the Spiral algorithm is being fed into ShortBuss, which fills the energy back into the mix in the form of second harmonic. This is what gives Righteous4 its tone and extra warmth, and it’s a nice fullness and bloom UNLESS you’re slamming it (it’s calibrated using the slider, where you select your target). If you are too loud, you’ll hear it. Your peak energy will still be going up to the real clipping threshold, just as before, but your RMS energy will tell you how loud you should go.

It’s that simple. You don’t have to use it to hit LUFS targets, but since it’s got Spiral in there it also broadens the heck out of the ‘target range’ so you can pick whatever seems right to you, and it’ll guide you. If you find you need to push louder, you can set Righteous4 for a higher target, and that will clean it right up and let you push harder into the internal ADClip. If you’re looking for big dynamic range, you can set Righteous4’s target lower, or simply set it for Apple or YouTube loudnesses and then just don’t push into it very hard: this will give you dynamics, but the replay-gain services will be kinder to the result because it’s somewhat saturated and compressed, just in a very gentle way if you’re hitting it that gently. And of course the output’s optimized for whatever bit depth you’ve selected, so you can directly target CD or 24/96 or ’32 bit file to send to further mastering’ if you still need to mix into something more organic than a hard, brittle digital mix buss with all the charm of math :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Righteous4 processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Righteous4)

**Categories**: Saturation

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Saturation](../categories/saturation.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
