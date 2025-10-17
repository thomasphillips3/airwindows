# Hull



## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

an alternate form of highpass/lowpass filter

## Detailed Overview

This is the second time I’ve done a filter based on stuff the stock market folks have got up to, and both of ’em start with H. First there was Holt, and now this is Hull. It’s set up to work as either a lowpass or highpass filter: the Bright control is really a dry/wet. Bright hard left gives you darkening and the normal output of the filter, Bright hard right subtracts the output giving you a highpass.

This is another audio chainsaw/proof of concept. I feel it’ll be useful as part of other plugins, in a controlled setting, but you can play with it however you like. Be careful, as setting the Freq control very high (increasing the averaging the plugin runs on, and lowering the cutoff frequency) can produce LOTS of CPU munching. I’ve left it that way in case people find a need for it and can handle the CPU demands, but especially at high sample rates it’s a beast at super-high averaging windows.

Hull is a form of playing averaging filters against each other to produce an ‘accurate’ picture of underlying movement beneath noise. This is of course not true: it only appears to be giving optimal information, but it’s effectively synthesizing fake info to make the chart look more specific in its trajectories. It does a really good job of looking like it’s magically clearing away the randomness, but I don’t believe it really is, and you can hear it in the audio performance: it’s dirty, produces obvious artifacts and accentuates weird stuff.

But for a sound effects filter, this is great! So, you can use Hull for various purposes, knowing it has ‘its own sound’ and will really bring a tone to your filtering. It sounds like a grungy old school analog filter that’s maybe distorting and being overloaded by the power of the audio going through it. The lowpass and highpass forms have very distinct tones: lowpassing sounds resonant and sonorous, and reminds me of the oldest Emu samplers (I’m working on getting a Eurorack filter that uses the same chip, to further explore this since I don’t yet have an SP1200). Highpassing does the opposite: it sounds like high frequency boosts done using Hull have a particular airiness and lightness to them.

Taking it way down to the bass and demolishing your CPU in the process, a couple interesting things happen. Lowpassing gives you kicks with a LOT of punch, which let through a bunch of midrange in a way that accentuates impact. (There may be a way to implement this with much lower CPU if it’s a fixed frequency filter: the buffer size isn’t a problem, but allowing the adjustment means implementing it naively and doing things the hard way). Highpassing way down in the bass gives an equally distinctive sound which would translate over smaller speakers very effectively.

This was a good day at work! I feel like modified versions of this principle will lead to some very cool-sounding EQs, even to stuff on the ’emulation’ side of things: this is because I like the sonority and intensity of these filters. They CAN also be CPU-efficient, though this implementation is not (except at high frequencies, where it is fine).

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

Hull shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Hull)

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
