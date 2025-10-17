# ADClip8

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Clipping |
| **Type** | Clipping |
| **Status** | Latest Release |

## Description

the ultimate Airwindows loudenator/biggenator

## Detailed Overview

The last time we saw an Airwindows ADClip, the full version rather than a neat and tidy stripped-down version, was October 8… of 2017. It's been more than six years since the king of loudenators saw an update, in part because ClipOnly got followed by ClipOnly2, which was such a good high-sample-rate clipper that it was all I needed for years. ClipOnly2 is still the cleanest, purest way to take small amounts of peak clipping to your signal: it's great as a safety clip.

But, while working on a new version tailored to the needs of Final Cut Pro (which is also coming), something new arose.

What would happen if the FCP version, which has a built-in slew clip and makes heavy use of Golden Ratios to arrive at its results, was adapted to a new ADClip? What if it was scaled to regular clipping levels, given a ceiling control to dial back its maximum to taste, what would happen if it was stacked up with a whole array of FinalClips in series like some of the other Airwindows plugins like to do? We're no longer dealing with ClipOnly2. Much like the original ADClip7, we're adding extra stuff and running a more complicated algorithm. But we've still got some of the special features of ADClip7, like the gain-matched mode and the Clips Only setting.

Enter ADClip8. It has more settings. They go Normal, Gain Matched, Clip Only… then, Afterburner, Explode, Nuke, Apocalypse, and lastly Apotheosis. No, really! That's the new settings.

What they represent is added stages, so Normal is a single stage (as is Gain Matched), Clip Only shows you where clips begin, and then the new modes are named for the sounds they produce, at two, three, four, five and six stages of special slew-clipped ClipOnly2 style sample-rate aware clipping. In practice, think 'bigger, bassier, thicker' as you continue to add stages. You may not always want to run the full six stages, you might want to voice it to your needs.

The interesting part is how all this affects intersample peaking. Because the process brings in slew clipping and repeated use of the ClipOnly2 algorithm, which resists harsh entry into and exit from a clipped state, dialing up ADClip8 and cranking the gain produces an intensely saturated sound that resists intersample peaking not through filtration, but mechanically. It will literally put in transition samples to resist the intersample peaks from going beyond regular clipping. The more stages, the more thoroughly it resists 'true peak'.

I would say don't use this for evil but who am I kidding. If you beat everyone with 'competitive loudness' this way, please never expect me to listen to what you did, I'll be hiding under my bed, regretting everything. :)

For what it's worth, 'Apotheosis' mode should also be a very nice way to do extremely moderate transparent clipping of challenging material: ClipOnly2 will still be more transparent but only sounds like a slightly brighter version of ADClip8 Normal mode. Apotheosis mode simply does more and I wouldn't blame anybody for preferring it. Hope you like ADClip8!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ADClip8 controls peaks and maximizes loudness through sophisticated clipping. Use it as a mastering tool or creative effect.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Clipping](../categories/clipping.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ADClip8)

**Categories**: Clipping

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Clipping](../categories/clipping.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
