#!/usr/bin/env python3
"""
Add missing plugins to docs/data/plugins.json.

Root cause: parse_data.py's what.txt regex requires the "is" verb and a period
terminator, missing ~109 entries (other verbs, "!" endings). Airwindopedia's
parse also only matches "is". This script broadens both to cover all 506 WinVST
plugins.

Strategy:
  1. Parse what.txt with a verb-agnostic split on `[coll=`
  2. Parse Airwindopedia.txt with a verb-agnostic delimiter regex
  3. Parse categories section from Airwindopedia.txt
  4. Walk WinVST for canonical plugin list
  5. Load existing plugins.json (360 entries)
  6. Build entries for the ~146 missing plugins
  7. Write merged plugins.json sorted by name
"""

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
WINVST = BASE / "plugins" / "WinVST"
AIRWINDOPEDIA = BASE / "Airwindopedia.txt"
WHAT_TXT = BASE / "what.txt"
PLUGINS_JSON = BASE / "docs" / "data" / "plugins.json"


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_what_txt(filepath: Path) -> dict[str, dict]:
    """
    Parse what.txt into a dict keyed by plugin name.
    Handles any verb (is/creates/extends/...) and both "." and "!" endings.
    """
    result: dict[str, dict] = {}
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    for raw in lines[1:]:  # skip header
        line = raw.strip()
        if not line or "[coll=" not in line:
            continue

        # Split on the [coll= tag boundary
        parts = line.split("[coll=", 1)
        left = parts[0].rstrip(" .")  # remove trailing period/space
        coll_str = parts[1].rstrip("]")
        tags = [t.strip() for t in coll_str.split(",") if t.strip()]

        # Split name from description: first word before first space is the name,
        # then a verb word, then the rest is description.
        # Pattern: PluginName <verb> <description>
        m = re.match(r"^(\S+)\s+\S+\s+(.+)$", left)
        if not m:
            continue

        name = m.group(1).strip()
        # Strip trailing punctuation from description
        description = m.group(2).strip().rstrip(".!")

        result[name] = {
            "description": description,
            "tags": tags,
            "is_latest": "Latest" in tags,
            "is_recommended": "Recommended" in tags,
            "is_basic": "Basic" in tags,
        }

    return result


def parse_airwindopedia(filepath: Path) -> dict[str, dict]:
    """
    Parse Airwindopedia.txt into a dict keyed by plugin name.
    The delimiter is:  ############ PluginName <verb> <rest of first line>\n\n<body>
    Captures the first-line description AND the full body text.
    """
    with open(filepath, encoding="utf-8", errors="replace") as f:
        content = f.read()

    result: dict[str, dict] = {}

    # Split on the ############ delimiter — some sections use single newline before it
    sections = re.split(r"\n+############\s+", "\n\n" + content)

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # First line is the one-liner; rest is body
        lines = section.split("\n", 1)
        first_line = lines[0].strip()
        body = lines[1].strip() if len(lines) > 1 else ""

        # Extract plugin name: first whitespace-delimited token
        m = re.match(r"^(\S+)\s+\S+\s+(.+?)\.?\s*$", first_line)
        if not m:
            continue

        name = m.group(1).strip()
        short_desc = m.group(2).strip().rstrip(".")

        # Clean Airwindopedia boilerplate from body end
        full_desc = body.strip()

        result[name] = {
            "short_description": short_desc,
            "full_description": full_desc,
        }

    return result


def parse_categories(filepath: Path) -> dict[str, list[str]]:
    """
    Parse the # Categories section from Airwindopedia.txt.
    Returns dict: plugin_name -> [category, ...]
    """
    with open(filepath, encoding="utf-8", errors="replace") as f:
        content = f.read()

    cat_match = re.search(r"# Categories\n\n(.*?)\n\n########", content, re.DOTALL)
    if not cat_match:
        return {}

    plugin_to_cats: dict[str, list[str]] = {}
    for line in cat_match.group(1).split("\n"):
        if ":" not in line:
            continue
        cat_name, plugins_str = line.split(":", 1)
        cat_name = cat_name.strip()
        for plugin in plugins_str.split(","):
            plugin = plugin.strip()
            if plugin:
                plugin_to_cats.setdefault(plugin, []).append(cat_name)

    return plugin_to_cats


