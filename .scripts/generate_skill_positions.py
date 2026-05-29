#!/usr/bin/env python3
"""Generate skill-positions.yaml — a lightweight skill tracking manifest.

Usage:
    python generate_skill_positions.py                  # full regeneration
    python generate_skill_positions.py --incremental    # append only new skills
    python generate_skill_positions.py --skill-id <id>  # update a single skill
"""

import argparse
import datetime
import os
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSITIONS_FILE = os.path.join(REPO_ROOT, 'skill-positions.yaml')
SKILLS_DIR = os.path.join(REPO_ROOT, 'skills')


def collect_files(skill_path: str) -> list[str]:
    """Recursively collect files, sorted: top-level first (alpha), then subdirectories."""
    if not os.path.isdir(skill_path):
        return []

    entries: list[tuple[int, str]] = []
    for root, _dirs, fnames in os.walk(skill_path):
        for fn in sorted(fnames):
            rel = os.path.relpath(os.path.join(root, fn), skill_path)
            rel = rel.replace('\\', '/')
            entries.append((rel.count('/'), rel))

    entries.sort(key=lambda x: (x[0], x[1]))
    return [e[1] for e in entries]


def is_skill_dir(path: str) -> bool:
    """A directory is a skill dir only if it contains both SKILL.md and skill.yaml."""
    return os.path.isfile(os.path.join(path, 'SKILL.md')) and os.path.isfile(os.path.join(path, 'skill.yaml'))


def discover_skills() -> list[str]:
    """Walk SKILLS_DIR and return sorted list of skill directory paths (relative to REPO_ROOT)."""
    found = []
    for root, dirs, _fnames in os.walk(SKILLS_DIR):
        if is_skill_dir(root):
            rel = os.path.relpath(root, REPO_ROOT).replace('\\', '/') + '/'
            found.append(rel)
        dirs.sort()
    found.sort()
    return found


def build_entry(skill_path: str) -> dict | None:
    """Build a single skill-positions entry from a skill directory."""
    full = os.path.join(REPO_ROOT, skill_path.rstrip('/'))
    yaml_file = os.path.join(full, 'skill.yaml')

    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            meta = yaml.safe_load(f) or {}
    except (OSError, yaml.YAMLError) as e:
        print(f"  WARNING: cannot read {skill_path}skill.yaml: {e}")
        return None

    skill_id = meta.get('skill_id')
    name = meta.get('name')
    if not skill_id or not name:
        print(f"  WARNING: {skill_path}skill.yaml missing skill_id or name, skipping")
        return None

    return {
        'skill_id': skill_id,
        'name': name,
        'files': collect_files(full),
        'path': skill_path,
    }


def load_existing() -> dict:
    """Load existing skill-positions.yaml, or return empty skeleton."""
    if not os.path.isfile(POSITIONS_FILE):
        return {'skills': {}}
    try:
        with open(POSITIONS_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
    except (OSError, yaml.YAMLError):
        return {'skills': {}}
    # index by skill_id for easy lookup
    data['skills'] = {s['skill_id']: s for s in data.get('skills', []) if isinstance(s, dict) and 'skill_id' in s}
    return data


def write_output(skills: list[dict]):
    """Write skill-positions.yaml with ordered keys."""
    data = {
        'updated_at': datetime.date.today().isoformat(),
        'total_skills': len(skills),
        'skills': skills,
    }
    with open(POSITIONS_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
    print(f"Written {len(skills)} skills to {POSITIONS_FILE}")


def cmd_full():
    """Full regeneration: scan all skills and overwrite."""
    print("Mode: full regeneration")
    paths = discover_skills()
    entries = []
    for p in paths:
        entry = build_entry(p)
        if entry:
            entries.append(entry)
    write_output(entries)


def cmd_incremental():
    """Incremental: only append skills not already in the file."""
    print("Mode: incremental")
    existing = load_existing()
    existing_skills = existing['skills']
    paths = discover_skills()

    new_count = 0
    for p in paths:
        full = os.path.join(REPO_ROOT, p.rstrip('/'))
        yaml_file = os.path.join(full, 'skill.yaml')
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                meta = yaml.safe_load(f) or {}
        except (OSError, yaml.YAMLError):
            continue
        skill_id = meta.get('skill_id')
        if not skill_id:
            continue
        if skill_id in existing_skills:
            continue
        entry = build_entry(p)
        if entry:
            existing_skills[skill_id] = entry
            new_count += 1
            print(f"  + {skill_id}")

    if new_count == 0:
        print("  No new skills found.")
    # rebuild ordered list (preserve original order, append new at end)
    skills_list = list(existing_skills.values())
    write_output(skills_list)


def cmd_skill(skill_id: str):
    """Update or add a single skill by skill_id."""
    print(f"Mode: single skill — {skill_id}")
    existing = load_existing()
    existing_skills = existing['skills']

    # search for the skill directory
    paths = discover_skills()
    target_path = None
    for p in paths:
        full = os.path.join(REPO_ROOT, p.rstrip('/'))
        yaml_file = os.path.join(full, 'skill.yaml')
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                meta = yaml.safe_load(f) or {}
        except (OSError, yaml.YAMLError):
            continue
        if meta.get('skill_id') == skill_id:
            target_path = p
            break

    if target_path is None:
        print(f"  ERROR: skill_id '{skill_id}' not found under {SKILLS_DIR}")
        sys.exit(1)

    entry = build_entry(target_path)
    if entry is None:
        sys.exit(1)

    existing_skills[skill_id] = entry
    skills_list = list(existing_skills.values())
    write_output(skills_list)


def main():
    parser = argparse.ArgumentParser(description='Generate skill-positions.yaml')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--incremental', action='store_true', help='Append only new skills')
    group.add_argument('--skill-id', type=str, metavar='ID', help='Update or add a single skill by skill_id')
    args = parser.parse_args()

    if args.skill_id:
        cmd_skill(args.skill_id)
    elif args.incremental:
        cmd_incremental()
    else:
        cmd_full()


if __name__ == '__main__':
    main()
