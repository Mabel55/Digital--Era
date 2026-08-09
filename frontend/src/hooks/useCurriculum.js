import { useQuery, useQueryClient } from '@tanstack/react-query';

// Bump this version string when curriculum.json is updated in a new deployment.
// This allows the browser to cache the file aggressively between deploys.
const CURRICULUM_VERSION = '1';

const fetchCurriculum = async () => {
  const response = await fetch(`/curriculum.json?v=${CURRICULUM_VERSION}`);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
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
  });
};

