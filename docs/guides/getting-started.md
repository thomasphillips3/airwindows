# Getting Started with Airwindows

Welcome to Airwindows! This guide will help you get started with the plugin collection.

## What is Airwindows?

Airwindows is a collection of over 400 open-source audio plugins created by Chris Johnson. These plugins cover everything from essential mixing tools to creative effects and experimental processors.

### Key Features

- **Open Source** - MIT licensed, free to use
- **Cross-Platform** - Mac, Windows, and Linux
- **Unique Algorithms** - Novel DSP not found elsewhere
- **Low CPU** - Efficient code
- **Well-Documented** - Comprehensive documentation

## Quick Start

### 1. Installation

#### Download Pre-Built Plugins

Visit the [GitHub Releases](https://github.com/airwindows/airwindows/releases) page and download:

- **Mac Users**: Download Mac AU or Mac VST
- **Windows Users**: Download Windows VST
- **Linux Users**: Download Linux VST or build from source

#### Install Plugins

**macOS:**
```bash
# Audio Units
sudo cp -r *.component /Library/Audio/Plug-Ins/Components/

# VST
sudo cp -r *.vst /Library/Audio/Plug-Ins/VST/
```

**Windows:**
```
Copy .dll files to:
C:\Program Files\VstPlugins\
```

**Linux:**
```bash
mkdir -p ~/.vst
cp *.so ~/.vst/
```

#### Rescan Plugins

Open your DAW and rescan for new plugins. The location of this option varies by DAW:

- **Ableton Live**: Preferences → Plug-ins → Rescan
- **Reaper**: Options → Preferences → VST → Re-scan
- **Logic Pro**: Automatically detects new AUs
- **FL Studio**: Options → Manage Plugins → Find Plugins

### 2. Your First Plugins

Start with these essential plugins to understand the Airwindows sound:

#### Console9 - Mix Bus Processing

The Console system is unique to Airwindows and fundamental to the "sound".

**Setup:**
1. Add **Console9Channel** to every track (or important tracks)
2. Add **Console9Buss** to your master fader
3. Leave all settings at default (0.5)

**What it does:**
Creates space and separation in your mix through encode/decode processing.

#### PurestGain - Gain Staging

A transparent gain plugin with no artifacts.

**Setup:**
1. Add to tracks that need level adjustment
2. Adjust gain as needed
3. That's it!

**Why it's special:**
Uses bit-shifting and noise shaping for perfect gain staging.

#### Chamber - Simple Reverb

A clean, golden-ratio-based reverb.

**Setup:**
1. Create aux send
2. Add Chamber to aux track
3. Set mix to 100% wet
4. Send from source track

**Parameters:**
- Size: Room size
- Mix: Dry/wet (use 100% on aux)

### 3. Essential Plugins by Category

#### For Mixing

- **Console9** - Mix bus glue
- **PurestGain** - Transparent gain
- **BeziComp** - Transparent compression
- **SmoothEQ2** - Musical EQ
- **ToTape8** - Tape emulation
- **kStation** - Vocal reverb

#### For Mastering

- **Monitoring3** - Final output stage
- **PurestConsole** - Minimal console
- **Pressure6** - Mastering compression
- **Dark** - Dither
- **ToTape8** - Subtle warmth

#### Creative Effects

- **Galactic** - Infinite reverb
- **GlitchShifter** - Pitch shifting
- **DeRez3** - Lo-fi degradation
- **GrooveWear** - Vinyl wear
- **PitchNasty** - Extreme pitch effects

## Understanding Airwindows Philosophy

### Less is More

Many Airwindows plugins have few controls. This is intentional:

- The sweet spot is pre-dialed
- Focus on music, not endless tweaking
- Faster workflow
- Better results

### No Emulations

Airwindows doesn't try to copy specific hardware:

- Original algorithms
- Focus on musical results
- Not burdened by "accuracy"
- Free to innovate

### Open Source

All code is available:

- Learn from the source
- Modify as needed
- Understand the algorithms
- Use in your own projects

## Common Workflows

### Basic Mix Setup

```
Tracks → Console9Channel → DAW Mixer → Console9Buss → Monitoring3 → Output
```

### Vocal Chain

```
Vocal → ButterComp2 → DeEss → Channel9 → kStation (reverb send)
```

### Master Chain

```
Mix → Console9Buss → BeziComp → ToTape8 → Monitoring3
```

### Creative Processing

```
Source → DeRez3 → Galactic → GrooveWear
```

## Learning Resources

### Documentation

- **[Main Documentation](../index.html)** - Interactive plugin browser
- **[Categories](../categories/)** - Plugins by function
- **[Individual Plugins](../plugins/)** - Detailed plugin pages
- **[Airwindopedia](../../Airwindopedia.txt)** - Complete descriptions

### Video Resources

- **YouTube Channel**: [youtube.com/@airwindows](https://www.youtube.com/@airwindows)
- Each plugin has a demo video
- Tutorials and explanations

### Community

- **Forum**: [forum.airwindows.com](https://forum.airwindows.com)
- **GitHub**: [github.com/airwindows/airwindows](https://github.com/airwindows/airwindows)
- **Patreon**: [patreon.com/airwindows](https://www.patreon.com/airwindows)

## Tips for Success

### Start Simple

1. Don't try to learn all 400+ plugins at once
2. Start with recommended plugins
3. Master a few before moving on
4. Build your toolkit gradually

### Use the Documentation

- Search for specific needs
- Browse by category
- Read plugin descriptions
- Watch demo videos

### Experiment

- Airwindows encourages experimentation
- Try "wrong" settings
- Stack plugins
- Find happy accidents

### Trust Your Ears

- Meters lie, ears don't
- A/B compare everything
- Take breaks
- Check in mono

## Common Questions

### Do I need all 400+ plugins?

No! Start with 10-20 core plugins. Many serve similar purposes with different flavors.

### Which plugins are most important?

See the "Recommended" tag in the documentation. These are tried-and-true favorites.

### Can I use Airwindows with other plugins?

Absolutely! Mix and match as needed. Airwindows excels at:
- Mix bus processing (Console)
- Final output (Monitoring, dither)
- Creative effects
- Subtle enhancement

### Are these "professional quality"?

Yes! Used on major label releases, film scores, and broadcast. The open-source nature means quality, not compromise.

### How do I choose between similar plugins?

Try them! Each has subtle differences. What works depends on your source material and taste.

### Can I use these commercially?

Yes! MIT license means you can:
- Use in commercial projects
- Modify the code
- Distribute modified versions
- Just don't claim you wrote it

## Next Steps

### Recommended Learning Path

**Week 1: Basics**
- Install and test plugins
- Set up Console system
- Learn PurestGain and basic tools

**Week 2: Mixing**
- Explore EQs and filters
- Try dynamics processors
- Experiment with saturation

**Week 3: Effects**
- Add reverbs and delays
- Try stereo widening
- Explore creative effects

**Week 4: Integration**
- Build your go-to plugin list
- Create templates in your DAW
- Develop your workflow

### Building Your Plugin Folder

Create a organized plugin folder in your DAW:

```
Airwindows/
├── Mixing/
│   ├── Console9Channel
│   ├── SmoothEQ2
│   ├── BeziComp
│   └── ToTape8
├── Effects/
│   ├── ClearCoat
│   ├── Galactic
│   └── GlitchShifter
├── Mastering/
│   ├── Console9Buss
│   ├── Monitoring3
│   └── Dark
└── Utilities/
    ├── PurestGain
    ├── EveryTrim
    └── Golem
```

### Creating Templates

Save time by creating DAW templates with:
- Console system pre-loaded
- Common routing
- Favorite sends/returns
- Standard plugin chains

## Troubleshooting

### Plugins Don't Load

- Check file permissions
- Verify plugin path
- Rescan in DAW
- Check architecture (32/64-bit)

### Sound Issues

- Check sample rate
- Verify buffer size
- Test with different audio
- Update DAW

### Performance Issues

- Disable unused plugins
- Freeze tracks
- Increase buffer size
- Check CPU usage

### Getting Help

1. Check this documentation
2. Search existing issues on GitHub
3. Ask in the forum
4. Report bugs on GitHub

## Advanced Topics

Once comfortable with basics:

- **[Building from Source](building.md)**
- **[Understanding Console Systems](../categories/consoles.md)**
- **[Mastering Workflow](../categories/subtlety.md)**
- **[Sound Design](../categories/effects.md)**

## Stay Updated

Airwindows is actively developed:

- **Watch GitHub** for new releases
- **Subscribe on YouTube** for plugin demos
- **Follow on Patreon** for early access
- **Join the forum** for discussions

---

## Quick Reference

### Essential Shortcuts

- **Search**: Use documentation website search
- **Filter**: By Latest, Recommended, Basic
- **Categories**: Browse by function
- **Related**: Find similar plugins

### Plugin Naming

- **Numbers** (Console9, ToTape8): Latest version
- **"Purest"**: Transparent processing
- **"2" suffix**: Updated version
- **"k" prefix**: Reverb series

### Common Abbreviations

- **AU**: Audio Unit (Mac)
- **VST**: Virtual Studio Technology
- **DSP**: Digital Signal Processing
- **ITB**: In The Box (all digital)
- **DAW**: Digital Audio Workstation

---

*Welcome to Airwindows! Enjoy exploring the plugins!*

*Last updated: 2024*  
*See also: [Building](building.md), [Main Documentation](../index.html)*

