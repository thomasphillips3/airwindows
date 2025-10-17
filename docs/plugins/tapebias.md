# TapeBias

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Lo-Fi |
| **Type** | Lo-Fi |
| **Status** | Latest Release |

## Description

a new piece of ToTape allowing you to underbias or overbias

## Detailed Overview

Closing in on the big update to ToTape, and here's a helpful detail, that's not existed in ToTape before. I've been doing recalls and rebuilds of the big ToTape7 for weeks, but this little aspect more or less worked right away.

Biasing a tape means adding a really high frequency to the sound, a supersonic frequency like 40k. You record to the tape, and this frequency being there means the iron oxide (or whatever metals are in use) gets jostled around, enough that slow gradual changes can be represented properly. Without it, signals kinda get stuck, It's like dither for tiny metal chunks stuck to plastic!

So there are two ways to go about figuring this one out.

One is to painstakingly model the whole system, in mathematical perfection, while overprocessing the heck out of everything, and then stick a virtual faceplate on it. And presumably charge a bunch of money. Not my jam.

The other is to HACK AWAY like mad until you can make noises that SOUND LIKE what's happening, ideally with nice simple algorithms that will retain the digital tone better. But what even is happening?

TapeBias is bypassed at 0.5. Perfect bias here means it applies NONE of the processing. In fact in the final ToTape7 (next week if all goes well!) you can literally bypass the processing at 0.5 to save CPU: it won't be doing anything anyway.

If you overbias, which is commonly suggested as a good practice within reason, you're applying this high frequency tone louder and louder. That will record onto the tape too, in fact you can de-flutter using it, but it's also eating up headroom: maybe, lots of headroom. If all your tape headroom is used up trying to record a supersonic tone, and bear in mind there's a boost/cut dynamic for treble already to try and minimize noise (not even counting Dubly!) then you'll be clipping the real highs more easily if the bias is too intense.

In comparison with test files recorded on real tape machines, I found that GoldenSlew did the nicest job of acting like the sound of overbiasing. TapeBias uses a very slightly changed version of GoldenSlew on overbiasing. If it's inside ToTape7 it's an even better effect because it combines with everything else, but in this case you have basically GoldenSlew for when you overbias.

By contrast, there's no such existing effect that acts like underbiasing. I could refer to a real tape recording and see the odd flat bits that pop up when the biasing isn't quite enough to handle the audio. The sound is known to go a little brighter, sort of dry things up… a possible sonic effect, especially if it's a plugin and not a giant pain to recalibrate tape machines just to do.

Turns out it's possible to do an algorithm that acts quite a bit like what happens with underbiasing, except that rather than put in flat bits of audio, it puts in slanted bits that do about the same thing… and it's a simple algorithm, and you can bring it in subtly or make it obvious. And it works very nicely in ToTape7, inside a full tape emulation with all its parts… but here you get it a week early, all by itself. Because, why not? Why not be able to use that part of the effect, isolated, perhaps for some sound design purpose, or to do weird things with LFOs in VCV Rack or who knows what else?

So, here's TapeBias. Turn it up to overbias, turn it down to underbias. Have fun :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

TapeBias processes audio in the Lo-Fi category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Lo-Fi](../categories/lo-fi.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/TapeBias)

**Categories**: Lo-Fi

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Lo-Fi](../categories/lo-fi.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
