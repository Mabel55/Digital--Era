"""
Batch 4: Re-apply List Comprehensions, Django, React, Pandas, CSS Styling
"""
import json

NEW_LESSONS = {

"List Comprehensions": [
  {
    "title": "Nested Comprehensions",
    "theory": "## Nested List Comprehensions\n```python\n# Flatten a 2D list\nmatrix = [[1,2,3], [4,5,6], [7,8,9]]\nflat = [num for row in matrix for num in row]\n# [1, 2, 3, 4, 5, 6, 7, 8, 9]\n\n# Create a 2D grid\ngrid = [[i*j for j in range(1,4)] for i in range(1,4)]\n# [[1,2,3], [2,4,6], [3,6,9]]\n\n# Conditional nested\neven_from_matrix = [n for row in matrix for n in row if n % 2 == 0]\n# [2, 4, 6, 8]\n```",
    "instructions": "## Task: Matrix Operations\n1. Create a 5x5 multiplication table using nested comprehension\n2. Flatten it to a single list\n3. Filter only values greater than 10\n4. Create a dict mapping value to its position",
    "starterCode": "# 5x5 multiplication table\ntable = [[r * c for c in range(1, ___)] for r in range(1, ___)]\n\nprint('Multiplication Table:')\nfor row in table:\n    print([f'{n:3}' for n in row])\n\n# Flatten\nflat = [n for row in ___ for n in ___]\nprint(f'\\nFlattened: {flat}')\n\n# Filter > 10\nbig = [n for n in flat if n > ___]\nprint(f'Values > 10: {sorted(set(big))}')\n\n# Position map\npositions = {\n    table[r][c]: (r+1, c+1)\n    for r in range(___)\n    for c in range(5)\n}\nprint(f'\\nPosition of 12: row {positions[12][0]}, col {positions[12][1]}')",
    "solution": "table=[[r*c for c in range(1,6)] for r in range(1,6)]\nprint('Multiplication Table:')\nfor row in table:print([f'{n:3}' for n in row])\nflat=[n for row in table for n in row]\nprint(f'\\nFlattened: {flat}')\nbig=[n for n in flat if n>10]\nprint(f'Values > 10: {sorted(set(big))}')\npositions={table[r][c]:(r+1,c+1) for r in range(5) for c in range(5)}\nprint(f'\\nPosition of 12: row {positions[12][0]}, col {positions[12][1]}')",
    "hint": "range(1, 6) for 1-5. Nested for in comprehension flattens. Dict comprehension for positions.",
    "rubric": "5x5 table created. Flattened correctly. Filtered > 10. Position dict maps values."
  },
  {
    "title": "Generator Expressions vs List Comps",
    "theory": "## Generators vs Lists\n```python\n# List comprehension — creates full list in memory\nnums_list = [x**2 for x in range(1000000)]  # Uses lots of RAM!\n\n# Generator expression — lazy, one at a time\nnums_gen = (x**2 for x in range(1000000))   # Almost no RAM!\n\n# Use generators with:\nsum(x**2 for x in range(100))     # Sum\nmax(x**2 for x in range(100))     # Max\nany(x > 50 for x in scores)       # Any match?\nall(x > 0 for x in scores)        # All match?\n```",
    "instructions": "## Task: Memory Efficient Processing\n1. Compare list comp vs generator for sum, any, all\n2. Use generators with sum(), any(), all(), max()\n3. Print results and explain when to use each",
    "starterCode": "import sys\n\n# Compare memory\nlist_comp = [x**2 for x in range(10000)]\ngen_expr = (x**2 for x in range(10000))\n\nprint(f'List size: {sys.getsizeof(list_comp):,} bytes')\nprint(f'Generator size: {sys.getsizeof(gen_expr):,} bytes')\n\n# Efficient aggregations with generators\nscores = [72, 85, 90, 68, 95, 82, 77, 91, 88, 73, 45, 98]\n\ntotal = sum(s for s in scores)\naverage = total / ___(scores)\npassing = sum(1 for s in scores if s >= ___)\nall_pass = all(s >= ___ for s in scores)\nany_perfect = any(s == ___ for s in scores)\nhighest = max(s for s in ___)\n\nprint(f'\\nTotal: {total}')\nprint(f'Average: {average:.1f}')\nprint(f'Passing (>=70): {passing}/{len(scores)}')\nprint(f'All passing: {all_pass}')\nprint(f'Any perfect (100): {any_perfect}')\nprint(f'Highest: {highest}')",
    "solution": "import sys\nlist_comp=[x**2 for x in range(10000)]\ngen_expr=(x**2 for x in range(10000))\nprint(f'List size: {sys.getsizeof(list_comp):,} bytes')\nprint(f'Generator size: {sys.getsizeof(gen_expr):,} bytes')\nscores=[72,85,90,68,95,82,77,91,88,73,45,98]\ntotal=sum(s for s in scores)\naverage=total/len(scores)\npassing=sum(1 for s in scores if s>=70)\nall_pass=all(s>=70 for s in scores)\nany_perfect=any(s==100 for s in scores)\nhighest=max(s for s in scores)\nprint(f'\\nTotal: {total}')\nprint(f'Average: {average:.1f}')\nprint(f'Passing (>=70): {passing}/{len(scores)}')\nprint(f'All passing: {all_pass}')\nprint(f'Any perfect (100): {any_perfect}')\nprint(f'Highest: {highest}')",
    "hint": "len(scores) for count. >= 70 for passing. == 100 for perfect. Generator uses () not [].",
    "rubric": "Memory comparison shown. sum() with generator. all() and any() used. Correct thresholds."
  },
  {
    "title": "Set & Dict Comprehensions",
    "theory": "## Set & Dict Comprehensions\n```python\n# Set comprehension (unique values)\nunique_lengths = {len(word) for word in ['hello', 'world', 'hi']}\n# {2, 5}\n\n# Dict comprehension\nsquares = {x: x**2 for x in range(5)}\n# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}\n\n# Filtering\npassing = {name: score for name, score in grades.items() if score >= 70}\n```",
    "instructions": "## Task: Data Transformation Pipeline\n1. Given raw student data, use set comp to find unique courses\n2. Use dict comp to create a grade lookup\n3. Use dict comp to group students by course\n4. Chain comprehensions for a final report",
    "starterCode": "students = [\n    {'name': 'Ada', 'course': 'Python', 'score': 92},\n    {'name': 'Tunde', 'course': 'SQL', 'score': 78},\n    {'name': 'Ngozi', 'course': 'Python', 'score': 85},\n    {'name': 'Kemi', 'course': 'AI', 'score': 95},\n    {'name': 'Bayo', 'course': 'SQL', 'score': 70},\n]\n\n# Unique courses (set comprehension)\nunique_courses = {s['___'] for s in students}\nprint(f'Courses: {unique_courses}')\n\n# Grade lookup (dict comprehension)\ngrades = {s['name']: 'A' if s['score']>=90 else 'B' if s['score']>=80 else 'C'\n          for s in ___}\nprint(f'Grades: {grades}')\n\n# Top scorers only (filtered dict comp)\nhonors = {s['name']: s['score'] for s in students if s['score'] >= ___}\nprint(f'Honors (90+): {honors}')\n\n# Count per course\nfrom collections import Counter\ncourse_counts = Counter(s['___'] for s in students)\nprint(f'Per course: {dict(course_counts)}')",
    "solution": "students=[{'name':'Ada','course':'Python','score':92},{'name':'Tunde','course':'SQL','score':78},{'name':'Ngozi','course':'Python','score':85},{'name':'Kemi','course':'AI','score':95},{'name':'Bayo','course':'SQL','score':70}]\nunique_courses={s['course'] for s in students}\nprint(f'Courses: {unique_courses}')\ngrades={s['name']:'A' if s['score']>=90 else 'B' if s['score']>=80 else 'C' for s in students}\nprint(f'Grades: {grades}')\nhonors={s['name']:s['score'] for s in students if s['score']>=90}\nprint(f'Honors (90+): {honors}')\nfrom collections import Counter\ncourse_counts=Counter(s['course'] for s in students)\nprint(f'Per course: {dict(course_counts)}')",
    "hint": "s['course'] for set comp. students for dict comp source. >= 90 for honors. Counter for counting.",
    "rubric": "Set comprehension for unique. Dict comp with ternary grades. Filtered dict comp. Counter used."
  }
],

"Django Web Framework": [
  {
    "title": "Django Models & ORM",
    "theory": "## Django Models\n```python\nfrom django.db import models\n\nclass Student(models.Model):\n    name = models.CharField(max_length=100)\n    score = models.IntegerField(default=0)\n    created_at = models.DateTimeField(auto_now_add=True)\n\n# ORM queries\nStudent.objects.create(name=\"Ada\", score=95)\nStudent.objects.filter(score__gte=90)\n```",
    "instructions": "## Task: Define Course Model\n1. Define a `Course` model with title (char), level (char), max_students (int).\n2. Write a mock query to filter courses with max_students >= 20",
    "starterCode": "class models:\n    class Model: pass\n    class CharField: pass\n    class IntegerField: pass\n\n# Mock Django Model\nclass Course(models.___):\n    title = models.___(max_length=200)\n    level = models.CharField(max_length=50, default='Beginner')\n    max_students = models.___()\n\nprint(\"Model Defined!\")\nprint(\"Query: Course.objects.filter(max_students__gte=20)\")",
    "solution": "class models:\n    class Model: pass\n    class CharField: pass\n    class IntegerField: pass\nclass Course(models.Model):\n    title=models.CharField(max_length=200)\n    level=models.CharField(max_length=50,default='Beginner')\n    max_students=models.IntegerField()\nprint(\"Model Defined!\")\nprint(\"Query: Course.objects.filter(max_students__gte=20)\")",
    "hint": "Inherit from models.Model. Use CharField and IntegerField.",
    "rubric": "Model inherits correctly. Fields defined. Mock query printed."
  },
  {
    "title": "Django Views & Routing",
    "theory": "## Views & URLs\n```python\nfrom django.http import HttpResponse\nfrom django.urls import path\n\ndef home(request):\n    return HttpResponse(\"Welcome to Mabel Academy\")\n\nurlpatterns = [\n    path('home/', home),\n]\n```",
    "instructions": "## Task: Simple View\n1. Write a view function `course_list(request)`\n2. It should return an HttpResponse with \"List of courses\"\n3. Define a `urlpatterns` list mapping '/courses' to the view",
    "starterCode": "class HttpResponse:\n    def __init__(self, text): self.text = text\n    def __repr__(self): return f\"HttpResponse: {self.text}\"\n\ndef path(route, view):\n    return f\"Route {route} -> {view.__name__}\"\n\n# Define the view\ndef course_list(request):\n    return ___(\"List of courses\")\n\n# Define urls\nurlpatterns = [\n    ___('/courses', ___)\n]\n\nprint(course_list({}))\nprint(urlpatterns)",
    "solution": "class HttpResponse:\n    def __init__(self,text):self.text=text\n    def __repr__(self):return f\"HttpResponse: {self.text}\"\ndef path(route,view):return f\"Route {route} -> {view.__name__}\"\ndef course_list(request):return HttpResponse(\"List of courses\")\nurlpatterns=[path('/courses',course_list)]\nprint(course_list({}))\nprint(urlpatterns)",
    "hint": "Return HttpResponse. path() takes route string and view function.",
    "rubric": "View returns HttpResponse. urlpatterns defined correctly."
  },
  {
    "title": "Django Templates",
    "theory": "## Django Templates\n```html\n<h1>{{ course.title }}</h1>\n<ul>\n{% for student in students %}\n    <li>{{ student.name }}</li>\n{% endfor %}\n</ul>\n```",
    "instructions": "## Task: Render Template\n1. Write a simulated template rendering engine\n2. Replace {{ variable }} with context values\n3. Render a simple course title",
    "starterCode": "def render_template(template, context):\n    for key, val in context.items():\n        template = template.replace(f'{{{{ {key} }}}}', str(val))\n    return template\n\ntpl = \"\"\"\n<html>\n  <h1>{{ title }}</h1>\n  <p>Level: {{ level }}</p>\n</html>\n\"\"\"\n\ncontext = {'___': 'Python Mastery', '___': 'Advanced'}\n\nhtml = render_template(tpl, context)\nprint(html)",
    "solution": "def render_template(template,context):\n    for key,val in context.items():\n        template=template.replace(f'{{{{ {key} }}}}',str(val))\n    return template\ntpl=\"\"\"\n<html>\n  <h1>{{ title }}</h1>\n  <p>Level: {{ level }}</p>\n</html>\n\"\"\"\ncontext={'title':'Python Mastery','level':'Advanced'}\nhtml=render_template(tpl,context)\nprint(html)",
    "hint": "Context keys must match the template variables exactly: 'title' and 'level'.",
    "rubric": "Context keys defined. Template renders correctly."
  }
],

"React Fundamentals": [
  {
    "title": "Components & JSX",
    "theory": "## React JSX\nJSX allows writing HTML-like syntax inside JavaScript.\n```jsx\nfunction Welcome(props) {\n  return <h1>Hello, {props.name}</h1>;\n}\n```",
    "instructions": "## Task: Build a React Component String\nWrite the JSX string for a `CourseCard` component that accepts a `title` prop.",
    "starterCode": "const jsx = `\nfunction CourseCard(___) {\n  return (\n    <div className=\"card\">\n      <h2>{props.___}</h2>\n    </div>\n  );\n}\n`;\nconsole.log(jsx);",
    "solution": "const jsx = `\nfunction CourseCard(props) {\n  return (\n    <div className=\"card\">\n      <h2>{props.title}</h2>\n    </div>\n  );\n}\n`;\nconsole.log(jsx);",
    "hint": "Pass props to the function. Access the property with props.title.",
    "rubric": "JSX written correctly with props.title."
  },
  {
    "title": "State & useState Hook",
    "theory": "## useState\nReact state allows components to keep track of dynamic data.\n```jsx\nimport { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return <button onClick={() => setCount(count + 1)}>{count}</button>;\n}\n```",
    "instructions": "## Task: State Simulator\nSimulate React's useState logic in JavaScript using a closure.",
    "starterCode": "function useState(initialValue) {\n  let state = initialValue;\n  function setState(newValue) {\n    state = ___;\n    console.log('State updated to:', state);\n  }\n  return [state, ___];\n}\n\nconst [count, setCount] = useState(0);\nsetCount(1);\nsetCount(2);",
    "solution": "function useState(initialValue) {\n  let state = initialValue;\n  function setState(newValue) {\n    state = newValue;\n    console.log('State updated to:', state);\n  }\n  return [state, setState];\n}\nconst [count, setCount] = useState(0);\nsetCount(1);\nsetCount(2);",
    "hint": "Assign newValue to state. Return state and setState function.",
    "rubric": "useState implementation works. Output logs state changes."
  },
  {
    "title": "Props & Data Flow",
    "theory": "## Props\nData flows downwards from parent to child via props.\n```jsx\nfunction Parent() {\n  return <Child message=\"Hello\" />;\n}\nfunction Child(props) {\n  return <p>{props.message}</p>;\n}\n```",
    "instructions": "## Task: Parent-Child Simulation\nSimulate rendering a parent component that passes data to a child component.",
    "starterCode": "function Child(props) {\n  return `<p>${props.___}</p>`;\n}\n\nfunction Parent() {\n  const data = \"React is awesome!\";\n  return `<div>${Child({ ___: data })}</div>`;\n}\n\nconsole.log(Parent());",
    "solution": "function Child(props) {\n  return `<p>${props.message}</p>`;\n}\nfunction Parent() {\n  const data = \"React is awesome!\";\n  return `<div>${Child({ message: data })}</div>`;\n}\nconsole.log(Parent());",
    "hint": "Pass an object to Child with the key matching what it expects.",
    "rubric": "Child invoked with props. Message rendered."
  }
],

"Pandas & NumPy Basics": [
  {
    "title": "NumPy Arrays",
    "theory": "## NumPy\n```python\nimport numpy as np\narr = np.array([1, 2, 3, 4, 5])\nprint(arr * 2) # [2 4 6 8 10] - Vectorized math!\n```",
    "instructions": "## Task: Array Math\n1. Create a NumPy array from 1 to 5.\n2. Multiply it by 10 and print.",
    "starterCode": "import numpy as np\narr = np.array([___])\nresult = arr * ___\nprint(result)",
    "solution": "import numpy as np\narr = np.array([1, 2, 3, 4, 5])\nresult = arr * 10\nprint(result)",
    "hint": "Create array [1, 2, 3, 4, 5]. Multiply by 10.",
    "rubric": "NumPy array created. Vectorized multiplication used."
  },
  {
    "title": "Pandas DataFrames",
    "theory": "## DataFrames\n```python\nimport pandas as pd\ndf = pd.DataFrame({'Name': ['Ada', 'Obi'], 'Score': [90, 80]})\nprint(df.head())\n```",
    "instructions": "## Task: Create a DataFrame\n1. Create a dictionary with student names and scores.\n2. Convert to a Pandas DataFrame.",
    "starterCode": "import pandas as pd\ndata = {'Name': ['Ada', 'Mabel'], 'Score': [95, 99]}\ndf = pd.___(___)\nprint(df)",
    "solution": "import pandas as pd\ndata = {'Name': ['Ada', 'Mabel'], 'Score': [95, 99]}\ndf = pd.DataFrame(data)\nprint(df)",
    "hint": "Use pd.DataFrame(data).",
    "rubric": "DataFrame created from dict."
  },
  {
    "title": "Filtering & Selecting Data",
    "theory": "## Filtering\n```python\nhigh_scores = df[df['Score'] > 85]\n```",
    "instructions": "## Task: Filter Students\n1. Filter the DataFrame to show only students with Score > 90.",
    "starterCode": "import pandas as pd\ndata = {'Name': ['Ada', 'Obi', 'Mabel'], 'Score': [95, 80, 99]}\ndf = pd.DataFrame(data)\nhigh_scores = df[___['Score'] > ___]\nprint(high_scores)",
    "solution": "import pandas as pd\ndata = {'Name': ['Ada', 'Obi', 'Mabel'], 'Score': [95, 80, 99]}\ndf = pd.DataFrame(data)\nhigh_scores = df[df['Score'] > 90]\nprint(high_scores)",
    "hint": "Use df[df['col'] > val].",
    "rubric": "Dataframe filtered correctly based on condition."
  }
],

"CSS Styling & Layout": [
  {
    "title": "CSS Selectors",
    "theory": "## CSS Selectors\n```css\n/* Element */\np { color: red; }\n/* Class */\n.highlight { background: yellow; }\n/* ID */\n#main { padding: 10px; }\n```",
    "instructions": "## Task: Write Selectors\nWrite CSS selectors for a class `card` and an ID `header`.",
    "starterCode": "const css = `\n___ {\n  border: 1px solid black;\n}\n___ {\n  font-size: 24px;\n}\n`;\nconsole.log(css);",
    "solution": "const css = `\n.card {\n  border: 1px solid black;\n}\n#header {\n  font-size: 24px;\n}\n`;\nconsole.log(css);",
    "hint": "Use . for class and # for ID.",
    "rubric": ".card and #header selectors used."
  },
  {
    "title": "Flexbox Basics",
    "theory": "## Flexbox\n```css\n.container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n```",
    "instructions": "## Task: Center Content\nUse flexbox properties to center content both horizontally and vertically.",
    "starterCode": "const css = `\n.box {\n  display: ___;\n  ___: center;\n  ___: center;\n}\n`;\nconsole.log(css);",
    "solution": "const css = `\n.box {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n`;\nconsole.log(css);",
    "hint": "justify-content and align-items center.",
    "rubric": "Flexbox used for centering."
  },
  {
    "title": "CSS Grid",
    "theory": "## CSS Grid\n```css\n.grid {\n  display: grid;\n  grid-template-columns: 1fr 1fr;\n}\n```",
    "instructions": "## Task: Create a Grid\nCreate a 3-column grid layout.",
    "starterCode": "const css = `\n.grid-container {\n  display: ___;\n  grid-template-columns: ___ ___ ___;\n}\n`;\nconsole.log(css);",
    "solution": "const css = `\n.grid-container {\n  display: grid;\n  grid-template-columns: 1fr 1fr 1fr;\n}\n`;\nconsole.log(css);",
    "hint": "display: grid. 1fr 1fr 1fr creates 3 equal columns.",
    "rubric": "Grid layout created with 3 columns."
  }
]

}

