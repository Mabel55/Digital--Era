import json, os

tracks_dir = "curriculum/tracks"

total_original = 0
total_dupes = 0
total_quizzes = 0

for filename in sorted(os.listdir(tracks_dir)):
    if filename.endswith(".json"):
        filepath = os.path.join(tracks_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            file_orig = 0
            file_dupes = 0
            file_quizzes = 0
            
            for course_name, course_data in data.items():
                lessons = course_data.get("lessons", [])
                for lesson in lessons:
                    title = lesson.get("title", "")
                    if "- Part 2" in title or "- Part 3" in title:
                        file_dupes += 1
                    elif lesson.get("type") == "quiz" and ("Part 2" in title or "Part 3" in title):
                        file_dupes += 1
                    else:
                        file_orig += 1
                        if lesson.get("type") == "quiz":
                            file_quizzes += 1
            
            total_original += file_orig
            total_dupes += file_dupes
            print(f"{filename}: {file_orig} original, {file_dupes} duplicates, {file_orig + file_dupes} total")

print(f"\n{'='*60}")
print(f"TOTAL ORIGINAL: {total_original}")
print(f"TOTAL DUPLICATES: {total_dupes}")
print(f"TOTAL ALL: {total_original + total_dupes}")
print(f"\nAfter removing dupes, we need {1000 - total_original} new lessons to reach 1000+")
