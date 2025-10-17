# Srsly2



## Quick Info

| | |
|---|---|
| **Category** | Stereo |
| **Type** | Stereo |
| **Status** | Stable |

## Description

a revisit of Srsly, to make the stereo widening more extreme

## Detailed Overview

“You call that a wide? Now THIS is a wide!”

A little while ago, I put out a plugin that reverse engineered the famous Hughes SRS stereo widener, from pictures in an old Popular Mechanics article. By applying a set of narrow little EQ boosts and cuts to stereo, mid and side channels, you could make a sort of holographic effect. Srsly still exists, just as it was, for use tweaking out more natural stereo imagery.

But the rabbit hole goes a bit deeper than just that…

Srsly was by request of my friend Chad whose Hughes SRS wasn’t working properly, and who wanted a plugin version that didn’t hum. I didn’t have one of my own, so it was largely guesswork. Thing is, somewhere in there I got my hands on one (thanks Patreon! Between that and getting a real Mackie 1202 to play with, it turns out it’s useful for me to get actual gear relevant to my plugin interests, especially when I’m not getting the plugin right at first)

And before I used it myself, I didn’t really ‘get it’, but then I started putting it on reverb returns, and quickly got very fond of a certain ultra-wide reverb field.

And then I got more heavily into mixing in the box (and not with my hardware stuff) after Console7 came out… and discovered that my ITB reverbs did NOT do that kind of wide, and tried out my original Srsly… and had the same problem Chad ran into. It just didn’t do what the hardware box did. But I wasn’t done… so I started running stuff into the real hardware box, and just fooling around with the specific audio I’d begun to use, and rapidly worked out what was happening. My original Srsly left out a lot. It was more ‘audiophile’, more subtle, would fit in with more accurate recordings, but the real deal hardware device could be pushed WAY farther.

…in a way that I could interpret. And coding ensued…

Meet Srsly2. I’ve intentionally not tried super hard to exactly duplicate what is, after all, an unobtainable original hardware box by Howard Hughes’ company. Variations of this are still being licensed for use in car stereos and things, and I intentionally make no claim that I’m duplicating someone else’s property.

But. But. BUT. What I was asked for, was to accomplish a particular effect, where the stereo wideness could be made crazy exaggerated. And I was able to interpret what a real hardware box (not original, though) was doing. And I continued to modify Srsly until, with Srsly2, you can now dial it in to do very similar crazy and unreasonable things… and that’s probably close enough for a free and open source plugin modeling an ancient hardware device that can’t really be found anymore. You’ll find the controls ought to work as you’d expect them to, and you may find as I did that leaving the Center control alone and cranking up the Space control just right, can get you into a wild and somewhat boosted and hyped zone that makes the most of your spectacular stereo content, in much the same way the original, obscure, Hughes box did.

That’s my hope, anyhow. Hope you like it! I know I’ll be using it on stuff.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Srsly2 processes audio in the Stereo category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Stereo](../categories/stereo.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Srsly2)

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
