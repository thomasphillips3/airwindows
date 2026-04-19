# BezEQ2

**Category:** Filter
**Source:** `plugins/WinVST/BezEQ2/`
**Unique ID:** `bzer`

## One-line sonic description

Three-band EQ via Bezier-delayed crossover — hides what it's doing; boosting highs and bass simultaneously sounds like no change was made; introduces slight latency.

## What it does algorithmically

Citation: "Far from the first BezEQ, this BezEQ2 has a special knack for hiding what it's doing. It can boost highs, boost bass, and the result is weirdly like no change was made. There's a quirk where if you cut the middle all the way to zero, the highs will also cut out (a side-effect of how the delays are set up)."

Like SmoothEQ, BezEQ2 uses a "sum to unity" crossover approach — the three bands add up to perfect fidelity at flat settings. Unlike SmoothEQ, BezEQ2 applies inter-band delays to cancel bass frequencies more accurately, creating different phase relationships. These delays are what cause the slight latency the plugin incurs.

The `x` parameters (B and D) are internal crossover position controls — they're exposed as parameters but their function is as crossover-band boundary adjustment, not gain. When the mid band is cut to zero (C all the way down), the delay structure causes high-band cancellation as a side effect.

6 double state variables — lighter than SmoothEQ3 despite the more complex crossover.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Treble | High band level |
| B | x | High/mid crossover position |
| C | Mid | Mid band level |
| D | x | Mid/bass crossover position |
| E | Bass | Bass band level |

## Typical use cases

- Subtle full-spectrum shaping where you want the EQ to be "transparent" — not obviously tipping tonal balance
- Mastering EQ for music that responds poorly to conventional shelving
- Experimentation: unusual phase relationships create a distinctive texture at extreme settings

## Sonic vocabulary tags

transparent, subtle, invisible EQ, unusual, phasey at extremes, mastering

## Port notes

- Introduces latency (band delay structure) — report via `getLatencySamples()` and compute the sample count from `overallscale`
- The crossover `x` parameters affect delay lengths — changes require state reset (or careful interpolation)
- 6 `double` state variables; all filter/delay state
- Not in `plugins.json` — read Proc.cpp for exact delay lengths and crossover math
- The "cutting mid to zero cancels highs" behavior is a known side-effect of the delay structure; preserve it, don't try to fix it
