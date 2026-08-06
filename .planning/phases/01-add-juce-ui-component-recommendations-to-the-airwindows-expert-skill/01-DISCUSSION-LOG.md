# Phase 1: Add JUCE UI Component Recommendations - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-19
**Phase:** 01-add-juce-ui-component-recommendations-to-the-airwindows-expert-skill
**Areas discussed:** Delivery format, Content depth, Component scope, JUCE version

---

## Delivery format

| Option | Description | Selected |
|--------|-------------|----------|
| New file: juce-ui-components.md | Keeps DSP porting and UI separate. SKILL.md navigation table gets a new row. Clean mental model. | ✓ |
| Extend integration-juce.md | Single doc for all JUCE integration. Simpler to find, but mixes two distinct concerns. | |
| You decide | Claude picks the structure during planning. | |

**User's choice:** New file — `references/juce-ui-components.md`
**Notes:** Clean separation: integration-juce.md = processor side, juce-ui-components.md = UI side.

---

## Content depth

| Option | Description | Selected |
|--------|-------------|----------|
| Code-backed reference | Each component gets: what it is, when to use it for Airwindows params, and a short C++ snippet. Mirrors integration-juce.md style. | ✓ |
| Quick reference table only | Component → use case table, no code. Faster to write, but agents may not know how to wire things up. | |
| Full tutorial with worked example | Build a complete example plugin UI end-to-end. Most thorough, may be overkill for a skill reference. | |

**User's choice:** Code-backed reference
**Notes:** Match the style of integration-juce.md — concrete, copy-paste ready.

---

## Component scope

| Option | Description | Selected |
|--------|-------------|----------|
| Airwindows-essential set | Slider, Label, TextButton, APVTS attachments, GenericAudioProcessorEditor as fallback. | |
| Full JUCE plugin UI toolkit | Add TabbedComponent, ComboBox, ToggleButton, custom paint(). More complete. | ✓ |
| Core + LookAndFeel customization | Core components plus custom LookAndFeel for visual identity. | |

**User's choice:** Full JUCE plugin UI toolkit

### LookAndFeel follow-up

| Option | Description | Selected |
|--------|-------------|----------|
| Yes — include it | One section on overriding drawRotarySlider / drawLinearSlider. | |
| No — keep it deferred | Skip LookAndFeel; cover in future phase. | ✓ |
| You decide | Claude judges during planning. | |

**User's choice:** Deferred — no LookAndFeel in this phase
**Notes:** Full toolkit (Slider/Label/TextButton/ToggleButton/ComboBox/TabbedComponent/paint()/APVTS attachments/GenericAudioProcessorEditor) but no LookAndFeel.

---

## JUCE version

| Option | Description | Selected |
|--------|-------------|----------|
| JUCE 8 | mixgame uses JUCE 8.0.4, JFTR plugins likely same. Note JUCE 7 differences where relevant. | ✓ |
| Version-agnostic | Avoid version-specific APIs. Safer across projects. | |
| JUCE 7 | Target older stable version. | |

**User's choice:** JUCE 8
**Notes:** Note API differences from JUCE 7 where relevant.

---

## Claude's Discretion

- Document section order and heading structure
- Whether to include a quick-reference summary table at the top
- Code snippet length

## Deferred Ideas

- LookAndFeel customization (drawRotarySlider, drawLinearSlider) — future phase or separate doc
