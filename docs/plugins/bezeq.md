# BezEQ

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

a strange, alien three-band shelving EQ

## Detailed Overview

You don't have an EQ anything like this. Nobody does. This is guaranteed new.

The reason is, nobody with audio training would try to apply Bezier curves to audio reconstruction (since it doesn't make sense, though it's nice and efficient to do), and if you did you'd get my latest DeRez which doesn't work like a normal frequency crush and so that would scare more people off, and then if you tried to use two DeRezzes in series as brickwall filters for a three-band shelving EQ, you'd so quickly run into problems (for instance, with test tones) that you'd immediately run away, never to return, knowing it would be impossible to get away with it.

And more fool anybody who did try ALL of these things and then gave up… because this is a hell of a thing, and now it's mine, which means now it's yours. I do Patreon so it doesn't matter if one of my plugins is scorned as an EQ and behaves terribly in testing. I can put it out anyway! And even explore the idea of building it into ConsoleH… but that's in development, and BezEQ is yours right now.

If you keep Treble, Mid and Bass exactly the same volume (any value, the settings will match) it will behave quite perfectly. Doesn't matter what the crossovers do. They're assembled subtractively so they'll add up to perfect, every time, if they're set to 'flat'. I often do that with 'general purpose' EQs or with things like StoneFire: it's good to have 'flat' be really, really free from issues. It's the opposite of breaking things into an FFT transform or an mp3 and then reconstructing them from the (limited) data.

Then, if you shut off Treble, the output is DeRez3 using the X control between Treble and Mid to set the cutoff.

And if you shut off Treble and Mid, the output is DeRez3 using the X control between Mid and Bass.

And if you shut off everything BUT Treble, it's the dry signal MINUS the first DeRez3. It's only the highs from what would've been a de-rezzed, pseudo-brickwall cutoff.

And if you have Treble AND Bass, you have that plus the derezzed Bass, which is what remains after the Mid goes through another 'filter' that's not really a filter. Same with if you only have Mid: it's derezzed treble-removed, but with the other derez subtracted.

Except you'll quickly learn that none of these are clean crossovers at all: you'll get a strange overtone that comes out at the filter cutoff and acts weird. You can add a LOT of deep bass and an extra tone, like a ring mod, through boosting bass and adjusting that cutoff. You can add bass through that extra tone by CUTTING bass and adjusting the cutoff. It's a bizarre toy but it works predictably and has its own sound, to love or hate.

And that's not even getting into when you do this, and then make the cutoffs fight each other by setting TxM very low and MxB very high, causing the distortions to distort and interact… you can get into a lot of trouble with this, and so totally reinvent the sound that it becomes unrecognizable.

And then dial it back to as subtle as you like, simply by making Treble, Mid and Bass be closer to each other.

Have fun and don't say I didn't warn you :)

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

BezEQ shapes frequencies through EQ. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BezEQ)

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
