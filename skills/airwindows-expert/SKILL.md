---
name: airwindows-expert
description: >-
  Expert guide to the Airwindows DSP plugin library by Chris Johnson (506
  open-source algorithms, MIT licensed). Covers plugin selection by sonic goal,
  algorithm details, C++ parameter interfaces, and porting into JUCE processors.
  Use when: the user asks which Airwindows plugin achieves a sonic goal (warm,
  gritty, phasey, glue, tape, air); asks how an Airwindows algorithm works;
  wants to port or integrate Airwindows DSP into a JUCE project; asks about
  console summing, tape saturation, dithering, or spatial/reverb algorithms in a
  plugin-development context; references a specific Airwindows plugin by name.
  Do NOT trigger on general audio mixing questions that don't mention plugins or
  code.
---

# Airwindows Expert

Airwindows is Chris Johnson's open-source DSP plugin library: 506 algorithms across
22 categories, MIT licensed, written in pure C++ with no external dependencies.
No GUIs — pure DSP. Every plugin processes stereo float and double at all sample rates.

## Repository layout

```
airwindows/
├── plugins/WinVST/{PluginName}/   ← canonical C++ source (506 plugins)
│   ├── {Name}.h                   ← class, enum, state variables
│   ├── {Name}.cpp                 ← lifecycle, parameter names/display
│   └── {Name}Proc.cpp             ← all DSP (processReplacing / processDoubleReplacing)
├── docs/data/plugins.json         ← 507 plugins with descriptions + categories
├── Airwindopedia.txt              ← complete text catalog (all 506, authoritative)
├── what.txt                       ← one-line summary per plugin
└── skills/airwindows-expert/
    ├── references/plugin-index.json    ← machine-readable index of all 506 plugins
    └── references/plugins/{name}.md   ← curated docs for 20 key plugins
```

`plugins.json` covers 507 entries — all WinVST plugins with descriptions and categories.
`plugin-index.json` covers all 506 WinVST plugins and is the authoritative existence check.

## Category taxonomy (22 categories)

| Category | Count | Description |
|----------|-------|-------------|
| Consoles | 45 | Analog console summing and bus character |
| Filter | 48 | EQ, parametric, and specialty filters |
| Reverb | 36 | Algorithmic and matrix reverb |
| Dynamics | 33 | Compressors, gates, limiters |
| Utility | 35 | Gain, routing, monitoring helpers |
| Brightness | 26 | High-frequency presence and air |
| Ambience | 25 | Delays, doubling, spatial thickening |
| Dithers | 23 | Wordlength reduction and noise shaping |
| XYZ Filters | 23 | X/Y/Z topology specialty filters |
| Effects | 28 | Ring mod, tremolo, exciter, creative |
| Lo-Fi | 19 | Bit crushing, sample-rate reduction, tape degradation |
| Subtlety | 19 | Mastering-grade transparent coloration |
| Distortion | 13 | Harmonic saturation and overdrive |
| Saturation | 17 | Smooth saturation and analog warmth |
| Bass | 10 | Sub-octave, low-end, infrasonic |
| Tape | 12 | Tape machine emulation |
| Stereo | 12 | MS processing, width, stereo field |
| Biquads | 9 | Biquad IIR filter primitives |
| Clipping | 9 | Hard and adaptive limiting/clipping |
| Noise | 9 | Noise generation, removal, shaping |
| Tone Color | 15 | Channel strip and bus coloration |
| Amp Sims | 17 | Guitar and bass amp emulation |

## Navigation guide — load the right reference

| Question type | Load this |
|---------------|-----------|
| "Which plugin for [sonic goal]?" | [sonic-vocabulary.md](references/sonic-vocabulary.md) |
| "How does [PluginName] work?" | [references/plugins/{name}.md](references/plugins/) if it exists; otherwise read `Airwindopedia.txt` or `{Name}Proc.cpp` directly |
| "All plugins in a category?" | [categories.md](references/categories.md) |
| "Port this DSP into JUCE" | [integration-juce.md](references/integration-juce.md) |
| "Build a plugin UI for an Airwindows-derived processor" | [juce-ui-components.md](references/juce-ui-components.md) |
| "What are Chris's recurring idioms?" | [dsp-idioms.md](references/dsp-idioms.md) |
| "Does plugin X exist / what are its parameters?" | Query `plugin-index.json` (506 records, one per plugin) |
| "MIT license, attribution?" | [licensing.md](references/licensing.md) |

## 20 curated plugin references

Detailed files exist for these plugins. For all others, use `plugin-index.json`.

**Console/Summing:** [console8-bussout](references/plugins/console8-bussout.md) · [console5-buss](references/plugins/console5-buss.md) · [purest-console-buss](references/plugins/purest-console-buss.md)

**Tape:** [totape9](references/plugins/totape9.md) · [ironoxide5](references/plugins/ironoxide5.md)

**Distortion/Saturation:** [hard-vacuum](references/plugins/hard-vacuum.md) · [density2](references/plugins/density2.md) · [spiral2](references/plugins/spiral2.md)

**Dynamics:** [buttercomp2](references/plugins/buttercomp2.md) · [pressure6](references/plugins/pressure6.md) · [varimu](references/plugins/varimu.md)

**Reverb:** [galactic2](references/plugins/galactic2.md) · [matrixverb](references/plugins/matrixverb.md)

**EQ/Filter:** [smootheq3](references/plugins/smootheq3.md) · [bezeq2](references/plugins/bezeq2.md)

**Brightness:** [air4](references/plugins/air4.md)

**Tone Color:** [busscolors4](references/plugins/busscolors4.md)

**Dithers:** [pauldither](references/plugins/pauldither.md) · [dark](references/plugins/dark.md)

**Clipping:** [adclip8](references/plugins/adclip8.md)

**Lo-Fi:** [derez3](references/plugins/derez3.md)

## Key design principles

- **No UI.** Parameters exposed as float A, B, C … Z (0.0–1.0 normalized). Host DAW provides display.
- **Dual precision.** Every plugin implements `processReplacing` (float) and `processDoubleReplacing` (double).
- **No external dependencies.** Pure C++ stdlib only.
- **Denormal prevention.** All plugins inject noise below `1.18e-23` using an Xorshift PRNG (`fpdL`/`fpdR`).
- **Sample-rate adaptive.** Modern plugins scale timing, filters, and buffers to `getSampleRate() / 44100.0`.
- **Chunked presets.** State serialized via binary `getChunk`/`setChunk`, not text.

See [dsp-idioms.md](references/dsp-idioms.md) for code-level detail on these patterns.
