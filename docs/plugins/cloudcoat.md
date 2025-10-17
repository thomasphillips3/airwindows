# CloudCoat

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

an array of blur effects with a taste for evil

## Detailed Overview

Welcome back to the dark side of Airwindows!

CloudCoat starts as an experiment. What if there was ClearCoat (a bank of small reverbs) except all the delays were allpasses?

Okay, so a bit of explanation: allpasses are like reverb parts, but they make stuff sound smeary and blurred, like bloom reverbs. I've got a bloom reverb, MV, which is just a stack of allpasses. Most of my recent work is about avoiding allpasses completely by using reverb matrixes that give me LOTS of echo returns, impossible numbers, so I don't have to cheat with allpasses. This kind of works and kind of doesn't (work in progress, see my recent livestreams). But what would happen if you took what was clearly a reverb, and just replaced all the delays with allpasses?

That's ClearCoat and CloudCoat. The idea was I could give a completely different texture, but using literally all the same reverb constants, and then I could hear what it was like. I expected it to be more a cloudy, diffuse texture, hence 'cloudcoat'.

You might notice one difference right away: ClearCoat sounds a lot roomier. That's because it's designed with a little bit of feedback to fill it out. Sustain, if you will. It's also way more spacious, and way more metallic and ringy. This is in line with how it only uses delays, and is all part of the research.

CloudCoat with sustain all the way off, is quite different. Depth and spaciousness is almost gone, but there's no metallicness either. It's like essence of fake artificial reverb blur. Remember, this too is a 4x4 Householder matrix: it's a complicated pile of allpasses, not something primitive like MV. I think it might find uses on pads or ambient sounds, or could be used to feed into ClearCoat at the same 'select' setting to create a more powerful room sound. With sustain all the way off, you can do many polite and nice things with CloudCoat.

Then, throw it on some drums and turn the sustain up and ALL HELL BREAKS LOOSE :)

CloudCoat is applying a kind of nonlinear reverb, like your classic 'nonlin' gated verb settings, but Airwindowsized. I'm allowing feedback, but of the four 'channels' of Householder feedback, each is also modulated by the output of the one next to it (a totally different sound)… WITHOUT smoothing. So the feedback is broken up by four banks of allpass output and cranked up to the point of meltdown, and that's CloudCoat. It disrupts the signal wildly and fiercely.

Why?

Because I tried it, on a livestream, and the drums absolutely exploded like nothing I've ever heard. There's rasp and rattle and an effect much like extreme compression while in a stone drum room, but there's no compression and no stone room. It just makes that sound. Instead of making it out of compressed, flat-topped compression smash, it's making the madness happen INSIDE the sound, meaning you can make it brutal and unbearable with ClearCoat and THEN loudenate it, unlike any other sort of compression or distortion. CloudCoat adds a whole new type of trash that is dynamic with your sound (again, nonlin) and automatically dials itself back if the source energy level does. It's a huge, nasty, energy-laden meltdown that can be escalated to pretty much any degree… and then dialed back down again, to pretty much any level of controllability, so long as you're using it on noisy percussion and as long as you're okay with its signature trash-sound, which is not like anything else and which is independent of added compression and distortion.

And then you can do blur/texture effects with the sustain on 0. Just don't bother trying to make it work with tiny amounts of sustain: it basically can't. 0 or trash are your only options, and then there is a universe of trash and meltdown if trash you choose.

But seriously, why?

Because it makes me laugh with delight when snares go off like something out of the imagination of Trent Reznor. I don't know what to tell you. Enjoy CloudCoat, if it's the kind of thing you enjoy.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

CloudCoat processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/CloudCoat)

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
