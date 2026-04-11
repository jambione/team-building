from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
KB_ROOT = ROOT / "knowledge_base"
DOCS_DIR = KB_ROOT / "documents"
CURRENT_DIR = KB_ROOT / "current"
ARCHIVE_DIR = KB_ROOT / "archive"
INDEX_FILE = DOCS_DIR / "index.md"


def index_doc_names(index_text: str) -> list[str]:
    # Only capture filename-style references; ignore full paths like knowledge_base/sessions/*.md.
    return re.findall(r"`([A-Za-z0-9._-]+\.md)`", index_text)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not INDEX_FILE.exists():
        print("KB lint failed: knowledge_base/documents/index.md not found.")
        return 1

    index_text = INDEX_FILE.read_text(encoding="utf-8")
    indexed_names = index_doc_names(index_text)
    indexed_set = set(indexed_names)

    # Check for duplicate index entries.
    seen: set[str] = set()
    dupes: set[str] = set()
    for name in indexed_names:
        if name in seen:
            dupes.add(name)
        seen.add(name)
    for duplicate in sorted(dupes):
        errors.append(f"index.md: duplicate entry '{duplicate}'")

    # Resolve indexed docs across docs/current/archive.
    searchable_dirs = [DOCS_DIR, CURRENT_DIR, ARCHIVE_DIR]
    for name in sorted(indexed_set):
        found = any((base / name).exists() for base in searchable_dirs)
        if not found:
            errors.append(
                f"index.md: referenced document '{name}' does not exist in documents/current/archive"
            )

    # Ensure top-level docs are indexed (excluding index itself).
    top_level_docs = sorted(p.name for p in DOCS_DIR.glob("*.md") if p.name != "index.md")
    for name in top_level_docs:
        if name not in indexed_set:
            warnings.append(f"index.md: top-level doc not indexed: '{name}'")

    # Surface very large docs as archive candidates.
    for doc in DOCS_DIR.glob("*.md"):
        if doc.name == "index.md":
            continue
        line_count = len(doc.read_text(encoding="utf-8").splitlines())
        if line_count > 350:
            warnings.append(
                f"{doc.relative_to(ROOT)}: {line_count} lines (consider moving to knowledge_base/archive/)"
            )

    if errors:
        print("KB lint failed:")
        for err in errors:
            print(f"- {err}")
        if warnings:
            print("KB lint warnings:")
            for warning in warnings:
                print(f"- {warning}")
        return 1

    print("KB lint passed.")
    if warnings:
        print("KB lint warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
