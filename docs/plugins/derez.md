# DeRez



## Quick Info

| | |
|---|---|
| **Category** | Lo-Fi |
| **Type** | Lo-Fi |
| **Status** | Stable |

## Description

an analog-style bit and sample rate crusher with continuous adjustments

## Detailed Overview

What would an analog bitcrusher even be? It doesn’t even make sense. You’ve got sixteen bits, eight bits, twelve bits: you can’t have, like, eight and a half bits.

Sure you can! DeRez is here! Its dark magic can be yours! If you don’t believe in dark magic, the source code can be and is yours under the MIT license. Folks who are constructing strange models of things like obscure old digital gear should find this useful: do whatever compansion thing you had in mind using for instance PurestConsole, then use DeRez to dial in the right amount of bitcrunch.

Here’s how you use it: slide the Frequency control down, to continuously sweep the sample-rate crushing. Slide the Resolution control down, to continuously sweep the bit crushing. There are no transition points: the algorithm will always let you do just a tiny bit more, or less, of either, because it’s really a floating-point algorithm at very high resolution. It’s doing a fairly simple samplerate crush and softening the transitions just a tad for an analog feel, and it’s doing the bit crush by chopping away bit-sized amounts and then truncating once it can no longer take away a whole ‘bit’. Due to this decision, a ‘bit’ can be any size at all, so you can sweep it without having transition points. Obviously, you can also automate the controls in your DAW to program continuous sweeps.

It should just work, and you’ll never have to lament, “But why can’t I set the bitcrusher to three and five-eighth bits?” Because now YOU CAN.

I know there are a few audiophile ears out there who’ll pop a blood vessel over this nasty little toy, but I’m not a ‘bit’ sorry. Those of you who love this will know who you are right away. Those of you who think this is a really irritating and pointless idea, this one is not for you, and there will be things coming up that are more to your taste.

This work is supported by Patreon, for those of you who like me making stuff even when I know it will get some flak and hate-comments: the whole point of being on Patreon for me is that I get freedom to do stuff that’s not popular. Mind you, it’s 2018, so this may well be one of the popular ones. Depends on whether bitcrushing and frequency crushing are ‘in’ or ‘out’. Another nice thing about keeping me around doing this stuff is that it stops mattering whether stuff is ‘in’ or ‘out’: I build the plugins on a Windows 7 VM and an OSX 10.6.8 system kept in a time capsule especially so that my stuff works EVERYWHERE, and by that I mean Mac, Windows, Linux and on machines so old they run PPC chips. Yep! The Mac builds are slightly larger because they’re triple binaries and run 32 bit, 64 bit, and PPC. They should probably also work on OSes older than 10.6.8 but I don’t even have any of those, it’s just build settings. So these plugins are as close as I can get to ‘Grandpa’s Tools’ levels of reliability, and you should never be forced to update, alter, or break your system just to keep up with compatibility with Airwindows plugins. This is in spite of Apple (for one) continuously breaking XCode w.r.t building for older OSes. Hence the old build system. Maybe one day I’ll be running that in a virtual machine that runs it ten times faster than the original laptop. Maybe I’ll run the Windows 7 virtual machine inside the 10.6.8 virtual machine inside the new computer. I will note that I have to keep the old Windows cut off from the internet, and have already had to do workarounds to stop Visual Studio breaking itself in a fit of pique that it can’t install Win10 over the Windows 7 and blow itself up, so it’s not only Apple that gets up to this stuff.

Support my Patreon, so I can keep on expanding the pool of plugins that don’t break your system demanding updates and wrecking the joint. I know acting that way gets you more money… because I barely have any money, and the folks working that strategy have lots of money. And it’s not a good enough excuse as far as I’m concerned, so as always I will just not do the behavior that I don’t like to see in others. Vote with your dollars, that’s a somewhat practical way to be heard. It won’t fix the world, but it definitely is able to keep me going :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DeRez processes audio in the Lo-Fi category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Lo-Fi](../categories/lo-fi.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DeRez)

**Categories**: Lo-Fi

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Lo-Fi](../categories/lo-fi.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
