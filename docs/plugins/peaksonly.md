# PeaksOnly



## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Stable |

## Description

a transformative mix check tool

## Detailed Overview

PeaksOnly is a mix check, like SubsOnly and SlewOnly before it, or Silhouette and other even stranger plugins. You pretty much need to not master through this one :D it totally wrecks the sound. BUT, it telegraphs information you might never have had, makes it more obvious than it’s ever been before.

Here’s how it works. PeaksOnly runs a little pile of allpass filters, but rather than just make them nice-sounding, it expands and expands and expands them, each time phase-rotating things a little more. It turns transient attacks of any kind into a little colorful wash, a flag of energy that stays at roughly the same level, but gets smeared out across time in a way you’d never normally hear.

Why does this matter? Because you wouldn’t hear it. Especially if you’re trying to work on headphones, brief sharp transients can become almost totally invisible, especially if they’re being peak-limited or get blended in with other sounds. That stuff can make your mix come alive, but how do you balance it? And if you’re on headphones, forget it: some peaks are just too brief, and unless you have a strangely powerful sense of energy levels that are normally invisible, there will be no managing the stuff that you simply can’t hear, the spiky intense sparks of audio like you get from passionate performances or tricks like using compression to spike up attack transients.

But with PeaksOnly, everything stays at exactly the same frequency balance (a trick of allpasses, especially mine which are prime-number spaced) but the bursts of energy, no matter how brief, get transformed into recognizable signals. If you’re short on transient impact, you’ll notice it. If you’re over-squashing attacks, you’ll end up with audio porridge. But if you’ve got a powerful, kicking, lively mix… every detail of it will be laid bare, turned into a sort of pantomime that exposes every transient at every frequency. Whether it’s how loud to make that snare or hi-hat, or how much sub-kick you can get away with, it’s all exposed. PeaksOnly is particularly fond of taking excess subsonic peaks and distorting ’em: you’ll never pack too much into the subs again.

It also tries to keep you at a sane loudness level (suitable for sending to mastering, if you really think you need to loudenate). Strangely, if you feed ‘mastered’ loud stuff into PeaksOnly and tolerate the distortion, it still reveals everything: there’s a difference between good ‘too loud’ and bad ‘too loud’, and PeaksOnly exposes that too. Anything out of balance, even in loudness land, will stick out.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PeaksOnly processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PeaksOnly)

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
