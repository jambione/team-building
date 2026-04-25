# Repo Discovery — knowledge-components

**Owner**: data | **Last Updated**: 2026-04-24 (kc-lib-ecac-integration-familiarization)

---

## Overview

| Field              | Value                                                                             |
| ------------------ | --------------------------------------------------------------------------------- |
| **Repo Name**      | knowledge-components                                                              |
| **Service Domain** | Healthcare coding, billing, grouping, and claims processing                       |
| **Tech Stack**     | .NET 6/8 (ASP.NET Core), Angular 19+, SQL Server, ag-Grid, Angular Material, RxJS |
| **Owner Agent**    | data                                                                              |
| **Hub Repo**       | team-building                                                                     |

Healthcare coding application with ASP.NET Core microservices backend and Angular frontend. Provides ICD-9/ICD-10 coding logic, grouper/pricer engines, label services, and an encoder UI.

---

## Feature Map

_What the crew has explored. Updated after every mission that touches this repo._

| Feature Area                                  | Location                                                                                                                                    | Purpose                                                                                                                   | Key Services / Components                                                                                                          | Last Explored |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Encoder — Coding Logic                        | `KnowledgeComponents/AngularApp/projects/kc-lib/src/lib/encoder/coding-logic/`                                                              | Search normalization, code lookup, and initial terminology resolution for the encoder UI                                  | `InitialTerminologyService`, `initial-terminology.service.spec.ts`                                                                 | 2026-04-16    |
| Encoder — Cell Renderers                      | `KnowledgeComponents/AngularApp/projects/kc-lib/src/lib/encoder/`                                                                           | ag-Grid cell renderers for encoder result display                                                                         | `px-simple-renderer`, `hcpcs-simple-renderer`                                                                                      | 2026-04-15    |
| Code Summary Sidebar                          | `KnowledgeComponents/AngularApp/projects/kc-app/`                                                                                           | Sidebar component displaying selected code summaries                                                                      | `code-summary-sidebar.component`                                                                                                   | 2026-04-15    |
| Context Menus (Phoenix)                       | `KnowledgeComponents/AngularApp/projects/kc-lib/src/lib/shared/context-menus/`                                                              | Custom CDK-overlay context menu system used by Phoenix code-summary grids                                                 | `ContextMenuService`, `MenuComponent`, `DiagnosisMenuOptionsComponent`, `ProcedureMenuOptionsComponent` et al                      | 2026-04-16    |
| Phoenix code-summary — renderer/editor family | `KnowledgeComponents/AngularApp/projects/kc-lib/src/lib/phoenix/code-summary/diagnosis-renderer/`, `hcpcs-renderer/`, `procedure-renderer/` | Six ag-Grid cell renderer/editor components (DX, HCPCS, PX); all styles managed via `_mixins.scss` canonical mixin system | `dx-simple-renderer`, `dx-simple-editor`, `hcpcs-simple-renderer`, `hcpcs-simple-editor`, `px-simple-renderer`, `px-simple-editor` | 2026-04-19    |
| Phoenix SCSS mixin system                     | `KnowledgeComponents/AngularApp/projects/kc-lib/src/lib/phoenix/_mixins.scss`                                                               | Two-tier canonical + alias mixin system for code-cell design language                                                     | `phoenix-code-input-grid`, `phoenix-code-renderer-grid`, `phoenix-simple-date-chip`, etc.                                          | 2026-04-19    |
| Legacy code-summary (boundary)                | `KnowledgeComponents/AngularApp/projects/kc-lib/src/lib/code-summary/`                                                                      | Legacy Optum-styled code summary — separate from Phoenix; uses `shared.scss`, Bootstrap, HTML tables                      | `code-summary.component`, `associated-code-dialog`, `critical-edits-modal`, `rem-codes-dialog`                                     | 2026-04-19    |
| Shared Library (kc-lib)                       | `KnowledgeComponents/AngularApp/projects/kc-lib/`                                                                                           | Reusable Angular components, services, and utilities shared across kc-app and kc-auth-admin                               | Exports via `public-api.ts`                                                                                                        | 2026-04-15    |
| Shared Library Packaging (kc-lib npm)         | `KnowledgeComponents/AngularApp/projects/kc-lib/`, `KnowledgeComponents/AngularApp/angular.json`, `.github/workflows/kc-build.yml`          | ng-packagr packaging of kc-lib as npm artifact consumed by external repos                                                 | `ng-package.json`, `package.json` (`@optum-knowledge-components/knowledge-components`), `build-kc-library` workflow step           | 2026-04-24    |
| Auth Admin UI                                 | `KnowledgeComponents/AngularApp/projects/kc-auth-admin/`                                                                                    | Authentication and administration interface                                                                               | —                                                                                                                                  | —             |
| SMART Launch                                  | `KnowledgeComponents/AngularApp/projects/smartapp-launch/`                                                                                  | SMART on FHIR launch application                                                                                          | —                                                                                                                                  | —             |
| Backend — CodingLogic                         | `KnowledgeComponents.CodingLogic/`                                                                                                          | ICD-9/ICD-10 coding logic, validation, and code search (ASP.NET Core Web API)                                             | —                                                                                                                                  | —             |
| Backend — CodingBook                          | `KnowledgeComponents.CodingBook/`                                                                                                           | Coding reference data, tabular services, and code books                                                                   | —                                                                                                                                  | —             |
| Backend — EGP                                 | `KnowledgeComponents.EditGroupPrice/`                                                                                                       | Claims grouping and pricing engine                                                                                        | —                                                                                                                                  | —             |
| Backend — AutoEGP                             | `KnowledgeComponents.AutoEditGroupPrice/`                                                                                                   | Automated grouping workflows and batch processing                                                                         | —                                                                                                                                  | —             |
| Backend — Label                               | `KnowledgeComponents.Label/`                                                                                                                | Coding label services and management                                                                                      | —                                                                                                                                  | —             |
| Backend — Shared                              | `KnowledgeComponents.Shared/`                                                                                                               | Common utilities, models, logging, DB helpers, WebAPI clients, auth, caching                                              | `IRequestLog`, `ISqlHelper`, WebAPI typed clients                                                                                  | —             |

