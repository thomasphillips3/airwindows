# Recurve

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

a special buss compressor with no threshold point

## Detailed Overview

Sometimes the most amazing things are the simplest.

Recurve is ONE line of code (per channel) plus a bit of implementation. It’s a compressor, and this ‘preview’ look at it is a lot like when Spiral came out: this is Recurve as a ‘black box’, set up for maximum explosiveness and impressiveness. (I’ve got more elegant plugins in the works and this will become a core technique due to its effectiveness and simplicity of coding, so this is the introduction to what the algorithm does)

Recurve works on principles similar to Spiral. It’s using a very high resolution sine calculation to affect the sound, and scales part of itself relative to the loudness of the sample it’s on. It also enjoys similar principles of ‘no sharp transitions, ever, for internal calculations’. In a clipper that means the rate of curvature doesn’t abruptly change, which is the principle behind Spiral. For Recurve, this is applied to the threshold of a compression and whether gain is being turned up or down.

If the signal is super-quiet, the gain doesn’t change. Recurve takes moments of space and ambience between loud sounds, and preserves their character. It doesn’t swoop up in volume: if you need sidechainy pumping, you have to use something else.

If the signal is medium, the gain gets turned up until it hits its max (with Recurve, it’ll exactly double the gain, which is BitShiftGain at its smallest increment. Exactly 6dB of very clean gain boosting things. This isn’t at a threshold: it’s at the most intense spot of a sine curve, so as a waveform passes through this zone it’ll increment the gain smoothly and without any transition points.

If the signal is loud enough, it pushes this curve back through zero to its most negative point, and the sine function delivers a -1, for the maximum gain-cut, which is also scaled by how loud the sample is. So Recurve can cut back an over-loud transient FAST. In fact everything it does is really fast because the lack of transition points and the gradual nature of this sine-triggering lets it react very efficiently without edginess. It also lets through sonority and projection but cuts dull and muted stuff, kind of like Pyewacket, but without Pyewacket’s inherent pointyness.

Sounds complicated? Just listen to stuff and switch it on. This is a preview in extra-dramatic form of an algorithm that’s going to find many uses in Airwindows plugins. It’s the compression equivalent of Spiral for saturation, and it could be adapted in many ways.

The way you get today is a buss-comp or limiter form, running in true (linked) stereo. Mix into it and Recurve will gracefully eat up whatever you send it, even if you push it real hard. There’s a built-in 6dB of very clean boost to show off what it can do, and there’s a clipper on the output in case you get carried away and want to slam it so hard that transient attacks might poke out. And because of Recurve’s curve-and-recurve gain adjustment style, you’ll get none of the usual compression pumping and breathing: it’s just plain different. I hope you like it. There will be more :)

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

Recurve controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Recurve)

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
