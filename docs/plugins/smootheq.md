# SmoothEQ

![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

a sharp, accurate, transparent three-band filter

## Detailed Overview

This follows AngleEQ, so it follows an extremely weird, colorful, poorly behaved EQ with a super-clean, accurate, well-behaved EQ, just for variety. Not in the sense that you dial in exact dBs and frequencies: it's still a 'by ear' filter like the great analog EQs, and I'm probably not the person you go to for 'add exactly two and a half dB of 3026 hz shelving and that's the important part, all EQs sound the same'.

When I say accurate, I mean that unlike AngleEQ if you set SmoothEQ flat you get EXACTLY what you put into it. It uses a subtractive technique that I like, not sure if other people do this, where the sound is assembled out of sub-bands that are always 'one band is the filtered, and the other is that subtracted from dry'. It's that which I couldn't do with AngleEQ, and which has been tricky with everything short of simple biquads (for which it works excellently).

And this is the breakthrough where I worked out how to do this thing I like, which I'm not sure anyone cares about but me, with ANY degree or order of filters so long as they're biquads. Maybe even beyond that, but turns out biquad filters are very cooperative with this.

SmoothEQ uses eighth-order crossovers: steep! They isolate real well. But so powerful is the technique that I can use Bessel filters instead of Butterworth, for nicer phase behavior. There are limits: I don't think I can use this for speaker crossovers, it's strictly for setting relative volumes of EQ bands and listening to a combined output. The trick is, if I apply cascaded filter crossovers and try to subtract it from dry, I get what I got in AngleEQ, a phasey mess.

But if I reconstitute the original signal from the 'sections' between EVERY stage of filtering, I get the degree of filter steepness I wanted, AND all the sums still reconstitute to a perfect, bit-identical input if set flat.

If you wanted an Airwindows five-band, or seven-band, or 31-band EQ this is how I'd have to go about it. I don't know if it would hold up at 31 bands of EQ, or how well that would work, but mathematically I know that if you set it flat you'd have ultimate, bit-identical, perfectly transparent sonics, because that's the only way the technique CAN work. There are obvious applications in making, for instance, a Mesa Boogie 5-band guitar EQ and having it sound amazing without analog modeling: sometimes what you want is the merits of analog processing, not just to imitate everything. It'll make EQs that are perfectly accurate set flat, and then you're shelving up and down bands of frequencies with extremely clean boundaries, as steep as you like.

SmoothEQ is a simple three-band version of this. Now that I know I can do it, I can do a future ConsoleO (orchestral) and really do a good job of keeping the tone even through filtering. This is not a linear phase EQ but does not need to be, since everything is either perfect or some degree of the tone produced by extreme EQ isolations: whatever that sound, if you add only a tiny amount of filtering you automatically get only a tiny amount of that tone color. That's why I build it in that peculiar way, to get that result.

It's going to be fun running with this technique and making stuff sound better, and I hope you like SmoothEQ :)

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

SmoothEQ shapes frequencies through EQ. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/SmoothEQ)

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
