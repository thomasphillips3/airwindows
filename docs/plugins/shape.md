# Shape

![Latest](https://img.shields.io/badge/-Latest-10b981) ![Recommended](https://img.shields.io/badge/-Recommended-6366f1)

## Quick Info

| | |
|---|---|
| **Category** | Subtlety |
| **Type** | Subtlety |
| **Status** | Latest Release |

## Description

an asymmetrical waveshaper for peak manipulating

## Detailed Overview

Here’s a really basic building block for ya. The key word here is asymmetrical.

Shape is a simple, often subtle, little plugin for either pulling out, or squishing in, parts of the waveform. It’s based on the same basic technology as Console: complementary sin() and asin() functions. But in Shape, you’re picking which you want to apply, and you’re offsetting things so you can hit one side of the waveform more than the other.

Works like this. The Shape control determines what you’re doing. In the middle (0.5) you’re not doing anything. Increase it to 1.0 and you are stretching out the peaks of the waveform. Turn it down to 0.0 and you’re squishing the peaks of the waveform: like a soft-saturation but no boost, just restricting the waveform and making it distorted. The control scales all this so if you’re not cranking it out, you have lots of headroom and very gentle effects.

The Offset control interacts with this by shifting things from one side to the other: 0.5 is no offset, 0.0 is negative and 1.0 is positive (in my sound editor in the video, this is the top half of the waveform as positive). The effect of this, especially if you’ve not cranked out the Shape control, is to make the Shape control do its thing to only one side of the wave. You shouldn’t automatically crank this one out either: you can, for nasty waveshaping tricks, but the power of Shape is in how transparently it can manage the positive and negative swings of your waveform.

Also, when we’re reshaping the waveform so asymmetrically, that’s built-in even harmonics: this is a recipe for warmth. It’s like a turbo version of my PurestWarm plugins but even smoother, or like a variation of my SingleEndedTriode plugin. Use it gracefully (not cranking out the controls all the way) and everything you do will be tonal adjustments of great purity and subtlety, which is why it can be a bit hard to hear its effect when the controls are very near the middle.

So the trick is to know what way you’re using it. If you’re doing sound design and you’re trying to get a sound to swing fully in both directions, you can either pick the part that you think is swinging too far (pos or neg), set the offset to favor that, and pull back that side by setting Shape lower than halfway (cutting BACK the side you’re focussing on), or you can pick the side that doesn’t go far enough, set the offset to favor it, and turn Shape UP to bring that side’s peaks up to match the other side.

Or if you’re working on a bass and want it to be warmer, you can just choose between more Shape (more of a triangle-ey result out of a sine input) or less Shape (more of a squared result out of a sine input) and then lean the Offset one way or the other to get the warmth you want (not all the way, or it won’t be as smooth).

Or, you can take your bass that you want to be purer, and try to identify whether it’s too triangle-ey or too square-ey, and then apply Shape to nudge it more in the direction of a pure sine-ey tone. It’s a waveshaper, so you can stack them up to get a VERY soft square or a soft-pointed triangle out of any sine-bass you start with, or put ’em back to the sine shape, or lean the offset one way or another, all very transparently.

I don’t know how clear all this is, because you probably don’t have this function laid out in this way, and it’s too subtle for normal plugin makers to be able to sell you. Any commercial plugin where turning it up doesn’t equal ‘more’ plus you can’t always hear what it does, is in big trouble. But I’m Patreon-supported so I don’t have to follow those rules, so I can give you Shape even if most people don’t get a big charge out of it and throw their money :)

And so I have. Enjoy Shape. My hope is that it serves its useful purpose for those who need to tweak exactly this, as transparently as possible. And if you didn’t need to… maybe you just didn’t know it was a thing. It is now! :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

Shape processes audio in the Subtlety category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Subtlety](../categories/subtlety.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/Shape)

**Categories**: Subtlety

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: Subtlety](../categories/subtlety.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
