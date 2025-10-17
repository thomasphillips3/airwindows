# EQ

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Latest Release |

## Description

just the EQ parts of CStrip

## Detailed Overview

CStrip actually came out of this: a set of EQs specially coded to work together. It’s a lossless three-band (as in, the bands are made by different IIR filtrations being subtracted from each other, so if it’s flat it’s totally bit-identical output and also it has no pre-echo) with a special highpass and lowpass. Each of these things gets switched out of the circuit if not in use (much like CStrip). That makes EQ a very nice default EQ for broad-stroke filtering.

The slopes aren’t super high, but that just helps it sound more natural (for a more striking-sounding filter, try Capacitor which is a more aggressively sloped highpass and lowpass). I could have given it set frequencies, but it seems like that’s kind of handy. This plugin is given to you (in AU, and Mac/Win/Linux VST) by request, as I’ve had a user ask for it even though CStrip is already out. So, for a simpler and more approachable Airwindows EQ, here’s EQ :)

This work is supported by my Patreon, and I’m happy to say I’m back in the top 50 of the ‘Music’ section at ‘Graphtreon‘: I always like that, feels like I’m getting somewhere with all this. I also like something else, too: I’m definitely giving you folks ‘Aura’ this month. It’s thanks in large part to a mysterious creature known as Slipperman who got involved, and in his honor, next month you’re getting ‘Golem’. Remember, the bigger a success the Patreon is, the more I’m able to persuade people that my way of doing things is good. So if you want this sort of thing to catch on, throw money as that’s all people pay attention to these days…

Other stuff I’m working on is Atmosphere, DeRez, and the latest Righteous, Righteous4. Also, if anybody wants to meet me, and also enjoy a rather special academic experience, I’m attending a scholarly lecture by a certain Doctor Bill Bruford in Albany NY this Tuesday, which I’m very excited for. I have no idea how well this’ll go over but I have a smaller version of the famous bent cymbal he discovered (the real one tragically broke after much use), and I mean to give it to him as a gift in honor of his creativity in the field of timbre. Anyway, wild horses wouldn’t keep me away from there, so if my car behaves itself you can meet both me and a REAL great person ;)

(as a follow-up, by 2022 I'm hanging down just above 100 in the global Patreon music rankings, and I did in fact get to Albany and the lecture by Bill Bruford. I got in late, and confused him with my cymbal gift after the lecture (Bruford: 'but it's not the one!' which, true, it was not, and I got quite flustered. I hope he understood in some way that I just wanted to give him something, somehow. And no Airwindows people were there, which simplified things I guess)

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

EQ shapes frequencies through EQ. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/EQ)

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
