import { useQuery, useQueryClient } from '@tanstack/react-query';
import { cacheCurriculum, getCachedCurriculum } from '../lib/offlineDB';

// Bump this version string when curriculum.json is updated in a new deployment.
// This allows the browser to cache the file aggressively between deploys.
const CURRICULUM_VERSION = '1';

const fetchCurriculum = async () => {
  try {
    const response = await fetch(`/curriculum.json?v=${CURRICULUM_VERSION}`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    
    // ★ Cache in IndexedDB as a second-layer offline backup
    // The Service Worker caches it too, but IndexedDB survives cache eviction
    try {
      await cacheCurriculum(data);
    } catch (cacheErr) {
      console.warn('[Curriculum] IndexedDB cache failed (non-critical):', cacheErr);
    }
    
    return data;
  } catch (networkError) {
    // ★ Network failed — try IndexedDB fallback
    console.log('[Curriculum] Network failed, trying IndexedDB cache...');
    const cached = await getCachedCurriculum();
    if (cached) {
      console.log('[Curriculum] Loaded from IndexedDB cache');
      return cached;
    }
    // No cache available either — propagate the error
    throw networkError;
  }
};

// Kick off the fetch immediately when this module is first imported — before auth
// resolves — so the 2.1 MB file is in-flight while the user profile loads.
let prefetchStarted = false;

export const prefetchCurriculum = (queryClient) => {
  if (prefetchStarted) return;
  prefetchStarted = true;
  queryClient.prefetchQuery({
    queryKey: ['curriculumData'],
    queryFn: fetchCurriculum,
    staleTime: Infinity,
  });
};

export const useCurriculum = () => {
  return useQuery({
    queryKey: ['curriculumData'],
    queryFn: fetchCurriculum,
    staleTime: Infinity,  // Never re-fetch while the app is open
    gcTime: 1000 * 60 * 60, // Keep in React Query cache for 1 hour
    // ★ Keep retrying — important for intermittent connections
    retry: 2,
    retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 10000),
  });
};
