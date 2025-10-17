# DoublePaul



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

like PaulDither but more so

## Detailed Overview

This is for sort of a special purpose.

I’ve got an outrageous custom dither (well, wordlength reducer: there’s no noise and no randomness in it) called Not Just Another Dither. For final output, it’s that I recommend.

However, I’ve got a mastering engineer friend (Hi Bob!) who favors another dither of mine, PaulDither. The reason is, it’s traditional TPDF dither. It handles dithering duties perfectly (with a slight Airwindows-izing: the weight of the final noise floor is balanced to make one ‘bit’ function as zero, and to make the dither activate adjacent bits on either side for a better sound. This also gives a teeny least-significant-bit DC offset, if you assume ‘zero’ is between the two smallest bits, positive and negative)

I wanted to give Bob (and anyone else selecting traditional TPDF) something fancier that still counted as purely normal dither. So, here’s DoublePaul.

It’s TPDF highpassed dither, just like PaulDither. But, I’m also using some adjacent samples to skew the noise profile even further into the highs. It’s just a redistribution of energy, and it leaves the key pair of full-intensity noise samples to stay as TPDF dither. I just doctored the way you hear the noise, to push it a little farther into the highs. I’ve also backed off the teeny DC offset, and shaped every filter tap by ear. If you liked PaulDither, try DoublePaul and see if you like taking the PaulDither concept just a teeny bit farther, with no penalty to how the TPDF works. It’s just like a little sinc interpolation, a thing that’s trying to hide the TPDF energy by pushing it farther into the extreme highs. If you don’t trust NotJustAnotherDither, but you’d like something even quieter than PaulDither, try this.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DoublePaul processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DoublePaul)

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
