# VariMu

**Category:** Dynamics
**Source:** `plugins/WinVST/VariMu/`
**Unique ID:** `vari`

## One-line sonic description

Dual-speed envelope follower compression with a vintage variable-mu character — slower and more organic than Pressure6, louder and more colored than ButterComp2.

## What it does algorithmically

Citation: "VariMu comes from Pressure4…[it adds] a more organic variation."

The algorithm uses two independent compression coefficient pairs (`muCoefficientA/B`) alternating via a `flip` toggle each sample — similar to ButterComp2's bipolar approach but applied to a vari-mu topology instead of bipolar waveform halves.

Threshold comparison uses squared signal amplitude (`muVaryL = threshold / squaredAmplitude`). Attack path: `muAttackL = sqrt(fabs(muSpeedAL))` — a square-root attack curve that's faster at low levels and slower at high levels, producing the characteristic "grab then ease" of vintage variable-mu hardware. Release: quadratic smoothing toward 1.0.

16 double state variables — meaningful filter/envelope state, with humorous denormal injection (modulo operations generating a cascade of microscopically tiny values to keep the compressor's internal state away from flush-to-zero).

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Intensity | Compression depth |
| B | Speed | Envelope follower speed (slower = more vintage character) |
| C | Output | Makeup gain |
| D | Dry/Wet | Blend |

## Typical use cases

- Mix bus vintage compression character (slower, more colored than Pressure6)
- Mastering bus where vari-mu character is wanted
- Drum bus for a "squished vintage" effect with Speed at slow settings
- When ButterComp2's bipolar character isn't the right texture

## Sonic vocabulary tags

vintage, vari-mu, organic, slow compression, warm, character, bus compressor

## Port notes

- 16 `double` state variables: dual A/B coefficient sets, speed variables, envelope states (L and R each)
- `flip` boolean — alternates A/B coefficients each sample; declare as `bool` member
- Square-root attack: `muAttackL = sqrt(fabs(muSpeedAL))` — preserve this; it's the character
- Denormal injection modulo cascade — preserve the stack of tiny arithmetic; it prevents CPU stalls in the envelope follower at near-silence
- Read Proc.cpp directly for the envelope update equations
