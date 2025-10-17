# PurestConsole3Channel

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Latest Release |

## Description

an alternate algorithm for minimalist Console

## Detailed Overview

Instead of immediately doing EveryConsole, how about the final Console version it'll contain?

This serves two purposes. First, it's an extension of the work I was doing in ConsoleZero: this is a custom sin()/asin() implementation along Airwindows lines, making it a little unusual. It uses a simple sin() approximation, but instead of being mathematically correct it applies all the multiplications and divides only in factors of two: bit shifts, in other words.

This is what ConsoleZero did, but more simply. This extends that to improve the sin()/asin() calculation, but then it's not doing that correctly, it's another approximation to make every calculation preserve the mantissas of the numbers as much as possible, every step of the way. Doesn't matter if it seems like a ridiculous thing to do, that's the experiment, and you already have this in mathematically perfect sin()/asin() form anyway: the original PurestConsole is just that.

The thing is, there are other gains. These new algorithms do so much with bit shifts that they're blazingly fast. Both this and ConsoleZero run fifteen tracks of mix on my M1 Macbook Pro at about 5% CPU, with a couple bonus plugins in there.

And that means if you're running something like current Reaper, as I am… with chain and individual FX oversampling… you can do that. And so I've made a video where I'm demonstrating a 96k project mixed in PurestConsole3, with ALL the Console plugins oversampled to 768k. (unless, because it's starting at 96k, the 16x oversampling is actually giving me 1.536 megahertz oversampling?)

And it went from 5% CPU, with presumably 16x oversampling on all Console tracks and the buss, at base 96k sampling rate, to 30% CPU. I could've doubled the project and it would still have run. (probably the original PurestConsole would not be able to do this)

And it sounds… different! You'll hear it. You surely can do it. It's got its own sound. Not an Airwindows sound, I think. Sort of smoothed off and glossy. In the video I demonstrate this output, versus non-oversampled PurestConsole3, versus ConsoleZero. And, having heard all the original sounds off my instruments and modular, I think ConsoleZero is rawer and more accurate (that's sort of the idea). But now, if you have a great love for oversampled nonlinear plugins, PurestConsole3 is my little gift, an Airwindows Console version that's designed to work with, not against, what you like.

Have fun, and I'll keep new stuff coming as well as I can!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Encode]
    B --> C[Summing]
    C --> D[Decode]
    D --> E[Output]
    style B fill:#6366f1
    style D fill:#f59e0b
```

## How It Works

PurestConsole3Channel is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PurestConsole3Channel)

**Categories**: Consoles

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Consoles](../categories/consoles.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
