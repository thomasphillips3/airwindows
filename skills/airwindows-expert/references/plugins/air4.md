# Air4

**Category:** Brightness
**Source:** `plugins/WinVST/Air4/`
**Unique ID:** `aiyu`

## One-line sonic description

Cascaded-difference presence lift with adaptive gain control and Sinew slew limiting — adds air and sparkle while preventing the harsh ultra-highs that cause overslew.

## What it does algorithmically

Citation: "Air4 extends Air3 in a way that can help people trying my Meter plugin, and unable to get good high frequencies without bombing the slew section with red 'overslew' spikes."

Stage 1 — Presence extraction: a cascade of differences (`pvSL`, `accSL`, `acc2SL`) computes second-order derivatives of the audio signal. This extracts content that's changing rapidly (high-frequency transients and presence) and adaptively mixes it with the dry signal. An adaptive gain control (`gainAL`) prevents the presence extraction from exceeding a limit, even if the source signal changes level suddenly.

The `Gnd` (ground) parameter biases the extraction — it computes a running average (`gndavgL`) that anchors the detector's center of gravity, preventing false triggering from DC or sub-bass content.

Stage 2 — Sinew slew limiter: applies a rate limit to the output using `cos(air[lastSL] * air[lastSL])` as a velocity-dependent threshold. This prevents the presence boost from creating extreme slew-rate spikes that would register as "overslew" on metering. The `DarkF` parameter scales this limiting.

`Ratio` blends between the presence-enhanced and dry signal.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Air | Presence extraction intensity |
| B | Gnd | Ground/anchor bias for the detector |
| C | DarkF | Sinew slew limiter intensity (higher = darker ceiling) |
| D | Ratio | Wet/dry blend |

## Typical use cases

- Adding air to mixes without harshness (DarkF controls the ceiling)
- Presence on vocals or acoustic instruments where overslew is a concern
- When Air3 causes overslew problems on your metering
- Mix bus air lift at the end of a chain

## Sonic vocabulary tags

air, sparkle, presence, open, bright, controlled, slew-limited

## Port notes

- Only 1 `double` state variable in `.h` (the `air[]` array is indexed by enum internally)
- `air[pvAL1..pvAL4]` — 4 cascaded prior samples for derivative computation (member array)
- `air[accSL1..3]`, `air[acc2SL1..2]` — first and second difference accumulators
- `air[gainAL]`, `air[gndavgL]` — adaptive gain and ground average
- `air[lastSL/SR]` — Sinew slew state (last output value)
- Presence extraction cascade structure is in Proc.cpp
- `overallscale` used for timing in the Sinew rate limiting
