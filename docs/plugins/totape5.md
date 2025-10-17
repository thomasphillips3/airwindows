# ToTape5



## Quick Info

| | |
|---|---|
| **Category** | Tape |
| **Type** | Tape |
| **Status** | Stable |

## Description

Airwindows analog tape emulation

## Detailed Overview

ToTape5 is the best Airwindows analog tape emulation. It builds upon the previous four versions (which have been some of my best sellers) and incorporates everything learned from the Purest series of plugins, to produce a tape emulation that does what analog does. (Analog tape does really good things for mixes, and it’s very difficult to get it right without sinking into a morass of overprocessing and digital blandness)

It’s better than Iron Oxide, always was. Iron Oxide is for ‘slamming tape for effect’, for putting on individual tracks, not realism. ToTape is for realism and quality: for ‘mixing to tape’, in the box. I don’t think there is anything else that can stand as much scrutiny as ToTape will: it’s developed on mastering-grade gear and when used in its most optimized state, it’s not a toy. It should be more transparent and musical than most plugins (never mind ‘tape emulation’ plugins, which are generally not even as transparent and musical as a good digital EQ plugin).

It has six controls: four if you don’t count Output and Dry/Wet, which are pretty obvious.

Louder defaults to 0.25 because the tape emulation soaks up some level. You can set it to 0 for added purity (it removes a gain trim stage if you do) and if you do that, you can plainly hear that the emulated tape ‘soaks up’ some of the audio, noticeably dropping the level while not seeming to alter the tone at all. There are no gain adjustments making that happen, it’s entirely tape saturation which is very transparent. (There is no compression, either.)

Softer is the treble softening. Defaults to 0, which is still on but very hi-fi and subtle. You can turn it up to get a more ‘old’ tape machine tone, and like the other controls if you need to finetune the effect by ear, your adjustments will probably be around 0.1 to 0.2 if you mean to retain the full fidelity of the mix.

Fatter is the head bump. Defaults to 0, which is still on, but subtle. It can be cranked up to silly/stupid levels if you like. Again, if you want to emphasize the extra roundness and fullness of tape, you might be tweaking this to 0.1 or 0.2. If you don’t have fantastic subwoofers or monitoring that can handle deep bass, leave this at 0! Boosting it will introduce deep lows very cleanly and you might not hear them unless your monitoring is up to scratch. You will also have to turn down Output if you boost this a lot.

Flutter is the tape flutter. Defaults to 0 which is OFF, see comment on ‘dry/wet’. The most amazingly awesome tape recorders did NOT have loads of flutter, but if you want a little ‘spaciness’ or ‘atmosphere’ you can put in small amounts of this, like 0.1 or so. Go by feel, if you can hear it fluttering it’s kind of too much. If you’re using this, please don’t use Dry/Wet to combine the result with dry: you’ll create a flangey effect and it’ll be more obvious than it should be. By design, Flutter is made so you can increase it until it’s too much, so please remember that realistic levels are more like 0.1: too subtle to immediately hear. Go by feel, or pretend you have a really terrific tape machine and leave it off entirely, set Flutter to 0. (For instance, anyone who’s mastering and intentionally adds flutter ought to think hard about whether that’s really helping.)

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

ToTape5 emulates magnetic tape characteristics including saturation, head bump, and flutter. Use it to add warmth and analog character.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tape](../categories/tape.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ToTape5)

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
