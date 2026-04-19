# Airwindows Sonic Vocabulary

Maps mixing/engineering terms to Airwindows plugins with one-line rationale.
**Citation** = Chris's own words (Airwindopedia or code comments).
**Inference** = algorithm-derived interpretation, marked explicitly.

---

## Warm / Warmth

Plugins that add second-harmonic density and analog-style softness.

| Plugin | Why |
|--------|-----|
| **HardVacuum** | Citation: "warmth control brings in second harmonic and nonlinearity like class A tube design" |
| **ToTape9** | Citation: tape saturation via hysteresis and IIR modeling "sounds huge" |
| **IronOxide5** | Citation: IPS-based bandwidth shaping creates bandpassed "warmth" character |
| **Console5Buss** | Inference: `asin()` encode/decode with slew accumulation rounds transients and adds low-mid density |
| **Tube / Tube2** | Inference: soft-clip tube curve emphasizes even harmonics |
| **SquareRoot** | Inference: progressive-width linear region stays warm without brightness artifacts |

---

## Glue / Cohesion

Plugins that make separate tracks sound like they belong together.

| Plugin | Why |
|--------|-----|
| **Console5Buss** | Citation (community): "big, beefy, large-console sound…adds glue and bigness" |
| **Console8BussOut** | Inference: ClipOnly2 output stage catches transient peaks without audible distortion, creating macro-level coherence |
| **ButterComp2** | Citation: "the one that sounds musical, that doesn't add pumping or breathing or artifacts" |
| **Pressure6** | Citation: "2-buss compressor feel" — gain reduction with organic movement |
| **PurestConsoleBuss** | Inference: shared `asin()` saturation applied to summed signal adds subtle common-mode density |

---

## Gritty / Crunchy / Dirty

Plugins with harmonic complexity and edge.

| Plugin | Why |
|--------|-----|
| **Density2** | Citation: "density, weight, color" — unusual algorithm preserved exactly; gritty character |
| **Dirt** | Inference: raw distortion stage with minimal smoothing |
| **Spiral2** | Inference: `sin(x·|x|)/|x|` saturation is smooth but at high drive becomes gritty |
| **IronOxide5 (high flutter)** | Inference: flutter at extreme settings adds pitch instability and grit |
| **HardVacuum (high Aura)** | Citation: "hot searing overtones you might not have heard from a plugin before" |
| **GrindAmp** | Inference: amp sim designed for grind/metal character |

---

## Saturated / Thick / Heavy

Full-sounding saturation without distortion.

| Plugin | Why |
|--------|-----|
| **Density2** | Citation: "density" is literally the parameter name; control adds weight |
| **ToTape9** | Citation: input slam into tape emulation "sounds huge" — adds density without transient damage |
| **BussColors4** | Inference: convolution-based coloration at high input adds transformer-style thickness |
| **HardVacuum (moderate Drive/Warmth)** | Citation: "class A tube design" adds saturation in a musical, thick way |
| **Console5Buss + Console5Channel** | Inference: full console chain with encode/decode creates thick summing character |

---

## Phasey / Swirly / Chorusy

Plugins that introduce phase movement or spatial modulation.

| Plugin | Why |
|--------|-----|
| **ADT** | Inference: artificial double tracking via modulated delay creates phase-based swirl |
| **StereoChorus** | Inference: chorus via modulated delay lines; phasey stereo movement |
| **MatrixVerb** | Citation: spring-reverb mode creates "twisting and distorting of the sonic space" |
| **GalacticVibe** | Inference: Galactic reverb variant with vibe modulation |
| **AngleEQ** | Inference: phase-scrambled resonant EQ; "deliberately phasey" design |

---

## Air / Sheen / Sparkle

High-frequency extension and presence without harshness.

| Plugin | Why |
|--------|-----|
| **Air4** | Citation: brings out "spatial position in air…CLOSE…within a few millimeters of your eardrum" |
| **Air / Air2 / Air3** | Inference: cascaded difference filters extract ultra-high presence |
| **PurestAir** | Inference: purest form of Air processing |
| **HardVacuum (Aura)** | Citation: "Aura control will bring out sparkly highs" |
| **SmoothEQ3 (High boosted)** | Inference: 3rd-order HF shelf via biquad crossover; musical high shelf |

