# PitchNasty

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Effects |
| **Type** | Effects |
| **Status** | Latest Release |

## Description

a primitive pitch shifter that also has primitive time-stretch artifacts

## Detailed Overview

So this is a bit unusual. Though this is a sound mangler, there's no bit crushing here, and in fact most of the time it's delivering a very high-res immediate and punchy pitch shift, super clean and tight.

It's just that the rest of the time it's throwing a nasty, loud sample-glitch, at audio rates. No, beyond that. It's throwing digital trash at you so hard it becomes a musical note!

And therein lies the secret of PitchNasty. This plugin brings you the heart of old school digital like your classic Akai stuff, back when they did not have the luxury of doing anything elegantly or nicely. Instead, you got things like time stretches that just plain looped a tight time cycle and overlapped it, producing a weird digital honk. Some folks really seem to crave that stuff, and there's a reason.

Turns out if you do that, your results tend to be very punchy, direct and intense, except for the weird robotic overtone that's welded to the sound like it's a musical note. Things like drums love being timestretched or repitched in this way! It's a whole retro tone, which PitchNasty starts off with. The crossover is very slightly 'clever' in a way the retro stuff isn't, for the purpose of making it sound more retro and less DAW-like: it keeps the presence very high while slightly masking the high frequency edge of the 'note' you get.

But then PitchNasty goes way beyond, in that Airwindows way. You've got two pitch controls, one giving you note intervals in half-steps, and the other being a pure pitch bend. They stack, for really high or low bends. Then, there's a control that's the same as the classic Akai method of setting the sample buffer size… but for this one, you specify the buffer as a musical note (six octave range). Set it insanely high and you're basically not able to pitch shift anymore because the buffer's too small, set it insanely low and it barely registers as a note anymore. And then after that, how about a feedback? How about a feedback that can be cranked to more or less constant regeneration? This gives you horrible wonderful old Eventide noises of many descriptions, or you can use traces of it to make your existing sound more complicated and harmonic-dense.

And then the whole thing's followed by a Dry/Wet, and you can see that PitchNasty sticks so tightly to the underlying sound that you can get it acting like a giant flanger or strange overtone generator. And that's the other secret of the crude old Akai-like time/pitch processing: when you don't have any RAM or CPU to work with, you can only do naive primitive things that happen to sound really immediate, direct, alive. It doesn't lose the impact of a drum track. If you set it up to thicken a snare by applying, Eventide-like, a 30% layer of pitch up (or down, with feedback), there is no flam or hesitation to the sound like more sophisticated algorithms would have to do.  Instead, it's just THERE in the sound, with a hefty dose of digital gnarliness, but woven right in to make a very 80s composite sound that's huge and fierce.

If you would like to use this as a time stretch, what you should do is open the source sound in an editor, change the sample rate without resampling until you have the new pitch you want and apply that, resample it back to what your working sample rate is (use a good resampling method, you don't need to use a bad one), THEN use PitchNasty to re-pitch it to what the target pitch is. That'll give you the time-stretch artifacts, because they are really just pitch-change artifacts used in a different light. Hope you like PitchNasty!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

PitchNasty processes audio in the Effects category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Effects](../categories/effects.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/PitchNasty)

**Categories**: Effects

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Effects](../categories/effects.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
