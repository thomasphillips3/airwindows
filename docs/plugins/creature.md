# Creature

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Latest Release |

## Description

a soft slew saturator, a new class of noisechanger

## Detailed Overview

So here's something new: didn't exist before, even I didn't have it.

Creature is a soft slew saturator. It's a way of working with applying a sin() function to slew clipping. In fact it applies an unbounded sin() function, so it might be technically considered a slew wavefolder? Because that's what everybody needed, was a slew wavefolder. How useful, nerdy, and pointless.

Not so much. Listen to this little monster.

Creature is up to 32 (or more, at high sample rates) soft slew saturators, stacked up like the poles of a filter. It acts like a distortion, except it's not a distortion. It acts like a filter, but it's even less of a filter. Its interaction with sample rate is really strange (has to scale up with the square root of the sample rate multiplier!)

And what Creature really does, is roar.

As you keep adding Depth, the gain and the thunder increase unreasonably. The total force on tap is pretty ridiculous, and it keeps getting harder to control as you turn it up. There's an Inv control that can give you a really interesting cancellation that acts like a highpass-ish, but not like any highpass you've ever heard. Using it in phase, in Wet mode, unleashes a monstrous overdrive with humongous bass that refuses to lose weight even at impossibly high gains (real interesting on drum rooms!)

There is no overdrive. There is no EQ. There is no highpass.

It's just Creature, which is very much its own beast. It's also a very, very simple algorithm (isn't that so often the way?) so especially at low Depth settings, all this monstrousness can be yours for almost no CPU. I'll be finding ways to put this to use, but as always, you've got it fresh from the plugin forges. Be careful, and have fun with your new Creature.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Creature processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Creature)

**Categories**: Saturation

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Saturation](../categories/saturation.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
