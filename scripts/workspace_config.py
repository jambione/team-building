from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = DEFAULT_ROOT / "workspace-config.json"


def _normalize_config_path(root: Path, config_path: str | None) -> Path:
    if not config_path:
        return root / "workspace-config.json"
    path = Path(config_path)
    if path.is_absolute():
        return path
    return (root / path).resolve()


def load_workspace_config(root: Path, config_path: str | None = None) -> dict[str, Any]:
    path = _normalize_config_path(root, config_path)
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("workspace-config.json must contain a JSON object at the top level.")
    return data


def get_nested(config: dict[str, Any], keys: list[str], default: Any) -> Any:
    current: Any = config
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def get_rel_path(config: dict[str, Any], key: str, default: str) -> str:
    value = get_nested(config, ["paths", key], default)
    if not isinstance(value, str) or not value.strip():
        return default
    return value.strip()