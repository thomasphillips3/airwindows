# Isolator



## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

a steep highpass or lowpass filter, like you might find in a speaker crossover

## Detailed Overview

Isolator is like some of my Biquad Filter plugins, except it’s tuned to a particular purpose. In DJing, one technique is to use a filter on the full mix for effect, and Isolator is geared towards two specific tricks in that vein: sweeping the filter down until the music is just a throb and then bringing it back, or sweeping the filter up to leave only highs and then dropping the bass back in.

This is done using a speaker-crossover style filter: Isolator is a fifth order Butterworth filter made out of three series biquad filters run inside an instance of Airwindows Console. It rolls off at 30 dB/octave (I think I had this as 36db/octave in the video, but that would be a sixth-order filter) and probably slightly steeper than that, because I’m up to my usual tricks and chose the fifth order Butterworth because it’s made out of Q factors that are a close approximation of the golden ratio. So, I’ve used that, making the filter JUST a bit steeper than normal :D also, the way the frequency control is mapped, means it gives you accurate control over the full Nyquist range of the filter AND still puts the midrange in the middle of the control, through changing the logarithm of the filter frequency. That means it always is able to go full-range no matter what sample rate you’re at: maxed out, is always ‘max sample rate’, it just sweeps farther up when run at higher sample rates once you’re at the far right of the control.

That’s the tech rundown. In practice, this is a lowpass/highpass filter. You can sweep it around, though it’s possible to freak it out if you throw a lot of filter-sweep activity at it in a zone where it’s handling a lot of energy. It wouldn’t be good to try and FM this control: biquads sound wonderfully smooth and rich but they won’t handle that treatment, especially run inside their own version of Console. You can use the treble and bass controls as a form of shelf, or output gain: note that I’ve set them up for instant response so you CAN FM them or do really aggressive, choppy things with them without upsetting the filter. That said, if you have a heavily bassy sound coming through them, you can get clicks since they will respond instantly: it’s that or have them chase the value, and you can’t do aggressive glitchy stuff if you chase the value, so I’ve got them responding directly. That does mean you can do stuff like have the lows coming through and then ‘flicker’ in the highs setting for a glitchy effect, at whatever speed you can automate the slider.

I expect mostly this will be useful for the classic ‘now it’s all bass… and now the full mix gradually swells up’ effect, but there are many possible uses. You can use it to neatly lop off highs or lows with the steepest cutoff possible that isn’t QUITE resonant. You can cut the bass on tracks with great accuracy, and you can use it as a shelf of great accuracy: the bands are made by subtracting from the lowpassed version, so having both treble and bass full up means you have literally unaltered digital audio, apart from some ‘zero dB’ multiplications. That means very subtle cuts in highs OR lows might be using a sharp near-resonant filter sound, but the less cut you have the cleaner the output will be. It’s a mastering-grade surgical high/low shelf, much like professional DJ isolators must be constructed to carry the full mix with ideal sound quality.

Except I can beat those in one very Airwindows detail: if you are using it as a lowpass, and you’ve got high on zero and low on 1 and you open up the filter completely sweeping it up… no matter what sample rate you’re at, once you reach 1 (full crank) on the frequency control, it seamlessly bypasses itself while still calculating the filtered signal. So, unlike analog isolators, when you run THIS isolator on the full mix, at times you’re not using it, it is literally not in the signal path anymore. :D

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Filter Stage]
    B --> C[Resonance]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```

## How It Works

Isolator shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Isolator)

**Categories**: Filter

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Filter](../categories/filter.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
