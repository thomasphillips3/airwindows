# Surge



## Quick Info

| | |
|---|---|
| **Category** | Dynamics |
| **Type** | Dynamics |
| **Status** | Stable |

## Description

a compressor for accentuating beats and pulses

## Detailed Overview

What is ‘ballistics’ when it comes to audio gear? It’s the way the gear handles dynamics coming in. It’s the swing of a VU meter that can tell you what your music feels like.

Or, since this is Airwindows and we don’t do no steenkin’ meters, ballistics is the way dynamics hit this compressor to produce outrageous groove.

This is also a good reason to keep me around working on stuff… this plugin wouldn’t exist if not for an earlier free VST plug from me, called SurgeTide. That one controls dynamics by altering the rate of change of the rate of change OF the rate of change of the audio. What, you may ask, would happen if you did that? I’ll tell you: firstly, there is no smoother compressor. It’s utterly, totally fluid and artifact-less, organic to the Nth degree. But, it doesn’t sound like it’s doing anything until suddenly it kicks in and starts making the dynamics swing up wildly to boost every beat. Incredibly hard to control. You really can get a sense of ‘huge surges of the musical tide’ emphasizing the deepest rhythms, but it’s a bear to set up!

And since I’m still out there working on stuff thanks to my Patreon, now there’s a whole new version, so different it counts as a separate compressor: Surge.

Here’s the thing. Compressors are as unique as, say, guitar overdrives. You can search for the magic one, but there can be all different sorts of ‘right one’, with hugely different characters to ’em. I made Pyewacket as a free VST. It delivers a super-articulate attack transient and leans out the sound rather than simply turning it down, and gives a ‘British Classic Rock’ vibe without any silly adding of faux-analog mud: that one clamps down on the body of sounds while leaving tons of intensity and headroom to the tone. Its ‘ballistics’ are very simple and it’s more about delivering a certain kind of attack, and making stuff more even and consistent.

Surge isn’t anything like that. It’s SurgeTide, but easier to control: just bring it up until it starts compressing enough, and don’t go too far to where it inverts the dynamics. You can hear it easily, unlike SurgeTide. But it still retains most of the uncanny fluid organic quality SurgeTide has, and most importantly, it has the ballistics. That means that if you put a pumping, rhythmic mix through it… it will accentuate the beats in a very aggressive way that’s not like anything you’ve heard before. The attacks pop way out, including the deepest bass pulses: this is yet another way to handle compressed bassy mixes and transform them into something punchier. And unlike SurgeTide, it’s very controllable.

You might want to push it hard enough that the dynamics jump way out. You might want to use it as ‘glue’ and hit it only very gently, and take advantage of that extreme fluid openness (a result of the way its control is so abstracted: again, it alters the rate of change of the rate of change OF the rate of change). The one thing it won’t do at all is limiter-like behavior, it’s way too funky for that! So anywhere you need to use a compressor that is just ultimately funky, bouncy, squishy… try Surge. It might be right up your alley.

Summary: Surge is more obvious and responds easier, SurgeTide is cleaner and harder to control.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Detector]
    B --> C[Gain Computer]
    C --> D[Gain Reduction]
    A --> D
    D --> E[Output]
    style C fill:#6366f1
    style D fill:#f59e0b
```

## How It Works

Surge controls dynamics through peak control. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.

## Usage Tips

- Start with gentle settings and increase as needed
- Use Dry/Wet for parallel compression if available
- Listen for pumping or artifacts
- A/B bypass to check if processing helps the mix


## Related Plugins

Browse other [Dynamics](../categories/dynamics.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Surge)

**Categories**: Dynamics

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Dynamics](../categories/dynamics.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
