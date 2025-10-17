# Energy2

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

electrifying fixed-frequency treble boosts for high sample rate

## Detailed Overview

Energy2 is energy boosts. Mostly treble, but you can also bring out aggression in the high-mids. These are NOT done through usual means. They’re a weird little algorithm that’s tied to the sample rate, and the big deal with Energy2 as an update is that it’s using my undersampling (which I just recently improved) to function as intended at high sample rates: it’s also more CPU-efficient than the original, but otherwise it’s the same (the original Energy might still be preferable for some, for instance if you absolutely must work at 48k and find it works better for you than Energy2 at that rate).

When I say energy boosts, what I mean is: this is not a normal EQ. You could not make the Energy2 sound happen by mimicking the frequency curve using a pile of biquad filters, or worse yet phase accurate EQ. It’s an entirely different algorithm, and this is what you get. Energy2 has enormous edge and focus around attack transients, not smearing them with pre-ring or high-Q traditional filtering, even though it produces very steep curves and isolates specific tones. Energy2 also has a definite color in how it adds frequencies: if you’re boosting upper mids with one of the lower sliders, you also get a bunch of highs along with it. Part of the sound. Probably shouldn’t struggle to remove those overtones too hard.

You can combine the sliders in weird ways to get very striking tone colors, but I think Energy2 is at its best when you focus on one color at a time, perhaps with a little of another color added or subtracted (less than zero means taking that tone color out: but remember, this is Energy2, it’s never completely tame or predictable). The breakthrough with Energy2 is that it’s designed to run at elevated sample rates, undersamples its boosts, but unlike the original Energy, it mixes that with a NON-undersampled Dry to get best of both worlds: the exact tone colors it ought to have, but against an unaltered, hi-res background. Since Energy’s generally able to get obnoxious levels of boost, the thing to do is get sounds where at least one slider is cranked out as far as it’ll go, and then use Inv/Dry/Wet to use only as much of that added energy as you need.

You get high and upper mid boosts, all the way up into the highest of air bands, that are more like they’re part of the original sound and not even added using EQ at all… but complete control over how much of that is added to the fully high-resolution sound at elevated sample rates. (and at CD rates, it works just like the original Energy, but with the CPU enhancement from not processing unused bands, plus the Inv/Dry/Wet is run at a higher word length than before, and uses modern Airwindows dithering to the floating point buss: that’s how old the original Energy was)

If I make a special Airwindows 96k mixing kit, like Starter Kit but more for experts adopting my mixing system rather than beginners, Energy2 almost defines what that would be like. It’s a very strong way to get a more Airwindows-y sound. (It’s also a nifty sort of anti-Soothe: nothing will pop out vibey overtones, intensity, and sonority like this plugin)

Hope ya like it. It’s one of the special ones. :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Energy2 processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Energy2)

**Categories**: Effects

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Effects](../categories/effects.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
