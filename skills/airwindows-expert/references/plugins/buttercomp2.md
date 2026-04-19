# ButterComp2

**Category:** Dynamics
**Source:** `plugins/WinVST/ButterComp2/`
**Unique ID:** `btcq`

## One-line sonic description

Bipolar interleaved compression — treats positive and negative waveform halves independently, with a subtle class A bias region that adds even-order harmonics under compression.

## What it does algorithmically

Citation: "Because of a thing C programming lets you do (assign, in an if statement) it turned out the original ButterComp didn't actually use the interleaved compressors after all…ButterComp2 is very much its own thing! It came up with a subtle tweak: it's a bipolar compressor, and when the two sides are compressing unevenly, you get some second harmonic."

Per sample:
- Two independent control signals (`controlApos`, `controlAneg`) track positive and negative waveform excursions separately
- When positive peaks exceed the threshold, `targetpos` reduces; negative does likewise independently
- Each control signal smooths toward its target at the `compress` rate
- `flip` alternates which control is applied to the current output sample
- When positive and negative compression are unequal, the residual asymmetry creates second harmonic content — this is the "class A bias" character

The result is a compressor that sounds musical even at high settings because the harmonic byproduct of compression masks the gain reduction artifacts.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Compress | Compression ratio/intensity |
| B | Output | Makeup gain (`B * 2.0` internally) |
| C | Dry/Wet | Blend |

## Typical use cases

- Bus compression where musical character is wanted alongside gain reduction
- Drum bus "glue" with added harmonic complexity
- Vocal bus to add density under compression
- Any situation where "the compressor sounds musical" is the goal

## Sonic vocabulary tags

glue, musical, warm, harmonic compression, bipolar, even-order, class A character

## Port notes

- 14 `double` state variables — 6 control signals (A/B pos/neg L/R) + 2 targets + `lastOutputL/R`
- `flip` boolean — alternates which control is applied; must be member
- No sample-rate dependencies in the core algorithm — `overallscale` minimal use
- `compress` maps from parameter A; check Proc.cpp for exact scaling
- Output parameter: `B * 2.0` — unity at 0.5, gain above 0.5
