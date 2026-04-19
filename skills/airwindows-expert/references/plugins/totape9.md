# ToTape9

**Category:** Tape
**Source:** `plugins/WinVST/ToTape9/`
**Unique ID:** `tot9`

## One-line sonic description

The definitive Airwindows tape emulation — flutter, bias, tilt, shape, and head bump, all built on a breakthrough core that Chris says "put the previous version to shame."

## What it does algorithmically

Citation: "The heart of ToTape is completely replaced by what I learned making TapeHack2, itself a giant leap over the original TapeHack, which was itself a huge discovery. When I tried this in the guts of ToTape I was just completely shocked by how huge it sounded."

The algorithm layers:
- **Tilt/Shape** implemented as Dubly-style encode/decode controls — Tilt leans toward brightness or darkness via bias adjustment; Shape controls old-school vs. big-studio character
- **Flutter** modulates delay buffer timing (`sweepL/R`) within `dL/dR[1002]` — the sweep speed is separately controllable
- **Bias** (`hysteresisL/R`) — hysteresis modeling that simulates oxide saturation response
- **Head bump** (`headBumpL/R`) — fixed-frequency biquad resonance modeling the LF boost from tape head coupling; HeadFrq adjusts the center frequency
- **Pre/post averaging arrays** at 2/4/8/16/32 sample resolutions (`avg32L[33]` etc.) for anti-aliasing and tape-style slew limiting
- **ClipOnly3 output stage** (`lastSampleL`, `intermediateL[18]`, `slewL[34]`) — same family as Console8's clipper
- 53 state variable doubles — the most complex plugin in the shortlist

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Input | Drive level into tape saturation |
| B | Tilt | Balance between brightness and darkness (Dubly-style) |
| C | Shape | Old-school vs. big-studio saturation character |
| D | Flutter | Flutter amount |
| E | FlutSpd | Flutter rate |
| F | Bias | Tape bias/saturation intensity |
| G | HeadBmp | Head bump resonance amount |
| H | HeadFrq | Head bump center frequency (Hz) |
| I | Output | Output gain |

## Typical use cases

- Full-mix tape processing on the master bus (subtle Bias + Tilt)
- Drum bus warmth with head bump to reinforce kick and snare
- Creative flutter and wow effects on specific tracks

## Sonic vocabulary tags

warm, tape, vintage, saturated, weighted, organic, flutter

## Port notes

- 53 `double` state variables — read `.h` carefully; allocate all `avg*`, `post*`, `gslew[]`, `hdbA[]`, `hdbB[]` arrays
- `dL[1002]`, `dR[1002]` — flutter delay buffers; must be member arrays
- `gcount` integer — flutter phase accumulator; member
- Head bump biquad (`hdbA/hdbB`) coefficients must be recomputed in `prepareToPlay` and when HeadFrq changes
- ClipOnly3 state (`intermediateL/R[18]`, `slewL/R[34]`, clip flags) — must be member state
- Read Proc.cpp for the flutter delay and head bump biquad implementation
