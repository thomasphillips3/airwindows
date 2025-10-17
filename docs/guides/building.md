# Building Airwindows Plugins

This guide covers building Airwindows plugins from source for all supported platforms.

## Prerequisites

### All Platforms

- Git (for cloning the repository)
- VST2 SDK (if building VST plugins)
- Text editor or IDE

### Linux

- GCC 7+ or Clang 6+
- CMake 3.10 or higher
- Make
- VST2 SDK headers

```bash
# Ubuntu/Debian
sudo apt-get install build-essential cmake git

# Fedora/RHEL
sudo dnf install gcc gcc-c++ cmake git

# Arch
sudo pacman -S base-devel cmake git
```

### macOS

- Xcode 12 or higher
- Xcode Command Line Tools
- macOS 10.13 or higher

```bash
# Install Xcode Command Line Tools
xcode-select --install
```

### Windows

- Visual Studio 2019 or higher
- Windows 10 or higher
- VST2 SDK

## Building on Linux

### Clone the Repository

```bash
git clone https://github.com/airwindows/airwindows.git
cd airwindows
```

### Build All Plugins

```bash
cd plugins/LinuxVST
mkdir -p build
cd build
cmake ..
make -j$(nproc)
```

This will build all plugins in parallel using all available CPU cores.

### Build Specific Plugin

```bash
cd plugins/LinuxVST
mkdir -p build
cd build
cmake ..
make Console9Channel  # Replace with desired plugin name
```

### Install Plugins

**System-wide installation:**

```bash
sudo make install
# Plugins will be installed to /usr/lib/vst/
```

**User installation:**

```bash
# Create VST directory if it doesn't exist
mkdir -p ~/.vst

# Copy plugins
cp *.so ~/.vst/
```

**Custom location:**

```bash
# Set custom VST path in your DAW or copy plugins there
cp *.so /path/to/your/vst/directory/
```

### Common Issues

**Issue: CMake can't find VST SDK**

```bash
# Download VST2 SDK and set path
export VST2_SDK_PATH=/path/to/vstsdk2.4
cmake .. -DVST2_SDK_PATH=$VST2_SDK_PATH
```

**Issue: Plugins not showing in DAW**

- Check DAW's VST plugin paths
- Rescan plugins in DAW
- Verify file permissions (`chmod +x *.so`)

## Building on macOS

### VST Plugins

```bash
cd plugins/MacVST
```

#### Using Xcode

1. Open the `.xcodeproj` file for the desired plugin
2. Select your target (Debug or Release)
3. Build (⌘B)
4. Plugin will be in `build/Release/`

#### Command Line

```bash
# Build with xcodebuild
xcodebuild -project PluginName.xcodeproj -configuration Release
```

#### Install

```bash
# Copy to system VST directory
sudo cp -r build/Release/PluginName.vst /Library/Audio/Plug-Ins/VST/

# Or user directory
cp -r build/Release/PluginName.vst ~/Library/Audio/Plug-Ins/VST/
```

### Audio Unit Plugins

```bash
cd plugins/MacAU
```

1. Open the `.xcodeproj` file
2. Build (⌘B)
3. Plugin will be installed automatically during build

**Verify installation:**

```bash
auval -a  # List all AUs
auval -v aufx PluginCode Plgn  # Validate specific plugin
```

### Code Signing

For distribution:

```bash
# Sign VST
codesign --deep --force --verify --verbose --sign "Developer ID" PluginName.vst

# Sign AU
codesign --deep --force --verify --verbose --sign "Developer ID" PluginName.component

# Verify
codesign --verify --deep --verbose=2 PluginName.vst
```

### Common Issues

**Issue: Xcode build fails**

- Update to latest Xcode
- Clean build folder (⌘⇧K)
- Delete `DerivedData` folder

**Issue: AU not validated**

```bash
# Kill audio component registration
killall -9 AudioComponentRegistrar

# Re-register
auval -v aufx PluginCode Plgn
```

