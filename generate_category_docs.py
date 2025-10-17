#!/usr/bin/env python3
"""
Generate category documentation pages for remaining categories
"""

import json
from pathlib import Path

# Category templates with descriptions and recommendations
CATEGORY_INFO = {
    'ambience': {
        'title': 'Ambience',
        'description': 'Delays, echoes, and ambience effects for creating space and depth in your mixes.',
        'overview': 'Ambience plugins create spatial effects through delay-based processing, from simple echoes to complex soundscapes.',
        'key_plugins': ['ClearCoat', 'TapeDelay2', 'PitchDelay', 'TripleSpread'],
        'use_cases': ['Creating depth', 'Stereo widening', 'Rhythmic delays', 'Atmospheric effects']
    },
    'amp-sims': {
        'title': 'Amp Sims',
        'description': 'Guitar and bass amplifier simulators for instrument processing.',
        'overview': 'Amp simulation plugins model the behavior of guitar and bass amplifiers, from clean to heavily distorted.',
        'key_plugins': ['PointyGuitar', 'ChimeyGuitar', 'GrindAmp', 'CrickBass'],
        'use_cases': ['Guitar tones', 'Bass processing', 'DI recording', 'Reamping']
    },
    'bass': {
        'title': 'Bass',
        'description': 'Bass enhancement, sub-bass generation, and low-end processing tools.',
        'overview': 'Bass plugins enhance and generate low-frequency content, from subtle reinforcement to synthetic sub-bass.',
        'key_plugins': ['DubSub2', 'OrbitKick', 'BassKit', 'Hermepass'],
        'use_cases': ['Bass reinforcement', 'Sub generation', 'Kick enhancement', 'Low-end control']
    },
    'biquads': {
        'title': 'Biquads',
        'description': 'Flexible biquad filters for precise frequency control and tone shaping.',
        'overview': 'Biquad filters are building blocks for EQs and filters, offering precise frequency control.',
        'key_plugins': ['BiquadStack', 'BiquadNonLin', 'BiquadPlus', 'Biquad'],
        'use_cases': ['Precise filtering', 'EQ building blocks', 'Tone shaping', 'Technical filtering']
    },
    'brightness': {
        'title': 'Brightness',
        'description': 'High-frequency enhancement, de-essing, and treble control plugins.',
        'overview': 'Brightness plugins control and enhance high frequencies, from subtle air to aggressive treble boost.',
        'key_plugins': ['Air4', 'DeBess', 'Sinew', 'Acceleration2'],
        'use_cases': ['Adding air', 'De-essing', 'Treble control', 'Brightness limiting']
    },
    'clipping': {
        'title': 'Clipping',
        'description': 'Peak control, loudness maximization, and clipping effects.',
        'overview': 'Clipping plugins control peaks and maximize loudness through various clipping algorithms.',
        'key_plugins': ['ADClip8', 'ClipOnly2', 'OneCornerClip', 'ClipSoftly'],
        'use_cases': ['Loudness maximization', 'Peak control', 'Safety limiting', 'Analog clipping emulation']
    },
    'distortion': {
        'title': 'Distortion',
        'description': 'Drive, saturation, and distortion effects for adding edge and character.',
        'overview': 'Distortion plugins add harmonics and edge, from subtle warmth to extreme destruction.',
        'key_plugins': ['Distortion', 'Edge', 'Drive', 'Mackity'],
        'use_cases': ['Adding grit', 'Harmonic enhancement', 'Creative distortion', 'Sound design']
    },
    'dithers': {
        'title': 'Dithers',
        'description': 'Dithering and wordlength reduction for final output processing.',
        'overview': 'Dither plugins reduce wordlength while managing quantization noise and maintaining audio quality.',
        'key_plugins': ['Dark', 'PaulDither', 'TPDFDither', 'NotJustAnotherDither'],
        'use_cases': ['Bit depth reduction', 'Final output', 'Mastering', 'Noise shaping']
    },
    'effects': {
        'title': 'Effects',
        'description': 'Creative effects, modulators, and sound design tools.',
        'overview': 'Effects plugins provide creative processing, from subtle modulation to extreme transformation.',
        'key_plugins': ['TakeCare', 'GlitchShifter', 'PitchNasty', 'Trianglizer'],
        'use_cases': ['Creative processing', 'Sound design', 'Modulation', 'Experimental effects']
    },
    'filter': {
        'title': 'Filter',
        'description': 'EQs, filters, and tone shaping tools for frequency control.',
        'overview': 'Filter plugins shape frequency response, from surgical EQs to creative tone-shapers.',
        'key_plugins': ['PearEQ', 'SmoothEQ2', 'Parametric', 'Isolator3'],
        'use_cases': ['EQ', 'Frequency shaping', 'Problem solving', 'Tone control']
    },
    'lo-fi': {
        'title': 'Lo-Fi',
        'description': 'Bit crushing, sample rate reduction, and vintage digital effects.',
        'overview': 'Lo-Fi plugins degrade audio quality in musical ways, from subtle vintage to extreme destruction.',
        'key_plugins': ['DeRez3', 'Pockey2', 'GrooveWear', 'Flutter2'],
        'use_cases': ['Lo-fi aesthetics', 'Bit reduction', 'Vintage digital', 'Creative degradation']
    },
    'noise': {
        'title': 'Noise',
        'description': 'Noise generators and textural sound sources for adding atmosphere.',
        'overview': 'Noise plugins generate various types of noise for texture, atmosphere, and sound design.',
        'key_plugins': ['Noise', 'DarkNoise', 'TapeDust', 'Silhouette'],
        'use_cases': ['Adding texture', 'Sound design', 'Atmosphere', 'Layering']
    },
    'saturation': {
        'title': 'Saturation',
        'description': 'Subtle harmonic enhancement and analog-style saturation.',
        'overview': 'Saturation plugins add harmonics and warmth, emulating analog circuitry and tape.',
        'key_plugins': ['PurestDrive', 'Tube2', 'Spiral2', 'Hypersoft'],
        'use_cases': ['Adding warmth', 'Harmonic enhancement', 'Analog emulation', 'Glue']
    },
    'stereo': {
        'title': 'Stereo',
        'description': 'Stereo widening, mid-side processing, and spatial effects.',
        'overview': 'Stereo plugins manipulate the stereo image, from subtle widening to creative spatial effects.',
        'key_plugins': ['Srsly3', 'Wider', 'Elliptical', 'AutoPan'],
        'use_cases': ['Stereo widening', 'Mid-side processing', 'Spatial enhancement', 'Imaging']
    },
    'subtlety': {
        'title': 'Subtlety',
        'description': 'Mastering-grade subtle processing and tone shaping.',
        'overview': 'Subtlety plugins provide gentle, high-quality processing for mastering and final touches.',
        'key_plugins': ['Mastering2', 'Interstage', 'Shape', 'Sweeten'],
        'use_cases': ['Mastering', 'Subtle enhancement', 'Final polish', 'Transparent processing']
    },
    'tone-color': {
        'title': 'Tone Color',
        'description': 'Console-style tone coloration and character addition.',
        'overview': 'Tone Color plugins add character and color, inspired by classic console channels.',
        'key_plugins': ['Channel9', 'BussColors4', 'Neverland', 'Crystal'],
        'use_cases': ['Adding character', 'Mix coloration', 'Console tones', 'Vintage vibes']
    },
    'utility': {
        'title': 'Utility',
        'description': 'Gain, metering, routing, and utility processors.',
        'overview': 'Utility plugins handle essential functions like gain, routing, metering, and format conversion.',
        'key_plugins': ['PurestGain', 'Monitoring3', 'Golem', 'BitShiftGain'],
        'use_cases': ['Gain control', 'Monitoring', 'Format conversion', 'Utility functions']
    },
    'xyz-filters': {
        'title': 'XYZ Filters',
        'description': 'Experimental and character filters with unique behaviors.',
        'overview': 'XYZ filters emulate vintage sampler DSP and create unique frequency-shaping effects.',
        'key_plugins': ['ZBandpass2', 'YBandpass', 'XBandpass', 'ZRegion2'],
        'use_cases': ['Creative filtering', 'Vintage sampler emulation', 'Character filters', 'Experimental']
    },
}

