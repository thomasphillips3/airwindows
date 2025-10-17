# Texturize

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Noise |
| **Type** | Noise |
| **Status** | Latest Release |

## Description

a hidden-noise plugin for adding sonic texture to things

## Detailed Overview

It all started with snake oil… or should I say secret snake oil?

There’s talk lately of a plugin which has gotten a rather critical reception: a plugin said to put subliminal noise into the sound, to produce near-magical enhancements of tone and all good things. But you can’t hear it directly… you gotta vibe it, listen and embrace the magic, and then you’ll believe…

People were, shall we say, critical of this approach :)

Since I’m free to code what I like, thanks to Patreon and all (and thank you, all who’re pitching in there) I took an interest, and now you have Texturize. It is NOT literally this other plugin, or their patents, or the specific method by which they make the magic concealed noise that makes everything better.

But what it IS, is a riff on several previous plugins I’ve had for years and years, to produce a very similar function… but THIS one, you can tweak and you can also crank it up and listen to only the noise to hear what it’s like. Ruin the magic… but learn how the trick is worked. And it turns out it is really not snake oil at all… it’s just another thing to do with audio, and it does seem to work, and everyone making a plugin of this nature will have their own ‘take’ on it: if you like mine maybe you’ll try out the other folks’ plugin with more of that open mind, having proved that the concept is sound. Or just use mine, which is open source and free :)

You get three controls. Bright makes the effect key off high frequencies more aggressively, to the point of hyping up energy, and Punchy varies between a softer, fuller sound and a real spiky choppy effect. And then there’s Dry/Wet, the heart of the plugin, where settings of 0.5 or less are probably going to keep the noise entirely inaudible, as it’s meant to be. Not heard… but felt. And the sonic transformation’s really interesting, all the more if it’s not obvious. It reminds me of how tape flutter can bring texture to pure tones, chorusing against nearby reflections for a fatter sound, but here it’s just noise… but noise doctored to act like the music and hide behind it.

And then of course you can crank it up until you plainly hear hints of the noise… or slam it until you only hear the noise. But to actually use the plugin properly, keep things at 0.5 and don’t push Bright or Punchy or especially Dry/Wet to where it’s gone too far: tweak it on that subliminal level, turning Wet down if you need to, and see what you get.

I might well start using it. It really does seem to work. Go ahead and fool with it and strip all its secrets… and see whether you believe, too :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Texturize processes audio in the Noise category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Noise](../categories/noise.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Texturize)

**Categories**: Noise

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Noise](../categories/noise.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
