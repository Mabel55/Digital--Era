import React, { useState, useEffect } from 'react';
import { WifiOff, Check } from 'lucide-react';

const OfflineBanner = () => {
  const [isOffline, setIsOffline] = useState(!navigator.onLine);
  const [showBanner, setShowBanner] = useState(false);

  useEffect(() => {
    const handleOffline = () => {
      setIsOffline(true);
      setShowBanner(true);
    };

    const handleOnline = () => {
      setIsOffline(false);
      // Keep banner visible briefly to show "back online" message
      setTimeout(() => setShowBanner(false), 3000);
    };

    window.addEventListener('offline', handleOffline);
    window.addEventListener('online', handleOnline);

    // Show banner on mount if already offline
    if (!navigator.onLine) {
      setShowBanner(true);
    }

    return () => {
      window.removeEventListener('offline', handleOffline);
      window.removeEventListener('online', handleOnline);
    };
  }, []);

  if (!showBanner) return null;

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      zIndex: 9999,
      padding: '0.6rem 1rem',
      textAlign: 'center',
      fontSize: '0.85rem',
      fontWeight: 600,
      fontFamily: "'Inter', sans-serif",
      transition: 'all 0.3s ease',
      background: isOffline
        ? 'linear-gradient(135deg, #ef4444, #dc2626)'
        : 'linear-gradient(135deg, #00e5a0, #00c98a)',
      color: isOffline ? '#fff' : '#0d0f14',
      boxShadow: isOffline
        ? '0 4px 20px rgba(239, 68, 68, 0.3)'
        : '0 4px 20px rgba(0, 229, 160, 0.3)',
      display: 'flex',
      justifyContent: 'center'
    }}>
      {isOffline ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <WifiOff size={16} /> You're offline — cached content is still available
        </div>
      ) : (
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Check size={16} /> Back online!
        </div>
      )}
    </div>
  );
};

export default OfflineBanner;
