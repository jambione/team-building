# Session Journal — 2026-04-19-15 phoenix-scss-mixin-consolidation

| Field              | Value                                                                     |
| ------------------ | ------------------------------------------------------------------------- |
| **Mission**        | phoenix-scss-mixin-consolidation                                          |
| **Date**           | 2026-04-19                                                                |
| **Status**         | closed                                                                    |
| **Target Repo**    | knowledge-components                                                      |
| **Session Type**   | Continuation (resumed from prior context — no separate Ready Room opened) |
| **Gates at Close** | lint ✅ · build-kc-library ✅                                             |

---

## Mission Objective

Perform a "same-substance-different-name" pattern analysis across the Phoenix code-summary renderer and editor SCSS files, consolidate duplicate style blocks into reusable canonical mixins in `_mixins.scss`, and bring the diagnosis renderer (the last un-themed component) onto the Phoenix mixin system.

---

## Decisions Made

1. **7 canonical mixins added** — `phoenix-code-input-grid`, `phoenix-code-renderer-grid`, `phoenix-grid-label`, `phoenix-row2-content`, `phoenix-simple-date-chip($padding)`, `phoenix-pill-empty`, `phoenix-mod-chip` — as the authoritative base for the code-cell design language.

2. **Thin-alias pattern adopted** — Existing `phoenix-hcpcs-*` and `phoenix-px-*` mixins kept as one-line wrappers calling the canonical mixins. No consumer files broken, backward compatibility preserved.

3. **`phoenix-dx-code-renderer` / `phoenix-dx-code-input` added** — DX-specific overrides (`color: var(--text-dark)`, `padding: 2px 5px`) isolated into named alias mixins rather than inlined at component level.

4. **`lib/code-summary` scoped out** — Confirmed to be a completely separate codebase (Optum legacy style system, Bootstrap, HTML tables). Phoenix mixin application there is a future mission — requires a full Optum → Phoenix token mapping pass first.

---

## Completions

| #   | Work Item                                                                                                                 | File(s) Changed                                                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 1   | Pattern analysis — 10 duplicate patterns identified                                                                       | (analysis only)                                                                        |
| 2   | 7 canonical mixins added to `_mixins.scss`                                                                                | `_mixins.scss`                                                                         |
| 3   | HCPCS mixin bodies collapsed to thin wrappers                                                                             | `_mixins.scss`                                                                         |
| 4   | PX mixin bodies collapsed to thin wrappers                                                                                | `_mixins.scss`                                                                         |
| 5   | `hcpcs-simple-renderer` inline blocks replaced with mixin calls                                                           | `hcpcs-simple-renderer.component.scss`                                                 |
| 6   | `px-simple-renderer` inline blocks replaced with mixin calls                                                              | `px-simple-renderer.component.scss`                                                    |
| 7   | `hcpcs-simple-editor` inline blocks replaced; `icon-bank` bug fixed (was not using existing `phoenix-dx-icon-bank` mixin) | `hcpcs-simple-editor.component.scss`                                                   |
| 8   | `px-simple-editor` inline block replaced                                                                                  | `px-simple-editor.component.scss`                                                      |
| 9   | `phoenix-dx-code-renderer` + `phoenix-dx-code-input` added; `dx-simple-renderer` + `dx-simple-editor` fully themed        | `_mixins.scss`, `dx-simple-renderer.component.scss`, `dx-simple-editor.component.scss` |
| 10  | Non-ASCII comment characters (`—`, `→`) fixed in new mixin comment lines                                                  | `_mixins.scss`                                                                         |
| 11  | Canonical section header comment added to `_mixins.scss` directing new component authors to use canonical mixins          | `_mixins.scss`                                                                         |

---

## Carry-Forward Items

None raised this session. The `lib/code-summary` → Phoenix migration is future scope, not a carry-forward defect.

---

## Discovery: `lib/code-summary` is a separate style universe

`projects/kc-lib/src/lib/code-summary/` (legacy) and `projects/kc-lib/src/lib/phoenix/code-summary/` (Phoenix) are not the same codebase:

- Legacy uses `@use '../shared/shared.scss'` (Optum `$optum*` SCSS variables)
- Phoenix uses `@use '../../_mixins'` (Phoenix CSS custom properties)
- Layout model differs: legacy = HTML tables + Bootstrap; Phoenix = CSS Grid + ag-Grid cell renderers
- Applying Phoenix styles to the legacy tree requires a full token mapping (Optum SCSS vars → Phoenix CSS vars) and structural HTML changes for the admit panel and button group

Captured in repo-discoveries/knowledge-components.md.
