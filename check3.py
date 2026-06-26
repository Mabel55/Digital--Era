import json

with open('frontend/src/data/courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Only look inside courseManifest
manifest_start = content.find('export const courseManifest')
manifest_content = content[manifest_start:]

courses_to_check = ['Python Fundamentals', 'SQL Fundamentals', 'HTML Essentials', 'Agent Foundations & Tools']

for c in courses_to_check:
    c_pos = manifest_content.find(f'"{c}":')
    if c_pos != -1:
        lessons_pos = manifest_content.find('"lessons":', c_pos)
        bracket_pos = manifest_content.find('[', lessons_pos)
        # Just grab the next 1000 chars to see what lessons it has
        block = manifest_content[bracket_pos:bracket_pos+1000]
        titles = [line.strip() for line in block.split('\\n') if '"title"' in line]
        print(f"\\n--- {c} ---")
        for t in titles[:5]:
            print(t)
    else:
        print(f"NOT FOUND: {c}")
