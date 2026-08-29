/**
 * offlineDB.js — IndexedDB wrapper for offline progress storage
 * 
 * Stores lesson completions, XP gains, and code submissions locally
 * so learners never lose progress during power outages or data loss.
 * Syncs back to server when connectivity returns.
 */

const DB_NAME = 'digital-era-offline';
const DB_VERSION = 1;

// Store names
const STORES = {
  PROGRESS_QUEUE: 'progress-queue',   // Queued progress updates to sync
  CACHED_PROGRESS: 'cached-progress', // Local mirror of user progress
  SAVED_CODE: 'saved-code',           // Code snapshots per lesson
  CACHED_CURRICULUM: 'cached-curriculum', // Backup of curriculum.json
};

/**
 * Open (or create) the IndexedDB database
 */
function openDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION);

    request.onupgradeneeded = (event) => {
      const db = event.target.result;

      // Queue of progress updates to sync when online
      if (!db.objectStoreNames.contains(STORES.PROGRESS_QUEUE)) {
        const store = db.createObjectStore(STORES.PROGRESS_QUEUE, { 
          keyPath: 'id', 
          autoIncrement: true 
        });
        store.createIndex('timestamp', 'timestamp', { unique: false });
        store.createIndex('synced', 'synced', { unique: false });
      }

      // Local cache of user's progress (mirrors server state)
      if (!db.objectStoreNames.contains(STORES.CACHED_PROGRESS)) {
        db.createObjectStore(STORES.CACHED_PROGRESS, { keyPath: 'courseName' });
      }

      // Saved code per lesson (more reliable than localStorage for large data)
      if (!db.objectStoreNames.contains(STORES.SAVED_CODE)) {
        db.createObjectStore(STORES.SAVED_CODE, { keyPath: 'key' });
      }

      // Curriculum JSON backup
      if (!db.objectStoreNames.contains(STORES.CACHED_CURRICULUM)) {
        db.createObjectStore(STORES.CACHED_CURRICULUM, { keyPath: 'id' });
      }
    };

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

/**
 * Helper to run a transaction
 */
async function withStore(storeName, mode, callback) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(storeName, mode);
    const store = tx.objectStore(storeName);
    const result = callback(store);
    
    tx.oncomplete = () => {
      db.close();
      resolve(result);
    };
    tx.onerror = () => {
      db.close();
      reject(tx.error);
    };
  });
}

// ─── Progress Queue (offline-first progress tracking) ───

/**
 * Queue a progress update for later sync.
 * Called every time a lesson is completed, even if offline.
 */
export async function queueProgressUpdate(courseName, lessonIndex, xpEarned = 10) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.PROGRESS_QUEUE, 'readwrite');
    const store = tx.objectStore(STORES.PROGRESS_QUEUE);
    
    store.add({
      courseName,
      lessonIndex,
      xpEarned,
      timestamp: Date.now(),
      synced: false,
    });

    tx.oncomplete = () => { db.close(); resolve(); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

/**
 * Get all unsynced progress updates
 */
export async function getUnsyncedProgress() {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.PROGRESS_QUEUE, 'readonly');
    const store = tx.objectStore(STORES.PROGRESS_QUEUE);
    const index = store.index('synced');
    const request = index.getAll(false);

    request.onsuccess = () => { db.close(); resolve(request.result); };
    request.onerror = () => { db.close(); reject(request.error); };
  });
}

/**
 * Mark progress updates as synced after successful server push
 */
export async function markProgressSynced(ids) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.PROGRESS_QUEUE, 'readwrite');
    const store = tx.objectStore(STORES.PROGRESS_QUEUE);

    ids.forEach(id => {
      const request = store.get(id);
      request.onsuccess = () => {
        const record = request.result;
        if (record) {
          record.synced = true;
          store.put(record);
        }
      };
    });

    tx.oncomplete = () => { db.close(); resolve(); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

/**
 * Clear all synced items from the queue (housekeeping)
 */
export async function clearSyncedProgress() {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.PROGRESS_QUEUE, 'readwrite');
    const store = tx.objectStore(STORES.PROGRESS_QUEUE);
    const index = store.index('synced');
    const request = index.openCursor(true);

    request.onsuccess = (event) => {
      const cursor = event.target.result;
      if (cursor) {
        cursor.delete();
        cursor.continue();
      }
    };

    tx.oncomplete = () => { db.close(); resolve(); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

// ─── Local Progress Cache (mirrors server) ───

/**
 * Save local progress state for a course
 */
export async function saveCachedProgress(courseName, completedLessons) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.CACHED_PROGRESS, 'readwrite');
    const store = tx.objectStore(STORES.CACHED_PROGRESS);
    
    store.put({
      courseName,
      completedLessons,
      updatedAt: Date.now(),
    });

    tx.oncomplete = () => { db.close(); resolve(); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

/**
 * Get cached progress for a course
 */
export async function getCachedProgress(courseName) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.CACHED_PROGRESS, 'readonly');
    const store = tx.objectStore(STORES.CACHED_PROGRESS);
    const request = store.get(courseName);

    request.onsuccess = () => { db.close(); resolve(request.result || null); };
    request.onerror = () => { db.close(); reject(request.error); };
  });
}

// ─── Saved Code ───

/**
 * Save code for a specific lesson (replaces localStorage usage)
 */
export async function saveCode(courseName, lessonIndex, code) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.SAVED_CODE, 'readwrite');
    const store = tx.objectStore(STORES.SAVED_CODE);
    
    store.put({
      key: `${courseName}_${lessonIndex}`,
      courseName,
      lessonIndex,
      code,
      savedAt: Date.now(),
    });

    tx.oncomplete = () => { db.close(); resolve(); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

/**
 * Load saved code for a specific lesson
 */
export async function loadCode(courseName, lessonIndex) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.SAVED_CODE, 'readonly');
    const store = tx.objectStore(STORES.SAVED_CODE);
    const request = store.get(`${courseName}_${lessonIndex}`);

    request.onsuccess = () => { db.close(); resolve(request.result?.code || null); };
    request.onerror = () => { db.close(); reject(request.error); };
  });
}

// ─── Curriculum Cache ───

/**
 * Cache curriculum.json data in IndexedDB as a fallback
 * This provides a second layer of offline caching beyond the Service Worker
 */
export async function cacheCurriculum(data) {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.CACHED_CURRICULUM, 'readwrite');
    const store = tx.objectStore(STORES.CACHED_CURRICULUM);
    
    store.put({
      id: 'curriculum',
      data,
      cachedAt: Date.now(),
    });

    tx.oncomplete = () => { db.close(); resolve(); };
    tx.onerror = () => { db.close(); reject(tx.error); };
  });
}

/**
 * Get cached curriculum from IndexedDB
 */
export async function getCachedCurriculum() {
  const db = await openDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(STORES.CACHED_CURRICULUM, 'readonly');
    const store = tx.objectStore(STORES.CACHED_CURRICULUM);
    const request = store.get('curriculum');

    request.onsuccess = () => { db.close(); resolve(request.result?.data || null); };
    request.onerror = () => { db.close(); reject(request.error); };
  });
}

// ─── Sync Status Helpers ───

/**
 * Get count of pending (unsynced) items
 */
export async function getPendingSyncCount() {
  const items = await getUnsyncedProgress();
  return items.length;
}

/**
 * Check if there are items waiting to sync
 */
export async function hasPendingSync() {
  const count = await getPendingSyncCount();
  return count > 0;
}
