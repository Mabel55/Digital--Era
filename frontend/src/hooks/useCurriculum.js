import { useQuery } from '@tanstack/react-query';

export const useCurriculum = () => {
  return useQuery({
    queryKey: ['curriculumData'],
    queryFn: async () => {
      const response = await fetch('/curriculum.json');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    },
    staleTime: Infinity, // The JSON doesn't change unless the app is rebuilt
  });
};
