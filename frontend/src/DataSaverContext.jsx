import React, { createContext, useContext, useState, useEffect } from 'react';

/**
 * DataSaverContext — Global toggle for data-saving mode
 * 
 * Design principles:
 * - OFF by default — no one's experience changes unless they opt in
 * - Everything is reversible — toggle off = back to full experience instantly
 * - No features are removed — they're deferred (lazy-loaded on demand)
 * - State persists in localStorage so the preference survives refreshes
 */
const DataSaverContext = createContext();

export const useDataSaver = () => {
  const context = useContext(DataSaverContext);
  if (!context) {
    // Graceful fallback — if used outside provider, behave as "off"
    return { dataSaver: false, setDataSaver: () => {} };
  }
  return context;
};

export const DataSaverProvider = ({ children }) => {
  const [dataSaver, setDataSaverState] = useState(() => {
    // Restore from localStorage, default to OFF
    return localStorage.getItem('de_data_saver') === 'true';
  });

  const setDataSaver = (value) => {
    setDataSaverState(value);
    localStorage.setItem('de_data_saver', value ? 'true' : 'false');
    
    // Toggle CSS class on root element for style-level optimizations
    if (value) {
      document.documentElement.classList.add('data-saver');
    } else {
      document.documentElement.classList.remove('data-saver');
    }
  };

  // Apply on mount if already enabled
  useEffect(() => {
    if (dataSaver) {
      document.documentElement.classList.add('data-saver');
    }
  }, []);

  return (
    <DataSaverContext.Provider value={{ dataSaver, setDataSaver }}>
      {children}
    </DataSaverContext.Provider>
  );
};
