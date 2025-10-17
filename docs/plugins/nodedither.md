# NodeDither



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

adjusta-TPDF-dither, like a dither flanger. Can do Paul and Tape settings

## Detailed Overview

And just one more dither plugin before the eagerly anticipated Naturalize… (because who will care about these then?) …NodeDither, the testbed upon which PaulDither and TapeDither were developed!

I still think it’s good to have those as separate plugins (for simplicity and purity of concept) but since the concept is ‘TPDF made up of a sample of noise, and then a delayed version either normal or inverted’, how can I not give out the tool I used to find things like TapeDither? This was coded to do something that wasn’t possible: put a big delay in so there’s a ‘cancellation node’ at around 1.5K, making the noise quieter there.

Trouble was, all you get is comb filtering and no nice clear ‘quieter’ zone. That’s why I experimented and found that four samples delay (inverted) gives you TapeDither, a nice softer noise. One sample inverted gives you PaulDither (in other words, a very bright one-pole highpass). Two samples gives you a neat silky texture which is still very bright. Eight samples gives you a thing kinda like TapeDither but even darker and beginning to sound flangey… you might call it CassetteDither, or maybe ‘TapeDither for 96K’.

Call it what you like, because NodeDither lets you use all those and anything else, up to really extreme delays that give heavy, heavy comb filtering (flangeyness). You can reinforce lows rather than cancelling them through out-of-phase, and dial in dark moody dither noises that fit better with your project. You can tune the flangey note of the dither to your track. All manner of silly things can be yours with NodeDither :)

And yes, you can make your noisefloor a flanger. I’ve demonstrated in the video how to do this with automation. If people really REALLY need a flange dither, I can make one later, but Naturalize will not be delayed any longer and is due to come out this Wednesday. But hopefully the possibilities of NodeDither are worth having! Or, put it this way: if NodeDither is for you, you know who you are and you’ve probably already downloaded it and are playing with the controls and thinking of how it would affect your creations.

Because, bottom line: this is still technically correct TPDF dither. It’s just also an instrument, now. Have fun playing it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

NodeDither processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/NodeDither)

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
