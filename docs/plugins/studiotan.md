# StudioTan



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

all the 'non-dither' dithers, up to date and convenient

## Detailed Overview

If you were curious about the new work in quantization I’ve been doing… where I’ve put out a series of experimental plugins with names like Dither Me Timbers and RawGlitters and then said they weren’t dithers, or if you tried stuff like Dither Me Timbers and then found your limiter set to 0dB was now giving you overs, or if it just didn’t make sense at the time…

This is for you.

StudioTan is the sum total of all I’ve been doing with ‘dither’ that isn’t dither, for the last two years. It’s got three algorithms, StudioTan, Dither Me Timbers, and Not Just Another Dither. Each one is brought up to date, optimized, voiced to do what it does best. The first two begin with the use of quantization to apply EQ at ‘noise floor’ levels and the third applies Benford Realness statistics at noise floor levels, and they all use noise shaping to refine that behavior and get a specific tonal result. Not one of these have been quite available before, even from previous versions of Dither Me Timbers or Not Just Another Dither: it’s the latest finetunings of the algorithms. None of them can produce signal outputs beyond -1 to 1 so they can’t produce overs (if you’re ‘mastering’ so hot you get intersample overs, firstly that’s not a great idea and secondly StudioTan can’t help you there). All three come with 24 and 16 bit options right there in the plugin, as experimenter time is over and this is the final form, requiring no more fussing with plugins.

The effect of each is more pronounced at 16 bit, and that’ll give you a sense of what is being subliminally imparted at the far subtler 24 bit level.

StudioTan is like the posh, glossy, high class output. It sounds kind of like expensive studios and tape, brings up micro-detail but suppresses harshness. It’s slick and makes things sound more flawless and possibly more boring, but satisfying.

Dither Me Timbers is like the spatially enhanced, electrically charged output. It makes sonic events spark out of a darker, spacious background, and gives a little energy to transients and attacks. It makes things sound more human and attitude-laden, so it’s more dramatic and attention-getting. It’s got different noise shaping behavior and voicing but in basic character it’s the opposite of StudioTan, and can be approached from that direction.

Not Just Another Dither is like the holographic, hi-fi output. It’s a bit darker than previous Not Just Another Dithers and its purpose is to have detail go down to a digital noise floor that’s a balance of all types of artifact (since you’re always going to have a noise floor of something, no matter what you do) without changing character in any way. Since this perceived character is so balanced (this time, not even airy hiss as a ‘identifiable’ floor change) the new Not Just Another Dither is the best choice to seem like infinite resolution without even a noise floor being there. Instead of making ‘a sound’ like the previous two, it’s the one that sounds completely open and unaffected.

None of these give sensible results with test tones: you can’t take a sine and enhance high frequency details, so you get purely garbage data. Don’t use Airwindows non-dither dithers for scientific processing or your rocket ships will blow up on the launch pad ;) these are literally tone controls in two cases and an obscure data handling technique for the third, and they are re-voiced for 2019 to best deliver their sonic mojo. You can do test tone stuff to satisfy yourself they aren’t placebo effect: they really do the noise-floor-EQing or Benford Realness stuff, and the source code is open. But for evaluating how they really work, the proof is in the listening.

What they do cannot be done any other way, and they’re the final artistic polish on sonic creations done in or outside the DAW. Use them on mixes, or when mastering raw analog captures to lower word lengths for CD. They are ‘final dither’ in function if not strict definition, the way to crystallize high-res audio data into an output file that retains all the magic you intended, whatever flavor of magic that’s meant to be. The three categories of tone color ought to cover your bases there.

I know this is all I’ll be using from now on :)

(followup: it absolutely was not. I continued to use NJAD in Monitoring until I wrote Dark, have used that some including in Monitoring2 and then came up with a new dither based on Ten Nines into Dark, which is in the original output buss of Console8)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

StudioTan processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/StudioTan)

**Categories**: Dithers

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Dithers](../categories/dithers.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
