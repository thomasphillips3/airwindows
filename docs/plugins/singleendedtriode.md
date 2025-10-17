# SingleEndedTriode

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Subtlety |
| **Type** | Subtlety |
| **Status** | Latest Release |

## Description

unusual analog modeling effects

## Detailed Overview

Everybody knows that analog modeling means distortion. (well… noise and distortion. And EQ, and overprocessing… but mostly distortion.)

However, it’s always the same sorts of distortion: soft or hard clipping generating harmonics. Here, have three totally different kinds!

Single Ended Triode does three things, and you don’t have to do them all at once (in fact you probably don’t want to).

The actual Single Ended Triode control is a special gain-staged saturation that’s asymmetrical. It’s a little like PurestWarm, only not, because rather than put a soft saturation on one-half of the waveform, it offsets everything and goes into the saturation with a bias voltage. Then it subtracts a related voltage, and scales the whole thing up or down based on how much distortion you’re looking to get. (shown in the source code, of course)

That means you have a ‘second harmonic generating’ asymmetrical distortion, but with NO crossover point. Unlike PurestWarm, SET is a continuous waveshaper just like using a real triode tube single-ended, and while you can crank it up to get obvious effects, its real magic is in using just a tiny amount to warm and sweeten things. It’s perhaps not ideal for the 2-buss because you’d simply be removing some of your mix energy on one half of the wave, but if the sweetening is what you need it might be worth it, because it’s a super clean way to do that. It’s only the asymmetrical distortion, and the interesting thing about that is: know how Spiral smooths the transition between sides of the sin() waveshaping, and that made it sound better? With Single Ended Triode, it’s capable of doing that transition when cranked way up… but used subtly, the entire audio output sits within one sin() calculation, and you don’t see a transition in the first place. This is literally why high end SET stereo rigs perform well for musicality and fluidness of sound: they have obvious faults but they’re great at avoiding crossover issues between push/pull sides of the circuit because they don’t have two sides to the circuit. It’s single-ended, and so is this algorithm unless you’re wildly distorting the heck out of it.

Crossover issues, you say?

Why yes. Meet Class AB (and Class B) Distortion.

This is the opposite. It adds nonlinearities as the signal passes through zero. It’s a STRONG tone coloring and certainly not for the 2-buss or nice mellow music: the Class B is downright nasty and you should be careful about using it if you have delicate tweeters, as it’ll create extremely harsh treble grit (though, interestingly, without Gibb effect converter clipping: that is when reconstruction of the wave makes treble go past what bass can do, when it clips the converter on highs. This is a kind that could blow your tweeters at super high volumes but does not clip the converter doing it)

The Class AB transitions through the middle of the wave in a more curvy way, causing the effect to lean towards the gritty upper-mids. Where might you find this kind of noise? Certainly not in any acoustic instrument. But… listen to certain old nasty tube Hammond organ sounds. Certain big guitar amps. Past a certain wattage, nearly every old tube amp is run push-pull (same with many transistor amps). They run hot, their calibrations drift… and one of the things that can happen to an amp is problems with that transition zone. Use Class B distortion and you’ll get very much the sound of purely transistor amps breaking down and going cold and gritty. Use Class AB (because with tubes, you’re probably going through output transformers and speakers that don’t have hi-fi tweeters) and you’ll get a bit of that gnarly rock-and-roll grit. There are expensive boutique stompboxes that can do this. Now you have it in a free, open-source plugin: open source devs, take note, because this one’s not often talked about or modeled. Most attention to amplifier crossover distortion has come from High End audiophile circles, and those guys have been getting mocked for decades. This stuff will not affect a frequency response plot. In certain systems of measurement you won’t even see it at all, and for years people have done naive measurement and claimed ‘it’s perfect, no further work needed!’ and the audiophiles were tearing their hair out, swearing that certain amps sounded like butt even if they measured ‘perfect’.

Little did they know that in 2018, musicians would be turning to those same horrible distortions for creative purposes, sweetening with Single Ended Triode, adding grit and attitude with Class AB distortion, and being able to put a layer of really brittle edgy brightness onto the occasional sound with Class B.

PS: some of you are having a lot of fun modeling existing hardware using elaborate combinations of Airwindows plugins. Just saying, these three sources of really specific coloration are exactly what you need to do that. Be careful of Class B as a little goes a long way (in fact, I would pick either Class AB or Class B but not both: study the circuit topology and only use AB and B where push/pull circuits actually exist, and remember they’re designed not to cause this kind of problem. AB contains overlap that stops the transition point from being exactly in the middle. Apply wisely.)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

SingleEndedTriode processes audio in the Subtlety category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Subtlety](../categories/subtlety.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/SingleEndedTriode)

**Categories**: Subtlety

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Subtlety](../categories/subtlety.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
