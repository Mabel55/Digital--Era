import React, { useState, useEffect } from 'react';

const PWAInstallPrompt = () => {
  const [deferredPrompt, setDeferredPrompt] = useState(null);
  const [showPrompt, setShowPrompt] = useState(false);
  const [isInstalled, setIsInstalled] = useState(false);

  useEffect(() => {
    // Check if already installed
    if (window.matchMedia('(display-mode: standalone)').matches) {
      setIsInstalled(true);
      return;
    }

    const handleBeforeInstallPrompt = (e) => {
      e.preventDefault();
      setDeferredPrompt(e);
      // Show the prompt after a delay so it doesn't interrupt the user immediately
      setTimeout(() => setShowPrompt(true), 5000);
    };

    const handleAppInstalled = () => {
      setIsInstalled(true);
      setShowPrompt(false);
      setDeferredPrompt(null);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    window.addEventListener('appinstalled', handleAppInstalled);

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
      window.removeEventListener('appinstalled', handleAppInstalled);
    };
  }, []);

  const handleInstall = async () => {
    if (!deferredPrompt) return;
    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    if (outcome === 'accepted') {
      setIsInstalled(true);
    }
    setDeferredPrompt(null);
    setShowPrompt(false);
  };

  const handleDismiss = () => {
    setShowPrompt(false);
  };

  if (isInstalled || !showPrompt) return null;

  return (
    <div style={styles.overlay}>
      <div style={styles.banner}>
        <div style={styles.iconRow}>
          <div style={styles.appIcon}>⚡</div>
          <div style={styles.textCol}>
            <strong style={styles.title}>Install Digital Era</strong>
            <span style={styles.subtitle}>
              Get faster access & work offline
            </span>
          </div>
        </div>
        <div style={styles.actions}>
          <button style={styles.installBtn} onClick={handleInstall}>
            Install App
          </button>
          <button style={styles.dismissBtn} onClick={handleDismiss}>
            Not Now
          </button>
        </div>
      </div>
    </div>
  );
};

const styles = {
  overlay: {
    position: 'fixed',
    bottom: '1.5rem',
    left: '50%',
    transform: 'translateX(-50%)',
    zIndex: 10000,
    animation: 'slideUp 0.4s ease-out',
    width: '90%',
    maxWidth: '420px',
  },
  banner: {
    background: 'rgba(19, 22, 30, 0.95)',
    backdropFilter: 'blur(20px)',
    border: '1px solid rgba(0, 229, 160, 0.3)',
    borderRadius: '16px',
    padding: '1.25rem',
    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.5), 0 0 40px rgba(0, 229, 160, 0.1)',
  },
  iconRow: {
    display: 'flex',
    alignItems: 'center',
    gap: '0.75rem',
    marginBottom: '1rem',
  },
  appIcon: {
    width: '48px',
    height: '48px',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, #0d0f14, #1a1d27)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '1.5rem',
    border: '1px solid rgba(37, 42, 58, 0.8)',
    flexShrink: 0,
  },
  textCol: {
    display: 'flex',
    flexDirection: 'column',
    gap: '0.2rem',
  },
  title: {
    color: '#e8eaf2',
    fontSize: '1rem',
    fontFamily: "'Syne', sans-serif",
  },
  subtitle: {
    color: '#8892aa',
    fontSize: '0.82rem',
  },
  actions: {
    display: 'flex',
    gap: '0.75rem',
  },
  installBtn: {
    flex: 1,
    padding: '0.65rem 1rem',
    background: 'linear-gradient(135deg, #00e5a0, #00c98a)',
    color: '#0d0f14',
    fontWeight: 700,
    border: 'none',
    borderRadius: '10px',
    cursor: 'pointer',
    fontSize: '0.9rem',
    transition: 'transform 0.2s, box-shadow 0.2s',
  },
  dismissBtn: {
    flex: 1,
    padding: '0.65rem 1rem',
    background: 'transparent',
    color: '#8892aa',
    fontWeight: 500,
    border: '1px solid rgba(37, 42, 58, 0.8)',
    borderRadius: '10px',
    cursor: 'pointer',
    fontSize: '0.9rem',
    transition: 'color 0.2s',
  },
};

export default PWAInstallPrompt;
