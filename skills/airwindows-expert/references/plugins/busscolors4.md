# BussColors4

**Category:** Tone Color
**Source:** `plugins/WinVST/BussColors4/`
**Unique ID:** `bsc4`

## One-line sonic description

Convolution-based bus coloration using hardware-measured impulse kernels — transformer, transistor, and tube character in one plugin.

## What it does algorithmically

Citation: "The most successful [tone] plugin I've ever had…based on a convolution model [from] hardware convolution kernels done at all different levels."

BussColors4 uses short convolution kernels captured from real hardware (NoiseVault's sets) applied at multiple drive levels. The Color parameter selects between different hardware characters — transformer, transistor, tube, and variations. Input Trim sets gain before convolution; Output Trim sets gain after; Dry/Wet blends processed and dry signals.

At 1726 lines (`total_lines`), this is one of the more complex plugins in the library. The convolution kernel runs per-sample (short FIR, not block-based), which is why the line count is high despite only 4 parameters.

Inference: The hardware-capture approach means the coloration is strictly based on real-world measurements, not modeled equations. At low Dry/Wet, it adds subtle transformer sheen; pushed hard, it saturates in a hardware-specific way.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Color | Selects hardware character (transformer/transistor/tube variants) |
| B | Input Trim | Drive into the convolution kernel; more drive = more color |
| C | Output Trim | Output level compensation |
| D | Dry/Wet | Blend of processed and dry signal |

## Typical use cases

- Bus character on mix groups when you want specific hardware-measured tone
- Subtle "this sounds like it went through gear" quality on the master bus
- Tracking into a specific analog-inspired color

## Sonic vocabulary tags

warm, transistor, tube, transformer, hardware, color, sheen

## Port notes

- 10 state variables (`state_var_doubles = 10`); convolution state must persist between blocks
- Read the Proc.cpp carefully — the convolution buffer management is non-trivial
- `overallscale` used for normalization; compute in `prepareToPlay`
- Input/Output Trim parameters use dB scaling — check Display methods for exact mapping
