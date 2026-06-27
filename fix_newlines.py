import json
import os

def fix_strings(obj):
    if isinstance(obj, dict):
        return {k: fix_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [fix_strings(item) for item in obj]
    elif isinstance(obj, str):
        # Replace literal backslash-n with actual newline
        return obj.replace('\\n', '\n').replace('\\t', '\t')
    else:
        return obj

tracks_dir = os.path.join('curriculum', 'tracks')

for filename in os.listdir(tracks_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(tracks_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        fixed_data = fix_strings(data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(fixed_data, f, indent=2, ensure_ascii=False)

print("Fixed formatting in all JSON files!")

# Rebuild courses.js
os.system("python build_courses.py")
