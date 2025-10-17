# ChimeyGuitar

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1) ![Basic](https://img.shields.io/badge/-Basic-f59e0b)

## Quick Info

| | |
|---|---|
| **Category** | Amp Sims |
| **Type** | Amp Sims |
| **Status** | Latest Release |

## Description

a supremely compressible instrument amp

## Detailed Overview

Here's a followup to PointyGuitar. What if, instead of distort, the imaginary amp compressed?

The tone stack works the same: in fact, it's exactly as it was in PointyGuitar, as is the cab simulation (a highpass and lowpass made out of AngleEQ, which is able to be very resonant and colorful). That's on purpose. I want it to be familiar, so the way the tone shaping works is exactly like PointyGuitar, and if you can dial one in, you can dial the other.

But instead of the basic distortion as found in 'FireAmp', what's there? BeziComp. Not even a normal compressor, no, it's the new experimental one that turns the amplification factor into a Bezier curve… but BeziComp has one instance of itself in play. ChimeyGuitar?

ChimeyGuitar has eight, at full crank.

Stacking compressors like this isn't unheard of: the FMR Really Nice Compressor has 'Super Nice' mode, which cascades three compressors in series. It's just that ChimeyGuitar does eight, of a new design which I don't think existed until I started it. That also means it's on me to sort out what the strengths and weaknesses of this new kind of compression are, seeing as we have as many as eight of them in between every EQ stage now.

First, it can react very quickly, but refuses to alias since it will not apply a volume 'corner' above its minimum radius. This matters less used inside ChimeyGuitar because plugins like this repeatedly filter out aliasing harmonics anyhow, but it's significant because usually as you have compression kick in you hear continued interaction between the sound, and the speed of attack. That lets you dial in a squished, unvarying sound by hearing that overtone as if it was a form of distortion (which it is), but BeziComp and ChimeyGuitar don't have any of that compression artifact at all.

Instead, you'll hear an odd warble when you push ChimeyGuitar too far. It's similar to when you're using DeRez3: while Bezier curves can sound like a brickwall filter, there's an strange resonance associated with it. In a compressor, when pushed hard, we hear this as tremblings of the loudness, as if trying to squish the signal makes it more jittery. It can come off like an old Arp Pro Soloist trying to imitate a trombone, but the thing to bear in mind is that you can always back off the Compres control until it cleans up again. The transparency of BeziComp means it'll clean up a whole bunch while still being compressed.

This is my go-to for articulate guitars and basses that don't seem to have saturation or distortion. It's got the flexibility of PointyGuitar, but super clean, or with strange new forms of saturation that are like derezzing. Hope you like it!

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ChimeyGuitar processes audio in the Amp Sims category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Amp Sims](../categories/amp-sims.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ChimeyGuitar)

**Categories**: Amp Sims

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Amp Sims](../categories/amp-sims.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
