# CStrip



## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Stable |

## Description

an Airwindows channel strip

## Detailed Overview

Sometimes, Airwindows dabbles with what you might call ‘the normal’ plugins: for instance, CStrip. I was asked to make a channel strip, and while I usually prefer to do things in a more modular sense, it seemed like a fine idea, and so now there’s an Airwindows channel strip, with sort of the usual things you might find there.

Sort of. ;)

It’s never quite that simple with Airwindows. So, you’ve got a three band EQ, but if you boost the top you get traces of the ‘Energy’ plugin just to add some aggressiveness to the extreme highs for heavy boosts. You’ve got crossover frequencies, you’ve got highpass and lowpass, but the highpass and lowpass aren’t normal algorithms either: they’re designed for ‘trapping in’ already bandlimited sounds to get the most out of them. There’s a gate, but it’s an Airwindows gate where the release is designed to pull the audio back in the sound picture, not just volume-ramp it. There’s a time delay control that exists only to give the track a micro-delay relative to other tracks for groove purposes. And there’s the compressor… CStrip uses the ButterComp algorithm plus a speed control that lets you do odd things like increase the speed hugely. ButterComp compresses interleaved samples in Class AB, so that’s four independent compressors per channel. If you crank the speed under heavy compression you can get artifacts (for normal behavior, keep the speed a lot lower).

The whole idea with CStrip was to do the channel strip, but take it out into stranger realms where it can be used for various sonic destruction. It may not be the last of such plugins: some new stuff coming out is giving me ideas for other ‘combination’ plugins, especially ones where the algorithms can be interwoven to produce effects you literally couldn’t have out of discrete plugins. (one day, I’ll be open sourcing all of that and telling other plugin coders all about it)

CStrip also uses a technique I came to rely on, where if a component of the plugin isn’t being used (for instance, the lowpass and highpass when set to their extremes switch off) then it gets completely bypassed, and not even the math of the component is used: this is sort of like how ‘unity gain’ in code isn’t the same as ‘bypass’. (if you’re in floating point and you’re multiplying by 1.0, you’re also doing a math operation at a given exponent and this can wipe out floating point values at very different levels of detail)

But that’s getting too wonky: I hope you enjoy CStrip.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

CStrip processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/CStrip)

**Categories**: Utility

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Utility](../categories/utility.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
