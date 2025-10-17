# Trianglizer

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

a special waveshaper that can transform sines into triangles

## Detailed Overview

This should be interesting. It's a waveshaper with a couple unusual tricks. Meet Trianglizer.

The first thing it can do is turn full-scale sines into triangle waves… sort of. The slope on the triangle wave is slightly inconsistent (because there isn't a magical math function to make the sine into a perfect triangle, it's just a side-effect of something else). It's all a product of some work I did refining the algorithms of Console 6 to improve their accuracy as they do a zero crossing, which is constantly when music is playing (whether or not the music is loud, it all centers on zero and issues around zero crossing produce class B distortion in tiny amounts)

The thing to note here is that, while it wants full scale sines for a sharp point on the triangle, if your sines aren't that loud, what it will do is instead make a triangle wave with a round point. The point gets sharper or rounder depending on how loud the wave is. That means it's a dynamic triangle, like there's a filter, except it's getting synthesized without one.

Plus, it's a waveshaper, so it doesn't care if you have a sine or anything else. It'll just reshape the wave for you. Then if you're not done, you can adjust the 'tri/fat' control and it'll do the same thing except it widens the top of the triangle into a rounded-top trapezoid wave, adding a different kind of saturation beyond simply clipping, while keeping the same slightly inconsistent 'triangle wave' angles, through zero crossing.

But what does that DO?

Turns out we are applying two different shapes to get our result. The loud stuff mostly gets turned down (though with Fat engaged, it's turned up to make peaks thicker and hotter). There's a place in the waveform where the level remains exactly the same, and all the transitions between these points are super smooth. But as the sound gets quieter still… that, too, gets turned down. The slope of the waveform remains totally smooth, but it's a shallower angle than the sine that feeds it, and even shallower than what a true triangle wave would give you (subtly including some dry signal might fix this).

And so, we have an effect that dries up fat siney basses and makes them more articulate, cutting the level a bit, when it's on Tri. On regular music, drums etc. it does likewise. Stuff drops back and becomes more dynamic, with the hottest peaks poking way out in spikey form. It'll make things more crisp and defined.

But the really interesting part is when you set it to Fat, and begin using that for added beef and slam. Because when you're doing that, you're doing the loudness saturation… but your quietness is simultaneously dropping back. So you get a super-dynamic retro effect that to me sounds like old Kinks albums or something: it's distorted, it's loud, but it's all punch and no wallow. Unlike just using sine functions to make everything super fat, this purely adds muscle and some variation of it is probably going to find its way into a retro Console emulation from me. It's that good at conveying Fifties and early Sixties sound, where everything was intensely dynamic yet weirdly opaque and dense and the sound was felt as much as heard.

Or, you could just play with it and see what you get :) I am only trying to interpret a new plugin I didn't have before, which is kind of like my old High Impact plugin, but using a far more elegant algorithm that could have all kinds of uses.

Just remember: set to Tri to lean out and point things, set to Fat for guts and punch while still leaning out things, and use the dry-wet if the effect is too strong. It handles the loud and soft parts separately while handling them at the same time with one very smooth and accurate algorithm. It's a mystery to me too, but I think it will find many uses as a sonic muscle-adder. Enjoy!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Trianglizer processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Trianglizer)

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
