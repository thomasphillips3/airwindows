# DubPlate

![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Utility |
| **Type** | Utility |
| **Status** | Stable |

## Description

ruthless dubplate mastering for electronic music

## Detailed Overview

It's possible you need this to make your music sound its best. I've used this literal plugin to put out a record! Just now, on something that I'd tried to get right for years!

It's also possible this is a retro-themed blast from the past with no use in a modern world of downloadable hyperaudio and that you'll immediately know it's trash not to be taken seriously.

Let's explain. A dub plate is like a vinyl record except it's cut from acetate, which wears out quicker. These are traditionally known as 'masters' and electroplated to make vinyl-stamping machinery, but you can also play them on a record player directly. The UK electronic music scene went through a phase where dubplates were extremely popular, with mastering houses booked solid and people waiting in lines to get their dubplates made from their DAT tapes. The experience of going to clubs and listening and dancing to this music was a golden age all its own, separate from the golden age of rock or metal or prog, etc. And there's a distinct dubplate sound that can be exploited, one that's wildly different from what you typically get out of DAWs or stuff like lofi hip-hop, even though people like to bring in lofi elements to resist the 'DAW sound'.

What's this dubplate sound made of? There's an unexpected reason beyond just the lacquer material. Airwindows DubPlate makes NO effort to mimic surface noise, or groove wear, or any of that. Instead, it acts like a mastering chain that's so bulletproof it can resist any terrible audio thrown at it. There's three ways it does this and gets the dubplate sound (it was dialed in using Airwindows Meter to track what's actually happening sonically)

First, you can't just throw any synthetic noise at a vinyl record and have it play. You can even break a lathe if you throw too much high frequency energy at it. So, DubPlate uses the 'glue' control in Mastering… except it uses an intensity Mastering can't even reach, and it uses two of them each set differently, just to get to what was coming off the dubplate example I had as a real life reference.

Second, the side channel is highpassed very aggressively! Dub plate houses had to handle anything that came in the door no matter how insane it was, and there was no time to fiddle with a troublesome DAT tape. If the guy had thrown in a full volume 808 kick distorted and out of phase, well, the mastering house had to turn it into a dubplate that played, and so the side channel doesn't let any bass in. (There's a special technique that might warrant more exploration, which I included to help things stay punchy even when filtering that aggressively).

Lastly, even the mid channel isn't safe! Making competitive dub plates, you couldn't let people swamp their audio with subsonic rumble no matter what they made their synths do. The gear of the time was already capable of getting you into trouble and burying everything in useless energy-sapping sub-bass, and musicians could be expected to get this wrong as easily as they could get it right. (Monitoring contains a zero cross section and a reference 40dB line that can show you whether your bass is unproductive in a live setting.) Plus, simply running into the analog amps and lathes of the day, the mastering chain, could drastically alter the subs. And so, Dubplate goes after extreme digital lows as well, reining things in until you could cut the output of the plugin to a lacquer and be pretty safe from trouble no matter what audio you put in. This one also uses the technique for having the force of the bass stick around while being reined in.

And that's the secret. If you have a fantastic playback system, killer subs, and years of mixing experience, then maybe you can get creative and come out with something that will be awesome, and then tweak it with Mastering and Meter, and you get to explore the farthest realms of audio creativity without setting a foot wrong.

If on the other hand your reach exceeds your grasp, you can put together creative exciting stuff that also happens to be real obnoxious on multiple levels. You're distorting too much, and you didn't notice that you went over-bright, and a bunch of things in your bass are freaking out, and it's too complicated and to make it safe takes away the heart of your creative decisions.

So, go into DubPlate… pad your stuff down with PurestGain if you have to, the output might peak louder even if it is pulling the subs back… and let the uncaring mastering chain strip down your sound into the gutsy heart of its intention. If it's hyperpop you wanted, maybe you check out right there. But if you're looking for size and depth and power and the sound of the dubplate era calls to you… maybe this brings your music the rest of the way there.

Hope you like it! I put out a record (Dragons Dub Plate Edition) specifically because I had music literally from that era made using those methods, and the plugin instantly turned it into the experience it was always meant to be. That record's at the usual bandcamp price but DubPlate is open source and free! See if it helps you out :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DubPlate processes audio in the Utility category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Utility](../categories/utility.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DubPlate)

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
