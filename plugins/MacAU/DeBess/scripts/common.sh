#!/bin/bash
# BBM_SCRIPT_VERSION=1.1.0
# Common build functions for JUCE projects
set -e

# Ensure Homebrew paths are in PATH (GUI apps don't inherit shell PATH)
if [ -d "/opt/homebrew/bin" ]; then
  export PATH="/opt/homebrew/bin:$PATH"
fi
if [ -d "/usr/local/bin" ]; then
  export PATH="/usr/local/bin:$PATH"
fi

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[1;33m'
export BLUE='\033[0;34m'
export NC='\033[0m'

print_error() { echo -e "${RED}ERROR: $1${NC}" >&2; }
print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_info() { echo -e "${YELLOW}→ $1${NC}"; }
print_header() { echo -e "${BLUE}═══ $1 ═══${NC}"; }

get_project_root() {
  local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  echo "$(cd "$script_dir/.." && pwd)"
}

detect_project_kind() {
  local project_root="$1"
  if [ -f "$project_root/CMakeLists.txt" ] || [ -f "$project_root/CmakeLists.txt" ] || [ -f "$project_root/cmakelists.txt" ]; then
    echo "cmake"
    return 0
  fi
  shopt -s nullglob
  local jucers=("$project_root"/*.jucer)
  shopt -u nullglob
  if [ ${#jucers[@]} -gt 0 ]; then
    echo "projucer"
    return 0
  fi
  if [ -d "$project_root/Builds/MacOSX" ]; then
    shopt -s nullglob
    local xcodes=("$project_root/Builds/MacOSX"/*.xcodeproj)
    shopt -u nullglob
    if [ ${#xcodes[@]} -gt 0 ]; then
      echo "projucer"
      return 0
    fi
  fi
  # Check for root-level .xcodeproj (Airwindows style)
  shopt -s nullglob
  local root_xcodes=("$project_root"/*.xcodeproj)
  shopt -u nullglob
  if [ ${#root_xcodes[@]} -gt 0 ]; then
    echo "airwindows"
    return 0
  fi
  echo "unknown"
}

find_cmake() {
  local cmake_paths=(
    "/opt/homebrew/bin/cmake"
    "/usr/local/bin/cmake"
    "/Applications/CMake.app/Contents/bin/cmake"
    "$(which cmake 2>/dev/null)"
  )
  for path in "${cmake_paths[@]}"; do
    if [ -n "$path" ] && [ -x "$path" ]; then
      echo "$path"
      return 0
    fi
  done
  print_error "CMake not found. Install via: brew install cmake"
  return 1
}

get_cmake() {
  if [ -z "$CMAKE_PATH" ]; then
    CMAKE_PATH=$(find_cmake)
    export CMAKE_PATH
  fi
  echo "$CMAKE_PATH"
}

find_projucer() {
  local projucer_paths=(
    "/Applications/Projucer.app/Contents/MacOS/Projucer"
    "/Applications/JUCE/Projucer.app/Contents/MacOS/Projucer"
    "$(which Projucer 2>/dev/null)"
  )
  for path in "${projucer_paths[@]}"; do
    if [ -n "$path" ] && [ -x "$path" ]; then
      echo "$path"
      return 0
    fi
  done
  print_error "Projucer not found. Install JUCE from https://juce.com"
  return 1
}

get_projucer() {
  if [ -z "$PROJUCER_PATH" ]; then
    PROJUCER_PATH=$(find_projucer)
    export PROJUCER_PATH
  fi
  echo "$PROJUCER_PATH"
}

get_cmake_project_name_and_version() {
  local project_root="$1"
  local cmake_file=""
  if [ -f "$project_root/CMakeLists.txt" ]; then
    cmake_file="$project_root/CMakeLists.txt"
  elif [ -f "$project_root/CmakeLists.txt" ]; then
    cmake_file="$project_root/CmakeLists.txt"
  elif [ -f "$project_root/cmakelists.txt" ]; then
    cmake_file="$project_root/cmakelists.txt"
  else
    print_error "CMakeLists.txt not found"
    return 1
  fi

  # Parse: project(Name VERSION x.y.z)
  local line
  line=$(grep -i "^[[:space:]]*project(" "$cmake_file" | head -n 1)
  if [ -z "$line" ]; then
    print_error "Could not find project(...) line in CMakeLists.txt"
    return 1
  fi

  local name
  local version
  name=$(echo "$line" | sed -E 's/^[[:space:]]*project\(([A-Za-z0-9_+-]+).*/\1/' | tr -d '[:space:]')
  version=$(echo "$line" | sed -E 's/.*VERSION[[:space:]]+([0-9.]+).*/\1/' | tr -d '[:space:])')

  if [ -z "$name" ] || [ -z "$version" ]; then
    print_error "Could not parse project name/version from: $line"
    return 1
  fi

  echo "$name|$version"
}

get_projucer_project_name() {
  local project_root="$1"
  shopt -s nullglob
  local jucers=("$project_root"/*.jucer)
  shopt -u nullglob
  if [ ${#jucers[@]} -eq 0 ]; then
    print_error "No .jucer file found at project root"
    return 1
  fi

  local first_line
  first_line=$(grep -E "<JUCERPROJECT" "${jucers[0]}" | head -n 1)
  if [ -z "$first_line" ]; then
    print_error "Could not find <JUCERPROJECT ...> in ${jucers[0]}"
    return 1
  fi

  local name
  name=$(echo "$first_line" | sed -E 's/.*name="([^"]+)".*/\\1/')
  if [ -z "$name" ] || [ "$name" = "$first_line" ]; then
    # fallback to folder name
    name=$(basename "$project_root")
  fi
  echo "$name"
}

get_juce_version_from_defines() {
  local project_root="$1"
  local defines="$project_root/JuceLibraryCode/JucePluginDefines.h"
  if [ ! -f "$defines" ]; then
    echo ""
    return 0
  fi
  local line
  line=$(grep -E "^[[:space:]]*#define[[:space:]]+JucePlugin_VersionString" "$defines" | head -n 1)
  if [ -z "$line" ]; then
    echo ""
    return 0
  fi
  # Extract "1.2.3"
  echo "$line" | sed -E 's/.*JucePlugin_VersionString[[:space:]]+"([^"]+)".*/\\1/'
}

get_projucer_project_name_and_version() {
  local project_root="$1"
  local name
  local version
  name=$(get_projucer_project_name "$project_root")
  version=$(get_juce_version_from_defines "$project_root")
  if [ -z "$version" ]; then
    version="0.0.0"
  fi
  echo "$name|$version"
}

get_airwindows_project_name_and_version() {
  local project_root="$1"
  local name
  local version="0.0.0"
  
  # Extract project name from folder name
  name=$(basename "$project_root")
  
  # Try to extract version from *Version.h file at root
  shopt -s nullglob
  local version_files=("$project_root"/*[Vv]ersion.h)
  shopt -u nullglob
  if [ ${#version_files[@]} -gt 0 ]; then
    local version_file="${version_files[0]}"
    # Look for version pattern like: #define VERSION "1.0.0" or similar
    local extracted
    extracted=$(grep -E '#define.*[Vv]ersion.*"[0-9]+\\.[0-9]+(\\.[ 0-9]+)?"' "$version_file" | head -n 1 | sed -E 's/.*"([0-9]+\\.[0-9]+(\\.[ 0-9]+)?)".*/\\1/' || true)
    if [ -n "$extracted" ]; then
      version="$extracted"
    fi
  fi
  
  # If not found at root, check source/ subdirectory
  if [ "$version" = "0.0.0" ] && [ -d "$project_root/source" ]; then
    shopt -s nullglob
    local source_version_files=("$project_root/source"/*[Vv]ersion.h)
    shopt -u nullglob
    if [ ${#source_version_files[@]} -gt 0 ]; then
      local version_file="${source_version_files[0]}"
      local extracted
      extracted=$(grep -E '#define.*[Vv]ersion.*"[0-9]+\\.[0-9]+(\\.[ 0-9]+)?"' "$version_file" | head -n 1 | sed -E 's/.*"([0-9]+\\.[0-9]+(\\.[ 0-9]+)?)".*/\\1/' || true)
      if [ -n "$extracted" ]; then
        version="$extracted"
      fi
    fi
  fi
  
  echo "$name|$version"
}

get_project_name_and_version() {
  local project_root="$1"
  local kind
  kind=$(detect_project_kind "$project_root")
  if [ "$kind" = "cmake" ]; then
    get_cmake_project_name_and_version "$project_root"
    return $?
  fi
  if [ "$kind" = "projucer" ]; then
    get_projucer_project_name_and_version "$project_root"
    return $?
  fi
  if [ "$kind" = "airwindows" ]; then
    get_airwindows_project_name_and_version "$project_root"
    return $?
  fi
  print_error "Could not detect project type (expected CMakeLists.txt, *.jucer, or *.xcodeproj)"
  return 1
}

sanitize_name() {
  # Replace spaces with hyphens (also collapse multiple spaces)
  echo "$1" | tr ' ' '-' | tr -s '-'
}

clean_build() {
  local project_root="$1"
  local build_dir="$project_root/build"
  
  print_info "Cleaning build directory..."
  rm -rf "$build_dir"
  mkdir -p "$build_dir"
  print_success "Build directory cleaned"
}

clean_build_projucer() {
  local project_root="$1"
  local build_dir="$project_root/Builds/MacOSX/build"
  print_info "Cleaning Xcode build directory..."
  rm -rf "$build_dir"
  print_success "Xcode build directory cleaned"
}

clean_build_airwindows() {
  local project_root="$1"
  local build_dir="$project_root/build"
  print_info "Cleaning Airwindows build directory..."
  rm -rf "$build_dir"
  print_success "Build directory cleaned"
}

configure_cmake() {
  local project_root="$1"
  local build_type="$2"
  local cmake_cmd
  cmake_cmd=$(get_cmake)
  
  print_info "Configuring CMake for $build_type build..."
  print_info "Using CMake: $cmake_cmd"
  
  export BBM_BUILD_TYPE="$build_type"
  "$cmake_cmd" -S "$project_root" -B "$project_root/build" -DCMAKE_BUILD_TYPE=Release
  print_success "CMake configured"
}

build_plugin() {
  local project_root="$1"
  local cmake_cmd
  cmake_cmd=$(get_cmake)
  
  print_info "Building..."
  "$cmake_cmd" --build "$project_root/build" --config Release -j$(sysctl -n hw.ncpu)
  print_success "Build completed"
}

resave_jucer_project() {
  local project_root="$1"
  
  # Find .jucer file
  shopt -s nullglob
  local jucers=("$project_root"/*.jucer)
  shopt -u nullglob
  
  if [ ${#jucers[@]} -eq 0 ]; then
    print_error "No .jucer file found in project root"
    return 1
  fi
  
  local jucer_file="${jucers[0]}"
  local projucer_cmd
  projucer_cmd=$(get_projucer)
  
  print_info "Generating Xcode project from $(basename "$jucer_file")..."
  "$projucer_cmd" --resave "$jucer_file"
  print_success "Xcode project generated"
}

build_plugin_projucer() {
  local project_root="$1"
  local build_type="$2"

  # Always regenerate Xcode project from .jucer to keep it in sync
  print_info "Regenerating Xcode project from .jucer file..."
  resave_jucer_project "$project_root" || return 1

  # Find the generated Xcode project
  local xcodeproj=""
  shopt -s nullglob
  local xcodes=("$project_root/Builds/MacOSX"/*.xcodeproj)
  shopt -u nullglob
  if [ ${#xcodes[@]} -gt 0 ]; then
    xcodeproj="${xcodes[0]}"
  fi

  if [ -z "$xcodeproj" ]; then
    print_error "No .xcodeproj found under Builds/MacOSX after generating"
    return 1
  fi

  print_info "Building Xcode project (all targets)..."
  export BBM_BUILD_TYPE="$build_type"
  xcodebuild -project "$xcodeproj" -configuration Release -alltargets build
  print_success "Xcode build completed"
}

build_plugin_airwindows() {
  local project_root="$1"
  local build_type="$2"

  local xcodeproj=""
  shopt -s nullglob
  local xcodes=("$project_root"/*.xcodeproj)
  shopt -u nullglob
  if [ ${#xcodes[@]} -gt 0 ]; then
    xcodeproj="${xcodes[0]}"
  fi

  if [ -z "$xcodeproj" ]; then
    print_error "No .xcodeproj found at project root"
    return 1
  fi

  print_info "Building Airwindows Xcode project..."
  export BBM_BUILD_TYPE="$build_type"
  # Legacy Airwindows: override i386 (deprecated), MACOSX_DEPLOYMENT_TARGET (10.4 unsupported)
  xcodebuild -project "$xcodeproj" -configuration Release -sdk macosx -alltargets build ARCHS="x86_64 arm64" MACOSX_DEPLOYMENT_TARGET=10.13
  print_success "Xcode build completed"
}

package_plugins() {
  local project_root="$1"
  local project_name="$2"
  local version="$3"
  local build_type="$4"
  local output_dir="$project_root/releases/$build_type/$version"
  
  print_info "Packaging plugins..."
  mkdir -p "$output_dir"
  
  local safe_name
  safe_name=$(sanitize_name "$project_name")
  
  local kind
  kind=$(detect_project_kind "$project_root")

  local vst3s=()
  local aus=()
  local aaxs=()
  local apps=()

  if [ "$kind" = "cmake" ]; then
    shopt -s nullglob
    local artefacts_dirs=("$project_root"/build/*_artefacts/Release)
    shopt -u nullglob

    if [ ${#artefacts_dirs[@]} -eq 0 ]; then
      print_info "No JUCE artefacts directory found under build/*_artefacts/Release (skipping packaging)"
      echo "$output_dir"
      return 0
    fi

    local artefacts="${artefacts_dirs[0]}"

    shopt -s nullglob
    vst3s=("$artefacts"/VST3/*.vst3)
    aus=("$artefacts"/AU/*.component)
    aaxs=("$artefacts"/AAX/*.aaxplugin)
    apps=("$artefacts"/Standalone/*.app)
    shopt -u nullglob
  elif [ "$kind" = "projucer" ]; then
    # Projucer/Xcode build output
    local artefacts="$project_root/Builds/MacOSX/build/Release"
    if [ ! -d "$artefacts" ]; then
      print_info "No Xcode Release build output found at Builds/MacOSX/build/Release (skipping packaging)"
      echo "$output_dir"
      return 0
    fi

    # Use find because Projucer output layout varies (may nest under products folder).
    local first_vst3
    local first_au
    local first_aax
    local first_app
    first_vst3=$(find "$artefacts" -maxdepth 4 -name "*.vst3" -print -quit 2>/dev/null || true)
    first_au=$(find "$artefacts" -maxdepth 4 -name "*.component" -print -quit 2>/dev/null || true)
    first_aax=$(find "$artefacts" -maxdepth 4 -name "*.aaxplugin" -print -quit 2>/dev/null || true)
    first_app=$(find "$artefacts" -maxdepth 4 -name "*.app" -print -quit 2>/dev/null || true)
    if [ -n "$first_vst3" ]; then vst3s=("$first_vst3"); fi
    if [ -n "$first_au" ]; then aus=("$first_au"); fi
    if [ -n "$first_aax" ]; then aaxs=("$first_aax"); fi
    if [ -n "$first_app" ]; then apps=("$first_app"); fi
  elif [ "$kind" = "airwindows" ]; then
    # Airwindows build output
    local artefacts="$project_root/build/Release"
    if [ ! -d "$artefacts" ]; then
      print_info "No Airwindows Release build output found at build/Release (skipping packaging)"
      echo "$output_dir"
      return 0
    fi

    # Use find because Airwindows output may vary (VST2, AU, etc.)
    local first_vst
    local first_vst3
    local first_au
    local first_aax
    local first_app
    first_vst=$(find "$artefacts" -maxdepth 4 -name "*.vst" -print -quit 2>/dev/null || true)
    first_vst3=$(find "$artefacts" -maxdepth 4 -name "*.vst3" -print -quit 2>/dev/null || true)
    first_au=$(find "$artefacts" -maxdepth 4 -name "*.component" -print -quit 2>/dev/null || true)
    first_aax=$(find "$artefacts" -maxdepth 4 -name "*.aaxplugin" -print -quit 2>/dev/null || true)
    first_app=$(find "$artefacts" -maxdepth 4 -name "*.app" -print -quit 2>/dev/null || true)
    # Prefer VST2 (.vst) for Airwindows, but also support VST3 if available
    if [ -n "$first_vst" ]; then vst3s=("$first_vst"); fi
    if [ -n "$first_vst3" ]; then vst3s=("$first_vst3"); fi
    if [ -n "$first_au" ]; then aus=("$first_au"); fi
    if [ -n "$first_aax" ]; then aaxs=("$first_aax"); fi
    if [ -n "$first_app" ]; then apps=("$first_app"); fi
  fi
  
  if [ ${#vst3s[@]} -gt 0 ]; then
    local base
    base=$(basename "${vst3s[0]}")
    (cd "$(dirname "${vst3s[0]}")" && zip -r "$output_dir/${safe_name}-VST3-${version}-${build_type}.zip" "$base")
    print_success "VST3 packaged"
  fi
  
  if [ ${#aus[@]} -gt 0 ]; then
    local base
    base=$(basename "${aus[0]}")
    (cd "$(dirname "${aus[0]}")" && zip -r "$output_dir/${safe_name}-AU-${version}-${build_type}.zip" "$base")
    print_success "AU packaged"
  fi
  
  if [ ${#aaxs[@]} -gt 0 ]; then
    local base
    base=$(basename "${aaxs[0]}")
    (cd "$(dirname "${aaxs[0]}")" && zip -r "$output_dir/${safe_name}-AAX-${version}-${build_type}.zip" "$base")
    print_success "AAX packaged"
  fi
  
  if [ ${#apps[@]} -gt 0 ]; then
    local base
    base=$(basename "${apps[0]}")
    (cd "$(dirname "${apps[0]}")" && zip -r "$output_dir/${safe_name}-Standalone-${version}-${build_type}.zip" "$base")
    print_success "Standalone packaged"
  fi
  
  print_success "Artifacts packaged to $output_dir"
  echo "$output_dir"
}