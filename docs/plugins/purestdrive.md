# PurestDrive

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Latest Release |

## Description

the magic saturation plugin of subtlety and French House tone

## Detailed Overview

The funny thing about PurestDrive is that I didn’t expect much from it at all.

This plugin (now coming to VST and open source) was simply an experiment. I’d been making complicated plugins with things like anti-aliasing, just a lot of calculation going on, and wasn’t sure I was getting what I wanted. It didn’t seem to be furthering the ‘Airwindows sound’. And I’d hit on an interesting tactic, noise shaping for the floating point buss. It seemed to me that you might be able to get a good sound by the opposite to complication: simplifying things, running the math at the highest possible resolution (in this case, long double precision, which is 80 bits on Intel and possibly 106 bits on PPC, which Airwindows still supports)

The saturation algorithm was going to be sin(), which is the smoothest saturation curve you can have. Then I thought it’d be good to get a little more sophisticated than that because I had quite a few plugins based on sin(), so I did this:

inputSample = sin(inputSample);
apply = (fabs(previousSample + inputSample) / 2.0) * intensity;
inputSample = (drySample * (1.0 – apply)) + (inputSample * apply);

That’s it. That’s what makes PurestDrive (apart from some code supporting it, which is up and documented on GitHub as part of making it open source).

What it does is this: it keeps the previous dry sample around, and ‘apply’ will be the combination of that and the saturated one. This makes apply be large if we’re on a low frequency wave, and if we’re doing a really bright transient apply might be zero. Intensity is how we include the slider control (0 to 1) and can also make apply be lower. Then, we’re adding the sin() effect, but ONLY relating to apply: we saturate the body of the sound, but as things get brighter or lower volume, we’re dynamically doing a dry/wet control at audio frequencies, so PurestDrive only throws saturation on dense solid material: airy highs, subtleties, get through more easily. As a side-effect, if our input gets super hot we can end up subtracting a little dry from the saturated inputSample.

What PurestDrive did… was take off and become hugely popular. I didn’t expect that, it was simply an experiment in tone purity and I didn’t think anyone would notice. I knew the little tweak with ‘apply’ sounded good, but I figured the whole thing was so subtle that it wasn’t going to set the world on fire. Yet, PurestDrive developed incredibly dedicated fans, using it all over their mixes, swearing by its tone.

And now, it’s a free and open source plugin, AU and Mac and PC VST. Remember it’s designed to not be a big obvious coat of paint over everything: because it’s using the dry sample so intensely, it cleans up and stays out of the way. But because it’s modulating between saturation and dry at audio frequencies based on both the current and previous sample, there’s a lot of textural effect on the sound. I never got so much mileage out of so few lines of code. Hope you like it. :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

PurestDrive processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PurestDrive)

**Categories**: Saturation

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Saturation](../categories/saturation.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
