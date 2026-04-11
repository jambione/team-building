from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def run_python_script(root: Path, script_rel_path: str) -> int:
    script_path = root / script_rel_path
    cmd = [sys.executable, str(script_path)]
    proc = subprocess.run(cmd, cwd=root, text=True)
    return proc.returncode


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(root: Path) -> list[str]:
    required = [
        "docs/reference/STATUS.md",
        "docs/reference/TEAM-TOPOLOGY.md",
        "scripts/validate-agent-structure.py",
        "scripts/kb-lint.py",
        "scripts/validate-discovery-kb-link.py",
        "scripts/validate-workspace.py",
        ".github/workflows/ci.yml",
        ".github/workflows/agent-structure-check.yml",
        ".github/workflows/kb-quality-check.yml",
        "knowledge_base/documents/index.md",
    ]
    errors: list[str] = []
    for rel in required:
        if not (root / rel).exists():
            errors.append(f"Missing required file: {rel}")
    return errors


def check_index_completeness(root: Path) -> list[str]:
    errors: list[str] = []
    index_file = root / "knowledge_base" / "documents" / "index.md"
    docs_dir = root / "knowledge_base" / "documents"
    if not index_file.exists():
        return ["knowledge_base/documents/index.md not found"]

    index_text = read_text(index_file)
    indexed_names = set(re.findall(r"`([A-Za-z0-9._-]+\.md)`", index_text))
    top_level_docs = {p.name for p in docs_dir.glob("*.md") if p.name != "index.md"}

    missing = sorted(top_level_docs - indexed_names)
    for name in missing:
        errors.append(f"index.md missing top-level document entry: {name}")

    return errors


def assert_contains(path: Path, expected: str, label: str) -> list[str]:
    text = read_text(path)
    if expected not in text:
        return [f"{label}: expected to contain '{expected}'"]
    return []


def assert_not_contains(path: Path, forbidden: str, label: str) -> list[str]:
    text = read_text(path)
    if forbidden in text:
        return [f"{label}: must not contain '{forbidden}'"]
    return []


def check_workflow_alignment(root: Path) -> list[str]:
    errors: list[str] = []

    ci = root / ".github" / "workflows" / "ci.yml"
    agent = root / ".github" / "workflows" / "agent-structure-check.yml"
    kb = root / ".github" / "workflows" / "kb-quality-check.yml"

    errors += assert_contains(
        ci,
        "python scripts/validate-workspace.py --check ci-core",
        "ci.yml",
    )
    errors += assert_not_contains(ci, "npm ci", "ci.yml")

    errors += assert_contains(
        agent,
        "docs/reference/TEAM-TOPOLOGY.md",
        "agent-structure-check.yml",
    )
    errors += assert_contains(
        agent,
        "docs/reference/STATUS.md",
        "agent-structure-check.yml",
    )
    errors += assert_contains(
        agent,
        "python scripts/validate-workspace.py --check agent-structure",
        "agent-structure-check.yml",
    )

    errors += assert_contains(
        kb,
        "python scripts/validate-workspace.py --check kb-quality",
        "kb-quality-check.yml",
    )

    return errors


def run_check(root: Path, check: str) -> int:
    errors: list[str] = []

    # Contract checks run for every mode to keep one strict entrypoint.
    errors.extend(check_required_files(root))
    errors.extend(check_workflow_alignment(root))

    if check in {"ci-core", "all"}:
        errors.extend(check_index_completeness(root))

    if errors:
        print("Workspace contract validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    if check in {"agent-structure", "ci-core", "all"}:
        if run_python_script(root, "scripts/validate-agent-structure.py") != 0:
            return 1

    if check in {"kb-quality", "ci-core", "all"}:
        if run_python_script(root, "scripts/kb-lint.py") != 0:
            return 1

    if check in {"kb-quality", "all"}:
        # Discovery check requires BASE_SHA and HEAD_SHA in env when used in CI.
        if "BASE_SHA" in os.environ and "HEAD_SHA" in os.environ:
            if run_python_script(root, "scripts/validate-discovery-kb-link.py") != 0:
                return 1
        else:
            print("Skipping discovery linkage check (BASE_SHA/HEAD_SHA not set).")

    print(f"Workspace validation passed for check mode: {check}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Unified workspace validation entrypoint.")
    parser.add_argument(
        "--check",
        choices=["all", "ci-core", "agent-structure", "kb-quality"],
        default="all",
        help="Validation profile to run.",
    )
    parser.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Workspace root to validate (defaults to repository root).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    return run_check(root, args.check)


if __name__ == "__main__":
    sys.exit(main())
