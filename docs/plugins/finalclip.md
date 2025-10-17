# FinalClip

![Latest](https://img.shields.io/badge/-Latest-10b981)

## Quick Info

| | |
|---|---|
| **Category** | Clipping |
| **Type** | Clipping |
| **Status** | Latest Release |

## Description

one stage of ADClip8 set up to clip +6dB for Final Cut Pro

## Detailed Overview

If you like ADClip8, this came first and is basically the seed of ADClip8.

FinalClip is a few variations on ClipOnly2, with a bit of slew clipping thrown in, and adjusted to work specifically for Final Cut Pro, the video software I use. This is because if I put any normal clipper such as you'd use in a DAW into Final Cut, it applies the clip to the cut at 6dB down. I can only assume this has to do with how it gain stages stuff for video. There's a way to gather clips into some sort of large composite clip and apply a 'master buss' plugin to the sum, and if you thought Airwindows Console in DAWs was awkward to set up, yikes! I'm not even trying to do that. I just run camera audio directly to the output of Final Cut and use that.

Because the clip point is 6 dB down, it seemed like I could build a special clipper just for Final Cut, that would always apply what I needed. I could control loud voice outbursts, soften the entry to/exit from clipped parts in the way ClipOnly2 does, and I could even throw in a very subtle slew-clip to just faintly soften treble information, so my sibilance off my Roswell Colares would never be annoying (it's pretty good already, the mic tries to imitate an ELA M 251)

Not only did this work, it turned out that allowing multiple stages of exactly this gave me ADClip8! So everybody wins.

And of course I'm immediately letting people have the tool I made for me. If you experience normal clippers such as ClipOnly taking effect 6dB down, this is the one to use. Or, if for instance you're hammering a peak limiter on your mix buss at way over +6dB to the buss, then you can try this to precondition what the limiter sees, and you might get a pleasing result.

But really, this just exists as a tool for me, or anyone who's using Final Cut and would like to drag a simple Airwindows clipper onto a (video) clip in the timeline, and have it make peaks more elegant, with no red clip lights happening and no abrasive highs when things get loud. Using this, I don't have to be that careful of my dynamic levels recording. If I suddenly yelp or talk loudly, clipping the camera's recording, this plugin will straighten it out and smooth off the corners just a bit so the loud bit isn't too objectionable.

Since there's next to nothing to say about this plugin, nothing to do (no controls) and nothing to show (in a DAW, the interface is a blank rectangle or an empty line), the video's full of everything else I do to get the audio for my plugin-posting videos. If you'd like to see my setup, have at it. Otherwise, totally ignore it and just use the plugin :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

FinalClip controls peaks and maximizes loudness through peak limiting. Use it as a mastering tool or creative effect.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Clipping](../categories/clipping.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/FinalClip)

**Categories**: Clipping

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Clipping](../categories/clipping.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
