# Dark

**Category:** Dithers
**Source:** `plugins/WinVST/Dark/`
**Unique ID:** `dark`

## One-line sonic description

Benford Realness analysis dither — "gives your music a blacker backdrop"; the current Airwindows community standard for mastering dither.

## What it does algorithmically

Citation: "Much like Not Just Another Dither (NJAD, my previous best) it analyzes the results of the audio, depending on whether the dither rounds up or down. With correct TPDF dither, it's a factor of randomness, a noise that breaks up patterns in the output. With NJAD, it runs a Benford Realness calculation and uses that."

Benford's Law states that in natural data, leading digits follow a specific distribution. Dark uses this principle to bias the dither rounding decision: instead of randomly choosing to round up or down (TPDF), Dark analyzes what the current sample's output "should" look like according to Benford probability — and chooses the rounding direction that makes the digital output more "natural-looking" at the bit level.

The perceptual result: the noise floor has a different texture than TPDF dither. Users consistently describe a "blacker backdrop" — quieter sounding silences, better depth, and more three-dimensionality in the spatial presentation of the mix.

0 double state variables (no persistent signal state, just PRNG). Very lightweight.

`Quant` / `DeRez` same as PaulDither.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Quant | Bit depth (16-bit or 24-bit) |
| B | DeRez | Additional resolution reduction |

## Typical use cases

- Final output dither on all masters — current recommended choice over NJAD, TPDF, and PaulDither
- When spatial depth and "blackness" of the noise floor matters
- HD mode: citation says it's "barely audible on its HD setting" — use freely

## Sonic vocabulary tags

black, dark backdrop, quiet, depth, mastering, reference dither, three-dimensional

## Port notes

- 0 double state variables — the Benford analysis is entirely within the per-sample computation, no memory
- The rounding decision logic is the whole algorithm — read Proc.cpp carefully for exact Benford calculation
- Apply last in the signal chain, same as all dither plugins
- In JUCE float-to-float: omit unless final export is to lower bit depth
