# Repo Discovery — optum-ecac-web-ui

**Owner**: data | **Last Updated**: 2026-04-24 (kc-lib-ecac-integration-familiarization)

---

## Overview

| Field              | Value                                                                 |
| ------------------ | --------------------------------------------------------------------- |
| **Repo Name**      | optum-ecac-web-ui                                                     |
| **Service Domain** | Enterprise CAC web UI for coding workflow and case management         |
| **Tech Stack**     | Angular 21.2.2, TypeScript 5.9.3, ASP.NET Framework host (.NET 4.7.2) |
| **Owner Agent**    | data                                                                  |
| **Hub Repo**       | team-building                                                         |

---

## Feature Map

_What the crew has explored. Updated after every mission that touches this repo._

| Feature Area                     | Location                                                               | Purpose                                                               | Key Services / Components                                                                                  | Last Explored |
| -------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------- |
| Angular application shell        | `EnterpriseCACUIWebApp/EnterpriseCACUIWebApp/eCACAngular/`             | Primary front-end application for Enterprise CAC                      | `src/main.ts`, `src/app/app.module.ts`, Angular CLI workspace config                                       | 2026-04-24    |
| KC library consumption           | `EnterpriseCACUIWebApp/EnterpriseCACUIWebApp/eCACAngular/src/app/`     | Consumes shared coding models/components/services from kc-lib package | Imports from `@optum-knowledge-components/knowledge-components/angularLib` across app modules and services | 2026-04-24    |
| Build-time KC package asset copy | `EnterpriseCACUIWebApp/EnterpriseCACUIWebApp/eCACAngular/angular.json` | Copies KC package static files from node_modules into build output    | Angular build `assets` entry for `@optum-knowledge-components/knowledge-components`                        | 2026-04-24    |
| CI package reliability guard     | `.github/workflows/StatusCheck.yml`                                    | Forces KC package installation before Angular build/test in PR checks | `npm i @optum-knowledge-components/knowledge-components --force` in build and test jobs                    | 2026-04-24    |

---

## Architecture Discoveries

_Patterns, dependency chains, service topology, and design decisions specific to this repo. Organized by feature area._

### KC Library Consumption Architecture (2026-04-24)

- eCAC imports shared contracts and UI artifacts from `@optum-knowledge-components/knowledge-components/angularLib` directly in many feature modules.
- Shared imports include both domain types (for example `IPatientRecord`, `CodeType`, reimbursement models) and runtime services/components (for example `KcApiService`, `KcLibModule`, `KcCodeSummaryComponent`).
- Root module integration includes direct imports from KC library in `src/app/app.module.ts`; the KC module and standalone exports are used inside eCAC's Angular composition.
- eCAC bootstrap in `src/main.ts` remains independent (loads app config and waits for X2JS), while KC library components are loaded through normal Angular module/component wiring.

### Dependency Strategy and Stability Signals (2026-04-24)

- Package is declared in `optionalDependencies` in `eCACAngular/package.json`.
- CI intentionally force-installs KC package even after `npm ci` to avoid transient lockfile/environment cases where `angularLib` resolution can fail.
- Build configuration copies package assets from node_modules so runtime static dependencies are present in distribution output.

### Segmented Import Pilot (2026-04-24, kc-lib-segmented-imports)

- Pilot conversion completed in `risk-summary` from monolithic `.../angularLib` imports to segmented paths:
  - `KcApiService` from `@optum-knowledge-components/knowledge-components/core`
  - `IPatientRecord` from `@optum-knowledge-components/knowledge-components/patient`
- For compatibility with currently published KC package versions, eCAC `tsconfig.json` paths currently alias `.../core` and `.../patient` to the existing `angularLib` build artifact path.
- Focused validation succeeded: `ng test --watch=false --browsers=ChromeHeadless --include="src/app/risk-summary/risk-summary.component.spec.ts"` passed (9 specs, 0 failures).
- Expansion batch applied: all exact single-symbol imports for `KcApiService` and `IPatientRecord` were migrated from `.../angularLib` to segmented subpaths across app source/spec files.
- Post-migration verification showed zero remaining exact single-symbol angularLib imports for these two symbols.

---

## Integration Points

_Cross-service calls, shared libraries, external dependencies, and API contracts._

| Integration                                                            | Direction | Description                                                                |
| ---------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------- |
| `@optum-knowledge-components/knowledge-components` -> eCAC Angular app | inbound   | Provides shared coding components, services, and model contracts via npm   |
| eCAC build -> KC package assets                                        | inbound   | Angular build copies KC package files from node_modules into app output    |
| eCAC CI -> JFrog ecac npm registry                                     | outbound  | Uses `ecac-npm-vir` registry and installs dependencies in StatusCheck jobs |

---

## Build & Test

_Commands, watch modes, config locations, and environment setup the crew has learned._

| Task                         | Command                                                                                                                                       | Notes                                                            |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Install Angular dependencies | `npm ci`                                                                                                                                      | Run in `EnterpriseCACUIWebApp/EnterpriseCACUIWebApp/eCACAngular` |
| Build Angular app            | `node --max_old_space_size=16384 node_modules/@angular/cli/bin/ng build --configuration=production --output-hashing=media --source-map=false` | CI build command                                                 |
| Test Angular app (CI-style)  | `ng test --karma-config=karma.conf.ci.js --code-coverage=true --watch=false --source-map=true --browsers=ChromeHeadless`                      | CI test command                                                  |
| Force-install KC package     | `npm i @optum-knowledge-components/knowledge-components --force`                                                                              | Executed in CI before build/test                                 |
| Set npm registry             | `npm config set registry https://centraluhg.jfrog.io/artifactory/api/npm/ecac-npm-vir/`                                                       | Required in CI and some local setups                             |

---

## Gotchas & Pitfalls

- CI performs `npm i @optum-knowledge-components/knowledge-components --force` after `npm ci`; local environments that skip this may observe package resolution differences.
- Imports are tied to `.../angularLib` export path; package layout changes upstream can cascade into widespread compile errors in eCAC.
- Build output includes copied KC package assets from node_modules; removing this asset copy block can introduce runtime missing-file regressions.
- Package is listed as an optional dependency, but effectively required by many app modules; treat it as a hard runtime dependency for build/test readiness.
- Until a KC package version containing `./core` and `./patient` export-map metadata is consumed in eCAC, keep `tsconfig.json` path aliases in place for segmented import compile-time resolution.

---

## Mission Discovery Log

_Rolling record of what was learned per mission. One row per mission that touched this repo._

| Date       | Mission Slug                            | Feature Area           | What Was Learned                                                                                                            |
| ---------- | --------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-24 | kc-lib-ecac-integration-familiarization | KC library consumption | Mapped npm dependency, angular build asset copy, app imports, and CI force-install behavior for KC package                  |
| 2026-04-24 | kc-lib-segmented-imports                | KC library consumption | Validated risk-summary pilot using segmented imports with temporary tsconfig aliasing and passing focused unit tests        |
| 2026-04-24 | kc-lib-segmented-imports                | KC library consumption | Expanded migration for exact `KcApiService`/`IPatientRecord` single-symbol imports and revalidated focused test compilation |

---

_Created: 2026-04-24 | Managed by data (architecture specialist)_
