# SideDull

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Latest Release |

## Description

like Sidepass, but a lowpass on the side channel. Treble-centerer

## Detailed Overview

There are some nice things about Patreon-era Airwindows. Not the money: that sucks, though I think I just about have basic survival taken care of as long as I don’t eat much and nothing happens to my car :)

No, the cool thing is this: I can put out tools that have NOTHING to do with a plugin marketplace. If even one person finds the plugin useful, I can put it out. SideDull is kind of like that. I was asked, ‘since Sidepass is great, can we have a lowpass version?’. And I went ‘huhh? why would anyone want to narrow just top end, or center mids and up while not touching lows?’

The answer is of course ‘why not?’ and ‘if you are sure you won’t be doing that, don’t install this plugin’ :)

I don’t need to explain what SideDull does: it’s the same as Sidepass but in reverse, narrowing/mono-ing highs and down. I WOULD like to explain something about its role in a DAW user’s toolkit, though. I’m seeing this increasing churn in the plugin industry, a frenzy of new stuff and new requirements and DRM systems and dongles and such. It’s like a fulltime job to keep up with your recording system. My own pet fear is updating something only to find that I’ve hosed myself and everything’s now broken.

That’s why SideDull, and every other plugin, is built on a time-capsule 10.6.8 system and the VST’s built on a time-capsule isolated-from-the-internet virtual Windows 7. I’m using the simplest possible interfaces (some vendors, like Blue Cat, have taken pains to implement the generic interface super well, and can even skin it attractively) and not touching stuff that causes forced obsolescence, which I think is really bad news for us all.

So, the free AU/VST plugins (and the Kagi AUs before them) can be like your favorite screwdriver: you get to have the best and simplest audio tools that do NOT break. That also means that if you can only afford legacy computers (or just like being frugal and spending your money on Rickenbackers, as I long to do) you aren’t out in the cold… ever. I’m dedicating the rest of my life to putting tools in the hands of kids and dinosaurs alike, and following it up with my open source initiative. And the longer I do live, the more of it I get to do: but if I keel over tomorrow, all the plugs will still work and I will have had a good day and slept with a clear conscience :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

SideDull processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/SideDull)

**Categories**: Stereo

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Stereo](../categories/stereo.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
