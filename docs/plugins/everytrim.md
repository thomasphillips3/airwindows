# EveryTrim

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

Left/Right, Mid/Side, and Master in one plugin

## Detailed Overview

EveryTrim is like PurestGain only more so: it is very simply every basic stereo trim you can have (in loudness terms, anyhow!) You get left, right, mid/side, and a master level control. It works on stereo tracks only, as mid/side is meaningless without stereo.

It’s also efficiently coded, suppresses denormal numbers, and uses the same noise shaping to the floating point buss you get in PurestGain. If you need a nice basic gain trim that does all those things (and nothing fancy: Wider is much more sophisticated, and I’ve got an idea for a still more sophisticated stereo-widener plugin that is in the works) then EveryTrim will come in handy. Begone, dull pan-pots! EveryTrim will also be simpler than using EdIsDim and MidSide just to adjust mid/side balances: while you can do that with that pair of plugins, they’re really for doing processing between them using another plugin (any plugin, doesn’t have to be M/S). With EveryTrim, you can tweak mid and side levels directly, in a more obvious way.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

EveryTrim processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/EveryTrim)

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
