# Building a JUCE Plugin Editor for Airwindows Processors

Covers `AudioProcessorEditor`, APVTS attachment classes, and the full standard widget set for building plugin GUIs around Airwindows-derived processors.

---

## Quick-reference: widgets and attachments

| Widget | APVTS attachment | Parameter type | Use for |
|--------|-----------------|----------------|---------|
| `Slider` | `SliderAttachment` | `AudioParameterFloat` | Airwindows float A-Z (0.0-1.0) |
| `ToggleButton` | `ButtonAttachment` | `AudioParameterBool` | On/off switches, mode flags |
| `ComboBox` | `ComboBoxAttachment` | `AudioParameterChoice` | Algorithm variants, integer choices |
| `TextButton` | none | n/a | Trigger actions (reset, preset load) |
| `Label` | none | n/a | Knob labels, dynamic value display |
| `TabbedComponent` | none | n/a | Multi-processor layouts (chained plugins) |
| Custom `Component` | none | n/a | VU meters, waveform display, visual feedback |
| `GenericAudioProcessorEditor` | automatic | all APVTS params | No-UI fallback, testing, prototyping |

---

## APVTS setup

`AudioProcessorValueTreeState` (APVTS) is the standard mechanism for binding parameters to UI controls with automation support. Airwindows float `A`, `B`, `C` params (0.0–1.0 normalized) map directly to `AudioParameterFloat` entries.

Declare APVTS in the processor header:

```cpp
juce::AudioProcessorValueTreeState apvts;
```

Construct it via `createParameterLayout()` — one `AudioParameterFloat` per Airwindows A/B/C param:

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

Read params in `processBlock` — live, thread-safe:

```cpp
float A = *apvts.getRawParameterValue("compress");
float B = *apvts.getRawParameterValue("output");
float C = *apvts.getRawParameterValue("wet");
```

> **JUCE 7 → 8 note:** The APVTS API is identical in JUCE 7 and 8. No breaking changes.

---

## AudioProcessorEditor structure

Declare widgets BEFORE their attachments in the class definition — attachment must be destroyed before the widget (C++ destruction is reverse of declaration order).

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

    // Widget declared BEFORE its attachment — destruction order rule
    juce::Slider compressSlider;
    juce::Label  compressLabel;
    juce::AudioProcessorValueTreeState::SliderAttachment compressAttachment;
    // Repeat pattern for each param
};
```

Wire everything in the constructor initializer list:

```cpp
MyEditor::MyEditor(MyProcessor& p, juce::AudioProcessorValueTreeState& apvts)
    : AudioProcessorEditor(&p), processor(p),
      compressAttachment(apvts, "compress", compressSlider)  // APVTS wires range + callbacks
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

---

## Slider — rotary and linear

Airwindows float A–Z parameters (0.0–1.0) map naturally to JUCE sliders. When using an APVTS attachment, `setRange()` is not needed — the attachment handles it.

```cpp
// Rotary (knob) — most common for effect parameters
juce::Slider knob;
knob.setSliderStyle(juce::Slider::RotaryVerticalDrag);
knob.setTextBoxStyle(juce::Slider::TextBoxBelow, false, 60, 20);
// setRange(0.0, 1.0) not needed when using SliderAttachment
addAndMakeVisible(knob);

// Linear horizontal — good for mix/wet params
juce::Slider wetSlider;
wetSlider.setSliderStyle(juce::Slider::LinearHorizontal);
wetSlider.setTextBoxStyle(juce::Slider::TextBoxRight, false, 50, 20);
addAndMakeVisible(wetSlider);
```

Attachment wires range, initial value, and automation callbacks automatically:

```cpp
class MyEditor : public juce::AudioProcessorEditor
{
public:
    MyEditor(juce::AudioProcessor& p, juce::AudioProcessorValueTreeState& state)
        : juce::AudioProcessorEditor(p),
          apvts(state),
          wetAttachment(apvts, "wet", wetSlider)
    {
        addAndMakeVisible(wetSlider);
    }

private:
    juce::AudioProcessorValueTreeState& apvts;
    juce::Slider wetSlider;
    juce::AudioProcessorValueTreeState::SliderAttachment wetAttachment;
};
```

---

## Label

Used to name knobs and display parameter values.

```cpp
juce::Label label;
label.setText("Compress", juce::dontSendNotification);
label.setJustificationType(juce::Justification::centred);
label.setFont(juce::Font(14.0f));
addAndMakeVisible(label);
```

Dynamic value display — attach to slider via `onValueChange` lambda:

```cpp
knob.onValueChange = [this] {
    valueLabel.setText(juce::String(knob.getValue(), 2), juce::dontSendNotification);
};
```

---

## TextButton

For trigger actions: bypass toggle, init preset, reset state. Not for Airwindows 0–1 params — use `SliderAttachment` for those. `TextButton` fires a one-shot callback with no parameter binding.

```cpp
juce::TextButton resetButton;
resetButton.setButtonText("Reset");
resetButton.onClick = [this] { processor.resetState(); };
addAndMakeVisible(resetButton);
```

---

## ToggleButton + ButtonAttachment

For boolean parameters — mode switches, linked/unlinked flags. Declare `AudioParameterBool` in the layout, then wire with `ButtonAttachment`.

