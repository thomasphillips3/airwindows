# Cans

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

a room simulator for headphone mixers

## Detailed Overview

Lots of people out there are stuck mixing on headphones, whether it's due to bad acoustics or noise complaints or simply not having a high-quality monitoring situation. After all, even if you put together speakers as revealing as NS10s, the  amplification and acoustic environment have to support them, plus you've got no hope of extending the monitoring to the bass without serious subwoofers and even more acoustic treatment, and this quickly expands to become unreasonable. So lots of people are stuck with headphones.

And why is that so hard to make work? A simple reason. Peak energy shapes the whole character of the sound (or lack of character, all too often these days). And in a good control room, it's not just about making everything dead. Diffusion and room geometry play an important role, and the sound always bounces around because that's what happens out in reality. We hear sounds in the context of a listening environment, and through this very specific reverberation, the peak energy makes itself known. But over headphones, especially great headphones that are free of artifacts and resonances, the peak energy just gets right by you. It happens too quickly and is gone before you register it.

In a great control room you get a better sense of what lives in the peak energy, by how sound bounces off those expensive diffusors and fancy wall geometries, giving you that enveloping acoustic space without it further confusing your ear. And there's people out there ready to sell (or rent!) you the pretend versions of various ultimate rooms, perhaps with pictures included so you can pretend you were there. But what if you just got an enveloping acoustic space or five, that you can bend into whatever shape suits your work… for free?

Airwindows Cans is not the same thing that's in the Monitoring plugins. It uses some of the same techniques (crossfade, allpass filters) but runs new reverb algorithms that haven't been used before, because it took days of computer time to grind out these five new verb spaces, all tailored for this one purpose.

StudioA is the smallest control room, and StudioE the largest, but this is not simply a rescaling of the algorithm: each one is a unique space, designed to best represent its purpose. You'll hear the room size most clearly in the way it reshapes the bass. The Diffuse control works like adding more acoustic diffusion to the room (technically, it lets you swap any comb filter for a corresponding allpass filter). Damping provides the upholstery: studio control rooms are not often echoey and 'live', and as you turn Damping down you put up more drapes and acoustic treatment, drying up the highs and mids of the room. Crossfade brings the stereo into a more centered place or causes it to swap sides mid-reverb, and Dry/Wet controls how much of the ambience you're including.

Setting everything to halfway should be a good starting point for headphone monitoring, but you can go wild trying different perspectives. For instance, in real life I have a mix check position that's upstairs in a hallway, well away from the speakers (and I've shown this on mixing streams before). In Cans, you get this by picking a larger room size, livening up Damping with a higher setting, and going more wet so you hear more of the room sound.

You can also, as I demonstrate in the video, just use it as a pretend drum room (or piano room, what have you: a studio space that's not a big hall). Because the early reflections are closely tied to the raw sound, Cans merges with the sound more than typical reverbs, as it's trying to do that rather than sound like a room of its own. Even if not mixing on headphones, this can find use!

But if you are mixing on headphones, the idea is always to find that setting in Cans that works for you in letting you hear and interpret everything in the mix, dial in your sounds and levels, and then turn it OFF before exporting. Because maybe you won't be listened to on other headphones… or maybe you'll be played at clubs, or live events, for crowds… or maybe the future means having your music played through listeners having their OWN version of Cans, or some other invented environment you can't control, in which case layering your pet monitoring environment onto all those places will turn into a muddy mess.

But if you're headphone mixing through your personal settings for Cans that make your favorite music sound like it should, and then you export your music without that interpretation built in, other people can get the most out of what you made over anything from a big club sound system, to a PA, to their own 'virtual space' that makes their music sound the way they want it to sound. Because Cans is about trying to give you a picture of all the energy in your mix, not just what's obvious over headphones. And if you find sound spaces you love using Cans, try building those sounds partly out of aggressive 'room sound making' on submixes and individual instruments, and then partly out of a much more subdued take on Cans on the whole 2-buss… and then turn it OFF for export.

After all, if you went to mix your work in a world-class studio that reveals everything, you give people the mix that environment let you do. You don't just put up mics in the back of the room and give people THAT :)

Hope you find Cans useful. Remember, if you need to make a lot of stuff much more ambient with Cans, do part of it in the mix on stems and instruments, and do part of it on the 2-buss (or monitor chain) to simulate your perfect control room, and then turn the 2-buss Cans off to get the real mix!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Cans processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Cans)

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
