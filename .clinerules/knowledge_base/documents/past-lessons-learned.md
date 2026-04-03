# Past Lessons Learned

## 2026-03-15 - Dark Mode Implementation

- Lesson: Using CSS variables + a single `dark` class on `<html>` is much simpler than multiple theme providers.
- Decision: Store user preference in both localStorage and backend profile.
- Outcome: Good performance, easy to maintain.

## 2026-02-28 - CI/CD Pipeline Issue

- Problem: Long build times due to unnecessary dependency installation.
- Solution: Implemented caching for node_modules and Docker layers.
- Result: Build time reduced by 65%.

## 2026-02-10 - Rally Story Handling

- Lesson: Always pull full acceptance criteria from Rally before starting implementation to avoid scope creep.