---

## Punch / Slam / Thump

Transient impact and attack definition.

| Plugin | Why |
|--------|-----|
| **ADClip8** | Citation: golden ratio clipping "designed for punchiness without artifacts" — inference from algorithm |
| **DrumSlam** | Inference: named for drum bus punch; dynamics + saturation combination |
| **Console8BussOut** | Inference: ClipOnly2 catches peaks cleanly, letting transients punch through below ceiling |
| **Thunder** | Inference: specifically designed for drum bus transient impact |
| **ToTape9 (Shape to bright)** | Inference: Tilt/Shape toward bright/punchy adds attack definition |

---

## Dark / Weight / Depth

Plugins that shift tonal balance downward or add low-end gravity.

| Plugin | Why |
|--------|-----|
| **Dark (dither)** | Citation: "gives your music a blacker backdrop" |
| **ToTape9 (Tilt to dark)** | Inference: tilt control toward dark mode shifts energy toward low frequencies |
| **IronOxide5 (low IPS)** | Inference: low IPS setting narrows bandwidth toward bass-heavy vintage tape character |
| **Slew / Slew3** | Inference: slew limiting rolls off extreme highs, darkening the signal |
| **DubSub2** | Inference: specifically designed to add sub-bass weight |
| **FathomFive** | Inference: deep sub-bass harmonic generation |

---

## Transparent / Clean / Open

Processing that's present but inaudible when subtracted from dry.

| Plugin | Why |
|--------|-----|
| **PurestConsoleBuss** | Citation: "most free from coloration Console system" — stateless `asin()` only |
| **PurestDrive** | Inference: minimal saturation drive designed for transparency |
| **PurestGain** | Inference: gain only, no processing artifacts |
| **SmoothEQ3** | Citation: "most approachable EQ" — 3rd-order Butterworth at Q=1.0, low artifact |
| **Dark (dither, HD mode)** | Citation: "if you think you can reliably hear this on its HD setting, I think you're mistaken" |

---

## Tape

Dedicated tape emulation character.

| Plugin | Why |
|--------|-----|
| **ToTape9** | Citation: "most successful plugin I've ever had" — flutter, bias, tilt, shape, head bump |
| **IronOxide5** | Citation: IPS-based bandwidth, flutter, noise — "better than commercial offerings" (community) |
| **IronOxideClassic / IronOxideClassic2** | Inference: older algorithm, different flavor of bandpassed tape saturation |
| **TapeHack2** | Citation: the "breakthrough" that powers ToTape9's core |
| **TapeDust** | Inference: noise-like artifacts from tape dust simulation |

---

## Console

Console summing and analog bus processing.

| Plugin | Why |
|--------|-----|
| **Console8BussOut + Console8BussIn** | Inference: latest full architecture, most modern anti-aliasing |
| **Console5Buss + Console5Channel** | Citation (community): "the big, beefy" workhorse console combination |
| **PurestConsoleBuss + PurestConsoleChannel** | Citation: "most free from coloration" — transparency reference |
| **BussColors4** | Citation: convolution-based bus coloration "huge deal…before console emulations were a thing" |
| **Channel9** | Inference: newer single-plugin channel with coloration |

---

## Tube / Transistor / Lo-Fi / Degraded

Character-specific coloration vocabulary.

| Term | Plugins |
|------|---------|
| **tube** | HardVacuum, Tube2, SingleEndedTriode |
| **transistor** | BussColors4 (transistor mode), Channel variants |
| **lo-fi** | DeRez3, HipCrush, Flutter2, GrooveWear, ChromeOxide |
| **degraded / crushed** | DeRez3, BitGlitter, DustBunny |
| **vintage sampler** | DeRez3 — Citation: "reinvents retro digital tones" with Bezier interpolation |
| **cool / clinical** | PurestConsoleBuss, PurestDrive — transparent processing chain |
