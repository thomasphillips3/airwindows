# DitherFloat



## Quick Info

| | |
|---|---|
| **Category** | Dithers |
| **Type** | Dithers |
| **Status** | Stable |

## Description

a demo of floating point truncation: can also dither to 32 bit float output

## Detailed Overview

This AirwindowsPedia entry contains the most current public domain source code for adding floating point dithering to your own work, either to a float or double precision buss (which would mean you'd have to be using something longer like long double for your internal processing).

DitherFloat is NOT for putting in mixes to 'dither the plugins'. It is a demo, and the only use you could possibly do with it is to put it on a double precision buss and dither to save as 32 bit floating point instead of double. I don't think that's productive. Again, DitherFloat is NOT a plugin to use on things to make them more dithered. It's a proof of concept, like putting 'DeRez' onto dither plugins to hear how that works. You can literally hear the truncation in floating-point mantissas using this plugin, and what it sounds like when those are dithered. On to the original post when this came out…

This began as a challenge. A forum poster said you couldn’t dither floating point outputs, and posted a link to a study explaining why.

Floating point (including the kind that fits between every plugin in a mix on MacOS or 32-bit bussed VST) has fixed point math of the kind one needs to dither, in a part of the number called the mantissa. (64-bit VST has it too, just more finely grained.) It’s not all that hard to work out how to apply dither to this part. You scale it up or down according to the part of the number called the exponent.

The trouble is (a) it’s hard enough getting people to dither to 16-bit CDs, and (b) the argument is that the amplitude of the dither would fluctuate madly, making it unhelpful and incorrect. This is kind of like how flat dither isn’t correct: with only one noise source what happens is, the noise floor fluctuates according to the waveform causing a kind of distortion. If you have a low sine wave you’ll hear the ripple effect of flat dither, and the argument is that dithering floating point is like that only more so (and so, nobody ever tried).

DitherFloat demonstrates this, and it’s not true. You can TPDF dither (even PaulDither, like I’m using here) floating point. The noise doesn’t fluctuate according to the waveform represented in the mantissa. It fluctuates according to the value in the EXPONENT, because it has to, because the quantization noise also fluctuates wildly in volume. And if you get it right, you end up with no truncation distortion at all, just like using TPDF to fixed point.

The video explains more and shows it working. It’s practically impossible to hear ONE stage of 32 bit truncation (may be literally impossible, I think) but you can cheat and hear it as obviously as you like. You just add a huge offset to the number, convert it to float, and then subtract the offset again: and that’s what DitherFloat does. It’s a demo. It shows you there’s still truncation in floats, and it shows you the way TPDF dither completely removes the truncation distortion. It linearizes the signal so that no trace of the truncation is present (that’s how correct dither works).

You can’t add DitherFloat after existing plugins to fix them: even though you can use it (with zero offset) to export a 64 bit buss to 32 bit float and dither it, by itself DitherFloat can’t fix existing plugins. You would have to put the code for the dithering, into every single plugin that outputs 32 bit floats. Every MacOS plugin, every singlereplacing VST (every older VST implementation before they implemented 64 bit buss). For the Airwindows library that would involve personally revising every plugin I’ve released under the VST/Patreon years, many hundreds of plugins.

So I did. :D

(as of 2022, all the 32 bit buss plugins I make still dither to the 32 bit floats. In 2021, I experimented and decided to make my internal busses double precision instead of long double, as I wasn't able to find a difference and thought it would save some CPU; at that point, Airwindows plugins running on the VST double processing buss began outputting directly without a dither stage, for a slight efficiency boost. They still have the DitherFloat code in case the random number needs to get used, but the application of the dither is meaningless when the buss is already double, so that bit is commented out.)

Below is the actual code, licensed as public domain, for both the 32 bit and the original 64 bit floating point dithers.

		//This is free and unencumbered software released into the public domain.
		//this is in the header file, defining a continuing variable
		uint32_t fpd; //this is an unsigned int used for the random generator

		//this is in reset, where we start off the variable as a default starting number
		fpd = 1.0; while (fpd < 16386) fpd = rand()*UINT32_MAX;
		
		//the random generator is xorshift32 which can't start off with zero.
		//if the reset is randomized, all the dithers are different randoms
		//then in the actual processing code:
		
		int expon; frexpf((float)inputSample, &expon);
		fpd ^= fpd << 13; fpd ^= fpd >> 17; fpd ^= fpd << 5;
		inputSample += ((double(fpd)-uint32_t(0x7fffffff)) * 5.5e-36l * pow(2,expon+62));

		//Anyone is free to copy, modify, publish, use, compile, sell, or
		//distribute this software, either in source code form or as a compiled
		//binary, for any purpose, commercial or non-commercial, and by any
		//means.
		//In jurisdictions that recognize copyright laws, the author or authors
		//of this software dedicate any and all copyright interest in the
		//software to the public domain. We make this dedication for the benefit
		//of the public at large and to the detriment of our heirs and
		//successors. We intend this dedication to be an overt act of
		//relinquishment in perpetuity of all present and future rights to this
		//software under copyright law.
		//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
		//EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
		//MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
		//IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
		//OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
		//ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
		//OTHER DEALINGS IN THE SOFTWARE.

64 bit version for hilarious overkill is almost identical but with small changes in frexp() and the constants. This is now a sort of mad community effort, so that becomes public domain too:


		//This is free and unencumbered software released into the public domain.
		//this is in the header file, defining a continuing variable
		uint32_t fpd; //this is an unsigned int used for the random generator

		//this is in reset, where we start off the variable as a default starting number
		fpd = 1.0; while (fpd < 16386) fpd = rand()*UINT32_MAX;
		
		//the random generator is xorshift32 which can't start off with zero.
		//if the reset is randomized, all the dithers are different randoms
		//then in the actual processing code:
		
		int expon; frexpf((double)inputSample, &expon);
		fpd ^= fpd << 13; fpd ^= fpd >> 17; fpd ^= fpd << 5;
		inputSample += ((double(fpd)-uint32_t(0x7fffffff)) * 1.1e-44l * pow(2,expon+62));

		//Anyone is free to copy, modify, publish, use, compile, sell, or
		//distribute this software, either in source code form or as a compiled
		//binary, for any purpose, commercial or non-commercial, and by any
		//means.
		//In jurisdictions that recognize copyright laws, the author or authors
		//of this software dedicate any and all copyright interest in the
		//software to the public domain. We make this dedication for the benefit
		//of the public at large and to the detriment of our heirs and
		//successors. We intend this dedication to be an overt act of
		//relinquishment in perpetuity of all present and future rights to this
		//software under copyright law.
		//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
		//EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
		//MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
		//IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
		//OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
		//ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
		//OTHER DEALINGS IN THE SOFTWARE.

It’s not complicated but it’s my own code and it’ll work: it’s even pretty easy to drop into other plugins. If anyone’s game to do that and shout out that they did, I’d love to hear about it.

If they don’t, they will just continue adding a little truncation with every single plugin, every single calculation, and now none of MY plugins do that :)

## Signal Flow

```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```

## How It Works

DitherFloat processes audio in the Dithers category. See the description above for specific functionality.

## Usage Tips

- Start with conservative settings
- A/B compare to hear the effect clearly
- Use in context with other processing
- Trust your ears over visual meters


## Related Plugins

Browse other [Dithers](../categories/dithers.md) plugins.


## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/DitherFloat)

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
