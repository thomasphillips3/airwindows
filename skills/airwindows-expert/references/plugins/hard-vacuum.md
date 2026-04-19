# HardVacuum

**Category:** Utility (but functionally: Saturation/Distortion)
**Source:** `plugins/WinVST/HardVacuum/`
**Unique ID:** `hrdv`

## One-line sonic description

Tube emulation with second-harmonic warmth (Warmth) and a high-overtone sparkle stage (Aura) — from gentle class A to "hot searing overtones."

## What it does algorithmically

Citation: "It's got a warmth control that brings in second harmonic and nonlinearity like you might see in a class A tube design, but set up to be abused if you'd like to produce exaggerated effects…It's got a control called Aura that will bring out sparkly highs and hot searing overtones you might not have heard from a plugin before."

The Warmth stage uses a sine-based saturation curve (Chris's "Airwindows sine-based saturation curve") parameterized to emphasize even-order harmonics — specifically second harmonic — mimicking the characteristic of class A tube amplifier stages. At moderate Warmth, it adds analog weight; at high Warmth, it produces exaggerated, non-musical saturation.

The Aura stage targets high-frequency content separately, bringing out sparkly upper harmonics. The interaction between Drive, Warmth, and Aura gives this plugin an unusually wide range — from subtle analog coloration to aggressive tube overdrive.

Only 2 double state variables — lightweight despite the sonic complexity; the algorithm is primarily stateless saturation curves rather than filter-state processing.

## Key parameters

| Param | Name | Sonic effect |
|-------|------|-------------|
| A | Drive | Input gain into saturation |
| B | Warmth | Second-harmonic character; class A tube emulation |
| C | Aura | Sparkly high overtones; searing at extremes |
| D | Output | Output gain |
| E | Dry/Wet | Blend |

## Typical use cases

- Subtle tube warmth on vocals, bass, or guitars (low Drive, low-to-mid Warmth)
- Sparkly top-end presence on acoustic instruments (moderate Warmth, low-mid Aura)
- Creative tube overdrive effects when pushed hard
- Bus warmth when a lighter touch than ToTape9 is needed

## Sonic vocabulary tags

warm, tube, second harmonic, sparkle, aura, class A, vintage, analog

## Port notes

- Only 2 `double` state variables — very lightweight to port
- Primarily a stateless saturation curve; parameter scaling is the complexity
- Drive parameter maps to gain before the saturation stage
- Sine-based saturation curve: use `sin()` applied to scaled input; check Proc.cpp for exact coefficients
- No sample-rate adaptation needed (stateless saturation)
