# Galactic2

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Latest Release |

## Description

a super-reverb REdesigned specially for pads and space ambient

## Detailed Overview

Galactic has been a huge success, no pun intended. It might be the most popular of my first batch of feedforward reverbs, and it's still available, from its banks of 4-wide householder matrix delay lines, to its pitch shift stereo widening.

So, why revisit Galactic? What is there to even improve? Well, it's a matter of taste. My newer big reverbs and realistic reverbs go for a bigger reverb matrix with a distinct, more organic texture to it. And I wasn't really satisfied with how you worked with Galactic: I'd imagined a thing where you'd have reverb space going, and then you'd 'paint' in other sound, perhaps with a slider, or just by overloading the existing space with other stuff.

And so, here we are. Galactic2. Drive, Sustain, Darken and Wetness. And a tone that owes more to the K series plate reverbs, than Infinity or Verbity. Sustain starts to feed back forever a little ways past two-thirds up, with halfway being long decays, and very short sustain being your kill switch. It'll creep up in gain at full crank, so be careful with that. Drive is how you feed in new audio while it's going, Wetness is probably going to be full crank for most use cases, and Darken goes from totally, scintillatingly bright to mellow and distant-sounding, both as part of the total output of the reverb, and as part of the feedback loop (so if you have bright stuff going, and you Darken, your sustain will start to get darker as it continues, which can add realism).

I keep saying it's like the kPlate reverbs, but I checked the code and it's still 4-wide Householder matrixes, like the original. So what makes this so different? Its handling of stereo, is what. Either you'll love or hate it. This is why you should love it. Unlike the original Galactic, this isn't a pair of matched reverbs using pitch bends to stereo-ize them for mono things. Galactic2 is a SINGLE giant stereo reverb that uses all the same delay values, but uses them crossways: one channel accesses the matrix vertically, the other accesses the matrix horizontally. It's 'the same', but all the echoes are arranged differently. These are way harder to come up with but it's what was used on the kPlate reverbs, except those are 5x5 matrixes and this is still a 4x4. There's just a teeny bit of crossmodulation to round it out.

What this means is, if you put stuff in the left, it makes a sort of cloud of reverb sound that's also mostly on the left. If you put stuff in on the right, likewise: you'll get 'space' happening mix right.

And if you put stuff in mono… you get WIDE center content. The whole texture is wider than what original Galactic can do, without use of chorusing or pitch shifting to widen it. That gives it a completely different character, which is why you've still got original Galactic to use if you want. This is a second bite of the apple. It's about trying to get even deeper into space, and I hope you enjoy it :)

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

Galactic2 creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Galactic2)

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
