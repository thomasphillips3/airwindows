#!/usr/bin/env python3
"""
Generate individual plugin documentation pages
Prioritizes Latest + Recommended plugins
"""

import json
import re
from pathlib import Path

def create_signal_flow_diagram(plugin):
    """Generate a Mermaid diagram based on plugin category"""
    category = plugin['categories'][0] if plugin['categories'] else 'Utility'
    
    diagrams = {
        'Consoles': """```mermaid
graph LR
    A[Input] --> B[Encode]
    B --> C[Summing]
    C --> D[Decode]
    D --> E[Output]
    style B fill:#6366f1
    style D fill:#f59e0b
```""",
        'Dynamics': """```mermaid
graph LR
    A[Input] --> B[Detector]
    B --> C[Gain Computer]
    C --> D[Gain Reduction]
    A --> D
    D --> E[Output]
    style C fill:#6366f1
    style D fill:#f59e0b
```""",
        'Reverb': """```mermaid
graph LR
    A[Input] --> B[Early Reflections]
    A --> C[Diffusion]
    C --> D[Feedback]
    D --> C
    B --> E[Mix]
    C --> E
    A --> E
    E --> F[Output]
    style C fill:#6366f1
    style D fill:#8b5cf6
```""",
        'Filter': """```mermaid
graph LR
    A[Input] --> B[Filter Stage]
    B --> C[Resonance]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```""",
        'Tape': """```mermaid
graph LR
    A[Input] --> B[Bias]
    B --> C[Saturation]
    C --> D[Head Bump]
    D --> E[Flutter]
    E --> F[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```""",
        'Distortion': """```mermaid
graph LR
    A[Input] --> B[Drive]
    B --> C[Waveshaping]
    C --> D[Filtering]
    D --> E[Output]
    style C fill:#f59e0b
```""",
        'Saturation': """```mermaid
graph LR
    A[Input] --> B[Harmonic Generation]
    B --> C[Soft Clipping]
    C --> D[Output]
    style B fill:#6366f1
    style C fill:#f59e0b
```""",
    }
    
    return diagrams.get(category, """```mermaid
graph LR
    A[Input] --> B[Processing]
    B --> C[Output]
    style B fill:#6366f1
```""")

