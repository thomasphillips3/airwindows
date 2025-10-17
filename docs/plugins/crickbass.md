# CrickBass

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

a flexible but aggressive bass tone for dual pickups

## Detailed Overview

I consider this a utility plugin, and maybe it'll find utility with you too. What's a CrickBass?

Chris's Rickenbacker Bass, set up with two DI inputs for neck pickup on the left and bridge pickup on the right.

Now you might ask, which Chris? Well, obviously, Chris from Airwindows, but this plugin really came into existence when I worked out some of the details about Chris Squire's Rickenbacker tone… because this is also in the style of what he did.

The trick to Crick is, that bridge pickup is rattly and abrasive and would seem to be a great candidate for distortion and re-amping. And the neck pickup's right up by the neck, thin and relatively low impedance, and would seem to be a good candidate for clean and accurate low-end.

And that's not what Chris Squire did, and when you hear and play through CrickBass you understand why that's not what he did. Squire liked to overdrive, not the bridge, but the neck pickup. That rattly clangy bridge was kept clean, even though it sounds amazing cranked through an amp.

CrickBass is a composite of the Airwindows plugins BigAmp and LilAmp, with BigAmp on the left to take the neck pickup and distort it, and LilAmp on the right to give the right amplike qualities to the bridge pickup. Both share the same set of drive and tone controls, but the controls cover different ranges on the different amps to produce a range of sounds that should all work and adapt to any stereo bass (as in, neck and bridge pickups on separate outputs). Use the controls on the bass to make subtler adjustments. Adjust the drive for how much gain you should have, remembering that the neck pickup is supposed to overdrive enough for a huge foundation of the sound, and that the bridge pickup is meant to be cleaner but not necessarily totally free of grit. Then adjust the tone so that clicks, string handling and so on, hit with the tone quality of whatever snare you're making the bass merge with.

Both of these amp sims make a point of applying anti-aliasing filtering as part of the EQ filtering that helps mimic a cab, so they're far from full-range but good at sounding analog. Even when set up to be bright as hell, that's still 'bass amp' bright rather than 'supertweeter' bright. The idea is to match other elements in the track with your bass string percussive noises, so they jump right out and hit like a train.

And then if you're NOT aiming for a really abrasive proggy tone… handle the string in such a way that it's not making vicious SKRONK noises :) maybe dial back the tone but do it with your playing, and let the 'amp' continue to deliver midrange articulation to the mix. That'll sit in the mix more effectively than something which sounds deep and bassy in solo.

If you're looking to get REAL abrasive, the remaining ingredient is fret buzz, and this combined with a really low action and heavy pick attack will get you into the Chris Squire zone very nicely (which some people don't like one bit… matter of taste and style, really).

You can also run a mono bass into it and it'll still work, but the intention is for neck pickup on the left and bridge pickup on the right. It'll sum the two sounds to mono in any event.

If this is the sort of thing you like, I might have given you a quick Crick in the neck (and the bridge!) and a real short-cut for bass DI tracking. Since this is a plugin, you can track right through it (zero latency) and then if you must do something else in the final mix, you still can. But it's meant to deliver this sort of tone in the most direct, no-fuss way imaginable. I'm looking forward to using this on everything: the extreme rawness of BigAmp and LilAmp turned out to be ideal for this purpose. If it's also useful to you, then yay! Bonus. Or of course misuse it, run breaks or synths or drums into it. Have fun!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

CrickBass processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/CrickBass)

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
