import json
import glob

missing = []
for f in glob.glob('curriculum/tracks/*.json'):
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for course, course_data in data.items():
            if len(course_data['lessons']) == 1 and course_data['lessons'][0]['title'].endswith('Coming Soon'):
                missing.append(course)

with open('missing_courses.txt', 'w', encoding='utf-8') as f:
    for m in missing:
        f.write(m + '\n')
print(f"Found {len(missing)} placeholder courses")
