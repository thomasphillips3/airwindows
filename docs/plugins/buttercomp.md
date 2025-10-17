# ButterComp



## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Stable |

## Description

my softest, smoothest compressor

## Detailed Overview

Sometimes a plugin can be a sort of cult favorite. That’s the story of ButterComp, a compressor of great subtlety that’s no use for quite a few normal compressor tasks… but still has a fervent following. I’ve been begged for the new version of this one (not merely VST, but revamped with all the current Airwindows sophistication and purity) and I’m delighted to bring it, though I think it might puzzle some people. If the stock Logic comp would do as well, this isn’t the plugin for you. But if you’re looking for a certain thing and thought it unattainable in software, this might be your lucky day.

Buttercomp, under the hood, is absolutely unique (or unique, until I start working on variations and until other people try to copy it. They’re free to, but it’ll be possible to test that quite easily with special audio files).

It’s a bipolar, interleaved compressor (with rather slow attack and release: a version with access to much faster dynamics is available in CStrip). This one’s the original, the cult classic. What is a bipolar, or an interleaved compressor? For the purposes of Buttercomp, it’s four totally independent compressors per channel. Two are sensitive to positive swing, and flip back and forth every sample. Two are sensitive to negative swing, also flipping back and forth every sample. The compression factor’s reconstructed through combining these poles, through the screen of the interleaved compressors switching back and forth at the Nyquist frequency… that mysterious digital frequency that is on the one hand the literal highest frequency that can be encoded, and the lowest frequency that ought to be totally rejected and filtered out.

What happens is this: the tone of things gets some added second harmonic, wherever the compression is more strong on one side than the other. High frequencies take on a particular airy openness, since they too get second harmonic, plus individual sample spikes can only affect one out of four compressors: ButterComp deals with all samples only as samples relative to other samples, and doesn’t get thrown off by isolated samples that don’t represent the actual waveform. It’s got a sound, but the sound is hard to define because of its extreme fluidity and purity.

If this sounds like your idea of fun, enjoy ButterComp. If you’re looking for the ‘all buttons in’ mode, I’ll get back to the drawing board and probably do something totally different for you. This compressor is not for everybody. Also, if you start slamming it really hard (demonstrated in the video), it’ll volume invert: you can squish it down to become more quiet than the quiet passages, but still it will retain its tone quality. It’s perhaps best used as a particular kind of ‘glue’ compressor, at which it is exceptional… or maybe I should say, it’s unique. Start working with it and you’ll soon work out whether you’re part of the ButterComp cult. Not everybody will be, and it’s only one type of sound… but nothing else can get that sound, and this is why I’ve kept this purest form of the algorithm available.

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

ButterComp controls dynamics through compression. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ButterComp)

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
