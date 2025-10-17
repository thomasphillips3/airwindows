#!/usr/bin/env python3
"""
Parse Airwindows plugin data from Airwindopedia.txt and what.txt
Generates JSON files for the documentation system
"""

import json
import re
from pathlib import Path

def parse_categories(text):
    """Extract category mappings from Airwindopedia.txt"""
    categories = {}
    
    # Find the Categories section
    cat_match = re.search(r'# Categories\n\n(.*?)\n\n########', text, re.DOTALL)
    if not cat_match:
        return categories
    
    cat_text = cat_match.group(1)
    
    # Parse each category line
    for line in cat_text.split('\n'):
        if ':' not in line:
            continue
        
        cat_name, plugins = line.split(':', 1)
        cat_name = cat_name.strip()
        plugin_list = [p.strip() for p in plugins.split(',')]
        
        categories[cat_name] = plugin_list
        
    return categories

def parse_plugin_descriptions(text):
    """Extract detailed descriptions for each plugin from Airwindopedia.txt"""
    descriptions = {}
    
    # Find all plugin sections (marked with ############ PluginName)
    pattern = r'############ ([^\n]+?) is ([^\n]+?)\.\n\n(.*?)(?=\n\n############|\Z)'
    matches = re.finditer(pattern, text, re.DOTALL)
    
    for match in matches:
        plugin_name = match.group(1).strip()
        short_desc = match.group(2).strip()
        long_desc = match.group(3).strip()
        
        descriptions[plugin_name] = {
            'short': short_desc,
            'full': long_desc
        }
    
    return descriptions

def parse_what_file(filepath):
    """Parse what.txt for plugin metadata"""
    plugins = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines[1:]:  # Skip header
        line = line.strip()
        if not line:
            continue
            
        # Parse format: PluginName is description.[coll=tags]
        match = re.match(r'(.+?) is (.+?)\.\[coll=(.*?)\]', line)
        if match:
            name = match.group(1).strip()
            description = match.group(2).strip()
            tags_str = match.group(3).strip()
            tags = [t.strip() for t in tags_str.split(',') if t.strip()]
            
            plugins.append({
                'name': name,
                'description': description,
                'tags': tags,
                'slug': name.lower().replace(' ', '-')
            })
    
    return plugins

def merge_plugin_data(plugins, descriptions, categories):
    """Merge all plugin data sources"""
    # Create reverse category lookup
    plugin_categories = {}
    for cat_name, plugin_list in categories.items():
        for plugin in plugin_list:
            if plugin not in plugin_categories:
                plugin_categories[plugin] = []
            plugin_categories[plugin].append(cat_name)
    
    # Merge data
    for plugin in plugins:
        name = plugin['name']
        
        # Add detailed description if available
        if name in descriptions:
            plugin['short_description'] = descriptions[name]['short']
            plugin['full_description'] = descriptions[name]['full']
        else:
            plugin['short_description'] = plugin['description']
            plugin['full_description'] = ''
        
        # Add categories
        plugin['categories'] = plugin_categories.get(name, ['Utility'])
        
        # Determine if it's Latest/Recommended/Basic
        plugin['is_latest'] = 'Latest' in plugin['tags']
        plugin['is_recommended'] = 'Recommended' in plugin['tags']
        plugin['is_basic'] = 'Basic' in plugin['tags']
    
    return plugins

def generate_categories_json(categories):
    """Generate categories metadata"""
    category_data = []
    
    # Define category descriptions
    cat_descriptions = {
        'Ambience': 'Delays, echoes, and ambience effects for creating space and depth',
        'Amp Sims': 'Guitar and bass amplifier simulators for instrument processing',
        'Bass': 'Bass enhancement, sub-bass generation, and low-end processing',
        'Biquads': 'Flexible biquad filters for precise frequency control',
        'Brightness': 'High-frequency enhancement, de-essing, and treble control',
        'Clipping': 'Peak control, loudness maximization, and clipping effects',
        'Consoles': 'Mix bus processing and analog console emulation systems',
        'Distortion': 'Saturation, drive, and distortion effects',
        'Dithers': 'Dithering and wordlength reduction for final output',
        'Dynamics': 'Compressors, limiters, gates, and dynamics processors',
        'Effects': 'Creative effects, modulators, and sound design tools',
        'Filter': 'EQs, filters, and tone shaping tools',
        'Lo-Fi': 'Bit crushing, sample rate reduction, and vintage digital effects',
        'Noise': 'Noise generators and textural sound sources',
        'Reverb': 'Reverb effects from small rooms to infinite spaces',
        'Saturation': 'Subtle harmonic enhancement and analog-style saturation',
        'Stereo': 'Stereo widening, mid-side processing, and spatial effects',
        'Subtlety': 'Subtle tone shaping and mastering-grade processors',
        'Tape': 'Tape emulation and magnetic recording simulation',
        'Tone Color': 'Console-style tone coloration and character addition',
        'Utility': 'Gain, metering, routing, and utility processors',
        'XYZ Filters': 'Experimental and character filters with unique behaviors'
    }
    
    for cat_name, plugins in categories.items():
        category_data.append({
            'name': cat_name,
            'slug': cat_name.lower().replace(' ', '-'),
            'description': cat_descriptions.get(cat_name, 'Audio processing plugins'),
            'plugin_count': len(plugins),
            'plugins': plugins
        })
    
    return category_data

def main():
    base_path = Path('/Users/thomasphillips/bombestaudio/airwindows')
    
    # Read source files
    print("Reading source files...")
    with open(base_path / 'Airwindopedia.txt', 'r', encoding='utf-8') as f:
        airwindopedia = f.read()
    
    # Parse data
    print("Parsing categories...")
    categories = parse_categories(airwindopedia)
    
    print("Parsing plugin descriptions...")
    descriptions = parse_plugin_descriptions(airwindopedia)
    
    print("Parsing plugin metadata...")
    plugins = parse_what_file(base_path / 'what.txt')
    
    print("Merging data...")
    plugins = merge_plugin_data(plugins, descriptions, categories)
    
    print("Generating categories JSON...")
    category_data = generate_categories_json(categories)
    
    # Write JSON files
    print("Writing plugins.json...")
    with open(base_path / 'docs' / 'data' / 'plugins.json', 'w', encoding='utf-8') as f:
        json.dump(plugins, f, indent=2)
    
    print("Writing categories.json...")
    with open(base_path / 'docs' / 'data' / 'categories.json', 'w', encoding='utf-8') as f:
        json.dump(category_data, f, indent=2)
    
    print(f"\nCompleted!")
    print(f"Total plugins: {len(plugins)}")
    print(f"Total categories: {len(category_data)}")
    print(f"Latest plugins: {sum(1 for p in plugins if p['is_latest'])}")
    print(f"Recommended plugins: {sum(1 for p in plugins if p['is_recommended'])}")
    print(f"Basic plugins: {sum(1 for p in plugins if p['is_basic'])}")

if __name__ == '__main__':
    main()

