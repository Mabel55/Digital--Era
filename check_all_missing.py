import json
import glob

missing = {}
for file in glob.glob('curriculum/tracks/*.json'):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for topic, topic_data in data.items():
        for lesson in topic_data.get('lessons', []):
            if lesson.get('type') != 'quiz' and len(lesson.get('theory', '')) <= 800:
                missing.setdefault(file, []).append(lesson.get('title'))

for file, titles in missing.items():
    print(file, len(titles))
    print(titles)
