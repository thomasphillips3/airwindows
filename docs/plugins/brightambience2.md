# BrightAmbience2



## Quick Info

| | |
|---|---|
| **Category** | Ambience |
| **Type** | Ambience |
| **Status** | Stable |

## Description

more BrightAmbience with better tone and more slapbacky effects

## Detailed Overview

This is just like BrightAmbience, except different in pretty much every detail. Techwise (skip to next paragraph if you like) it is using a totally different prime number series, ‘super-primes’ for its delay spacing, and then it’s offsetting alternately left and right delay taps to the next prime number in line, meaning that it’s a dual mono ‘ambience’ but center signals WILL get stereo spread. Also, there’s a kind of regeneration that was real tricky to do, but it means you can get a clean digital slapback, or any degree of ‘fuzzed out’ bright ambient slapback all the way to the wash of sparkly atmosphere, either subtly regenerated or cleanly gated.

Okay, but what does it do, and what does it sound like?

Super ultra bright ambience space that doesn’t get in the way. You can put it on things like drums for 80s gated verb, you can do dub-like things through using it to make a blurry slapback, but this thing is bonkers at putting Star Quality Vocal Glitter on voices. You don’t have to have it loud, and you don’t have to stretch it out so long that it feels like a reverb. That’s not the point, this is about doing that classic Lexicon thing (without, I might add, using ANY actual Lexicon sounds or algorithms) where you can fill in a bright, glossy atmosphere around the voice that makes it sound like star quality. You probably don’t want to treat it like a reverb, on a send or whatever (maybe on a vocal bus? It’ll handle split harmony vocals very elegantly since it’s dual-mono). Instead you want to use it like your lead vocals alone go into a special chamber. Might also be an inspiring thing to monitor while tracking: I sure had fun playing with it in my headphones, and if it’s on your mix while tracking you might not have to print it on the actual vocal track. Everything about it is evolved from BrightAmbience, even the algorithm that makes it.

Oh, also if you’re a coder and want to get your hands on the delay taps, it took hours of looking up and typing in specific prime numbers, as there is no such thing as a ‘list of super-primes except every other one uses the next real prime after the super-prime, making the list pan every little echo to alternate sides using inter-aural delays’. And maybe you never even thought of such a thing. But if you think you can make use of such a thing, in the .h file (for the AU, anyway) is a definition of ‘primeL[]’ and ‘primeR[]’ that you can simply copy and paste. It’s 489 total entries which will get you a half-second or more out from the dry signal, even at 96k, and you just use ‘primeL[]’ and ‘primeR[]’ to specify the delay taps you want, typically in a range (like, entries 40 to 60 will give you a little ambient blur starting at whatever ‘primeL[40]’ is, which is 1031 samples)

It’s MIT license so you only have to shout me out and you can do anything you want with it… so don’t say I never gave you nothin’ :D

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BrightAmbience2 processes audio in the Ambience category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Ambience](../categories/ambience.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BrightAmbience2)

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
