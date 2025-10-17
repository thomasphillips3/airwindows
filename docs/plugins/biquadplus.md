# BiquadPlus



## Quick Info

| | |
|---|---|
| **Category** | Biquads |
| **Type** | Biquads |
| **Status** | Stable |

## Description

Biquad plus zipper noise suppression! For twiddling the controls

## Detailed Overview

By request, a kind of bugfix!

Understand, a simpler implementation of a biquad filter isn’t a ‘bug’, exactly. I may have not had everything figured out, but if you’re designing fixed filters or looking to tune in EQs on something in your mix, the biquad filters I’ve been making are actually better. Without the extra smoothing code they run more efficiently and eat less CPU, and they’re still useful, plus there’s less to them so they’re more approachable.

But, a lot of musicians seem to enjoy cranking the filters around… and now that I’m using Bespoke all the time, I can put an LFO literally on any damn thing by rightclicking it. And it wasn’t all that difficult to do… I rolled it in to some documentation upgrades I did on the advice of Paul from Surge Synthesizer. One thing about hanging out with the open source music people is, stuff starts happening faster than you could possibly imagine. I had a crash bug in Bespoke on some strange things I needed to build into my main music making procedures, and Ryan had a fix the next MORNING. It’s daunting and wonderful to hang out with these earnest, motivated people.

You’ll see more on that, sooner than you think.

But right now… enjoy a cleaner, smoother Biquad, plus zipper noise suppression! I needed to come up with my Airwindows way to accomplish this, and got it done. More to come.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BiquadPlus processes audio in the Biquads category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Biquads](../categories/biquads.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BiquadPlus)

**Categories**: Biquads

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Biquads](../categories/biquads.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
