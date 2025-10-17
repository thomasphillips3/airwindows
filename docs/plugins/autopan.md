# AutoPan

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

for getting some organic stereo movement into your mix

## Detailed Overview

This is pretty simple: I got asked for an auto-pan. So I Airwindowsified it a bit, and here you go.

It’s set up to get some nice organic movement into your mix in various ways. Rate is how fast it goes (from nearly static, to a rapid flutter).

Phase means each channel relative to each other: on either side, you get full L-R and back again. At the center, it’s a mono tremolo (though, for stereo channels). Off-center, it’ll offset the sines in such a way that the sound sets up a swirling, circular stereo motion: swooping forward from the side, going across, and then back to near-silence again. Basically, centered is ‘not side motion’ and to the sides is ‘more side motion’.

Wide just cuts the mid channel. What this does for the auto-panning is, it’ll make stuff stretch out a bit beyond the edges of the speakers. If you’ve got something full to the side then you’ll get a bit of the opposite on the other speaker. Full wide is ‘only side channel’ and you’ll hear it in both because that’s what you get when you have only side channel: centered ‘mono’ sound, just out of phase completely. You’ll probably want to use smaller amounts of this, unless…

Dry/Wet is the final useful thing here. You can set up extreme stuff, like full Side or weird motions with Phase, and then just dial it back with Dry/Wet and it’ll give you a nice subtle activity of whatever you set up: don’t sleep on Dry/Wet here, you can get nice effects through using aggressive settings elsewhere and just sneaking in a little Dry/Wet. Especially if you’re doing extreme things with Wide, Dry/Wet is how you can integrate that into a sound so it’s just a nice little subtle motion that’s interesting. Or of course you can just crank it out, I’m not your mom :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

AutoPan processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/AutoPan)

**Categories**: Stereo

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Stereo](../categories/stereo.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