def create_plugin_page(plugin):
    """Generate a complete plugin documentation page"""
    
    tags_display = []
    if plugin['is_latest']:
        tags_display.append('![Latest](https://img.shields.io/badge/-Latest-10b981)')
    if plugin['is_recommended']:
        tags_display.append('![Recommended](https://img.shields.io/badge/-Recommended-6366f1)')
    if plugin['is_basic']:
        tags_display.append('![Basic](https://img.shields.io/badge/-Basic-f59e0b)')
    
    tags_line = ' '.join(tags_display) if tags_display else ''
    
    content = f"""# {plugin['name']}

{tags_line}

## Quick Info

| | |
|---|---|
| **Category** | {', '.join(plugin['categories'])} |
| **Type** | {plugin['categories'][0] if plugin['categories'] else 'Utility'} |
| **Status** | {'Latest Release' if plugin['is_latest'] else 'Stable'} |

## Description

{plugin['description']}

"""
    
    # Add detailed description if available
    if plugin.get('full_description'):
        content += f"""## Detailed Overview

{plugin['full_description']}

"""
    
    # Add signal flow
    content += f"""## Signal Flow

{create_signal_flow_diagram(plugin)}

## How It Works

"""
    
    # Category-specific how it works
    category = plugin['categories'][0] if plugin['categories'] else 'Utility'
    
    how_it_works = {
        'Consoles': f"{plugin['name']} is part of the Airwindows Console system. Use the Channel version on tracks and the Buss version on the master to create a unique summing environment that adds space and dimension to your mix.",
        'Dynamics': f"{plugin['name']} controls dynamics through {'compression' if 'Comp' in plugin['name'] or 'Press' in plugin['name'] else 'peak control'}. The algorithm responds to your audio in a musical way, providing transparent to aggressive dynamic control.",
        'Reverb': f"{plugin['name']} creates spatial effects through {'plate emulation' if 'Plate' in plugin['name'] else 'algorithmic reverb'}. Use it to add depth, space, and dimension to your tracks.",
        'Filter': f"{plugin['name']} shapes frequencies through {'EQ' if 'EQ' in plugin['name'] else 'filtering'}. Use it for tone shaping, problem solving, or creative sound design.",
        'Tape': f"{plugin['name']} emulates magnetic tape characteristics including {'saturation, head bump, and flutter' if 'ToTape' in plugin['name'] else 'specific tape behaviors'}. Use it to add warmth and analog character.",
        'Distortion': f"{plugin['name']} adds harmonics and edge through {'saturation' if 'Sat' in plugin['name'] else 'distortion'}. Use it for adding grit, warmth, or aggressive processing.",
        'Clipping': f"{plugin['name']} controls peaks and maximizes loudness through {'sophisticated clipping' if 'ADClip' in plugin['name'] else 'peak limiting'}. Use it as a mastering tool or creative effect.",
    }
    
    content += how_it_works.get(category, f"{plugin['name']} processes audio in the {category} category. See the description above for specific functionality.")
    
    content += """

## Usage Tips

"""
    
    # Category-specific tips
    tips = {
        'Consoles': [
            "Use matching Channel and Buss plugins (don't mix versions)",
            "Start with settings at 0.5 (neutral)",
            "Place Channel on all important tracks",
            "Place Buss on master fader only",
        ],
        'Dynamics': [
            "Start with gentle settings and increase as needed",
            "Use Dry/Wet for parallel compression if available",
            "Listen for pumping or artifacts",
            "A/B bypass to check if processing helps the mix",
        ],
        'Reverb': [
            "Less is often more - start conservative",
            "Use pre-delay for clarity",
            "EQ the reverb return (cut lows, sometimes highs)",
            "Match decay time to song tempo",
        ],
        'Filter': [
            "Make small adjustments - EQ is powerful",
            "Cut first, boost second (if needed)",
            "Check your changes in context with the full mix",
            "Use solo to identify problem frequencies",
        ],
    }
    
    default_tips = [
        "Start with conservative settings",
        "A/B compare to hear the effect clearly",
        "Use in context with other processing",
        "Trust your ears over visual meters",
    ]
    
    for tip in tips.get(category, default_tips):
        content += f"- {tip}\n"
    
    content += f"""

## Related Plugins

"""
    
    # This would ideally find actually related plugins, but for now use category
    content += f"Browse other [{category}](../categories/{category.lower().replace(' ', '-')}.md) plugins.\n"
    
    content += f"""

## Technical Details

**Source Code**: [View on GitHub](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/{plugin['name']})

**Categories**: {', '.join(plugin['categories'])}

**Available Formats**:
- Mac AU
- Mac VST
- Windows VST
- Linux VST

## Resources

- [All Airwindows Plugins](../../README.md)
- [Category: {category}](../categories/{category.lower().replace(' ', '-')}.md)
- [Airwindows Website](https://www.airwindows.com)
- [Airwindows GitHub](https://github.com/airwindows/airwindows)

---

*Part of the Airwindows plugin collection - Open source audio processing plugins*

*Last updated: 2024*
"""
    
    return content

def main():
    base_path = Path('/Users/thomasphillips/bombestaudio/airwindows')
    output_dir = base_path / 'docs' / 'plugins'
    output_dir.mkdir(exist_ok=True)
    
    # Load plugin data
    print("Loading plugin data...")
    with open(base_path / 'docs' / 'data' / 'plugins.json', 'r', encoding='utf-8') as f:
        plugins = json.load(f)
    
    # Prioritize Latest + Recommended
    priority_plugins = [p for p in plugins if p['is_latest'] or p['is_recommended']]
    other_plugins = [p for p in plugins if not (p['is_latest'] or p['is_recommended'])]
    
    print(f"\nTotal plugins: {len(plugins)}")
    print(f"Priority plugins (Latest/Recommended): {len(priority_plugins)}")
    print(f"Other plugins: {len(other_plugins)}")
    
    # Generate priority plugins first
    print(f"\nGenerating priority plugin documentation...")
    for i, plugin in enumerate(priority_plugins, 1):
        slug = plugin['slug']
        content = create_plugin_page(plugin)
        
        output_path = output_dir / f"{slug}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if i % 10 == 0:
            print(f"  Created {i}/{len(priority_plugins)} priority plugins...")
    
    print(f"✓ Created {len(priority_plugins)} priority plugin pages")
    
    # Generate remaining plugins
    print(f"\nGenerating remaining plugin documentation...")
    for i, plugin in enumerate(other_plugins, 1):
        slug = plugin['slug']
        content = create_plugin_page(plugin)
        
        output_path = output_dir / f"{slug}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if i % 20 == 0:
            print(f"  Created {i}/{len(other_plugins)} remaining plugins...")
    
    print(f"✓ Created {len(other_plugins)} remaining plugin pages")
    
    print(f"\n✓ Complete! Generated documentation for all {len(plugins)} plugins")
    print(f"  Priority: {len(priority_plugins)}")
    print(f"  Standard: {len(other_plugins)}")

if __name__ == '__main__':
    main()

