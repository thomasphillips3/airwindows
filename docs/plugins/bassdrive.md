# BassDrive

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

an old secret weapon, like a kind of bass amp

## Detailed Overview

There was this plugin called BassDrive… and it was a secret weapon. It was unlike any Airwindows plugin because it ran on painfully hard-coded biquad filter code, looked up from calculators online: which also meant it was locked to 44.1K (at least, to get the expected behavior). But it was also unlike anyone else’s plugin of that nature, because it used lots of Airwindows overdrive inside it. The controls seemed to say normal EQ things like ‘bass, mid, treble’, but they didn’t give you those things, they gave you funny bands voiced in a weird way.

And this is because it was the eccentric Airwindows way of trying to mimic the SansAmp Bass DI. Not the pedal form… the rackmount RBI version.

The weird part is I ended up not liking that one (I came to prefer the pedal-form VT Bass) but before I got rid of it, I’d gone and shaped biquad filters to its voicings. But then, I implemented them strangely (note the intense notch at 10K, not present in the real one!) and made ’em overdrive a lot more. So it’s a lot LIKE a SansAmp RBI, but then again it’s totally not because it turned into its own thing.

And then, even though this could be used for bass guitars, I started to hear about how it was working as a secret weapon on heavy guitar sounds…

So this is exactly how the ‘secret weapon’ plugin was. It’s the blast from the past, now also available for Mac, Windows and Linux VST. And I know how eccentric it is, but sometimes that’s the point. I’m working on a bunch of stuff that’s meant to be normal (or at least flexible). This ain’t. It’s just weird. If you hate it, it’s not getting any better, abandon it with a clear conscience. On the other hand if its dark magic speaks to you… then hey, enjoy the new weapon. And rest assured that people who need good behavior out of their plugins will not be finding your secret, because BassDrive will scare them away first.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BassDrive processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BassDrive)

**Categories**: Amp Sims

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Amp Sims](../categories/amp-sims.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
