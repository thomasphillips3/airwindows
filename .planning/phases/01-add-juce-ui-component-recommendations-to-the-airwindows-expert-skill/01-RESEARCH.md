# Phase 1 Research: JUCE UI Component Recommendations for airwindows-expert

**Phase:** 01 — Add JUCE UI component recommendations to the airwindows-expert skill  
**Researched:** 2026-04-19  
**Approach:** Documentation phase — create `juce-ui-components.md` reference + update SKILL.md nav table

---

## 1. What this phase produces

Two file changes only:

1. **New file:** `skills/airwindows-expert/references/juce-ui-components.md`  
   A copy-paste-ready reference for coding agents building JUCE plugin editors around Airwindows-derived processors. Covers the full standard widget set, APVTS attachment classes, and a no-UI fallback.

2. **Edit:** `skills/airwindows-expert/SKILL.md` navigation table  
   Add one row routing "Build a plugin UI for an Airwindows-derived processor" questions to the new doc.

---

## 2. Style template — integration-juce.md

The existing `integration-juce.md` is the style model. Key conventions to match:

- **Top-level title + one-sentence description**, then `---`
- **Architecture mismatch table** at top (sets context for the audience)
- **H2 sections** (`##`) for each major topic
- **Code blocks** with `cpp` language tag; snippets are realistic but trimmed (not exhaustive)
- **Comments in snippets** explain *why*, not just what
- **Quick-reference checklist** at the end (markdown checkboxes `- [ ]`)
- Prose is terse and direct — no hand-wavy text; every sentence is actionable

---

## 3. JUCE 8 UI component reference (the actual technical content)

### 3.1 APVTS — the right way to wire Airwindows float A–Z params

`AudioProcessorValueTreeState` (APVTS) is JUCE's standard mechanism for binding parameters to UI controls with automation support. For Airwindows plugins, the float `A`, `B`, `C` params (0.0–1.0 normalized) map directly to `AudioParameterFloat` entries.

**APVTS declaration (processor header):**
```cpp
juce::AudioProcessorValueTreeState apvts;
```

**APVTS construction (processor constructor):**
```cpp
MyProcessor::MyProcessor()
    : apvts(*this, nullptr, "Parameters", createParameterLayout())
{}

juce::AudioProcessorValueTreeState::ParameterLayout MyProcessor::createParameterLayout()
{
    juce::AudioProcessorValueTreeState::ParameterLayout layout;
    // Airwindows A param: "Compress" 0.0–1.0, default 0.5
    layout.add(std::make_unique<juce::AudioParameterFloat>(
        "compress", "Compress",
        juce::NormalisableRange<float>(0.0f, 1.0f), 0.5f));
    layout.add(std::make_unique<juce::AudioParameterFloat>(
        "output", "Output",
        juce::NormalisableRange<float>(0.0f, 1.0f), 1.0f));
    layout.add(std::make_unique<juce::AudioParameterFloat>(
        "wet", "Wet",
        juce::NormalisableRange<float>(0.0f, 1.0f), 1.0f));
    return layout;
}
```

**Reading params in processBlock:**
```cpp
float A = *apvts.getRawParameterValue("compress");  // live, thread-safe read
float B = *apvts.getRawParameterValue("output");
float C = *apvts.getRawParameterValue("wet");
```

> **JUCE 7 → 8 note:** The APVTS API is identical in JUCE 7 and 8. No breaking changes here.

---

### 3.2 AudioProcessorEditor structure

```cpp
class MyEditor : public juce::AudioProcessorEditor
{
public:
    MyEditor(MyProcessor& p, juce::AudioProcessorValueTreeState& apvts);
    ~MyEditor() override;
    void paint(juce::Graphics& g) override;
    void resized() override;

private:
    MyProcessor& processor;

    juce::Slider compressSlider;
    juce::Label  compressLabel;
    juce::AudioProcessorValueTreeState::SliderAttachment compressAttachment;
    // ... repeat for each param
};
```

**Constructor:**
```cpp
MyEditor::MyEditor(MyProcessor& p, juce::AudioProcessorValueTreeState& apvts)
    : AudioProcessorEditor(&p), processor(p),
      compressAttachment(apvts, "compress", compressSlider)  // APVTS wires it
{
    compressSlider.setSliderStyle(juce::Slider::RotaryVerticalDrag);
    compressSlider.setTextBoxStyle(juce::Slider::TextBoxBelow, false, 60, 20);
    addAndMakeVisible(compressSlider);

    compressLabel.setText("Compress", juce::dontSendNotification);
    compressLabel.setJustificationType(juce::Justification::centred);
    addAndMakeVisible(compressLabel);

    setSize(300, 200);
}
```

