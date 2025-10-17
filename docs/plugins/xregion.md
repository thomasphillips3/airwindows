# XRegion

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | XYZ Filters |
| **Type** | XYZ Filters |
| **Status** | Latest Release |

## Description

distorted staggered bandpasses, for extreme soundmangling

## Detailed Overview

XNotch too normal for you? HERE YA GO :D

XRegion is made out of bandpasses, like XBandpass, and if you keep the First and Last controls set the same it does act like an increasingly manic bandpass.

But, if they’re set differently and the Nuke control is up (engaging more poles of filtering) here’s what happens: first we go into the First bandpass, distorting before we filter (turns out if we make these filters glitch out the result is just too predictable) and then we go through each successive bandpass (up to five) each of which goes a step farther towards the frequency setting that’s in Last. We’re covering a region, we’re spreading the response out.

But we’re also distorting, each time.

So, if First is a higher frequency than Last, we get progressively lower pitched bandpasses and a sort of thick, roaring, dense tone. But if Last is a higher pitch than First… we’re starting with a bassy distort, and then filtering out the SOUND and keeping only the DISTORTIONS. Oh, and the farther apart you spread the controls the more gain it uses.

So basically this is raw industrial mayhem. It’s so bonkers you can use it inside uLaw and the result won’t even be crazier. In theory you can use this to get a really intense bandpass effect, for instance distorting a snare or something, and carefully control the gain and ‘Nuke’ (less of that means less bandpasses, and it won’t go all the way towards ‘Last’ anymore). But you can also just go nuts with it for some filter-sweepy, very distorted effects that won’t be like anything you’ve heard. I suspect the ‘nice’ uses of this will be much more limited, though in theory it should be as good at those as XBandpass is (to get a nice smooth distort, don’t spread First and Last too wide, or set them too high or too low, and balance the result with Dry/Wet)

There are a lot of people who won’t need this… at ALL. For those who do… hope you like it :)

As an aside, XRegion can do a really killer overdriven bass amp kind of a tone.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

XRegion processes audio in the XYZ Filters category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [XYZ Filters](../categories/xyz-filters.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/XRegion)

**Categories**: XYZ Filters

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: XYZ Filters](../categories/xyz-filters.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
