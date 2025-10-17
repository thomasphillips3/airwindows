# BitGlitter

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Lo-Fi |
| **Type** | Lo-Fi |
| **Status** | Latest Release |

## Description

an old-sampler style digital lo-fi plugin

## Detailed Overview

DeRez is the simpler, purer bit and frequency crusher, and is still the best ‘analog setting’ bitcrusher (because it lets you use floating-point or fractional frequency and bit crushes). It’s a very pure example of those things and you can make it gate with a touch of DC offset from DC Voltage, and it’s even got a touch of grit softening when it frequency crushes to improve its tone.

BitGlitter, however, isn’t DeRez. BitGlitter’s something a lot more sophisticated: a kind of sampler emulator. At every stage it’s designed not for bitcrush alone, but to get the particular tonalities you can get out of primitive old samplers. An earlier attempt intentionally went after the old Akai sound, but currently BitGlitter has no specific model. It’s just there to dial in a kind of punchy grit that will make beats sit well against other elements: the video demonstates this.

Now, I know there are people who get mad when I make plugins like these. They say, ‘stop making the sound worse!’ and I understand what they mean, but sorry, I won’t stop because I know there are elements to certain ‘bad’ sounds that aren’t just ‘bad’ but usefully different. BitGlitter maximizes this as much as I can, and might be the go-to textural element for this sort of thing if generic bitcrushing etc. just never works for you. And then for some people I think it’ll immediately be their best friend, but I don’t need to explain to that crew what this is. For those who aren’t used to ‘crappy old sampler’ magic…

First, BitGlitter’s got gain trim going into a stage of Spiral analog-style saturation. You can overdrive the input effectively. Then, it does a hint of bitcrushing and splits into two separate frequency crushers, each set slightly different. This isn’t ‘accurate’ to any real retro sampler, but it helps broaden the sound. The output of these are blended and given an output gain and a dry/wet in case you need to sneak a little clarity back in there, and a slight averaging blur is added to the blend to further emulate analog circuitry.

The result is a coarser, more opaque sound which still lacks modern digital ‘edge’: you can plainly see on a metering plugin like Voxengo SPAN how the highs are softened. It’s not a digital bright-maker, it’s a texture-changer and impact-maker. Especially if you go for darker regions of the Bit Glitter control, you can use this to add ridiculous amounts of midrange punch in that ‘retro hip-hop’ kind of way. There’s a visceralness and aliveness to the grunge because it’s made by an algorithm to act like analog gear might: you won’t get the same result out of just a pile of typical DAW bitcrush and EQ. BitGlitter will do the extreme damage you might be looking for, but it’ll do it with a personality that contributes instead of detracts.

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

BitGlitter processes audio in the Lo-Fi category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Lo-Fi](../categories/lo-fi.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/BitGlitter)

**Categories**: Lo-Fi

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Lo-Fi](../categories/lo-fi.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