def create_category_page(slug, info, plugins, output_dir):
    """Generate a category documentation page"""
    
    # Filter plugins for this category
    category_plugins = [p for p in plugins if info['title'] in p['categories']]
    
    # Get recommended plugins
    recommended = [p for p in category_plugins if p['is_recommended']][:6]
    latest = [p for p in category_plugins if p['is_latest']][:6]
    
    content = f"""# {info['title']} Plugins

{info['description']}

## Overview

{info['overview']}

**Plugin Count**: {len(category_plugins)}  
**Recommended**: {len([p for p in category_plugins if p['is_recommended']])}  
**Latest**: {len([p for p in category_plugins if p['is_latest']])}

## Key Plugins

"""
    
    # Add recommended plugins
    if recommended:
        content += "### Recommended\n\n"
        for plugin in recommended:
            content += f"#### {plugin['name']}\n"
            content += f"{plugin['description']}\n\n"
    
    # Add usage scenarios
    content += f"""## Common Use Cases

"""
    for use_case in info['use_cases']:
        content += f"- **{use_case}**\n"
    
    content += f"""

## All Plugins in This Category

"""
    
    # List all plugins
    for plugin in sorted(category_plugins, key=lambda x: x['name']):
        tags = []
        if plugin['is_latest']: tags.append('Latest')
        if plugin['is_recommended']: tags.append('Recommended')
        if plugin['is_basic']: tags.append('Basic')
        tag_str = f" *{', '.join(tags)}*" if tags else ""
        
        content += f"### {plugin['name']}{tag_str}\n"
        content += f"{plugin['description']}\n\n"
    
    # Add footer
    content += f"""
## Related Categories

"""
    
    # Find related categories based on plugin overlap
    related = []
    for other_cat in CATEGORY_INFO:
        if other_cat != slug:
            overlap = len([p for p in plugins if info['title'] in p['categories'] and CATEGORY_INFO[other_cat]['title'] in p['categories']])
            if overlap > 5:
                related.append((CATEGORY_INFO[other_cat]['title'], other_cat, overlap))
    
    related.sort(key=lambda x: x[2], reverse=True)
    for name, cat_slug, count in related[:4]:
        content += f"- **[{name}]({cat_slug}.md)** - {count} shared plugins\n"
    
    content += """
## Resources

- **GitHub Source**: [Browse Source Code](https://github.com/airwindows/airwindows/tree/master/plugins/LinuxVST/src/)
- **Video Demos**: [YouTube Channel](https://www.youtube.com/@airwindows)
- **Forum**: [Discussions](https://forum.airwindows.com)

---

*Last updated: 2024*
"""
    
    # Write file
    output_path = output_dir / f"{slug}.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {output_path.name}")

def main():
    base_path = Path('/Users/thomasphillips/bombestaudio/airwindows')
    output_dir = base_path / 'docs' / 'categories'
    
    # Load plugin data
    with open(base_path / 'docs' / 'data' / 'plugins.json', 'r', encoding='utf-8') as f:
        plugins = json.load(f)
    
    # Generate category pages
    print("Generating category documentation pages...")
    for slug, info in CATEGORY_INFO.items():
        create_category_page(slug, info, plugins, output_dir)
    
    print(f"\nCompleted! Generated {len(CATEGORY_INFO)} category pages.")

if __name__ == '__main__':
    main()

