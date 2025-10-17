# Ultrasonic

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Latest Release |

## Description

a very clean, plain, high quality supersonic filter, for using inside digital mixes

## Detailed Overview

Now here’s a handy little utility plugin… sort of the ultimate Airwindows plugin, not only does it not have an interface, it doesn’t have a sound! :D

Here’s why you should care… especially if you work at high sample rates.

Aliasing in digital mixes is annoying. You typically don’t hear it directly, but it coarsens and flattens the mix, throwing all sorts of funny harmonics in there at random frequencies, like subtly ring modulating everything (the aliased harmonics go off on frequencies not related to the original notes, and clash). It’s often very subtle, but it turns up everywhere you have nonlinearities. If you distort stuff in digital mixes, you run straight into aliasing problems. Same if you compress, or do anything nonlinear… and even if you make a mix as pristine and minimal as possible, if you’re mixing in the Airwindows Console system that uses nonlinearities too.

You can run at higher sample rates and that gives you more room, you can use soft saturations (like what’s in Console) and that makes the harmonics appear in order so only the highest frequencies will fold back and alias, but it’s in a computer: you’ll always run into the limits of juggling numbers and calling it music, and you’ll experience aliasing through nearly anything you do.

But what if you just took those problem frequencies away?

Ultrasonic is very simple. It has no controls. It’s a really steep lowpass filter at 20K (five poles, and it works out to 10th order Butterworth filtering). Unlike some ‘audible’ Airwindows filters that are supposed to sound interesting, Ultrasonic doesn’t use internal Console processing: that would be a nonlinearity, and defeat the purpose. Instead, it’s a super high resolution very boring and plain supersonic filter, calculating stuff at long double resolution, dithering its result to whatever floating point buss your DAW uses, and otherwise having no sound of its own.

Drop it into your (preferably 96k or 192k) digital mix and it will clean up anything nonlinear that goes after it. This includes Console! Just because Console ‘decodes’ doesn’t mean it can’t be hurt by aliasing of its nonlinearities: it just distorts so gently that it’s not automatically worse, but any aliasing that turns up in ConsoleChannel doesn’t get taken away by ConsoleBuss. Digital only gets worse, not better, and the trick is to make it get worse as slowly as possible while you work with it.

When you use Ultrasonic, for instance on every channel in a Console mix, you trade a degree of rawness and immediacy for an ease and smoothness that is immediately apparent if your stuff is running into nonlinearities anywhere. In many ways it makes the digital mix sound more analog. The tradeoff is, it’s still five poles of biquad filtering, and it will make stuff sound a bit slick, a bit more ‘processed’. You can kinda hear that you’re doing the extra processing, but the texture change is really appealing: stuff sits back (less super-treble will always sound more like the audio ‘sits back’ and is more polite) and bright shiny stuff sounds purer and sweeter. This is all the more true if you’re processing heavily.

It’s very easy to use: just put the plugin before anything that might alias. By itself it should have no sound (though if you have true 96k or 192k audio, it of course is obliterating your real supersonic content). There are no controls and nothing to do, it isn’t itself nonlinear so it shouldn’t interact with anything, you don’t have to gain stage it or pay any attention to it at all. Very plain, simple, hopefully pretty low-CPU for all that it’s five poles of filtering at stinkin-high calculation accuracy.

Put it on everything that you want to smooth out and un-digitalize. Sometimes there’s nothing quite like beating the problem into the ground with a sledgehammer. For frequencies over 20K and the aliasing that loves them, this is that sledgehammer. (It is also biquad filtering, so it runs with zero latency and you can track through it)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Ultrasonic processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Ultrasonic)

**Categories**: Brightness

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Brightness](../categories/brightness.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
