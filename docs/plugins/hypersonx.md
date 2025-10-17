# HypersonX

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Latest Release |

## Description

like UltrasonX but with seven stages instead of five

## Detailed Overview

This one’s pretty straightforward. If you know UltrasonX, this is the same thing but for Hypersonic. These are ultrasonic filters for use at high sample rates such as 96k: for less processing than it would take to oversample a bunch of stuff you can run the whole mix at an elevated sample rate and put filtering between nonlinear stages: it works better to do a little filtering in many places, and it helps the mix from seeming overprocessed.

HypersonX is steeper, because it’s seven stages instead of only five. It cuts off a little higher, so it should go right past 20k without hinting at rolling off or softening anything. But since it (like Hypersonic itself) is seven stages, that means you’ve got to find seven spots in your mix to stick the respective stages of the filter.

Like UltrasonX (and like future Console versions I do that will use this technology), you have to have one each of every stage of HypersonX, from input to final 2-buss. That means you don’t have to repeat ’em across all channels: for instance, if you’re running stage A and B on the channels, and C, D and E on submixes, and F and G on the 2-buss, that’s way less filters than you’d have if you placed just one Hypersonic on the start of every single channel, AND it will work better because it’ll keep every little nonlinear stage in check. Otherwise, they can seize on small bits of aliasing and alias them further until they combine and become obvious. Single filtering at the input won’t protect you from this. Distributed filtering will.

This might not be for everybody. The thing is, if you’re running at high sample rates and you want to resist aliasing and have a warm, analog tone that still retains clarity, this might be for you… and similarly to other Airwindows inventions, the cumbersome nature of HypersonX could become your secret weapon. Who wants to carefully arrange to have one each of seven types of inaudible filtering across your signal path, from channel start to end of 2-buss? Possibly you, if the resulting tone speaks to your musical tastes. The barrier to entry is a setup that’s a pain in the butt and fussy rules for how it works (you can combine it with the original PurestConsole if you’d like to also have the cleanest possible Airwindows Console mix, that’s a whole other set of fussy rules!) but you might find the results a little spectacular.

I hope so! The next thing for me is building this into the next version(s) of Console, and I believe it will help things a whole lot. But with HypersonX, you don’t have to wait. Use it on its own or combine it with any earlier version of Console (not Console7 or PurestConsole2, which have their own filtering, but Console 5 or 6 or PurestConsole or Atmosphere or PDConsole which didn’t have ultrasonic filtering built in) and begin constructing your own in-house mixing board, and get your personal sound.

(followup: this became the ultrasonic filter tech for Console8)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

HypersonX processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/HypersonX)

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
