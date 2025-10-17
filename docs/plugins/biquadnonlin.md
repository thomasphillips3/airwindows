# BiquadNonLin



## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Stable |

## Description

Capacitor2, but for biquad filtering

## Detailed Overview

A biquad filter is a very basic piece of typical DAW EQs. If you were going to think of the most ordinary, normal, non-special digital EQ that would sound like every other digital EQ, you're probably going to be stacking up biquad filters. It is the most boring of digital filters, at least ones that are kind of flexible.

Let's break it!

BiquadNonLin takes the traditional biquad filter, complete with cutoff and Q factor, and applies the same technique used in Capacitor2. That was the one where I read about Murata ceramic capacitors showing striking variations in value, based upon how much voltage pressure was against them. Which is not to say all capacitors do that… but knowing this has happened in the real world suggests that it's an avenue to pursue. And so, Capacitor2 brought in this interesting nonlinearity based on real-world stuff, like a (in fact literally a) frequency modulation… and then it sat for a while. Because how would you even apply that to a carefully worked out algorithm like a biquad?

The answer is 'you just do'. Does it produce a clean result? Nope. You can break things pretty thoroughly, especially up near the Nyquist frequency. But you can apply less… I find 0.5 tends to work quite well… and you can get the same kind of nonlinearity.

It's just that this time, you can do it on a steep, resonant filter, and get that more analog texture on something that's otherwise very controllable. I'm looking to use this on many things: I think it'll make for a better-sounding distributed ultrasonic filter, and I'd also like to make a multistage version to use as the guts of a future ConsoleSL… because it should work more like a steeper but less vibey filter, except with the analogification.

Anyway, here's BiquadNonLin: one biquad filter, lightly broken for your sonic pleasure. Type at 0 is a lowpass, Type at 1 is a bandpass. The biquad tended to explode when I tried to make it do highpasses or notches, but it turned out I could just make the dry/wet an Inv/Wet control, so that means you just use Inv instead, and Type at 0 becomes the highpass (it's subtracted) and Type at 1 is the notch. If you have a hard time hearing the nonlinearity, setting it to highpass and sweeping it up at high NonLin should make it real obvious.

Oh, one more thing…

Today, the first VST3 is out… kind of. I have it up on GitHub at https://github.com/airwindows/Meter and you see it in the video for BiquadDouble. The thing is, I can't build it anywhere else except a single VST3 on my own machine, for Mac Apple Silicon only. The project on GitHub is all the code, up to date, and it's supposed to be able to build all sorts of different versions.

You can fork it, you can download it, you can try to get it to compile just like I did. There's lots of people smarter than me about computers and they didn't make this meter, so I had to. So, if you can make a Pamplejuce project compile, Meter is yours today, no matter what sort of computer you're on or what platform you're targeting. VST3? AU for iPad? AAX? Knock yourself out.

If you get anything to work, tell me how you did it, and everyone can have the result. Otherwise, I will keep plugging away, and eventually I'll get this stuff sorted out. But if you're impatient… the GPLed code is there, it compiled for me, let me know how you do :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BiquadNonLin processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BiquadNonLin)

**Categories**: Biquads

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Biquads](../categories/biquads.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
