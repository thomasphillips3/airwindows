# Point

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

an explosive transient designer

## Detailed Overview

Point was introduced in 2007, just ahead of an amazing series of spatializers, analog modelers, and stompbox-style FX that consumed months of work. The curious thing is, Point didn’t. It’s one of those odd plugins that only required an idea: ‘what would happen if I did this?’, and an afternoon of coding. And ever after, it’s lived on as a mysterious and untameable plugin monster, secret weapon and mixer’s friend, always just as an obscure Audio Unit…

…until now.

You get three controls: an input trim, the Point control, and a reaction speed. Point goes from -1.0 to 1.0 and ‘dry’ is 0.0. Reaction speed goes from 0.0 to 1.0 and there’s nothing to particularly suggest where anything should be set, so I’ll tell you now, and I’ll also tell you where NOT to set it if you know what’s good for you.

For squishing off the fronts of snaredrums to make them huge, use Point -1.0 and a reaction speed around 0.166.

To spotlight cymbal attacks while rounding the drums, use Point -1.0 and a reaction speed around 0.14.

To hype up kick drum attacks and suppress the sustain in a gatey sort of way, use a reaction speed of around 0.3 and carefully add positive Point until you have the effect you want.

To blow up the DAW and kill your ears, do that and crank Point to 1.0, then stop the transport, and then start it up again with Point still at 1.0…

That’s your warning. Point is kind of like a ZVex Fuzz Factory or some such mad hardware device: the range of settings DOES include ‘out of control’, and it’s such a simple ‘circuit’ that it does little to restrain things when you Go Too Far and operate it in a state that will explode. It won’t just do it out of nowhere, but don’t make it transition between ‘off’ and Point 1.0: even if you have the fader buried, it can still clobber you.

The reason I leave behaviors like that in there, in a plugin like Point, is that some people will want the full range of Point’s output, and will be following it with something to manage Point’s outbursts. If you’ve got it surrounded with plugins to tame it, I want you to be able to use Point settings near or at 1.0, and if you set it near that, you’ll immediately hear how intense it’s being so it won’t come as too much of a shock to discover it’s become an unstable isotope of transient destruction.

:)

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

Point controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Point)

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