def inject_lessons_safe(filepath, new_lessons):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only inject into courseManifest section!
    manifest_start = content.find('courseManifest')
    if manifest_start == -1:
        print("ERROR: courseManifest not found!")
        return

    injected = 0
    skipped = 0

    for course_name, lessons in new_lessons.items():
        # Search for exactly `"CourseName":` after manifest start
        course_pos = content.find(f'"{course_name}":', manifest_start)
        if course_pos == -1:
            print(f'  SKIP: "{course_name}" not found in manifest')
            skipped += 1
            continue
        
        # Now find its lessons array
        lessons_key = content.find('"lessons"', course_pos)
        if lessons_key == -1:
            print(f'  SKIP: No "lessons" array for "{course_name}"')
            skipped += 1
            continue
            
        bracket_start = content.find('[', lessons_key)
        if bracket_start == -1:
            skipped += 1
            continue
            
        depth = 0
        bracket_end = -1
        for i in range(bracket_start, min(bracket_start + 100000, len(content))):
            if content[i] == '[': depth += 1
            elif content[i] == ']':
                depth -= 1
                if depth == 0:
                    bracket_end = i
                    break
                    
        if bracket_end == -1:
            print(f'  SKIP: No closing bracket for "{course_name}"')
            skipped += 1
            continue

        # Check if we already added these lessons (rudimentary check on first title)
        first_title = f'"title": "{lessons[0]["title"]}"'
        if content[bracket_start:bracket_end].find(first_title) != -1:
            print(f'  SKIP: "{course_name}" already has these new lessons!')
            skipped += 1
            continue

        # Format new lessons
        new_entries = ''
        for lesson in lessons:
            new_entries += ',\\n      ' + json.dumps(lesson, ensure_ascii=False)
            
        # Splice them in
        content = content[:bracket_end] + new_entries + '\\n    ' + content[bracket_end:]
        injected += len(lessons)
        print(f'  OK: Added {len(lessons)} lessons to "{course_name}"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'\\n=== SUMMARY ===')
    print(f'Injected: {injected} new lessons')

if __name__ == '__main__':
    inject_lessons_safe('frontend/src/data/courses.js', NEW_LESSONS)
