# ConsoleMCChannel

![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Consoles |
| **Type** | Consoles |
| **Status** | Stable |

## Description

the initial, bright take on the MCI console

## Detailed Overview

ConsoleMC is replacing my fully analog mixing system, which I'm now looking to sell off. Technically, just the mixer, as I can re-use the Lavry for tracking, where I used to have it dedicated to re-capturing the mixdown from the Heritage Audio mixer. This is what it took, to retire that glorious beast.

It's a channel strip that functions like a normal Console Channel, except it's got treble, a sweepable mid that only boosts (like the classic MCI mid boost), bass, a fader that runs before the EQ section like the classic MCI, and a special pan switching network that's like an evil cousin of LCR panning. And it's a summing buss that brings the summing character of the big MCI desks with a gnarly analog dirtiness that's not simply 'add a distortion box' but is actually a modification of other recent and unique work I've put out.

ConsoleMC draws on the following recent plugins: Creature. SubTight. Sinew. ResEQ2. Pear. BitShiftPan. There is not a single normal DSP algorithm in this thing unless you count sin() and asin() functions. It is ALL built out of current, 2023 Airwindows plugins that have all been pretty well received, sometimes with a fair bit of excitement. I told you all this was working up to something. This is it.

Specifically, this is the first 'it' to come together: I've got at least five other big console concepts that deserve this treatment, but ConsoleMC is right here for you to jump into, right now. There's a couple reverbs in the demo, including kCathedral which is a call-out to the corresponding Bricasti patch. Those are for later.

ConsoleMC is designed around running at 96k (or possibly 192k if you're so inclined) but ought to work at 44.1k. If you're at low sample rate and seek to oversample it 2x or 4x it shouldn't do it any harm.

ConsoleMC is NOT flat when set neutrally: use ConsoleMD for that. ConsoleMC, in its debugged form, uses the technique from SubTight to rein in subsonic bass, and this ends up applying a touch of very high-frequency 'air' that was unexpected. The original release also didn't scale this effect to sample rate (it's a very new algorithm that didn't seem to work that way at first) but the Redux version, which becomes the go-to version of ConsoleMC, does scale to high sample rates without losing additional bass. Again, for a DAWlike flat response use ConsoleMD, which has those 'inter-stage' highpasses stripped out. If you're okay with mixing into a slight presence lift and would like extra personality go with ConsoleMC.

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

ConsoleMCChannel is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.

## Usage Tips

- Use matching Channel and Buss plugins (don't mix versions)
- Start with settings at 0.5 (neutral)
- Place Channel on all important tracks
- Place Buss on master fader only


## Related Plugins

Browse other [Consoles](../categories/consoles.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ConsoleMCChannel)

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
