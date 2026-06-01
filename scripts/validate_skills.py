#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md file.

Checks:
  1. The file has a YAML-style frontmatter block delimited by '---'.
  2. The frontmatter contains non-empty 'name' and 'description' fields.
  3. The 'name' value matches the parent directory name.

Exits with status 1 if any skill is invalid. No third-party dependencies.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Return a dict of top-level frontmatter keys, or None if absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return None  # closing '---' never found


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: skills directory not found at {SKILLS_DIR}")
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print(f"ERROR: no SKILL.md files found under {SKILLS_DIR}")
        return 1

    errors: list[str] = []
    for skill in skill_files:
        rel = skill.relative_to(ROOT)
        dir_name = skill.parent.name
        fm = parse_frontmatter(skill.read_text(encoding="utf-8"))
        if fm is None:
            errors.append(f"{rel}: missing or malformed frontmatter block")
            continue
        if not fm.get("name"):
            errors.append(f"{rel}: missing 'name' field")
        elif fm["name"] != dir_name:
            errors.append(
                f"{rel}: name '{fm['name']}' does not match directory '{dir_name}'"
            )
        if not fm.get("description"):
            errors.append(f"{rel}: missing 'description' field")

    if errors:
        print("Validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"Validation passed: {len(skill_files)} skill(s) OK")
    for skill in skill_files:
        print(f"  - {skill.parent.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
