# Galactic2

**Category:** Reverb
**Source:** `plugins/WinVST/Galactic2/`
**Unique ID:** `galb`

## One-line sonic description

Householder matrix reverb redesigned for "painting" space — Drive loads the reverb space, Sustain holds it, Darken shapes tone; 108 state variable doubles, the most complex reverb on the shortlist.

## What it does algorithmically

Citation: "I'd imagined a thing where you'd have reverb space going, and then you'd 'paint' in other sound, perhaps with a slider, or just by overloading the existing space with other stuff."

The core is a Householder feedback reverb matrix — banks of delay lines whose outputs are combined via Householder transformation to create infinite diffuse reverb. Galactic2 uses dual parallel Householder matrices that feed into each other (same architecture as MatrixVerb but tuned for lushness rather than flexibility).

Drive controls how aggressively new signal "paints into" the existing reverb space — at high Drive, transients load the reverb matrix heavily and you get a wash of spatial energy. Sustain controls how long the reverb tails hold (feedback gain in the matrix). Darken applies a lowpass to the feedback path, rolling off high frequencies over successive reflections.

108 double state variables — the delay line buffers for Householder matrices are large.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Drive | How aggressively signal loads the reverb space |
| B | Sustain | Reverb tail length (matrix feedback gain) |
| C | Darken | Highpass rolloff on feedback path (more = darker tails) |
| D | Wetness | Wet/dry blend |

## Typical use cases

- Lush pad reverb — Galactic2's intended use case
- Ambient wash on synths and strings (high Sustain + Darken)
- Creating a "space" that exists before the music enters it (pre-load with Drive)
- When you want Airwindows reverb character without MatrixVerb's spring modes

## Sonic vocabulary tags

lush, spacious, ambient, wash, pad reverb, infinite, immersive, Householder

## Port notes

- 108 `double` state variables — the delay line buffers are the bulk of this
- Read Proc.cpp for exact buffer sizes and Householder matrix coefficients
- Both L and R channels have separate matrix state — never share
- `overallscale` scales delay buffer indices for sample-rate adaptation
- Large memory footprint — allocate buffers in `prepareToPlay`, not on the stack
