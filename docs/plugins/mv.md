# MV



## Quick Info

| | |
|---|---|
| **Category** | Ambience |
| **Type** | Ambience |
| **Status** | Stable |

## Description

a dual-mono reverb based on BitShiftGain and the old Midiverbs

## Detailed Overview

Back in the days of really old school digital reverbs, there were a couple weird and obscure ones that had a special mojo. I’ve got one: the original Alesis Midiverb. It’s quite low-fi and only has RCA jacks, but there’s a certain something about its sound.

Turns out one of its secrets isn’t so secret: the first two versions of the Midiverb don’t have a multiply unit. That means you can’t do certain reverb things correctly. Reverbs use a kind of delay effect called an allpass filter, which involves multiplying by 0.618 (I’ve sometimes generalized this to ‘the golden ratio to N decimal places’, where N equals ‘a lot’). But the old Midiverb couldn’t do that… so it made an ‘allpass filter’ by multiplying its stuff by 0.5. A bit shift.

Airwindows fans will know that there’s something special about a bit shift: especially in floating point, you can change volumes by 6dB pretty much losslessly. No, make that ‘totally losslessly’ since in floating point you’re only changing the exponent and could change it right back and lose absolutely nothing: the mantissa is never touched.

What would happen if you took this old school way of doing allpasses, and made a modern reverb out of it, using full-quality floating point to do it? What if you followed up by making the regeneration also strictly ‘bit shift’, increments of 6dB or infinite regeneration, losslessly? What if you added a way to roll off highs by averaging output samples of the allpasses, and did THAT entirely using bit shifts as well? And allowed for a big number of allpasses (26, all different increasing prime lengths), and gave varying treble rolloff by independently controlling which of the allpasses got the average treatment?

Welcome to the infinite land of MV. This is nothing like a normal reverb, but it’s got some great superpowers, not least of which is the ability to just sustain a ‘bloom’ forever. You can automate it by kicking the regeneration up to 1.0 any time you like.

You can dial in different degrees of highs roll-off using the bright control, or leave it at 100% shiny. Combining this with more restrained regenerations like 0.51 or 0.26 at medium-to-high sizes will give you very decent ‘impossibly huge reverbs’ of various characters. MV doesn’t do early reflections or plausible spaces, just the infinite wash, but that’s somewhat configurable.

It runs dual-mono, so you can dial down the size a bit (not too much or it’ll get nasty, you’re removing allpasses from the chain) and use it as an ambiance generator, and it’ll put all reverb tails ‘behind’ the sounds that make them: centered stuff stays centered, wide or stereo stuff goes super-wide. For this reason it’s very suited to use on auxes and submixes: you can add ‘space’ that’s very pure-sounding

It can do full, 1/2, 1/4, 1/8 and I think 1/16 level regenerations: set the feedback and it will use the bit shift amount nearest below the setting, so no matter what you do it will always retain its audio character. And the whole thing runs inside a PurestConsole instance except for the regeneration, which is extra… which means that if you build up a wall of infinite reverb, it can’t go into reverb runaway because distorted samples will wrap around and get quieter: you’ll have to trim down the output, but this makes infinite regeneration super-usable without applying any kind of compressor or limiter inside the loop. Since you can also do zero regeneration and it’s just a pile of allpasses, you can also do a ‘gated reverb’ effect if you like, which is good at airing up the mix but then getting out of the way.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

MV processes audio in the Ambience category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Ambience](../categories/ambience.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/MV)

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
