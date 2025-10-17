# LeadAmp

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

an amp sim with a clear, penetrating, vocal tone

## Detailed Overview

LeadAmp acts like one of the ‘normal’ ampsims, but leaning more towards the vocal, fluid, Vox-y side of things. It’s a distinctive voice and even though they’re all pretty simple and direct, it’s really obvious how LeadAmp isn’t the same flavor as FireAmp or GrindAmp: distinctly different vibe even though they are all cut from the Airwindows super-direct amp sim cloth.

The Airwindows amp sims are all fairly simple designs: highpass, cascading gain stages with ultrasonic filtering between them (often tuneable so you can suppress aliasing even at low sample rates, but they're meant for 96k use) and a cab simulator on the end that's dynamically convolved but also a truncated, brief section of tone color.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

LeadAmp processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/LeadAmp)

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
