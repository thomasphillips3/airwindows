---
phase: 01-add-juce-ui-component-recommendations-to-the-airwindows-expert-skill
plan: "01"
subsystem: skills/airwindows-expert
tags: [documentation, juce, plugin-ui, skill-reference]
dependency_graph:
  requires: []
  provides: [juce-ui-components reference doc, SKILL.md nav routing for UI questions]
  affects: [skills/airwindows-expert/SKILL.md]
tech_stack:
  added: []
  patterns: [APVTS attachment pattern, widget-before-attachment declaration order]
key_files:
  created:
    - skills/airwindows-expert/references/juce-ui-components.md
  modified:
    - skills/airwindows-expert/SKILL.md
decisions:
  - LookAndFeel customization deferred to future phase (per D-08) — keeps doc focused and bounded
  - JUCE 8 targeted; JUCE 7 differences noted inline where they exist
  - Checklist extended to 10 items (plan required 8 minimum) for completeness
metrics:
  duration_minutes: 15
  completed_date: "2026-04-20"
  tasks_completed: 2
  tasks_total: 2
  files_created: 1
  files_modified: 1
---

# Phase 01 Plan 01: Add JUCE UI Component Recommendations — Summary

JUCE plugin editor reference doc created covering APVTS attachment classes, all standard widgets, and `GenericAudioProcessorEditor` fallback for Airwindows-derived processors, with nav routing added to SKILL.md.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Write juce-ui-components.md | f56fc9d50 | skills/airwindows-expert/references/juce-ui-components.md (created, 313 lines) |
| 2 | Update SKILL.md navigation table | b6b986d44 | skills/airwindows-expert/SKILL.md (+1 row) |

## What Was Built

### skills/airwindows-expert/references/juce-ui-components.md

New 313-line reference doc covering the JUCE plugin editor layer for Airwindows-derived processors. Matches `integration-juce.md` style exactly: H2 sections, `cpp`-tagged code blocks, terse actionable prose, checklist at end.

Sections:
- Quick-reference cheat-sheet table (widgets × attachments × parameter types × use cases)
- APVTS setup — `createParameterLayout()` with `AudioParameterFloat` wiring Airwindows A/B/C params
- `AudioProcessorEditor` structure — widget-before-attachment declaration order rule, initializer-list wiring
- Slider — rotary and linear; `setRange()` not needed with `SliderAttachment`
- Label — static naming + dynamic value display via `onValueChange` lambda
- TextButton — `onClick` lambda; noted as not for Airwindows 0–1 params
- ToggleButton + `ButtonAttachment` — `AudioParameterBool` wiring
- ComboBox + `ComboBoxAttachment` — `AudioParameterChoice`, item IDs start at 1
- `TabbedComponent` — chained Airwindows processor layout, `owner=true` lifetime management
- Custom `paint()` — `GainMeter` example with `juce::Timer` at 30fps
- `GenericAudioProcessorEditor` — no-UI fallback, zero code required

JUCE 7 → 8 differences noted inline: APVTS API unchanged; `GenericAudioProcessorEditor` respects `ParameterGroup` in JUCE 8; `ComboBoxAttachment` item ID mapping documented.

### skills/airwindows-expert/SKILL.md

One row added to the navigation table after "Port this DSP into JUCE":

```
| "Build a plugin UI for an Airwindows-derived processor" | [juce-ui-components.md](references/juce-ui-components.md) |
```

All existing rows intact, no reformatting.

## Verification Results

All 11 acceptance tests passed:
- File exists at expected path
- 20 matches for attachment class names (required >=4)
- 17 cpp code blocks (required >=5)
- JUCE 8 mentioned in doc (2 inline notes)
- TabbedComponent, GenericAudioProcessorEditor present
- 10 checklist items (required >=5)
- No LookAndFeel content (deferred per D-08)
- SKILL.md nav row present, UI question row present, DSP row intact

## Deviations from Plan

None — plan executed exactly as written.

## Known Stubs

None — this plan produces documentation only. All code snippets are complete and ready for copy-paste use.

## Self-Check: PASSED

- `skills/airwindows-expert/references/juce-ui-components.md` — FOUND (f56fc9d50)
- `skills/airwindows-expert/SKILL.md` (nav row) — FOUND (b6b986d44)
