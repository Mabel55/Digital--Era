"""
Batch 5: Massive Expansion Script using robust injection engine.
Adding new lessons to various missing sections.
"""
import json

NEW_LESSONS = {

"Intro to Backend": [
  {
    "title": "What is the Backend?",
    "theory": "## Backend Architecture\nThe backend is the 'server-side' of an application. It handles:\n1. **Business Logic:** The rules of the application.\n2. **Database:** Storing and retrieving data.\n3. **APIs:** Communicating with the frontend.",
    "instructions": "## Task: Identify Backend Components\nAssign the correct component to the variables.",
    "starterCode": "# What stores the data?\ndata_storage = '___'\n\n# What processes the business rules?\nprocessor = '___'\n\nprint(f'{data_storage} and {processor}')",
    "solution": "data_storage = 'Database'\nprocessor = 'Server'\nprint(f'{data_storage} and {processor}')",
    "hint": "Database and Server",
    "rubric": "Correctly assigned Database and Server."
  },
  {
    "title": "Servers vs Clients",
    "theory": "## The Client-Server Model\n- **Client:** The browser or mobile app making requests.\n- **Server:** The computer in a data center responding to requests.",
    "instructions": "## Task: Server or Client?\nCreate a list of clients and a list of servers.",
    "starterCode": "clients = ['Browser', '___']\nservers = ['Database', '___']\nprint(clients, servers)",
    "solution": "clients = ['Browser', 'Mobile App']\nservers = ['Database', 'API']\nprint(clients, servers)",
    "hint": "Mobile App is a client. API is a server.",
    "rubric": "Lists properly categorized."
  },
  {
    "title": "Introduction to JSON",
    "theory": "## JSON Data Format\nJSON (JavaScript Object Notation) is the standard format for sending data between client and server.",
    "instructions": "## Task: Create a JSON Object\nWrite a valid JSON string representing a student.",
    "starterCode": "import json\nstudent_json = '___'\nparsed = json.loads(student_json)\nprint(parsed['name'])",
    "solution": "import json\nstudent_json = '{\"name\": \"Ada\", \"age\": 25}'\nparsed = json.loads(student_json)\nprint(parsed['name'])",
    "hint": "Use double quotes for keys and string values in JSON.",
    "rubric": "Valid JSON string that can be parsed."
  }
],

"Python for Web": [
  {
    "title": "Why Python for Backend?",
    "theory": "## Python's Web Ecosystem\nPython is popular for backend development due to its readability and powerful frameworks like Django and FastAPI.",
    "instructions": "## Task: List Python Frameworks\nCreate a list of 3 popular Python web frameworks.",
    "starterCode": "frameworks = ['___', '___', '___']\nfor f in frameworks: print(f)",
    "solution": "frameworks = ['Django', 'FastAPI', 'Flask']\nfor f in frameworks: print(f)",
    "hint": "Django, FastAPI, Flask.",
    "rubric": "3 valid Python frameworks listed."
  },
  {
    "title": "WSGI and ASGI",
    "theory": "## Server Interfaces\n- **WSGI:** Synchronous Python web standard (e.g., used by Django, Flask).\n- **ASGI:** Asynchronous Python web standard (e.g., used by FastAPI).",
    "instructions": "## Task: Sync vs Async\nCategorize frameworks into WSGI or ASGI.",
    "starterCode": "wsgi_frameworks = ['___']\nasgi_frameworks = ['___']\nprint(wsgi_frameworks, asgi_frameworks)",
    "solution": "wsgi_frameworks = ['Django', 'Flask']\nasgi_frameworks = ['FastAPI']\nprint(wsgi_frameworks, asgi_frameworks)",
    "hint": "Django/Flask are WSGI. FastAPI is ASGI.",
    "rubric": "Frameworks correctly assigned."
  },
  {
    "title": "Virtual Environments",
    "theory": "## Dependency Isolation\nVirtual environments keep dependencies required by different projects separate.",
    "instructions": "## Task: Create a venv command\nWrite the terminal command to create a virtual environment named `env`.",
    "starterCode": "command = '___ -m ___ ___'\nprint(command)",
    "solution": "command = 'python -m venv env'\nprint(command)",
    "hint": "python -m venv env",
    "rubric": "Command string matches exactly."
  }
],

"JavaScript Basics": [
  {
    "title": "Variables: let and const",
    "theory": "## Modern JS Variables\nUse `const` for values that won't change, and `let` for values that will. Avoid `var`.",
    "instructions": "## Task: Define Variables\nDefine a constant `PI` and a changing variable `score`.",
    "starterCode": "const js_code = `\n___ PI = 3.14159;\n___ score = 0;\nscore += 10;\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst PI = 3.14159;\nlet score = 0;\nscore += 10;\n`;\nconsole.log(js_code);",
    "hint": "const for PI, let for score.",
    "rubric": "const and let used correctly."
  },
  {
    "title": "Arrow Functions",
    "theory": "## Arrow Functions\nA shorter syntax for writing functions: `const add = (a, b) => a + b;`",
    "instructions": "## Task: Write an Arrow Function\nWrite an arrow function `multiply` that takes two numbers and returns their product.",
    "starterCode": "const js_code = `\nconst multiply = (___) => ___;\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst multiply = (a, b) => a * b;\n`;\nconsole.log(js_code);",
    "hint": "(a, b) => a * b",
    "rubric": "Arrow function syntax used properly."
  },
  {
    "title": "Array Methods (map, filter)",
    "theory": "## Functional Array Methods\n`map` transforms an array. `filter` removes elements based on a condition.",
    "instructions": "## Task: Map and Filter\nUse `map` to double an array, and `filter` to keep only even numbers.",
    "starterCode": "const js_code = `\nconst nums = [1, 2, 3, 4];\nconst doubled = nums.___(n => n * 2);\nconst evens = nums.___(n => n % 2 === 0);\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst nums = [1, 2, 3, 4];\nconst doubled = nums.map(n => n * 2);\nconst evens = nums.filter(n => n % 2 === 0);\n`;\nconsole.log(js_code);",
    "hint": "map for doubling, filter for evens.",
    "rubric": "map and filter methods used correctly."
  }
]

}

def inject_lessons_safe(filepath, new_lessons):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    manifest_start = content.find('courseManifest')
    if manifest_start == -1: return

    injected = 0
    for course_name, lessons in new_lessons.items():
        course_pos = content.find(f'"{course_name}":', manifest_start)
        if course_pos == -1: continue
        lessons_key = content.find('"lessons"', course_pos)
        if lessons_key == -1: continue
        bracket_start = content.find('[', lessons_key)
        if bracket_start == -1: continue
            
        depth = 0; bracket_end = -1
        for i in range(bracket_start, min(bracket_start + 100000, len(content))):
            if content[i] == '[': depth += 1
            elif content[i] == ']':
                depth -= 1
                if depth == 0: bracket_end = i; break
        if bracket_end == -1: continue

        first_title = f'"title": "{lessons[0]["title"]}"'
        if content[bracket_start:bracket_end].find(first_title) != -1: continue

        new_entries = ''
        for lesson in lessons:
            new_entries += ',\\n      ' + json.dumps(lesson, ensure_ascii=False)
            
        content = content[:bracket_end] + new_entries + '\\n    ' + content[bracket_end:]
        injected += len(lessons)
        print(f'OK: Added {len(lessons)} lessons to "{course_name}"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\\nTOTAL: {injected}')

if __name__ == '__main__':
    inject_lessons_safe('frontend/src/data/courses.js', NEW_LESSONS)
