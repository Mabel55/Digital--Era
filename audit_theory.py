import json
import os

tracks_dir = "curriculum/tracks"
short_theories = []
total_lessons = 0

for fname in sorted(os.listdir(tracks_dir)):
    if not fname.endswith(".json"):
        continue
    filepath = os.path.join(tracks_dir, fname)
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            courses = json.load(f)
        except:
            continue
    
    if not isinstance(courses, dict):
        continue

    for course_name, course_data in courses.items():
        if not isinstance(course_data, dict):
            continue
        lessons = course_data.get("lessons", [])
        for lesson in lessons:
            total_lessons += 1
            title = lesson.get("title", "UNKNOWN")
            theory = lesson.get("theory", "")
            theory_len = len(theory)
            if theory_len < 500:
                short_theories.append({
                    "file": fname,
                    "course": course_name,
                    "title": title,
                    "length": theory_len
                })

print(f"Total lessons: {total_lessons}")
print(f"Lessons with short theory (<500 chars): {len(short_theories)}")
print()

# Group by file
by_file = {}
for s in short_theories:
    by_file.setdefault(s["file"], []).append(s)

for fname, items in sorted(by_file.items()):
    print(f"\n=== {fname}: {len(items)} short ===")