## Building on Windows

### Using Visual Studio

1. Navigate to `plugins/WinVST/`
2. Open `PluginName/PluginName.vcxproj` in Visual Studio
3. Select configuration (Release/x64 recommended)
4. Build → Build Solution (F7)
5. DLL will be in `x64/Release/`

### Install

```bash
# Copy to VST directory
copy x64\Release\PluginName.dll "C:\Program Files\VstPlugins\"

# Or user directory
copy x64\Release\PluginName.dll "%USERPROFILE%\Documents\VstPlugins\"
```

### Batch Building

Create a batch file to build multiple plugins:

```batch
@echo off
for /d %%D in (*) do (
    if exist "%%D\%%D.vcxproj" (
        echo Building %%D...
        msbuild "%%D\%%D.vcxproj" /p:Configuration=Release /p:Platform=x64
    )
)
```

### Common Issues

**Issue: Missing VST SDK**

- Download VST2 SDK
- Update project properties:
  - C/C++ → Additional Include Directories
  - Add VST SDK path

**Issue: Build errors**

- Ensure Windows SDK is installed
- Update Visual Studio to latest version
- Check Platform Toolset in project properties

## Build Configurations

### Debug vs Release

**Debug:**
- Includes debugging symbols
- Larger file size
- Slower performance
- Useful for development

**Release:**
- Optimized code
- Smaller file size
- Best performance
- For distribution

### Optimization Flags

Linux/Mac (CMake):

```cmake
# Add to CMakeLists.txt
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
```

## Testing Plugins

### Basic Testing

1. Load plugin in DAW
2. Process test audio
3. Check for:
   - Crashes
   - Audio artifacts
   - Parameter response
   - CPU usage

### Validation Tools

**macOS Audio Units:**

```bash
auval -v aufx PluginCode Plgn
```

**VST Validator:**

Use your DAW's built-in VST validator or tools like:
- Reaper ReaValidate
- VST Plugin Checker

## Continuous Integration

### GitHub Actions Example

```yaml
name: Build Plugins

on: [push, pull_request]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: sudo apt-get install build-essential cmake
      - name: Build
        run: |
          cd plugins/LinuxVST
          mkdir build && cd build
          cmake ..
          make -j
```

## Troubleshooting

### General Issues

**Plugins not loading:**
- Check file permissions
- Verify architecture (32-bit vs 64-bit)
- Check DAW plugin paths

**Build fails:**
- Check dependencies
- Update build tools
- Clean build directory

**Audio artifacts:**
- Check sample rate handling
- Verify buffer sizes
- Test at different sample rates

### Getting Help

- **GitHub Issues**: [Report bugs](https://github.com/airwindows/airwindows/issues)
- **Forum**: [Community discussion](https://forum.airwindows.com)
- **Documentation**: [Read the docs](../index.html)

## Advanced Topics

### Custom VST SDK Location

```bash
# Linux/Mac
cmake .. -DVST2_SDK_PATH=/custom/path/to/vstsdk

# Windows (in Visual Studio)
# Project Properties → C/C++ → Additional Include Directories
```

### Cross-Compilation

#### Linux to Windows

```bash
# Install MinGW
sudo apt-get install mingw-w64

# Configure CMake
cmake .. -DCMAKE_TOOLCHAIN_FILE=windows-toolchain.cmake
```

### Optimization

**Enable link-time optimization:**

```bash
cmake .. -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=TRUE
```

**Profile-guided optimization:**

1. Build with profiling enabled
2. Run typical usage
3. Rebuild with profile data

## Resources

- **Official Repo**: [github.com/airwindows/airwindows](https://github.com/airwindows/airwindows)
- **VST SDK**: [Steinberg VST SDK](https://www.steinberg.net/vst3sdk)
- **CMake Docs**: [cmake.org](https://cmake.org)

---

*Last updated: 2024*  
*See also: [Getting Started](getting-started.md), [Contributing](contributing.md)*

