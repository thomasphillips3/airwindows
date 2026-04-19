# Pressure6

**Category:** Dynamics
**Source:** `plugins/WinVST/Pressure6/`
**Unique ID:** `prs6`

## One-line sonic description

Refactored vari-mu-style compression with organic movement and `sin()` saturation at the wet threshold — simple algorithm, huge range of character.

## What it does algorithmically

Citation: "Pressure6 is the result of refactoring the Pressure compression algorithm as it's never been refactored before…It also has an entirely new sound, from having isolated some of the strangest and trickiest qualities of the original Pressure. My target was '2-buss compressor feel'."

The core: `muComp` is a gain reduction coefficient that tracks signal level. When the maximum of L/R absolute values exceeds threshold, `muComp` is multiplied down; when below, it recovers toward 1.0. The envelope speed `muSpd` is bounded and updated with quadratic damping (`muSpd * (muSpd - 1.0)`), creating an envelope that responds nonlinearly — fast on transients, slower to release.

At the wet/dry boundary, a `sin()` saturation stage is applied: this introduces musical saturation rather than hard clipping at the gain reduction boundary, and is why compressed Pressure6 sounds "organic" rather than artificial.

Only 2 double state variables — one of the most efficient compressors in the library despite its character.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Compres | Compression depth |
| B | Ratio | Attack/release speed (ratio, not attack/release separately) |

## Typical use cases

- Mix bus "2-buss feel" compression
- Organic gain riding on vocals or room mics
- When Pressure4/5 doesn't move right — Pressure6 was specifically designed to fix that
- Paired with ButterComp2 for a two-stage dynamics chain

## Sonic vocabulary tags

organic, glue, vari-mu, 2-buss, smooth, musical, vintage compression

## Port notes

- Only 2 `double` state variables (`muComp`, `muSpd`) — trivially lightweight to port
- Quadratic envelope damping: `muSpd = muSpd * (muSpd - 1.0)` in the update step — preserve this exactly
- `sin()` saturation at wet threshold: don't replace with a simpler curve; this is the character
- Read Proc.cpp for the soft-knee and quadratic damping equations
