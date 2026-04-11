from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / ".github" / "agents"
STATUS_FILE = ROOT / "docs" / "reference" / "STATUS.md"


def parse_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    return parts[1]


def parse_list_block(frontmatter: str, key: str) -> list[str]:
    pattern = rf"(?ms)^{re.escape(key)}:\s*\n((?:\s+-\s+[^\n]+\n)*)"
    match = re.search(pattern, frontmatter)
    if not match:
        return []
    block = match.group(1)
    return [line.strip()[2:].strip() for line in block.splitlines() if line.strip().startswith("- ")]


def parse_handoff_targets(frontmatter: str) -> list[str]:
    return re.findall(r"(?m)^\s+-\s+to:\s*([a-z0-9\-]+)\s*$", frontmatter)


def parse_status_entries(text: str) -> list[str]:
    # STATUS.md paths are documented as markdown list items in backticks.
    return re.findall(r"(?m)^-\s+`([^`]+)`\s*$", text)


def main() -> int:
    files = sorted(AGENTS_DIR.glob("*.agent.md"))
    if not files:
        print("No agent files found.")
        return 1

    known_agents = {f.name.replace(".agent.md", "") for f in files}
    errors: list[str] = []

    picard_agents: list[str] = []
    picard_handoffs: list[str] = []

    for file in files:
        text = file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm:
            errors.append(f"{file}: missing or malformed frontmatter")
            continue

        handoff_targets = parse_handoff_targets(fm)
        for target in handoff_targets:
            if target not in known_agents:
                errors.append(f"{file}: handoff target '{target}' does not map to an agent file")

        if file.name == "picard.agent.md":
            picard_agents = parse_list_block(fm, "agents")
            picard_handoffs = handoff_targets

    if not picard_agents:
        errors.append("picard.agent.md: no agents list found")
    if not picard_handoffs:
        errors.append("picard.agent.md: no handoffs found")

    for target in picard_handoffs:
        if target not in picard_agents:
            errors.append(
                f"picard.agent.md: handoff target '{target}' is missing from picard agents list"
            )

    if not STATUS_FILE.exists():
        errors.append("docs/reference/STATUS.md: file not found")
    else:
        status_text = STATUS_FILE.read_text(encoding="utf-8")
        status_paths = parse_status_entries(status_text)
        if not status_paths:
            errors.append("docs/reference/STATUS.md: no file path entries found")
        for rel_path in status_paths:
            if rel_path.startswith("/"):
                errors.append(f"docs/reference/STATUS.md: path '{rel_path}' must be repo-relative")
                continue
            file_path = ROOT / rel_path
            if not file_path.exists():
                errors.append(
                    f"docs/reference/STATUS.md: referenced path does not exist: '{rel_path}'"
                )

    if errors:
        print("Agent structure validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Agent structure validation passed.")
    print(f"Validated {len(files)} agent files.")
    print("Validated docs/reference/STATUS.md references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
