import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate-workspace.py"


def write_file(root: Path, rel_path: str, content: str) -> None:
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def pass_script(name: str) -> str:
    return f"import sys\nprint('{name} ok')\nsys.exit(0)\n"


class ValidateWorkspaceTests(unittest.TestCase):
    def build_fixture(self, root: Path) -> None:
        write_file(root, "docs/reference/STATUS.md", "- `docs/reference/TEAM-TOPOLOGY.md`\n")
        write_file(root, "docs/reference/TEAM-TOPOLOGY.md", "team topology\n")

        write_file(root, "scripts/validate-agent-structure.py", pass_script("agent"))
        write_file(root, "scripts/kb-lint.py", pass_script("kb"))
        write_file(root, "scripts/validate-discovery-kb-link.py", pass_script("discovery"))
        write_file(root, "scripts/validate-repo-topology.py", pass_script("topology"))
        write_file(root, "scripts/validate-mission-manifests.py", pass_script("manifest"))
        write_file(root, "scripts/validate-carryforward-state.py", pass_script("carryforward"))
        # Required only for file-presence contract check.
        write_file(root, "scripts/validate-workspace.py", "# fixture placeholder\n")

        write_file(
            root,
            ".github/workflows/ci.yml",
            "name: CI\nrun: python scripts/validate-workspace.py --check ci-core\n",
        )
        write_file(
            root,
            ".github/workflows/agent-structure-check.yml",
            "name: Agent\n"
            "paths:\n"
            "  - docs/reference/TEAM-TOPOLOGY.md\n"
            "  - docs/reference/STATUS.md\n"
            "run: python scripts/validate-workspace.py --check agent-structure\n",
        )
        write_file(
            root,
            ".github/workflows/kb-quality-check.yml",
            "name: KB\nrun: python scripts/validate-workspace.py --check kb-quality\n",
        )

        write_file(root, "knowledge_base/documents/a.md", "doc A\n")
        write_file(
            root,
            "knowledge_base/documents/index.md",
            "# Index\n- `a.md`\n",
        )

    def run_validator(self, root: Path, check: str):
        cmd = [
            sys.executable,
            str(VALIDATOR),
            "--check",
            check,
            "--root",
            str(root),
        ]
        return subprocess.run(cmd, text=True, capture_output=True)

    def test_ci_core_passes_on_valid_fixture(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            self.build_fixture(fixture_root)

            result = self.run_validator(fixture_root, "ci-core")
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_fails_on_status_path_drift(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            self.build_fixture(fixture_root)
            (fixture_root / "docs/reference/STATUS.md").unlink()

            result = self.run_validator(fixture_root, "agent-structure")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Missing required file: docs/reference/STATUS.md", result.stdout)

    def test_fails_when_index_missing_top_level_doc(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture_root = Path(temp_dir)
            self.build_fixture(fixture_root)
            write_file(fixture_root, "knowledge_base/documents/new-top-level.md", "extra\n")

            result = self.run_validator(fixture_root, "ci-core")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                "index.md missing top-level document entry: new-top-level.md",
                result.stdout,
            )


if __name__ == "__main__":
    unittest.main()
