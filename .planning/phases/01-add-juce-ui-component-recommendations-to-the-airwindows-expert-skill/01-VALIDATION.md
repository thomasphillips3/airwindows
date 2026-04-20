---
phase: 1
slug: add-juce-ui-component-recommendations-to-the-airwindows-expert-skill
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-19
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | none — documentation phase (bash/grep checks only) |
| **Config file** | none |
| **Quick run command** | `ls skills/airwindows-expert/references/juce-ui-components.md` |
| **Full suite command** | see Per-Task Verification Map below |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run the relevant existence/grep check from the verification map
- **After every plan wave:** Run all grep checks in the map
- **Before `/gsd:verify-work`:** All checks must pass
- **Max feedback latency:** ~5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 1-01-01 | 01 | 1 | D-01 | existence | `test -f skills/airwindows-expert/references/juce-ui-components.md && echo PASS` | ❌ W0 | ⬜ pending |
| 1-01-02 | 01 | 1 | D-05/06/07 | content | `grep -c "SliderAttachment\|ButtonAttachment\|ComboBoxAttachment\|GenericAudioProcessorEditor" skills/airwindows-expert/references/juce-ui-components.md` (expect ≥4) | ❌ W0 | ⬜ pending |
| 1-01-03 | 01 | 1 | D-03/04 | content | `grep -c '^\`\`\`cpp' skills/airwindows-expert/references/juce-ui-components.md` (expect ≥5) | ❌ W0 | ⬜ pending |
| 1-01-04 | 01 | 1 | D-09/10 | content | `grep -i "JUCE 8\|JUCE 7" skills/airwindows-expert/references/juce-ui-components.md` | ❌ W0 | ⬜ pending |
| 1-02-01 | 02 | 1 | D-02 | content | `grep "juce-ui-components" skills/airwindows-expert/SKILL.md` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `skills/airwindows-expert/references/juce-ui-components.md` — new file (created in Plan 01)
- [ ] `skills/airwindows-expert/SKILL.md` — nav table row added (Plan 02)

*If none: "Existing infrastructure covers all phase requirements."*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Style matches integration-juce.md | D-04 | Subjective style conformance | Open both files side by side; confirm H2 sections, checklist at end, code blocks with `cpp` tag, terse prose |
| Quick-reference cheat-sheet table present | Claude's Discretion | Layout review | Read top of juce-ui-components.md; verify table mapping widget → attachment class → use-case |

---

## Validation Sign-Off

- [ ] All tasks have automated verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 10s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
