# IronOxideClassic



## Quick Info

| | |
|---|---|
| **Category** | Tape |
| **Type** | Tape |
| **Status** | Stable |

## Description

the purer, simpler, early form of Iron Oxide before all the features

## Detailed Overview

As promised, here is the 2017-ized version of the pure, sweet, original Iron Oxide. No more grit or tape flutter or noise!

It’s funny how this works. If you’re a commercial developer, and you release a plugin that’s real popular, one thing that happens is people begin asking for more. More features, more variations, this and that and the other. The flutter in Iron Oxide 5 came about that way: it migrated over from ToTape (which is also coming to free VST).

Every new thing added is something lost. But since I’m no longer doing strictly commercial development (it’s steadily all becoming free, backed by my Patreon which allows all this to happen) I can do things like confuse the ‘market’ and release both the feature-full Iron Oxide 5, and the stripped-down Iron Oxide Classic. This one is just like the original: input trim, ips control, and output trim. Better yet, it has the pure unsullied tone of the very first Iron Oxide, only brought up to date so it noise shapes to the 32 bit buss etc.

Even if you liked the grunge factor of the very adjustable Iron Oxide 5 (more controls may be added but bear in mind I have a commitment to release plugins like BussColors, not just keep revising Iron Oxide!) you might want to check this out. And if later versions of Iron Oxide wandered away from what works for you, for instance if you’re making electronic music and needed much cleaner handling of synthetic tones… this is your lucky day!

Hope you like Iron Oxide Classic. It is, truly, one of the Airwindows classics, now for free VST and brought up to date. :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Bias]
    B --> C[Saturation]
    C --> D[Head Bump]
    D --> E[Flutter]
    E --> F[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

IronOxideClassic emulates magnetic tape characteristics including specific tape behaviors. Use it to add warmth and analog character.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tape](../categories/tape.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/IronOxideClassic)

**Categories**: Tape

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Tape](../categories/tape.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
