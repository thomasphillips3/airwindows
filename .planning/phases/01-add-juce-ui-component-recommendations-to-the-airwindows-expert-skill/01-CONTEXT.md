# Phase 1: Add JUCE UI Component Recommendations to the Airwindows-Expert Skill - Context

**Gathered:** 2026-04-19
**Status:** Ready for planning

<domain>
## Phase Boundary

Add a new reference document (`juce-ui-components.md`) to `skills/airwindows-expert/references/` that covers JUCE UI components for building plugin GUIs around Airwindows-derived processors. Update SKILL.md navigation table to point to the new doc. The existing `integration-juce.md` covers the processor/DSP side; this doc covers the editor/UI side. LookAndFeel customization is explicitly out of scope.

</domain>

<decisions>
## Implementation Decisions

### Delivery format
- **D-01:** New file: `skills/airwindows-expert/references/juce-ui-components.md` — do NOT extend `integration-juce.md`
- **D-02:** Update `skills/airwindows-expert/SKILL.md` navigation table with a new row pointing to the new doc (question type: "Build a plugin UI for an Airwindows-derived processor")

### Content depth
- **D-03:** Code-backed reference — each component gets: what it is, when to use it for Airwindows params, and a short C++ snippet
- **D-04:** Match the style and depth of `integration-juce.md`: concrete, copy-paste ready, no hand-wavy prose

### Component scope
- **D-05:** Cover the full JUCE plugin UI toolkit: `Slider` (rotary + linear), `Label`, `TextButton`, `ToggleButton`, `ComboBox`, `TabbedComponent`, custom `paint()` for custom drawing
- **D-06:** Include APVTS attachment classes: `SliderAttachment`, `ButtonAttachment`, `ComboBoxAttachment` — show how to wire Airwindows float A–Z parameters to UI controls
- **D-07:** Include `GenericAudioProcessorEditor` as a no-UI fallback (useful for headless/testing scenarios)
- **D-08:** Do NOT cover `LookAndFeel` customization — deferred to a future phase

### JUCE version
- **D-09:** Target JUCE 8 (aligns with mixgame JUCE 8.0.4 and JFTR plugins)
- **D-10:** Note API differences from JUCE 7 where relevant (e.g., any changed APVTS APIs)

### Claude's Discretion
- Document section order and heading structure
- Whether to include a quick-reference summary table at the top (like a cheat sheet before detailed sections)
- Code snippet length — keep them illustrative, not exhaustive

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Existing skill structure (pattern to follow)
- `skills/airwindows-expert/SKILL.md` — navigation table to update; defines how agents route to references
- `skills/airwindows-expert/references/integration-juce.md` — DSP-side JUCE integration guide; the new doc must match this style

### Airwindows parameter convention
- `plugins/WinVST/ButterComp2/ButterComp2.h` — representative example of float A–Z parameter declarations to reference in APVTS wiring examples

No external specs — requirements are fully captured in decisions above.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `integration-juce.md`: Style template — section headers, code block format, checklist at end. New doc should follow this exactly.
- `plugin-index.json`: 506 plugins with parameter counts — useful for grounding "how many params does a typical plugin have" context in the doc

### Established Patterns
- `SKILL.md` navigation table format: `| Question type | Load this |` — new row slots in here
- All 20 curated plugin docs follow a consistent structure — the new reference doc should feel native to the skill

### Integration Points
- `SKILL.md` is the entry point agents read first; the new nav row is the hook that makes the UI doc discoverable
- The doc is consumed by coding agents building JUCE plugin UIs — write for that audience

</code_context>

<specifics>
## Specific Ideas

- No specific references or "I want it like X" moments — open to standard approaches beyond the style match with `integration-juce.md`

</specifics>

<deferred>
## Deferred Ideas

- LookAndFeel customization (drawRotarySlider, drawLinearSlider) — future phase or separate doc
- None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-add-juce-ui-component-recommendations-to-the-airwindows-expert-skill*
*Context gathered: 2026-04-19*
