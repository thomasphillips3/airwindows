# kCathedral2



## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Stable |

## Description

a giant reverby space modeled after the Bricasti Cathedral

## Detailed Overview

Here we go: this should do nicely.

This is still a 5x5 Householder matrix like the last time, but that's about the only similarity, and it's not at all the same matrix as last time. I am keeping that as kCathedral because I know full well that people find uses for things, but you can hear pretty plainly in my video on kCathedral2 that this is in another league (as they will all be, going forward).

How was that done? A lot of it was time spent generating possible reverb matrices. There's a wide array of ways to evaluate how those become reverbs, none of which existed when I made the original kCathedral. I knew what I wanted but I had no way to measure it… and no way to generate thousands, millions, billions of possible options and automate the process of throwing out the metallic or lame ones. And that changed, over months of work on the tools.

There's also new things that didn't exist in the more purist, uncompromising kCathedral. The new one uses one of my reverb delays differently, by turning it into a single solitary allpass (well, two, one per channel) and also adding the very subtlest of modulation to just that one allpass (not inside it, as a separate effect). None of this was present in the original, but even though it's only the tiniest amount, it's felt.

But most of all, this time around it's using a completely different approach to early reflections. The real Bricasti Cathedral uses early reflections so strong I mistook them for dry signal being let in. Original kCathedral used a 3x3 matrix, very gingerly, trying not to be obvious because I thought I was hearing dry energy off the Bricasti, therefore the early reflections had to be much quieter, right? kCathedral2 uses a 4x4 matrix… which means it's able to literally use a patch from ClearCoat/CloudCoat, except without regeneration (the sound literally bounces away into the cathedral and doesn't even enter the deep reverb field). That's early reflections that can stand alone as their own reverb.

It's subtle, but it's also where I was able to step away from the Bricasti sound and try to establish my own. I think you'll find that the deep room tone is about the same, and the depth of space, but I want those early reflections to be a lot more diffuse (but NOT allpassy), so I've scaled them up and spread them out. It should sound more like detail in the actual room rather than an obvious back wall, which I think will be more useful for how I'll be using it. And I've got a lot closer to that textural butter-sound of the real Bricasti, while retaining some of my own goals for the project.

Welcome to kCathedral2. Oops, I did it again (this time more like what I intended for the first time). Thanks to my Patreon patrons, who are literally the reason I can persist at goals like this, and without whom I might have to stop halfway and not get to stuff like this. Hope you like it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Early Reflections]
    A --> C[Diffusion]
    C --> D[Feedback]
    D --> C
    B --> E[Mix]
    C --> E
    A --> E
    E --> F[Output]
    style C fill:#6366f1
    style D fill:#8b5cf6
```

## How It Works

kCathedral2 creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/kCathedral2)

**Categories**: Reverb

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Reverb](../categories/reverb.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