def get_winvst_names(winvst_root: Path) -> list[str]:
    """Return sorted list of plugin names from WinVST directory."""
    return sorted(p.name for p in winvst_root.iterdir() if p.is_dir())


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Loading existing plugins.json...")
    with open(PLUGINS_JSON, encoding="utf-8") as f:
        existing: list[dict] = json.load(f)
    existing_names = {p["name"] for p in existing}
    print(f"  {len(existing)} existing entries")

    print("Parsing what.txt...")
    what_data = parse_what_txt(WHAT_TXT)
    print(f"  {len(what_data)} entries parsed")

    print("Parsing Airwindopedia.txt...")
    awind_data = parse_airwindopedia(AIRWINDOPEDIA)
    print(f"  {len(awind_data)} entries parsed")

    print("Parsing categories...")
    categories = parse_categories(AIRWINDOPEDIA)
    print(f"  {len(categories)} category mappings")

    print("Reading WinVST plugin list...")
    all_names = get_winvst_names(WINVST)
    print(f"  {len(all_names)} WinVST plugins")

    missing = [n for n in all_names if n not in existing_names]
    print(f"\n{len(missing)} plugins to add")

    new_entries: list[dict] = []
    sourced_from_what = 0
    sourced_from_awind = 0
    stubs = 0

    for name in sorted(missing):
        slug = name.lower()
        what = what_data.get(name, {})
        awind = awind_data.get(name, {})
        cats = categories.get(name, [])

        description = (
            what.get("description")
            or awind.get("short_description")
            or ""
        )
        short_description = (
            awind.get("short_description")
            or what.get("description")
            or ""
        )
        full_description = awind.get("full_description", "")
        tags = what.get("tags", [])
        is_latest = what.get("is_latest", False)
        is_recommended = what.get("is_recommended", False)
        is_basic = what.get("is_basic", False)

        if not cats:
            cats = ["Utility"]

        entry = {
            "name": name,
            "description": description,
            "tags": tags,
            "slug": slug,
            "short_description": short_description,
            "full_description": full_description,
            "categories": cats,
            "is_latest": is_latest,
            "is_recommended": is_recommended,
            "is_basic": is_basic,
        }
        new_entries.append(entry)

        if what and awind:
            sourced_from_what += 1
        elif awind:
            sourced_from_awind += 1
        else:
            stubs += 1
            print(f"  STUB (no data): {name}")

    print(f"\nSource breakdown:")
    print(f"  what.txt + Airwindopedia: {sourced_from_what}")
    print(f"  Airwindopedia only:       {sourced_from_awind}")
    print(f"  Stubs (WinVST only):      {stubs}")

    merged = existing + new_entries
    merged.sort(key=lambda p: p["name"].lower())

    # Enrichment pass: update any entry missing descriptions using better-parsed data
    enriched = 0
    for entry in merged:
        name = entry["name"]
        if entry.get("full_description") and entry.get("description"):
            continue  # already complete
        awind = awind_data.get(name, {})
        what = what_data.get(name, {})
        if not entry.get("description") and (what.get("description") or awind.get("short_description")):
            entry["description"] = what.get("description") or awind.get("short_description", "")
            enriched += 1
        if not entry.get("short_description") and awind.get("short_description"):
            entry["short_description"] = awind["short_description"]
        if not entry.get("full_description") and awind.get("full_description"):
            entry["full_description"] = awind["full_description"]
        if not entry.get("categories"):
            entry["categories"] = categories.get(name, ["Utility"])

    if enriched:
        print(f"\nEnriched {enriched} previously-stub entries")

    print(f"\nWriting {len(merged)} entries to plugins.json...")
    with open(PLUGINS_JSON, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print("Done.")
    print(f"  Before: {len(existing)}")
    print(f"  Added:  {len(new_entries)}")
    print(f"  After:  {len(merged)}")


if __name__ == "__main__":
    main()
