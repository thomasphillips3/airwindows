# Tape



## Quick Info

| | |
|---|---|
| **Category** | Tape |
| **Type** | Tape |
| **Status** | Stable |

## Description

simplified, all-purpose tape mojo: my personal jam

## Detailed Overview

This one’s for me. It’s very similar to last week’s ToTape, but with the following differences:

-simpler name
-overdrive uses Spiral, not the Mojo algorithm
-simpler controls (not exactly ‘input gain’ but close)
-changes to the Head Bump algorithm
-no flutter

This is what I WANTED to do with ToTape6, and didn’t. In some ways, that’s good: if I’d axed flutter I would not have spent all day struggling with it and coming up with a better algorithm that more closely resembles real physical tape, something that could come in handy for future echo plugins etc. If I’d done the things I’ve done with Tape, to ToTape6, then ToTape6 wouldn’t be as adjustable as it is. There’s room for both, and I gave people the complicated many-knobs version because I know you too well ;) and I know what people like, and I’m there for you.

But I also have dreams of my own. So, the plugin (first ever from Airwindows) that carries just the generic name ‘Tape’ is Airwindows tape emulation MY way.

I’ve heard a lot of tape in my time, being over 50 years old. I’ve dubbed and re-dubbed tapes a lot. So I dialed in (and re-programmed) Tape by loading up eight instances of it, in a row, and making it behave itself as well as could be expected while running audio through eight instances of Tape. It’s not meant to be clean if you do that: it’s meant to be eightfold trash, but the right kind of trash I’m familiar with when you’ve got that much generation loss and head bump buildup. I knew that if I could get that right, if I could get it to behave okay under that kind of duress, I could rely on it as a go-to output stage (going just before Monitoring) that would condition the sound in the right kind of way.

And so it does.

Tape will be heard from again, but much as ToTape5 bore the standard for Airwindows tape emulation for years, Tape is my personal choice for ‘mix into’ DAW output stage and it’ll stand for a while, I think. If you need more phat or more flutter or more controls etc etc, use ToTape6, which is just as good in many ways. This is just my ‘director’s cut’ version, designed to my tastes, for if you trust my ears and my choices. Since it’s Airwindows, ToTape6 (and 5) still works and you can have both. This one is for those of you who pursue the simple creed: I have a (virtual) tape machine. I record to my tape machine. I am happy. :)

This plugin came out with an original version and then had a Redux update in which I added a control: a slider for the head bump, as people were finding the head bump excessive. Cranking it up all the way gave you the original behavior, but I defaulted it to 0.5.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Bias]
    B --> C[Saturation]
    C --> D[Head Bump]
    D --> E[Flutter]
    E --> F[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Tape emulates magnetic tape characteristics including specific tape behaviors. Use it to add warmth and analog character.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tape](../categories/tape.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Tape)

**Categories**: Tape

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Tape](../categories/tape.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
