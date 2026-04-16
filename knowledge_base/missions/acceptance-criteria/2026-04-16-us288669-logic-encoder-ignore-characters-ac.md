# Acceptance Criteria — us288669-logic-encoder-ignore-characters

---

## Metadata

| Field            | Value                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------- |
| **Mission**      | Update Logic Encoder search normalization to ignore additional punctuation characters |
| **Mission Slug** | `us288669-logic-encoder-ignore-characters`                                            |
| **Date**         | 2026-04-16                                                                            |
| **Author**       | troi                                                                                  |
| **Approved By**  | picard — `[AC-APPROVED: us288669-logic-encoder-ignore-characters]`                    |
| **Status**       | approved                                                                              |

---

## Definition of Done

Execution is complete when all acceptance criteria below have at least one passing automated test and the post-execution review verifies the updated normalization behavior.

---

## Acceptance Criteria

### AC-01: Ignore Additional Punctuation

**Scenario**: Main-term search input contains punctuation characters requested in the Rally story.

- **Given** the user enters a Logic Encoder search term that includes `(`, `)`, `&`, or `-`
- **When** the encoder prepares the term for the `InitialTerminology` request
- **Then** those punctuation characters are removed from the normalized search term
- **And** the remaining meaningful search text is preserved in order

---

### AC-02: Preserve Existing Ignore Words

**Scenario**: Main-term search input includes words already configured to be ignored.

- **Given** the user enters a Logic Encoder search term containing `of`, `or`, `and`, or `the`
- **When** the encoder normalizes the term before search
- **Then** those ignored words are still removed from the search term
- **And** the new punctuation-removal behavior does not reintroduce or alter the existing ignored-word behavior

---

### AC-03: Maintain Existing Search Flow

**Scenario**: A valid search term is submitted through the Logic Encoder after normalization.

- **Given** the user enters a search term longer than one character in the Logic Encoder
- **When** the search is submitted through the existing initial terminology flow
- **Then** the request still uses the current debounce, cancellation, and result-handling path
- **And** the normalized search term is the value sent to the API request body

---

## Traceability

| AC ID | MDR Decision Outcome                                                      | Tests Written | Track C Verified |
| ----- | ------------------------------------------------------------------------- | :-----------: | :--------------: |
| AC-01 | Strip parentheses, ampersands, and hyphens in Logic Encoder normalization |      [x]      |       [ ]        |
| AC-02 | Preserve the current ignored-word behavior                                |      [x]      |       [ ]        |
| AC-03 | Keep the existing initial terminology request path intact                 |      [x]      |       [ ]        |

---

## troi's Notes

Normalization must stay observable through focused unit tests so future regex changes do not silently alter search behavior.
Track C verification remains conditional because the `kc-lib` spec run is blocked by unrelated existing Phoenix procedure-renderer TypeScript test errors outside this mission's scope.

---

_"troi returns control to picard. [ac-draft-complete]"_
