# UltrasonicMed



## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Stable |

## Description

two stages of supersonic filter, for using inside digital mixes

## Detailed Overview

Hi! This is just what it says on the tin. Airwindows Ultrasonic is the stacked-up, five-biquad filter that rolls off everything above 20k, so in theory it has no sound of its own. It’s there to work in high sample rate mixes, between plugins that have nonlinearities and don’t have their own filtering (some of mine do, like Console7) and it will clean up the top-end of a digital mix.

But, the original Ultrasonic has SO many stages of filtering that it starts to become audible, softening the highs, and if you used lots of them you’d eat your CPU and would be over-processing.

So, enter Ultrasonic Lite (and Ultrasonic Medium).

These are the same sort of thing, except Ultrasonic Lite has only one stage of filtering, and Ultrasonic Medium has two. They also start a teeny bit higher, on the assumption that if you’re reaching for a Lite version of the filter, you’re looking to not hammer your highs too much. Ultrasonic Medium also subtly staggers the placement of its filters so it has a two-stage roll-off that is hopefully more natural sounding than just doubling up Ultrasonic Lite on its own.

Use these just like you would use Ultrasonic, if there are places in your digital mix where you think you’d benefit from suppressing ultrasonic frequencies. These are not brickwalls: the idea here is that you can sprinkle these throughout your mix, anywhere you like, both before and after things that are nonlinear and distorty. For the strongest possible effect, use the original Ultrasonic… but in places where you don’t need that much help with the ultra-highs, try Medium or Lite and apply a cleaner, subtler filter that lets more of the air through.

If you’ve got something that’s causing an aliasing that will give problems further down the mix chain, and you put Ultrasonic Lite in front of it and the aliasing that would’ve bounced back down to 40k is turned down before it even aliases, making that unwanted 40k quieter… and then there’s another Ultrasonic Lite afterwards and that directly turns down the unwanted, aliasing 40k… then you’ve got a gentle, distributed aliasing suppression across your whole mix, that will really control the tendency of aliasing to just build up and go critical on ya :)

(followup: turns out using many instances of this WILL tend to roll off your highs, where using the full version won't. This is because the full version's doing more processing, but creating a steeper filter. This insight led to UltrasonX, and later versions of Console)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

UltrasonicMed processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/UltrasonicMed)

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
