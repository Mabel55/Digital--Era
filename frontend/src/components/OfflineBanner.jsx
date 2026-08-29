import React, { useState, useEffect } from 'react';
import { WifiOff, Check, CloudOff, RefreshCw, Download } from 'lucide-react';
import { getPendingSyncCount } from '../lib/offlineDB';

const OfflineBanner = () => {
  const [isOffline, setIsOffline] = useState(!navigator.onLine);
  const [showBanner, setShowBanner] = useState(false);
  const [pendingSync, setPendingSync] = useState(0);

  useEffect(() => {
    const handleOffline = () => {
      setIsOffline(true);
      setShowBanner(true);
      refreshPendingCount();
    };

    const handleOnline = () => {
      setIsOffline(false);
      // Keep banner visible briefly to show "back online" + syncing message
      refreshPendingCount();
      setTimeout(() => setShowBanner(false), 4000);
    };

    window.addEventListener('offline', handleOffline);
    window.addEventListener('online', handleOnline);

    // Show banner on mount if already offline
    if (!navigator.onLine) {
      setShowBanner(true);
      refreshPendingCount();
    }

    return () => {
      window.removeEventListener('offline', handleOffline);
      window.removeEventListener('online', handleOnline);
    };
  }, []);

  const refreshPendingCount = async () => {
    try {
      const count = await getPendingSyncCount();
      setPendingSync(count);
    } catch (e) {
      // IndexedDB may not be available
    }
  };

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
        ? 'linear-gradient(135deg, #f59e0b, #d97706)'
        : 'linear-gradient(135deg, #00e5a0, #00c98a)',
      color: isOffline ? '#0d0f14' : '#0d0f14',
      boxShadow: isOffline
        ? '0 4px 20px rgba(245, 158, 11, 0.3)'
        : '0 4px 20px rgba(0, 229, 160, 0.3)',
      display: 'flex',
      justifyContent: 'center',
      flexWrap: 'wrap',
      gap: '4px',
    }}>
      {isOffline ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', justifyContent: 'center' }}>
          <WifiOff size={16} />
          <span>You're offline — lessons & Python still work!</span>
          {pendingSync > 0 && (
            <span style={{ 
              background: 'rgba(0,0,0,0.15)', 
              padding: '2px 8px', 
              borderRadius: '100px',
              fontSize: '0.75rem',
            }}>
              {pendingSync} update{pendingSync !== 1 ? 's' : ''} will sync when online
            </span>
          )}
        </div>
      ) : (
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Check size={16} />
          <span>Back online!</span>
          {pendingSync > 0 && (
            <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
              <RefreshCw size={14} style={{ animation: 'spin 1s linear infinite' }} />
              Syncing {pendingSync} update{pendingSync !== 1 ? 's' : ''}...
            </span>
          )}
        </div>
      )}
    </div>
  );
};

export default OfflineBanner;
