# PaulDither

**Category:** Dithers
**Source:** `plugins/WinVST/PaulDither/`
**Unique ID:** `paul`

## One-line sonic description

Paul Kellett's triangular single-pole highpass TPDF dither — quieter and airier than flat TPDF, twice as CPU efficient; the mix engineer's standard dither.

## What it does algorithmically

Citation (Chris citing Paul Frindle / Sony Oxford): "The one we use most is triangular single pole high pass dither. It's not freq bent enough to sound odd, but is slightly less audible than flat dither. It can also be easily made by taking one sample of dither away from the previous one – this gives you the triangular PDF and the filtering in one go."

Implementation: rather than generating two independent random samples and subtracting (standard TPDF), Paul dither stores the previous dither sample and subtracts it from the current one. This is mathematically identical to TPDF but also applies a single-pole highpass to the noise spectrum (since differencing is a highpass operation in the Z domain).

Result: the dither noise is spectrally shaped toward higher frequencies where it's harder to hear. It's also half the random number generation of standard TPDF (one random per sample instead of two), making it twice as CPU efficient.

`Quant` selects bit depth (16-bit or 24-bit, with potential DeRez below). `DeRez` can intentionally reduce resolution further.

Only 2 state variables: `previousDitherL/R` (the prior sample's dither value).

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Quant | Bit depth selection (16-bit or 24-bit) |
| B | DeRez | Additional resolution reduction |

## Typical use cases

- Final output dither on all mixes and masters going to 16-bit or 24-bit delivery
- Default dither when you want low audibility without Dark's Benford analysis
- When CPU efficiency matters (half the PRNG calls vs. flat TPDF)

## Sonic vocabulary tags

clean, airy, quiet, transparent, highpassed noise, mastering, dither

## Port notes

- 2 `double` state variables: `previousDitherL`, `previousDitherR`
- The subtraction approach: `currentDither = randomSample; shaped = currentDither - previousDither; previousDither = currentDither;`
- Apply at the absolute end of the signal chain, after all processing
- In JUCE at 32-bit float: typically omit (no wordlength reduction happening); include only when exporting to 16-bit or 24-bit
- Read Proc.cpp for the exact subtraction dither implementation
