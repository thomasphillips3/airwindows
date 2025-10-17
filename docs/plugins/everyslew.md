# EverySlew

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Latest Release |

## Description

a wide variety of unique sound processing tools

## Detailed Overview

Where to even begin? This is the Swiss Army Chainsaw of treble processing plugins. It'll do Slew, GoldenSlew, PlatinumSlew, or any combination of them, forwards, backwards and inside out. I hesitate even to recommend it as there is no real introduction to it, or any other plugin or processor that will really teach you how to use it. If you'd like to just tame unruly high frequencies, you can still use GoldenSlew or PlatinumSlew, and as long as you can still hear audio coming out you're fine (don't crank up Slew or GoldenSlew all the way to 1.0 unless you want to sample and hold, because they will do what you asked).

But if you're still reading, here's what you get extra in EverySlew, which is mainly for me to use developing versions of Console that sound like real analog desks.

Firstly, the Depth control gives you number of stages, with full crank being the equivalent of GoldenSlew or PlatinumSlew. For many sounds there will be no difference between the full ten stages those have, and much fewer. It'll be hard to hear. Fewer stages means lighter CPU load, so I'll be finding optimal settings here, but it also means less of the 'golden' effect when given extreme inputs. When used to take off only the brightest highs (more on that later) you can use fewer stages with no penalty. Two or three should suffice: 0.2 or 0.3 or so.

Secondly, the Halo control gives you a terrifying, industrial meltdown of a sound that also introduces attenuation into the deep bass. I called it Halo because it brings in an odd sparkliness and energy that could come in handy. It uses another level of previous-sample to try and identify actual corners, changes in the angle of the wave, like my DeEss and Acceleration plugins do. I've never got this algorithm to work until now: having made it work, it's a strange and unruly thing. Realistic settings will all be rather low, especially if Slew is anything like obvious. HIgh Halo settings are a kind of terrible distortion I've never quite heard before: I expect this to be used in anger to make some very aggressive noises not quite like any other (which is always handy, right?)

Lastly, you've now got a dry/wet. But not JUST a dry/wet, an Inv/Dry/Wet. Dry is 0.5 on the control. Crank it up and you have full wet… but set it to Inv, and you can make it cancel out the dry signal. When you do that, it shows you only the bits that are slew clipping, and silences everything else. So, for the first time, it's a slew clipper where you can monitor the clipping only, and directly hear exactly what the thing is doing. And this is handy, because the effect is very hard to hear at the levels it should be used! It will tend to make things sound exactly like they already did, except with glue and space in the mix, combing over the stray edges and points. Setting it to Inv means you can hear the points being put into place. Also, if you're using Halo, you can hear when that begins to reshape the effect, bringing in lows and so on.

EverySlew isn't for everybody. I made it because I'll need it. I share it because that's what I do. If you're the sort of person to like this sort of thing, I hope you like it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

EverySlew processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/EverySlew)

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