**Key rule:** `SliderAttachment` must be declared AFTER the `Slider` in the class definition (destruction order: attachment destroyed before slider — safe). Declare attachments AFTER their associated widgets.

---

### 3.3 Slider — rotary and linear

Airwindows float A–Z parameters (0.0–1.0) map naturally to JUCE sliders.

**Rotary (knob) — most common for effect parameters:**
```cpp
juce::Slider knob;
knob.setSliderStyle(juce::Slider::RotaryVerticalDrag);
knob.setTextBoxStyle(juce::Slider::TextBoxBelow, false, 60, 20);
knob.setRange(0.0, 1.0);  // not needed if using APVTS attachment
addAndMakeVisible(knob);
```

**Linear horizontal — good for mix/wet params:**
```cpp
juce::Slider wetSlider;
wetSlider.setSliderStyle(juce::Slider::LinearHorizontal);
wetSlider.setTextBoxStyle(juce::Slider::TextBoxRight, false, 50, 20);
addAndMakeVisible(wetSlider);
```

**Attachment wires range and callbacks automatically:**
```cpp
juce::AudioProcessorValueTreeState::SliderAttachment wetAttachment;
// in constructor:
wetAttachment(apvts, "wet", wetSlider)  // range, value, and callbacks all handled
```

---

### 3.4 Label

Used to name knobs and display parameter values.

```cpp
juce::Label label;
label.setText("Compress", juce::dontSendNotification);
label.setJustificationType(juce::Justification::centred);
label.setFont(juce::Font(14.0f));
addAndMakeVisible(label);
```

**Dynamic value display** — attach to slider via `onValueChange`:
```cpp
knob.onValueChange = [this] {
    valueLabel.setText(juce::String(knob.getValue(), 2), juce::dontSendNotification);
};
```

---

### 3.5 TextButton

For trigger actions (bypass, reset, preset load). Not typically used for Airwindows 0–1 params, but useful for bypass or "init preset" controls.

```cpp
juce::TextButton resetButton;
resetButton.setButtonText("Reset");
resetButton.onClick = [this] { processor.resetState(); };
addAndMakeVisible(resetButton);
```

---

### 3.6 ToggleButton + ButtonAttachment

Airwindows plugins occasionally have boolean parameters (e.g., a mode switch). In JUCE, use `AudioParameterBool` + `ToggleButton`.

```cpp
// In createParameterLayout():
layout.add(std::make_unique<juce::AudioParameterBool>("mode", "Mode", false));

// In editor:
juce::ToggleButton modeButton;
juce::AudioProcessorValueTreeState::ButtonAttachment modeAttachment;
// constructor:
modeAttachment(apvts, "mode", modeButton)

modeButton.setButtonText("Linked");
addAndMakeVisible(modeButton);
```

---

### 3.7 ComboBox + ComboBoxAttachment

For integer-choice parameters (e.g., algorithm variant, oversampling factor). Map to `AudioParameterChoice`.

```cpp
// In createParameterLayout():
layout.add(std::make_unique<juce::AudioParameterChoice>(
    "algo", "Algorithm",
    juce::StringArray{"Linear", "Cubic", "Sinc"}, 0));

// In editor:
juce::ComboBox algoBox;
juce::AudioProcessorValueTreeState::ComboBoxAttachment algoAttachment;
// constructor:
algoAttachment(apvts, "algo", algoBox)

algoBox.addItem("Linear", 1);
algoBox.addItem("Cubic",  2);
algoBox.addItem("Sinc",   3);
addAndMakeVisible(algoBox);
```

> **JUCE 8 note:** `ComboBoxAttachment` in JUCE 8 expects item IDs to start at 1 (not 0). The attachment maps choice index 0 → ComboBox item ID 1 automatically, but manually added items must start at ID 1.

---

### 3.8 TabbedComponent

Useful for plugins with many Airwindows processors chained (e.g., console + tape + eq). Each tab can hold a different processor's controls.

```cpp
juce::TabbedComponent tabs;
// in constructor:
tabs.setTabBarDepth(30);
tabs.addTab("Dynamics",  juce::Colours::darkgrey, new DynamicsPanel(apvts), true);
tabs.addTab("Tone",      juce::Colours::darkgrey, new TonePanel(apvts),     true);
addAndMakeVisible(tabs);
```

In `resized()`:
```cpp
tabs.setBounds(getLocalBounds());
```

---

### 3.9 Custom paint() — parameter-driven drawing

For visual feedback (VU meter, waveform, gain reduction). Override `paint()` in a custom `Component`:

```cpp
class GainMeter : public juce::Component, public juce::Timer
{
public:
    void paint(juce::Graphics& g) override
    {
        g.fillAll(juce::Colours::black);
        float level = processor.getGainReduction();  // 0.0–1.0
        g.setColour(juce::Colours::green);
        g.fillRect(0.0f, 0.0f, (float)getWidth() * level, (float)getHeight());
    }
    void timerCallback() override { repaint(); }
};
```

