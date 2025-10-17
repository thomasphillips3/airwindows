# Pop3

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

the dynamics from ConsoleX

## Detailed Overview

As I work on all the things that go into ConsoleX, now and then it becomes useful to give you a little preview. Pop3 is like that. It's the latest Airwindows compressor, but also gate, this time.

I hope it's pretty simple to understand, because in ConsoleX you get two of them per channel/buss, one for the Fire band and one for the Stone band. (if needed, I'll put out a StoneFire compressor to help you practice that). In this case, it's a fullrange dynamics processor tailored to my needs with ConsoleX.

For the compression section, Threshold brings down the squish. It doesn't use makeup gain, so you use it to restrain the sound. Attack and Release work as you'd expect, though Pop3 runs a new sense circuit that's very transparent in action. The Ratio control is simply a dry/wet: if you have signals peaking really hot, over 0dB, you'll have to set Ratio to 0 to truly bypass the compression. Since this'll be available in multiple places on multiple bands it's designed to be more a 'glue' type, though you can run audio really hot into it in order to get an exaggerated result. In the final version you use the Stone and Fire controls to boost post-compression if you want.

The gate section had to be designed into Pop3, like it is in ConsoleX. It triggers off the uncompressed signal, so whatever you do with compression has no effect. It uses its own threshold (coming up from zero) with a release that goes from slow to brutally fast, and a handy Sustain control which stretches out the gating to control whether it's sputtery or crisp. This gate is good at tightening things up, especially with the sustain feature there as a primary control, and again: works totally independently of the compressor, so you can sculpt those dynamics (or put percussive bumps on things using the gate ratio to dial in the spike and then blend it with the regular signal) and then shape your primary audio to make it more squishy. I found that just kicking in the compressor slightly gives a huge change in texture compared to only using the gate.

I wanted it to be extremely approachable because you deal with two of them in parallel in ConsoleX, and not even with a normal crossover, instead with multiple Kalman filters and a set of parametrics that bypass all the compression (but which are in fact gated, but the different parametrics and the Air band respond to different gates).

The glimpse of ConsoleX interface is only a rough draft: in particular, I gotta add user control over whether that 3D effect is on the knobs at top and bottom. Some people will prefer it flat, some will like the extra room provided by some of the knobs being seen edge-on. Also I have a lot of work to do on the dynamic positioning and reflowing of controls, perhaps with some divider lines to help highlight which knobs went where. Suffice to say, all my days and all my attention are focussed on this now, and I hope it comes out (right now it's not running properly in my DAW Reaper, so there's bugfixing too)

Talk to ya later, and I hope you enjoy the chance to come to grips with Pop3.

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

Pop3 controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Pop3)

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
