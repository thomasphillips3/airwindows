# BlockParty

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Latest Release |

## Description

like a moderately saturated analog limiter

## Detailed Overview

What do you get when you cross an Airwindows compressor, with OneCornerClip?

Pretty much this. Okay, so it wasn’t a very difficult riddle, was it?

BlockParty acts like a somewhat distorty limiter. It’s not at all about lookahead (in fact it doesn’t have any) or preserving tones pristinely. Instead, it takes the onset of sounds that would compress, and manipulates the attack in the way that OneCornerClip does. The threshold gets kicked way down, and gradually expands to full scale, and since the threshold’s determining compression, that means BlockParty doesn’t have a stable compression threshold. It’s interactive with the audio you’re giving it.

Because it’s on the OneCornerClip model, that means it’s a mostly-compressor with OneCornerClip-like behaviors. That means bass which blooms and has fullness even under heavy load, and highs that don’t poke out or distract. The result is a thing that sounds real analog-y but not super clean. You can use very small amounts of it (there’s a lot of gain on tap) to do peak limiting for loudness maximizing, or you can slam things into it for effect. It’s called BlockParty because heavily limited stuff sounds like blocks of loudness: it’ll get you some of those sounds, but not as cleanly as your classic ‘loudness war’ limiters. It’ll also smash drums and things in its own distinctive way, which might be its strongest suit. On the end of it is a clipping stage to make sure nothing you do will ever produce overs. The clipping stage is AFTER the dry/wet, so to get a true dry you’ve got to turn it off: this is because raw digital clipping is another style of loudenating, so if you were going super-hot into BlockParty and wanted to dial in some pure digital clipping you could use the dry/wet to do it (or, if including some dry would have given you overs because your direct buss signal includes overs).

BlockParty is a fierce loudenator with a voice and style all its own, using techniques that are distinctly Airwindows. It might be just what you needed, or it might be a little too grungy for you… but either way, there’s nothing quite like it, so check it out.

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

BlockParty controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BlockParty)

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
