# CansAW

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

Chris's Airwindows room, in a plugin, for headphone mixers

## Detailed Overview

This is pretty straightforward. Remember Cans? Every possible control room sound from compact to huge, adjustable any way you like?

This is the Airwindows presets. That's all.

By that I mean: I've been developing my mix room, where I do all my work, for years. By now I've got speakers, subwoofers (stereo), extensive room treatment, multiple mix check positions up to and including a stairwell at the back that leads up to a small hallway, from which you can hear how a mix hits a much larger space and how it'll work there. I have to close all the doors like to my bedroom to use that mix position, and I've shown it on mixing livestreams (though miking it can get hissy as I'm not using live-gig levels here). It's real-world acoustics used to better document how a mix works in different situations, and it works really well, better than anything you could do over headphones.

And I've made a version of Cans that does these exact mix positions, including the hallway mix check, and while it is not as good as real life… it's not bad, not bad at all. It tells you some of the same things. It worked, in other words.

This is for me as much as you. If it's out there, even if my house gets flattened by a meteor or perhaps Elon Musk experiencing a nuclear K-hole, and I survive the meteor or madman, and I have a laptop and some headphones, I can work after a fashion :) there's enough out there whether it's publically available tracks from my own music or new synths like Six Sines or my perennial fave Surge XT (which can fire one-shot percussion samples off the wavetable osc), and of course I can download ConsoleX just like anybody (making progress on helping Yaeltex put out the control surface I designed!) and that means I, like anybody else, have access to some of the universe of free audio stuff, that universe that's become so broad that I can even do the music I care about, with just a bunch of downloading open source projects :)

Of course if the meteor gets me all bets are off and you're gonna have trouble getting ConsoleH out of anybody else. But that's why I'm burning the midnight oil (well, up-very-early firewood?) to keep making stuff: I'm not done and I've got even more exciting stuff than ConsoleX in the works, as well as lots of extra support stuff to put everything in gear, and studio tricks to give audio (that can be sampled and re-used) that hasn't been heard right for decades. Starting to figure all that out, and I hope I can convey my enthuiasm.

For today, here's CansAW. You can get to any setting in it using Cans (it's all Room D, for a start). But each setting is dialed in as exactly as I could get it, using real acoustical audio for reference, in the mix environment I've been developing for years. If I had access to all the mix rooms in the world I'd give you the approximation of those as well, but here's my place, in the box :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

CansAW processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/CansAW)

**Categories**: Utility

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Utility](../categories/utility.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
