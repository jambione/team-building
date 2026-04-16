# Acceptance Criteria — phoenix-labels-loading-dots

## Metadata

| Field            | Value                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------- |
| **Mission**      | Add dancing dots loading animation to Phoenix grid label divs while labels call is in-flight |
| **Mission Slug** | `phoenix-labels-loading-dots`                                                                |
| **Date**         | 2026-04-15                                                                                   |
| **Author**       | troi                                                                                         |
| **Approved By**  | picard — `[AC-APPROVED: phoenix-labels-loading-dots]`                                        |
| **Status**       | approved                                                                                     |

---

## Definition of Done

> Execution is complete when all Acceptance Criteria below have:
>
> 1. At least one passing automated test per scenario
> 2. Track C (troi) verified in the post-execution review
>
> Code may not be merged until both conditions are met.

---

## Acceptance Criteria

### AC-01: Dots visible when label is blank (PX renderer)

**Scenario**: A row in the ICD-10 CM or ICD-10 PCS simple grid has a blank label field while the label call is in-flight.

- **Given** a `px-simple-renderer` cell where `params.data['label']` is falsy (`''` or `undefined`)
- **When** the cell is rendered or refreshed
- **Then** a `.label-loading-dots` element is visible inside `.label-area`
- **And** the three dot `<span>` children animate with staggered bounce
- **And** no `cdkSmartTooltip` is active on the dots element

---

### AC-02: Label text replaces dots when label resolves (PX renderer)

**Scenario**: The label call completes and `LabelService` populates the label field on the row data.

- **Given** a `px-simple-renderer` cell that was showing dancing dots
- **When** `params.data['label']` becomes a non-empty string and ag-Grid calls `refresh()`
- **Then** the `.label-loading-dots` element is no longer rendered
- **And** the `.px-label` div is visible with the resolved label text
- **And** `cdkSmartTooltip` is active with the label text value
- **And** grid row height has not changed between loading and resolved states

---

### AC-03: Dots visible when label is blank (HCPCS renderer)

**Scenario**: A row in the HCPCS simple grid has a blank label field while the label call is in-flight.

- **Given** a `hcpcs-simple-renderer` cell where `params.data['label']` is falsy (`''` or `undefined`)
- **When** the cell is rendered or refreshed
- **Then** a `.label-loading-dots` element is visible inside `.label-area`
- **And** the three dot `<span>` children animate with staggered bounce
- **And** no `cdkSmartTooltip` is active on the dots element

---

### AC-04: Label text replaces dots when label resolves (HCPCS renderer)

**Scenario**: The label call completes and `LabelService` populates the label field on the HCPCS row.

- **Given** a `hcpcs-simple-renderer` cell that was showing dancing dots
- **When** `params.data['label']` becomes a non-empty string and ag-Grid calls `refresh()`
- **Then** the `.label-loading-dots` element is no longer rendered
- **And** the `.hcpcs-label` div is visible with the resolved label text
- **And** `cdkSmartTooltip` is active with the label text value

---

### AC-05: Accessibility — loading state announced

**Scenario**: A screen reader user navigates to a cell with a pending label.

- **Given** the `.label-loading-dots` element is visible
- **When** a screen reader reads the element
- **Then** `aria-label="Loading label"` is present on the dots container

---

### AC-07: Dots visible when admit DX label is blank

**Scenario**: An admit DX code is added to the pill row while the label call is still in-flight.

- **Given** an `admit-dx-pill` where `code.label` is falsy (`''` or `undefined`)
- **When** the pill is rendered
- **Then** a `.admit-dx-pill__label--loading` span with dancing dots is visible
- **And** no `cdkSmartTooltip` is active on the loading span
- **And** `aria-label="Loading label"` is present on the loading span

---

### AC-08: Admit DX label text replaces dots when label resolves

**Scenario**: `LabelService` populates the admit DX code label and Angular's change detection re-evaluates the pill.

- **Given** an `admit-dx-pill` that was showing dancing dots
- **When** `code.label` becomes a non-empty string
- **Then** the `.admit-dx-pill__label--loading` span is no longer rendered
- **And** the standard `.admit-dx-pill__label` span is visible with the resolved label text
- **And** `cdkSmartTooltip` is active with the label text value
- **And** the pill grid row height has not changed between loading and resolved states

---

### AC-06: Non-label cells unaffected

**Scenario**: Other parts of the renderer (code, date, row-actions, provider editor) are not affected by the label loading state.

- **Given** the dots are visible
- **When** the user interacts with the code pill, date picker, or delete button
- **Then** all interactions work identically to the non-loading state
- **And** the `.row-actions` hover overlay still appears correctly

---

## Traceability

| AC ID | MDR Decision Outcome                        | Tests Written | Track C Verified |
| ----- | ------------------------------------------- | :-----------: | :--------------: |
| AC-01 | `!params.data['label']` → show dots (PX)    |      [ ]      |       [ ]        |
| AC-02 | label resolves → show text (PX)             |      [ ]      |       [ ]        |
| AC-03 | `!params.data['label']` → show dots (HCPCS) |      [ ]      |       [ ]        |
| AC-04 | label resolves → show text (HCPCS)          |      [ ]      |       [ ]        |
| AC-05 | aria-label on dots container                |      [ ]      |       [ ]        |
| AC-06 | Adjacent controls unaffected                |      [ ]      |       [ ]        |

---

## troi's Notes

- The dots container must have the same `line-height` and `min-height` as `.px-label` / `.hcpcs-label` to eliminate any row geometry shift when the animation transitions to text.
- The 3-dot bounce animation is intentionally subtle — dots at `4px` diameter, `#667085` color (secondary text), 1.2s cycle. This reads as "gentle waiting" not "loading emergency."
- Provider editor and row-actions visibility is controlled by `isProviderEditorOpen` and hover state — neither is coupled to the label state. No interaction regression expected.
