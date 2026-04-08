from pathlib import Path
import os
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run_git(args: list[str]) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return proc.stdout


def changed_files(base_sha: str, head_sha: str) -> list[Path]:
    output = run_git(["diff", "--name-only", f"{base_sha}...{head_sha}"])
    files = []
    for line in output.splitlines():
        path = line.strip()
        if path:
            files.append(ROOT / path)
    return files


def file_contains_discovery(path: Path) -> bool:
    if not path.exists() or path.is_dir():
        return False
    if path.suffix.lower() not in {".md", ".txt", ".py", ".yml", ".yaml"}:
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    return "[NEW DISCOVERY]" in text or "NEW DISCOVERY" in text


def main() -> int:
    base_sha = os.environ.get("BASE_SHA")
    head_sha = os.environ.get("HEAD_SHA")

    if not base_sha or not head_sha:
        print("BASE_SHA and HEAD_SHA must be set.")
        return 1

    files = changed_files(base_sha, head_sha)
    discovery_paths = [p for p in files if file_contains_discovery(p)]
    kb_updates = [
        p
        for p in files
        if p.relative_to(ROOT).as_posix().startswith("knowledge_base/")
    ]

    if discovery_paths and not kb_updates:
        print("Discovery validation failed:")
        print("- Found NEW DISCOVERY markers but no knowledge_base/ files changed in this diff.")
        print("- Discovery files:")
        for path in discovery_paths:
            print(f"  - {path.relative_to(ROOT)}")
        return 1

    print("Discovery validation passed.")
    if discovery_paths:
        print(f"- NEW DISCOVERY markers found in {len(discovery_paths)} file(s).")
        print(f"- KB updates found in {len(kb_updates)} file(s).")
    else:
        print("- No NEW DISCOVERY markers found in changed files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
