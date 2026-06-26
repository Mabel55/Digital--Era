import json

with open('frontend/src/data/courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

courses = ['List Comprehensions', 'Django Web Framework', 'React Fundamentals', 'Pandas & NumPy Basics', 'CSS Styling & Layout']

for c in courses:
    pos = content.find(f'"{c}"')
    if pos != -1:
        print(f"Found: {c}")
        # print 50 chars around it
        start = max(0, pos - 20)
        end = min(len(content), pos + 100)
        print(repr(content[start:end]))
    else:
        print(f"NOT FOUND: {c}")
