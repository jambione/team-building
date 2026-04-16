#!/usr/bin/env python3
"""
Generate a reusable mission context packet for faster mission discovery.

This script snapshots key KB documents into one compact JSON file so discovery
can load one packet instead of reading multiple source documents each run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

DEFAULT_DOCS = [
    "knowledge_base/current/workspace-context.md",
    "knowledge_base/current/session-continuity.md",
    "knowledge_base/current/team-quick-reference.md",
    "knowledge_base/documents/past-lessons-learned.md",
]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def load_document(repo_root: Path, rel_path: str, max_lines: int) -> Dict[str, object]:
    doc_path = repo_root / rel_path
    result: Dict[str, object] = {
        "path": rel_path,
        "exists": doc_path.exists(),
    }

    if not doc_path.exists():
        return result

    raw = doc_path.read_text(encoding="utf-8", errors="ignore")
    lines = raw.splitlines()
    clipped = "\n".join(lines[:max_lines])
    stat = doc_path.stat()

    result.update(
        {
            "mtimeUtc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
            "sizeBytes": stat.st_size,
            "lineCount": len(lines),
            "capturedLineCount": min(len(lines), max_lines),
            "sha256": sha256_text(raw),
            "content": clipped,
        }
    )

    return result


def build_packet(repo_root: Path, docs: List[str], max_lines: int) -> Dict[str, object]:
    payload_docs = [load_document(repo_root, doc, max_lines) for doc in docs]
    return {
        "schemaVersion": 1,
        "generatedAtUtc": datetime.now(tz=timezone.utc).isoformat(),
        "repoRoot": str(repo_root),
        "documents": payload_docs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate mission context packet")
    parser.add_argument(
        "--output",
        default="knowledge_base/current/mission-context-packet.json",
        help="Packet output path relative to repo root",
    )
    parser.add_argument(
        "--docs",
        nargs="*",
        default=DEFAULT_DOCS,
        help="Relative document paths to include in the packet",
    )
    parser.add_argument(
        "--max-lines",
        type=int,
        default=250,
        help="Max lines captured per document",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    out_path = repo_root / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)

    packet = build_packet(repo_root=repo_root, docs=args.docs, max_lines=args.max_lines)
    out_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    included = sum(1 for doc in packet["documents"] if doc.get("exists"))
    total = len(packet["documents"])
    print(f"Context packet written: {out_path}")
    print(f"Documents included: {included}/{total}")


if __name__ == "__main__":
    main()
