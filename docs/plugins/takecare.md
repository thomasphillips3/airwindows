# TakeCare

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

a lush chorus ensemble universe

## Detailed Overview

The idea was to revisit plugins like Melt, with an eye to even more disconcerting sonic spaces like the works of The Caretaker. Seemed reasonable to do. I started off with my Melt plugin, to see what would happen.

Then, in working on Householder matrices, I found that using a Householder matrix for a 3x3 grid of delays (rather than simply using them as delays, which I'd done before, thinking 'what difference could there possibly be?') made a HUGE difference. This is what's creating early reflections in my plugins post kBeyond (which it turned out I immediately went beyond).

So, if you can do that with a 3x3 grid of delays that produces 27 echoes per channel… what if those delays were instead a chorus ensemble machine?

This is TakeCare. Most of the work I did on it, was using synth pads in order to make giant illbient soundscapes, and indeed it's quite good at that. You can get real seasick off TakeCare. I've also set it up so the 'buffer' control can be manipulated to intentionally create horrible noises: at full regen, it'll even feed back at small buffer settings, and it's made to go into distortion a little below full scale in case you want to get real crunchy. It's also using an old Console algorithm internally, to expand the space inside the blast of noise.

And then it turns out that if you keep it more calm, less regen, very small buffers and the depth not too extreme… it's a gorgeous chorus ensemble on something as revealing as a vintage Fender Rhodes. It generates stereo width, supplies a lovely pad of lushness around the instrument, and doesn't have to be weird at all. This could come in handy on things like synth pads, voices, who knows what? Think 'lush stereo chorus ensemble' and dial it in to whatever your needs are. The range on this is pretty nuts, because it was originally designed for radical uses but cleans up really well.

I hope you like it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

TakeCare processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/TakeCare)

**Categories**: Effects

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Effects](../categories/effects.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
