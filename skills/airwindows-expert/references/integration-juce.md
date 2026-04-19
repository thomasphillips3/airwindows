# Integrating Airwindows DSP into a JUCE AudioProcessor

Practical guide for lifting a plugin's DSP loop from `{Name}Proc.cpp` into a JUCE
`AudioProcessor`. Airwindows and JUCE have different architectures — understand the
mismatches before copying code.

---

## Architecture mismatch summary

| Airwindows | JUCE |
|-----------|------|
| `processDoubleReplacing(double**, double**, VstInt32)` | `processBlock(AudioBuffer<float>&, MidiBuffer&)` |
| Per-sample loop: `while (--sampleFrames >= 0)` | Block loop: `for (int i = 0; i < buffer.getNumSamples(); i++)` |
| Parameters as `float A, B, C` (0.0–1.0) | Parameters via `AudioProcessorValueTreeState` or `AudioParameterFloat` |
| No smoothing (parameter read once per block) | JUCE expects smooth automation — add smoothing |
| `getSampleRate()` from AudioEffectX | `getSampleRate()` from AudioProcessor |
| State initialized in constructor | State initialized in `prepareToPlay` |
| Output dither at end of per-sample loop | Optional — JUCE float buffers don't need 32-bit dither |

---

## State variables → member variables

Everything in the Airwindows `private:` section of `{Name}.h` becomes a member
of your `AudioProcessor` subclass.

```cpp
// From ButterComp2.h — copy these as-is:
double controlAposL, controlAnegL, controlBposL, controlBnegL;
double targetposL, targetnegL, lastOutputL;
double controlAposR, controlAnegR, controlBposR, controlBnegR;
double targetposR, targetnegR, lastOutputR;
bool flip;
uint32_t fpdL, fpdR;
```

Do NOT declare them as locals inside `processBlock` — they carry state between calls.

---

## prepareToPlay — replace the constructor body

Move all initialization from the Airwindows constructor into `prepareToPlay`:

```cpp
void MyProcessor::prepareToPlay(double sampleRate, int /*samplesPerBlock*/)
{
    // Reset all state variables (copy from Airwindows constructor):
    controlAposL = controlAnegL = 1.0;
    controlBposL = controlBnegL = 1.0;
    targetposL = targetnegL = 1.0;
    lastOutputL = 0.0;
    // ... (repeat for R channel)
    flip = false;
    fpdL = 1; while (fpdL < 16386) fpdL = rand() * UINT32_MAX;
    fpdR = 1; while (fpdR < 16386) fpdR = rand() * UINT32_MAX;

    // Compute sample-rate-dependent constants (from Airwindows preamble):
    overallscale = sampleRate / 44100.0;
    spacing = static_cast<int>(std::floor(overallscale));
}
```

Store `sampleRate` and `overallscale` as members. Never call `getSampleRate()` inside
the per-sample loop.

---

## processBlock — adapt the per-sample loop

```cpp
void MyProcessor::processBlock(AudioBuffer<float>& buffer, MidiBuffer&)
{
    // Read parameters once per block (Airwindows does this too)
    double compress = A;  // or however you expose parameters
    double output   = B * 2.0;
    double wet      = C;

    auto* channelL = buffer.getWritePointer(0);
    auto* channelR = buffer.getWritePointer(1);

    for (int i = 0; i < buffer.getNumSamples(); ++i)
    {
        double inputSampleL = channelL[i];
        double inputSampleR = channelR[i];

        // Denormal prevention (keep from Airwindows):
        if (fabs(inputSampleL) < 1.18e-23) inputSampleL = fpdL * 1.18e-17;
        fpdL ^= fpdL << 13; fpdL ^= fpdL >> 17; fpdL ^= fpdL << 5;

        // ---- paste Airwindows DSP here ----

        channelL[i] = static_cast<float>(inputSampleL);
        channelR[i] = static_cast<float>(inputSampleR);
    }
}
```

---

## Parameter smoothing — add this, Airwindows doesn't

Airwindows reads `A`, `B`, `C` once at the top of each block and uses that value for
the entire block. Automation creates step discontinuities (zipper noise) at block
boundaries.

JUCE fix: use `SmoothedValue<double>`:

```cpp
// In header:
juce::SmoothedValue<double> compressSmoothed;

// In prepareToPlay:
compressSmoothed.reset(sampleRate, 0.02);  // 20ms smoothing

// In processBlock, before the loop:
compressSmoothed.setTargetValue(A);

// In the per-sample loop:
double compress = compressSmoothed.getNextValue();
```

---

## Sample-rate-dependent filter coefficients

Airwindows recomputes filter coefficients at the top of `processDoubleReplacing`
using `getSampleRate()`. In JUCE, do this in `prepareToPlay` AND in `processBlock`
only if a parameter changed (cheaper than every block):

```cpp
// In prepareToPlay:
recomputeCoefficients(getSampleRate());

// In processBlock — check for parameter changes:
if (parametersChanged.exchange(false))
    recomputeCoefficients(getSampleRate());
```

---

## Stereo handling

Airwindows consistently uses `L` and `R` suffix variables. Every state variable has
a mirror (`iirSampleAL` / `iirSampleAR`). When porting, make sure both channels get
their own state — never share filter state between L and R.

---

## Float vs. double

Airwindows `processDoubleReplacing` uses `double` throughout for precision. JUCE
`AudioBuffer<float>` gives you floats. Cast on read and write; keep all intermediate
math as `double`:

```cpp
double inputSampleL = static_cast<double>(channelL[i]);
// ... all processing in double ...
channelL[i] = static_cast<float>(inputSampleL);
```

---

## Output dither — usually skip it in JUCE

The floating-point output dither in Airwindows (`frexpf` + scaled PRNG noise) is
designed for reducing 32-bit float wordlength. In a JUCE plugin running at 32-bit
float throughout, this adds noise without benefit. Omit it unless you're doing
intentional wordlength reduction (dither plugins only).

---

## Quick-reference checklist

- [ ] All state variables declared as class members (not locals)
- [ ] State initialized in `prepareToPlay`, not constructor
- [ ] `overallscale = sampleRate / 44100.0` computed in `prepareToPlay`
- [ ] `fpdL`/`fpdR` denormal prevention kept in the per-sample loop
- [ ] Filter coefficients recomputed when parameters change (not every sample)
- [ ] `SmoothedValue` added for automation-exposed parameters
- [ ] L and R state variables kept separate (never shared)
- [ ] All math in `double`; cast to `float` only at buffer write
