# Console8BussOut

**Category:** Consoles
**Source:** `plugins/WinVST/Console8BussOut/`
**Unique ID:** `c8bo`

## One-line sonic description

The cleanest, most modern buss output stage — `sin()` saturation + ClipOnly2 peak management + anti-aliasing at high sample rates.

## What it does algorithmically

Console8BussOut is the sum-side half of the Console8 system (pair with Console8BussIn or Console8Channel). Input gain is smoothed between automation frames, then scaled and soft-clipped at π/2, followed by `sin()` saturation that hard-clips at ±1.0.

At sample rates above 49 kHz, a fixed biquad anti-aliasing lowpass (24 kHz corner, Q=0.52) runs before the output stage.

The output stage is ClipOnly2: a soft-knee clipper that tracks positive/negative clip events across samples and interpolates smoothly between the clipped and unclipped value using golden-ratio-derived weights (`0.7058208 + 0.2609148·x` or `0.2491717 + 0.7390851·x`). A sample-rate-scaled ring buffer (`intermediateL[spacing]`) handles timing alignment.

This introduces latency equal to one 44.1 kHz sample at any sample rate.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Fader | Input/output gain; 0.5 = unity, above 0.5 drives into sin() saturation |

## Typical use cases

- Final buss output stage in a Console8 chain
- Soft peak management on a mix bus without a compressor
- Modern console character with anti-aliasing protection

## Sonic vocabulary tags

clean, punchy, controlled, modern, anti-aliased, console

## Port notes

- `spacing = floor(overallscale)` — allocate `intermediateL/R[18]` as member arrays
- `wasPosClipL / wasNegClipL` — clip state flags, declare as `bool` members
- `fix[]` biquad array (size `fix_total`) — declare as member, compute coefficients in `prepareToPlay`
- `hsr` boolean — set once in `prepareToPlay` from sample rate
- The ClipOnly2 interpolation spans multiple samples; the ring buffer MUST be member state
- Introduces 1 sample of latency at 44.1 kHz (more at higher SR) — report via `getLatencySamples()`
