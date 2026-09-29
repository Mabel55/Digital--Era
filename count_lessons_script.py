import re

with open(r'frontend\src\data\courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all course names and count their lessons
manifest_start = content.find('export const courseManifest = {')
manifest = content[manifest_start:]

# Find each course and count lessons
courses = re.findall(r'"([^"]+)":\s*\{\s*"aiRubric"', manifest)
for i, course in enumerate(courses):
    pos = manifest.find(f'"{course}"')
    # Find end of this course
    if i + 1 < len(courses):
        next_course = courses[i+1]
        next_pos = manifest.find(f'"{next_course}"')
    else:
        next_pos = len(manifest)
        
    chunk = manifest[pos:next_pos]
    lesson_count = chunk.count('"title":')
    print(f'{course}: {lesson_count} lessons')
