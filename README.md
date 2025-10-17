# Airwindows Audio Plugins

**400+ Open Source Audio DSP Plugins** - Mixing, Mastering, Effects & Sound Design

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-airwindows-blue)](https://github.com/airwindows/airwindows)
[![Website](https://img.shields.io/badge/Website-airwindows.com-green)](https://www.airwindows.com)

## 📖 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Repository Structure](#repository-structure)
- [Building Plugins](#building-plugins)
- [Plugin Categories](#plugin-categories)
- [Using the Documentation Website](#using-the-documentation-website)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## 🎵 Overview

Airwindows is a comprehensive collection of over 400 audio plugins created by Chris Johnson. These plugins cover everything from mixing and mastering tools to creative effects and experimental DSP. All plugins are:

- **Open Source** - MIT licensed, free to use and modify
- **Cross-Platform** - Available for Mac (AU/VST), Windows (VST), and Linux (VST)
- **High Quality** - Professional-grade DSP with unique algorithms
- **Well-Documented** - Extensive documentation and usage examples
- **Actively Developed** - Regular updates and new releases

### Key Features

- 🎛️ **22 Categories** - Organized by function (Consoles, Dynamics, Reverb, etc.)
- ⚡ **Efficient Code** - Optimized for low CPU usage
- 🔬 **Unique Algorithms** - Many use novel DSP techniques not found elsewhere
- 📚 **Extensive Documentation** - Detailed explanations of how each plugin works
- 🎓 **Learning Resource** - Excellent for understanding audio DSP concepts

## 🚀 Quick Start

### Using Pre-Built Plugins

1. Visit the [Releases Page](https://github.com/airwindows/airwindows/releases)
2. Download the appropriate package for your platform
3. Extract and copy to your plugin directory
4. Rescan plugins in your DAW

### Building from Source

```bash
# Clone the repository
git clone https://github.com/airwindows/airwindows.git
cd airwindows

# Build Linux VST plugins
cd plugins/LinuxVST
mkdir build && cd build
cmake ..
make

# Build on Mac (see docs/guides/building.md for detailed instructions)
# Build on Windows (see docs/guides/building.md for detailed instructions)
```

See [Building Plugins](#building-plugins) for platform-specific instructions.

## 📚 Documentation

### Interactive Documentation Website

The repository includes a comprehensive documentation system:

```bash
# Open the documentation website
open docs/index.html
# or on Linux: xdg-open docs/index.html
# or on Windows: start docs/index.html
```

The documentation website provides:

- **Plugin Browser** - Search and filter all 400+ plugins
- **Category Navigation** - Browse plugins by function
- **Detailed Plugin Pages** - Full descriptions, parameters, and usage examples
- **Signal Flow Diagrams** - Visual representations of how plugins work
- **Related Plugins** - Discover similar plugins

### Documentation Files

- **[Airwindopedia.txt](Airwindopedia.txt)** - Complete plugin descriptions from original blog posts
- **[what.txt](what.txt)** - Quick reference with one-line descriptions
- **[docs/plugins/](docs/plugins/)** - Individual markdown files for each plugin
- **[docs/categories/](docs/categories/)** - Category-specific documentation
- **[docs/guides/](docs/guides/)** - Building and usage guides

## 📁 Repository Structure

```
airwindows/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── Airwindopedia.txt                  # Complete plugin documentation
├── what.txt                           # Plugin quick reference
│
├── docs/                              # Documentation system
│   ├── index.html                     # Main documentation website
│   ├── styles.css                     # Website styles
│   ├── app.js                         # Interactive functionality
│   ├── data/                          # Plugin data (JSON)
│   │   ├── plugins.json              # All plugin metadata
│   │   └── categories.json           # Category information
│   ├── categories/                    # Category documentation
│   ├── plugins/                       # Individual plugin docs
│   ├── images/                        # Documentation images
│   └── guides/                        # Usage and build guides
│
├── plugins/                           # Plugin source code
│   ├── LinuxVST/                     # Linux VST builds
│   │   ├── CMakeLists.txt
│   │   ├── README.md
│   │   └── src/                      # Plugin source code (400+ plugins)
│   │       ├── Acceleration/
│   │       ├── Console9Channel/
│   │       └── ...                   # All plugin folders
│   │
│   ├── MacVST/                       # Mac VST projects
│   ├── MacAU/                        # Mac Audio Unit projects
│   ├── MacSignedVST/                 # Signed Mac VST
│   ├── MacSignedAU/                  # Signed Mac AU
│   ├── WinVST/                       # Windows VST projects
│   │
│   └── Templates/                    # Plugin templates
│       ├── AirwindowsAUTemplate.zip
│       ├── AirwindowsMacVSTTemplate.zip
│       └── AirwindowsWinVSTTemplate.zip
│
└── parse_data.py                      # Data parsing script
```

## 🔧 Building Plugins

### Linux (VST)

```bash
cd plugins/LinuxVST
mkdir -p build && cd build
cmake ..
make

# Install to system plugin directory
sudo make install

# Or copy manually
cp *.so ~/.vst/
```

**Requirements:**
- GCC or Clang
- CMake 3.10+
- VST2 SDK headers

### macOS (VST/AU)

```bash
# VST builds
cd plugins/MacVST
# Open .xcodeproj files in Xcode

# AU builds  
cd plugins/MacAU
# Open .xcodeproj files in Xcode

# Build and install through Xcode
```

**Requirements:**
- Xcode 12+
- macOS 10.13+
- VST2 SDK (for VST builds)

### Windows (VST)

```
1. Open Visual Studio
2. Load plugins/WinVST/{PluginName}/{PluginName}.vcxproj
3. Build for Release/x64
4. Copy .dll files to C:\Program Files\VstPlugins\
```

**Requirements:**
- Visual Studio 2019+
- Windows 10+
- VST2 SDK

For detailed build instructions, see [docs/guides/building.md](docs/guides/building.md).

## 🎛️ Plugin Categories

Plugins are organized into 22 functional categories:

### Mixing & Mastering
- **Consoles** (44 plugins) - Mix bus processing and analog console emulation
- **Dynamics** (31 plugins) - Compressors, limiters, gates, and expanders
- **Filter** (42 plugins) - EQs, filters, and tone shaping
- **Clipping** (8 plugins) - Loudness maximization and peak control
- **Dithers** (23 plugins) - Dithering and wordlength reduction

### Creative Effects
- **Reverb** (32 plugins) - From small rooms to infinite spaces
- **Ambience** (25 plugins) - Delays, echoes, and spatial effects
- **Distortion** (13 plugins) - Drive, saturation, and distortion
- **Saturation** (16 plugins) - Subtle harmonic enhancement
- **Effects** (27 plugins) - Modulation, pitch shifting, and sound design

### Tone Shaping
- **Brightness** (24 plugins) - High-frequency enhancement and control
- **Bass** (10 plugins) - Bass enhancement and sub generation
- **Tone Color** (15 plugins) - Console-style character addition
- **Subtlety** (19 plugins) - Mastering-grade subtle processing

### Specialized Tools
- **Amp Sims** (14 plugins) - Guitar and bass amplifier simulation
- **Biquads** (9 plugins) - Flexible filter building blocks
- **Lo-Fi** (17 plugins) - Bit crushing and vintage digital effects
- **Noise** (8 plugins) - Noise generation and texture
- **Stereo** (11 plugins) - Stereo widening and M/S processing
- **Tape** (10 plugins) - Magnetic tape emulation
- **Utility** (34 plugins) - Gain, metering, and routing tools
- **XYZ Filters** (23 plugins) - Experimental character filters

## 🌐 Using the Documentation Website

The documentation website is a single-page application that provides:

### Features

1. **Search** - Real-time search across all plugins
2. **Filtering** - Filter by Latest, Recommended, or Basic tags
3. **Category Browser** - Browse by functional category
4. **Plugin Details** - Comprehensive information for each plugin:
   - Full description from Airwindopedia
   - Parameter explanations
   - Signal flow diagrams
   - Related plugins
   - Links to source code
5. **Dark/Light Theme** - Toggle between themes
6. **Responsive Design** - Works on desktop, tablet, and mobile

### Navigation

- **Home** - Featured plugins and category overview
- **Categories** - Browse all 22 categories
- **All Plugins** - Complete plugin list with filtering
- **Search** - Type to search by name, category, or description

### Keyboard Shortcuts

- `/` - Focus search bar
- `Esc` - Clear search
- `←` - Go back

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues

- Bug reports
- Feature requests
- Documentation improvements
- Build problems

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Documentation Contributions

- Improve plugin descriptions
- Add usage examples
- Create tutorials
- Fix typos and clarifications

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**In short**: You can use, modify, and distribute these plugins freely, including in commercial projects. Attribution is appreciated but not required.

## 💬 Support

### Resources

- **Website**: [airwindows.com](https://www.airwindows.com)
- **GitHub**: [github.com/airwindows/airwindows](https://github.com/airwindows/airwindows)
- **Patreon**: [patreon.com/airwindows](https://www.patreon.com/airwindows)
- **YouTube**: [youtube.com/@airwindows](https://www.youtube.com/@airwindows)

### Getting Help

1. Check the [documentation website](docs/index.html)
2. Read [Airwindopedia.txt](Airwindopedia.txt) for detailed explanations
3. Search [existing GitHub issues](https://github.com/airwindows/airwindows/issues)
4. Join community discussions on the forum

### Supporting Development

If you find these plugins useful, consider:

- ⭐ Starring the repository
- 💰 Supporting on [Patreon](https://www.patreon.com/airwindows)
- 📢 Sharing with others
- 🐛 Reporting bugs and issues
- 📝 Contributing documentation

---

## 🎓 For AI Training & Learning

This repository is specifically documented for:

- **Learning Audio DSP** - Clear explanations of algorithms and techniques
- **AI Training** - Structured, comprehensive documentation
- **Code Examples** - Well-commented, readable source code
- **DSP Research** - Novel algorithms and approaches

All plugins include:
- Detailed descriptions of the algorithm
- Explanation of parameters
- Use cases and applications
- Signal flow information
- Source code with comments

---

**Made with ❤️ by Chris Johnson**

*Last updated: 2024*

