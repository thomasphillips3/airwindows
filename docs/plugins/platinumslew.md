# PlatinumSlew



## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Stable |

## Description

the best easy-to-use slew clipper

## Detailed Overview

This is something I've specialized in for a while: types of processing that aren't common. Slew clipping is like what you see out of certain op-amps, circuits that can't keep up with high frequencies and are given semi-magical qualities having to do with just the right IC and so on. And you can program that, and I have (for instance my Channel plugins, or Guitar Conditioner).

And then I discovered, in GoldenSlew, that you could cascade slew clippings and it'd actually give you a unique sound, unlike just using one slew clipping.

And then it went beyond, as I tried to incorporate another previous sample and bring in the rate of change of the direction of the slew, and ran into strange audio bugs that were the digital equivalent of my circuits blowing up or short-circuiting, unable to handle what I was asking of them…

…and came out the other end with PlatinumSlew (and a plan for a more complicated, control-laden plugin where I can get really detailed control over everything that happens in the plugin).

The original Slew, and GoldenSlew after it, is a bit of an audio chainsaw. For instance, if you slam it to full crank it acts as a sample and hold, because that's literally what you get when you cut slew to 0.0: permanent holding of whatever voltage you had. Good for use in the VCV Rack port, not so good for subwoofers. So, don't use those for swooping the audio down to bass and then silence, especially not fast, or you'll trap energy.

PlatinumSlew explores a new space in slew clipping where its algorithms don't hold energy in the same way. But what does it sound like? It sounds like a record. It sounds retro. What happens is, you can control the transients of the high-end, but then as you push further, as it gets darker, it also begins to alter the subsonics, the bass… which is something I've never been able to do, not like this. It's not a filter, this is a clipper. But it's not clipping the bass… it's hard to explain.

Crank it way up and hear the odd things it does when you push it way too far… and know that you can bring in just tiny amounts of that very unusual, very retro, very vibey flavor. This tech is central to where I'm going with the new Console designs, as I come up with stuff that really truly sounds like classic desks. It immediately found its way into my music, taking my legit analog gear that last little distance it needed as post processing. It's mastering friendly if your tweeters and ears are good enough to hear its subtlest effects. And unlike the swiss army knife version I'm still developing, this one is one slider which can't be set wrong, and it's free and open source, and it's yours. Hope you like it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PlatinumSlew processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PlatinumSlew)

**Categories**: Brightness

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Brightness](../categories/brightness.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
