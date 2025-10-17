# ResEQ2

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

a single, sharp, sonorous mid peak

## Detailed Overview

This is another 'piece of an upcoming great plugin'. In order to do an MCI console properly I had to do a good mid peak.

And we're talking 'way better than just a sharp biquad filter' mid peak. I needed clarity and character beyond what regular digital EQ cookbooks could cook up.

ResEQ2 continues on the work I started in the original ResEQ, where I observed that Manley EQ impulses for sharp resonances seemed to be like a sine-like ring, except the onset did NOT seem to be at the same frequency: seemed to start faster, even double the frequency. I made a whole plugin, ResEQ, giving it my best shot for generating multiple resonant 'rings' and combining them, to produce a convolution impulse that was the sum of multiple analog-like resoances. It still exists: it's way before I routinely worked at 96k, and it's got a lot of quirks, but it does get a distinct sound.

I returned to those deep, murky waters when trying to come up with a sweepable mid peak like certain classic analog consoles.

ResEQ2 is the result. It's the opposite of what you'll normally find in great classic analog consoles. A lot of the classics really had quite limited analog EQ: detailed parametric sculpting came in with SSL, and to some extent API before that. In the olden days, things were a lot simpler (and you gained something sonically from this simplicity).

But there were a few special cases, and so you had MCI's sweepable mid, that could only boost. Not cut. It just gave you a sort of ring, wherever you wanted it. Not the most flexible circuit… but a hitmaker.

This is because, contrary to modern practice, there's huge power in being able to single out a midrange, upper-mid, or treble frequency, and sort of just open up the top of it so it can get effortlessly loud. Instead of just blasting everything, you find one presence peak on your track that really lets it speak, and you just give that a boost. More peak energy, more clarity exactly where it's most useful, and it's almost never in the same place for different instruments or vocalists, so the combined sound of the mix cuts through on dozens of sonorities at once, and everything is powerful and clear.

It's the mids equivalent of Airwindows Weight for bass, and it works incredibly well (even if you do it with biquads or EQ-design cookbooks). And I don't have the analog-Console projects finished yet… but you can have this part of it now.

Use the 'ow argh way too extreme' settings like 1.0, where everything kind of turns into an audio laser, to dial in exactly what spot opens up an instrument or voice for maximum passion and sonority. Then, dial it back to around 0.5 and begin increasing it, seeing at what point you've got too much of a good thing. ResEQ2 is great at being a subtle light-bringer and giving clarity to a track. It's also a full-on energy weapon that can be set to 'way too much', so use it however you please. The resonance increases as you turn it up, so feel free to dial it back if it gets ringy. Probably not a good plugin for mixing live sound unless you like dial-a-feedback :) hope you enjoy ResEQ2!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Filter Stage]
    B --> C[Resonance]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

ResEQ2 shapes frequencies through EQ. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ResEQ2)

**Categories**: Filter

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Filter](../categories/filter.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
