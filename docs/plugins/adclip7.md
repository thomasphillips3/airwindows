# ADClip7



## Quick Info

| | |
|---|---|
| **Category** | Clipping |
| **Type** | Clipping |
| **Status** | Stable |

## Description

the original Airwindows loudness maximizer/ peak control

## Detailed Overview

Finally! The newest version of Airwindows’ famous ADClip is out, and it’s Mac and PC VST for the first time, and it’s free! If you have dense, busy mixes and you want to push their loudness to the max, this is the one you want. And, oddly, if you’re mastering for streaming services or iTunes and don’t want to do a thing besides convey your mix at a set LUFS and intersample peak level, this is still the one you want :)

Here’s how it works.

You’ve got a boost control, a soften control, an enhance control, and a popup or multi-function control with three options: normal, gain matched, and Clip Only. These are all interactive, so I’ll explain them in the context of that ‘mode selector’ popup.

In normal mode, boost makes things louder. This is a clipper, and no more polite method can ever make things louder than a clipper: you need to either give it a busy and complicated mix to mask the clip artifacts, or use it to snip off non-tonal percussive peaks, at which it excels. A clipper does NOT produce ‘limiter-like unvarying block of sound’, and you shouldn’t try to achieve that. A clipper gives you punchy but LOUD, and tries to retain all the dynamics you’re feeding it, rather than smooth them out for a ‘clean’ sound.

The soften control manages the way that high frequencies enter and exit the clips. It algorithmically reshapes the edges of your clip, stopping it from getting digital glare and fizz. This is the heart of ADClip (also present in my simpler clippers, not counting One Corner Clip, which is still upcoming).

The soften control also balances the outputs of two separate energy-fill algorithms, one for bass and one for highs. This was the response to a certain other loudness maximizer that launched proclaiming clippers were dead, and which is still promising its version 2 (and some bugfixes) while ADClip has gone far beyond it. Turned out the secret of that one was an elaborate way of massaging clipped-off loudness back into the signal, in a way that was supposed to be transparent but ‘cracked’ into artifacts when pushed too hard. The algorithms were presumably very sophisticated, which tends to just make the breaking point more obvious when you hit it.

The Airwindows version is a completely different, cruder and more direct version of doing the same thing, so when you slam the heck out of ADClip7, you get a deep bass slam that ‘overhangs’ a bit to add weight, and still fits into the clipped output. And you get the softened, analog-style clips to add ‘heat’ and overtones, but you also get a high-mids reinforcement that normally just highlights bright transients that would otherwise be lost to the clipping. And the Enhance control lets you go between purely ‘analog clip’ energy, and these added reinforcements.

The gain-matched mode has two uses. You could use it to ‘set your slam level’ in a way guaranteed not to trick you into thinking louder is better: it turns the output down, so instead of hearing everything get bigger and louder, you just listen for the point that the clipping’s adversely affecting the sound. Then you can flip back to normal mode, if that’s what you wanted (maximum loudness without blatant grunge). Or, you can ignore the slam and use gain-matched mode as I demonstrate in the video: ADClip7 already suppresses intersample peaks when they’re part of clipping, already reinforces energy lost to clipping, so you can use it in conjunction with a tool like Youlean’s loudness meter to dial in a specific intersample peak level for iTunes or other such picky streaming services. It’ll work like padding the output. and if you’re already in the ballpark LUFS-wise, ADClip is a far more sophisticated tool than just limiting and then padding the output to get to your ‘true peak’ target.

The last mode is Clip Only, and rather than selecting the various algorithm outputs individually, this version of ADClip gives you them at their respective loudnesses, combined. That means you can engage this mode to hear ONLY the clips, and check that you’re not hearing any recognizable ‘scrunch’ of continuing clippage. But since you’re also hearing the enhance outputs, you can adjust softness and enhance level to balance the stuff being introduced to the sound. My recommendation is to set the controls so no one type of artifact predominates: it’s not necessarily great to throw in a bunch of ‘enhance’ bass just because you can. If you’re hearing that much of it that you’re tempted to use it as an effect, you’re definitely also over-slamming your music.

So my recommendation in 2017 heading to 2018, is to use ADClip7 in gain-matched mode, to keep that ‘true peak’ measurement within the Mastered For iTunes requirements. I’m sure not everybody will stick to that, but I’m happy to say it is actually quite good for doing that, and if people want to smash stuff with it and enjoy the bass thud, that’s their affair. Remember a clipper makes stuff dynamic and punchy, not ‘flattened out’: use a limiter if you need dynamically flat, or perhaps both. In this modern era of replay gain, I’m going to suggest that dynamic and punchy is where it’s at. Learn the lessons of the LUFS meter! They’re available to us all, now.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ADClip7 controls peaks and maximizes loudness through sophisticated clipping. Use it as a mastering tool or creative effect.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Clipping](../categories/clipping.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ADClip7)

**Categories**: Clipping

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Clipping](../categories/clipping.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
