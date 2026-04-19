# Airwindows Category Map

Derived from `Airwindopedia.txt` and `plugins/WinVST/`. 22 categories, 506 plugins total.
For plugin existence and parameters, query `plugin-index.json`.

---

## Consoles (45 plugins)

Analog summing and console character. Used in channel strips and bus processing.
The core algorithm pairs a Channel plugin (on every track) with a Buss plugin (on the sum).

**Architecture:** Channel encodes signal (typically via `sin()` or `asin()` saturation);
Buss decodes and sums. This complementary encode/decode approach creates analog-style
summing nonlinearity without simply adding distortion.

**Key series:**
- **Console5** — `asin()` encode/decode with slew limiting; "richer, warmer, big console sound"
- **Console8** — `sin()` encode, ClipOnly2 on buss output, anti-aliasing at high SR; most current
- **PurestConsole** — stateless `asin()` only; ultra-transparent, adds depth without color
- **ConsoleLA / ConsoleMC / ConsoleMD** — character variants modeled on specific desk topologies
- **ConsoleX / ConsoleX2** — extended-parameter channel strips with EQ built in

**Notable:** Console5Buss is the workhorse; PurestConsoleBuss is the transparency reference.

---

## Filter (48 plugins)

EQ, parametric, and specialty filter algorithms. The largest category.

**Notable plugins:**
- **SmoothEQ3** — 3rd-order Butterworth crossover at simplified Q=1.0; approachable 3-band EQ
- **BezEQ2** — Bezier-curve crossover EQ; subtle latency, unusually transparent
- **AngleEQ** — deliberately phasey; resonant behavior for creative use
- **Dattorro** — state variable filter with Chris's custom softclip on bandpass output
- **Interstage** — subtle analogizer; contains high frequencies within hardware-like zone
- **Biquad / BiquadStack** — raw biquad primitives for building filter chains
- **Hull / Hull2** — moving-average filters; very gentle, no ringing
- **Capacitor / Capacitor2** — simulates capacitor-coupled high-pass behavior

---

## Reverb (36 plugins)

Algorithmic and matrix reverb processors.

**Notable plugins:**
- **Galactic / Galactic2 / Galactic3** — Householder matrix reverb; lush, spacious; Galactic2 adds Drive/Sustain/Darken control
- **MatrixVerb** — dual parallel Householder reverbs feeding back into each other; spring-like to enormous
- **VerbTiny / VerbThic** — classic artificial reverb shapes; Tiny expands, Thic adds fog
- **NonlinearSpace** — gated/experimental; pre-delay and shape controls
- **PocketVerbs** — collection of small room/ambience treatments
- **kCathedral / kPlate / kWoodRoom** — convolution-based, specific acoustic spaces

---

## Dynamics (33 plugins)

Compressors, gates, and gain-riding processors.