---

## Architecture Discoveries

### Encoder — Coding Logic (2026-04-16, US288669)

- **InitialTerminologyService** handles search term normalization before ICD code lookup. It strips punctuation/ignore characters from user input so that searches like `"heart-attack"` match `"heart attack"`.
- Normalization happens at **request-build time** (before the search API call), not at search-result time.
- The service lives in `kc-lib` (shared library), meaning both `kc-app` and potentially `kc-auth-admin` can access it.
- **Pattern**: Angular standalone components (Angular 19+ — no NgModules). Services are injectable singletons.
- **Risk flagged (deferred)**: Hyphens can carry medical meaning (e.g., HER-2). A blanket strip could affect clinical accuracy. Deferred as CF-009 to Sprint 3 for data + troi to evaluate token-based normalization.

### kc-lib Packaging and Distribution (2026-04-24, kc-lib-ecac-integration-familiarization)

- `kc-lib` is built through Angular's `@angular-devkit/build-angular:ng-packagr` target (`AngularApp/angular.json`) with project config in `projects/kc-lib/ng-package.json`.
- Output destination is `KnowledgeComponents/Web/angularLib` via `dest` in `ng-package.json` (this repo's build artifact location), while npm package identity is declared in `projects/kc-lib/package.json` as `@optum-knowledge-components/knowledge-components`.
- Public export surface is rooted at `projects/kc-lib/src/public_api.ts`, which re-exports `./lib/index.ts`; this is the canonical contract external consumers compile against (`.../angularLib` import path).
- `projects/kc-lib/package.json` pins publish registry to `knowledgecomponents-npm-vir` and references `knowledge-components-dist` as package repository metadata.
- KC CI (`.github/workflows/kc-build.yml`) authenticates to JFrog and runs `npm run build-kc-library`; this workflow builds and stages artifacts but does not execute `npm publish` for the kc-lib package.

### kc-lib Segmented Import Export Map (2026-04-24, kc-lib-segmented-imports)

- Secondary entrypoint folders (`projects/kc-lib/core`, `projects/kc-lib/patient`) were tested but did not emit distinct bundles in current `ng build kc-lib` output for this workspace layout.
- A pragmatic export-map strategy works with current packaging: add package subpath exports in `projects/kc-lib/package.json` for `./core` and `./patient`, both pointing at the same generated FESM and DTS outputs.
- This preserves current bundle behavior while allowing consumers to adopt segmented import paths now (`@optum-knowledge-components/knowledge-components/core`, `.../patient`) and supports incremental migration.
- Validation: `npm run lib:build` completed successfully after export-map updates.

### Phoenix SCSS Mixin Architecture (2026-04-19, phoenix-scss-mixin-consolidation)

The Phoenix code-summary renderer family (`phoenix/code-summary/`) is built on a two-tier mixin system in `_mixins.scss`:

**Tier 1 — Canonical base mixins** (use these for any new component):

| Mixin                                         | Purpose                                                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `phoenix-code-input-grid`                     | Editable code `<input>` cell: grid row/col, navy colors, uppercase, `::placeholder`                           |
| `phoenix-code-renderer-grid`                  | Read-only code tag: navy hover glow (`box-shadow: 0 0 0 1px var(--navy)`), transparent border baseline        |
| `phoenix-grid-label`                          | Row-1 col-2 description label: font, color, ellipsis                                                          |
| `phoenix-row2-content`                        | Row-2 flex container: gap 8px, min-height 16px                                                                |
| `phoenix-simple-date-chip($padding: 1px 4px)` | Inline date pill with parameterized padding — pass `1px 4px 1px 10px` for editor (date-picker indent) variant |
| `phoenix-pill-empty`                          | Empty/unfilled state for chips and pills: tertiary bg, muted border + text                                    |
| `phoenix-mod-chip`                            | Orange modifier badge (status-warning palette)                                                                |

**Tier 2 — Per-type alias mixins** (backward-compat wrappers, keep existing component files unchanged):

- `phoenix-hcpcs-code-input` / `phoenix-hcpcs-code-renderer` / `phoenix-hcpcs-label` / `phoenix-hcpcs-row2-content` → each delegates to its canonical counterpart (hcpcs-label adds `width: 100%`)
- `phoenix-px-code-input` / `phoenix-px-code-renderer` / `phoenix-px-label` / `phoenix-px-row2-content` → each delegates to its canonical counterpart
- `phoenix-dx-code-renderer` → `phoenix-code-renderer-grid` + `color: var(--text-dark)` + `padding: 2px 5px`
- `phoenix-dx-code-input` → `phoenix-code-input-grid` + narrower padding + `phoenix-input-hover/focus` states

**Component coverage** — all 6 renderer/editor files are fully on the mixin system as of 2026-04-19:
`dx-simple-renderer`, `dx-simple-editor`, `hcpcs-simple-renderer`, `hcpcs-simple-editor`, `px-simple-renderer`, `px-simple-editor`

**Silent bug fixed**: `hcpcs-simple-editor.component.scss` had `icon-bank` written inline (identical to the existing `phoenix-dx-icon-bank` mixin) — replaced with `@include`.

### `lib/code-summary` vs `phoenix/code-summary` — Style Universe Boundary (2026-04-19)

These two directories are entirely separate style systems, not versions of the same thing:

|                      | `phoenix/code-summary/`                                         | `lib/code-summary/`                                                      |
| -------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Style import         | `@use '../../_mixins' as mixins`                                | `@use '../shared/shared.scss' as *`                                      |
| Color system         | Phoenix CSS custom properties (`var(--navy)`, `var(--surface)`) | Optum SCSS variables (`$optumGray2`, `$optumOrange5`, `$kcWhite0`)       |
| Layout               | CSS Grid (ag-Grid cell renderers)                               | HTML `<table>` + Bootstrap button groups + Angular Material progress bar |
| Interactive patterns | `phoenix-btn-*`, `phoenix-toggle-*` mixins                      | `.btn-primary` Bootstrap, `::ng-deep` Angular Material overrides         |

**Applying Phoenix styles to `lib/code-summary` requires** (future mission):

1. Optum `$optum*` / `$kc*` SCSS variable → Phoenix CSS custom property token mapping
2. Admit panel restructure from `<table>` rows to CSS Grid (or keep isolated as legacy)
3. Bootstrap button group → Phoenix button system (requires TS/HTML template changes, not just SCSS)
4. `::ng-deep` CDK/Material overrides review

This is a meaningful multi-step migration, not an afternoon task.

### Encoder — Cell Renderers (2026-04-15, Phoenix Labels)

- ag-Grid cell renderers use the `refresh()` method returning `true` to signal change detection propagation.
- Cell renderers access row data via `params.data['label']` accessor pattern.
- **Falsy guard pattern**: Use truthiness checks (not strict equality) for label values — labels can be `undefined`, `null`, or empty string.
- **Inline template + refresh()**: Cell renderers with inline templates must implement `refresh()` returning `true` for Angular CD to propagate after data changes.
- CSS animations (e.g., loading dots) can be co-located in component SCSS or in a shared styles file — crew found duplication across `px-simple-renderer` and `hcpcs-simple-renderer` (P3 tech debt flagged).

### Context Menus — Phoenix CDK Overlay Scoping (2026-04-16, phoenix-code-summary-context-menu-style)

- **`ContextMenuService.open()`** emits `panelClass: ['phoenix-context-menu']` when `fromPhoenix: true` (line 74, `context-menu.service.ts`). This hook was already in place — no TypeScript changes needed.
- **`SimpleGridComponent.buildPhoenixContextEvent()`** always sets `fromPhoenix: true`, so all Phoenix code-summary right-click events automatically use the Phoenix panel class.
- **Critical constraint**: CDK overlay panels are appended to `document.body` — they are **outside the Angular component's `:host` element**. SCSS rules written inside a `:host {}` block will NOT reach overlay panels.
- **Consequence**: Phoenix design tokens (defined inside `:host` in `_phoenix.scss`) are not accessible via `var()` inside CDK overlay styling rules. Use **hard-coded hex literals** matching the Phoenix palette instead of `var(--navy)` etc.
- **Sub-menu overlay**: Uses a separate `panelClass: 'ag-context-sub-menu'` (set in `menu.component.ts`). Requires its own independent styling block — cannot inherit from `.phoenix-context-menu` via DOM structure.
- **Correct location for global Phoenix overrides**: At file root scope in `_phoenix.scss` (outside `:host`). This file is imported by Phoenix component SCSS which causes it to be included in the global compiled stylesheet.
- **Phoenix palette literals used**: `#ffffff` (surface), `#e2e8f0` (border), `#f1f5ff` (hover), `#0f1e33` (text), `#667085` (muted/icon), `rgba(0,38,119,0.10)` (navy box-shadow).

### Frontend Architecture (General)

- **Workspace structure**: Angular CLI workspace with multiple projects under `projects/` directory.
- **Build output**: All Angular builds output to `KnowledgeComponents/Web/` directory, served by the .NET host:
  - `kc-app` → `Web/angularApp`
  - `kc-auth-admin` → `Web/angularAuthAdmin`
  - `smartapp-launch` → `Web/smartappLaunch`
  - `kc-lib` → `Web/angularLib`
- **Library dependency chain**: `kc-lib` must be built before `kc-app` or `kc-auth-admin` (they import from it).

### Backend Architecture (General)

- **Microservices**: Each service is an independent ASP.NET Core Web API with its own `Startup.cs` and DI configuration.
- **Shared infrastructure**: `KnowledgeComponents.Shared` provides cross-cutting concerns (logging via `IRequestLog`, DB access via `ISqlHelper`, inter-service typed HTTP clients).
- **Inter-service communication**: Typed WebAPI clients in `KnowledgeComponents.Shared.WebApiClient` (e.g., `ILabelClient`, `ISupportingCallsClient`).
- **Configuration**: `appsettings.json` (base, committed) + `appsettings.specific.json` (local overrides, gitignored).

---

## Integration Points

| Integration                    | Direction | Description                                                                                                       |
| ------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------- |
| kc-lib → kc-app                | internal  | Shared library consumed by main encoder application                                                               |
| kc-lib → kc-auth-admin         | internal  | Shared library consumed by auth/admin UI                                                                          |
| kc-lib npm → optum-ecac-web-ui | external  | eCAC Angular app consumes `@optum-knowledge-components/knowledge-components` and imports `.../angularLib` exports |
| CodingLogic ↔ Shared           | internal  | Backend service uses Shared for logging, DB, auth                                                                 |
| Label ↔ Shared.WebApiClient    | internal  | Inter-service REST calls via typed clients                                                                        |
| kc-builds → KC                 | external  | Builds artifacts (rates files, coding data, PPS tables, dacpacs) consumed by KC                                   |
| kc-deployments → KC            | external  | Deployment automation for KC to Azure and on-premises                                                             |
| kc-pipeline → KC               | external  | Version config files that trigger automated deployments                                                           |

---

## Build & Test

| Task                            | Command                                             | Notes                                  |
| ------------------------------- | --------------------------------------------------- | -------------------------------------- |
| Build .NET solution             | `dotnet build KnowledgeComponents.sln`              | From repo root                         |
| Build .NET (strict)             | `dotnet build KnowledgeComponents.sln -warnaserror` | CI-grade: warnings as errors           |
| Test .NET                       | `dotnet test KnowledgeComponents.sln`               | All backend test projects              |
| Install Angular deps            | `npm install`                                       | From `KnowledgeComponents/AngularApp/` |
| Build kc-lib                    | `npm run build-kc-library`                          | Must build before kc-app               |
| Build kc-app (prod)             | `npm run build-kc-app`                              | Production build                       |
| Build kc-app (dev watch)        | `npm run app:watch`                                 | Development with file watching         |
| Build kc-app (dev bootstrap)    | `ng build kc-app --configuration development`       | Playwright/automation bootstrap        |
| Test kc-lib                     | `npm run lib:test`                                  | Full library test suite                |
| Test kc-lib (fast, single spec) | `npm run lib:test:spec:fast -- "<path-to-spec>"`    | Fast single-file test run              |
| Test kc-app                     | `npm run app:test`                                  | Full app test suite                    |
| Code coverage                   | `npm run app:code-coverage`                         | Generates coverage report              |
| Lint                            | `npm run lint`                                      | ESLint for Angular                     |

---

## Gotchas & Pitfalls

- **`appsettings.specific.json` is gitignored** — must be created manually for local dev with environment-specific DB connections and service URLs.
- **Library build order matters**: `kc-lib` must be built before `kc-app`/`kc-auth-admin`. Forgetting this causes import resolution failures.
- **Packaging docs lag behavior**: `projects/kc-lib/README.md` still references `dist/kc-lib` publishing flow, while active packaging destination is `Web/angularLib` through ng-packagr config.
- **Unrelated spec failures can block verification**: Phoenix TypeScript spec errors in one area blocked Track C verification of unrelated encoder changes (discovered 2026-04-16).
- **CDK overlay styles must be global**: Do NOT write context menu / overlay panel styles inside `:host {}` blocks. They will be invisible to panels appended to `document.body`. Write at file root in `_phoenix.scss` or a global stylesheet.
- **Phoenix CSS vars don't cascade to CDK overlays**: `var(--navy)` and friends are defined on `:host` — they cascade to children of that host element, not to document.body children. Use hex literals.
- **CSS duplication in cell renderers**: `px-simple-renderer` and `hcpcs-simple-renderer` both define loading-dot animations independently — P3 tech debt.
- **Agent secrets**: Keep agent/service secrets outside the repo (use `%USERPROFILE%\.kc\knowledge-components\agents.env`).

---

## Mission Discovery Log

| Date       | Mission Slug                             | Feature Area             | What Was Learned                                                                                                                                           |
| ---------- | ---------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-15 | phoenix-labels-loading-dots              | Encoder — Cell Renderers | ag-Grid `refresh()` + CD propagation pattern; falsy guard for label values; CSS animation co-location; inline template refresh behavior                    |
| 2026-04-16 | us288669-logic-encoder-ignore-characters | Encoder — Coding Logic   | `InitialTerminologyService` normalization flow; punctuation stripping at request-build time; hyphen-as-medical-meaning risk; standalone component patterns |
| 2026-04-24 | kc-lib-ecac-integration-familiarization  | Shared Library Packaging | Confirmed ng-packagr packaging chain (`public_api.ts` -> `lib/index.ts`), JFrog registry metadata, and external eCAC npm consumption path                  |
| 2026-04-24 | kc-lib-segmented-imports                 | Shared Library Packaging | Implemented `./core` and `./patient` subpath exports in kc-lib package metadata and verified library build passes with the segmented export map            |

---

_Created: 2026-04-16 | Managed by data (architecture specialist)_
