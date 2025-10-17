# Sweeten

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Subtlety |
| **Type** | Subtlety |
| **Status** | Latest Release |

## Description

where you can find super-clean second harmonic

## Detailed Overview

So this serves a few purposes. Sweeten is one of the super-minimal, one knob plugins. It makes second harmonic: much like SingleEndedTriode, or Inflamer. The first purpose is to exist, so if you're thinking 'I gotta sweeten this sound, now which Airwindows plugin of the three billion and twelve does that? Conflagration? No, that can't be it' then you can go 'is there one literally called Sweeten', and now there is! And it does what you'd expect, even harmonics (second harmonic, specifically). That's all it does.

Another purpose is because I use stuff like this in my designs. So it's useful to have a chunk of code that I can take and put in the midrange section of an EQ, or something, if I think it's lacking that subtle nonlinearity which comes out of some circuits. Sweeten is specifically designed to let me do that quickly and easily, and if I make a tool for myself which is actually neat and efficient, I give it to people.

The only thing Sweeten can do that you can't already do with Inflamer is be simple, and maybe one or two fewer math operations, and that's IT. This isn't new (second harmonic isn't new, either). My hope is that it's such an elegant, easily identifiable little device that it'll come in handy. It's also using the stepped-control, bit-shift-gain thing I do lately, so one thing about it is that it'll prevent you overprocessing. If you turn it up until you can hear it a little too well, drop back a step and then you can't tell it's doing anything, but it very much still is. For many types of processing (second harmonic emphatically included!) the optimal setting is where it's doing its thing but at no point is it ever distracting or sticking out as a mixing mistake. Sweeten is predisposed to quickly get you to that point with no fuss.

I'll be using it: if anybody else finds it useful, that's even better :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Sweeten processes audio in the Subtlety category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Subtlety](../categories/subtlety.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Sweeten)

**Categories**: Subtlety

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Subtlety](../categories/subtlety.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
