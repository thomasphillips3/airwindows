# Dark

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Latest Release |

## Description

a wordlength reducer that gives your music a blacker backdrop

## Detailed Overview

Some weeks are MY kind of fun…

This won’t make big changes in your audio. In fact if you think you can reliably hear this on its HD setting, I think you’re mistaken. And yet, this might be the funnest thing I’ve done all year.

Why? Because I’m back to the dithers again. I figured out a way (or two) to go EVEN FARTHER in the direction I’d chosen. And it worked: it worked super well, and you can have it. Introducing Airwindows Dark.

How does it work? It’s very simple, really. Much like Not Just Another Dither (NJAD, my previous best) it analyzes the results of the audio, depending on whether the dither rounds up or down. With correct TPDF dither, it’s a factor of randomness, a noise that breaks up patterns in the output. With NJAD, it runs a Benford Realness calculation and uses that (for a more natural-sounding audio output). But Dark?

It simply works out the average trajectory of where the audio’s going. It’s following the lower frequencies, suppressing the highs. And then it makes its choice based solely on whatever is going to further this trajectory… and keep the output as smooth as possible. It is ‘dithering’ with intent, doing whatever it has to in order to get a darker, softer output. All done by truncation alone.

The result is delightful, if you are into analog sonics and the absence of bright digital artifacts and hisses. It is NOT obvious, unless 16 bit artifacts are already obvious to you, and at HD (24 bit) it is purely a matter of thoroughness and making correct choices and you shouldn’t be hearing a difference. You damn sure won’t be able to blind test a difference (that requires much more obvious stuff happening).

But, but, but! If your experience with audio (and probably loud listening levels, and REALLY good monitoring, and amazing source files) involves sinking into a lush bed of analog-rich sonics, where you quickly notice subtle shifts in sonic attitude and then take much longer to get used to them and form your judgements… there’s nothing at all like this.

It can only wordlength reduce, so especially at 24 bit it shouldn’t be able to ever hurt bright sounds that are supposed to be there. It’s only dithering (in a novel way). But it’s doing its thing in a way that’s completely outside of anything you can do with filtering or normal processing. If you need depth and space, if you need rich black silence behind your mix, this beats NJAD… soundly.

I hope you like it. The demonstration at 8 bit wordlength in the video ought to show you what to expect. Dark is yours to use (in fact, you can have the source code under the MIT license!). For now, if you are using Monitoring you’ll need to switch it off to use Dark, as Monitoring defaults to a 24 bit wordlength reduction using NJAD and I’m not prepared to simply update it and have it default to Dark for all things.

Though I’m tempted. ;) (in fact, this is what Monitoring2 became)

And in turn, within two weeks, Dark became Dark Redux: same Dark, exactly as before, BUT now it has one added control. DeRez! Just like in the DeRez plugin, it zooms seamlessly down to 1 (or 0) bits. It’s continuous, not discrete: you can do one and a half bits or whatever, play it by ear. Except that unlike the DeRez plugin, it’s still Dark… so you can hear more clearly what the new wordlength reducer is doing.

It defaults to 0, which is exactly as it was before. Both the 24 and 16 bit settings derez, which means you can take it to 0 bit (silence) with 16 bit, switch to 24 bit, and the result is you’re listening to 8 bit. (if you need really specific behavior, you can use BitShiftGain before and after the plugin to get exact bit values).

This makes it possible to do old school sampling effects, dark bitcrushed sounds. It also demonstrates that the Dark algorithm is a bit special, because you have to really trash the wordlength to deteriorate the tone much. It’s more like a slightly noisier, slightly funkier, slightly gated grunge tone, even though the output is literally just bitcrushing. There isn’t even any smoothing applied to get the ‘dark’ tonality, it’s literally all a wordlength reducer, and with DeRez at 0 it’s exactly the original Dark plugin.

If there’s a problem or if you need to not see a control marked ‘DeRez’, my updates-in-place always leave the original file there, in this case renamed to DarkOriginal. They have the same ID and DAWs ought to be able to handle swapping the new one in, even on existing projects that use Dark, it’s just to make sure people can get back the original release if they ever need to.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Dark processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Dark)

**Categories**: Dithers

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Dithers](../categories/dithers.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
