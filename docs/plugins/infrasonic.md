# Infrasonic



## Quick Info

| | |
|---|---|
| **Category** | Bass |
| **Type** | Bass |
| **Status** | Stable |

## Description

a very steep subsonic filter, built like Ultrasonic

## Detailed Overview

If you saw my recent post about Ultrasonic… this is the same, but at the opposite frequency extreme! It will nuke DC offsets and reshape thunderous rumblings into specifically ‘audible’ subsonic rumblings. That doesn’t mean it will always make the amplitude of subsonic bass go down: there may be times when it alters the waveform so it peaks higher. But it’s the same thing as Ultrasonic: tenth-order Butterworth highpass filter, executed as cleanly as possible (NOT with an internal Console system expanding the tone) using very high resolution math.

Normal audio recordists and people working with analog sources will probably find this does nothing for them. But if you get frisky with DAWs and do weird things in the digital mix, you may just end up producing low frequencies that aren’t properly sonic anymore. Normally, you’ll be using various highpasses to tune your deep bass for the purposes of your mix, and this isn’t for that: it’s a more abstract concept of a filter.

If you’d like to neatly excise everything below 20hz and retain EVERYTHING remotely considered an audio frequency, especially if you’ve got DC offsets coming out of your other digital processing (I’ve tried to fix a lot of my plugins that do this, but there are other plugins out there which can produce it), then this might be handy. It’s also one of the Airwindows featureless add-and-forget plugins, and I’ve always liked making those: speeds your workflow. No window to open, just put it in the relevant place and you’re good to go.

I will also note that this is very likely not what you want for a mastering highpass, because the steepness of the filter means a lot of crazy phase shift. I see it more as a special effects filter, something that can take a rumbly noise and give you a very tailored, impactful result with minimal content actually below 20hz. Sound design is where I'd use Infrasonic, and I'd check to see if I still liked it better than a normal subsonic highpass.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Infrasonic processes audio in the Bass category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Bass](../categories/bass.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Infrasonic)

**Categories**: Bass

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Bass](../categories/bass.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
