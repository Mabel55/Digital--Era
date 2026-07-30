import { useQuery } from '@tanstack/react-query';

export const useCurriculum = () => {
  return useQuery({
    queryKey: ['curriculumData'],
    queryFn: async () => {
      // Add a cache buster so that if a user has a corrupted HTML file cached for this URL,
      // the browser is forced to re-fetch the real JSON.
      const response = await fetch('/curriculum.json?v=' + Date.now());
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    },
    staleTime: Infinity, // The JSON doesn't change unless the app is rebuilt
  });
};
