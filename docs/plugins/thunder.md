# Thunder

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

a compressor that retains or exaggerates subsonic bass when you push it

## Detailed Overview

Compressors are tricky little beasts: they tend to eat low-end, they react differently at low intensities than when you slam ’em, and each sort of compressor has a ‘voice’ that defines how it acts.

There’s a crude way to deal with the low-end problem, which is to put in a crossover: either to split into multiband compression, or simply highpass the sense circuit so the compressor can’t compress extreme lows and just lets them through. I’ve been asked to do this and have actually tried it on PurestSquish, but I was never satisfied with the results. It seemed like just half-breaking the compressor and I felt there had to be a better way…

Thunder is that better way. Instead of passing through the bass, it transforms it in a way similar to FathomFive, and uses that live, active signal to modulate what the compressor sees, where in turn the compressor’s output is modulated by the intense lows. It’s a little complicated, so you can watch the video or simply download it and try it. Thunder is free (bear in mind that my only compensation is the Patreon I’ve created. To do this onward into the future, that Patreon must succeed)

If you’re auditioning Thunder, a word of warning. You’re going to have to monitor the extreme lows. This plugin can prepare music for the hugest sound systems or the finest audiophile playback, but if you can’t hear what it’s doing you may get in trouble with it. Decent headphones ought to suffice (not earbuds!). If you have subwoofers, this will test them. You can also use the mix-check plugin SubsOnly to test how you’re doing, that will spotlight the subs for you.

The range of adjustment starts with gentle ‘glue’ compression as the subsonics begin to open up the mix. Then, a bottom octave will appear anchoring everything. Push beyond that and you start to get into more compressed 2-buss, with the extreme lows taking on a punchier, thumpier character. Add more Thunder and the bass gets frisky and aggressive and dominates. Then, when you go even beyond that, we’re talking about ridiculous monstrous mega-bass, and more or less wrecking the sound of everything else (it’s useful to be able to go to weird broken settings in case you want to step back just a bit and have a really extreme effect). This is not a multiband compressor (there’s only one stereo comp in the plugin) but when driven really hard it can go even more bonkers than a multiband compressor.

Remember, the low Thunder settings are useful too as a glue comp, for a buss compressor that’s extremely transparent and true to the tone of the mix! The middle settings are just as functional. All of these settings have their own usefulness. Choose wisely (or unwisely, if you prefer).

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

Thunder controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Thunder)

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
