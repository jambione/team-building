# Testing Strategy — team-building

**Owner**: troi  
**Last Updated**: 2026-04-12  
**Closes**: TD-006 (TESTING.md placeholder)

---

## Purpose

This document defines the test strategy for the `team-building` hub repository — specifically the Python validation scripts in `scripts/`. It describes test types, coverage expectations, and how to run tests locally and in CI.

---

## Test Stack

| Tool | Role |
|------|------|
| `pytest` | Test runner (can run `unittest.TestCase` tests unchanged) |
| `pytest-cov` | Coverage measurement and threshold gate |
| `unittest` | Test case base class (all existing tests use it) |

Install test dependencies:
```bash
pip install -r requirements-dev.txt
```

---

## Test Types

### 1. Integration Tests (subprocess-based)

**Location**: `tests/test_validate_*.py`  
**Pattern**: Each test invokes a validation script as a subprocess and asserts on exit code and stdout.

These tests verify end-to-end script behaviour against temporary fixture directories. They are the primary safety net for the validation scripts (`validate-workspace.py`, `validate-carryforward-state.py`, `validate-mission-manifests.py`).

**Coverage measurement**: Subprocess-invoked scripts are excluded from direct coverage measurement (see `.coveragerc`). They are covered behaviourally by integration tests.

### 2. Unit Tests (direct import)

**Location**: `tests/test_workspace_config.py`  
**Pattern**: Directly imports `scripts/workspace_config.py` and tests each function with explicit inputs and edge cases.

These tests provide measurable line and branch coverage. The coverage gate (`--cov-fail-under=80`) applies to the modules measured by direct import.

**Coverage scope** (`.coveragerc`):
- **Measured**: `scripts/workspace_config.py` (importable, no hyphen in filename)
- **Excluded from measurement**: `scripts/validate-*.py`, `scripts/kb-lint.py` (subprocess-invoked; covered by integration tests)

> **Sprint 3 action (TD-010)**: Add direct-import tests for the hyphenated scripts using `importlib.util.spec_from_file_location`. This will expand the measured coverage scope and allow the `--cov-fail-under` threshold to be raised above 80%.

---

## Running Tests Locally

```bash
# All tests, with coverage report
pytest tests/ -v \
  --cov=scripts \
  --cov-config=.coveragerc \
  --cov-fail-under=80 \
  --cov-report=term-missing

# Specific test file
pytest tests/test_workspace_config.py -v

# Generate JUnit XML (same as CI)
pytest tests/ --junitxml=test-results.xml
```

---

## Coverage Threshold

| Current threshold | 80% |
|-------------------|-----|
| Scope | `scripts/workspace_config.py` |
| Baseline (2026-04-12) | 100% |
| Raise to | 90%+ once TD-010 (direct-import tests for validate-*.py) ships |

A CI run that passes without meeting the coverage threshold is a build failure. The threshold is enforced by `--cov-fail-under=80` in ci.yml.

---

## CI Integration

Tests run in the `validate-runtime-matrix` job across three legs:

| Matrix Leg | OS | Shell |
|-----------|-----|-------|
| linux-bash | ubuntu-latest | bash |
| linux-pwsh | ubuntu-latest | pwsh |
| windows-pwsh | windows-latest | pwsh |

Test result artifacts (JUnit XML) are uploaded from the `linux-bash` leg to the workflow run and retained for 30 days. Access them from the GitHub Actions run summary.

---

## File Naming Conventions

| Test type | Location | Naming |
|-----------|----------|--------|
| Integration | `tests/test_validate_<script-stem>.py` | Matches the script being tested |
| Unit | `tests/test_<module_name>.py` | Matches the importable module name |

---

## Adding New Tests

1. Create `tests/test_<target>.py`
2. Use `unittest.TestCase` as the base class (pytest will collect it)
3. For scripts with hyphens: use `importlib.util.spec_from_file_location` to import
4. For new importable modules: add to `--cov` scope in `.coveragerc` (remove from `omit` if applicable)
5. Run `pytest tests/ -v --cov=scripts --cov-config=.coveragerc --cov-fail-under=80` locally before pushing

---

_Created: 2026-04-12 | Owner: troi | Review cadence: Each sprint_
