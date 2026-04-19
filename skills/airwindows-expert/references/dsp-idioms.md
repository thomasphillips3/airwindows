# Airwindows DSP Idioms

Six recurring patterns across all 506 plugins. Understanding these is prerequisite
to reading any Airwindows Proc.cpp or porting code into JUCE.

---

## 1. fpdL / fpdR — Denormal prevention via Xorshift PRNG

**Every plugin uses this.** Floating-point processors stall on subnormal numbers
(absolute value below ~1.18e-38). Airwindows injects microscopically small noise
to keep silent audio above the flush-to-zero threshold.

```cpp
// In constructor — seed the PRNG:
fpdL = 1.0; while (fpdL < 16386) fpdL = rand() * UINT32_MAX;
fpdR = 1.0; while (fpdR < 16386) fpdR = rand() * UINT32_MAX;

// In processDoubleReplacing, at input:
if (fabs(inputSampleL) < 1.18e-23) inputSampleL = fpdL * 1.18e-17;
if (fabs(inputSampleR) < 1.18e-23) inputSampleR = fpdR * 1.18e-17;

// Update PRNG every sample (Xorshift-32):
fpdL ^= fpdL << 13; fpdL ^= fpdL >> 17; fpdL ^= fpdL << 5;
fpdR ^= fpdR << 13; fpdR ^= fpdR >> 17; fpdR ^= fpdR << 5;
```

**Why Xorshift-32:** Fast, no division, no trig. Passes enough randomness tests for
audio dither. The PRNG is also reused for the output dither (idiom 2).

**JUCE port note:** Declare `uint32_t fpdL, fpdR` as member variables. Initialize in
`prepareToPlay`. The per-sample PRNG update is part of the audio loop, not overhead
to be avoided.

---

## 2. Floating-point output dither

Applied after all processing, before writing to the output buffer. Scales noise to
the precision floor of the current sample value — preventing dithering artifacts even
at 32-bit float.

```cpp
// Scale noise floor to current sample's floating-point exponent:
int expon;
frexpf((float)inputSampleL, &expon);
fpdL ^= fpdL << 13; fpdL ^= fpdL >> 17; fpdL ^= fpdL << 5;
inputSampleL += ((double(fpdL) - uint32_t(0x7fffffff)) * 5.5e-36l * pow(2, expon + 62));
*out1 = inputSampleL;
```

Present in Console, EQ, and summing plugins. Not in all plugins — simple distortion
plugins may omit this. In `processDoubleReplacing` this is often omitted or simplified.

---

## 3. Sample-rate adaptation

Modern plugins scale all time-dependent values to maintain consistent sonic character
across sample rates.

```cpp
// At the top of processDoubleReplacing, before the sample loop:
double overallscale = 1.0;
overallscale /= 44100.0;
overallscale *= getSampleRate();

// Use it to scale filter coefficients, delay lengths, envelope times:
int spacing = floor(overallscale);          // for delay buffers (1 at 44.1k, ~2 at 88.2k)
double iirAmount = pow(B, 3.0) / overallscale;  // filter cutoff stays constant in Hz
```

Some plugins use a simpler boolean check:
```cpp
bool hsr = (getSampleRate() > 49000.0);    // engage anti-aliasing only at high SR
```

**JUCE port note:** Call `getSampleRate()` once in `prepareToPlay`, store it, and pass
to `processBlock`. Recomputing `overallscale` inside the sample loop is wasteful.

---

## 4. Biquad state-variable (canonical Airwindows form)

All biquad filters use the same enum-indexed double array, avoiding named struct members.
This makes copying, zeroing, and swapping filter state trivial.

```cpp
enum {
    biq_freq, biq_reso, biq_a0, biq_a1, biq_a2,
    biq_b1, biq_b2, biq_sL1, biq_sL2, biq_sR1, biq_sR2,
    biq_total
};
double biq[biq_total];   // zeroed in constructor

// Per-sample processing (left channel):
double outSample = (inputSampleL * biq[biq_a0]) + biq[biq_sL1];
biq[biq_sL1] = (inputSampleL * biq[biq_a1]) - (outSample * biq[biq_b1]) + biq[biq_sL2];
biq[biq_sL2] = (inputSampleL * biq[biq_a2]) - (outSample * biq[biq_b2]);
```

Coefficients computed once per buffer (in `processDoubleReplacing` preamble) via standard
bilinear transform with `tan()`. The same enum is reused for `fix[]`, `highFast[]`,
`hdbA[]`, etc. — always the same structure, just different variable names.

---

## 5. Interleaved console latency buffer

Used in all Console8/Output-stage plugins to handle sample-rate-dependent latency
without changing the summing topology. The buffer depth equals one 44.1 kHz sample
at any sample rate.

```cpp
// State in .h:
double lastSampleL, intermediateL[18];
bool wasPosClipL, wasNegClipL;

// In processDoubleReplacing (Console8BussOut):
spacing = floor(overallscale);
intermediateL[spacing] = inputSampleL;
for (int x = spacing; x > 0; x--) intermediateL[x-1] = intermediateL[x];
lastSampleL = intermediateL[0];
```

The `wasPosClipL / wasNegClipL` flags track which side of the waveform was last
clipped, enabling the ClipOnly2 interpolation that smoothly handles clip boundaries.

**Why 18 slots:** At 192 kHz, `overallscale ≈ 4.35`, so `spacing = 4`. 18 gives margin.

---

## 6. iir / control prefix state variables

IIR filter accumulators are named with an `iir` prefix; dynamics envelope states
use `control` or `mu`. These naming conventions appear identically across tape,
saturation, dynamics, and console plugins.

```cpp
// IIR one-pole lowpass (used for DC blocking, tone, sidechain):
iirSampleAL = (iirSampleAL * (1.0 - iirAmount)) + (inputSampleL * iirAmount);
double highpassL = inputSampleL - iirSampleAL;    // subtract to get highpass

// Dynamics envelope (ButterComp2 style):
if (inputSampleL > 0)
    targetposL = 1.0 - (fabs(inputSampleL) * compress);
// ... smooth toward target:
controlAposL = (controlAposL * (1.0 - speed)) + (targetposL * speed);
```

`flip` boolean (alternating each sample between A/B state sets) appears in ButterComp2,
Spiral2, VariMu, and others — it implements interleaved processing without a separate
loop.
