# DeRez3

**Category:** Lo-Fi
**Source:** `plugins/WinVST/DeRez3/`
**Unique ID:** `drzz`

## One-line sonic description

Bitcrusher with Bezier cubic interpolation — quantizes to reduced bit depth, then smoothly interpolates between quantized steps; "reinvents retro digital tones."

## What it does algorithmically

Citation: "When I undersample a reverb, I'm taking a sample only every two or four samples. But you can use interpolation so you're getting as smooth a waveform as you'd expect. What if I took a known bit depth — say 8-bit — and applied the same cubic interpolation?"

The algorithm:
1. **Bitcrushing:** multiply by `bitFactor = 2^bit`, floor to integer, divide back — creates hard quantization steps
2. **Bezier interpolation:** maintains a circular buffer of three consecutive quantized samples (`bez_AL/BL/CL`). A phase accumulator (`bez_cycle`) increments by the resampling ratio `rez` each sample. When the accumulator completes a cycle, the next quantized sample is captured. Between cycles, Bezier cubic interpolation blends between the stored samples — creating smooth curves between the stair-stepped quantization boundaries

The result sounds unlike standard bitcrushing: the quantization artifacts are present but "softened" — you hear the lo-fi texture without the harsh aliasing of naive bitcrushing. At different Rate and Rez combinations, you get textures ranging from vintage sampler (e.g., S900, SP-1200) to extreme digital degradation.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Rate | Sample rate reduction (resampling ratio) |
| B | Rez | Bit depth reduction |
| C | Dry/Wet | Blend |

## Typical use cases

- Lo-fi hip hop drum processing
- Vintage sampler emulation (S900, SP-1200, MPC character)
- Creative degradation on synths or pads
- Resampling artifacts on anything for texture

## Sonic vocabulary tags

lo-fi, vintage, sampler, bitcrushed, degraded, retro digital, texture, gritty

## Port notes

- 7 `double` state variables: 3 bez circular buffer values per channel + cycle accumulator + current sample accumulators
- `bez_cycle` accumulator: increments by `rez` each sample, wraps at 1.0 — when it wraps, advance the circular buffer
- Bezier cubic blend uses the stored A/B/C samples and `bez_cycle` as the interpolation position
- `Rate` and `Rez` are linearly interpolated across the block (rezA/rezB, bitA/bitB) — smooth automation
- Read Proc.cpp for exact Bezier weights and cycle management
