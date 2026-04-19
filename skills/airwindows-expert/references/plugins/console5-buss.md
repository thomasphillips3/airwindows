# Console5Buss

**Category:** Consoles
**Source:** `plugins/WinVST/Console5Buss/`
**Unique ID:** `conk`

## One-line sonic description

The "big, beefy, large-console" buss — `asin()` saturation with slew accumulation and DC servo; richer and warmer than Console8.

## What it does algorithmically

Console5Buss decodes the `asin()`-encoded signal from Console5Channel. The algorithm:

1. Smoothed gain (`gainchase`) with a variable chase speed that ramps from 350 to 2500 samples — fast enough to track automation, slow enough to avoid zipper noise
2. Input hard-clipped to ±1.0, then passed through `asin()` saturation
3. Slew calculation: difference between current sample and `lastFXBuss` (previous output); difference clamped to ±π/2, then `sin()` applied and accumulated into a feedback buffer — enhancement via `asin()`, reduction via `sin()` (Chris's complementary pair)
4. DC servo: `iirCorrect` accumulates DC offset and applies a very fine proportional trim (`0.0000001 / overallscale`) scaled toward zero — prevents low-frequency buildup across long sessions
5. Floating-point output dither

The slew accumulation is what creates the "rich, warm" character — it gently rounds transient edges and adds a subtle low-mid density that Console8 doesn't have.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Input | Input level into the saturation stage; 0.5 = moderate drive |

## Typical use cases

- Paired with Console5Channel on every track for full-mix console processing
- Bus groups where warm analog density is desired
- Mix bus "glue" without a compressor

## Sonic vocabulary tags

warm, glue, rich, big, console, analog, beefy

## Port notes

- `gainchase`, `chasespeed`, `settingchase` — all smoothing state; declare as `double` members
- `lastSampleBussL/R`, `lastFXBussL/R` — one-sample delay state; declare as `double` members
- `iirCorrectL/R` — DC servo accumulator; declare as `double` members; initialize to 0.0
- No latency introduced
- DC servo operates at `0.0000001 / overallscale` — don't omit it; it prevents issues on very long sessions
