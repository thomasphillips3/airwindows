# Preponderant

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

Airwindows Anti-Soothe, a strange tone intensifier and balancer

## Detailed Overview

Sometimes, it’s just… strange.

Preponderant was created in an attempt to combine the old ResEQ concept with Soothe, in such a way that it’d give you three tightly controlled bands of emphasis (one thing Airwindows is all about is maximizing resonant sonority and intensity, not blindly removing it) and then also balance them on the fly so that all the bands would tend to be constantly active. This would bring up the high band, for instance, giving that ‘hyping of detail’ effect. In theory, it’d work.

And maybe it does. But I don’t blame you if this one just drives you crazy and makes you mad. I had to scramble to get rid of an extra 24 dB of gain on tap for each band because when I started making the video, the plugin went insane and started blowing up: I thought I could let it throw in extra energy but I was sorely mistaken. One hasty bugfix later, we have… something? We have Preponderant. There is thankfully nothing else like it anywhere :D

Turn up Resonance and Wet to hear what it’s focussing on. Use the Narrow, Medium and Wide controls to dial in frequency bands: each is twice as wide as the previous, so using Narrow will give you the tightest focus on a frequency range. Set ’em to areas in your sound (middle is the midrange). Preponderant is named because it can be tuned between areas of preponderant energy, and areas of power or areas of no energy, and it’ll compensate to give about the same output for each band you select, no matter how much energy is ‘supposed’ to be there. It’ll boost quietness, suppress intense resonant areas that are much louder than they should be, or you can simply tune to a different frequency range and avoid the resonant stuff.

Also, it’s not a compressor. In no sense is it turning down louder stuff, or up quieter stuff. If you put it on drums you’ll scream in horror (unless you know exactly what you’re doing and have other drums to fill in a more continuous sonic flow). It’s rapidly balancing the bands while keeping the dynamics just as they are. Might be good on spot mics, toms or kick or something. Horrible on room mics or overall mics. Good on heavy guitar stems as it’ll retain dynamics there. It will be immediately obvious whether Preponderant is working on a track or stem.

You HAVE to pick real audio for every band, or it will just make some up. Subsonics on a skinny guitar? It’ll turn down the other bands until it thinks they balance with whatever subsonics you selected. By the same token, ice-pick zone on the same guitar? It’ll make it balance with the other bands you chose.

This will sound terrible. So, turn down the resonance until the sound is less insanely resonant. It’ll still sound terrible. Turn the dry/wet right back to dry (which will probably sound real boxy and dull by comparison).

Then, feed in a little of the Preponderant, just until you start to hear it accentuate the stuff that you chose.

THERE you go.

Preponderant is one of those Airwindows audio chainsaws. The final version (without the 24 dB boosts) is intentionally made to just cut and restrict stuff, explicitly so if you don’t know what you’re doing you’ll hate it and not use it. This is intentional as you could hurt your mix, your ears, and your sensibilities.

On the other hand, if you know how to dial in areas of power and focus and find three things about a sound that are useful in the fray of a mix, I’m not sure I’ve ever made a plugin that will so aggressively give you what you ask it for. (and if that’s not enough, a few of you will want to use the original version. I’m not going to encourage this, and you must choose: that or the real, volume-cutting version. They install with the same name and the same ID so you can’t have both, and shouldn’t have the boosty version, ever. But if you want to blow up your mix, then YES, you may. The rest of you, and me, please work with the one that doesn’t boost?)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Preponderant processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Preponderant)

**Categories**: Effects

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Effects](../categories/effects.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
