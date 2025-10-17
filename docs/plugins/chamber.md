# Chamber

![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Reverb |
| **Type** | Reverb |
| **Status** | Stable |

## Description

a feedforward reverb based on the golden ratio

## Detailed Overview

I actually meant to do something completely different. Honest.

It was time to dig into the feedforward reverbs again, maybe rearrange them in some interesting way. Do something with the geometry of them, have them go two-into-three-into-four or something along those lines, and we were hanging out in the Monday coding livestream, starting to experiment… and one of my crew tossed out a sequence of numbers. Fibonacci numbers. Could we hear what those sounded like as delay constants?

Wasn’t bad. Chat got buried in Fibonacci numbers for a while: we are always enthusiastic at finding weird applications of things that shouldn’t be any use. After all, to get reverb tails to become seamless, the delay constants have to be set up properly. Prime numbers are key. Fibonacci sequences have nothing to do with this. And then, someone in chat observed… as the Fibonacci numbers get bigger they start approximating to the golden ratio.

Yoicks, scooby! We’d better try it! AND THEN…

Chamber is a feedforward reverb, using three banks of four delays each in a Householder feedback matrix, except it’s feedforward. Only the very end feeds back into the beginning again, just like Verbity, just like Galactic (it is dual-mono like Verbity, as its peculiar merits fit well with a dual-mono arrangement). And the delays go to a longest delay (maximum delay size) and each one in turn, back to the first, is exactly the golden ratio smaller than the previous. It’s like a big spiral of delay times, perfect to lots of decimal places. If you listen to just one instance of each delay (by turning Longness to zero, and Chamber lets you HAVE literally zero feedback), that’s a weird stuttery slapback. By itself, an arbitrary little chirp, a complicated slapback that doesn’t sound particularly interesting.

And then if you turn the feedback up, with Longness, it stretches out into a continuous, seamless, perfect reverb tail, just as if all the delay times had been worked out to be perfect little prime ratios.

This was an astounding discovery. It means you can dial in any degree of feedback or none, use any delay time (everything’s calculated out on the fly), do anything with it and it’ll adapt. It’ll always sound like a chamber, hence the name, but it’s maybe more malleable than any reverb I’ve ever made. And to make it even more malleable, Chamber’s Darkness control is tweaked so that the fall-off over time is always accurate to the sound of audio decaying in air in a theoretically ultimate room (studied from recordings of giant underground concrete cisterns) but the tone-shaping is darkened using very warm, basic IIR filters. And on top of that, a new control for the feedforward reverbs: since Chamber is such a studio tool, I gave it a highpass. So you can plunk it on any sort of buss or channel, run it mostly dry, bring in the reverb (Chamber and Verbity are designed so as you add verb, the dry remains unaltered until you get to 0.5 on the Wetness control, at which point the verb is at full volume and you start fading the dry signal) and then begin dialing back the bassiness of the reverb without touching the dry. Very useful for a chamber or plate send, and built right in!

Hope you like it. Oh, and one more thing: in working on this, I found a bug that was in the Undersampling code I use. The bug was making a bit of unwanted edge, only in high sample rate stuff, only above 20kHz. I’d had someone discover this in Verbity, but I didn’t know what to do other than filter it at the time, and hadn’t done anything yet.

So now (as of right now: redownload what you need) Verbity, Galactic, IronOxideClassic2, and Chamber are FIXED. Go back and redownload them, or get them out of the collections for various different platforms. They have all had the ultrasonic noise cleaned up: there is still a touch of audio there as part of the algorithm, but it turns out it’s much less than I thought and that’s reflected in cleaner sound. It should not change saved mixes significantly as it is entirely supersonic, but if it did it would only help as the traces of noise weren’t useful for any purpose, they were a bug, samples being slightly out of order at 96 and 192k. No change at 44.1 or 48k.

Chamber actually goes a step farther, in that I added more code that subtly averages the supersonic samples… that can apply to new plugins going forward, but Verbity, Galactic, and IronOxideClassic2 don’t have that as it could work like a tone change. So, compare the new Verbity to Chamber if you’d like to check out the tiny amount of added depth we’ll have going forward.

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

Chamber creates spatial effects through algorithmic reverb. Use it to add depth, space, and dimension to your tracks.

## Usage Tips

- Less is often more - start conservative
- Use pre-delay for clarity
- EQ the reverb return (cut lows, sometimes highs)
- Match decay time to song tempo


## Related Plugins

Browse other [Reverb](../categories/reverb.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Chamber)

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
