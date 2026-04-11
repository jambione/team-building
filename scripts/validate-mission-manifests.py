from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from workspace_config import get_nested, get_rel_path, load_workspace_config


ROOT = Path(__file__).resolve().parents[1]
VALID_SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


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


def is_sha_or_na(value: str) -> bool:
    cleaned = value.replace("`", "").strip().lower()
    return cleaned in {"n/a", "na"} or bool(VALID_SHA_RE.fullmatch(cleaned))


def canonical_hash(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def validate_schema_contract(schema_path: Path, expected_schema_version: str) -> list[str]:
    if not schema_path.exists():
        return [f"Mission execution schema file not found: {schema_path}"]

    try:
        schema = json.loads(read_text(schema_path))
    except json.JSONDecodeError as exc:
        return [f"Mission execution schema is not valid JSON ({schema_path}): {exc}"]

    if not isinstance(schema, dict):
        return [f"Mission execution schema must be a JSON object: {schema_path}"]

    errors: list[str] = []
    for key in ["$schema", "type", "properties", "required"]:
        if key not in schema:
            errors.append(f"Mission execution schema missing top-level field '{key}': {schema_path}")

    schema_version = str(schema.get("x-schema-version", ""))
    if schema_version != expected_schema_version:
        errors.append(
            "Mission execution schema version mismatch: "
            f"expected '{expected_schema_version}' got '{schema_version}' ({schema_path})"
        )

    return errors


def validate_json_manifest(
    json_manifest_path: Path,
    expected_repos: list[str],
    expected_schema_version: str,
) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(read_text(json_manifest_path))
    except json.JSONDecodeError as exc:
        return [f"JSON manifest is not valid JSON ({json_manifest_path}): {exc}"]

    if not isinstance(data, dict):
        return [f"JSON manifest must be an object: {json_manifest_path}"]

    required_top_level = {
        "schema_version",
        "mission_slug",
        "mission_type",
        "repos",
        "waves",
        "replay_hash",
    }
    for key in sorted(required_top_level):
        if key not in data:
            errors.append(f"JSON manifest missing required field '{key}': {json_manifest_path}")

    schema_version = str(data.get("schema_version", ""))
    if schema_version != expected_schema_version:
        errors.append(
            "JSON manifest schema_version mismatch: "
            f"expected '{expected_schema_version}' got '{schema_version}' ({json_manifest_path})"
        )

    if data.get("mission_type") != "multi-repo":
        errors.append(f"JSON manifest mission_type must be 'multi-repo': {json_manifest_path}")

    repos = data.get("repos", [])
    if not isinstance(repos, list) or not repos:
        errors.append(f"JSON manifest repos must be a non-empty list: {json_manifest_path}")
        repos = []

    repo_names_seen: set[str] = set()
    repo_to_final_sha: dict[str, str] = {}
    repo_to_wave: dict[str, int] = {}
    for idx, repo_entry in enumerate(repos, start=1):
        prefix = f"JSON manifest repos[{idx}]"
        if not isinstance(repo_entry, dict):
            errors.append(f"{prefix} must be an object: {json_manifest_path}")
            continue

        for field in ["repo", "branch", "base_ref", "final_commit_sha", "role", "wave"]:
            if field not in repo_entry:
                errors.append(f"{prefix} missing required field '{field}': {json_manifest_path}")

        repo_name = str(repo_entry.get("repo", "")).strip()
        if not repo_name:
            errors.append(f"{prefix}.repo must be non-empty: {json_manifest_path}")
            continue

        if repo_name in repo_names_seen:
            errors.append(f"JSON manifest has duplicate repo entry '{repo_name}': {json_manifest_path}")
        repo_names_seen.add(repo_name)

        final_commit_sha = str(repo_entry.get("final_commit_sha", "")).strip()
        if not is_sha_or_na(final_commit_sha):
            errors.append(
                f"{prefix}.final_commit_sha must be 7-40 hex SHA or n/a: {json_manifest_path}"
            )
        repo_to_final_sha[repo_name] = final_commit_sha.replace("`", "").strip().lower()

        wave_value = repo_entry.get("wave")
        if not isinstance(wave_value, int) or wave_value < 1:
            errors.append(f"{prefix}.wave must be an integer >= 1: {json_manifest_path}")
        else:
            repo_to_wave[repo_name] = wave_value

    expected_repo_set = {repo for repo in expected_repos if repo}
    if expected_repo_set != repo_names_seen:
        missing = sorted(expected_repo_set - repo_names_seen)
        extra = sorted(repo_names_seen - expected_repo_set)
        if missing:
            errors.append(
                "JSON manifest missing repos from mission index: "
                f"{', '.join(missing)} ({json_manifest_path})"
            )
        if extra:
            errors.append(
                "JSON manifest has extra repos not listed in mission index: "
                f"{', '.join(extra)} ({json_manifest_path})"
            )

    waves = data.get("waves", [])
    if not isinstance(waves, list) or not waves:
        errors.append(f"JSON manifest waves must be a non-empty list: {json_manifest_path}")
        waves = []

    for idx, wave_entry in enumerate(waves, start=1):
        prefix = f"JSON manifest waves[{idx}]"
        if not isinstance(wave_entry, dict):
            errors.append(f"{prefix} must be an object: {json_manifest_path}")
            continue

        for field in ["wave", "repo", "gate_commit_sha", "result"]:
            if field not in wave_entry:
                errors.append(f"{prefix} missing required field '{field}': {json_manifest_path}")

        wave_number = wave_entry.get("wave")
        repo_name = str(wave_entry.get("repo", "")).strip()
        gate_commit_sha = str(wave_entry.get("gate_commit_sha", "")).replace("`", "").strip().lower()
        result = str(wave_entry.get("result", "")).strip().lower()

        if not isinstance(wave_number, int) or wave_number < 1:
            errors.append(f"{prefix}.wave must be an integer >= 1: {json_manifest_path}")
        if repo_name not in repo_names_seen:
            errors.append(f"{prefix}.repo is not present in repos ledger: {json_manifest_path}")
        if result not in {"pass", "fail"}:
            errors.append(f"{prefix}.result must be 'pass' or 'fail': {json_manifest_path}")

        if isinstance(wave_number, int) and wave_number > 1:
            upstream_shas = {
                sha
                for repo, sha in repo_to_final_sha.items()
                if repo_to_wave.get(repo, 0) < wave_number and VALID_SHA_RE.fullmatch(sha)
            }
            if upstream_shas:
                if not VALID_SHA_RE.fullmatch(gate_commit_sha):
                    errors.append(
                        f"{prefix}.gate_commit_sha must be a concrete upstream SHA for wave > 1: {json_manifest_path}"
                    )
                elif gate_commit_sha not in upstream_shas:
                    errors.append(
                        f"{prefix}.gate_commit_sha must match a prior-wave final_commit_sha: {json_manifest_path}"
                    )
            elif gate_commit_sha not in {"n/a", "na"}:
                errors.append(
                    f"{prefix}.gate_commit_sha must be n/a when no prior-wave concrete SHA exists: {json_manifest_path}"
                )

    replay_hash = str(data.get("replay_hash", "")).strip().lower()
    if not SHA256_RE.fullmatch(replay_hash):
        errors.append(f"JSON manifest replay_hash must be a 64-char sha256 hex: {json_manifest_path}")
    else:
        payload = dict(data)
        payload.pop("replay_hash", None)
        expected_hash = canonical_hash(payload)
        if replay_hash != expected_hash:
            errors.append(
                "JSON manifest replay_hash does not match canonical payload hash: "
                f"expected {expected_hash} ({json_manifest_path})"
            )

    return errors


def validate_manifest_content(
    manifest_path: Path,
    repo_value: str,
    manifest_marker: str,
    ledger_header_regex: str,
) -> list[str]:
    errors: list[str] = []
    text = read_text(manifest_path)

    if manifest_marker not in text:
        errors.append(
            f"Manifest missing required marker '{manifest_marker}': "
            f"{manifest_path}"
        )

    # Allow normalized or formatter-aligned markdown tables.
    ledger_header_pattern = re.compile(ledger_header_regex, flags=re.MULTILINE)
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate mission manifest coverage.")
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

    mission_index_rel = get_rel_path(config, "mission_index", "knowledge_base/missions/mission-index.md")
    mission_index = root / mission_index_rel

    registry_start = get_nested(config, ["mission_manifests", "registry_start"], "## Mission Registry")
    registry_end = get_nested(config, ["mission_manifests", "registry_end"], "## Status Key")
    required_headers = get_nested(
        config,
        ["mission_manifests", "required_headers"],
        ["Date", "Slug", "Repo(s)", "Log", "Manifest"],
    )
    manifest_marker = get_nested(
        config,
        ["mission_manifests", "manifest_marker"],
        "## Mission Execution Manifest",
    )
    schema_version = str(
        get_nested(
            config,
            ["mission_manifests", "schema_version"],
            "1.0.0",
        )
    )
    schema_rel = str(
        get_nested(
            config,
            ["mission_manifests", "schema_file"],
            "knowledge_base/missions/schemas/mission-execution-plan.schema.json",
        )
    )
    schema_path = root / schema_rel
    ledger_header_regex = get_nested(
        config,
        ["mission_manifests", "ledger_header_regex"],
        r"^\|\s*Repo\s*\|\s*Branch\s*\|\s*Final\s+Commit\s+SHA\s*\|",
    )

    if not mission_index.exists():
        print(f"Missing required file: {mission_index}")
        return 1

    index_text = read_text(mission_index)
    start = index_text.find(str(registry_start))
    end = index_text.find(str(registry_end))
    if start == -1:
        print("Mission index validation failed: missing '## Mission Registry' section.")
        return 1

    section = index_text[start:end] if end != -1 else index_text[start:]
    headers, rows = parse_markdown_table(section)
    if not headers:
        print("Mission index validation failed: mission registry table is missing or malformed.")
        return 1

    required_headers_set = {
        value for value in required_headers if isinstance(value, str) and value.strip()
    }
    missing_headers = sorted(required_headers_set - set(headers))
    if missing_headers:
        print("Mission index validation failed: missing required columns:")
        for header in missing_headers:
            print(f"- {header}")
        return 1

    errors: list[str] = []
    errors.extend(validate_schema_contract(schema_path, schema_version))
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

        manifest_path = (mission_index.parent / manifest_target).resolve()
        if not manifest_path.exists():
            errors.append(f"Manifest file not found: {manifest_target}")
            continue

        repo_names = [clean_repo_name(part) for part in repo_value.split(",") if clean_repo_name(part)]

        json_manifest_path = manifest_path.with_suffix(".json")
        if not json_manifest_path.exists():
            errors.append(
                "Multi-repo mission must include JSON execution plan sibling file: "
                f"{json_manifest_path}"
            )
            continue

        errors.extend(validate_json_manifest(json_manifest_path, repo_names, schema_version))

        errors.extend(
            validate_manifest_content(
                manifest_path,
                repo_value,
                str(manifest_marker),
                str(ledger_header_regex),
            )
        )

    if errors:
        print("Mission manifest validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Mission manifest validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
