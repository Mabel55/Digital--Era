import re

with open('frontend/src/data/courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace literal \n with actual newline
content = content.replace(',\\n      {', ',\n      {')
content = content.replace('}\\n    ]', '}\n    ]')

with open('frontend/src/data/courses.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed syntax errors in courses.js")
