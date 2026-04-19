# SmoothEQ3

**Category:** Filter
**Source:** `plugins/WinVST/SmoothEQ3/`
**Unique ID:** `sme3`

## One-line sonic description

3rd-order Butterworth crossover EQ — three bands via cascaded biquad + IIR smoothing; "most approachable EQ" with low artifact and musical shelving behavior.

## What it does algorithmically

Citation: "SmoothEQ3 is how to get 3rd order steepness at very low CPU…you can't vary Q because math is simplified to take advantage of how the accurate Q value for this filter is always exactly 1.0."

Two biquad crossover filters split the signal into three bands:
- Low biquad: fixed at 200 Hz (bass/mid split)
- High biquad: fixed at 4000 Hz (mid/treble split)

Q=1.0 for both, which simplifies the bilinear transform math and is computed at exactly the right slope for the three-band split. After the biquad crossover, each band passes through exponential IIR smoothing (steepening the rolloff further, effectively achieving 3rd-order behavior without explicit 3rd-order filter math).

The three bands are then scaled by their respective gain parameters (High, Mid, Bass) and summed.

This technique (SmoothEQ's "reconstruct from crossover" approach) was originally developed for AngleEQ to handle weird phase behavior — applied to clean biquads it adds a sonic character people noticed and described as "smooth."

8 SR references indicate this is highly sample-rate-adaptive — crossover frequencies are computed in Hz terms that stay constant across sample rates.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | High | Treble shelf level |
| B | Mid | Mid band level |
| C | Bass | Bass shelf level |

## Typical use cases

- Mix bus EQ when you want "always sounds good" shelving
- Tracking EQ for quick tone shaping without surgical precision
- When you want to reach for an EQ and not think too hard about phase artifacts
- The EQ section of ConsoleH extracted as a standalone tool

## Sonic vocabulary tags

smooth, musical, clean, shelving EQ, approachable, low-artifact

## Port notes

- 6 `double` state variables: biquad sL1/sL2 for both crossovers + IIR smoothing states (L and R each)
- Fixed crossover frequencies (200 Hz / 4000 Hz) — precompute all biquad coefficients in `prepareToPlay`
- `overallscale` scales the IIR smoothing; 8 sample-rate references means timing/smoothing is carefully adapted
- The Q=1.0 simplification means coefficient calculation is lighter than a fully parameterized EQ
- Read Proc.cpp for exact Butterworth coefficient derivation
