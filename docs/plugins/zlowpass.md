# ZLowpass



## Quick Info

| | |
|---|---|
| **Category** | XYZ Filters |
| **Type** | XYZ Filters |
| **Status** | Stable |

## Description

a lowpass made to sound and act like the Emu e6400 Ultra lowpass

## Detailed Overview

Onward! Today we have ZLowpass. I think this one might be the closest to the hardware yet! It works like my previous Z series filters, except it’s the lowpass this time.

You might notice my video looks a bit different: that’s because my Blackmagic ATEM Mini finally and permanently blew up. I’m pretty sure I know why: there were times I ran it for long periods, I’ve often run many inputs into it or had it working hard doing things like chromakeying/lumakeying stuff at higher resolution and downscaling the result to HD, or running my laptop’s HDMI feed into it and having it upscale THAT to the higher native resolution, overlay the main camera and then downscale again to HD. On top of that, I’ve had it sitting on top of my Lavry DAC, and we’ve had some heat waves this summer.

So, it melted. For a while it just had its input to the computer die (I found a Razer capture card to be more reliable) and then in some livestreams it’s been flaking out, and tonight it blew up for good and couldn’t even run a single camera. Anyone out there, be careful with these things. They’re just $300 or so, but you cannot push them too hard in warm conditions or they will melt. Or maybe the fan blew up. I know I can’t return it under warranty because, being me, I took it apart to see if I could make the cooling work better. Too little too late. Be warned and don’t run these little buggers hard, or do lots of up and downscaling, while sitting them on a warm thing. No more ATEM Mini.

Until I get another, that is, and this time will NOT touch a thing about it, will fill in any warranty card it has, and will probably get a little laptop cooler pad or something. Whatever it takes, because my setup ended up pretty sweet if it wasn’t for the thing melting under the strain. (Replacement of the ATEM will NOT be out of what I’m saving up for getting a bigger and more classic sampler. Never fear, that journey will progress unhindered.)

Anyway, here’s ZLowpass :D

(followup: I did in fact replace the ATEM Mini, put it on a heatsink with a blue heatsink pad between, and used it extensively, and the replacement didn't melt. I ended up putting it aside and shooting video directly on the camera, so I could use 4k resolutions. The replacement ATEM with the heatsink should still be good.)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

ZLowpass processes audio in the XYZ Filters category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [XYZ Filters](../categories/xyz-filters.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/ZLowpass)

**Categories**: XYZ Filters

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: XYZ Filters](../categories/xyz-filters.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
