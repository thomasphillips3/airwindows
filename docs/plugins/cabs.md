# Cabs

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

an Airwindows guitar speaker cabinet simulator

## Detailed Overview

I’ve been asked for ITB guitar plugins before. Never been all that interested, because I like real amps and real tubes etc: have never found a lot of enthusiasm for going to great lengths to digitally fake all the colorations of some amp/speaker or other, because when the soul’s not there the color is irrelevant.

This is different. I took on the challenge of updating my old Cabs plugin: originally dynamically convolved cab impulses, except they hadn’t been MADE with that in mind so it became a series of wild experiments. I wasn’t happy… then.

Cabs completely overhauled everything I’d attempted. It’s undersampled, so it’ll run on whatever sample rate you like, efficiently. It’s got the same tricks of allowing you to heighten the particular speaker coloration it uses, or dial it right back to nothing.

But around that core is a completely different approach to getting ITB amp tones. I’m using the cab size and ‘room loud’ controls to let you dial in the exact presentation you want, from clear and up front power-soaked clearness to complete wall-of-stacks meltdown, and beyond (in classic Airwindows fashion). This is done through an alternate approach to loudness emulation based on the destruction of audio signals through ultimate volume, such as a Space Shuttle takeoff, and what happens to the waveforms there.

I think you should listen to it. Careful that you don’t jump for odd settings right away and get confused: for instance, settings of Room Loud beyond say 0.6 are not really real-world things. Settings of the cab tone intensity beyond 0.6 or 0.7 might be a bit weird. The way the cabs take on character and intensity is related to cab size: everything is basically related to everything else. You have to know what sound you’re trying to get, to clone something real-world. This is not a preset box, at all, at all. You have to be a real guitar tone maven to dial this in to convincing amp clone territory.

OR… or… or!

You can use the range of adjustment here, with the controls that give you a basic idea of ‘what you’re doing and how you want it’, combined with for instance Edge or the upcoming Dirt plugin (softer saturation) to get tones that DO NOT EXIST but act like real amps in significant ways. You can get tones that you can’t get in the real world, and dial them in to match what’s in your head: in some cases maybe to a point that the real world amps couldn’t reach.

And track through them because the whole rig (when using entirely Airwindows plugins) runs NO LATENCY, so it’ll feel as close as it can to the real thing, and respond with electric immediacy.

And then unlike any real amp situation… once you’ve got the final mix done, you can wiggle any of these parameters to where they need to be for THE SONG and tune the tones to best suit whatever else is there, even if it didn’t exist when you were tracking it. This is a freedom of the DAW experience (don’t go too overboard, make decisions!) and it might bring you the results you need.

And all of this can be lightly applied to any other tone: real genuine amp-and-cab that was tracked too quietly or didn’t pick up enough mojo, synths, drums, you name it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Cabs processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Cabs)

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
