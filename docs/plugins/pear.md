# Pear



## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

the testbed for a new filter, implemented as a highpass/lowpass shelf

## Detailed Overview

Welcome to the Airwindows skunkworks, where you can get your hands on really unusual experiments!

Pear is a new sort of filter I'm looking to use for my famous-console versions of Console. I've taken the concept of Holt and altered it along the lines I explored in Console Zero, and then I ran with the things I experimented in BitShiftPan a little more.

So, now you have a fixed frequency shelving EQ that can be either a lowpass or a highpass, and it uses an algorithm that is literally different than anything used before, with a behavior that's likewise not like anything else (the code certainly isn't going to be found elsewhere, and the slope steepens as it nears the edge of the passband: cascading it, which this plugin lets you do, makes that end point ever-steeper rather than adding a bump to a steepening overall slope like in any normal filter)

What's it sound like? Hear for yourself, it's yours. My take on it is that it's exactly what I need for the future of Console: this is not a synth filter, it's a desk filter. I can make it be really clear, even when doing extreme things at really steep slopes. It's not a scientific filter for doing really accurate curves, it's for sounding musically good.

I'm not sure what the frequencies are, partly because the transition point is an increasing slope even when it ends up quite steep, and partly because it's not calculated on the basis of frequencies. Those filter points come out of the use of bit-shifting in the algorithm: it will still work in designs that don't use that, and I'll be using more carefully placed crossover points in future Console versions, but for this one, treat it as a switchable EQ. One way to get an EQ point to shift slightly is to increase or decrease the number of nodes (also stepped): consider it the digital equivalent of an analog switched circuit. Use the inv/wet control to dial in how much highpassing or lowpassing you want: that becomes your shelving control on the filter.

Another part of the big-console sound is saturation, and this filter does not include that: expect what I do with this to be more intense as far as sounding like real big consoles. I'll need to configure that to suit the target console, as some are famously dirty: so often, people restoring these desks are told how to replace the dead capacitors and the original inductors, on the grounds that the original ones had no headroom (HMMMM…) but for now, Pear is very pure in tone, and it doesn't distort on its own.

It's going to be a lot of work doing what I'm going to do with this tech, and that's not even counting the changes to my reverbs that will come about as I learn from the Bricasti: sure enough, I've identified stuff that I can probably do, and the result should be worth it. I'll try not to bog down and keep plugins coming out as I dig into all this! Stay tuned :)

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

Pear shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Pear)

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
