# Slew3

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Latest Release |

## Description

a new approach to slew clipping meant for a more analog-like darkening effect

## Detailed Overview

A Chris’s work is never done! Or at least it’s not, when it comes to refining basic tonal building blocks that apply to many plugins. It’s just recently that I updated Capacitor with an analog behavior found (quite strikingly) in certain real-world capacitors. I’m at it again.

This makes a third Slew plugin, and every one is strikingly different. Slew (original) darkens radically and makes a grungy, clipped tone (it’s in Channel, too, very subtly). Slew2, though there are some similarities in code, acts wildly different: it produces an intense rolloff that is only right up at the Nyquist frequency, and is an elegant anti-glare solution, but barely has a tone at all.

Slew3 uses ideas from Acceleration and DeBess to produce a slew clipping that’s actually reading information beyond what the samples provide: it’s like it reconstructs the wave a bit and is most effective where you’d get intersample peaks. It’s NOT an EQ: it has very striking dynamic qualities. It’s not a pure ‘glare cutter’ like Slew2, either: there’s a limit to how much it will darken. But what it’s all about is producing an analog top-end on your digital content.

This is an experimental plugin. In development, some of my audio caused it to freak out, and it took extra time to get it to behave (I suppose I could also put out the freak-out version but for now let’s stay safe, OK?). It’s not quite linear or predictable (neither is real analog) and though I feel like it might have some very serious mojo to bring, I’m also interested in whether it dies given certain kinds of audio. I’m pretty sure I have it tamed to where it won’t do anything crazy, but is it really the silver bullet? I guess we’ll find out together.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Slew3 processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Slew3)

**Categories**: Brightness

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Brightness](../categories/brightness.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
