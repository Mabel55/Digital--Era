import json
from rebuild_curriculum import track_courses
import os

index_curriculum = {}
for track, levels in track_courses.items():
    index_curriculum[track] = {}
    for level, courses in levels.items():
        index_curriculum[track][level] = courses
        
with open(os.path.join("curriculum", "index.json"), "w", encoding="utf-8") as f:
    json.dump(index_curriculum, f, indent=2)

print("Fixed index.json")
os.system("python build_courses.py")
