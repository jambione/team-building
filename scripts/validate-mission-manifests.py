from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MISSION_INDEX = ROOT / "knowledge_base" / "missions" / "mission-index.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_markdown_table(section_text: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = [line.strip() for line in section_text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return [], []

    header = [cell.strip() for cell in lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return header, rows


def extract_link_target(cell_value: str) -> str | None:
    match = re.search(r"\[[^\]]*\]\(([^)]+)\)", cell_value)
    if not match:
        return None
    return match.group(1).strip()


def clean_repo_name(raw_value: str) -> str:
    return raw_value.replace("`", "").strip()


def is_multi_repo(repo_value: str) -> bool:
    cleaned = clean_repo_name(repo_value)
    return "," in cleaned


def validate_manifest_content(manifest_path: Path, repo_value: str) -> list[str]:
    errors: list[str] = []
    text = read_text(manifest_path)

    if "## Mission Execution Manifest" not in text:
        errors.append(
            "Manifest missing required marker '## Mission Execution Manifest': "
            f"{manifest_path}"
        )

    # Allow normalized or formatter-aligned markdown tables.
    ledger_header_pattern = re.compile(
        r"^\|\s*Repo\s*\|\s*Branch\s*\|\s*Final\s+Commit\s+SHA\s*\|",
        flags=re.MULTILINE,
    )
    if not ledger_header_pattern.search(text):
        errors.append(
            "Manifest missing required Repo Execution Ledger header columns: "
            f"{manifest_path}"
        )

    repo_names = [clean_repo_name(part) for part in repo_value.split(",") if clean_repo_name(part)]
    for repo in repo_names:
        if repo not in text:
            errors.append(f"Manifest does not reference repo '{repo}': {manifest_path}")

    return errors


def main() -> int:
    if not MISSION_INDEX.exists():
        print(f"Missing required file: {MISSION_INDEX}")
        return 1

    index_text = read_text(MISSION_INDEX)
    start = index_text.find("## Mission Registry")
    end = index_text.find("## Status Key")
    if start == -1:
        print("Mission index validation failed: missing '## Mission Registry' section.")
        return 1

    section = index_text[start:end] if end != -1 else index_text[start:]
    headers, rows = parse_markdown_table(section)
    if not headers:
        print("Mission index validation failed: mission registry table is missing or malformed.")
        return 1

    required_headers = {"Date", "Slug", "Repo(s)", "Log", "Manifest"}
    missing_headers = sorted(required_headers - set(headers))
    if missing_headers:
        print("Mission index validation failed: missing required columns:")
        for header in missing_headers:
            print(f"- {header}")
        return 1

    errors: list[str] = []
    for row in rows:
        repo_value = row.get("Repo(s)", "")
        if not is_multi_repo(repo_value):
            continue

        manifest_value = row.get("Manifest", "").strip()
        if manifest_value in {"", "-", "—"}:
            errors.append(
                "Multi-repo mission is missing manifest link for slug "
                f"{row.get('Slug', '<unknown>')}"
            )
            continue

        manifest_target = extract_link_target(manifest_value)
        if not manifest_target:
            errors.append(
                "Multi-repo mission manifest cell must be a markdown link for slug "
                f"{row.get('Slug', '<unknown>')}"
            )
            continue

        manifest_path = (MISSION_INDEX.parent / manifest_target).resolve()
        if not manifest_path.exists():
            errors.append(f"Manifest file not found: {manifest_target}")
            continue

        errors.extend(validate_manifest_content(manifest_path, repo_value))

    if errors:
        print("Mission manifest validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Mission manifest validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
