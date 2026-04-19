# MatrixVerb

**Category:** Reverb
**Source:** `plugins/WinVST/MatrixVerb/`
**Unique ID:** `mxvb`

## One-line sonic description

Two parallel Householder reverbs feeding back into each other — wildly adjustable from spring-like flutter to enormous concrete cavern, with vibrato, damping, and flavor controls.

## What it does algorithmically

Citation: "It's actually two parallel Householder reverbs in the place of one. But what would happen if you had them feed back into each other, not just into themselves? Turns out two different things can happen. One is a twisting and distorting of the sonic space into a distinctly… SPRING-like [character]."

The cross-coupled Householder matrix creates emergent behavior:
- At certain Speed/Flavor settings: spring reverb character (the cross-coupling creates flutter-like oscillation in the reverb tail)
- At other settings: enormous, diffuse, natural room/hall character ("highs fall away at the same rate they would in a giant concrete cavern")

Speed controls the modulation rate of the coupled matrices (vibrato-like variation in the delay times). Vibrato adds pitch-modulated variation independently. RmSize scales the overall delay line lengths (room size). Filter shapes the input to the reverb; Damping shapes the feedback.

45 state variables — large, but smaller than Galactic2.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Filter | Input filtering before reverb |
| B | Damping | Feedback highpass (more = brighter tails) |
| C | Speed | Householder modulation rate |
| D | Vibrato | Additional pitch modulation |
| E | RmSize | Room size (delay line scaling) |
| F | Flavor | Cross-coupling character between matrices |
| G | Dry/Wet | Blend |

## Typical use cases

- Spring reverb on guitars (specific Speed + Flavor combinations)
- Massive hall reverb on orchestral or ambient material (low Speed, large RmSize)
- Creative spaces — the two-matrix coupling creates reverbs unlike anything else
- Experimentation: this plugin rewards unusual settings

## Sonic vocabulary tags

spring, spacious, cavernous, complex, flexible, phasey at extremes, Householder

## Port notes

- 45 `double` state variables — delay line buffers for two separate Householder matrices
- The cross-coupling between matrices is in the Proc.cpp feedback path — read carefully before porting
- Speed and Vibrato interact; the modulation is applied to delay line indices, not a separate LFO
- RmSize scales all delay lengths; changes require re-allocating or re-indexing buffer usage
- `overallscale` applied to delay indices for sample-rate adaptation
