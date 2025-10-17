# VinylDither



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

a high-performance dither that converts digital noise to ‘groove noise’

## Detailed Overview

To explain this dither, I’ve got to talk about SACD (DSD) a little.

There’s a super-hi-fi digital format known as DSD (direct stream digital). It uses a sample rate in the megahertz, but not as many bits (as few as one, even!) and is tricky to work with. It’s a bit like having Class D amplifiers: those also use an incredibly high frequency switching system, and produce a clear, fluid sound that totally lacks some audio flaws.

DSD is like that. There are some things it does incredibly well, and other things it gets wrong. Notably, it’s incredibly good at delivering accuracy on deep bass notes, but it’s all over the place on supersonic frequencies and can produce a ‘splat’ of high-frequency overreaction if you drive it too hard there. The performance of DSD increases as frequency lowers. All its ugly is reserved for the super-highs, but nothing comes close in the midrange, low mids, bass and so on. That’s fundamental to how the format works: accuracy becomes a statistical pitch-related thing and the deeper you go, the more of a lock DSD has on the sonic truth.

What if it was possible to emulate this behavior in a dither? First, you’d need to use a really intense noise shaper, not just dither noise. Then, you’d have to make it have the same frequency-related thing where lows get increased accuracy. And lastly, you’d pay the same price: it’d drive the error of the system into the highs and do a lot of unpredictable, ugly things there.

Meet VinylDither! It’s the extension of an old dither I had called Ten Nines, which does exactly this. With Ten Nines I was able to get a noise floor under -200db on 16 bit audio (if I remember correctly)… but only at frequencies ten hertz and below! It also spit out loudish crackling noises at high frequencies. The experiment worked, but not everybody loved it.

However, if you weren’t paying close attention, the noise behavior was kind of like record surface noise, and that gave me ideas.

VinylDither is the result of pursuing those ideas. It’s a dither/noise shaper which completely removes the ‘steady white noise’ noise floor of normal dithered digital, and replaces it with a more crackly, surface-noise kind of sound. That’s produced from storing up error energy that would mess up your midrange and bass, and releasing it in bursts and sparks. VinylDither is the first of three dithers I’m releasing that are professional quality, boutique dithers and sonically better than TPDF. If it’s really important to you for your noise floor to be featureless and sound like white noise down there, you won’t want this. However, if you’re an analogophile and like vinyl records, you’ll instantly recognize the ‘vibe’ of this one. It does an incredibly good job at giving ‘vinyl’ clues down at the threshold of hearing but this is not a ‘sound effect’ being added, it’s the natural digital error being rearranged to get that effect.

So, if you want ‘vinyl’ effects added to your mix so it sounds like a retro vinyl record coming off the computer, this is the single subtlest way you can do that, plus you could combine it with other things (like the Audio Unit ‘ToVinyl’ which does elliptical EQ and has an amazing groove wear emulation built in) and get a completely different vibe. Wrecking your sounds with heavy overprocessing isn’t necessary! You can just pick specific things to give a more subtle vinyl feel, and VinylDither is the perfect dither choice for it. Yes, it’s got more depth and warmth and vibe than plain old TPDF (or truncation), but I think the interesting part is examining the faults of VinylDither (crackling noises, not smooth noise) and understanding how they can be turned into advantages (crackling noises OK, do not correct! As it says on my vinyl copy of Live At Leeds cooge )

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

VinylDither processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/VinylDither)

**Categories**: Dithers

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Dithers](../categories/dithers.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
