# Past Lessons Learned

## 2026-03-20 – Dark Mode Implementation

- **Lesson**: Using CSS variables + a single `dark` class on `<html>` is far simpler and more maintainable than multiple theme providers or context-heavy solutions.
- **Decision**: Store user preference in both localStorage (for instant UI) and backend profile (for persistence).
- **Outcome**: Good performance and easy future extensions.

## 2026-02-28 – CI/CD Performance Issues

- **Problem**: Long build times due to repeated dependency installation.
- **Solution**: Added proper caching for `node_modules` and Docker layers.
- **Result**: Build time reduced by ~65%. Always evaluate caching early.

## 2026-02-10 – Rally Story Handling

- **Lesson**: Always fetch and carefully review full acceptance criteria from Rally before starting implementation.
- **Outcome**: Significantly reduced scope creep and rework.

## 2026-01-15 – Mobile Bug Example

- **Lesson**: Test on real devices early — emulators can miss subtle layout and touch issues.
