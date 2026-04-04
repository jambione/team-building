// src/components/dark-mode/controls/DarkModeProvider.tsx
// Dark mode provider component.
// Follows the principle of single responsibility and maintainability.

import { createContext, useContext, useState } from 'react';

export const DarkModeContext = createContext<DarkModeContextType | null>(null);

export interface DarkModeContextType {
  isDark: boolean;
  toggleDarkMode: () => void;
}

export const useDarkMode = (initialIsDark?: boolean) => {
  const context = useContext(DarkModeContext);
  if (!context) {
    throw new Error('useDarkMode must be used within a DarkModeProvider');
  }
  return context;
};

export const DarkModeProvider = ({ children, initialIsDark = false }: { children: React.ReactNode; initialIsDark?: boolean }) => {
  const [isDark, setIsDark] = useState(initialIsDark);

  const toggleDarkMode = () => {
    setIsDark((prev) => !prev);
  };

  return (
    <DarkModeContext.Provider value={{ isDark, toggleDarkMode }}>
      {children}
    </DarkModeContext.Provider>
  );
};