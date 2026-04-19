# PurestConsoleBuss

**Category:** Consoles
**Source:** `plugins/WinVST/PurestConsoleBuss/`
**Unique ID:** `pcob`

## One-line sonic description

The transparency reference — stateless `asin()` saturation only; no slew, no gain, no DC servo; adds spatial depth without color.

## What it does algorithmically

The simplest console algorithm Chris makes. Per sample:

1. Hard-clip input to ±1.0 (required — without this, `asin()` receives out-of-range values and produces NaN DC offset at full blast)
2. Apply `asin()` saturation
3. Dither to 32-bit float (disabled in double-precision path)

That's the entire algorithm. No internal state at all (`state_var_doubles = 0`). No parameters. The decoder side (PurestConsoleChannel) encodes with `sin()`, this decodes with `asin()` — the pair is mathematically complementary, so with no gain and very clean signal, the net effect approaches transparency.

## Key parameters

None — this plugin has zero parameters by design.

## Typical use cases

- Master buss where you want the console topology effect (spatial depth, common-mode density) without tonal coloration
- A/B reference: run this alongside Console5Buss to hear what the slew accumulation adds
- Minimalist mixes where any added color is unwanted

## Sonic vocabulary tags

transparent, clean, open, reference, purest, depth without color

## Port notes

- No state variables to declare (beyond `fpdL`/`fpdR` for the dither PRNG)
- No `prepareToPlay` initialization needed beyond PRNG seeding
- The `±1.0` input clip before `asin()` is mandatory — do not remove it
- Zero latency, zero parameters — trivial to integrate
