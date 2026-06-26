import json, glob

files = glob.glob('curriculum/tracks/*.json')
total_courses = 0
total_lessons = 0

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            track_courses = len(data)
            track_lessons = sum(len(c.get('lessons', [])) for c in data.values())
            
            total_courses += track_courses
            total_lessons += track_lessons
    except Exception as e:
        print(f"Error reading {f}: {e}")

print(f"Validation Complete.")
print(f"Total Tracks: {len(files)}")
print(f"Total Courses: {total_courses}")
print(f"Total Lessons: {total_lessons}")
