# Mission Execution Manifest Template

> Instructions: copy this template into `knowledge_base/missions/manifests/YYYY-MM-DD-<mission-slug>.manifest.md`.
> Required for any mission where `Repo(s)` includes more than one repository.

---

## Mission Execution Manifest — [mission-slug]

| Field           | Value                                                     |
| --------------- | --------------------------------------------------------- |
| Mission Slug    | `<mission-slug>`                                          |
| Date            | YYYY-MM-DD                                                |
| Session Journal | `knowledge_base/sessions/YYYY-MM-DD-HH-<mission-slug>.md` |
| Mission Log     | `knowledge_base/missions/YYYY-MM-DD-<mission-slug>.md`    |
| Mission Type    | `single-repo` / `multi-repo`                              |

---

## Repo Execution Ledger

| Repo             | Branch                   | Final Commit SHA        | Base Ref          | Checkpoint Commit(s)   | Role                     | Notes |
| ---------------- | ------------------------ | ----------------------- | ----------------- | ---------------------- | ------------------------ | ----- |
| `<owner/repo-a>` | `mission/<mission-slug>` | `<40-char-sha>` / `n/a` | `<branch-or-sha>` | `<sha1, sha2>` / `n/a` | upstream / primary       |       |
| `<owner/repo-b>` | `mission/<mission-slug>` | `<40-char-sha>` / `n/a` | `<branch-or-sha>` | `<sha1, sha2>` / `n/a` | downstream / integration |       |

---

## Wave Gates

| Wave   | Repo             | Gate Condition        | Result      |
| ------ | ---------------- | --------------------- | ----------- |
| Wave 1 | `<owner/repo-a>` | n/a                   | pass / fail |
| Wave 2 | `<owner/repo-b>` | `Wave 1 commit <sha>` | pass / fail |

---

## Carry-Forward Provenance

| CF-ID  | Item | Source Repo    | Source Mission   | Target Sprint |
| ------ | ---- | -------------- | ---------------- | ------------- |
| CF-XXX |      | `<owner/repo>` | `<mission-slug>` | Sprint N      |

---

## Verification Checklist

- [ ] Every repo in mission scope appears exactly once in Repo Execution Ledger
- [ ] Every multi-repo wave gate references a concrete upstream commit SHA when applicable
- [ ] Mission manifest link added to `knowledge_base/missions/mission-index.md`
- [ ] Session journal and mission log links are valid
