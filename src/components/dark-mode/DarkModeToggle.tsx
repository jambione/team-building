// Dark mode toggle component
import { useState, useEffect } from 'react';

export const DarkModeToggle = () => {
  const [isDark, setIsDark] = useState(false);

  // Check user preference on load
  useEffect(() => {
    const savedPreference = localStorage.getItem('darkMode') === 'true';
    setIsDark(savedPreference);
    document.documentElement.classList.toggle('dark', savedPreference);
  }, []);

  // Toggle dark mode
  const toggleDarkMode = () => {
    const newIsDark = !isDark;
    setIsDark(newIsDark);
    localStorage.setItem('darkMode', String(newIsDark));
    document.documentElement.classList.toggle('dark', newIsDark);
  };

  return (
    <button onClick={toggleDarkMode}>
      {isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
    </button>
  );
};