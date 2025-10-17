# Highpass



## Quick Info

| | |
|---|---|
| **Category** | Filter |
| **Type** | Filter |
| **Status** | Stable |

## Description

a time warp, for retro midrangey sounds

## Detailed Overview

These (Lowpass and Highpass) are mixing EQs, not mastering ones (though I’m not the boss of you). They’re complementary: the one is the inverse of the other. However, because of their peculiarities that makes them behave quite differently. What they have in common is they’re interleaved IIR filters, something people don’t normally do. The experiment here has to do with my discovery that digital audio only exists in sets of samples (never just as the isolated sample: the waveform isn’t there, the sample value is only a signpost that the audio is to weave its way around)

They’ve also got a very unusual parameter, soft/hard or loose/tight, which controls how the IIR filters are fed audio. When you offset it, you get a situation where the cutoff is higher at louder volumes, or at quieter volumes. This is on a sample-by-sample basis so it’s a tone-character modification, subtle but interesting. Loose/tight is just the best way I could describe what’s happening there.

Lowpass gives you a treble rolloff (some have joked that I make dozens of treble rolloffs! Yes, but they all sound different) and what’s immediately obvious is, the stuff right up by Nyquist on the threshold of hearing is not rolled off with the rest of the treble. Also, if you only want to cut extreme treble, you can do it with just adjusting the soft/hard control away from the center position. At deeper cut settings, the soft/hard control gives you two different textures (both of which keep a hint of ‘air’ right up top). The dry/wet control allows you to blend your result. Lowpass gives you big sounds with various colorations and a sparkly gloss that comes from your underlying sound: it’s a big-ifying filter that might suit huge synth pads or orchestral tracks.

Highpass, the inverse of this, gives totally different impressions. The same filter-offset behavior turns into ‘loose/tight’ and the extreme treble gets stepped on, rather than retained. This makes Highpass take on ‘classic’ tonalities, particularly with the offset on ‘loose’, which gives a tubey and softened texture. If you run it full-wet, you’ll get a radical ‘analogification’, wiping out all extreme lows and the highest highs, and sounding like some small vintage radio at high filter settings. It’s a small-ifying filter that’s also a time warp (with offset on ‘tight’, you have a transistor radio instead, still retro-sounding!) and all you have to do is dial in your boost area and then balance it with dry/wet to get intense texture shaping that normal EQs can’t come close to delivering.

Again, these are not mastering EQs unless you face really unusual mastering requirements. They’re mixing tools, and they really do act like different animals so they’re each contained in their own plug. They’ve been around for ages but the revision to VST form has brought them a new level of tonal sophistication plus the very useful dry/wet controls that take them out of ‘experiment-land’ (they have always been building blocks for plugins such as Guitar Conditioner) and makes them stand alone as useful mix tools.

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

Highpass shapes frequencies through filtering. Use it for tone shaping, problem solving, or creative sound design.

## Usage Tips

- Make small adjustments - EQ is powerful
- Cut first, boost second (if needed)
- Check your changes in context with the full mix
- Use solo to identify problem frequencies


## Related Plugins

Browse other [Filter](../categories/filter.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Highpass)

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
