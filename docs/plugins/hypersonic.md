# Hypersonic

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Brightness |
| **Type** | Brightness |
| **Status** | Latest Release |

## Description

Ultrasonic, but steeper and higher cutoff

## Detailed Overview

Hypersonic is the same as Ultrasonic, except it’s running seven stages of filtering instead of five, and it cuts off a little higher: for these reasons, it’s the Airwindows ultrasonic filter that ought to not soften the super-highs even for golden ears and sparkling youths :) I don’t think the original Ultrasonic sounds bad and I use its type of filtering in my work a lot, but I also like depth in sound and the presentation of a soundstage that’s not too upfront and close. It makes sense that the slight softening of super-bright frequencies that original Ultrasonic gives you, wouldn’t work for everybody: not everyone wants ‘glue’ or ‘analog’ or ‘recording console’, sometimes you just want the purest digital you can get.

I think there’s a fair chance this filter will work out for folks whose aesthetic leans toward the superultramegahyperbright, even if that ain’t me. It combines enough filter stages to act like a 14th-order Butterworth, and it cuts off just high enough beyond 20K that you should get everything up to insect-repellent audio, unsoftened.

I’m also working on something else that may give rise to big changes (I know, it’s like 2022 is all the promised big changes, but this one might be extra interesting). Compare Ultrasonic to Hypersonic… CPU-wise. I am pretty sure that I’ve got Hypersonic outperforming Ultrasonic on every possible platform, even though it has two more filter stages than Ultrasonic. The question is, am I making a choice that is hurting the sound?

A bit of background. There are a lot of devs who like using 32-bit floats for audio math. They’re fast, can be calculated in parallel… but everything you do with them, you erode away louder samples by constantly truncating your internal variables to roughly 25 bits. You’ll never hear that doing it once… but for every little calculation, which could be thousands or tens of thousands? I think that’s a hidden difference between digital audio and analog audio, and I think it matters.

So much so, that I run an internal buss in my plugins that is 1,099,511,627,776 times more high-resolution than that. It’s served me well, and I like the sound I get. But I’ve also run across folks who use a slightly different arrangement: they’re not dithering floating point like I am, but they ARE using a high-res buss. How high res? 536,870,912 times better than the more efficient floats, that’s how high res. Now, what I’ve been doing is one trillion ninety-nine billion five hundred eleven million six hundred twenty-seven thousand seven hundred seventy-six times more high-res than your average float. But who’s to say that we can’t get by with only five hundred million times better than your average float? :D

And so, we have Hypersonic. It’s using more filters than Ultrasonic, but running faster, and it’s still five hundred million times more accurate than your average float-based audio software, and it still dithers to a 32-bit buss such as CoreAudio on the Mac. But hey, if you’re running Reaper or something else with a double precision buss, it doesn’t have to dither at all as it’s working natively at that resolution! So my challenge is this: does anybody, myself included, hear ANYTHING more truncate-ey or degraded about Hypersonic when compared to Ultrasonic, even though it’s running more stages of filtering? I challenge you, tell me if you think you can hear a drop in quality here. I’m all about the overkill, but I suspect I can get there on the native Reaper 64-bit buss: and of course everything AU or otherwise that does run a 32-bit buss gets dithered to that buss whether it’s Mac or PC or Linux, and I’m thinking I can start to bring some really serious performance gains to everything. I will of course keep an archive of all the Airwindows plugins as they existed before re-hacking them in this new way, so you will be able to have access to the previous plugins (of all kinds) that ran the ultra-super-hyper-overkill audio buss. Might be desirable for mastering folks, or those who are incredibly fussy about analog-style sounds. I’ve been doing a fine job of keeping the audio busses cranked wide open to ultimate resolution for years, and the whole Airwindows library is like that.

But if my suspicions are correct, we can have that as backup and then also have the whole Airwindows library running WAY faster.

And then when we move on to the new format CLAP, and begin to bring out select plugins with GUI and interfaces and metering, they can also run their audio stuff at that nice happy medium between high efficiency and no-compromise audio buss.

(followup: I did in fact end up re-hacking the entire Airwindows plugins collection on all platforms as double precision rather than long double. Though on some processors like the Mac M1 it weirdly turned out that the long doubles were fine and didn't cost me extra CPU, hence I didn't gain anything much from the change on my own systems)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Hypersonic processes audio in the Brightness category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Brightness](../categories/brightness.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Hypersonic)

**Categories**: Brightness

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Brightness](../categories/brightness.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
