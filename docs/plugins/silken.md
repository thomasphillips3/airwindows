# Silken

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

a high frequency boost that gives ambience and texture

## Detailed Overview

Here's one where the plugin is probably better than my ability to demo it. Silken is a kind of high frequency boost, based on PrimeFIR used in 'prime mode' but backwards, so rather than being a lowpass with lots of ambient leakage, it's a method of subtracting such a brickwall mostly linear phase lowpass with different leakage.

So that's a lot. You can simply listen to it and see whether it is able to do 'silky high frequency boosts such as you might use for lead vocals' or you can bear with me as I try to explain HOW it does that thing. Because, even though stuff's kinda hectic around here and my video wasn't good, the plugin I made really brings a useful texture. If I could sing better I'd be all over this demonstrating how great it is, and even so it might help out. I feel it might click with people so it behooves me to explain how it's real.

So, you can run a brickwall filter, using a 'window' (one of the controls) to determine just how steep the filter's gonna be. It's an algorithm called a sinc filter, and the wider the window, the steeper your brickwall can be. It's a phase-linear filter, so it has pre-echo and it has latency. Silken does not compensate for this latency, which depends on how wide the window is: it's a slightly unusual arrangement because it's not completely symmetrical in an effort to cut down on the latency.

So far so good. It's like a shelf for boosting highs and cutting lows. But then, bring in what PrimeFIR does. That lets you make the filter only from prime numbered samples, and not every sample. What happens when you make a sparse filter like that? I've made multiple plugins that use this TYPE of effect: BrightAmbience, and in fact my classic plugin Iron Oxide. There's plenty of experience in using this type of effect… at least with me :)

PrimeFIR can make a 'lowpass' out of only prime-numbered samples (part of the filter, not just counting every sample in your audio) and it lets through a sort of 'haze' around the filtered sound, as audio across the whole window bleeds through. What Silken does is different in two ways. First, it's subtracting the filtered part, to make it a highpass. Second, it's constructing the filter out of only NON-prime samples, this time. So what's happening is, it's more effective at being a highpass than PrimeFIR is at being a lowpass, but the stuff that leaks through is still out of the prime numbers because those are now the ones NOT being subtracted.

You get a highpass where, the harder you push it, the more of an 'aura of silky ambience' you get around the highs. It will sort of diffuse super high frequency transient information, like a diffusion filter does for visual information. The result is flattering in exactly the same way a camera's diffusion filter is. It should work fine on even the most high quality sources, but it should be an absolute lifesaver on the kind of nasty mic (like certain lavaliers!) that puts out distressing hyperfocussed bright transients. Now, you can diffuse that and change the texture of it, not just turn the brightness you've got up and down.

Hope you like it :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Filter Stage]
    B --> C[Resonance]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Silken shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Silken)

**Categories**: Filter

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Filter](../categories/filter.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
