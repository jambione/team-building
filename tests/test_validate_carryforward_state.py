import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate-carryforward-state.py"


def write_file(root: Path, rel_path: str, content: str) -> None:
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sprint_state_content(*, source_mission: str = "`mission-a`", source_commit: str = "`abc1234`") -> str:
    return f"""# Sprint State

## Carry-Forward Items (from prior sprints)

| ID | Item | Owner | Source Mission | Priority | Target Sprint |
|----|------|-------|----------------|----------|---------------|
| CF-001 | Demo item | geordi | {source_mission} | P3 | Sprint 2 |

## Cross-Repo Carry-Forwards

| ID | Item | Source Mission | Source Repo | Source Commit | Target Repo | Owner | Target Sprint |
|----|------|----------------|-------------|---------------|-------------|-------|---------------|
| CF-X01 | Cross-repo dependency | `mission-a` | `org/service-a` | {source_commit} | `org/service-b` | riker | Sprint 2 |

## Open Conditional Close Checklists

| Mission Slug | Item | Owner | Due Sprint | Verification Criterion | Status |
|--------------|------|-------|------------|----------------------|--------|
| — | — | — | — | — | — |
"""


class ValidateCarryForwardStateTests(unittest.TestCase):
    def run_validator(self, root: Path):
        cmd = [
            sys.executable,
            str(VALIDATOR),
            "--root",
            str(root),
        ]
        return subprocess.run(cmd, text=True, capture_output=True, cwd=root)

    def test_validator_passes_with_valid_provenance(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            write_file(
                fixture_root,
                "knowledge_base/documents/sprint-state.md",
                sprint_state_content(),
            )

            result = self.run_validator(fixture_root)
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_validator_fails_when_source_mission_missing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            write_file(
                fixture_root,
                "knowledge_base/documents/sprint-state.md",
                sprint_state_content(source_mission=""),
            )

            result = self.run_validator(fixture_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Carry-forward row missing Source Mission value.", result.stdout)

    def test_validator_fails_when_source_commit_invalid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            write_file(
                fixture_root,
                "knowledge_base/documents/sprint-state.md",
                sprint_state_content(source_commit="`not-a-sha`"),
            )

            result = self.run_validator(fixture_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                "Cross-repo carry-forward Source Commit must be 7-40 hex SHA or 'n/a'.",
                result.stdout,
            )


if __name__ == "__main__":
    unittest.main()
