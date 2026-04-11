from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPOLOGY_FILE = ROOT / "WORKSPACE-TOPOLOGY.md"
ALLOWED_DEPENDENCY_TYPES = {
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


def parse_spoke_repos(text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    section = get_section(text, "## Spoke Repos", "## Inter-Repo Dependency Map")
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


def validate_dependency_types(text: str) -> list[str]:
    errors: list[str] = []
    section = get_section(text, "## Inter-Repo Dependency Map", "## Workspace Routing Rules")
    rows = parse_table_rows(section)
    if len(rows) < 2:
        return ["Inter-Repo Dependency Map table is missing or malformed."]

    for row in rows[2:]:
        if len(row) < 3:
            continue
        dep_type = clean_cell(row[2])
        if not dep_type or dep_type.startswith("_("):
            continue
        if dep_type not in ALLOWED_DEPENDENCY_TYPES:
            errors.append(
                "Invalid dependency type in WORKSPACE-TOPOLOGY.md: "
                f"{dep_type} (allowed: {', '.join(sorted(ALLOWED_DEPENDENCY_TYPES))})"
            )

    return errors


def main() -> int:
    if not TOPOLOGY_FILE.exists():
        print(f"Missing required file: {TOPOLOGY_FILE}")
        return 1

    text = read_text(TOPOLOGY_FILE)
    _, errors = parse_spoke_repos(text)
    errors.extend(validate_dependency_types(text))

    if errors:
        print("Repo topology validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Repo topology validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
