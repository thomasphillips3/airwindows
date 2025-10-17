# SoftClock

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Latest Release |

## Description

a groove-oriented time reference

## Detailed Overview

By special request, here's SoftClock before I can properly demo and use it. I'll have to play catch-up!

SoftClock is a timing reference, like a click track… but far more powerful, because it does not synchronize machines so much as it synchronizes HUMANS. You put it on an unused track, and route it to another track AS AUDIO which you then record, in the arrange window as just another audio file. This can be done as you lay down an initial track while listening to the SoftClock output.

What's the noise it makes? Frequency swoops, of a tone. It doesn't turn on and off, there's no attack or decay… a continuous tone which drops in volume as the pitch drops, but otherwise is just a drone… and this is your new click track.

The next question is 'for the love of God, why would you do such a thing?' Because not only is this not a percussive sound, it doesn't even have a definable attack, and yet it proposes to replace click tracks, and in fact wants to become a timing reference for a world of 'human played' music where nothing is snapped to grid. There will be no grid, just human-played tracks riffing over SoftClock.

The reason is, Entrainment. The 'swoop' of the tone mimicks the swing of a drummer's arm, or the strum of a guitar… or a dancer's body. It's digitally accurate, but directs the listener not toward an inhumanly accurate 'tick' but towards a motion… and when many players are moving in synchrony, that's when you have a powerful groove.

But there's more. It's also a reference to where you are in the bar. The non-accented beats ebb down to a lower tone, and then ramp up again toward the One, which is the loudest and highest-pitched swoop of the tone. The amount of variation can be controlled, as can the basic pitch. Bear in mind the volume does modulate, but not in such a way as to produce an attack, even at the fastest speed settings. You dial it in to mimic the motion of your body playing, whether that's groovy or laid-back or hammering, and the non-accented beats always show you where you are in the bar, in an easy-to-hear way, even if the beats are themselves swung or the backbeat is slowed to add weight and bombast.

What about those accented beats? Firstly, they're louder and higher-pitched, but they're also spaced out in an interesting way. You see, SoftClock can give you 4/4, or eighth notes, or four bars of 4/4… but it will also give you odd times beyond your humble sevens and elevens. It'll give variations on funny times when you've gone beyond 4/4. Here's the list, and how they're counted:

1, 2, and 3 are counted as you'd expect. 4 is counted as 2,2. 5 is counted as 3,2 (in other words: one two three one two, with one being the accent). 6 is 3-3, and 7 is counted backwards from how Pink Floyd's 'Money' had it: 4-3, one two three four one two three. 8 is 4-4, 9 is 3-3-3, 10 is 5-5.

Then things get more complicated. Note that Count numbers 8, 16, 24 and 32 are reserved for 4/4 with accents every eight beats, so you can have normal time but hear the unaccented beats guide you around one, two, three or four bars and highlight the first One.

11 is counted four ways: 3332, 443, 551, 65.
13 is counted three ways: 3334, 445, 553.
17 is counted four ways: 44441, 5552, 773, 881. 
19 is counted four ways: 44443, 5554, 775, 883.
23 is counted four ways: 444443, 5558, 7772, 887.

Count the accents and they'll come in these spacings. It's options for 'sub-phrases', repetitions or modulations up front and a variation for a turn-around, orienting you to the odd rhythm. The idea is for the repetitions to themselves be easily countable, and ideally seem to fit into a 'four sections but one is different' or 'three sections but one is different' model.

This is in line with a music arrangement game I've been developing that's more likely to see life as a video-game now than as the card game I'd intended. Point being, SoftClock can do normal metronome things (except using entrainment rather than ticking at you) and orientation things as far as locating you in the bar, but it can also combine all that into a baffling proggy rhythm that nevertheless guides you into grooving and memorable riffs of many kinds. If the standard variations on freaky prime-numbered prog-meters aren't enough, you can play with Swing and the delay of BigBeat (accented beats) until you've gone full Beefheart: or, rather, full Magic Band and John French drum parts.

Dive as deep as you like, or keep it more simple: SoftClock has you covered. You may be surprised at how much easier it is to hear, entrain, and orient yourself when using a click track that refuses to click. Remember, lay it down as a track, don't try to match it to a normal click, don't grid anything! SoftClock is for gridless grooves, and music that sounds human because it moves like humans. See how it feels.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

SoftClock processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/SoftClock)

**Categories**: Utility

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Utility](../categories/utility.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