Start the timer in `prepareToPlay` or the editor constructor:
```cpp
meter.startTimerHz(30);  // 30fps repaint
```

---

### 3.10 GenericAudioProcessorEditor — no-UI fallback

`GenericAudioProcessorEditor` renders all APVTS parameters as a list of sliders automatically. Zero UI code required. Useful for:
- Headless / testing scenarios
- Quick prototypes before building a custom editor
- Confirming parameters are wired correctly

```cpp
juce::AudioProcessorEditor* MyProcessor::createEditor()
{
    return new juce::GenericAudioProcessorEditor(*this);
}

bool MyProcessor::hasEditor() const { return true; }
```

**JUCE 8 note:** `GenericAudioProcessorEditor` respects APVTS parameter groups — if you use `ParameterGroup` in your layout, the generic editor renders collapsible group headers.

---

## 4. SKILL.md nav table update

Current table (from SKILL.md):

```markdown
| Question type | Load this |
|---------------|-----------|
| "Which plugin for [sonic goal]?" | sonic-vocabulary.md |
| "How does [PluginName] work?" | references/plugins/{name}.md |
| "All plugins in a category?" | categories.md |
| "Port this DSP into JUCE" | integration-juce.md |
| "What are Chris's recurring idioms?" | dsp-idioms.md |
| "Does plugin X exist / what are its parameters?" | plugin-index.json |
| "MIT license, attribution?" | licensing.md |
```

**New row to insert** (logically after the "Port this DSP into JUCE" row):

```markdown
| "Build a plugin UI for an Airwindows-derived processor" | [juce-ui-components.md](references/juce-ui-components.md) |
```

---

## 5. Document structure recommendation

Based on `integration-juce.md` style analysis:

```
# Building a JUCE Plugin Editor for Airwindows Processors

<one-sentence description>

---

## Quick-reference: APVTS attachments

<cheat-sheet table: widget | attachment class | use for>

---

## APVTS setup
## AudioProcessorEditor structure
## Slider — rotary and linear
## Label
## TextButton
## ToggleButton + ButtonAttachment
## ComboBox + ComboBoxAttachment
## TabbedComponent
## Custom paint()
## GenericAudioProcessorEditor — no-UI fallback

---

## Quick-reference checklist
- [ ] ...
```

The cheat-sheet table at the top is "Claude's discretion" from CONTEXT.md — recommend including it. It mirrors the pattern of `integration-juce.md`'s architecture mismatch table and gives agents a fast orientation before the detailed sections.

---

## 6. JUCE 7 → 8 API differences (relevant to this doc)

| Area | JUCE 7 | JUCE 8 |
|------|--------|--------|
| APVTS | Unchanged | Unchanged |
| SliderAttachment | Unchanged | Unchanged |
| ButtonAttachment | Unchanged | Unchanged |
| ComboBoxAttachment | Unchanged | Unchanged |
| GenericAudioProcessorEditor | Basic | Respects `ParameterGroup` for collapsible sections |
| TabbedComponent | Unchanged | Unchanged |
| `AudioParameterFloat` | Constructor takes min/max/default | Unchanged |

**Bottom line:** JUCE 8 API for plugin editors is backward-compatible with JUCE 7. Note the `GenericAudioProcessorEditor` group rendering improvement — that's the only meaningful difference to call out.

---

## Validation Architecture

### What to test
This phase produces documentation only — no executable code. Validation is:

1. **File existence check** — new file at `skills/airwindows-expert/references/juce-ui-components.md`
2. **SKILL.md nav update** — new row present in navigation table
3. **Style conformance** — new doc matches `integration-juce.md` structure (H2 sections, checklist at end, `cpp` code blocks)
4. **Coverage check** — all D-05 through D-07 components present in doc (Slider, Label, TextButton, ToggleButton, ComboBox, TabbedComponent, paint(), GenericAudioProcessorEditor, APVTS attachment classes)
5. **JUCE version note** — D-10: doc mentions JUCE 8 target and JUCE 7 differences where relevant

---

## 8. Planning implications

This phase is **one wave, one or two plans:**

| Plan | What | Files modified |
|------|------|----------------|
| Plan A | Write `juce-ui-components.md` | `skills/airwindows-expert/references/juce-ui-components.md` (new) |
| Plan B | Update SKILL.md nav table | `skills/airwindows-expert/SKILL.md` (edit) |

Both plans are so tightly coupled (the nav update is 1 line referencing the new file) that a single plan covering both is viable. Planner's choice.

**No code changes, no builds, no tests** — just file creation + one-line edit.

---

## RESEARCH COMPLETE
