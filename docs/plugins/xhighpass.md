# XHighpass

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

a distorted digital EQ, inspired by retro sampler DSP

## Detailed Overview

Continuing the weird filter pursuits while I work on the M1 compiled VSTs! This is another distorted filter, except that if you distort the insides of a biquad highpass it makes NASTY zapping noises.

So… yay?

Those who like that sort of thing might like this. It’s pretty good at making really mean aggressive highpasses, except that you can’t clean up the results by dropping the frequency down into the bass and subs: it will just clip easier, which will cause more horrible zap noises. So I guess, only try this if you like that sort of thing. They can’t all be zingers, though this one is quite literally a zapper :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

XHighpass processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/XHighpass)

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
