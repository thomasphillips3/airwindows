# Console5DarkCh



## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Stable |

## Description

a richer, warmer Console system

## Detailed Overview

Console5 uses some more ‘expensive’ math operations, where previous Consoles tried to do their thing while keeping the Channel component as low-CPU as they possibly could. This might mean a heavier CPU cost, or it might be not that much of a difference. It’s a change (the math here more closely resembles Density or PurestDrive).

What do you gain? Using this more advanced math means there are functions which can exactly ‘undistort’ what comes in (more on that property later: there’s a variation on Console that perfectly nulls when only one track is active). This brings an added level of bigness and signal purity. Then, Console5 applies a similar behavior to the slew factor, but backwards to what the amplitude factor is getting. Doing that takes Console5 away from perfect transparency (and subtlety) and gives it a big, beefy, large-console sound that still doesn’t radically alter individual tones… but throws in TONS of ‘glue’ and solidness compared to the raw digital mix.

This is not a thing you’d struggle to hear (listen for depth and space, not frequency changes). This is not a thing that’d get washed out in mp3 encoding (in fact, because of the way it restricts slews in Console5Buss, it’ll actually help encoding a teeny bit, because superhigh frequencies waste bandwidth better used on the mids). This is the new Console, and it should be a real revelation to mix through, no matter what style or genre you’re working in.

As seen in the video, if you’ve got a DAW that can enable/disable plugins on selected channels, you can audition it with one mouse click to switch. Console5 works like this: you want Console5Channel on every channel feeding the 2-buss (with all submixing and all post-plugin faders at unity gain), and Console5Buss first on the 2-buss. That’s all, just replace digital summing with this system. If you can do post-fader plugins, you can use the faders (otherwise, best use the trims on the Console5Channels, or any earlier gain trim). The point is to replace your digital summing network with the Console5 system.

If you have that mastered, you can start playing with stuff like putting things ‘inside’ Console: delays, reverbs, EQs. Plain digital EQ in particular benefits from being post-Console5Channel on the track. Gain stage everything so you’re not slamming Console5Buss more than about +3 dB: it should survive hot peaks but there’s no special benefit to clipping it, and Console5Buss will clip there. Ideally, you’ll frame a mix with Console5 in place, and you may find you don’t need to do nearly as much ‘twitchy DAW stuff’ to get things sounding acceptable. Console5 addresses the root of the problem in a way no other ‘console emulation’ does. (if they do, you’ll find they have exactly the same constraints: needing to keep unity gain between Channel and Buss plugins is a dead giveaway they are using the Airwindows design)

This is the Console version that can generate DC offset from sawtooth waveforms due to its interaction with slew rate handling, and the final Console5 you can get attempts to accomodate that. For the launch version (with a different DC-block strategy in place), use C5RawConsole.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Encode]
    B --> C[Summing]
    C --> D[Decode]
    D --> E[Output]
    style B fill:#6366f1
    style D fill:#f59e0b
```

## How It Works

Console5DarkCh is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Console5DarkCh)

**Categories**: Consoles

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Consoles](../categories/consoles.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
