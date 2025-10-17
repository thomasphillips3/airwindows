# Highpass2

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

an unusual-sounding variable-slope highpass filter

## Detailed Overview

So, the way the interleaved IIR filters act in Highpass is like this: the harder you filter, the more the filter rolls off the very highest frequencies. That’s because it’s like the inverse of Lowpass2. It’s got the same four poles, the same type of tone doctoring (in this case, loose and tight for what bass remains) but the way to use it might be distinct.

I think it works well for getting a subsonic roll-off (perhaps with the four poles of filtering, like a mini ToVinyl highpass) and then using the Loose option to let the bass move a little more. I found it more difficult to distinguish what the funny-named slider was doing, but it’s still intense on high settings. And it’s great for trapping in high percussion because of the clarity of the passband and the way it rolls off over 20K (or higher, if you’re at higher sample rates).

And of course, like Lowpass2, this is here to fix the limitations of the original Highpass on those very same sample rates, going from no filtering to total filtering.

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

Highpass2 shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Highpass2)

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
