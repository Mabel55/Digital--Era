import json
with open('curriculum/tracks/backend.json', encoding='utf-8') as f:
    data = json.load(f)

for topic in data.values():
    for lesson in topic.get('lessons', []):
        if lesson.get('type') != 'quiz' and len(lesson.get('theory', '')) <= 800:
            print(f'\"{lesson.get("title")}\": \"\",')
