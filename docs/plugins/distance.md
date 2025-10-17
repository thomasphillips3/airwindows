# Distance



## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

a sound design or reverb far-away-izer

## Detailed Overview

Here’s another utility plugin: Distance is specifically set up to mimic through-air high frequency attenuation. It’s from my initial wave of Airwindows plugins, come to VST and with a new twist: though in the video it’s a one-knobber, when you download it you’ll find that it’s got a Dry/Wet control, just to expand the things you can do with it. That’s new! I try to listen to people, even when it’s tempting to make it a super-dedicated one-trick pony.

As you can see from how it behaves, Distance is a lot more complicated than just running a shelf. For that reason, I suggest this plugin for sound design and creative mixing purposes. Don’t try to use it for mastering or 2-buss, I feel it’s too intensely colored. However, for creative use it’s exactly what it says on the tin! Stick it on anything that’s supposed to ‘read’ sonically like it’s super far away, and you’ll be able to hear for miles and miles. Works on anything from pads to thunder to basses to reverb returns (I suggest using it on reverb returns rather than sends: it will be able to add thunder and size to the output of the reverb algorithm)

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

Distance shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Distance)

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
