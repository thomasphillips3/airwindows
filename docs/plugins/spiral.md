# Spiral



## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Stable |

## Description

the new best smoothest distortion algorithm

## Detailed Overview

What if… the building-block sine-based saturation routine I build so many things on, which I thought was the smoothest distortion you could have, is NOT the ideal distortion?

I was watching a youtube video by Brady Haran, on his ‘Numberphile’ channel. It was about the golden ratio, and it showed the little drawing you’ve maybe seen, where you take a golden rectangle, and then make a square on it and put a circle segment (like when I use sine curves for my distortions), and then make a smaller square next to it and a circle section on that which connects, and so on ad infinitum. A ‘spiral’ like a seashell, a golden ratio spiral.

And Brady says, ‘of course this isn’t actually a spiral’ and my mind: blown.

Because of course it isn’t. It’s circle pieces butted up against each other, and only looks like it’s connected because it’s pretty flat going through those points. But the rate of curvature changes really suddenly and drastically at those points… and does it the same way, at the zero crossing of ConsoleChannel, Density, PurestDrive, PurestWarm, Channel, and lots and lots of other plugins I’ve made. It’s part of the ‘fatter, smooth’ sound of some of my distortions. Seemingly really fat and analog-sounding, but there’s a discontinuity as you go through zero, which is why it makes the audio sound obviously different.

People do like making the audio sound different, but people HATE the sound of discontinuities. An old version of Channel where I hacked in a ‘flat’ undistorted section, got me a huge blowback of dismay and outrage until I put it back to the simple sine-based one. People are incredibly sensitive to second order discontinuities, where the output number will be 0 but the direction things are changing will suddenly be the opposite. That’s what made the old ‘New Channel’ be such a failure: the center of the wave was flat no-distortion, and then without making a visible discontinuity it would suddenly change to ‘tighter sine-based saturation curve’, both on the negative and positive sides of the wave. It would look perfectly normal but people just hated the sound. Now I know why. And now it turns out the sine based one HAS a discontinuity, at the zero crossing, right where you’d get class AB and B distortion, and it never occurred to me.

And I can fix it, and turn the code for that part into ONE line of reinvented original code, which will be open source because I’m Patreon-supported and don’t have to stop people using my good audio code (they only have to credit me when they use it: it will be very possible to tell when they do. They don’t have to pay anything since it’s an MIT license, and they don’t have to open their own source, just publically credit that they used my Spiral code).

And of course I did: here, have Spiral, free. You can just install this and listen to it, if the video and the post are too long. This is the proof of concept which can be used in several useful ways. There are no controls, at all. You can gain stage into it and do stuff with it and sit it on the top of every track like it was PurestDrive or Channel, or use it as a 2-buss clipping stage, where it will clip to around -1.4dB with about -0.4 intersample peak maximum (so it is Mastered For iTunes friendly, used as a final clip). It also has a ‘freak out mode’ if you massively overdrive it, and you can do that with things like uncompressed drums, and it makes noises you’ve never heard before, or when used more gently it just sounds like the ultimate analogification.

I really had no idea I could do a basic saturation algorithm (which still uses long double precision sines as part of it) that was that good. It’s a considerably bigger sonic improvement than the new noise shaping technique, because what it does is on a far higher level… though of course it also is using the new noise shaping, for good measure. All the latest everything, right here.

Bear in mind, the original sin()-based one in Console5, PurestConsole etc. is still optimal for Console5 encode/decode because it can be lossless and has significant effect at low levels. My tape emulation stuff uses the ‘fattening’ effect of that on purpose. I can’t just go through and replace everything because all the sounds will change. I have to re-voice everything that would take advantage of the new code, and I’ll do it, and it’ll take time and effort, and probably become new versions of things so you can still have the ‘sine fatness’ versions if you want them. I don’t like taking sounds away from people, and old tones shouldn’t be removed or made inaccessible.

But what if there’s a WAY better analog-sounding distortion effect based on the way that the ‘constructed’ golden ratio seashell/spiral made of circle sections in boxes that get smaller, is NOT correct because much like the simplest sine-based overdrive, it doesn’t start with zero distortion but with the same tiny distortion the whole time (which, in joining to the opposite pole, makes a discontinuity you can’t see much like the golden ratio ‘spiral’ has discontinuities you can’t see?) …and I fixed it?

Try Spiral, and I will get to work incorporating this into my library of audio plugins that I make available using my Patreon.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Spiral processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Spiral)

**Categories**: Saturation

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Saturation](../categories/saturation.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
