# Stonefire

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

the non-EQ EQ designed for ConsoleX

## Detailed Overview

There's a reason people have never turned to using Kalman filters for audio purposes.

They're tricky little buggers, unpredictable, with a 'filter slope' that makes no sense at all. They'll take the crossover point and bounce it around wildly, they'll throw in weird gatey behaviors, they'll turn what's supposed to be a 'smooth' 'filtered' sound into an edgy growl and sputter. They're meant to pull real data out of a pile of noise, not to take real audio and give you anything sensible. Nobody would want a Kalman filter for audio purposes.

Stonefire uses two different kinds of Kalman filters for audio, as crossovers. The top crossover is the same as what's in Air3. The bottom crossover comes with a range control (even though that won't give you a 'frequency') and is the same as what's in Kalman.

And when used properly, Stonefire gives you unprecedented levels of tonal control over the texture and presentation of your sound, in a way that almost doesn't even have to do with frequency.

There's three bands, plus the Range control. Air, Fire, and Stone. Each can be cut back to zero, or boosted (Fire and Stone match, while Air has a lot more gain on tap but will match from 0.5 down to 0.0.) If you cut them back to zero you'll get the weird Kalman behavior, but it'll help you set the Range control appropriately. You can set it so Stone covers the lowest lows (never JUST those, it will always do other stuff too) or up to the high mids and lower treble.

Then, if you keep everything balanced and make smaller adjustments, the secret of the Kalman filter emerges. You have to use it as a crossover, and let it apply its incredibly strong character to texture, not frequency. It utterly fails to be a 'filter', but it's an extraordinary texture-shaper, and it's what I'm going to be building the upcoming ConsoleX system around.

Use the Air control like you would in Air3. You can cut back super-highs while seeming to not affect the brightness at all, with a strikingly natural effect. Or, boost it to bring that sparkly aura and light up the sound. It's a custom algorithm that deals with high sample rates by just ramping up the boost: treat it with respect, but it's there to serve your needs for glitter or lack of same.

Use the Fire control like it was an attitude knob, as much as a midrange. You can get a lot of wildness out of this one with careful settings of Range. Between Fire and Stone, only one can be louder: it's a crossover. If you're boosting Fire, that means you want your sound to command attention.

Use the Stone control like it's the bedrock of your sound. If you lean entirely on it and kill all the Fire, you'll get a monumentally heavy, sputtering, gatey foundation that zeroes in on the lowest lows, but also tries to put backbone behind anything it thinks is heavy and powerful. This includes lower midrange. Cutting it can control unwieldy bass, but adding it isn't the same as adding a 'bass boost': it'll zero in on things like kick weight and try to present them with unnatural isolation. The secret to adding weight with the Stone control is to let it not seem to be that much of a boost: you can transform the feel of a sound well before you hear 'added bass'. You can also dial the Range up and use the same effect up into the midrange, for an intensely solid punchy character anywhere a sound seems flimsy.

God help you if you try to measure this thing with PluginDoctor or SPAN. I don't even have any idea what will happen. It's all made out of Kalman filters, which are not for use with audio.

Except… when they are ;)

Enjoy the new tone shaping. If it's too ugly, use way less, see how it treats you :)

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

Stonefire shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Stonefire)

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
