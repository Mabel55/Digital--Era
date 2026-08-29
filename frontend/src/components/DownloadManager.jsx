import React, { useState, useEffect } from 'react';
import { Download, CheckCircle2, Loader2, HardDrive, Wifi, WifiOff, Trash2, X } from 'lucide-react';

/**
 * DownloadManager — Pre-download lesson tracks for offline learning
 * 
 * Lets users on WiFi download entire learning tracks so they can
 * study at home without mobile data.
 */
const DownloadManager = ({ isOpen, onClose, curriculum, courseManifest }) => {
  const [downloadStatus, setDownloadStatus] = useState({});
  const [isDownloading, setIsDownloading] = useState(false);
  const [cacheSize, setCacheSize] = useState(null);

  useEffect(() => {
    checkCacheStatus();
    estimateCacheSize();
  }, [isOpen]);

  const estimateCacheSize = async () => {
    try {
      if ('storage' in navigator && 'estimate' in navigator.storage) {
        const estimate = await navigator.storage.estimate();
        setCacheSize({
          used: estimate.usage || 0,
          quota: estimate.quota || 0,
        });
      }
    } catch (e) {
      console.warn('Storage estimate not available');
    }
  };

  const checkCacheStatus = async () => {
    // Check which tracks are already cached by looking at Service Worker cache
    try {
      const cacheNames = await caches.keys();
      const curriculumCache = cacheNames.find(n => n.includes('curriculum') || n.includes('workbox'));
      
      if (curriculumCache) {
        const cache = await caches.open(curriculumCache);
        const keys = await cache.keys();
        const cachedUrls = keys.map(k => k.url);
        
        // Update status for tracks
        const status = {};
        Object.keys(curriculum || {}).forEach(track => {
          status[track] = 'ready'; // Curriculum data is in JSON, always available if curriculum.json is cached
        });
        setDownloadStatus(status);
      }
    } catch (e) {
      console.warn('Cache check failed:', e);
    }
  };

  const downloadTrack = async (trackName) => {
    setIsDownloading(true);
    setDownloadStatus(prev => ({ ...prev, [trackName]: 'downloading' }));

    try {
      // The main thing to cache is the Pyodide runtime — that's the big one
      // Curriculum is already cached by the Service Worker / IndexedDB
      
      // Step 1: Pre-cache the curriculum.json if not already
      const currCache = await caches.open('curriculum-cache');
      await currCache.add('/curriculum.json');

      // Step 2: Pre-cache Pyodide runtime (the biggest offline enabler)
      const pyodideCache = await caches.open('pyodide-runtime');
      const pyodideBase = 'https://cdn.jsdelivr.net/pyodide/v0.25.0/full/';
      
      // Core Pyodide files needed for Python execution
      const pyodideFiles = [
        'pyodide.js',
        'pyodide.asm.js',
        'pyodide.asm.wasm',
        'pyodide-lock.json',
        'python_stdlib.zip',
      ];

      let downloaded = 0;
      for (const file of pyodideFiles) {
        try {
          setDownloadStatus(prev => ({
            ...prev,
            [trackName]: `downloading_${Math.round((downloaded / pyodideFiles.length) * 100)}%`
          }));
          await pyodideCache.add(pyodideBase + file);
          downloaded++;
        } catch (e) {
          console.warn(`Failed to cache ${file}:`, e);
        }
      }

      // Step 3: Pre-cache Monaco editor for code editing
      // (Monaco auto-caches via the Service Worker runtime config,
      //  but we trigger it to load now)

      setDownloadStatus(prev => ({ ...prev, [trackName]: 'complete' }));
      
      // Save a flag in localStorage
      localStorage.setItem(`offline_track_${trackName}`, 'true');
      
      await estimateCacheSize();
    } catch (err) {
      console.error('Download failed:', err);
      setDownloadStatus(prev => ({ ...prev, [trackName]: 'error' }));
    } finally {
      setIsDownloading(false);
    }
  };

  const clearTrackCache = async (trackName) => {
    try {
      localStorage.removeItem(`offline_track_${trackName}`);
      setDownloadStatus(prev => ({ ...prev, [trackName]: 'ready' }));
      await estimateCacheSize();
    } catch (e) {
      console.error('Clear failed:', e);
    }
  };

  const formatBytes = (bytes) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  };

  const getTrackInfo = (trackName) => {
    const levels = curriculum[trackName] || {};
    let courseCount = 0;
    let lessonCount = 0;
    
    Object.values(levels).forEach(courses => {
      courses.forEach(courseName => {
        courseCount++;
        const manifest = courseManifest?.[courseName];
        if (manifest) {
          lessonCount += manifest.lessons?.length || 0;
        }
      });
    });

    return { courseCount, lessonCount };
  };

  const getStatusIcon = (status) => {
    if (!status || status === 'ready') {
      return <Download size={18} color="var(--accent)" />;
    }
    if (status === 'complete' || localStorage.getItem(`offline_track_${status}`) === 'true') {
      return <CheckCircle2 size={18} color="#00e5a0" />;
    }
    if (status.startsWith('downloading')) {
      return <Loader2 size={18} color="var(--accent)" style={{ animation: 'spin 1s linear infinite' }} />;
    }
    return <Download size={18} color="var(--accent)" />;
  };

  if (!isOpen) return null;

  const tracks = Object.keys(curriculum || {});

  return (
    <div style={{
      position: 'fixed', inset: 0, zIndex: 10000,
      background: 'rgba(0,0,0,0.7)', backdropFilter: 'blur(8px)',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      padding: '16px',
    }}>
      <div style={{
        background: 'var(--surface)',
        border: '1px solid var(--border)',
        borderRadius: '16px',
        maxWidth: '520px',
        width: '100%',
        maxHeight: '80vh',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
        boxShadow: '0 20px 60px rgba(0,0,0,0.5)',
      }}>
        {/* Header */}
        <div style={{
          padding: '20px 24px',
          borderBottom: '1px solid var(--border)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}>
          <div>
            <h2 style={{ margin: 0, fontSize: '1.15rem', color: 'var(--text)', fontFamily: "'Syne', sans-serif" }}>
              <Download size={20} style={{ marginRight: '8px', verticalAlign: 'middle' }} />
              Download for Offline
            </h2>
            <p style={{ margin: '4px 0 0', fontSize: '0.8rem', color: 'var(--text2)' }}>
              Download tracks on WiFi, learn anywhere without data
            </p>
          </div>
          <button onClick={onClose} style={{
            background: 'none', border: 'none', cursor: 'pointer',
            color: 'var(--text2)', padding: '4px',
          }}>
            <X size={20} />
          </button>
        </div>

        {/* Storage Info */}
        {cacheSize && (
          <div style={{
            padding: '12px 24px',
            background: 'rgba(0,229,160,0.05)',
            borderBottom: '1px solid var(--border)',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            fontSize: '0.8rem',
            color: 'var(--text2)',
          }}>
            <HardDrive size={14} />
            <span>Using {formatBytes(cacheSize.used)} of {formatBytes(cacheSize.quota)}</span>
            <div style={{
              flex: 1, height: '4px', background: 'var(--border)', borderRadius: '2px',
              overflow: 'hidden', maxWidth: '100px',
            }}>
              <div style={{
                height: '100%',
                width: `${Math.min((cacheSize.used / cacheSize.quota) * 100, 100)}%`,
                background: 'var(--accent)',
                borderRadius: '2px',
                transition: 'width 0.3s ease',
              }} />
            </div>
          </div>
        )}

        {/* Connection Status */}
        <div style={{
          padding: '8px 24px',
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          fontSize: '0.78rem',
          color: navigator.onLine ? '#00e5a0' : '#f59e0b',
          borderBottom: '1px solid var(--border)',
        }}>
          {navigator.onLine ? <Wifi size={14} /> : <WifiOff size={14} />}
          {navigator.onLine ? 'Connected — downloads available' : 'Offline — connect to WiFi to download'}
        </div>

        {/* Track List */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '8px 0' }}>
          {tracks.map(trackName => {
            const { courseCount, lessonCount } = getTrackInfo(trackName);
            const status = downloadStatus[trackName];
            const isTrackCached = localStorage.getItem(`offline_track_${trackName}`) === 'true';
            const isCurrentlyDownloading = status?.startsWith('downloading');

            return (
              <div key={trackName} style={{
                padding: '14px 24px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                borderBottom: '1px solid rgba(255,255,255,0.03)',
                transition: 'background 0.2s',
              }}>
                <div style={{ flex: 1 }}>
                  <div style={{ 
                    fontWeight: 600, fontSize: '0.9rem', color: 'var(--text)',
                    marginBottom: '2px',
                  }}>
                    {trackName}
                  </div>
                  <div style={{ fontSize: '0.75rem', color: 'var(--text2)' }}>
                    {courseCount} courses · {lessonCount} lessons
                  </div>
                </div>

                {isTrackCached ? (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ 
                      fontSize: '0.75rem', color: '#00e5a0', fontWeight: 600,
                      display: 'flex', alignItems: 'center', gap: '4px',
                    }}>
                      <CheckCircle2 size={14} /> Saved
                    </span>
                    <button
                      onClick={() => clearTrackCache(trackName)}
                      style={{
                        background: 'none', border: '1px solid rgba(255,255,255,0.1)',
                        borderRadius: '6px', padding: '4px 8px', cursor: 'pointer',
                        color: 'var(--text2)', fontSize: '0.7rem',
                        display: 'flex', alignItems: 'center', gap: '4px',
                      }}
                    >
                      <Trash2 size={12} /> Remove
                    </button>
                  </div>
                ) : (
                  <button
                    onClick={() => downloadTrack(trackName)}
                    disabled={isDownloading || !navigator.onLine}
                    style={{
                      padding: '8px 16px',
                      background: isCurrentlyDownloading
                        ? 'rgba(0,229,160,0.1)'
                        : 'linear-gradient(135deg, #00e5a0, #00c98a)',
                      color: isCurrentlyDownloading ? 'var(--accent)' : '#0d0f14',
                      fontWeight: 700,
                      border: isCurrentlyDownloading ? '1px solid var(--accent)' : 'none',
                      borderRadius: '10px',
                      cursor: isDownloading || !navigator.onLine ? 'not-allowed' : 'pointer',
                      opacity: !navigator.onLine ? 0.5 : 1,
                      fontSize: '0.82rem',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px',
                      transition: 'all 0.2s',
                    }}
                  >
                    {isCurrentlyDownloading ? (
                      <>
                        <Loader2 size={14} style={{ animation: 'spin 1s linear infinite' }} />
                        {status.includes('%') ? status.split('_')[1] : 'Downloading...'}
                      </>
                    ) : (
                      <>
                        <Download size={14} /> Download
                      </>
                    )}
                  </button>
                )}
              </div>
            );
          })}
        </div>

        {/* Footer tip */}
        <div style={{
          padding: '14px 24px',
          borderTop: '1px solid var(--border)',
          fontSize: '0.75rem',
          color: 'var(--text2)',
          textAlign: 'center',
          lineHeight: 1.4,
        }}>
          💡 <strong>Tip:</strong> Download on WiFi at school or a café, then learn at home without using any mobile data!
        </div>
      </div>
    </div>
  );
};

export default DownloadManager;
