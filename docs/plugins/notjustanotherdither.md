# NotJustAnotherDither



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

a next-gen wordlength reducers for 24 bit with DeRez

## Detailed Overview

The votes are in, and the Internet has spoken. We’ve got a name for the new noise shaping variant on Naturalize, after a January of wild suggestions. Seems most people simply wanted to emphasize that this was not your ordinary dither, not your daddy’s TPDF.

This is the plugin (two, in fact) that beats all the other ones, including the original Naturalize. In normal use, this ‘dither’ (in fact it’s not a dither at all: it’s the Benford realness stuff from Naturalize, run with a noise shaper, and all the added random noise taken OUT) will make any fixed-point output sound like infinite resolution. It’s AU, Mac and PC VST. It has a switch for 16/24 bit operation (defaults to 24) and a ‘DeRez’ control where you can get low-bit NJAD audio if you like, or if you want to audition its noise floor behavior.

The output levels are low, without a bunch of extra energy coming from the noise shaper: it’s pretty well behaved, though like any hyper-performance ‘dither’ this is really meant for output formats. I don’t think any harm can come from repeatedly using this in processing, but you can always use a normal TPDF if you want no change in tonal balance (plain TPDF dither only adds broadband noise: more opaque, but if it builds up it won’t accentuate anything: dithers with a lot of high frequency energy can end up exaggerating that.)

(followup: I added a 16/24 bit switch, and DeRez. Also, the most current version of this is in Monitoring.)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

NotJustAnotherDither processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/NotJustAnotherDither)

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
