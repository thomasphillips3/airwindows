# EveryConsole



## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Stable |

## Description

mix-and-match Airwindows Console

## Detailed Overview

Sometimes I give people tools AS I am working on them…

EveryConsole contains the original Console algorithm, Console6, Console7, the sin()/asin() routine that's the guts of Console8 and PurestConsoles 1 and 2, BShifty which is the near-sin() approximation that's in PurestConsole3 from last week, and Console Zero.

All of these algorithms are stripped of all the tone shaping parts and ultrasonic filterings to be the bare-minimum functions for their purposes. That doesn't mean they are every Airwindows saturation routine: Distortion has more. But these are all the ones designed to encode and then decode on the buss.

And, EveryConsole includes both the Channel functions, and the Buss functions, under one hood. So you basically select the version you want, and whether it's channel or buss.

Because there's no filtering or tone shaping these lend themselves to oversampling, for instance Reaper's new oversampling. That doesn't mean it'll be better: I think it kinda won't, but if you have oversampling capacity this is now yours to fool with. EveryConsole gives you access to the raw encode/decode functions without making you use them in an Airwindows way.

That's not why I made it, though. I'm working on modeling the sound of big classic consoles, and I've got a lot of audio reference, and I needed to do a lot of study of how different Console versions combined. I'm already working on doing tone shaping to get closer to the target, and I wondered whether mismatching Console versions got you types of presentations that reminded the listener of specific big consoles.

That would be a YES.

So I'm busily at work using this plugin to monitor a lot of variations on Console and compare them to classic records, and if I get to have a tool then so do you! So, here is EveryConsole. If you'd like to combine it with the distributed ultrasonic filtering I like to use, then load up UltrasonX or HypersonX and arrange the instances of those so they're in the right places around the EveryConsole instances. If you'd like more like Console7's ability to bring elements forward and back in mix, or Console8's tone, you have to use those as there's extra stuff built into the plugins. But if you want more basic building blocks to assemble your own Airwindows big console… this is for you as much as it is for me.

Hope you like it!

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

EveryConsole is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/EveryConsole)

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
