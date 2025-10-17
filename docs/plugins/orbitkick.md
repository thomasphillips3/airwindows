# OrbitKick

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Bass |
| **Type** | Bass |
| **Status** | Latest Release |

## Description

a bass generator and kick drum reinforcer

## Detailed Overview

If you've seen modern recording, you've probably seen a little drumlike object in front of bass drums. This device is a 'SubKick'. It's basically an NS10 woofer hung in front of the kick, so it can be knocked around by subsonic bass waves, and transfer that to electricity for recording. It might or might not be in an actual drum shell, needs to be recorded with an actual preamp (these can have very high output though!) and acts as just another mic, but one that captures the very deepest bass in conjunction with your full drumkit and all your other mics.

But what if you could do that… without the pre? And also without the little drum shell, and without the NS10 speaker, and for that matter without the drumkit. Just 'deep bass subs' like a kick drum. On anything.

Enter OrbitKick. This is basically a little physical simulation, like a planet orbiting a sun. When your input sound hits, it kicks this thing into orbit and it just spins, gradually slowing down as its orbit gets bigger and bigger. It's a little like a second-order sine wave, in that it's one of those Airwindows things that can get out of hand, which is what the controls are for.

Drop is how fast the note will drop, from 'not at all' to real quick. Shape is the same, but makes it drop quicker to start off, so it's your taper: it gives you punchier attacks, rather than 'modular guy beeeoooo' kicks that have no impact. Start controls how high up your attack goes, in conjunction with Thresh, which is the threshold at which the note is kicked off… and Finish is where the note cuts off (set super low, you can get clicky releases).

That's all. If you want shorter kicks, make it drop faster, start lower, or finish higher. These controls do it all. That includes weird nasty effects where the note is triggered in a scruffy, inconsistent way. OrbitKick does NOT sound like a sample. It's like a living bass thing, able to put the lowest of bottom octaves on whatever percussive thing you like, or add a thump or 'pewww!' laser sound to any other thing so long as it has a distinct attack. And without a distinct attack it will still work but it'll make an unpleasant noise. And if you can only listen on a laptop or cellphone you may never hear what it does at all…

This one goes out to DnB friends of mine in London :) rarely do I get a plugin that will wreak so much mayhem on really, really big sound systems. Be careful out there, or don't :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

OrbitKick processes audio in the Bass category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Bass](../categories/bass.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/OrbitKick)

**Categories**: Bass

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Bass](../categories/bass.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
