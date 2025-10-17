# Gatelope

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

a special gate that applies filters

## Detailed Overview

Gatelope was initially developed for Ola Sonmark, to solve the following problem: can you gate a tom mic in such a way that it rejects cymbal bleed, but lets the lows sustain longer, and then transitions into silence gracefully?

It just so happens that in developing that, I also wanted to do the opposite: reject low frequency rumble and sustain the highs more. I thought it might be useful for tightening up spot mics on kick drums. And the result… does both those things, and anywhere in between, and various other effects besides. It’s existed as a secret, Mac-only, AU-only weapon for long enough. I didn’t want to wait any longer, so enjoy Gatelope now (the Mac AU build contains an extra plugin, Gatelinked, which works like the VSTs: Gatelope in AU is ‘N to N’ and meant to be used on mono tracks, and the VSTs and Gatelinked are exactly the same, but linked stereo to prevent the stereo image from going to the side randomly)

The way to use Gatelope is, find the proper gating threshold with the top slider. Attack Speed might help depending on where you find that point. Then, Treble Sustain and Bass Sustain can be reduced to let the gate start gating. If you reduce Treble Sustain, it will be opening fully on an attack and then rolling off the treble as it closes. If you reduce Bass Sustain, it'll be rolling off bass as it closes. When these two roll-offs sweep past each other, your signal is gated and quiet: use the dry/wet to make the effect be at a lower ratio and let through some natural sound.

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

Gatelope controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Gatelope)

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
