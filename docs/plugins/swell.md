# Swell

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

Dial-an-attack, like sidechaining

## Detailed Overview

Every now and then you come up with something a little different. The fun of that is in identifying it.

I’ve been listening to house music by Deadmau5, and I took an interest in the way the sidechaining worked. (That’s the way the music, or the reverb, or the pads, get ‘smooshed’ down by the kick drum and then swing back up in volume again.) The Mau5 is pretty good about talking about his techniques, which I appreciate (I’d love to do a coffee run with that guy someday) and he’s spent some time showing people how instead of actually sidechaining, he automates an LFO which he applies to track volume. It gets a great effect.

I wondered whether it’d work to do a gate that intentionally opened real slow. Specifically, it seemed possible to treat ‘full volume’ as a ‘floor’ and have a ‘decay’ that falls up toward 1.0 rather than down to 0. It’d never quite get there, but it could have a similar envelope as the fall-off of natural reverb, just upside down.

If that sounds odd, don’t worry about it, just try Swell. It has a threshold like a gate, and the Swell control handles the attack speed once the gate opens. The dry/wet works as you’d expect. Sort of like Deadmau5’s LFO trick, it doesn’t have to be a real sidechain, and is independent of whatever kick you have going on. Unlike the LFO trick, it’s also not tied to tempo: Swell reacts to EVERY attack that comes along, provided the threshold’s set right.

What this does is very interesting. I expect to see this turn up in an EDM channel strip at some point. Essentially, you can play with the controls in various ways and completely step on the attack of anything you want. This relates to GROOVE and the layering of stuff in a dance mix: any element, no matter what it is, can be turned into a pad and back again, just by squishing away its attack. You can do it live, you can take an element (snare, punchy chord) and manipulate how it hits inside the groove. Extreme values make stuff extra soft and quiet and squishy, and then if you drop the threshold or Swell, you can have the element jump right back out again, and the control is direct, not relative to a sidechained track or LFO setting. It’s a more organic approach, more hands-on, and I think it’ll fit into a lot of people’s mixes. There’s always a place for balancing the intensity of the attacks of your tracks, and that’s literally what Swell does.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Detector]
    B --> C[Gain Computer]
    C --> D[Gain Reduction]
    A --> D
    D --> E[Output]
    style C fill:#6366f1
    style D fill:#f59e0b
```

## How It Works

Swell controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Swell)

**Categories**: Dynamics

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Dynamics](../categories/dynamics.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
