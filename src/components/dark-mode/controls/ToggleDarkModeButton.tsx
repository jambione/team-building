// src/components/dark-mode/controls/ToggleDarkModeButton.tsx
// Dark mode toggle button component.
// Follows the principle of single responsibility and maintainability.

import { useDarkMode } from './index';

export const ToggleDarkModeButton = () => {
  const { isDark, toggleDarkMode } = useDarkMode(isDark);

  return (
    <button onClick={() => toggleDarkMode()}>Toggle Dark Mode</button>
  );
};