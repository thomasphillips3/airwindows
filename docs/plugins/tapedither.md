# TapeDither



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

TPDF dither with noise like reel-to-reel tape

## Detailed Overview

I thought I had it all worked out. Put out a proper, well-coded TPDF dither, the highpassed variation on it I’ve called PaulDither, and move on to the fancy boutique stuff.

But there was this one experiment I had in mind. If you could do the highpass by delaying and then subtracting the random noise (and it gained you a bit of efficiency in the bargain), why not delay it more? It’d create comb filtering, a cancellation node. Why not keep delaying until the cancellation node dropped right down to around 1.5K?

Surely this would give me a nice cancellation notch right where the ear is most sensitive, and heightened clarity. What could go wrong?

Nope! I made a prototype, called it ‘NodeDither’, began experimenting, and immediately found that I’d made… a flanger! The long delay settings were useless. It made obvious overtones just out of the dither noise, a blatant tone color cast that wouldn’t produce the desired effect. It didn’t even produce an obvious notch in the response where I wanted it. The only thing it did do, was continue to function as a working TPDF dither no matter what the setting was (more on this later).

But, something else turned up in the experiments, and that’s what brought you TapeDither.

If you use one sample of delay and inverting the noise, you get PaulDither: simple one-pole highpass. If you use two samples of delay, you get another sort of texture: kind of silky, but still digitally bright and intrusive. Using lots of delay, such as ten samples, starts to sound like the flanger, undesirable.

But, there’s something interesting about powers-of-two delay times. One, two, four, eight and so on, these delay times are slightly less ‘colored’ in tone than the others. I think it has to do with interactions with the sample rate: they seem to line up more neatly, making it slightly more easy not to hear the pitch of the ‘flangey’ quality.

And four samples of delay (and then inverting the noise) produces something rather special: a noise profile that closely resembles what you hear off reel-to-reel tape.

I can’t specify particular brands because (a) I hate when people do that to brand names not their own and (b) it’s a technical discovery, not some complicated way of forcing digital audio to mimic a particular brand. It’s no specific tape stock or tape machine. But what it is, is a voicing for TPDF dither that rolls off in an obvious way, around where tape noise rolls off. There’s another little bump past that, which many people won’t be able to hear, and then it begins to roll off again as it reaches the Nyquist frequency beyond where digital audio can’t go. Compare that to any normal flat, TPDF, or highpassed dither. Those keep putting out noise energy right up to the frequency limit.

TapeDither is every bit a TPDF dither, technically correct and flawless as far as dither goes. But it also is a highpassed dither with a softer tonal voicing that resembles good tape machines, and that doesn’t affect the dither performance at all. It doesn’t attenuate the audio content at all. Only the background dither noise is turned into what you’d get off a tape deck, all while the audio is protected from truncation and digital artifacts.

I would use this anywhere I was sending processed stems or tracks outboard to a multichannel DAC, for mixing in the analog domain or summing with an outboard summing box. Without hesitation. I’d use fancier boutique dithers on the 2-buss, though this will work there too… but if I was doing an analog mix from a multichannel converter, there is nothing I’d rather use than TapeDither. (maybe Naturalize. Maybe.)

That’s because it’s one thing to apply an interesting dither (like Spatialize, for instance, or some noise shaper) on the 2-buss and get a unique texture or presentation on the audio. But if you’re stacking up lots of tracks and all of them get the same treatment, it’s vital to use something that won’t develop an exaggerated tone signature when multiplied that way. For dither, TPDF gives you that behavior, and TapeDither is the TPDF that most closely mimics the reality of analog mixing back in the days of big reel-to-reel machines. The tone of its noise floor is already more pillowy, mellow and relaxing than most TPDF or highpassed TPDF, and then when you stack up lots of tracks of it, the texture’s better still.

I’m still excited to bring out Naturalize, but I’m just as excited about what TapeDither means. It makes me want to build analog consoles and mix into them, just so I can put TapeDither on any output that’s not playing raw 24 bit data exactly as captured. Anything with processing or gain on it would get a dithered output, and it would be a matter of—faders up—hello, Seventies :)

Well, I like audio from the Seventies. I suppose I’d better work out how to do some of the sonic quirks of Doubly while I’m at it! Not that a rock band would use Doubly…

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

TapeDither processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/TapeDither)

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
