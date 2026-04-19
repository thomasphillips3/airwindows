#!/usr/bin/env python3
"""
Airwindows plugin metadata extractor.

Walks plugins/WinVST/ and produces a plugin-index.json with one record per
plugin. Cross-references with docs/data/plugins.json for descriptions,
categories, and flags.

Usage (from airwindows repo root or anywhere):
    python3 skills/airwindows-expert/scripts/extract-plugin-metadata.py

Output:
    skills/airwindows-expert/references/plugin-index.json
"""

import json
import re
import sys
import argparse
from pathlib import Path


# ── Paths ──────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
AIRWINDOWS_ROOT = SKILL_DIR.parent.parent  # airwindows/
OUTPUT_FILE = SKILL_DIR / "references" / "plugin-index.json"


# ── Regex patterns ─────────────────────────────────────────────────────────────

RE_UNIQUE_ID = re.compile(r"kUniqueId\s*=\s*'([^']*)'")
RE_NUM_PARAMS = re.compile(r"kNumParameters\s*=\s*(\d+)")
RE_PARAM_NAME = re.compile(
    r"case\s+kParam_?([A-Z]+):\s*vst_strncpy\s*\([^,]+,\s*\"([^\"]+)\""
)
RE_PARAM_ENUM_ENTRIES = re.compile(r"\bkParam_?([A-Z]+)\s*=\s*(\d+)")
RE_TOP_COMMENT = re.compile(r"^/\*.*?\*/", re.DOTALL)
RE_DOUBLE_MEMBER = re.compile(r"^\s+double\s+\w+", re.MULTILINE)
RE_FPD = re.compile(r"\bfpd[LR]\b")
RE_SAMPLE_RATE = re.compile(r"\bgetSampleRate\(\)|\bsampleRate\b")
RE_GET_PARAM_NAME_FUNC = re.compile(
    r"::getParameterName\s*\([^)]*\)\s*\{(.*?)\}",
    re.DOTALL,
)
RE_GET_PARAM_LABEL_FUNC = re.compile(
    r"::getParameterLabel\s*\([^)]*\)\s*\{(.*?)\}",
    re.DOTALL,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def read_file(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def extract_top_comment(cpp_text: str) -> str:
    m = RE_TOP_COMMENT.match(cpp_text.lstrip())
    if not m:
        return ""
    lines = m.group(0).splitlines()
    cleaned = []
    for line in lines:
        line = line.strip().lstrip("*").strip()
        if not line or line.startswith("===") or line == "=":
            continue
        cleaned.append(line)
    return " | ".join(cleaned)


def extract_unique_id(h_text: str) -> str:
    m = RE_UNIQUE_ID.search(h_text)
    return m.group(1) if m else ""


def extract_num_parameters(h_text: str) -> int:
    m = RE_NUM_PARAMS.search(h_text)
    return int(m.group(1)) if m else 0


def extract_param_enum_order(h_text: str) -> list[str]:
    """Returns param suffixes in index order: ['A','B','C'] or ['HIP','LOP','AIR',...]"""
    entries = RE_PARAM_ENUM_ENTRIES.findall(h_text)  # [('A', '0'), ('HIP', '0'), ...]
    if not entries:
        return []
    sorted_entries = sorted(entries, key=lambda x: int(x[1]))
    return [suffix for suffix, _ in sorted_entries]


def extract_parameter_names(cpp_text: str) -> dict[str, str]:
    """{'A': 'Compress', 'HIP': 'Hi Pass', ...} keyed by enum suffix."""
    func_match = RE_GET_PARAM_NAME_FUNC.search(cpp_text)
    if not func_match:
        return {}
    return {suffix: name for suffix, name in RE_PARAM_NAME.findall(func_match.group(1))}


def extract_parameter_labels(cpp_text: str) -> dict[str, str]:
    func_match = RE_GET_PARAM_LABEL_FUNC.search(cpp_text)
    if not func_match:
        return {}
    return {suffix: label for suffix, label in RE_PARAM_NAME.findall(func_match.group(1))}


# ── Plugin extractor ──────────────────────────────────────────────────────────

def extract_plugin(plugin_dir: Path, airwindows_root: Path) -> dict:
    name = plugin_dir.name
    rel_dir = str(plugin_dir.relative_to(airwindows_root))

    h_path = plugin_dir / f"{name}.h"
    cpp_path = plugin_dir / f"{name}.cpp"
    proc_path = plugin_dir / f"{name}Proc.cpp"

    h_text = read_file(h_path) or ""
    cpp_text = read_file(cpp_path) or ""
    proc_text = read_file(proc_path) or ""

    total_lines = (cpp_text.count("\n") + 1) + (proc_text.count("\n") + 1 if proc_text else 0)

    num_params = extract_num_parameters(h_text)
    enum_order = extract_param_enum_order(h_text)
    param_names_raw = extract_parameter_names(cpp_text)
    param_labels_raw = extract_parameter_labels(cpp_text)

    # Zero-parameter plugins (e.g. ClipOnly) are valid
    if num_params == 0:
        parameters: list[dict] | str = []
    elif param_names_raw and enum_order:
        parameters = [
            {
                "index": i,
                "enum_suffix": suffix,
                "name": param_names_raw.get(suffix, f"Param{suffix}"),
                "label": param_labels_raw.get(suffix, ""),
            }
            for i, suffix in enumerate(enum_order[:num_params])
        ]
    else:
        parameters = "unparsed"

    search_text = proc_text if proc_text else cpp_text
    fpd_refs = len(RE_FPD.findall(search_text))
    sr_refs = len(RE_SAMPLE_RATE.findall(search_text))
    state_vars = len(RE_DOUBLE_MEMBER.findall(h_text))

    return {
        "name": name,
        "slug": name.lower(),
        "source_dir": rel_dir,
        "files": {
            "h": str(h_path.relative_to(airwindows_root)) if h_path.exists() else None,
            "cpp": str(cpp_path.relative_to(airwindows_root)) if cpp_path.exists() else None,
            "proc_cpp": str(proc_path.relative_to(airwindows_root)) if proc_path.exists() else None,
        },
        "unique_id": extract_unique_id(h_text),
        "num_parameters": num_params,
        "parameters": parameters,
        "top_comment": extract_top_comment(cpp_text),
        "complexity": {
            "total_lines": total_lines,
            "fpd_references": fpd_refs,
            "sample_rate_references": sr_refs,
            "state_var_doubles": state_vars,
            "has_proc_cpp": proc_path.exists(),
        },
        "airwindopedia": None,
    }


# ── Cross-reference ───────────────────────────────────────────────────────────

def load_plugins_json(airwindows_root: Path) -> dict[str, dict]:
    path = airwindows_root / "docs" / "data" / "plugins.json"
    if not path.exists():
        print(f"  WARNING: {path} not found — skipping cross-reference")
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return {p["name"].lower(): p for p in data}


def apply_cross_reference(record: dict, plugins_lookup: dict) -> dict:
    entry = plugins_lookup.get(record["slug"])
    if entry:
        record["airwindopedia"] = {
            "short_description": entry.get("short_description", ""),
            "full_description": entry.get("full_description", ""),
            "categories": entry.get("categories", []),
            "is_latest": entry.get("is_latest", False),
            "is_recommended": entry.get("is_recommended", False),
            "is_basic": entry.get("is_basic", False),
            "tags": entry.get("tags", []),
        }
    return record


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Extract Airwindows plugin metadata")
    parser.add_argument(
        "--airwindows-root",
        type=Path,
        default=AIRWINDOWS_ROOT,
        help=f"Path to the airwindows repo root (default: {AIRWINDOWS_ROOT})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_FILE,
        help=f"Output JSON file (default: {OUTPUT_FILE})",
    )
    args = parser.parse_args()

    airwindows_root = args.airwindows_root.resolve()
    winvst_dir = airwindows_root / "plugins" / "WinVST"

    if not winvst_dir.exists():
        print(f"ERROR: WinVST directory not found at {winvst_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Airwindows root : {airwindows_root}")
    print(f"Scanning        : {winvst_dir}")

    plugins_lookup = load_plugins_json(airwindows_root)
    print(f"  plugins.json  : {len(plugins_lookup)} entries loaded")

    plugin_dirs = sorted(
        p for p in winvst_dir.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )
    print(f"  Plugin dirs   : {len(plugin_dirs)} found\n")

    records: list[dict] = []
    parse_failures: list[str] = []
    no_proc: list[str] = []

    for plugin_dir in plugin_dirs:
        try:
            record = extract_plugin(plugin_dir, airwindows_root)
            record = apply_cross_reference(record, plugins_lookup)
            if record["parameters"] == "unparsed":
                parse_failures.append(record["name"])
            if not record["complexity"]["has_proc_cpp"]:
                no_proc.append(record["name"])
            records.append(record)
        except Exception as e:
            print(f"  ERROR {plugin_dir.name}: {e}", file=sys.stderr)
            parse_failures.append(plugin_dir.name)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    # ── Report ────────────────────────────────────────────────────────────────
    documented = sum(1 for r in records if r["airwindopedia"] is not None)
    fully_parsed = sum(1 for r in records if r["parameters"] != "unparsed")

    print(f"✓  {len(records)} records written → {args.output}")
    print(f"   Airwindopedia cross-refs : {documented}/{len(records)}")
    print(f"   Parameters parsed        : {fully_parsed}/{len(records)}")

    if parse_failures:
        print(f"\n   ⚠  Parse failures ({len(parse_failures)}):")
        for n in parse_failures[:20]:
            print(f"      - {n}")
        if len(parse_failures) > 20:
            print(f"      … and {len(parse_failures) - 20} more")

    if no_proc:
        print(f"\n   ⚠  Missing Proc.cpp ({len(no_proc)}):")
        for n in no_proc[:10]:
            print(f"      - {n}")
        if len(no_proc) > 10:
            print(f"      … and {len(no_proc) - 10} more")

    # ── Spot-check ────────────────────────────────────────────────────────────
    print("\n── Spot-check samples ───────────────────────────────────────────")
    for sample_name in ["ButterComp2", "ToTape9", "PaulDither", "Galactic2"]:
        match = next((r for r in records if r["name"] == sample_name), None)
        if not match:
            print(f"\n{sample_name}: NOT FOUND")
            continue
        print(f"\n{sample_name}:")
        print(f"  unique_id  : {match['unique_id']}")
        print(f"  num_params : {match['num_parameters']}")
        if match["parameters"] == []:
            print(f"    (no parameters)")
        elif match["parameters"] != "unparsed":
            for p in match["parameters"]:
                suffix = f" [{p['label']}]" if p["label"] else ""
                print(f"    {p['enum_suffix']}: {p['name']}{suffix}")
        else:
            print(f"    parameters: unparsed")
        c = match["complexity"]
        print(f"  lines      : {c['total_lines']}  fpd: {c['fpd_references']}  sr: {c['sample_rate_references']}  doubles: {c['state_var_doubles']}")
        if match["airwindopedia"]:
            print(f"  categories : {match['airwindopedia']['categories']}")
            print(f"  desc       : {match['airwindopedia']['short_description'][:80]}")
        else:
            print(f"  airwindopedia: (not in plugins.json)")


if __name__ == "__main__":
    main()
