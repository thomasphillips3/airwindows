# Task: Build an `airwindows-expert` skill

I have an Airwindows repository at `./airwindows/` (Chris Johnson's
open-source plugin collection). Build a Claude skill at
`./skills/airwindows-expert/` that future Claude Code sessions — and
subagents spawned by them — can load to become fluent in this codebase.

The skill's job is to let a coding agent answer questions like:
- "Which Airwindows plugin gives me that warm, glued console-bus feel?"
- "How does ToTape's saturation stage actually work?"
- "I want phasey movement without a traditional LFO — what fits?"
- "Port the core DSP loop from Console7 into my JUCE processor."

## Phase 0 — Read the authoring guide

Before touching anything else, read `/mnt/skills/examples/skill-creator/SKILL.md`
in full. It's the canonical guide for skill structure, SKILL.md frontmatter,
progressive disclosure, and reference organization. Follow it. If anything
below conflicts with it, the skill-creator guide wins — surface the
conflict to me instead of silently picking one.

Also skim one example of a skill that acts as a *router* over a large
corpus rather than inlining everything: `/mnt/skills/public/pdf-reading/SKILL.md`
is a reasonable model. That's the shape we want — SKILL.md teaches the
map, references hold the territory.

## Phase 1 — Investigate the Airwindows repo (CHECKPOINT)

Do real exploration before authoring. Specifically:

1. **Directory map.** Airwindows is organized by plugin format (VST2, VST3,
   AU, LV2, CLAP, etc.) with per-plugin folders under each. Find where
   the canonical C++ sources live — typically one format's tree is the
   "reference" and the others are near-mirrors. Pick that tree and use
   it as the source of truth. Note the path in your checkpoint.
2. **Taxonomy from evidence.** Derive categories from the actual repo,
   not from memory. Look at README files, any `docs/` or website-data
   checked in, and the plugin names themselves. Chris's own groupings
   (console/summing, saturation/tape, EQ/tilt, reverb/space, dither,
   "weird/experimental", utility, etc.) should emerge from what's there.
   If the repo contains conflicting groupings, pick one and say why.
3. **Recurring idioms.** While exploring, note Chris's DSP idioms that
   repeat across plugins: the `fpdL`/`fpdR` floating-point dither pattern,
   his interleaved-sample console model, denormal handling, sample-rate
   adaptation, the "not-just-an-LFO" modulation tricks. These deserve
   their own reference doc later — capture the list now.
4. **Plugin shortlist.** Pick 15–25 high-signal plugins for the first
   documentation pass, chosen to (a) cover every category you identified
   and (b) include the ones a working mix engineer actually reaches for:
   the Console series, ToTape/IronOxide, Density, BussColors, Galactic,
   Air, Tape, PurestConsole, ChannelEVH, Tilt, etc. Use judgment. Don't
   pick 25 saturators.

**STOP HERE and report back to me with:**
- The directory you chose as source of truth and why.
- The category taxonomy you derived, with 1-line descriptions.
- The list of recurring DSP idioms you noticed.
- Your 15–25 plugin shortlist, grouped by category, with a one-line
  justification per plugin.
- Anything in the repo that confused you or that you couldn't confidently
  categorize.

Wait for my confirmation before proceeding to Phase 2. This checkpoint
matters — the taxonomy and shortlist are the decisions I actually want
to review. Per-plugin docs after that are mostly grinding.

## Phase 2 — Build the extraction script first

Before authoring per-plugin reference files by hand, write a small
extraction script that walks the Airwindows source tree and pulls out,
for every plugin (not just the shortlist), a structured metadata record.
This is the scaffolding step — it turns the mechanical work into a batch
operation and leaves you free to spend real effort on the interpretive
parts (sonic vocabulary, algorithm prose, port notes).

Place the script at `skills/airwindows-expert/scripts/extract-plugin-metadata.py`
(Python preferred over bash for this — the parsing is non-trivial).

