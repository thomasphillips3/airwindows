# HighImpact

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Distortion |
| **Type** | Distortion |
| **Status** | Latest Release |

## Description

distorted grit and punch without fatness

## Detailed Overview

Sometimes it’s all in the name.

High Impact has been one of the Airwindows secret weapons for a long time. It’s a pretty basic idea: know how Density distorts and makes audio huge and fat, and Drive distorts and doesn’t make stuff as fat? High Impact answers the question, ‘what if you could distort and not make things fatter AT ALL’.

This is not EQ I’m talking about, though it can come off like EQ depending on what you feed into it. High Impact combines a distortion and anti-distortion circuit to reshape the transfer function of the audio, as follows: crank it up, and quiet subtle samples aren’t turned up much. Then medium samples are turned up a LOT, and then the loudest samples are distorted and hit a wall past which they can’t go. The result is an obvious distort which doesn’t bloat things. It’s a ‘dial-a-rasp’, or ‘dial-a-slam’ for percussive noises, and though the concept is two different kinds of overdrive combined, it’s an Airwindows plugin so it’s not overprocessed, it’s super raw.

That suits this plugin super well, and that’s why the AU-only High Impact has been a secret weapon for many people for years—and now it’s out for Mac and PC VST.

A word about the ‘secret weapon’ thing: I hate that. Do as I do, and communicate openly. Airwindows plugins are not preset things that you hide somewhere to add magic sauce to your mixes. They require intention, and there’s no one right way to use them: Airwindows plugins are like if a certain mic modeler you can rent that offers ‘silky expensive microphone models’ had just a blank ugly faceplate with just one knob, ‘silky’. And you could use it as a guitar stompbox if you wanted, not even a microphone anymore, and it was no longer connected to a ‘magic gear item’ so you’d have to ask, ‘HOW silky does this sound need to be, in my mix?’ because there was no one right answer.

That’s what Airwindows is like. For High Impact, read ‘raspy’ or ‘mean’ or ‘grindy’, whatever describes the sound for you. Now you’ve got an extra parameter: instead of just bass, treble, loud, soft (or even fat and thin) you’ve got ‘aggro’ on a knob. That can relate to any bit of audio you’re working with… and your ‘secret sauce’ is not the plugin, but your sense of taste (or tastelessness) in using and abusing it. So, don’t keep Airwindows plugins a secret weapon. I hate that. Tell people what you’re using, so I can get more supporters and keep doing all this, on a bigger and bigger scale.

Speaking of which, I have a Patreon milestone! As of a couple days ago, I hit $600 a month, and I’ve recently changed that to be the point where I start releasing the Kagi catalog! Now, people sometimes bail as the first of the month rolls around (and also I don’t get paid quite the full amount shown). So, it’s possible this milestone will go poof as we reach May, in which case we’re still waiting. BUT, if the dust settles and it’s still over $600 going into May, I will put out Iron Oxide 4 (the second most popular plugin I have EVER made) as free AU/VST!

(oh my God, I look so young in that video o_O )

If I’m still over $600 when May begins, you get THAT plugin free. My hope is that, as I reach this stage, people get more of an idea of what’s possible out of my Patreon project. All this time, I’ve been putting out more than 47 plugins entirely from the ‘freebie pile’, and not touching the ones that kept me in business a decade. Now, we start to get into the serious ones, the ones worth $50 to a lot of people. I’ve even drawn up a timeline on the Patreon, showing when each plugin will come out if I stay above $600. (if I clear $1000 they go twice as fast and I’ll revise the timeline accordingly!)

Here’s where things REALLY get interesting. Hang on to your DAWs, because we’re about to go full warp drive :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Drive]
    B --> C[Waveshaping]
    C --> D[Filtering]
    D --> E[Output]
    style C fill:#f59e0b
```

## How It Works

HighImpact adds harmonics and edge through distortion. Use it for adding grit, warmth, or aggressive processing.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Distortion](../categories/distortion.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/HighImpact)

**Categories**: Distortion

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Distortion](../categories/distortion.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
