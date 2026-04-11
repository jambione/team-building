import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate-mission-manifests.py"


def write_file(root: Path, rel_path: str, content: str) -> None:
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def compute_replay_hash(payload: dict) -> str:
    data = dict(payload)
    data.pop("replay_hash", None)
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def valid_execution_plan() -> dict:
    plan = {
        "schema_version": "1.0.0",
        "mission_slug": "demo-multi-repo",
        "mission_type": "multi-repo",
        "repos": [
            {
                "repo": "org/repo-a",
                "branch": "mission/demo-multi-repo",
                "base_ref": "main",
                "final_commit_sha": "a1b2c3d",
                "role": "primary",
                "wave": 1,
                "notes": "",
            },
            {
                "repo": "org/repo-b",
                "branch": "mission/demo-multi-repo",
                "base_ref": "main",
                "final_commit_sha": "n/a",
                "role": "integration",
                "wave": 2,
                "notes": "",
            },
        ],
        "waves": [
            {"wave": 1, "repo": "org/repo-a", "gate_commit_sha": "n/a", "result": "pass"},
            {
                "wave": 2,
                "repo": "org/repo-b",
                "gate_commit_sha": "a1b2c3d",
                "result": "pass",
            },
        ],
        "replay_hash": "",
    }
    plan["replay_hash"] = compute_replay_hash(plan)
    return plan


class ValidateMissionManifestTests(unittest.TestCase):
    def build_fixture(self, root: Path, plan: dict) -> None:
        write_file(
            root,
            "workspace-config.json",
            json.dumps(
                {
                    "paths": {
                        "mission_index": "knowledge_base/missions/mission-index.md",
                    },
                    "mission_manifests": {
                        "schema_version": "1.0.0",
                        "schema_file": "knowledge_base/missions/schemas/mission-execution-plan.schema.json",
                        "registry_start": "## Mission Registry",
                        "registry_end": "## Status Key",
                        "required_headers": ["Date", "Slug", "Repo(s)", "Log", "Manifest"],
                        "manifest_marker": "## Mission Execution Manifest",
                        "ledger_header_regex": "^\\\\|\\\\s*Repo\\\\s*\\\\|\\\\s*Branch\\\\s*\\\\|\\\\s*Final\\\\s+Commit\\\\s+SHA\\\\s*\\\\|",
                    },
                },
                indent=2,
            )
            + "\n",
        )
        write_file(
            root,
            "knowledge_base/missions/schemas/mission-execution-plan.schema.json",
            json.dumps(
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "x-schema-version": "1.0.0",
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
                indent=2,
            )
            + "\n",
        )
        write_file(
            root,
            "knowledge_base/missions/mission-index.md",
            "# Mission Index\n\n"
            "## Mission Registry\n\n"
            "| Date | Slug | Repo(s) | Log | Manifest |\n"
            "| ---- | ---- | ------- | --- | -------- |\n"
            "| 2026-04-11 | `demo-multi-repo` | `org/repo-a`, `org/repo-b` | [→](2026-04-11-demo.md) | [→](manifests/2026-04-11-demo.manifest.md) |\n\n"
            "## Status Key\n",
        )
        write_file(
            root,
            "knowledge_base/missions/manifests/2026-04-11-demo.manifest.md",
            "## Mission Execution Manifest\n\n"
            "## Repo Execution Ledger\n\n"
            "| Repo | Branch | Final Commit SHA | Base Ref | Checkpoint Commit(s) | Role | Notes |\n"
            "| ---- | ------ | ---------------- | -------- | -------------------- | ---- | ----- |\n"
            "| `org/repo-a` | `mission/demo-multi-repo` | `a1b2c3d` | `main` | `n/a` | primary | |\n"
            "| `org/repo-b` | `mission/demo-multi-repo` | `n/a` | `main` | `n/a` | integration | |\n",
        )
        write_file(
            root,
            "knowledge_base/missions/manifests/2026-04-11-demo.manifest.json",
            json.dumps(plan, indent=2) + "\n",
        )

    def run_validator(self, root: Path):
        cmd = [
            sys.executable,
            str(VALIDATOR),
            "--root",
            str(root),
        ]
        return subprocess.run(cmd, text=True, capture_output=True)

    def test_validator_passes_with_valid_json_execution_plan(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            self.build_fixture(fixture_root, valid_execution_plan())

            result = self.run_validator(fixture_root)
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_validator_fails_when_replay_hash_is_invalid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            plan = valid_execution_plan()
            plan["replay_hash"] = "0" * 64
            self.build_fixture(fixture_root, plan)

            result = self.run_validator(fixture_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("replay_hash does not match canonical payload hash", result.stdout)

    def test_validator_fails_when_wave_gate_sha_does_not_match_upstream(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            plan = valid_execution_plan()
            plan["waves"][1]["gate_commit_sha"] = "deadbee"
            plan["replay_hash"] = compute_replay_hash(plan)
            self.build_fixture(fixture_root, plan)

            result = self.run_validator(fixture_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("gate_commit_sha must match a prior-wave final_commit_sha", result.stdout)


if __name__ == "__main__":
    unittest.main()
