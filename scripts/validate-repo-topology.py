from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from workspace_config import get_nested, get_rel_path, load_workspace_config


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ALLOWED_DEPENDENCY_TYPES = {
    "api-contract",
    "shared-lib",
    "build-order",
    "data-schema",
    "config",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def get_section(text: str, start_heading: str, end_heading: str | None = None) -> str:
    start = text.find(start_heading)
    if start == -1:
        return ""
    if end_heading is None:
        return text[start:]
    end = text.find(end_heading, start)
    if end == -1:
        return text[start:]
    return text[start:end]


def parse_table_rows(section_text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in section_text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        # Skip markdown header separators.
        if re.fullmatch(r"\|[-|\s:]+\|?", line):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        rows.append(parts)
    return rows


def clean_cell(value: str) -> str:
    return value.replace("`", "").strip()


def parse_spoke_repos(text: str, spoke_start: str, spoke_end: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    section = get_section(text, spoke_start, spoke_end)
    rows = parse_table_rows(section)
    if len(rows) < 2:
        return [], ["Spoke Repos table is missing or malformed."]

    data_rows = rows[2:]
    repos: list[str] = []
    for row in data_rows:
        if not row:
            continue
        repo = clean_cell(row[0])
        if not repo or repo.startswith("_("):
            continue
        repos.append(repo)

    duplicates = sorted({repo for repo in repos if repos.count(repo) > 1})
    for repo in duplicates:
        errors.append(f"Duplicate spoke repo entry in WORKSPACE-TOPOLOGY.md: {repo}")

    return repos, errors


def validate_dependency_types(
    text: str,
    dependency_start: str,
    dependency_end: str,
    allowed_dependency_types: set[str],
) -> list[str]:
    errors: list[str] = []
    section = get_section(text, dependency_start, dependency_end)
    rows = parse_table_rows(section)
    if len(rows) < 2:
        return ["Inter-Repo Dependency Map table is missing or malformed."]

    for row in rows[2:]:
        if len(row) < 3:
            continue
        dep_type = clean_cell(row[2])
        if not dep_type or dep_type.startswith("_("):
            continue
        if dep_type not in allowed_dependency_types:
            errors.append(
                "Invalid dependency type in WORKSPACE-TOPOLOGY.md: "
                f"{dep_type} (allowed: {', '.join(sorted(allowed_dependency_types))})"
            )

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate workspace repo topology.")
    parser.add_argument(
        "--root",
        default=str(ROOT),
        help="Workspace root to validate (defaults to repository root).",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Optional workspace config path (absolute or relative to --root).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    config = load_workspace_config(root, args.config)

    topology_rel_path = get_rel_path(config, "topology", "WORKSPACE-TOPOLOGY.md")
    topology_file = root / topology_rel_path

    spoke_start = get_nested(config, ["topology", "spoke_section_start"], "## Spoke Repos")
    spoke_end = get_nested(
        config,
        ["topology", "spoke_section_end"],
        "## Inter-Repo Dependency Map",
    )
    dependency_start = get_nested(
        config,
        ["topology", "dependency_section_start"],
        "## Inter-Repo Dependency Map",
    )
    dependency_end = get_nested(
        config,
        ["topology", "dependency_section_end"],
        "## Workspace Routing Rules",
    )
    allowed_dep_types = get_nested(
        config,
        ["topology", "allowed_dependency_types"],
        sorted(DEFAULT_ALLOWED_DEPENDENCY_TYPES),
    )
    allowed_dep_types_set = {
        value for value in allowed_dep_types if isinstance(value, str) and value.strip()
    } or DEFAULT_ALLOWED_DEPENDENCY_TYPES

    if not topology_file.exists():
        print(f"Missing required file: {topology_file}")
        return 1

    text = read_text(topology_file)
    _, errors = parse_spoke_repos(text, str(spoke_start), str(spoke_end))
    errors.extend(
        validate_dependency_types(
            text,
            str(dependency_start),
            str(dependency_end),
            allowed_dep_types_set,
        )
    )

    if errors:
        print("Repo topology validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Repo topology validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
