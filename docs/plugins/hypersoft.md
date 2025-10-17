# Hypersoft

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Saturation |
| **Type** | Saturation |
| **Status** | Latest Release |

## Description

a more extreme form of soft-clipper

## Detailed Overview

A funny thing happened on the way to posting the video for this…

Hypersoft is a new softclipper. Its purpose was to answer the question 'what if a softclipper, that develops a sharper and sharper corner as you overdrive it, placed that corner NOT up at the maximum volume, but somewhere else?'

I feel like this isn't investigated because it's 'wasting' the distortion, assigning it to quieter parts of the sound, and that it's been such an assumption that everything be LOUD, that nobody would even try such a weird experiment. But I've been working on Airwindows Meter, and looking at how hit records in my collection produce these 'clouds' of peak energy and slew energy that always take up more space than modern mixes allow. And so, I wondered: what even do you get, if you used soft-clipping and techniques like wavefolding to produce a 'curve' where the 'flat-topping' instead became a circle or something, and it tries to get progressively sharper somewhere in the middle?

So I started working with test tones, sine waves, and hashed it out for a while on livestreams and made a thing that produced this curve, plus the wavefolding caused the 'flat top' that you eventually hit, to stick around longer than it normally would, and then curve down into a strange point. When you send a ramping-up louder and louder sine into this, the harmonics it produces go from very soft and mellow, to more sharp and high-frequency, based on how loud the sine was. (compare to a hardclip, where you get highs immediately and then they mostly don't change.)

On music, it's a wildly grungey dirt-factory that's almost as colorful as class AB distortion, for some of the same reasons. The place that the 'curve' changes most sharply is no longer at the top. But it's still a softclip, so quiet sounds don't grind as they would in class AB distortion. It goes from subtly punchy and textural, all the way to aggressively gnarly.

And then I made a video and used a simple room-miced drum beat, a basic boom-bap played as well as I could, just two mics placed in front of the kit, and cranked up Hypersoft until I thought it sounded pretty amazing, thought I'd be able to use something like that.

And ContentID flagged it as Rammstein, 'Das Alte Leid' and refused to let me monetize it. (ads that run are out of my hands now, and go to Rammstein.) With no other processing at all, my simple drum playing has apparently become Rammstein enough to fool YouTube. The raw mic feed wouldn't do that at all: Rammstein is a highly processed modern-metal sound. But there it was.

What's happening is this: drum impacts are being allowed to persist (like in the highly sculpted sound) but the body of the sound is brought up and reshaped interestingly, producing a 'big' effect that acts kind of like the sound is experienced in real life. Pushed hard enough the dynamics will invert, but it'll take a lot to do that. It's a new form of softclip which I think lends itself to drums, but will probably also suit basses.

You get Input, Depth, Bright and Output. 0.5 is as neutral as it gets though the effect will add a little boost just by reshaping. Depth specifies how many additional wavefoldings to apply (each runs its own sin() function so high settings will cost a bit more CPU) and more Depth intensifies the effect, making it more focused and colorful. Adding Bright means all the wavefoldings will be used even if they're going to alias: less Bright means the wavefoldings start to bail out when they risk aliasing. Note that this WILL NOT fix aliasing! It changes the tone in such a way that you can dial in the amount of treble hype you get out of Hypersoft, or leave it as a darker effect.

This will not be as effective a loudenator as just clipping the crud out of something, before you ask. This adds harmonics and intensity while retaining dynamics. In fact it tries to heighten dynamics by throwing more overtones when the overload is greater. I think it's going to be really, really useful but not for simple loudenating: if you're after intensification and impact, Hypersoft might come in handy. I hope you find it helpful :)

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

Hypersoft processes audio in the Saturation category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Saturation](../categories/saturation.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Hypersoft)

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
