# Density2

**Category:** Distortion
**Source:** `plugins/WinVST/Density2/`
**Unique ID:** `den2`

## One-line sonic description

An older unusual saturation algorithm preserved exactly — "density, weight, color" on a spectrum from subtle analog body to gritty saturation.

## What it does algorithmically

Citation: "I refactored it to retain EVERYTHING unintentional or unusual. I gave it modern Airwindows handling of denormalized numbers, and it dithers to floating point instead of using the noise shaping to floating point that I used back then. Everything else is just as it was: no 'fixing' or making it do what I 'meant to do'."

The original algorithm has quirks that Chris intentionally preserved without correction. The Density control sweeps across a range from subtle body (low values) to gritty saturation (high values). A two-pole IIR highpass (Highpass parameter) is applied before saturation to prevent DC buildup and control the low-frequency character. Output and Dry/Wet round out the control set.

At 18 double state variables, there's meaningful filter state — the highpass carries between samples and the saturation curve has history. The "unusual" algorithm is the saturation function itself, which differs from Chris's later smooth `sin()`/`asin()` curves.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Density | Saturation intensity; controls "density, weight, color" |
| B | Highpass | Pre-saturation IIR highpass cutoff |
| C | Output | Output gain |
| D | Dry/Wet | Blend |

## Typical use cases

- Adding density and weight to a mix bus or subgroup
- "Making things more" without a specific sonic target
- When you want an older, quirkier saturation character vs. Spiral2's smoothness
- Tracking saturation on guitars or drums for attitude

## Sonic vocabulary tags

gritty, dense, weighted, body, color, saturation, attitude, unusual

## Port notes

- 18 `double` state variables; some are saturation history, some highpass filter state
- The unusual algorithm is the value — don't "fix" it when porting
- Highpass IIR coefficients scale with `overallscale`; compute in `prepareToPlay`
- The original's noise-shaping-to-float is replaced with modern dither; keep the dither
