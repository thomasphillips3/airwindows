# Biquad



## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Stable |

## Description

the Airwindows implementation of a biquad filter

## Detailed Overview

This little puppy is really flexible!

That’s true of any biquad filter, but I find most of them are really flexible and slightly plastic. Traditionally biquads require special handling, because you can’t push them too far before they break, and also they sound ‘DAW-y’ and synthetic. Not in the same way as linear-phase EQs, mind you, but still with something about them that feels digital.

So I fixed that :) with a couple caveats. Firstly, part of it is brute force. I figured that if biquads run into trouble with 32-bit coefficients on some filter curves, and it’s widely known that you should do things like run ’em in series to get better behavior, we could always run long doubles and be totally sure they work as intended. Overkill? Meh. Sure, but it’s known that these break due to losing control of themselves due to not long enough wordlengths. Why wouldn’t they work and sound better with long enough wordlengths? And so they do. Also, you get to run simpler biquads if you don’t have to run lots of them, so it averages out. I think it’s just a matter of audio DSP coders stubbornly insisting on not using long data words on the grounds it doesn’t matter to the sound. This, when the filters go obviously wrong under some conditions for just that reason? Anyway, here’s long double biquad, because nobody else was doing it far as I know.

The second part is trickier, because if you use it you remove some functionality. Biquads make great DC blockers. But, biquads also work through the summing of many delay taps, all very close together. Some are on input, others on output. They’re a mixing of multiple copies of the signal.

That means Console applies to the biquad filter.

We already knew that, of course: I’ve long observed that you can put Console (or BussColors4/ConsoleBuss4) around a bog-standard DAW EQ and get an enhanced sound out of it. Mind you, I wasn’t controlling that EQ, but it still worked. But now, I have Console5 (not 6, but I COULD do 6 in the right context) built right into Biquad. So, it does expect to have a signal between -1 and 1 (or lower than 0dBFS in the DAW), and that means Biquad itself can’t remove huge DC offsets ten times the size of the audio content. (It can still remove smaller offsets just fine). And it runs into basically PurestConsoleChannel, does the biquad, then uses PurestConsoleBuss and goes out to an inverse/dry/wet control (which itself has multiple uses).

What’s a biquad, you ask? The Airwindows biquad uses four of the six common biquad options (I prefer to do shelves with subtractive/additive use of filtered audio). The top control has settings one through four. They go lowpass, highpass, bandpass and notch. That’s what I consider the platonic set of biquads, and it lets the filter design be simple and clear. You can set a frequency (in ‘amount of the audio range’) from ‘zero’ to ‘one’. There’ll be EQs with more specific frequencies, that’s easy, but this is proof of concept and to be used by ear, plus it will always cover DC to Nyquist at any sample rate. Zero is not really DC, because that kills the biquad: also, One is not really the Nyquist frequency (half the sample rate) for the same reason. But, they act a lot like they range that far, because the high resolution lets Biquad calculate things accurately even that far out of the normal range.

They don’t update/recalculate every sample, but the way I’ve defined the data structures means they could if you wanted them to (at a cost in higher CPU-eating). The code’s MIT licensed open source, so GPL people can just take it if they credit me, and all the projects that are using the Airwindows library are advised to get up to date and include this one. Set right, it is THE ultimate sample-instrument tone shaper to sit ‘under the hood’ and voice somebody’s musical product after the sample-playback stuff is taken care of. You’ll be seeing a lot of stuff come out that uses this code, as there are many plugins that require this type of filter to work, often ones that will benefit from the sonic improvements that are part of Biquad.

More will be revealed. Suffice to say this is a very useful building block that’ll allow for some very special plugins.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Biquad processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Biquad)

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
