# DubPlate2

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

like an ITB mastering house for electronic music

## Detailed Overview

By request, more DubPlate… and new instructions on how to get this sound.

Turned out the audio reference I used to chart a path from digital audio master to the sound of that very dubplate, wasn't as simple as I'd thought it to be. I didn't have the real master… and then, when I was fortunate enough to get it, it turned out there wouldn't be a simple way to go from that to the correct sound. The plate had been cut from an earlier mix, and the mastering engineer had complained about how bright it was, and applied more than a bit of EQ. That meant I couldn't treat it like it was a simple one-step process. I'd have to build in an EQ to do what the engineer did, before I could apply the same stuff DubPlate used. On the bright side, that would let the 'lathe' be cleaner, less aggressive. But there would have to be controls that matched what had happened to my reference in real life.

But there was an EQ I hadn't revisited for a while… that turned out to be just right for the job. My Baxandall EQ had gone to version 2 already, stripping out some early 'analog effects' I'd used in the first version.

Turned out that adding an input trim control, adding the analog effects back again (I'd used the Console5 processing for this), running this into DubPlate and readjusting it using the real reference audio but this time also doing the EQing and then compensating for the changes that no longer needed to be handled by the lathe… got me what I'd wanted in the first place.

Provided, that is, you operate it properly… so here's the new version of how to get a dub plate sound using DubPlate2.

Firstly, if your audio is perfect and you run it flat, you only need to pad it down with the input control until you have NO, repeat NO clips. The processing even without EQing can produce overs. Baxandall3 (built into DubPlate) is able to peak some way hotter than 0dB, to the point that you'd need a safety clipper like ADClip8 or ClipOnly2. Do not use one! Don't use a limiter, or anything like that, just pad the Input until there are no clips at all on your output.

This is important because you can't put a safety clipper between your audio and the lathe. The corners produced by a clipper are hell on lathes, high frequency energy that can burn the cutting head right out. The EQ and things like the elliptical filter and normal highpasses that are part of the circuitry are able to rearrange your audio a bit, stopping it from having the digital clips and brickwalls it might have, generating smoother peaks that don't follow the usual digital rules for where energy sits. To get a real dub plate sound, get your loudness through midrange, not through clipping the peaks.

But you have an EQ, so what if you need to use that? It's a very gentle filter, Baxandall3. You can certainly lift the highs or lows, or indeed cut them if that's what you need. The thing is, you have to follow the same rule. Even more so, as Baxandall3 is an analog-style filter that's capable of saturating when pushed! You can add deep lows to work around the bass loss from the lathe and elliptical filter. This will only get you so far, plus you'll discover that it eats up your loudness without giving you that much in return. You can add extreme highs, and the same thing will happen. You'll be fighting the lathe all to produce a more untrackable record that won't even be loud… since, remember, you have to pad the level until it doesn't clip. Otherwise you'll automatically not get a dubplate-type sound.

So, think in terms of midrange, allow the record to act like a record, and you should be able to get your ideal dubplate sound out of DubPlate2. You can use Meter to really dial in your results, but even without it the work should be pretty straightforward. Let it give you the sonic peaks your sound deserves, and DubPlate2 will be able to do its job :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DubPlate2 processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DubPlate2)

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
