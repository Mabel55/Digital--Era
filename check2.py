import json

with open('frontend/src/data/courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

manifest_start = content.find('courseManifest')
print(f"Manifest starts at: {manifest_start}")

courses = ['List Comprehensions', 'Django Web Framework', 'React Fundamentals', 'Pandas & NumPy Basics', 'CSS Styling & Layout']

for c in courses:
    pos = content.find(f'"{c}":', manifest_start)
    if pos != -1:
        print(f"Manifest Key Found: {c}")
    else:
        print(f"NOT IN MANIFEST: {c}")
