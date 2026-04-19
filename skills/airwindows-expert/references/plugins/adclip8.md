# ADClip8

**Category:** Clipping
**Source:** `plugins/WinVST/ADClip8/`
**Unique ID:** `adcs`

## One-line sonic description

Golden-ratio adaptive clipping limiter with slew stage — the first significant update to ADClip since 2017, incorporating the FCP golden ratio architecture.

## What it does algorithmically

Citation: "What would happen if the FCP version, which has a built-in slew clip and makes heavy use of Golden Ratios to arrive at its results, was adapted to a new ADClip? What if it was scaled to regular clipping levels?"

The "ADClip" family uses adaptive clipping — rather than a simple hard clip at ±1.0, the clipper analyzes the approaching waveform and interpolates a smooth clip boundary. ADClip8 adds:
- Golden ratio scaling for clip boundary interpolation (φ ≈ 1.618 and its reciprocal ≈ 0.618 used as interpolation weights)
- A slew clip stage before the main clipper (same as the Sinew plugin) that limits rate-of-change rather than amplitude — prevents the clipper from creating discontinuities that would cause aliasing
- Mode parameter selects between clipping behaviors (inferred from 3-mode structure)

4 double state variables — small; most of the algorithm is per-sample computation, not state.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Boost | Input gain before clipping (dB) |
| B | Ceiling | Output ceiling level |
| C | Mode | Clipping behavior mode |

## Typical use cases

- Mix bus peak limiting without compression — loud without pumping
- Safety limiting before delivery (Ceiling at -0.1 dBFS or similar)
- Competitive loudness on EDM, pop, or rock without traditional limiters
- Mode experimentation: different modes suit different material

## Sonic vocabulary tags

punchy, loud, clean, limiting, hard limit, competitive, brickwall

## Port notes

- 4 `double` state variables: slew state + clip boundary tracking
- Mode parameter requires conditional branching in the DSP — check Proc.cpp for Mode 0/1/2 paths
- Boost maps to dB gain — use `pow(10, Boost/20)` for conversion
- Ceiling maps to a linear amplitude ceiling for the output stage
- Slew clip runs before main clip — preserve this ordering when porting