**Notable plugins:**
- **ButterComp / ButterComp2** — bipolar compressor; each half of the waveform treated independently
- **Pressure4 / Pressure5 / Pressure6** — vari-mu style; organic gain reduction, simple algorithm huge range
- **VariMu** — dual-speed envelope follower; more vintage-feel than Pressure
- **Logical4** — hardware stereo bus compressor behavior
- **BeziComp** — Bezier-curve gain reduction; technically perfect but "doesn't move right" (Chris's note)
- **SoftGate** — noise gate with soft knee
- **Thunder** — track-based transient shaping

---

## Tape (12 plugins)

Tape machine emulation: saturation, flutter, bias, and transport effects.

**Notable plugins:**
- **ToTape9** — most current; input, tilt, shape, flutter, flutter speed, bias, head bump, head freq, output
- **ToTape6 / ToTape7 / ToTape8** — evolutionary predecessors; still valid; each adds features
- **IronOxide5** — separate tape saturation algorithm; IPS-based bandwidth control, flutter, noise
- **IronOxideClassic / IronOxideClassic2** — older algorithm; different character
- **FromTape** — tape-style processing on input rather than output path
- **TapeHack / TapeHack2** — Chris's experimental tape core; TapeHack2 is the breakthrough used in ToTape9

---

## Saturation (17 plugins)

Smooth saturation without the aggressive character of Distortion.

**Notable plugins:**
- **Spiral / Spiral2** — `sin(x * |x|) / |x|` nonlinear; very smooth; Spiral2 adds presence and highpass
- **PurestDrive** — minimal saturation drive; transparent
- **PurestSaturation** — saturation in purest form
- **Tube / Tube2** — soft-clip tube emulation with sample history
- **SquareRoot** — `sqrt`-based saturation; linear region widens progressively
- **Hypersoft** — ultra-gentle soft saturation

---

## Distortion (13 plugins)

Harmonic saturation and overdrive with more pronounced character.

**Notable plugins:**
- **HardVacuum** — tube warmth (second harmonic) + Aura (sparkly highs overtones)
- **Density / Density2** — unusual older algorithm preserved exactly; "density, weight, color"
- **Drive** — basic saturation drive
- **Dirt** — gritty, raw distortion character
- **Mackity** — specific Mac-modeled distortion character

---

## Dithers (23 plugins)

Wordlength reduction and noise shaping for final output.

**Notable plugins:**
- **PaulDither** — Paul Kellett's TPDF single-pole highpass (previous-sample subtraction); quieter and airier
- **Dark** — Benford Realness analysis; "blacker backdrop"; current community standard
- **NotJustAnotherDither (NJAD)** — Benford analysis predecessor to Dark
- **TPDFDither** — flat TPDF; reference implementation
- **NodeDither** — multi-tap shaped TPDF
- **SpatializeDither** — dither with spatial spreading

Always apply dither as the absolute final step before output at the target bit depth.

---

## Brightness (26 plugins)

High-frequency presence, air, and slew-rate shaping.

**Notable plugins:**
- **Air / Air2 / Air3 / Air4** — cascaded differences for presence lift; Air4 adds DarkF (high-freq limiting)
- **PurestAir** — airier version using Chris's purest approach
- **Slew / Slew2 / Slew3** — slew-rate limiting; darkens/controls extreme highs
- **Acceleration / Acceleration2** — acceleration limiting; tames edge without removing brightness
- **DeEss / DeBess** — de-essing via slew-rate control on sibilance frequencies

---

## Distortion / Lo-Fi / Effects — remaining categories

- **Lo-Fi (19):** Bit crushing, sample-rate reduction, flutter, tape degradation. Key: **DeRez3** (Bezier-interpolated bitcrusher), **HipCrush**, **Flutter2**
- **Clipping (9):** Hard and adaptive limiters. Key: **ADClip8** (golden ratio clipper), **ClipOnly / ClipOnly2 / ClipOnly3**, **FinalClip**
- **Stereo (12):** MS processing, width. Key: **StereoFX**, **Srsly / Srsly2 / Srsly3**, **MidSide**
- **Tone Color (15):** Bus coloration. Key: **BussColors4** (convolution-based), **Channel4–9**, **Apicolypse**
- **Subtlety (19):** Mastering-grade transparent processing. Key: **Interstage**, **Desk**, **PurestWarm**
- **Bass (10):** Low-end shaping. Key: **DubSub2**, **BassKit**, **FathomFive**
- **Biquads (9):** Filter primitives. Key: **BiquadStack**, **BiquadNonLin**
- **Noise (9):** Noise tools. Key: **DarkNoise**, **DeNoise**, **VoiceOfTheStarship**
- **Utility (35):** Gain, monitoring, routing. Key: **PurestGain**, **BitShiftGain**, **Monitoring**
- **Ambience (25):** Spatial effects. Key: **ADT**, **StereoChorus**, **MV / MV2**
- **Effects (28):** Creative. Key: **GlitchShifter**, **Fracture / Fracture2**, **RingModulator**
- **Amp Sims (17):** Amp emulation. Key: **FireAmp**, **LeadAmp**, **GrindAmp**
- **XYZ Filters (23):** Specialty topologies. **Z-series** = zero-delay feedback; **Y-series** = inverted response; **X-series** = experimental
