# PointyGuitar

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

a supremely adaptable instrument amp

## Detailed Overview

Sometimes the best way to get the performance of a very analog thing in a very digital format is to accentuate, not the spirit of the analog, but the capacities of the digital. What you get then is not fake gutless imitations of the artifacts of the analog thing, but the heart of why we go for that analog thing. Meet PointyGuitar, which is all amps. Just adjust… if, that is, you know what the analog sound is made of.

Here's how it works. SmoothEQ was a sort of breakthrough: the ability to get very steep EQ crossovers while still zeroing out at perfect, unaltered fidelity. It sounds the way it does because it reconstitutes the original source between every stage, rather than doing independent EQ bands and trusting that they'll be 'just as good' because the gains and EQ slopes match up closely enough.

Then there's AngleEQ, a sort of disaster: a very heavily colored EQ where the crossovers are so phasey that it's like running stuff through a speaker. The opposite: whether as a highpass or a lowpass, it produces a weird physicality and scrambles the sound pretty good.

PointyGuitar is both, in series, with a basic distortion (as found in FireAmp) between every EQ stage. There can be lots of these EQ stages, so there can be lots of stages of this simple softclip, but it's always on the full sound, not a 'multiband'.

What happens? Any given section might add small amounts of overdrive. It's not an electrical circuit and it's run at double precision so there is no thermal noise/Johnson noise: it's just a bit of overdrive if you're boosting a band. Otherwise, if it's flat it's extremely flat (interestingly, inside the flat EQ it's still using the AngleEQ math, but in such a way that it sums to perfectly flat. Using biquads would've got steeper crossovers, but requiring more stages turned out perfect here)

As it's passed on to the next stage, any distortion harmonic that doesn't fit into the following band just plain gets filtered out. This is most notable in the amount you can crank the 'High' band. It's around 3K for guitar chug, but it's resisting aliasing super hard considering the amount of gain you can add. Same applies for every band except Presnce. You get that, High, Mid, Low and Sub. For high gain '5150' type sounds, you boost High and cut Low.

Once you have your sound, be it super high gain or clean Fendery stuff (again, boosting High often helps things sound more amp-like) it's over to the highpass and lowpass. HSpeakr cuts off the bright, and LSpeakr limits the size of your virtual cabinet. They're pure AngleEQ and combine to produce a bandlimited sound without use of a cabinet impulse, harnessing the intensity of the EQ/saturation stages so that the tone sits right. Very delicate adjustments are what you want here, but both those controls have pretty much full range adjustability. 50 foot speaker, or clock radio, are available if you should need them.

In this way, first building a sound out of identifying which frequency bands need most saturation and which to back off, and then channeling that very saturated but very clean sound through extremely colorful bandpassing, you produce an amplike sound (guitar or bass, any amp of any kind, it just depends how you adjust it) which fits immediately into whatever space in the mix you need, with the right tone colorings…

…at ZERO LATENCY.

It runs without oversampling, and all the EQs operate directly without pre-ring, as analog circuits do. So you can track directly with PointyGuitar, set any way you like, dial in the basic sound of any sort of amp no matter how clean or dirty, and have it respond so immediately that you'll notice if anything else in your recording chain is adding latency. It'll feed back like any real amp, it'll feel connected to your fingers, and you can dial it to do anything you want, pretty much. If there's a cabinet honk or something that you actually want to add (rather than just remove) you can run the whole thing into ConsoleX and dial that on the parametric, perhaps in conjunction with the Speakr controls.

I may have just replaced my little tube amp and iso cab and new speaker DI box at a stroke. Didn't expect that, but both my ears and Airwindows Meter tell me PointyGuitar is in the zone, even for really difficult sought-after guitar tones. The range is pretty shocking: it ought to do bass amps, Plexis on Variacs, ratty little Peaveys, you name it.

Oh, and you get a gate (basically DigitalBlack) that triggers off the input before the distortion, but gates between the 'amp' and Speakr so that even if you've got it firing really staccato and quick, it'll merge with your string-damping and act like part of your playing, for guitar OR bass.

Enjoy. This should work both for vintage tone guys AND Reznorian madmen. :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PointyGuitar processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PointyGuitar)

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
