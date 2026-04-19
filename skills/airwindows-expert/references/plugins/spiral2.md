# Spiral2

**Category:** Saturation
**Source:** `plugins/WinVST/Spiral2/`
**Unique ID:** `spis`

## One-line sonic description

The smoothest saturation algorithm in the library — `sin(x·|x|)/|x|` nonlinear curve with a one-sample-delayed presence branch that lets onset transients through.

## What it does algorithmically

Citation: "it occurred to me, if I was blending between dry signal and the sin() function saturated signal using the signal itself as the blend factor, I was just using a sample. Well, I also knew how to store a sample, and then the next time it'd be 'lastSample'. And what would happen if I blended between dry and the saturated one… using the Previous sample?"

The core saturation: `sin(x * fabs(x)) / fabs(x)` — amplitude-dependent nonlinear scaling. At low amplitudes the curve is nearly linear; at higher amplitudes it compresses progressively.

Two branches run in parallel:
- **Main:** `sin(currentSample * fabs(currentSample)) / fabs(currentSample)`
- **Presence:** `sin(currentSample * fabs(prevSample)) / fabs(prevSample)` — using the previous sample's amplitude as the scaling factor

Using the previous-sample amplitude on the presence branch means that sudden transients (appearing out of silence) get scaled less aggressively — the one-sample-delayed amplitude hasn't caught up yet. This is what Chris discovered: transients pass through with more integrity than smooth sustained signals.

Two complementary IIR highpass filters (alternating A/B each sample via `flip`) remove DC. Presence parameter blends between main and presence branches.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Input | Drive level (quadratic scaling: `pow(A*2, 2)`) |
| B | Highpass | Pre-saturation highpass cutoff (IIR, cubic scaling) |
| C | Presence | Blend between presence branch and main branch |
| D | Output | Output level |
| E | Dry/Wet | Blend |

## Typical use cases

- Smoothest saturation on any source — fewer audible artifacts than `sin()` or `asin()` alone
- Vocal saturation where transient integrity matters
- Bus saturation as an alternative to console processing
- Setting Presence at midpoint gives a hybrid transient-aware character

## Sonic vocabulary tags

smooth, silky, saturation, transient-aware, clean drive, presence

## Port notes

- 6 `double` state variables: `iirSampleAL/R`, `iirSampleBL/R`, `prevSampleL/R`
- `flip` boolean — alternates IIR filter A/B each sample; declare as `bool` member
- `prevSampleL/R` — stores dry input before processing; update AFTER the DSP, not before
- Highpass IIR amount: `pow(B, 3.0) / overallscale` — sample-rate-dependent, compute in `prepareToPlay` or per block if B changes
- Input gain: `pow(A * 2.0, 2.0)` — quadratic; large values push hard into saturation quickly
