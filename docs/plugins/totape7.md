# ToTape7



## Quick Info

| | |
|---|---|
| **Category** | Tape |
| **Type** | Tape |
| **Status** | Stable |

## Description

Airwindows tape emulation with bias and Dubly

## Detailed Overview

So about that simplification of ToTape? Nah. But… set everything to the middle and you can ignore all the many controls.

ToTape7 not only upgrades pretty much every single thing about ToTape, but it brings new functionality beyond any previous version (even when they're good) and it lets you go completely bonkers tailoring signature new sounds however you like them. This is the ToTape for people who wanted all the controls, and more. It's the ToTape for salvaging any sort of audio no matter how DAW-like it is… and it's the ToTape that can be stripped right down to serve as its own FromTape, anytime you like, or if you're trying to run lots of channels of it because you want to tape all the things and then mix them down also to tape. Which it's great at, by the way, as it soaks up loudness super well and even has a ClipOnly2 built in so it can serve, standalone, as your ultimate loudness clipper.

ToTape7 has exactly as many controls as you can fit in Airwindows Consolidated, which means it'll also run in VCV Rack. That means there are some possible controls it skips, and exactly one control that's dual-ganged with two things riding on one single knob. It's just a different knob this time: used to be dual-ganged on the knob marked Soften. The controls from top to bottom operate Dubly Encode, Drive, Flutter, Bias, Head Bump, and Dubly Decode. Again, set everything to the middle for 'normal', but you can go way past normal if you want.

Dubly Encode (not the same thing but the same concept as a famous noise reduction system) applies a brightened and compressed boost to the audio pre-tape, with the amount governed by Amt and the highs cutoff by Freq. (Dubly Decode is exactly the same, except it simply subtracts the effect it makes: this is the secret Seventies tape sound, especially when you tune the Dublies to produce effects). Match them to get mostly 'normal' sound, mismatch them for effect: mind that you don't boost Decode Amt too much or it will produce sort of anti-crunch sound, going past 'cancellation' to obvious distortion. (or do it if you feel like it, I'm not your boss)

Tape Drive is your boost (or pad). 0.5 is unity gain. Boost if you want lots of tape drive, or to loudenate. You should have a good ability to do this and make it sound the way you want. Since Dubly was added, it's even better at allowing for clean gain here, as Dubly tends to suppress harmonics from distortion.

Flutter is like Flutter2, but is NOT exactly the same. It's updated, even since Flutter2, for the purpose of letting the '3D tape' emulation (letting tape bend laterally as well as stretch) be more accurate. It's also toned down a bit so 0.5 gives you a reasonable, real-world flutter effect. The two channels will use their randomness to try and chase each other a little, much like how TPDFWide does the same thing to be LESS correlated. Turns out with default settings this is really, really good at getting a spacious tape realism without letting the imaging go too weird. You can also bypass the whole thing by setting Flutter to zero: if you're running at low sample rate, consider doing that if you're running lots of ToTape and losing the extreme highs. I might not run Flutter on multitracks, just the buss.

Bias is usually set to slight overbiasing. It's like GoldenSlew, but it's simplified and it's being run between Dubly encode and decode, so it's acting differently from the standalone GoldenSlew. Underbiasing also works but is a different algorithm that's probably not going to be people's first choice, but you can do it. Slight overbiasing is your best weapon against unpleasant tizzy highs.

Head Bump is like DubSub2, but it too is updated even more to get more out of ToTape7. There's a highpass built in at 0.5 setting that balances the bump against the rest of the audio, making it so if you stack up the plugin it doesn't get too messy, modeled after references of real tape machines doing multiple generations. Anywhere you set the head bump frequency should get reasonable results with Head Bump at 0.5. If you pull it back OR boost it, you begin to drop the highpass as you do that, meaning it will either crossfade over to the original digital bass (with extended subs) as you reduce the bump, or it'll start adding even more exaggerated bump to the original bass as you crank. So, it's a special voicing for doing all of the things, with 0.5 as the 'peak realism' and most restrictive setting. Ouside that, just pick whether you want less 'tape bass', or 'mega bass' by combining the source and the bump.

Said bump still does the thing from DubSub2 where it's also giving a mild notch at double the frequency, which is characteristic of pretty much all real tape machines. You get to pick the frequency, because why would you be tied to a given machine when they're all different frequencies already, and when the heart of the effect is not getting the frequency right, but the unusual Airwindows head bump algorithm that'll work just fine however you voice it?

And Dubly Decode helps you get even smoother, more compressed sound out of the tape saturation, and lets you dial it in by both amount and frequency. Be aware that it's a really gentle treble-slope, so making subtle changes to frequency will have an effect on the character of the sound but won't produce wild effects. Basically, if Dubly mostly balances but Enc is crossing over lower than Dec, there will be a sort of lower midrange hype that comes through: if Dec is lower than Enc, it's going to be drying up that energy and making it a bit tighter. They're supposed to cancel out, but half the reason classic records all sound different from each other is that this system in real life required a lot of fussy tuning, and some people set it up by ear and ended up with distinct tone qualities for their studios when they did. It's not so much 'EQ' qualities as texture. Experiment with it to see if you have preferences.

And that's ToTape7! Ought to hold people for a while, and be a decent upgrade from ToTape6, even though people really like that one (and it's still there so you can still have it anytime you want).

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

ToTape7 emulates magnetic tape characteristics including saturation, head bump, and flutter. Use it to add warmth and analog character.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Tape](../categories/tape.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ToTape7)

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
