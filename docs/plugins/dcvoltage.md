# DCVoltage

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

literally a DC control voltage, in a plugin

## Detailed Overview

This is exactly what it says on the tin. Do NOT just put this in a mix and crank it up to see what it’ll do. If your whole system is DC-coupled you will blow your woofers, just like that, after a big ‘whump’. I will not take responsibility for damage caused by misusing unusual tools.

What SHOULD you do? Here are some ideas.

There is no DC offset filter nearly as good as applying an opposite offset. Use metering, perhaps option/alt-dragging on the slider if your DAW permits it, to cancel out a DC offset without any sonic penalty at all. This is called a ‘DC servo’, but digitally. If you can get it perfect and then bounce files so you can work with a center corrected section (so you don’t have to get a pop from turning it on or off) this would be the highest quality way to get rid of a FIXED DC offset without altering any of the bass at all. It’ll retain right down to 0.001 hz or whatever, and only kill what is totally unvarying DC.

If you have a converter that’s DC coupled, and analog modular synthesizers, you can use this to create and modulate control voltages. Use it as a voltage source and then mix stuff together using DAW routing much like you use patchcords on your synthesizers, and be careful not to route control voltages to your monitors! I know there are people who’ve done odd things to get DC voltages inside their DAWs. Now it’s a lot simpler :)

This plugin may not be any use to you, and don’t play with it if you don’t know what it is. If it is useful to you, you already know exactly what you’ll do with it, so go right ahead, now you’ve got DAW control voltages out of a simple plugin.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DCVoltage processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DCVoltage)

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
