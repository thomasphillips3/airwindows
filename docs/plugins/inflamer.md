# Inflamer

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Subtlety |
| **Type** | Subtlety |
| **Status** | Latest Release |

## Description

an Airwindowsized take on the waveshapers in Oxford Inflator

## Detailed Overview

How do you take a famous, beloved plugin and make it better?

In a recent livestream, I saw a video make the very convincing argument that the famous Oxford Inflator is the combination of two very simple waveshapers. Like, spectacularly simple. One's a bit more complicated than the other, and one is essentially just second harmonic, nothing more. The person making the video set up the two simple waveshapers and demonstrated that for all manner of settings on the real Inflator, they could make a Melda waveshaper produce identical outputs.

Of course, you didn't get the UI. You didn't get the band splitter. There's a clip meter of some sort: also not included. However this meter, these controls work: nope. But… now there are algorithms that are public, some of 'em so simple as to defy property (hard to argue that you can own one line of code that makes things second harmonic, it'd be like me claiming to own sin() )

What could you do, to make this better in any way?

Well, that's where my recent experiments come in. Meet Airwindows Inflamer (NOT Inflator). It doesn't do the same things, quite. There's no band splitter. There's a curve control, but it doesn't go -50 to +50, it goes from 0 to 1. And while it blends the two waveshapers… it does so in a more cumbersome and possibly more pure way.

Inflamer is different because it's using my BitShiftGain style gain trimming, internally, as if it was a dry/wet, but with the two waveshapers instead of a dry and a wet. The Drive control is also bit shifts (very accurate divisions by powers of 2). The Effect control, as with the real Inflator, is normal and is in fact a dry/wet, and there you can have subtle adjustments to what is, I hope, a sonically optimized version of the effect.

But you cannot have the band splitting, or fine gradations of Curve. In fact many settings of Curve will end up being a slight volume drop when used at unity gain (Drive in the middle). It is possible a bunch of people will shoot this out against the real, iLoked, for pay, bestseller plugin, and will decide mine is crap because it is often quieter than the real one.

GOOD. I'm not trying to rain on anyone's parade. You have to know what you're doing to evaluate this. It's much like how, when I start doing takes on Bricasti, they'll be in my own style. I am not cloning things, even when the underlying algorithms are trivially simple. Inflamer is different and the range of adjustments are in 6 dB steps on Curve and Drive and often you might find the result comes into the mix 3 or more dB quieter than it would from the Sony plugin, and that's as it should be.

And if I'm correct that leaning on these insights into digital math gives their own kind of benefits, I've managed to make an Inflamer which is more mastering-grade, more transparent and sonorous, and better sounding (IF you can live with the only settings I allow you to pick) than the real one. That's why I'm restricting it the way I am.

There you have it. Inflamer is obviously not Oxford Inflator, has less options and restricted choices, and if you shoot them out head to head without matching levels carefully, it will probably always come out quieter than Oxford Inflator. And it is only some waveshapers, simplified and restricted even more than the original.

And for some, it'll be just better, in critical listening. Sometimes it takes radical methods to beat an already stellar plugin. I hope you like Inflamer, and that it doesn't inflame you too much, unless you like that sort of thing.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Inflamer processes audio in the Subtlety category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Subtlety](../categories/subtlety.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Inflamer)

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
