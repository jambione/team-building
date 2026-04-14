"""
Direct unit tests for scripts/workspace_config.py.

These tests import the module directly (unlike the subprocess-based integration
tests in test_validate_workspace.py) so that pytest-cov can measure actual
coverage. This partially closes TD-010 (unit tests for validation scripts).
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

# workspace_config.py lives in scripts/ which is not a package; add it to path.
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from workspace_config import (  # noqa: E402
    _normalize_config_path,
    get_nested,
    get_rel_path,
    load_workspace_config,
)


class TestNormalizeConfigPath(unittest.TestCase):
    def test_returns_default_path_when_no_config_path(self):
        root = Path("/tmp/test-root")
        result = _normalize_config_path(root, None)
        self.assertEqual(result, root / "workspace-config.json")

    def test_returns_default_path_when_empty_string(self):
        root = Path("/tmp/test-root")
        result = _normalize_config_path(root, "")
        self.assertEqual(result, root / "workspace-config.json")

    def test_returns_absolute_path_unchanged(self):
        # Use a real temporary directory so the absolute path is valid on all OSes.
        with tempfile.TemporaryDirectory() as tmp:
            abs_config = str(Path(tmp) / "custom-config.json")
            root = Path("/tmp/some-other-root")
            result = _normalize_config_path(root, abs_config)
            self.assertEqual(result, Path(abs_config))

    def test_resolves_relative_path_under_root(self):
        root = Path("/tmp/test-root")
        result = _normalize_config_path(root, "subdir/config.json")
        self.assertEqual(result, (root / "subdir/config.json").resolve())


class TestLoadWorkspaceConfig(unittest.TestCase):
    def test_returns_empty_dict_when_file_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = load_workspace_config(Path(tmp))
            self.assertEqual(result, {})

    def test_returns_parsed_dict_when_file_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "workspace-config.json"
            cfg.write_text(json.dumps({"required_files": ["a.md"]}), encoding="utf-8")
            result = load_workspace_config(Path(tmp))
            self.assertEqual(result, {"required_files": ["a.md"]})

    def test_raises_value_error_when_top_level_is_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "workspace-config.json"
            cfg.write_text("[1, 2, 3]", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_workspace_config(Path(tmp))

    def test_raises_value_error_when_top_level_is_string(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "workspace-config.json"
            cfg.write_text('"just a string"', encoding="utf-8")
            with self.assertRaises(ValueError):
                load_workspace_config(Path(tmp))

    def test_explicit_config_path_overrides_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            custom = Path(tmp) / "custom.json"
            custom.write_text(json.dumps({"custom_key": True}), encoding="utf-8")
            result = load_workspace_config(Path(tmp), config_path=str(custom))
            self.assertEqual(result, {"custom_key": True})

    def test_absolute_config_path_found_outside_root(self):
        with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
            cfg = Path(tmp2) / "external.json"
            cfg.write_text(json.dumps({"external": True}), encoding="utf-8")
            result = load_workspace_config(Path(tmp1), config_path=str(cfg))
            self.assertEqual(result, {"external": True})


class TestGetNested(unittest.TestCase):
    def test_retrieves_value_at_single_key(self):
        self.assertEqual(get_nested({"x": 5}, ["x"], default=0), 5)

    def test_retrieves_deeply_nested_value(self):
        config = {"a": {"b": {"c": 99}}}
        self.assertEqual(get_nested(config, ["a", "b", "c"], default=None), 99)

    def test_returns_default_for_missing_top_level_key(self):
        self.assertEqual(get_nested({}, ["missing"], default="fallback"), "fallback")

    def test_returns_default_when_intermediate_key_absent(self):
        config = {"a": {"x": 1}}
        self.assertEqual(get_nested(config, ["a", "b"], default=42), 42)

    def test_returns_default_when_intermediate_value_is_not_dict(self):
        config = {"a": "not-a-dict"}
        self.assertEqual(get_nested(config, ["a", "b"], default="default"), "default")

    def test_returns_none_default_explicitly(self):
        self.assertIsNone(get_nested({}, ["missing"], default=None))

    def test_returns_falsy_value_correctly(self):
        self.assertEqual(get_nested({"flag": False}, ["flag"], default=True), False)

    def test_returns_zero_correctly(self):
        self.assertEqual(get_nested({"count": 0}, ["count"], default=1), 0)


class TestGetRelPath(unittest.TestCase):
    def test_returns_path_from_config(self):
        config = {"paths": {"sprint_state": "knowledge_base/documents/sprint-state.md"}}
        result = get_rel_path(config, "sprint_state", "default.md")
        self.assertEqual(result, "knowledge_base/documents/sprint-state.md")

    def test_returns_default_when_paths_section_missing(self):
        self.assertEqual(get_rel_path({}, "sprint_state", "default.md"), "default.md")

    def test_returns_default_when_key_missing_in_paths(self):
        config = {"paths": {"other_key": "other.md"}}
        self.assertEqual(get_rel_path(config, "sprint_state", "default.md"), "default.md")

    def test_returns_default_when_value_is_empty_string(self):
        config = {"paths": {"sprint_state": ""}}
        self.assertEqual(get_rel_path(config, "sprint_state", "default.md"), "default.md")

    def test_strips_whitespace_from_value(self):
        config = {"paths": {"sprint_state": "  path/to/file.md  "}}
        self.assertEqual(get_rel_path(config, "sprint_state", "default.md"), "path/to/file.md")

    def test_returns_default_when_value_is_not_a_string(self):
        config = {"paths": {"sprint_state": 123}}
        self.assertEqual(get_rel_path(config, "sprint_state", "default.md"), "default.md")

    def test_returns_default_when_value_is_whitespace_only(self):
        config = {"paths": {"sprint_state": "   "}}
        self.assertEqual(get_rel_path(config, "sprint_state", "default.md"), "default.md")


if __name__ == "__main__":
    unittest.main()