**What the script must extract, per plugin:**
- Plugin name and canonical source directory path (relative to `./airwindows/`)
- Primary `.cpp` / `.h` file paths
- Any README, `.txt`, or description file content found in the plugin dir
- The parameter list. Airwindows plugins declare parameters in a
  predictable pattern (typically in the `.h` file or a `GetParameterName`
  / `getParameterText` style function). Parse this structurally — don't
  just regex for strings.
- Approximate DSP complexity signals: total `.cpp` line count, count of
  `fpdL`/`fpdR` references (indicates Chris's dither idiom is present),
  presence of `sampleRate` conditionals (indicates sample-rate-adaptive
  DSP), count of internal state variables.
- Any inline comments at the top of the `.cpp` — these often contain
  Chris's own sonic description and are gold for the vocabulary map.

**Output format:** a single `plugin-index.json` written to
`skills/airwindows-expert/references/` containing an array of records,
one per plugin. This file is both (a) an input to the authoring step and
(b) a useful reference in its own right — when a future session needs to
know "does a plugin called X exist and where is it," this is faster than
a filesystem walk.

**Run the script** against `./airwindows/` and verify the output looks
sane before moving on. Spot-check 3–4 plugins against the actual source
to confirm the extraction is accurate. If the parameter parsing is
brittle for some plugins, record that — it's fine for the script to emit
`"parameters": "unparsed"` for edge cases rather than guessing wrong.

**Report to me:**
- Total plugin count found.
- A sample record or two from the JSON.
- Any extraction failures or edge cases worth knowing about.

Then proceed to Phase 3.

## Phase 3 — Author the skill

Using the `plugin-index.json` as input, build the skill. Structure:

```
skills/airwindows-expert/
  SKILL.md                      ← taxonomy, navigation, when to load refs
  references/
    plugin-index.json           ← from Phase 2; machine-readable catalog
    categories.md               ← category map, derived from the repo
    sonic-vocabulary.md         ← human mixing terms → plugins
    dsp-idioms.md               ← Chris's recurring patterns
    integration-juce.md         ← porting into a JUCE processor
    licensing.md                ← MIT + attribution notes
    plugins/
      console7.md
      totape.md
      density.md
      ...                       ← one file per documented plugin
  scripts/
    extract-plugin-metadata.py  ← from Phase 2
    find-plugin.sh              ← ripgrep helper over ./airwindows/ (optional)
```

### SKILL.md requirements

- **Frontmatter `description`** must fire on: Airwindows-specific questions,
  DSP algorithm references in a plugin-development context, mixing
  vocabulary like "warm"/"gritty"/"phasey"/"glue" when paired with code
  or plugin intent, and porting C++ DSP into a JUCE project. Do NOT
  make it so broad it triggers on every audio question — "how do I
  compress vocals" should not load this skill.
- **Body** teaches the map, not the territory. Cover: what Airwindows is,
  the category taxonomy, how sonic vocabulary maps to categories, the
  path layout under `./airwindows/`, the existence and purpose of
  `plugin-index.json` (so a session can look up plugins that weren't
  documented in depth), and — critically — explicit instructions on
  which reference file to load for which kind of question. Keep it tight.
  SKILL.md is not a tutorial.

### Per-plugin reference files

For the 15–25 shortlisted plugins, author a human-curated reference
file. Use `plugin-index.json` to pre-fill the mechanical fields
(source path, parameters, complexity signals) and then spend your real
effort on the interpretive fields. Each `plugins/*.md` follows a
consistent template:

- **Category** (from the taxonomy)
- **One-line sonic description** in mix-engineer vocabulary
- **What it does algorithmically** — in prose, not a code dump. If you
  can't describe it confidently from the source, say so.
- **Key parameters** and what they do sonically
- **Typical use cases** — what a mix engineer actually reaches for it for
- **Sonic vocabulary tags** — the human terms that should route here
- **Source path** — relative to `./airwindows/`
- **Port notes** — anything non-obvious about lifting it into JUCE
  (state that has to persist, sample-rate behavior, stereo handling)

Keep each plugin file tight. Target ~40–80 lines. A bloated reference
is a useless reference.

Plugins not in the shortlist are still discoverable via
`plugin-index.json` — future passes can promote them to full references
as needed.

### Sonic vocabulary reference

Map terms → plugins → one-line *why*. Cover at minimum: warm, warmth,
glue, cohesion, gritty, crunchy, dirty, saturated, phasey, swirly,
chorusy, wide, air, sheen, sparkle, open, punch, thump, slam, weight,
cool, clean, clinical, transparent, tape, console, tube, transistor,
lo-fi, degraded, crushed.

Ground these in Chris's own language where possible — his code comments,
READMEs, or airwindows.com copy if it's checked into the repo. The
`plugin-index.json` includes extracted top-of-file comments; mine those
for Chris's own sonic descriptions. When you're extrapolating from the
algorithm rather than citing Chris, mark it as your inference, not his
claim. This distinction matters.

### DSP idioms reference

Document the recurring patterns you found in Phase 1 and that the
extraction script surfaced via its complexity signals: the `fpdL`/`fpdR`
noise-shaping/dither state, the interleaved-sample console model,
denormal prevention idioms, sample-rate adaptation patterns, any
recurring modulation tricks. Short illustrative snippets (≤15 lines) are
fine and useful here — this is the one place code excerpts earn their
keep. Explain *why* Chris does it that way, not just what the code is.

### Integration reference

`integration-juce.md` covers practical porting into a JUCE
`AudioProcessor`: which state goes as members vs. locals, how to handle
sample rate in `prepareToPlay`, stereo channel handling, parameter
smoothing (Airwindows typically doesn't smooth — note what that means
for automation), and how the per-sample structure of most Airwindows
plugins maps onto JUCE's block-based `processBlock`.

## Hard constraints

- **No verbatim code dumps.** Describe algorithms in prose and point at
  file paths. Short snippets (≤15 lines) to illustrate a recurring idiom
  are the only exception, and only in `dsp-idioms.md`.
- **No inventing plugins.** If a plugin you expected doesn't exist in
  this repo version, say so. Don't hallucinate. `plugin-index.json` is
  ground truth for what's present.
- **No padding.** A tight 40-line plugin reference beats a bloated
  200-line one every time. If you're repeating yourself, cut.
- **Mark inference vs. citation.** When the sonic description comes from
  Chris's own words (including the top-of-file comments extracted by the
  script), it's a citation. When it's your read of the algorithm, it's
  inference. Use different framing for each ("Chris describes this as…"
  vs. "The algorithm suggests…").