```cpp
// In createParameterLayout():
layout.add(std::make_unique<juce::AudioParameterBool>("mode", "Mode", false));

// In editor class (widget before attachment):
juce::ToggleButton modeButton;
juce::AudioProcessorValueTreeState::ButtonAttachment modeAttachment;

// In constructor initializer list:
// modeAttachment(apvts, "mode", modeButton)

// In constructor body:
modeButton.setButtonText("Linked");
addAndMakeVisible(modeButton);
```

---

## ComboBox + ComboBoxAttachment

For integer-choice parameters — algorithm variants, oversampling factor, mode selection. Map to `AudioParameterChoice` in the layout. Item IDs must start at 1.

```cpp
// In createParameterLayout():
layout.add(std::make_unique<juce::AudioParameterChoice>(
    "algo", "Algorithm",
    juce::StringArray{"Linear", "Cubic", "Sinc"}, 0));

// In editor class:
juce::ComboBox algoBox;
juce::AudioProcessorValueTreeState::ComboBoxAttachment algoAttachment;

// In constructor initializer list:
// algoAttachment(apvts, "algo", algoBox)

// In constructor body — IDs start at 1, not 0:
algoBox.addItem("Linear", 1);
algoBox.addItem("Cubic",  2);
algoBox.addItem("Sinc",   3);
addAndMakeVisible(algoBox);
```

> **JUCE 8 note:** `ComboBoxAttachment` maps choice index 0 → ComboBox item ID 1 automatically. Manually added items must start at ID 1 or the mapping will be off by one.

---

## TabbedComponent

For plugins chaining multiple Airwindows processors (e.g., console + tape + EQ). Each tab holds one processor's controls. Pass `true` as the owner flag so `TabbedComponent` deletes the panels.

```cpp
juce::TabbedComponent tabs { juce::TabbedButtonBar::TabsAtTop };

// In constructor:
tabs.setTabBarDepth(30);
tabs.addTab("Dynamics",  juce::Colours::darkgrey, new DynamicsPanel(apvts), true);
tabs.addTab("Tone",      juce::Colours::darkgrey, new TonePanel(apvts),     true);
addAndMakeVisible(tabs);
```

In `resized()` — tabs fill the whole editor:

```cpp
void MyEditor::resized()
{
    tabs.setBounds(getLocalBounds());
}
```

---

## Custom paint()

For visual feedback — VU meter, gain reduction display, waveform. Subclass `juce::Component` and `juce::Timer`. Pull state from the processor via a simple float accessor; repaint on a timer callback.

Meter reads must use `std::atomic` or a lock-free FIFO — never read a plain `float` written by the audio thread (data race, UB). Expose the value as `std::atomic<float>` on the processor:

```cpp
// In MyProcessor:
std::atomic<float> gainReduction { 0.0f };
// In processBlock: gainReduction.store(computedLevel);
```

```cpp
class GainMeter : public juce::Component, public juce::Timer
{
public:
    explicit GainMeter(MyProcessor& p) : processor(p) {}

    void paint(juce::Graphics& g) override
    {
        g.fillAll(juce::Colours::black);
        float level = processor.gainReduction.load();  // atomic read — safe on message thread
        g.setColour(juce::Colours::green);
        g.fillRect(0.0f, 0.0f, (float)getWidth() * level, (float)getHeight());
    }

    void timerCallback() override { repaint(); }

private:
    MyProcessor& processor;
};
```

Start the timer in the editor constructor — 30 fps is smooth without burning CPU:

```cpp
meter.startTimerHz(30);
```

---

## GenericAudioProcessorEditor — no-UI fallback

`GenericAudioProcessorEditor` renders all APVTS parameters as a scrollable list of sliders automatically. Zero UI code. Use it to confirm parameter wiring is correct before building a custom editor.

```cpp
juce::AudioProcessorEditor* MyProcessor::createEditor()
{
    return new juce::GenericAudioProcessorEditor(*this);
}

bool MyProcessor::hasEditor() const { return true; }
```

> **JUCE 8 note:** `GenericAudioProcessorEditor` in JUCE 8 respects `ParameterGroup` — if you organize APVTS params into groups, the generic editor renders collapsible group headers. No change needed in JUCE 7; groups are simply ignored there.

---

## Quick-reference checklist

- [ ] APVTS declared in processor header and constructed with `createParameterLayout()`
- [ ] One `AudioParameterFloat` per Airwindows A-Z param, `NormalisableRange(0.0f, 1.0f)`
- [ ] Slider (or other widget) declared BEFORE its attachment in the editor class
- [ ] Attachment constructed in editor constructor initializer list: `attachment(apvts, "id", widget)`
- [ ] `addAndMakeVisible` called for every widget in the constructor
- [ ] `resized()` sets bounds for all widgets
- [ ] Timer started for any custom paint components: `startTimerHz(30)`
- [ ] `GenericAudioProcessorEditor` used for initial testing before building a custom editor
- [ ] `ComboBox` item IDs start at 1 (not 0) when using `ComboBoxAttachment`
- [ ] `TabbedComponent` panels passed with `owner=true` so tabs manage panel lifetime
