# NaturalizeDither



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

deterministic dither that uses Benford Realness calculations for each sample

## Detailed Overview

Last and definitely not least in the dither-fest: Naturalize! This dither is often considered best by listeners. It works on every genre, at every sample rate. It adds no tonal color to the audio, and the noise it produces is quiet… but more than quiet, the noise of Naturalize has a fugitive quality where it seems to ‘hide’ behind the reverb tails, and once you start listening to the music it’s difficult to hear there’s any noise present. The sense of reality produced by the music is compelling enough that it doesn’t draw attention to the noise floor at all.

How can this be? I kept the secret for eight years but now that Airwindows is supported by a Patreon, I’m free to communicate how I did it, because my compensation is basically ‘the number of people out there who think I ought to keep working in this field’, and the more of those the better. I don’t have to keep Naturalize just to myself anymore, because it helps the Patreon when I’m generous. So, go ahead and download and use it for free (it’s running at 24 bit, use BitShiftGain to get 16 bit out of it) and here’s how Naturalize works.

Benford’s Law is a statistical technique: basically, it says that in lists of natural data, if you get rid of all the leading zeroes, the first digit other than zero is most likely to be ‘one’. That’s no matter what scale the number is at: no matter how many zeroes you have to take away to get to the first number, it’s more likely to be ‘one’ than, say, ‘nine’.

In fact, it’s ‘one’ thirty percent of the time, and the other leading digits are progressively rarer. How much rarer? I’ll give you a piece of the Naturalize code and the numbers I’m using.

byn[0] = 1000;
byn[1] = 301;
byn[2] = 176;
byn[3] = 125;
byn[4] = 97;
byn[5] = 79;
byn[6] = 67;
byn[7] = 58;
byn[8] = 51;
byn[9] = 46;

This works on sample data that varies in logarithmic scale: fortunately, audio is already that way. Something like a reverb tail is perfect for Benford realness calculations! As the sound dies away, it SHOULD fall into just this sort of pattern: millions of sample numbers, scaling down to tiny near-zero values. It ought to be the perfect picture of Benford’s law.

Here’s what Naturalize is. Every sample can be truncated in two directions: up or down, to the nearest value. So we do both, and then we run the Benford’s Law calculation on each, and we see which choice will get us closer to that perfect ‘realness’ distribution.

Then we just choose that direction :) that’s it! Each sample, we always choose the direction that will bring us closer to Benford’s Law.

This works on a statistical basis, to produce a collection of sample values that hold to what you’d get if you directly sampled ‘reality’. It erodes unnatural qualities in the digital audio, and it’s pleasing to listen to. There’s no excess energy to worry about: it’s always within one least significant bit of the target audio. And I might be able to improve upon it (I initially remembered it as having no noise sources at all, but it’s using some noise to shake up the values a bit for better distributing) but as 2017 begins, doing this gives you the best sounding dither in the world. I’d be happy to see if I can make it even better: support my Patreon, after all I came up with this thing in the first place, stands to reason I can develop it even further. Maybe I’ll make it entirely deterministic, with no noise at all. I’m sure I tried that already, but sometimes persistence pays off.

(followup: Naturalize is the first example of what then became NJAD and went through a couple of revisions: the most current and best version of NJAD/Naturalize is the NJAD that is in the plugin Monitoring.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

NaturalizeDither processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/NaturalizeDither)

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
