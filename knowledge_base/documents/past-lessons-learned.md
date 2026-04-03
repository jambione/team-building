# Past Lessons Learned

## 2026-03-20 - Dark Mode Implementation

- Lesson: CSS variables + single `dark` class on `<html>` is far simpler and more maintainable than multiple theme providers.
- Decision: Store user preference in both localStorage and backend profile.

## 2026-02-28 - CI/CD Performance

- Problem: Long build times due to repeated dependency installation.
- Solution: Added caching for node_modules and Docker layers.
- Result: Build time reduced by ~65%.

## 2026-02-10 - Rally Story Handling

- Lesson: Always fetch and review full acceptance criteria from Rally before starting implementation.
- Outcome: Reduced scope creep and rework.
