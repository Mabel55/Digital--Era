import re

with open('frontend/src/data/courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all course names in courseManifest
courses = re.findall(r'"([^"]+)":\s*\{\s*"aiRubric"', content)

for course in courses:
    start = content.find(f'"{course}"')
    # Find the lessons array
    lessons_start = content.find('"lessons"', start)
    if lessons_start == -1:
        print(f'{course}: 0 lessons')
        continue
    # Count "title" entries within ~50000 chars
    block = content[lessons_start:lessons_start+50000]
    # Find the closing of this course's lessons array
    bracket_count = 0
    end_idx = 0
    found_start = False
    for i, ch in enumerate(block):
        if ch == '[' and not found_start:
            found_start = True
            bracket_count = 1
            continue
        if found_start:
            if ch == '[':
                bracket_count += 1
            elif ch == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    end_idx = i
                    break
    
    lesson_block = block[:end_idx] if end_idx > 0 else block[:5000]
    lesson_count = len(re.findall(r'"title":\s*"', lesson_block))
    print(f'{course}: {lesson_count} lessons')

print(f'\nTotal courses in manifest: {len(courses)}')
