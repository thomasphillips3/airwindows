# Hermepass

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Bass |
| **Type** | Bass |
| **Status** | Latest Release |

## Description

a mastering highpass to set by ear only

## Detailed Overview

This is specially by request from Gregg of Hermetech Mastering: it’s my try at a specific plugin he wanted. He wasn’t able to find a fantastic-sounding highpass with JUST a frequency control and slope, no bling, no other stuff, as small as possible.

This is of course right up my alley :)

All the more when he responded warmly to my idea of having both the cutoff and slope have NO LABELING to guide you: just 0-1 sliders. You have to listen. That’s the whole point, and I delighted in taking it that one stage further.

Two stages further, because I worked out how to make the slope control continuous. It uses up to six poles (staggered, an idea that Gregg and I independently came up with: it’s present in my ToVinyl2 and ToVinyl3) but as each pole is added it gets its own little dry/wet internally, so you can have two and a half or four and a third poles. Smooth continuous adjustment of how many poles (and how steep the slope), much like my bit-crusher has continuous sample rate crush and bit depth crush.

Three stages since it uses Airwindows interleaved IIR filtering for the very first stage to start off at a slope even shallower than one pole of IIR: sort of ‘half a pole of filtering’ to start off.

The controls are set up to give useful results around the middle of their travel. I’m not sure exactly how many poles that is, or what frequency: use your ears, says me and Gregg (for whom I made this). I do know that depending on how you set it, the transparent cutting of extreme low frequencies WILL give rise to higher peaks, so either gain stage it or use limiting or clipping. This plugin is not a loudenator. It’s a tone shaper, for retaining every possible bit of tonality while reshaping the extreme lows to trim the lowest frequencies: it’s sound balancing, not ‘make louder-ing’.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Hermepass processes audio in the Bass category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Bass](../categories/bass.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Hermepass)

**Categories**: Bass

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Bass](../categories/bass.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
