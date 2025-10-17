# Wolfbot

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

an aggressive Kalman bandpass with evil in its heart

## Detailed Overview

So it's possible that I simply went too far.

This was inspired by, and specifically modelled after, the famous transformer DI 'Wolfbox', which I don't have. I had only a youtube video made by somebody who did have a real Wolfbox DI (and at that, not a vintage one) and who was A/Bing it against a different DI. I'm putting this out because I was asked to, but understand that it's a science experiment.

And by that I mean, literal science experiment. It answers the question, 'what happens when you use two Kalman filters to mimic the bandpassing of a vintage transformer DI box?' plus there's a bit of saturation on the end. The saturation is not the aggressive distortion you hear: that's the Kalman filters acting as comes naturally! It's possible that DI bass is the single worst signal you could try to put through this plugin that was designed to work on bass, and voiced using examples of bass and DI guitar. It's possible something has gone quite horribly wrong.

Or.

It's possible that this will come in handy more than anybody imagined. The thing is, I worked real hard to get the 'voice' of this dialed in just right, and THEN checked to see what it was really doing. It has a bit of saturation (should rein in snaps and pops nicely) but the grind it delivers isn't from that, it's from specifically the highpass Kalman filter, which is turning the whole sound into a sort of bass horn! I was shocked to see how much this strange plugin turns otherwise normal DI signals into sort of fat beefy pulse waves. Wolfbot is not gentle, and doesn't have any more controls than the original Wolfbox did, and while some kinds of sounds (drums, snares etc) get voiced in a convincingly 'bandpass' way, other sounds like the DIs it was designed to do, get utterly transformed.

It acts more like a bass amp than a transformer DI, but more like some strange new invention than either… and the specific way it retains the hammering, brutal directness of bass low-mids, while wiping out irritating string-gloss (even on a Rickenbacker bridge pickup) and nuking ALL the real bass to make room for kick drums and sub-synths, means in a strange way Wolfbot entirely succeeded. I have a pile of amp-sims, multiple DIs and transformer DIs, and real amps, and none of them are even close to doing this, whatever 'this' is.

I need to try it in some mixes, and so can you. I bet I can add deep-bass boosts and get something else out of it, but even just as it is, I can immediately hear how it would fill in a spot where bass guitars are supposed to go. It's just that rather than going crazy on the channel EQ, or running a bass amp and going crazy on that, it will just do that sound right away and it'll sit in an otherwise full-range mix reinforcing exactly what I want the bass guitar to reinforce.

I've looked at the output in a wave editor and it's terrifying to think that this monstrous thing is probably my new go-to DI bass plugin, but here we are. Oh, and I bet you anything this makes basses project better on a phone. Have fun :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Wolfbot processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Wolfbot)

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
