# kCathedral4



## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Stable |

## Description

the Cathedral sound expressed as distant space

## Detailed Overview

Flagship reverb takes whatever the newest technology is, and expresses it in the flashiest possible way. kCathedral's always been that for me, but the technology's come a long way over the years. And it turns out even kBeyond was only a preview, and there's major upgrades in store. kBeyond was using a literal million echo returns out of 3x3 and 6x6 matrices, but as the 3x3 only produces 27 echoes for early reflections I hadn't bothered to implemented it as a full Householder matrix (involving multiplications for non-4x4 matrices, and some of the feedback being inverted, and the 3x3 doesn't actually use local feedback even)

And then I tried it… the video shows the two files I made to see what would happen, and the one done like it is in kBeyond is sparkly and complex, and the one with the real Householder is a quantum leap in depth and realism.

And that's what's in kCathedral4, along with the Pear2 algorithm for filtering the deep-field reverb feed. It can do deep verb even unfiltered and bright, but when you mute it down to Bricasti degrees of darkness, you get a spaciousness that's beyond anything I've had.

The algorithm is generated using the genetic algorithm: trying 'populations' of reverb constants and measuring how well they produce a result. I've learned things like how the total delay lengths of matrix paths added together are what need to add up to primes to sound right: it's been really complicated, but worth it. I'm going to have some amazing small rooms and loud halls too, chambers, you name it. We're just going back to the Cathedral, because it's a really cool sound. You could put choirs or pipe organs or Tangerine Dream in it, but you can also put whatever you like in there. Doesn't matter what you start with, you'll end up with sound you can bathe in.

I'll keep working: remember, each reverb plugin is designed around a dedicated algorithm tuned using the Genetic Algorithm to optimize for whatever its vibe requires, so the character of each one will be different in ways beyond just adjustment of the parameters. You do get parameters though: regen, filter for the deep field, loudness of the early reflection section. I'm working on extending this and look forward to doing more with it, but kCathedral4 is for you to enjoy right now :)

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

kCathedral4 creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/kCathedral4)

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
