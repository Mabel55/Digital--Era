"""
Phase 1: Strip all 'Part 2' and 'Part 3' duplicate lessons from every track JSON file.
Keeps all original lessons intact.
"""
import json, os

tracks_dir = "curriculum/tracks"
total_removed = 0

for filename in sorted(os.listdir(tracks_dir)):
    if not filename.endswith(".json"):
        continue
    
    filepath = os.path.join(tracks_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    file_removed = 0
    for course_name, course_data in data.items():
        if "lessons" not in course_data:
            continue
        
        original_count = len(course_data["lessons"])
        course_data["lessons"] = [
            lesson for lesson in course_data["lessons"]
            if "- Part 2" not in lesson.get("title", "") 
            and "- Part 3" not in lesson.get("title", "")
        ]
        removed = original_count - len(course_data["lessons"])
        file_removed += removed
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    total_removed += file_removed
    print(f"[OK] {filename}: removed {file_removed} duplicates")

print(f"\nDONE! Total removed: {total_removed} duplicate lessons")