- **Skill is partially self-contained.** Someone cloning this repo
  without `./airwindows/` present should still get the taxonomy, sonic
  vocab, idioms, integration guidance, and the full plugin index — only
  the `plugins/*.md` references point at paths that won't resolve
  without the Airwindows repo, and that's fine.

## Deliverable (end of Phase 3)

1. Final directory tree of `skills/airwindows-expert/`.
2. Full `SKILL.md` contents.
3. Confirmation that `extract-plugin-metadata.py` ran cleanly and
   `plugin-index.json` is populated, with the total plugin count.
4. The list of plugins documented in depth this pass vs. deferred to
   `plugin-index.json`-only coverage, with a one-line reason per
   deferred plugin so I can direct the next pass.
5. **Gaps and uncertainty log.** Anything in the Airwindows repo you
   found confusing, any plugin whose algorithm you couldn't confidently
   describe, any place you extrapolated sonic vocabulary without
   grounding, any extraction-script edge cases. I'd rather have a clear
   gap list than papered-over confidence.

## Working style

- Use TodoWrite to track the phases and don't skip Phase 1's checkpoint.
- Read the skill-creator guide before anything else. If you find
  yourself about to author SKILL.md from intuition, stop and re-read it.
- When in doubt between "document more plugins" and "document fewer
  plugins better" — fewer, better. Coverage can expand in a second pass,
  and `plugin-index.json` means undocumented plugins are still
  discoverable.
