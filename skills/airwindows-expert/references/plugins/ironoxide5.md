# IronOxide5

**Category:** Tape
**Source:** `plugins/WinVST/IronOxide5/`
**Unique ID:** `feob`

## One-line sonic description

Dedicated tape saturation algorithm with dual IPS bandwidth controls, flutter, and noise — the mix engineer's tape tool when ToTape9 is too much.

## What it does algorithmically

Citation: "Iron Oxide 2 split the 'ips' top and bottom cutoffs, so you could vary the 'bandpassy' quality it had. It used the same unusual algorithm, but made it more flexible. It also incorporated an unusual sort of anti-aliasing in the form of a 'tape noise' factor that blurred slew."

IronOxide5's core algorithm: dual IIR filters define a bandwidth window (Tape High and Tape Low IPS controls). The IPS values map to low-pass and high-pass filter frequencies that together create the "bandpassy" quality characteristic of different tape speeds — low IPS (7.5 ips) sounds narrow and warm; high IPS (30 ips) sounds wider and brighter. Flutter adds time-domain modulation. Noise adds a controllable tape hiss floor.

Inv/Dry/Wet goes from -1.0 (inverted wet) through 0.0 (dry) to 1.0 (full wet) — the invert mode is useful for null-testing.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Input Trim | Drive level (dB) |
| B | Tape High | Upper bandwidth IPS (high tape speed = bright/wide) |
| C | Tape Low | Lower bandwidth IPS (low tape speed = warm/narrow) |
| D | Flutter | Flutter modulation amount |
| E | Noise | Tape noise floor level |
| F | Output Trim | Output gain (dB) |
| G | Inv/Dry/Wet | -1.0 to 1.0 wet mix |

## Typical use cases

- Individual track tape saturation (not full-mix; better suited to subgroups)
- Drum overhead "7.5 ips" warmth — low IPS narrows bandwidth appealingly
- Creative flutter on vocals or pads
- Null testing via Inv mode to hear exactly what tape adds

## Sonic vocabulary tags

warm, tape, bandpassed, IPS, flutter, vintage, saturation

## Port notes

- 33 state variables — IIR filter state, flutter delay buffer, averaging buffers
- IPS parameters map to Hz values for IIR coefficient computation — check `Proc.cpp` for exact mapping
- Input/Output Trim are in dB — use `pow(10, dB/20)` for conversion
- Inv/Dry/Wet: handle the negative range (inverted wet) explicitly in blend code
