from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from workspace_config import get_nested, load_workspace_config


DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def run_python_script(root: Path, script_rel_path: str) -> int:
    script_path = root / script_rel_path
    cmd = [sys.executable, str(script_path)]
    proc = subprocess.run(cmd, cwd=root, text=True)
    return proc.returncode


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(root: Path, config: dict) -> list[str]:
    default_required = [
        "docs/reference/STATUS.md",
        "docs/reference/TEAM-TOPOLOGY.md",
        "scripts/validate-agent-structure.py",
        "scripts/kb-lint.py",
        "scripts/validate-discovery-kb-link.py",
        "scripts/validate-repo-topology.py",
        "scripts/validate-mission-manifests.py",
        "scripts/validate-carryforward-state.py",
        "scripts/validate-workspace.py",
        ".github/workflows/ci.yml",
        ".github/workflows/agent-structure-check.yml",
        ".github/workflows/kb-quality-check.yml",
        "knowledge_base/documents/index.md",
    ]

    required = get_nested(config, ["required_files"], default_required)
    if not isinstance(required, list):
        required = default_required

    errors: list[str] = []
    for rel in required:
        if not isinstance(rel, str) or not rel.strip():
            continue
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


def check_workflow_alignment(root: Path, config: dict) -> list[str]:
    errors: list[str] = []

    default_assertions = {
        "ci.yml": {
            "contains": [
                "python scripts/validate-workspace.py --check ci-core",
            ],
            "not_contains": ["npm ci"],
        },
        "agent-structure-check.yml": {
            "contains": [
                "docs/reference/TEAM-TOPOLOGY.md",
                "docs/reference/STATUS.md",
                "python scripts/validate-workspace.py --check agent-structure",
            ]
        },
        "kb-quality-check.yml": {
            "contains": [
                "python scripts/validate-workspace.py --check kb-quality",
            ]
        },
    }
    assertions = get_nested(config, ["workflow_assertions"], default_assertions)
    if not isinstance(assertions, dict):
        assertions = default_assertions

    workflow_dir = root / ".github" / "workflows"
    for filename, checks in assertions.items():
        if not isinstance(filename, str) or not isinstance(checks, dict):
            continue
        path = workflow_dir / filename
        label = filename
        for expected in checks.get("contains", []):
            if isinstance(expected, str):
                errors += assert_contains(path, expected, label)
        for forbidden in checks.get("not_contains", []):
            if isinstance(forbidden, str):
                errors += assert_not_contains(path, forbidden, label)

    return errors


def run_check(root: Path, check: str) -> int:
    config = load_workspace_config(root)
    errors: list[str] = []

    # Contract checks run for every mode to keep one strict entrypoint.
    errors.extend(check_required_files(root, config))
    errors.extend(check_workflow_alignment(root, config))

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

    if check in {"deterministic", "ci-core", "all"}:
        if run_python_script(root, "scripts/validate-repo-topology.py") != 0:
            return 1
        if run_python_script(root, "scripts/validate-mission-manifests.py") != 0:
            return 1
        if run_python_script(root, "scripts/validate-carryforward-state.py") != 0:
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
        choices=["all", "ci-core", "agent-structure", "kb-quality", "deterministic"],
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
