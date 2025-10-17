# PurestFade

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

just like PurestGain, but for LONG fades

## Detailed Overview

This is a plugin for one person.

Okay, it’s a plugin that EXISTS because one person asked the right thing at the right time. A mastering engineer emailed me and said, PurestGain is great, it’s just perfect, everything I need except… when I do fades with it, there’s a discontinuity when I go from 0.001 volume on the Slow Fade, to 0. It cuts out abruptly, and that’s a problem. Can you help?

I can!

Thing is, PurestGain is designed so you can whack that control around aggressively. It doesn’t mute instantly, but you can kill a track real fast in a mix, gracefully, without zipper noise. PurestGain is correct for some users. If you needed to have a control on some kind of USB controller, like a NanoKontrol or something (say you’re doing an automation pass) you might well need to trim the overall gain with the top slider, and then assign the hardware controller to the bottom slider and automate. It’ll smooth out the incoming MIDI data and the result will be dynamic and aggressive, will feel like you’re yanking faders around on a real board. That’s the design intent for the ballistics of PurestGain.

PurestFade is totally different. If you are at full crank and snap it instantly to zero, you’ll get an automated fade of about eight seconds or so. It gets subtler and subtler the quieter you go, until at the point of silence you literally can’t mess up the fade: it will always smooth out the last tiny bit.

If you drag it slower than ten seconds you can do any slowness of fade you want, smooth as you like. And, an interesting thing is that if you need a faster fade than the automatic one (of just going fully to zero in an instant and letting the plugin do it) what you can do is manually drag it down faster than that. It’ll chase your fade speed, which means if you’re doing an unnaturally fast fade it’ll be trying to smooth you out a bit but it will let you do that. I think it’s the ultimate smoothed fade.

And, in mixing (since it’s still PurestGain at heart) I think you can decide which you prefer, and if you’ve got a style then you know which one is right for you. Probably won’t be both. If you need to do abrupt, dynamic things it’s PurestGain you’ll want… but if your fader moves are generally more subtle, invisible, then you’re probably going to always want PurestFade for everything. (The top control will still give you more rapid moves if you need them)

Which one is the right one for you? Most likely you already know which one you’ll be using, just from the descriptions.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PurestFade processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PurestFade)

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
