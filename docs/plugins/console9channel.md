# Console9Channel

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Latest Release |

## Description

just the summing from ConsoleX

## Detailed Overview

Here we have the first part of ConsoleX that can come out and be put into use, just as it will be used in ConsoleX.

You see, the upcoming Console system is the big one with all the EQs and multiple dynamics paths and StoneFire built in, and it's got so much going on it requires the development of an elaborate GUI (for which a lot of work has already been done). But the guts of the system remains Airwindows Console and that gets its own development. Console is the system by which all the sound sources get pre-distorted and then un-distorted on the buss after summing, for a sound that (in theory) doesn't touch the tones of any individual mix element, but alters the spaces between the sounds.

So when using Console (or any version like Console9 that's strict about this) you should expect to hear exactly the same sounds you originally had, but they'll sit differently. They'll make up a more convincing space, in a subtle way that shouldn't mess with your sounds, that will just make it easier to make those sounds gel into a mix that feels good.

The algorithms for Console9 (as used in ConsoleX) are new, but they came about through work I did revising Console6. It turns out there's a resource called 'Herbie' that helps you re-hack algorithms to work better in floating point. That's immediately of interest to me, as I'm fascinated by the ways our simple digital math erodes and harms the tone of our sounds… I've already done a lot of work on word length and dithering, and I already advocate double precision processing over the use of simple floats. But it turns out algorithms that don't play right by Herbie can have special (bad) qualities, and the original Console6 plugins were guilty of this.

What would happen is there'd be a big spike of inaccuracy as the calculations swept by zero. And that's as may be, but we're dealing with audio: especially with low frequencies, the sound is constantly sweeping through zero! It's digital math reinventing how to make crossover distortion as found in class AB amplifiers. Herbie exists to re-design such algorithms so they sweep through zero (or wherever else there's an issue) perfectly. It'll also estimate how much extra CPU it'll take: sometimes it'll do a silly approximation and say 'oh hey, if you just replace all the outputs with 0 you still have X much accuracy but the code runs much quicker!'

There were optimizations for Console6, and the version in Consolidated (and in the downloadable plugin collections) is the new version. The download from when Console6 first came out, remains the same for historical purposes and so you can get a hold of exactly how it was when it came out (this is true for pretty much all Airwindows plugins: use the collections or Consolidated to have the recentest versions).

But it turned out there was also a set of distort/undistort curves available from using the same type of math as in Console6, the Herbie-optimized sort, except scaling things by the golden ratio (of course it had to be the golden ratio, that thing pops up all over the place) and this produced a new sound for Console. It's got more headroom than any previous Console system, while also having some of the raw intensity of Console6 (which, even fixed, might be a little too raucous and garagey for most purposes). It's got a real good sense of transparency but it strongly brings that Console vibe to the spaces between the notes. And it's the summing buss that is going into ConsoleX.

The reason I say it's also the part that will be used IN ConsoleX, is because I'm adopting some Chris Lord-Alge-isms in ConsoleX. My take on how sends and verbs and things should be handled in ConsoleX is to use them kind of like Console8 uses submixes: you'll be sending stuff from channels to other channels that have the verbs on them.

The difference is, when you do that you put Console9Buss at the top of the sent-to channel… put in your verb or whatever, all wet… and then run the result through ANOTHER instance of ConsoleXChannel, and sum that. So, the idea is 'decode and then recode, except you get literally all the processing from any ConsoleXChannel, all over again, on the verb or delay returns'. And then you adjust those the same way you'd adjust any other channel: they just come in on even more channels, and all the same features apply. And so, Console9Buss is your 'decode' for making further verb stuff happen, because you don't need to run the full ConsoleXBuss to do that.

There's still loads of work to get ConsoleX done, plus I'm having another crack at ToTape to address the eager aliasing that came out of Dubly2. Unlike that weird beast, Console9 is very clean and simple so you can oversample it to the moon if you wanted to: I will not be doing that, I'll be running it at 96k and it will be fine. There is a reason people got an 'analog immediacy' hit off ToTape7: aliasing suppression is a tradeoff between artifact minimization and overprocessing tone-flattening, and in ToTape you're hearing one extreme. I'm still going to see whether I can have best of both worlds but I'm not taking away the ToTape7 people enjoyed. And when ConsoleX comes out, there'll be a dedicated 'only the tone controls' plugin (for use pre-EQing stuff to a channel instance of ToTape, which is a black art of its own) and so you'd be able to run the EQs and then oversample the summing buss to the moon if that pleases you, using Console9 to stand in for the built-in versions that are part of ConsoleX.

For now, I will continue to get over my recent bout of COVID (I'm testing negative, have just lost a lot of energy so be patient), will continue working through the backlog of plugins that can come out, and I'll talk to ya later :)

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

Console9Channel is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Console9Channel)

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
