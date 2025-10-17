# ClearCoat

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Ambience |
| **Type** | Ambience |
| **Status** | Latest Release |

## Description

an array of bright ambience reverbs

## Detailed Overview

So, after months of work on refining Householder reverb matrices and realism and depth, and getting started on the huge tasks of mastering the tones of Bricasti reverbs and million-dollar analog recording consoles… I make a dual-mono bright ambience.

What's that for? First of all, it's for me. I'm using it immediately on album mixes. But beyond that, it's an example of something very Airwindows-like: once I get access to something, I share it. I wasn't able to do sounds like these when I did the kPlate reverbs. I tried. My tools for making the Householder matrix stuff hadn't evolved enough yet: this is why kChamberAR sounds the way it does. I had bright ambiences, but they were very artificial (though, nifty in their own right)

And this is what I'm sharing now: I got it to work. Next stage unlocked, with not one but effectively seventeen bright ambiences in one. ClearCoat is the one-stop shop for sparkle and atmosphere. It's not about lingering verb tails: the space it produces is dual-mono and remains tied to the sound that's creating it, and while there is feedback in the algorithm, it's calculated to be exactly halfway between the purity of infinite sustain, and the purity of BitShiftGain in the feedback path cutting the feedback by 6.08 dB. The idea there is to produce a consistent tone in the feedback path while allowing it to bloom a little. Basically more Chris from Airwindows experimentation: see if you like the results in the sense of space the plugin creates.

On top of that, I'm exploring a refinement of SubTight, the same plugin that backfired on me in ConsoleMC. I think if I scale it to sample rate a certain way, that might tame it, and the kind of energy it brought is perfect for this plugin. The brightening and subs-cutting is happening after the reverb matrix, to enliven the space.

It's simple to use: top slider picks a setting, bottom slider is your dry/wet. Add just a bit for in-line air on an instrument or submix, go all-wet for use on an aux. I'm using it as my Verb 1, with the upcoming kCathedral for Verb 2.

Why go for specifically this effect? The theory here is simple: you get better mixes when you're serving a purpose rather than throwing tone colors around just to make them happen. ClearCoat is there to be an extremely refined and intense form of 'nearfield reflections', like singing in a bathroom, or drumming in a live drum room. Yes, you can turn it way up and it'll sound like a really bright reverb, like a small (to medium) room with tile or stone walls. But what you can also do is turn it right down once you have the tone color you want… and then HINT at that tone color, with it.

And if you do that, ClearCoat ought to give you the gloss you're looking for, while minimally affecting the rest of the mix. No clutter, no excess energy, no trace of a tone character beyond what you need, and a cleaner mix as a result.

Let me know if ClearCoat works for you, and especially whether it's acting OK at diverse sample rates with the changes I made in SubTight. If so, I can and will update the actual SubTight plugin AND ConsoleMC to correspond (if you're working at 1x sample rates there will be no change for you, but if you're working 2x or 4x or oversampling 2x or 4x, you might not have to compensate for the brightness as much to get your sound)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ClearCoat processes audio in the Ambience category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Ambience](../categories/ambience.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ClearCoat)

**Categories**: Ambience

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Ambience](../categories/ambience.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
