import json, os

tracks_dir = "curriculum/tracks"
total_courses = 0
total_lessons = 0

for filename in sorted(os.listdir(tracks_dir)):
    if filename.endswith(".json"):
        filepath = os.path.join(tracks_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            courses = len(data)
            lessons = sum(len(v.get("lessons", [])) for v in data.values())
            total_courses += courses
            total_lessons += lessons
            print(f"{filename}: {courses} courses, {lessons} lessons")

print(f"\n--- TOTAL: {total_courses} courses, {total_lessons} lessons ---")
