# Ditherbox



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

a switchable selection of dithers in 16 and 24 bit, plus monitoring tools

## Detailed Overview

This one’s fairly simple to explain. It’s (nearly) every Airwindows dither plugin in one box, with a control to select between them.

Well, there’s a bit more: Ditherbox comes with 16 bit versions built in (the individual plugins are based on 24 bit, with the exception of NotJustAnotherCD). So rather than messing around with BitShiftGain (which will still give you any weird bit depth you could wish for) you can output to CD-quality 16 bit directly from Ditherbox. That was kind of waiting for Ditherbox to come out, didn’t want to steal all of its thunder.

Oh, did I say thunder? Ditherbox also comes with monitoring tools: calibrated SlewOnly and SubsOnly playback, where it’s supposed to give you roughly the same levels and dynamics from full bandwidth, SlewOnly and SubsOnly. Might not be exactly the same, but if one of them is wildly different from the full bandwidth you might have a look at the mix.

Lastly, it has a new trick: Silhouette! The idea behind this one is simple: calibrated noise replaces your mix. If you can still hear beats and dynamic behavior, or best of all if your music is kind of recognizable, it’s a good sign! That means your mix is communicating information dynamically. If it’s just a wash, you might want to look at your overcompression or over-limiting, because especially now in the days of replay gain, it’s good to leave the ability to communicate with dynamics and not squish everything too much. It’ll also tell you things about how spikey your compression peaks are, and the dynamic texture of your drum impacts.

This plugin marks the open-sourcing of everything I’ve ever done dither-wise, including the Benford Realness-based Not Just Another Dither (named by the internet!). Seemed sensible, as they are all included in Ditherbox (well… actually the TPDF-based stuff like TapeDither, NodeDither, PaulDither, DoublePaul didn’t get included as they weren’t in the original Ditherbox. I’m kind of exhausted doing this one and VSTing it and opensourcing everything: there was a lot of fussy porting work and barely room to move the slider on the VST: forgive, plz?)

Anyhow, with MOST of the Airwindows dither work represented, hopefully this is fun to fool with. I do still recommend Not Just Another Dither on general principles, as in practical terms it’s the best one. You can still put TapeDither on outputs going to a mix, I’m just saying, it all culminated in NJAD.

As a follow-up in 2022 (not 2018, when this came out), Ditherbox is somewhat out of date. The version of NJAD in it isn't the most current: Monitoring has a better one. Monitoring also has Peaks, which is superior to Silhouette at the task Silhouette is for. One of the reasons Ditherbox still exists is, if someone got into it and REALLY liked the version of NJAD in there, it's all very well making improvements but I should keep unaltered versions of things. And that's what Ditherbox is now: it's not a go-to in my opinion, but if someone was depending on it, it got through a series of additional ports (like to signed AU and VST for Mac M1 processors, native) without anything about it changing. This has value of its own.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Ditherbox processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Ditherbox)

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
