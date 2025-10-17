# SubsOnly



## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Stable |

## Description

a mix check plugin that shows you only the extreme lows

## Detailed Overview

By request, here’s my mix monitoring tools, for VST and Audio Unit, Mac and PC! Please remember, these like Guitar Conditioner are control-less plugins so you don’t operate them by opening their windows: they’re either on or off, which probably is shown in your DAW mixer window already.

SlewOnly gives you what it says on the tin: only the difference between samples, expressed as a sample. This produces a super-bright sound with zero latency and absolutely no pre-ring or post-ring. You can do two poles of this filtering: just add another SlewOnly. But, as is, this will give you an incredibly clear and transparent window on the ultra-highs, so you can dial in subtleties in the treble. Beware: don’t switch right back to the normal sound or it’ll sound incredibly dull. Rest your ears for a moment before resuming work.

SubsOnly does the same thing for subsonic bass. It sounds a little like a house party from an adjacent house. You can tweak sub-bass elements and really hear how they’re balancing against each other, and if you’re packing too much into the subs you’ll hear that as well. Get things thumping properly through SubsOnly and it should translate well to all manner of bassbins and subwoofers.

Lastly, these are calibrated (in SlewOnly quite literally: pink noise will be about the same amplitude with or without it, though the tone will be way different) so that you can switch them in and out, and expect roughly the same loudnesses. It’s okay if SubsOnly is louder for fullbodied bass: with that, it’s not so much about level-matching, it’s about getting your sound (at whatever desired loudness) and then having the bass still make sense through SubsOnly. If you’re madly overloading it, there won’t be groove, just a lot of thunder and noise, at elevated levels. These go on at the end of your master buss, so you can hear what your 2-buss chain did to the sound. Especially if you try and go for ‘commercially loud’ volumes, sanity checking with these tools can be a real silver bullet.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

SubsOnly processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/SubsOnly)

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
