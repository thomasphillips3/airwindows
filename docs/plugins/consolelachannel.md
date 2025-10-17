# ConsoleLAChannel

![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Stable |

## Description

the Airwindows take on the Quad Eight console

## Detailed Overview

APIs and Neves and MCI, oh my… well, ConsoleLA emulates the most incredible console you've never heard of. This thing was the sound of LA in the seventies. It's on the back cover of Steely Dan records, it's been seen in Tom Scholz's basement, and it's heard even on classic 70s LA and Hollywood and San Francisco records it didn't make… because it's the production model of a whole lineage of West Coast custom recording consoles with similar designs and circuitry. And you can still get them, apparently, the company lives… but I don't know where, or for how much, or how, as there's no sign of prices or any way to get them. There's none on Reverb, Vintage King doesn't have any, good luck even finding channel strips…

Meet the Quad Eight.

This sound echoes through the Seventies. Tons of Steely Dan, tons of Zappa, Grateful Dead, Neil Young, Joni Mitchell… that's not even counting the wilder sightings, like when people figured this console mixed The Wall, or hearing it on Yes's Relayer album. The thing is, this was THE big production console before the days of Neve and API and SSL. Quad Eight were the first to go into production and come up with a recording console that you could just buy, set up, and use. Before them, you had to build your own.

Quad Eight were (are, since the website says they can still make you gear) supplying the film industry, and it shows. These desks are amazing at making movies for your ears. (in the Zappa phrase, on the Hot Rats album, which was done at the Whitney studios in Glendale the year before they got a Neve, so that album was likely also Quad Eight or a kindred West Coast console)

ConsoleLA, like ConsoleMC before it, is a bit of a different approach to emulating these great old dinosaurs, some still things you could conceivably find and have, some forever lost. The thing is, this is the nearest thing to custom point-to-point wiring of discrete transistors. On top of that, the Quad Eight ran a higher supply voltage than anybody: negative 28 to positive 28 volts, for enormous energy and headroom. The way to get these sounds is not layer upon layer of 'digital emulation' but trying to get the behaviors right with minimal, atypical algorithms. Only then can you get the energy and sonority of the real Quad Eight.

The filtering is a whole other thing from the MCI. No mid peak here. The slopes are more gradual, but you can cut the hell out of the mids, and the deeper into the Seventies we got, the deeper the midrange cuts became. What I've done with ConsoleLA is try to make the simplest, most approachable Console system that can get the widest range of sounds as heard on these records, and reward you when you pursue music-recording in the old school, human way.

This doubtless won't be the last, but it might just end up being my favorite. I hope you like ConsoleLA :)

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

ConsoleLAChannel is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ConsoleLAChannel)

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
