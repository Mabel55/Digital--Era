import json
import re
import os

# 1. Read courses.js and extract the courseManifest JSON
with open(r'frontend\src\data\courses.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Find the courseManifest object
start_idx = js_content.find('export const courseManifest = ') + len('export const courseManifest = ')
end_idx = js_content.find('; // end courseManifest')
manifest_json_str = js_content[start_idx:end_idx]

# Load it into a python dict
manifest = json.loads(manifest_json_str)

# 2. Read frontend.json
frontend_json_path = os.path.join('curriculum', 'tracks', 'frontend.json')
with open(frontend_json_path, 'r', encoding='utf-8') as f:
    frontend_data = json.load(f)

# 3. Update the three courses we added beginner lessons to
courses_to_update = ["HTML5 Essentials", "CSS Styling", "JS Basics"]
for course in courses_to_update:
    if course in manifest:
        frontend_data[course] = manifest[course]
        print(f"Updated {course} in frontend.json with {len(manifest[course]['lessons'])} lessons.")
    else:
        print(f"Warning: {course} not found in parsed manifest.")

# 4. Save frontend.json
with open(frontend_json_path, 'w', encoding='utf-8') as f:
    json.dump(frontend_data, f, ensure_ascii=False, indent=2)

print("Saved frontend.json successfully.")
