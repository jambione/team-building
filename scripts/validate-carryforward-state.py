from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]


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


def parse_markdown_table(section_text: str) -> tuple[list[str], list[list[str]]]:
    lines = [line.strip() for line in section_text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return [], []

    header = [cell.strip() for cell in lines[0].strip("|").split("|")]
    rows: list[list[str]] = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        rows.append(cells)
    return header, rows


def clean(value: str) -> str:
    return value.replace("`", "").strip()


def is_placeholder_row(cells: list[str]) -> bool:
    if not cells:
        return True
    first = clean(cells[0])
    return first.startswith("_(") or first in {"—", "-", ""}


def valid_commit(value: str) -> bool:
    v = clean(value).lower()
    if v in {"n/a", "na"}:
        return True
    if re.fullmatch(r"[0-9a-f]{7,40}", v):
        return True
    return False


def validate_carry_forward_items(text: str) -> list[str]:
    errors: list[str] = []
    section = get_section(text, "## Carry-Forward Items", "## Cross-Repo Carry-Forwards")
    headers, rows = parse_markdown_table(section)
    if not headers:
        return ["Carry-Forward Items table is missing or malformed."]

    required = {"ID", "Item", "Owner", "Source Mission", "Priority", "Target Sprint"}
    missing = sorted(required - set(headers))
    if missing:
        errors.append("Carry-Forward Items table missing required columns: " + ", ".join(missing))
        return errors

    col = {name: headers.index(name) for name in required}
    for row in rows:
        if is_placeholder_row(row):
            continue
        if not clean(row[col["Source Mission"]]):
            errors.append("Carry-forward row missing Source Mission value.")

    return errors


def validate_cross_repo_items(text: str) -> list[str]:
    errors: list[str] = []
    section = get_section(text, "## Cross-Repo Carry-Forwards", "## Open Conditional Close Checklists")
    headers, rows = parse_markdown_table(section)
    if not headers:
        return ["Cross-Repo Carry-Forwards table is missing or malformed."]

    required = {
        "ID",
        "Item",
        "Source Mission",
        "Source Repo",
        "Source Commit",
        "Target Repo",
        "Owner",
        "Target Sprint",
    }
    missing = sorted(required - set(headers))
    if missing:
        errors.append("Cross-Repo Carry-Forwards table missing required columns: " + ", ".join(missing))
        return errors

    col = {name: headers.index(name) for name in required}
    for row in rows:
        if is_placeholder_row(row):
            continue

        source_mission = clean(row[col["Source Mission"]])
        source_repo = clean(row[col["Source Repo"]])
        source_commit = clean(row[col["Source Commit"]])
        target_repo = clean(row[col["Target Repo"]])

        if not source_mission:
            errors.append("Cross-repo carry-forward row missing Source Mission value.")
        if not source_repo:
            errors.append("Cross-repo carry-forward row missing Source Repo value.")
        if not target_repo:
            errors.append("Cross-repo carry-forward row missing Target Repo value.")
        if not valid_commit(source_commit):
            errors.append(
                "Cross-repo carry-forward Source Commit must be 7-40 hex SHA or 'n/a'."
            )

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate carry-forward provenance state.")
    parser.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Workspace root to validate (defaults to repository root).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    sprint_state = root / "knowledge_base" / "documents" / "sprint-state.md"
    if not sprint_state.exists():
        print(f"Missing required file: {sprint_state}")
        return 1

    text = read_text(sprint_state)
    errors: list[str] = []
    errors.extend(validate_carry_forward_items(text))
    errors.extend(validate_cross_repo_items(text))

    if errors:
        print("Carry-forward state validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Carry-forward state validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
