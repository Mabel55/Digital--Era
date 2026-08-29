import { useState, useEffect, useCallback, useRef } from 'react';
import { 
  getUnsyncedProgress, 
  markProgressSynced, 
  clearSyncedProgress,
  getPendingSyncCount 
} from '../lib/offlineDB';

/**
 * useOfflineSync — Background sync hook
 * 
 * Watches for connectivity changes and automatically syncs
 * queued progress updates to the server when the user comes back online.
 * 
 * Usage:
 *   const { pendingCount, isSyncing, lastSyncTime, syncNow } = useOfflineSync(token);
 */
export function useOfflineSync(token) {
  const [pendingCount, setPendingCount] = useState(0);
  const [isSyncing, setIsSyncing] = useState(false);
  const [lastSyncTime, setLastSyncTime] = useState(null);
  const syncInProgress = useRef(false);

  // Refresh the pending count
  const refreshPendingCount = useCallback(async () => {
    try {
      const count = await getPendingSyncCount();
      setPendingCount(count);
    } catch (e) {
      console.error('[OfflineSync] Failed to get pending count:', e);
    }
  }, []);

  // Core sync function — pushes all queued progress to server
  const syncNow = useCallback(async () => {
    if (!token || !navigator.onLine || syncInProgress.current) return;

    syncInProgress.current = true;
    setIsSyncing(true);

    try {
      const unsyncedItems = await getUnsyncedProgress();
      
      if (unsyncedItems.length === 0) {
        setIsSyncing(false);
        syncInProgress.current = false;
        return;
      }

      console.log(`[OfflineSync] Syncing ${unsyncedItems.length} queued progress updates...`);

      const syncedIds = [];

      // Process each queued progress update
      for (const item of unsyncedItems) {
        try {
          const res = await fetch('/users/me/progress', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`,
            },
            body: JSON.stringify({
              course_name: item.courseName,
              lesson_index: item.lessonIndex,
            }),
          });

          if (res.ok) {
            syncedIds.push(item.id);
          } else if (res.status === 401) {
            // Token expired — stop syncing, user needs to re-login
            console.warn('[OfflineSync] Token expired, stopping sync');
            break;
          }
          // For other errors (500, etc.), skip this item and try the next
        } catch (networkErr) {
          // Network error mid-sync — stop and retry later
          console.warn('[OfflineSync] Network error during sync, will retry later');
          break;
        }
      }

      // Mark successfully synced items
      if (syncedIds.length > 0) {
        await markProgressSynced(syncedIds);
        console.log(`[OfflineSync] Successfully synced ${syncedIds.length}/${unsyncedItems.length} items`);
        setLastSyncTime(Date.now());
      }

      // Clean up old synced items
      await clearSyncedProgress();

      // Refresh count
      await refreshPendingCount();

    } catch (err) {
      console.error('[OfflineSync] Sync failed:', err);
    } finally {
      setIsSyncing(false);
      syncInProgress.current = false;
    }
  }, [token, refreshPendingCount]);

  // Watch for connectivity changes
  useEffect(() => {
    const handleOnline = () => {
      console.log('[OfflineSync] Back online — triggering sync');
      // Small delay to let the connection stabilize
      setTimeout(syncNow, 2000);
    };

    window.addEventListener('online', handleOnline);
    return () => window.removeEventListener('online', handleOnline);
  }, [syncNow]);

  // Initial sync on mount (if online and has token)
  useEffect(() => {
    refreshPendingCount();
    if (token && navigator.onLine) {
      // Sync any items that accumulated while offline
      syncNow();
    }
  }, [token, syncNow, refreshPendingCount]);

  // Periodic sync every 5 minutes while online
  useEffect(() => {
    if (!token) return;

    const interval = setInterval(() => {
      if (navigator.onLine) {
        syncNow();
      }
    }, 5 * 60 * 1000);

    return () => clearInterval(interval);
  }, [token, syncNow]);

  return {
    pendingCount,
    isSyncing,
    lastSyncTime,
    syncNow,
    refreshPendingCount,
  };
}
