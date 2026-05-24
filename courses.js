// ═══════════════════════════════════════════════════
//  MABEL ACADEMY — courses.js  (Full Expanded Edition)
// ═══════════════════════════════════════════════════

const curriculum = {
  "Python Core": {
    "Beginner":      ["Python Fundamentals", "Control Flow & Loops", "Functions & Scope", "Lists & Tuples", "Dictionaries & Sets"],
    "Intermediate":  ["OOP in Python", "File Handling & Exceptions", "Modules & Packages", "List Comprehensions", "Iterators & Generators"],
    "Advanced":      ["Decorators & Closures", "Concurrency in Python", "Design Patterns", "Metaprogramming", "Memory & Performance"]
  },
  "Frontend": {
    "Beginner":      ["HTML Essentials", "CSS Styling & Layout", "JavaScript Basics", "Forms & Validation", "Responsive Design Basics"],
    "Intermediate":  ["DOM Manipulation", "Fetch API & AJAX", "ES6+ Modern JS", "CSS Animations", "LocalStorage & State"],
    "Advanced":      ["React Fundamentals", "React Hooks & Context", "Performance Optimization", "Testing Frontend Code", "Build Tools & Webpack"]
  },
  "Backend": {
    "Beginner":      ["Intro to Backend", "HTTP & REST Concepts", "Python for Web", "JSON & APIs", "Environment & Setup"],
    "Intermediate":  ["REST APIs with FastAPI", "Authentication & JWT", "Database Integration", "Middleware & Validation", "Background Tasks"],
    "Advanced":      ["Async Python", "Microservices", "API Security & Rate Limiting", "Caching with Redis", "Deployment & Docker"]
  },
  "SQL & Databases": {
    "Beginner":      ["SQL Fundamentals", "Filtering & Sorting", "Joins & Relationships", "Aggregations & Grouping", "Subqueries"],
    "Intermediate":  ["Indexes & Performance", "Stored Procedures", "Transactions & ACID", "Views & CTEs", "PostgreSQL Deep Dive"],
    "Advanced":      ["Query Optimization", "Database Design Patterns", "NoSQL with MongoDB", "ORMs with SQLAlchemy", "Sharding & Replication"]
  },
  "Data Science": {
    "Beginner":      ["Intro to Data Science", "Pandas & NumPy Basics", "Data Cleaning", "Exploratory Data Analysis", "Data Visualization"],
    "Intermediate":  ["Statistical Analysis", "Intro to Machine Learning", "Scikit-Learn Pipelines", "Regression Models", "Classification Models"],
    "Advanced":      ["Feature Engineering", "Ensemble Methods", "Model Evaluation & Tuning", "Time Series Analysis", "Deep Learning Basics"]
  },
  "AI Engineering": {
    "Beginner":      ["AI & ML Concepts", "Python for AI", "Working with APIs", "Prompt Engineering", "AI Use Cases"],
    "Intermediate":  ["LLM Fundamentals", "RAG Pipelines", "LangChain Basics", "Vector Databases", "Fine-tuning Concepts"],
    "Advanced":      ["LangChain & Agents", "Multi-Agent Systems", "LLM Evaluation", "Production AI Systems", "AI Safety & Ethics"]
  }
};

const courseManifest = {

// ━━━━━━━━━━━━━━━━━━━━━━━━━
// PYTHON CORE — BEGINNER
// ━━━━━━━━━━━━━━━━━━━━━━━━━

"Python Fundamentals": {
  aiRubric: "Check variables correctly typed, print statements work, f-strings used.",
  lessons: [
    {
      title: "Variables & Data Types",
      theory: "## Variables\nPython is dynamically typed.\n\n```python\nname = 'Ada'      # str\nage  = 25         # int\nprice = 9.99      # float\nactive = True     # bool\nprint(type(name)) # <class 'str'>\n```",
      instructions: "## Task: Your Profile\n1. Create `name` (string), `age` (int), `height` (float), `is_student` (bool)\n2. Print all four with labels\n3. Print `type(name)`",
      starterCode: "name = ___\nage = ___\nheight = ___\nis_student = ___\n\nprint('Name:', ___)\nprint('Age:', ___)\nprint('Height:', ___)\nprint('Student:', ___)\nprint('Type:', type(___))",
      solution: "name = 'Ada Okonkwo'\nage = 22\nheight = 1.65\nis_student = True\nprint('Name:', name)\nprint('Age:', age)\nprint('Height:', height)\nprint('Student:', is_student)\nprint('Type:', type(name))",
      hint: "Strings need quotes. Integers are whole numbers. Floats have a decimal. Booleans are True or False.",
      rubric: "All 4 variables correctly typed and printed. type() called."
    },
    {
      title: "String Operations",
      theory: "## Strings\n```python\nfull = 'Ada Okonkwo'\nprint(len(full))       # 11\nprint(full.upper())    # ADA OKONKWO\nprint(full[0:3])       # Ada\nprint(f'Hi {full}!')   # Hi Ada Okonkwo!\n```",
      instructions: "## Task: String Manipulation\n1. Create `first_name` and `last_name`\n2. Combine into `full_name`\n3. Print length, uppercase\n4. Print greeting f-string",
      starterCode: "first_name = '___'\nlast_name  = '___'\nfull_name = ___ + ' ' + ___\n\nprint('Length:', ___)\nprint('Upper:', ___)\nprint(f'Hello, {full_name}! Welcome to Mabel Academy.')",
      solution: "first_name = 'Ada'\nlast_name  = 'Okonkwo'\nfull_name = first_name + ' ' + last_name\nprint('Length:', len(full_name))\nprint('Upper:', full_name.upper())\nprint(f'Hello, {full_name}! Welcome to Mabel Academy.')",
      hint: "Use len() for length, .upper() for caps.",
      rubric: "Concatenation correct. len() and upper() used. f-string correct."
    },
    {
      title: "Numbers & Arithmetic",
      theory: "## Operators\n| Op | Meaning |\n|---|---|\n| + | Add |\n| - | Subtract |\n| * | Multiply |\n| / | Divide |\n| // | Floor div |\n| % | Modulo |\n| ** | Power |",
      instructions: "## Task: Invoice Calculator\n1. `price_per_item = 1500`, `quantity = 7`\n2. Calculate subtotal\n3. Apply 7.5% VAT\n4. Print all three rounded to 2 decimal places",
      starterCode: "price_per_item = 1500\nquantity = 7\n\nsubtotal = ___\nvat = ___\ntotal = ___\n\nprint(f'Subtotal: N{subtotal}')\nprint(f'VAT: N{round(___, 2)}')\nprint(f'Total: N{round(___, 2)}')",
      solution: "price_per_item = 1500\nquantity = 7\nsubtotal = price_per_item * quantity\nvat = subtotal * 0.075\ntotal = subtotal + vat\nprint(f'Subtotal: N{subtotal}')\nprint(f'VAT: N{round(vat, 2)}')\nprint(f'Total: N{round(total, 2)}')",
      hint: "VAT = subtotal * 0.075. Total = subtotal + vat. Wrap in round(value, 2).",
      rubric: "Correct multiplication. VAT = 0.075. round() used on both."
    },
    {
      title: "User Input & Type Casting",
      theory: "## Input\n```python\nname  = input('Enter name: ')    # always string\nage   = int(input('Age: '))      # cast to int\nprice = float(input('Price: '))  # cast to float\n```\nCasting: `int()`, `float()`, `str()`, `bool()`",
      instructions: "## Task: Simple Calculator\n1. Take two numbers as input, cast to float\n2. Print sum, difference, product, quotient (rounded to 2dp)",
      starterCode: "a = float(input('Enter first number: '))\nb = float(___)\n\nprint(f'Sum: {a + b}')\nprint(f'Difference: {___}')\nprint(f'Product: {___}')\nprint(f'Quotient: {round(___ / ___, 2)}')",
      solution: "a = float(input('Enter first number: '))\nb = float(input('Enter second number: '))\nprint(f'Sum: {a + b}')\nprint(f'Difference: {a - b}')\nprint(f'Product: {a * b}')\nprint(f'Quotient: {round(a / b, 2)}')",
      hint: "Wrap input() with float(). Use a+b, a-b, a*b, a/b.",
      rubric: "Both inputs cast to float. All 4 operations printed."
    },
    {
      title: "Comments & Code Style",
      theory: "## Good Style\n```python\n# Single-line comment\n\n\"\"\"\nDocstring / multi-line comment\n\"\"\"\n\n# snake_case for variables\nstudent_name = 'Ada'\n\n# UPPER_CASE for constants\nMAX_SCORE = 100\n```\nPEP 8 is the Python style guide.",
      instructions: "## Task: Clean Up & Document\nRewrite this messy code properly:\n```python\nx='ada'\ny=22\nZ=True\nprint(x,y,Z)\n```\n1. Use snake_case names\n2. Add a docstring at the top\n3. Add inline comments\n4. Use an f-string",
      starterCode: '"""\nPurpose: ___\nAuthor: ___\n"""\n\n# Student information\nstudent_name = "___"  # full name\nstudent_age = ___     # age in years\nis_enrolled = ___     # enrollment status\n\nprint(f"___ | Age: {___} | Enrolled: {___}")',
      solution: '"""\nPurpose: Display student profile\nAuthor: Mabel Academy\n"""\n\nstudent_name = "Ada Okonkwo"  # full name\nstudent_age = 22              # age in years\nis_enrolled = True            # enrollment status\n\nprint(f"{student_name} | Age: {student_age} | Enrolled: {is_enrolled}")',
      hint: "Docstring uses triple quotes at the very top. snake_case joins words with underscores.",
      rubric: "Docstring present. snake_case used. Comments added. f-string output correct."
    }
  ]
},

"Control Flow & Loops": {
  aiRubric: "Check if/elif/else syntax, correct indentation, loop ranges, break/continue.",
  lessons: [
    {
      title: "If / Elif / Else",
      theory: "## Conditionals\n```python\nscore = 75\nif score >= 70:\n    print('Pass')\nelif score >= 50:\n    print('Average')\nelse:\n    print('Fail')\n```\nComparison: ==, !=, >, <, >=, <=\nLogical: and, or, not",
      instructions: "## Task: Grade Calculator\nAssign letter grades:\n- 90-100 → A\n- 80-89 → B\n- 70-79 → C\n- 60-69 → D\n- Below 60 → F\n\nPrint: `Score: 85 → Grade: B`",
      starterCode: "score = 85\n\nif ___:\n    grade = 'A'\nelif ___:\n    grade = 'B'\nelif ___:\n    grade = 'C'\nelif ___:\n    grade = 'D'\nelse:\n    grade = 'F'\n\nprint(f'Score: {score} -> Grade: {grade}')",
      solution: "score = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelif score >= 70:\n    grade = 'C'\nelif score >= 60:\n    grade = 'D'\nelse:\n    grade = 'F'\nprint(f'Score: {score} -> Grade: {grade}')",
      hint: "Start from highest boundary and work down with >=.",
      rubric: "5 branches. Boundaries at 90,80,70,60. Correct output."
    },
    {
      title: "For Loops",
      theory: "## For Loops\n```python\nfor i in range(1, 6):  # 1,2,3,4,5\n    print(i)\n\nfor i, item in enumerate(['a','b','c']):\n    print(i, item)\n```",
      instructions: "## Task: Multiplication Table\nPrint the 7 times table from 1 to 12.",
      starterCode: "for i in range(___, ___):\n    result = ___\n    print(f'7 x {i} = {result}')",
      solution: "for i in range(1, 13):\n    result = 7 * i\n    print(f'7 x {i} = {result}')",
      hint: "range(1, 13) gives 1 to 12. result = 7 * i.",
      rubric: "range(1,13). result = 7*i. Format correct."
    },
    {
      title: "While Loops",
      theory: "## While\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1  # must increment!\n```",
      instructions: "## Task: Countdown\nCount down from 10 to 1, then print 'Liftoff!'",
      starterCode: "countdown = 10\nwhile ___ > ___:\n    print(countdown)\n    countdown ___\nprint('Liftoff!')",
      solution: "countdown = 10\nwhile countdown > 0:\n    print(countdown)\n    countdown -= 1\nprint('Liftoff!')",
      hint: "Condition is countdown > 0. Decrement with -= 1.",
      rubric: "Condition > 0. countdown -= 1. Liftoff after loop."
    },
    {
      title: "Break & Continue",
      theory: "## Loop Control\n- `break` — exit loop\n- `continue` — skip iteration\n\n```python\nfor i in range(10):\n    if i == 3: continue\n    if i == 7: break\n    print(i)\n```",
      instructions: "## Task: First Even > 10\nLoop 1-30. Skip odd numbers with continue. When you find the first even > 10, print it and break.",
      starterCode: "for n in range(1, 31):\n    if n % 2 != 0:\n        ___\n    if n > ___:\n        print(f'First even > 10: {n}')\n        ___",
      solution: "for n in range(1, 31):\n    if n % 2 != 0:\n        continue\n    if n > 10:\n        print(f'First even > 10: {n}')\n        break",
      hint: "n % 2 != 0 means odd. continue skips. break exits.",
      rubric: "continue for odds. break after first even > 10. Output is 12."
    },
    {
      title: "Nested Loops",
      theory: "## Nested Loops\n```python\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(f'{i}x{j}={i*j}', end=' ')\n    print()\n```\nInner loop runs fully for each outer iteration.",
      instructions: "## Task: 5x5 Multiplication Grid\nPrint a 5x5 grid. Use `end='\\t'` to tab-separate values.",
      starterCode: "for i in range(1, ___):\n    for j in range(1, ___):\n        print(___ * ___, end='\\t')\n    print()",
      solution: "for i in range(1, 6):\n    for j in range(1, 6):\n        print(i * j, end='\\t')\n    print()",
      hint: "Both ranges (1, 6). Multiply i*j. end='\\t' for spacing. print() resets line.",
      rubric: "Both ranges correct. i*j. end='\\t'. print() for newline."
    }
  ]
},

"Functions & Scope": {
  aiRubric: "Check def, parameters, return statement, correct calls.",
  lessons: [
    {
      title: "Defining Functions",
      theory: "## Functions\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Ada'))  # Hello, Ada!\n```",
      instructions: "## Task: Temperature Converter\nWrite `celsius_to_fahrenheit(c)`. Formula: F = (C x 9/5) + 32\nTest with 0, 100, 37.",
      starterCode: "def celsius_to_fahrenheit(c):\n    f = ___\n    return ___\n\nprint(celsius_to_fahrenheit(0))    # 32.0\nprint(celsius_to_fahrenheit(100))  # 212.0\nprint(celsius_to_fahrenheit(37))   # 98.6",
      solution: "def celsius_to_fahrenheit(c):\n    f = (c * 9/5) + 32\n    return f\nprint(celsius_to_fahrenheit(0))\nprint(celsius_to_fahrenheit(100))\nprint(celsius_to_fahrenheit(37))",
      hint: "(c * 9/5) + 32. Store in f and return it.",
      rubric: "Correct formula. return present. 3 test calls."
    },
    {
      title: "Default & Keyword Arguments",
      theory: "## Defaults\n```python\ndef greet(name, greeting='Hello'):\n    return f'{greeting}, {name}!'\n\ngreet('Ada')              # Hello, Ada!\ngreet('Ada', 'Good day') # Good day, Ada!\n```",
      instructions: "## Task: Receipt Generator\nCreate `create_receipt(item, price, quantity=1, currency='NGN')`\nReturn: `Receipt: 3x Jollof Rice = NGN 4500`",
      starterCode: "def create_receipt(item, price, quantity=___, currency=___):\n    total = ___\n    return f'Receipt: {quantity}x {item} = {currency} {total}'\n\nprint(create_receipt('Suya', 800))\nprint(create_receipt('Rice', 1500, quantity=3))\nprint(create_receipt('Coffee', 2000, currency='USD'))",
      solution: "def create_receipt(item, price, quantity=1, currency='NGN'):\n    total = price * quantity\n    return f'Receipt: {quantity}x {item} = {currency} {total}'\nprint(create_receipt('Suya', 800))\nprint(create_receipt('Rice', 1500, quantity=3))\nprint(create_receipt('Coffee', 2000, currency='USD'))",
      hint: "Default quantity=1, currency='NGN'. total = price * quantity.",
      rubric: "Correct defaults. total computed. Format matches."
    },
    {
      title: "Multiple Return Values",
      theory: "## Returning Multiple Values\n```python\ndef min_max(nums):\n    return min(nums), max(nums)\n\nlo, hi = min_max([3,1,9])\nprint(lo, hi)  # 1 9\n```",
      instructions: "## Task: Score Statistics\nWrite `score_stats(scores)` returning mean, highest, lowest, pass_count (>=60).\nUnpack and print all four.",
      starterCode: "def score_stats(scores):\n    mean = sum(scores) / len(scores)\n    highest = ___\n    lowest = ___\n    passes = len([s for s in scores if s >= ___])\n    return ___, ___, ___, ___\n\nscores = [78, 92, 45, 88, 60, 34, 75]\nmean, high, low, passes = score_stats(scores)\nprint(f'Mean:{mean:.1f} High:{high} Low:{low} Passes:{passes}')",
      solution: "def score_stats(scores):\n    mean = sum(scores) / len(scores)\n    highest = max(scores)\n    lowest = min(scores)\n    passes = len([s for s in scores if s >= 60])\n    return mean, highest, lowest, passes\n\nscores = [78,92,45,88,60,34,75]\nmean, high, low, passes = score_stats(scores)\nprint(f'Mean:{mean:.1f} High:{high} Low:{low} Passes:{passes}')",
      hint: "max(), min(). List comprehension for passes. Return 4 values comma-separated.",
      rubric: "max/min used. Comprehension correct. 4 values returned and unpacked."
    },
    {
      title: "Scope: Local vs Global",
      theory: "## Scope\n```python\nx = 10  # global\n\ndef change():\n    x = 99  # local only\n    print(x)  # 99\n\nchange()\nprint(x)  # still 10\n```\nUse `global` keyword to modify globals.",
      instructions: "## Task: Counter with Global\n1. `counter = 0`\n2. `increment()` — adds 1 using global\n3. `reset()` — sets to 0\n4. Call increment 5 times, print, reset, print again",
      starterCode: "counter = 0\n\ndef increment():\n    global ___\n    counter ___\n\ndef reset():\n    global ___\n    counter = ___\n\nfor _ in range(5):\n    ___\n\nprint(f'After 5: {counter}')\n___\nprint(f'After reset: {counter}')",
      solution: "counter = 0\n\ndef increment():\n    global counter\n    counter += 1\n\ndef reset():\n    global counter\n    counter = 0\n\nfor _ in range(5):\n    increment()\n\nprint(f'After 5: {counter}')\nreset()\nprint(f'After reset: {counter}')",
      hint: "'global counter' inside both functions. += 1 to increment. = 0 to reset.",
      rubric: "global keyword in both. += 1 correct. reset to 0. Both prints correct."
    },
    {
      title: "Lambda Functions",
      theory: "## Lambda\n```python\nsquare = lambda x: x ** 2\nprint(square(5))  # 25\n\n# With sorted/filter/map\nnums = [3,1,4,1,5]\nsorted_desc = sorted(nums, key=lambda x: -x)\n```",
      instructions: "## Task: Sort Students by Score\n`students = [(name, score), ...]`\n1. Sort by score descending using lambda\n2. Filter passing students (>=60) with filter()",
      starterCode: "students = [('Ada',88),('Tunde',55),('Ngozi',92),('Emeka',67),('Amaka',45)]\n\nranked = sorted(students, key=lambda s: ___, reverse=___)\n\nprint('Rankings:')\nfor i, (name, score) in enumerate(ranked, 1):\n    print(f'{i}. {name}: {score}')\n\npassed = list(filter(lambda s: ___ >= 60, students))\nprint(f'Passed: {[s[0] for s in passed]}')",
      solution: "students = [('Ada',88),('Tunde',55),('Ngozi',92),('Emeka',67),('Amaka',45)]\n\nranked = sorted(students, key=lambda s: s[1], reverse=True)\nprint('Rankings:')\nfor i, (name, score) in enumerate(ranked, 1):\n    print(f'{i}. {name}: {score}')\n\npassed = list(filter(lambda s: s[1] >= 60, students))\nprint(f'Passed: {[s[0] for s in passed]}')",
      hint: "s[1] is the score. reverse=True for descending. filter: s[1] >= 60.",
      rubric: "Lambda accesses s[1]. reverse=True. filter lambda correct."
    }
  ]
},

"Lists & Tuples": {
  aiRubric: "Check list creation, indexing, slicing, list methods, tuple immutability.",
  lessons: [
    {
      title: "Creating & Indexing Lists",
      theory: "## Lists\n```python\nfruits = ['mango','banana','pawpaw']\nprint(fruits[0])    # mango\nprint(fruits[-1])   # pawpaw\nprint(fruits[1:3])  # ['banana','pawpaw']\nprint(len(fruits))  # 3\n```",
      instructions: "## Task: Classroom List\n1. Create list of 5 student names\n2. Print first and last\n3. Print students 2-4 using slice\n4. Print total count",
      starterCode: "students = [___, ___, ___, ___, ___]\n\nprint('First:', ___)\nprint('Last:', ___)\nprint('Middle 3:', ___)\nprint('Total:', ___)",
      solution: "students = ['Ada','Tunde','Ngozi','Emeka','Amaka']\nprint('First:', students[0])\nprint('Last:', students[-1])\nprint('Middle 3:', students[1:4])\nprint('Total:', len(students))",
      hint: "[0] is first, [-1] is last. Slice [1:4] gives indices 1,2,3.",
      rubric: "5 items. [0], [-1], [1:4], len() all correct."
    },
    {
      title: "List Methods",
      theory: "## Methods\n```python\nmy = [3,1,4]\nmy.append(9)      # add end\nmy.insert(1, 7)   # insert at index\nmy.remove(4)      # remove value\nmy.sort()         # sort in place\nmy.reverse()      # reverse\nmy.pop()          # remove & return last\n```",
      instructions: "## Task: Shopping Cart\nStart with `cart = ['rice','beans']`\n1. Add 'tomatoes' and 'palm oil'\n2. Insert 'salt' at index 1\n3. Remove 'beans'\n4. Sort alphabetically\n5. Print final cart",
      starterCode: "cart = ['rice', 'beans']\n\ncart.___('tomatoes')\ncart.___('palm oil')\ncart.___(1, 'salt')\ncart.___('beans')\ncart.sort()\n\nprint('Cart:', cart)",
      solution: "cart = ['rice','beans']\ncart.append('tomatoes')\ncart.append('palm oil')\ncart.insert(1, 'salt')\ncart.remove('beans')\ncart.sort()\nprint('Cart:', cart)",
      hint: "append() adds end. insert(idx,val). remove(val) removes first match.",
      rubric: "append twice, insert at 1, remove 'beans', sort. Output correct."
    },
    {
      title: "Tuples",
      theory: "## Tuples — Immutable Lists\n```python\ncoords = (6.5244, 3.3792)\nx, y = coords  # unpacking\n\n# Tuples can be dict keys\nlocations = {(6.5, 3.4): 'Lagos'}\n```\nUse tuples for fixed data.",
      instructions: "## Task: Student Record Tuple\n1. Create `student = (name, age, course, gpa)`\n2. Unpack into 4 variables\n3. Use the tuple as a dict key",
      starterCode: "student = ('Ada Okonkwo', 22, 'Computer Science', 4.5)\n\nname, age, course, gpa = ___\nprint(f'{name} | {course} | GPA: {gpa}')\n\nrecords = {}\nrecords[___] = 'active'\nprint(records)",
      solution: "student = ('Ada Okonkwo', 22, 'Computer Science', 4.5)\nname, age, course, gpa = student\nprint(f'{name} | {course} | GPA: {gpa}')\nrecords = {}\nrecords[student] = 'active'\nprint(records)",
      hint: "Unpack by assigning: name, age, course, gpa = student. Use whole tuple as key.",
      rubric: "Tuple created. Unpacking correct. Tuple as dict key."
    }
  ]
},

"Dictionaries & Sets": {
  aiRubric: "Check dict syntax, .get(), .items(), .keys(), .values(), set operations.",
  lessons: [
    {
      title: "Dictionary Basics",
      theory: "## Dicts\n```python\ns = {'name':'Ada','age':22}\nprint(s['name'])          # Ada\nprint(s.get('grade','N/A')) # safe\ns['gpa'] = 4.5            # add\ndel s['age']              # delete\nfor k,v in s.items():\n    print(k, v)\n```",
      instructions: "## Task: Student Registry\n1. Dict with name, age, course, score\n2. Print name with [] and score with .get()\n3. Add grade key (A if >=80 else B)\n4. Delete score\n5. Loop and print all key-value pairs",
      starterCode: "student = {'name':'___','age':___,'course':'___','score':88}\n\nprint(student[___])\nprint(student.get(___, 'Not graded'))\n\nstudent[___] = 'A' if student['score'] >= 80 else 'B'\ndel student[___]\n\nfor key, value in student.___():\n    print(f'{key}: {value}')",
      solution: "student = {'name':'Ada','age':22,'course':'Python','score':88}\nprint(student['name'])\nprint(student.get('score','Not graded'))\nstudent['grade'] = 'A' if student['score'] >= 80 else 'B'\ndel student['score']\nfor key,value in student.items():\n    print(f'{key}: {value}')",
      hint: ".get(key, default) is safe. .items() for looping. del removes a key.",
      rubric: "[] and .get() used. Grade added. del used. .items() loop correct."
    },
    {
      title: "Sets & Operations",
      theory: "## Sets\n```python\na = {1,2,3,4}\nb = {3,4,5,6}\nprint(a | b)  # union\nprint(a & b)  # intersection\nprint(a - b)  # difference\nprint(a ^ b)  # symmetric diff\n```",
      instructions: "## Task: Enrolment Overlap\nTrack A: {Ada, Tunde, Ngozi, Emeka}\nTrack B: {Ngozi, Emeka, Amaka, Bola}\n\nFind: students in both, all students, only Track A, exactly one track",
      starterCode: "track_a = {'Ada','Tunde','Ngozi','Emeka'}\ntrack_b = {'Ngozi','Emeka','Amaka','Bola'}\n\nboth   = ___ & ___\nall_s  = ___ | ___\nonly_a = ___ - ___\nexcl   = ___ ^ ___\n\nprint(f'Both: {both}')\nprint(f'All: {all_s}')\nprint(f'Only A: {only_a}')\nprint(f'Exclusive: {excl}')",
      solution: "track_a = {'Ada','Tunde','Ngozi','Emeka'}\ntrack_b = {'Ngozi','Emeka','Amaka','Bola'}\nboth   = track_a & track_b\nall_s  = track_a | track_b\nonly_a = track_a - track_b\nexcl   = track_a ^ track_b\nprint(f'Both: {both}')\nprint(f'All: {all_s}')\nprint(f'Only A: {only_a}')\nprint(f'Exclusive: {excl}')",
      hint: "& intersection, | union, - difference, ^ symmetric difference.",
      rubric: "All 4 operations correct. Results printed."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// PYTHON CORE — INTERMEDIATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"OOP in Python": {
  aiRubric: "Check class, __init__, self, methods, inheritance, super().__init__().",
  lessons: [
    {
      title: "Classes & Objects",
      theory: "## Classes\n```python\nclass Student:\n    def __init__(self, name, age):\n        self.name = name\n        self.age  = age\n    def greet(self):\n        return f'Hi I am {self.name}'\n\nada = Student('Ada', 22)\nprint(ada.greet())\n```",
      instructions: "## Task: BankAccount Class\nCreate `BankAccount(owner, balance=0)` with:\n- `deposit(amount)` — adds to balance\n- `withdraw(amount)` — subtracts or prints 'Insufficient funds'\n- `get_balance()` — returns balance",
      starterCode: "class BankAccount:\n    def __init__(self, owner, balance=___):\n        self.owner = ___\n        self.balance = ___\n\n    def deposit(self, amount):\n        self.balance += ___\n        print(f'Deposited N{amount}. Balance: N{self.balance}')\n\n    def withdraw(self, amount):\n        if amount > self.___:\n            print('Insufficient funds')\n        else:\n            self.balance -= ___\n            print(f'Withdrawn N{amount}. Balance: N{self.balance}')\n\n    def get_balance(self):\n        return ___\n\nacc = BankAccount('Ada')\nacc.deposit(5000)\nacc.withdraw(2000)\nacc.withdraw(10000)\nprint(f'Final: N{acc.get_balance()}')",
      solution: "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amount):\n        self.balance += amount\n        print(f'Deposited N{amount}. Balance: N{self.balance}')\n    def withdraw(self, amount):\n        if amount > self.balance:\n            print('Insufficient funds')\n        else:\n            self.balance -= amount\n            print(f'Withdrawn N{amount}. Balance: N{self.balance}')\n    def get_balance(self):\n        return self.balance\n\nacc = BankAccount('Ada')\nacc.deposit(5000)\nacc.withdraw(2000)\nacc.withdraw(10000)\nprint(f'Final: N{acc.get_balance()}')",
      hint: "Use self.balance throughout. Check amount > self.balance before withdrawing.",
      rubric: "__init__ correct. deposit/withdraw modify self.balance. Insufficient check present."
    },
    {
      title: "Inheritance",
      theory: "## Inheritance\n```python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return '...'\n\nclass Dog(Animal):\n    def speak(self):\n        return f'{self.name}: Woof!'\n\nd = Dog('Rex')\nprint(d.speak())\n```",
      instructions: "## Task: Employee Hierarchy\n- Base `Employee(name, salary)` with `get_info()`\n- `Manager(name, salary, team_size)` — overrides `get_info()`\n- `Intern(name, duration)` — salary defaults 50000",
      starterCode: "class Employee:\n    def __init__(self, name, salary):\n        self.name = ___\n        self.salary = ___\n    def get_info(self):\n        return f'{self.name} | N{self.salary}'\n\nclass Manager(___):\n    def __init__(self, name, salary, team_size):\n        super().__init__(___, ___)\n        self.team_size = ___\n    def get_info(self):\n        return super().get_info() + f' | Team: {self.team_size}'\n\nclass Intern(___):\n    def __init__(self, name, duration):\n        super().__init__(name, salary=___)\n        self.duration = ___\n    def get_duration(self):\n        return f'{self.name} interns for {self.duration} months'\n\nprint(Manager('Tunde',500000,8).get_info())\nprint(Intern('Amaka',6).get_info())\nprint(Intern('Amaka',6).get_duration())",
      solution: "class Employee:\n    def __init__(self,name,salary):\n        self.name=name; self.salary=salary\n    def get_info(self):\n        return f'{self.name} | N{self.salary}'\n\nclass Manager(Employee):\n    def __init__(self,name,salary,team_size):\n        super().__init__(name,salary)\n        self.team_size=team_size\n    def get_info(self):\n        return super().get_info()+f' | Team: {self.team_size}'\n\nclass Intern(Employee):\n    def __init__(self,name,duration):\n        super().__init__(name,salary=50000)\n        self.duration=duration\n    def get_duration(self):\n        return f'{self.name} interns for {self.duration} months'\n\nprint(Manager('Tunde',500000,8).get_info())\nprint(Intern('Amaka',6).get_info())\nprint(Intern('Amaka',6).get_duration())",
      hint: "Pass (Employee) in class def. super().__init__() calls parent. Override get_info in Manager.",
      rubric: "Both inherit Employee. super().__init__() used. Manager overrides. Intern defaults salary."
    },
    {
      title: "Dunder Methods",
      theory: "## Magic/Dunder Methods\n```python\nclass Book:\n    def __init__(self, title, pages):\n        self.title = title\n        self.pages = pages\n    def __str__(self):\n        return f'Book: {self.title}'\n    def __len__(self):\n        return self.pages\n    def __repr__(self):\n        return f'Book({self.title!r}, {self.pages})'\n\nb = Book('Python', 300)\nprint(b)      # Book: Python\nprint(len(b)) # 300\n```",
      instructions: "## Task: Vector Class\nCreate a `Vector(x, y)` class with:\n- `__str__` → `Vector(3, 4)`\n- `__add__` → adds two vectors\n- `__len__` → returns magnitude as int (sqrt(x²+y²))\n- `__eq__` → True if x and y are equal",
      starterCode: "import math\n\nclass Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __str__(self):\n        return f'Vector({self.___}, {self.___})'\n    def __add__(self, other):\n        return Vector(self.x + ___.x, self.y + ___.y)\n    def __len__(self):\n        return int(math.sqrt(self.x**2 + ___))\n    def __eq__(self, other):\n        return self.x == ___.x and self.y == ___.y\n\nv1 = Vector(3, 4)\nv2 = Vector(1, 2)\nprint(v1)\nprint(v1 + v2)\nprint(len(v1))   # 5\nprint(v1 == v2)  # False",
      solution: "import math\nclass Vector:\n    def __init__(self,x,y):\n        self.x=x; self.y=y\n    def __str__(self):\n        return f'Vector({self.x}, {self.y})'\n    def __add__(self,other):\n        return Vector(self.x+other.x, self.y+other.y)\n    def __len__(self):\n        return int(math.sqrt(self.x**2+self.y**2))\n    def __eq__(self,other):\n        return self.x==other.x and self.y==other.y\n\nv1=Vector(3,4); v2=Vector(1,2)\nprint(v1)\nprint(v1+v2)\nprint(len(v1))\nprint(v1==v2)",
      hint: "__add__ returns a new Vector. __len__ uses math.sqrt. __eq__ compares both x and y.",
      rubric: "All 4 dunders defined. __add__ returns Vector. __len__ returns int magnitude. __eq__ correct."
    }
  ]
},

"List Comprehensions": {
  aiRubric: "Check [expr for x in iterable if condition] syntax.",
  lessons: [
    {
      title: "Basic Comprehensions",
      theory: "## List Comprehensions\n```python\n# Old way\nsquares = []\nfor x in range(5):\n    squares.append(x**2)\n\n# Comprehension\nsquares = [x**2 for x in range(5)]\n# [0, 1, 4, 9, 16]\n```",
      instructions: "## Task: Three Comprehensions\n1. Squares of 1-10\n2. Even numbers from 1-20\n3. Words longer than 4 chars from a sentence",
      starterCode: "squares = [___ for x in range(1, 11)]\nprint(squares)\n\nevens = [n for n in range(1, 21) if ___ == 0]\nprint(evens)\n\nsentence = 'Mabel Academy teaches backend and frontend development'\nlong_words = [w for w in sentence.split() if len(w) > ___]\nprint(long_words)",
      solution: "squares = [x**2 for x in range(1,11)]\nprint(squares)\nevens = [n for n in range(1,21) if n%2==0]\nprint(evens)\nsentence = 'Mabel Academy teaches backend and frontend development'\nlong_words = [w for w in sentence.split() if len(w)>4]\nprint(long_words)",
      hint: "x**2 for squares. n%2==0 for evens. len(w)>4 for long words.",
      rubric: "All 3 comprehensions correct."
    },
    {
      title: "Dict & Set Comprehensions",
      theory: "## Dict/Set Comprehensions\n```python\n# Dict\ngrades = {name: 'A' if s>=80 else 'B'\n          for name,s in scores.items()}\n\n# Set (unique)\nlengths = {len(w) for w in words}\n```",
      instructions: "## Task: Grade Dictionary\nFrom `[(name, score)]` tuples:\n1. Dict `{name: score}`\n2. Dict `{name: grade}` — A>=80, B>=70, C>=60, F\n3. Set of unique grades",
      starterCode: "data = [('Ada',88),('Tunde',72),('Ngozi',95),('Emeka',55),('Amaka',65)]\n\nscores = {name: score for name, score in ___}\n\ndef get_grade(s):\n    if s>=80: return 'A'\n    elif s>=70: return 'B'\n    elif s>=60: return 'C'\n    else: return 'F'\n\ngrades = {name: get_grade(___) for name, score in data}\nunique = {___ for ___ in grades.values()}\n\nprint(scores)\nprint(grades)\nprint('Grades:', unique)",
      solution: "data=[('Ada',88),('Tunde',72),('Ngozi',95),('Emeka',55),('Amaka',65)]\nscores={name:score for name,score in data}\ndef get_grade(s):\n    if s>=80:return 'A'\n    elif s>=70:return 'B'\n    elif s>=60:return 'C'\n    else:return 'F'\ngrades={name:get_grade(score) for name,score in data}\nunique={g for g in grades.values()}\nprint(scores)\nprint(grades)\nprint('Grades:',unique)",
      hint: "Dict comprehension: {k:v for k,v in data}. Set: {expr for x in iterable}.",
      rubric: "Both dict comprehensions correct. get_grade called. Set from .values()."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// BACKEND
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"REST APIs with FastAPI": {
  aiRubric: "Check decorators, Pydantic models, path/query params, HTTPException.",
  lessons: [
    {
      title: "Your First FastAPI App",
      theory: "## FastAPI\n```python\nfrom fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': 'Hello!'}\n```\nRun: `uvicorn main:app --reload`\nDocs: `http://localhost:8000/docs`",
      instructions: "## Task: Student API\n1. GET / → `{message, version}`\n2. GET /student/{name} → `{student, status}`",
      starterCode: "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {___: 'Mabel Academy API', ___: '1.0'}\n\n@app.get('/student/{___}')\ndef get_student(name: str):\n    return {___: name, ___: 'enrolled'}",
      solution: "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef root():\n    return {'message':'Mabel Academy API','version':'1.0'}\n@app.get('/student/{name}')\ndef get_student(name: str):\n    return {'student':name,'status':'enrolled'}",
      hint: "Path params in {curly braces} in URL and as function params.",
      rubric: "Both endpoints defined. Path param correct. Both return dicts."
    },
    {
      title: "POST with Pydantic",
      theory: "## Request Body\n```python\nfrom pydantic import BaseModel\n\nclass Item(BaseModel):\n    name: str\n    price: float\n    in_stock: bool = True\n\n@app.post('/items/')\ndef create(item: Item):\n    return item\n```",
      instructions: "## Task: Enrollment Endpoint\nCreate `EnrollmentRequest(student_name, course, level='Beginner')`\nPOST /enroll → returns enrolled=True, student, course, welcome message",
      starterCode: "from fastapi import FastAPI\nfrom pydantic import BaseModel\napp = FastAPI()\n\nclass EnrollmentRequest(BaseModel):\n    student_name: ___\n    course: ___\n    level: str = ___\n\n@app.post('/enroll')\ndef enroll(req: ___):\n    return {\n        'enrolled': True,\n        'student': ___,\n        'course': ___,\n        'message': f'Welcome to {req.course}!'\n    }",
      solution: "from fastapi import FastAPI\nfrom pydantic import BaseModel\napp = FastAPI()\nclass EnrollmentRequest(BaseModel):\n    student_name: str\n    course: str\n    level: str = 'Beginner'\n@app.post('/enroll')\ndef enroll(req: EnrollmentRequest):\n    return {'enrolled':True,'student':req.student_name,'course':req.course,'message':f'Welcome to {req.course}!'}",
      hint: "Fields need type hints. Access with req.field_name. Default: level='Beginner'.",
      rubric: "BaseModel used. 3 fields typed. Default level. Fields accessed correctly."
    },
    {
      title: "Query Params & Pagination",
      theory: "## Query Parameters\n```python\n@app.get('/students/')\ndef list_students(skip: int=0, limit: int=10):\n    return students[skip: skip+limit]\n\n# Call: GET /students/?skip=0&limit=5\n```",
      instructions: "## Task: Paginated Courses\n1. In-memory list of 10 courses\n2. GET /courses/ with skip=0, limit=5\n3. GET /courses/search with required `q` param",
      starterCode: "from fastapi import FastAPI, Query\napp = FastAPI()\n\ncourses = ['Python','FastAPI','SQL','React','Docker','ML','AI','Git','Linux','Testing']\n\n@app.get('/courses/')\ndef list_courses(skip: int=___, limit: int=___):\n    return courses[___: ___ + ___]\n\n@app.get('/courses/search')\ndef search(q: str = Query(min_length=___)):\n    results = [c for c in courses if ___.lower() in c.lower()]\n    return {'query':q,'results':results,'count':len(results)}",
      solution: "from fastapi import FastAPI, Query\napp = FastAPI()\ncourses=['Python','FastAPI','SQL','React','Docker','ML','AI','Git','Linux','Testing']\n@app.get('/courses/')\ndef list_courses(skip:int=0,limit:int=5):\n    return courses[skip:skip+limit]\n@app.get('/courses/search')\ndef search(q:str=Query(min_length=2)):\n    results=[c for c in courses if q.lower() in c.lower()]\n    return {'query':q,'results':results,'count':len(results)}",
      hint: "Slice: courses[skip:skip+limit]. Case-insensitive: q.lower() in c.lower().",
      rubric: "Defaults 0 and 5. Slice correct. Search filters. min_length=2."
    },
    {
      title: "HTTP Errors & Status Codes",
      theory: "## HTTPException\n```python\nfrom fastapi import HTTPException\n\n@app.get('/item/{id}')\ndef get(id: int):\n    if id not in db:\n        raise HTTPException(status_code=404, detail='Not found')\n    return db[id]\n```\n200 OK, 201 Created, 400 Bad Request, 404 Not Found",
      instructions: "## Task: CRUD with Errors\n`students = {1:'Ada', 2:'Tunde'}`\n1. GET /students/{id} — 404 if missing\n2. POST /students/ — 400 if ID exists\n3. DELETE /students/{id} — 404 if missing",
      starterCode: "from fastapi import FastAPI, HTTPException\napp = FastAPI()\nstudents = {1:'Ada', 2:'Tunde'}\n\n@app.get('/students/{sid}')\ndef get_student(sid: int):\n    if sid not in ___:\n        raise HTTPException(status_code=___, detail='Not found')\n    return {'id':sid, 'name':students[sid]}\n\n@app.post('/students/', status_code=201)\ndef add_student(sid: int, name: str):\n    if sid in ___:\n        raise HTTPException(status_code=___, detail='ID exists')\n    students[___] = name\n    return {'created': name}\n\n@app.delete('/students/{sid}')\ndef delete_student(sid: int):\n    if sid not in students:\n        raise HTTPException(___=404, ___='Not found')\n    del students[___]\n    return {'deleted': sid}",
      solution: "from fastapi import FastAPI,HTTPException\napp=FastAPI()\nstudents={1:'Ada',2:'Tunde'}\n@app.get('/students/{sid}')\ndef get_student(sid:int):\n    if sid not in students:\n        raise HTTPException(status_code=404,detail='Not found')\n    return {'id':sid,'name':students[sid]}\n@app.post('/students/',status_code=201)\ndef add_student(sid:int,name:str):\n    if sid in students:\n        raise HTTPException(status_code=400,detail='ID exists')\n    students[sid]=name\n    return {'created':name}\n@app.delete('/students/{sid}')\ndef delete_student(sid:int):\n    if sid not in students:\n        raise HTTPException(status_code=404,detail='Not found')\n    del students[sid]\n    return {'deleted':sid}",
      hint: "raise HTTPException(status_code=404). Check 'in students' first.",
      rubric: "404 for missing. 400 for duplicates. All 3 endpoints work."
    },
    {
      title: "Authentication with JWT",
      theory: "## JWT Auth Pattern\n```python\nfrom jose import jwt\n\nSECRET = 'mysecret'\nALGO   = 'HS256'\n\ndef create_token(data: dict):\n    return jwt.encode(data, SECRET, ALGO)\n\ndef decode_token(token: str):\n    return jwt.decode(token, SECRET, [ALGO])\n```\nInstall: `pip install python-jose`",
      instructions: "## Task: Token Auth\n1. `create_token(username)` — returns JWT\n2. `verify_token(token)` — returns username or raises 401\n3. POST /login — returns token\n4. GET /me with `Authorization: Bearer <token>` header — returns username",
      starterCode: "from fastapi import FastAPI, HTTPException, Header\nfrom jose import jwt, JWTError\n\napp = FastAPI()\nSECRET = 'mabel-secret'\nALGO   = 'HS256'\n\ndef create_token(username: str):\n    return jwt.encode({'sub': ___}, SECRET, algorithm=___)\n\ndef verify_token(token: str):\n    try:\n        payload = jwt.decode(___, SECRET, algorithms=[ALGO])\n        return payload[___]\n    except JWTError:\n        raise HTTPException(status_code=___, detail='Invalid token')\n\n@app.post('/login')\ndef login(username: str, password: str):\n    if username == 'ada' and password == 'pass123':\n        return {'token': create_token(___)}\n    raise HTTPException(status_code=401, detail='Wrong credentials')\n\n@app.get('/me')\ndef get_me(authorization: str = Header(...)):\n    token = authorization.replace('Bearer ', '')\n    username = verify_token(___)\n    return {'user': username}",
      solution: "from fastapi import FastAPI,HTTPException,Header\nfrom jose import jwt,JWTError\napp=FastAPI()\nSECRET='mabel-secret'\nALGO='HS256'\ndef create_token(username:str):\n    return jwt.encode({'sub':username},SECRET,algorithm=ALGO)\ndef verify_token(token:str):\n    try:\n        payload=jwt.decode(token,SECRET,algorithms=[ALGO])\n        return payload['sub']\n    except JWTError:\n        raise HTTPException(status_code=401,detail='Invalid token')\n@app.post('/login')\ndef login(username:str,password:str):\n    if username=='ada' and password=='pass123':\n        return {'token':create_token(username)}\n    raise HTTPException(status_code=401,detail='Wrong credentials')\n@app.get('/me')\ndef get_me(authorization:str=Header(...)):\n    token=authorization.replace('Bearer ','')\n    return {'user':verify_token(token)}",
      hint: "jwt.encode({'sub':username}). Decode with jwt.decode(). Extract 'sub' from payload.",
      rubric: "create_token encodes sub. verify_token decodes and returns sub. login and /me endpoints correct."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━
// SQL & DATABASES
// ━━━━━━━━━━━━━━━━━━━━━━━━━

"SQL Fundamentals": {
  aiRubric: "Check valid SQL syntax, SELECT/FROM/WHERE structure.",
  lessons: [
    {
      title: "SELECT & FROM",
      theory: "## Basic SQL\n```sql\nSELECT column1, column2 FROM table;\nSELECT * FROM students;\nSELECT name AS student_name FROM students;\n```",
      instructions: "## Task: Query Students\nAssume `students(id, name, age, course, score)`\n1. Select all students\n2. Select name and course only\n3. Select name AS student_name, score AS exam_score",
      starterCode: "-- 1. All students\n___ * ___ students;\n\n-- 2. Name and course\nSELECT ___, ___ FROM ___;\n\n-- 3. With aliases\nSELECT name ___ student_name, score ___ exam_score FROM ___;",
      solution: "SELECT * FROM students;\n\nSELECT name, course FROM students;\n\nSELECT name AS student_name, score AS exam_score FROM students;",
      hint: "SELECT then columns, FROM then table. AS for aliases.",
      rubric: "All 3 queries correct. AS used."
    },
    {
      title: "WHERE Clause",
      theory: "## Filtering\n```sql\nSELECT * FROM students WHERE score >= 70;\nSELECT * FROM students WHERE name LIKE 'A%';\nSELECT * FROM students WHERE score BETWEEN 60 AND 80;\nSELECT * FROM students WHERE course IN ('Python','SQL');\n```",
      instructions: "## Task: 4 Filter Queries\n1. Score >= 80\n2. Python course AND age < 25\n3. Name starts with 'A'\n4. Score between 60 and 79",
      starterCode: "-- 1.\nSELECT * FROM students WHERE ___ >= ___;\n\n-- 2.\nSELECT * FROM students WHERE course = ___ ___ age < ___;\n\n-- 3.\nSELECT * FROM students WHERE name ___ 'A%';\n\n-- 4.\nSELECT * FROM students WHERE score ___ 60 ___ 79;",
      solution: "SELECT * FROM students WHERE score >= 80;\nSELECT * FROM students WHERE course='Python' AND age<25;\nSELECT * FROM students WHERE name LIKE 'A%';\nSELECT * FROM students WHERE score BETWEEN 60 AND 79;",
      hint: "LIKE 'A%' for pattern. BETWEEN x AND y inclusive.",
      rubric: "All 4 queries correct. LIKE and BETWEEN used."
    },
    {
      title: "ORDER BY & LIMIT",
      theory: "## Sorting\n```sql\nSELECT * FROM students ORDER BY score DESC;\nSELECT * FROM students ORDER BY score DESC LIMIT 3;\nSELECT * FROM students ORDER BY course ASC, score DESC;\n```",
      instructions: "## Task: Rankings\n1. All students by score descending\n2. Top 5 students\n3. By course A-Z, then score highest within each",
      starterCode: "-- 1.\nSELECT * FROM students ORDER BY score ___;\n\n-- 2.\nSELECT * FROM students ORDER BY score DESC ___ 5;\n\n-- 3.\nSELECT * FROM students ORDER BY course ___, score ___;",
      solution: "SELECT * FROM students ORDER BY score DESC;\nSELECT * FROM students ORDER BY score DESC LIMIT 5;\nSELECT * FROM students ORDER BY course ASC, score DESC;",
      hint: "DESC for high-to-low. LIMIT after ORDER BY. Multi-column with comma.",
      rubric: "DESC correct. LIMIT 5. Multi-sort ASC then DESC."
    },
    {
      title: "Aggregations & GROUP BY",
      theory: "## Aggregate Functions\n```sql\nSELECT COUNT(*) FROM students;\nSELECT AVG(score), MAX(score), MIN(score) FROM students;\n\nSELECT course, AVG(score) AS avg_score\nFROM students\nGROUP BY course\nHAVING AVG(score) > 70;\n```",
      instructions: "## Task: Course Statistics\n1. Count of students per course\n2. Average score per course\n3. Courses where average score > 75\n4. Highest and lowest score overall",
      starterCode: "-- 1. Count per course\nSELECT course, ___(*)  AS count\nFROM students\n___ BY course;\n\n-- 2. Average per course\nSELECT course, ___(score) AS avg\nFROM students GROUP BY course;\n\n-- 3. Avg > 75\nSELECT course, AVG(score) AS avg\nFROM students GROUP BY course\n___ AVG(score) > ___;\n\n-- 4. Overall high/low\nSELECT ___(score) AS highest, ___(score) AS lowest\nFROM students;",
      solution: "SELECT course, COUNT(*) AS count FROM students GROUP BY course;\nSELECT course, AVG(score) AS avg FROM students GROUP BY course;\nSELECT course, AVG(score) AS avg FROM students GROUP BY course HAVING AVG(score)>75;\nSELECT MAX(score) AS highest, MIN(score) AS lowest FROM students;",
      hint: "COUNT(*) counts rows. GROUP BY splits into groups. HAVING filters groups (not WHERE).",
      rubric: "COUNT/AVG/MAX/MIN correct. GROUP BY used. HAVING not WHERE for aggregate filter."
    },
    {
      title: "JOINs",
      theory: "## JOIN Types\n```sql\n-- INNER: only matching rows\nSELECT s.name, e.course\nFROM students s\nINNER JOIN enrollments e ON s.id = e.student_id;\n\n-- LEFT: all left + matching right\nSELECT s.name, e.course\nFROM students s\nLEFT JOIN enrollments e ON s.id = e.student_id;\n```",
      instructions: "## Task: Join Queries\nTables: `students(id,name)`, `enrollments(id,student_id,course,grade)`\n1. INNER JOIN — students with their courses\n2. Filter grade = 'A'\n3. LEFT JOIN — all students, even unenrolled",
      starterCode: "-- 1. INNER JOIN\nSELECT s.name, e.course\nFROM students ___\n___ JOIN enrollments e ON s.___ = e.___;\n\n-- 2. With filter\nSELECT s.name, e.course, e.grade\nFROM students s INNER JOIN enrollments e ON s.id=e.student_id\nWHERE e.grade = ___;\n\n-- 3. LEFT JOIN\nSELECT s.name, e.course\nFROM students s\n___ JOIN enrollments e ON s.id = e.student_id;",
      solution: "SELECT s.name, e.course FROM students s INNER JOIN enrollments e ON s.id=e.student_id;\nSELECT s.name,e.course,e.grade FROM students s INNER JOIN enrollments e ON s.id=e.student_id WHERE e.grade='A';\nSELECT s.name,e.course FROM students s LEFT JOIN enrollments e ON s.id=e.student_id;",
      hint: "INNER JOIN returns only matches. LEFT JOIN keeps all left rows. ON specifies join condition.",
      rubric: "INNER JOIN correct. WHERE grade filter. LEFT JOIN used correctly."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━
// DATA SCIENCE
// ━━━━━━━━━━━━━━━━━━━━━━━━━

"Pandas & NumPy Basics": {
  aiRubric: "Check imports, array ops, DataFrame creation, filtering, apply().",
  lessons: [
    {
      title: "NumPy Arrays",
      theory: "## NumPy\n```python\nimport numpy as np\narr = np.array([1,2,3,4,5])\nprint(arr * 2)     # [2,4,6,8,10]\nprint(arr.mean())  # 3.0\nprint(arr.shape)   # (5,)\n```",
      instructions: "## Task: Score Analysis\n`scores = [78,92,65,88,74,91,55,83]`\n1. Convert to NumPy array\n2. Print mean, max, min, std\n3. Count scores > 80\n4. Print sorted descending",
      starterCode: "import numpy as np\nscores=[78,92,65,88,74,91,55,83]\narr = np.array(___)\n\nprint(f'Mean: {___:.1f}')\nprint(f'Max: {___}')\nprint(f'Min: {___}')\nprint(f'Std: {___:.2f}')\n\nabove = arr[arr > ___]\nprint(f'Above 80: {len(above)}')\nprint(np.sort(arr)[::-1])",
      solution: "import numpy as np\nscores=[78,92,65,88,74,91,55,83]\narr=np.array(scores)\nprint(f'Mean:{arr.mean():.1f}')\nprint(f'Max:{arr.max()}')\nprint(f'Min:{arr.min()}')\nprint(f'Std:{arr.std():.2f}')\nabove=arr[arr>80]\nprint(f'Above 80:{len(above)}')\nprint(np.sort(arr)[::-1])",
      hint: "arr.mean(), arr.max(), arr.min(). Boolean index: arr[arr>80]. Sort desc: np.sort(arr)[::-1].",
      rubric: "np.array used. All stats. Boolean index. Descending sort."
    },
    {
      title: "Pandas DataFrames",
      theory: "## Pandas\n```python\nimport pandas as pd\ndf = pd.DataFrame({'name':['Ada'],'score':[88]})\nprint(df.head())\nprint(df.describe())\ndf['grade'] = df['score'].apply(lambda s: 'A' if s>=80 else 'B')\n```",
      instructions: "## Task: Student Report\n5 students (name, course, score)\n1. info()\n2. Average score\n3. Highest scorer\n4. Filter score >= 80\n5. Add grade column (Pass/Fail)",
      starterCode: "import pandas as pd\ndata={'name':['Ada','Tunde','Ngozi','Emeka','Amaka'],'course':['Python','FastAPI','Python','SQL','AI'],'score':[88,72,95,58,81]}\ndf=pd.DataFrame(___)\ndf.info()\n\nprint(f'Average: {df[___].mean():.1f}')\ntop=df.loc[df['score'].idxmax(), ___]\nprint(f'Top: {top}')\n\nhigh=df[df[___]>=80]\nprint(high)\n\ndf['grade']=df['score'].apply(lambda s: ___ if s>=60 else ___)\nprint(df)",
      solution: "import pandas as pd\ndata={'name':['Ada','Tunde','Ngozi','Emeka','Amaka'],'course':['Python','FastAPI','Python','SQL','AI'],'score':[88,72,95,58,81]}\ndf=pd.DataFrame(data)\ndf.info()\nprint(f'Average:{df[\"score\"].mean():.1f}')\ntop=df.loc[df['score'].idxmax(),'name']\nprint(f'Top:{top}')\nhigh=df[df['score']>=80]\nprint(high)\ndf['grade']=df['score'].apply(lambda s:'Pass' if s>=60 else 'Fail')\nprint(df)",
      hint: "df['score'].mean(). idxmax() gets index of max. Boolean filter: df[df['score']>=80].",
      rubric: "DataFrame created. info(). idxmax. Filter. apply lambda."
    },
    {
      title: "Data Cleaning",
      theory: "## Cleaning\n```python\ndf.isnull().sum()          # count NaN\ndf.dropna()                # drop NaN rows\ndf.fillna(0)               # fill NaN\ndf.drop_duplicates()       # remove dupes\ndf['col'].str.strip()      # trim whitespace\ndf['col'].astype(int)      # type conversion\n```",
      instructions: "## Task: Clean a Messy Dataset\nGiven a DataFrame with NaN values, duplicates, and wrong types:\n1. Check and report null counts\n2. Fill missing scores with the mean\n3. Drop duplicate rows\n4. Convert score column to int\n5. Strip whitespace from names",
      starterCode: "import pandas as pd\nimport numpy as np\n\ndata = {\n    'name':  ['Ada ', ' Tunde', 'Ngozi', 'Ada ', 'Emeka'],\n    'score': [88, None, 95, 88, 72]\n}\ndf = pd.DataFrame(data)\n\n# 1. Null counts\nprint(df.___().sum())\n\n# 2. Fill missing score with mean\nmean_score = df['score'].___()  \ndf['score'] = df['score'].fillna(___)\n\n# 3. Drop duplicates\ndf = df.drop_duplicates()\n\n# 4. Convert score to int\ndf['score'] = df['score'].astype(___)\n\n# 5. Strip whitespace\ndf['name'] = df['name'].str.strip()\n\nprint(df)",
      solution: "import pandas as pd, numpy as np\ndata={'name':['Ada ',' Tunde','Ngozi','Ada ','Emeka'],'score':[88,None,95,88,72]}\ndf=pd.DataFrame(data)\nprint(df.isnull().sum())\nmean_score=df['score'].mean()\ndf['score']=df['score'].fillna(mean_score)\ndf=df.drop_duplicates()\ndf['score']=df['score'].astype(int)\ndf['name']=df['name'].str.str.strip()\nprint(df)",
      hint: "isnull().sum() for nulls. fillna(mean). drop_duplicates(). astype(int). str.strip().",
      rubric: "isnull used. fillna with mean. drop_duplicates. astype(int). str.strip on names."
    }
  ]
},

"Intro to Machine Learning": {
  aiRubric: "Check sklearn imports, train_test_split, fit, predict, accuracy_score.",
  lessons: [
    {
      title: "Your First ML Model",
      theory: "## Scikit-Learn\n```python\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\n\nX_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)\nmodel = LogisticRegression()\nmodel.fit(X_train, y_train)\ny_pred = model.predict(X_test)\nprint(accuracy_score(y_test, y_pred))\n```",
      instructions: "## Task: Iris Classifier\n1. Load Iris dataset\n2. Split 80/20\n3. Train LogisticRegression\n4. Print accuracy\n5. Show classification report",
      starterCode: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score, classification_report\n\niris = load_iris()\nX, y = iris.___, iris.___\n\nX_train,X_test,y_train,y_test = train_test_split(\n    X, y, test_size=___, random_state=42)\n\nmodel = LogisticRegression(max_iter=200)\nmodel.___(X_train, y_train)\ny_pred = model.___(X_test)\n\nprint(f'Accuracy: {accuracy_score(y_test,y_pred):.2%}')\nprint(classification_report(y_test, y_pred, target_names=iris.target_names))",
      solution: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score, classification_report\niris=load_iris()\nX,y=iris.data,iris.target\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nmodel=LogisticRegression(max_iter=200)\nmodel.fit(X_train,y_train)\ny_pred=model.predict(X_test)\nprint(f'Accuracy:{accuracy_score(y_test,y_pred):.2%}')\nprint(classification_report(y_test,y_pred,target_names=iris.target_names))",
      hint: "iris.data is X, iris.target is y. test_size=0.2. model.fit() trains, model.predict() predicts.",
      rubric: "data/target loaded. 0.2 split. fit/predict called. accuracy_score and classification_report."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━
// AI ENGINEERING
// ━━━━━━━━━━━━━━━━━━━━━━━━━

"Prompt Engineering": {
  aiRubric: "Check prompt structure: role, context, task, format specified.",
  lessons: [
    {
      title: "Anatomy of a Good Prompt",
      theory: "## Prompt Structure\n1. **Role** — who the AI is\n2. **Context** — background\n3. **Task** — what to do\n4. **Format** — how to respond\n\n```python\nsystem = 'You are a senior Python tutor. Be concise.'\nuser   = 'Explain Python lists in 2 sentences with one code example.'\n```",
      instructions: "## Task: Design 3 Prompts\nWrite system + user prompts for:\n1. A Nigerian cooking assistant\n2. A Python code reviewer\n3. A quiz question generator\n\nFor each: specify role, task, output format.",
      starterCode: "# 1. Cooking Assistant\ncooking_system = 'You are ___, a Nigerian cooking expert. ___'\ncooking_user   = 'Task: ___ Format: ___'\n\n# 2. Code Reviewer  \nreview_system = '___'\nreview_user   = 'Review this code: {code} Format: ___'\n\n# 3. Quiz Generator\nquiz_system = '___'\nquiz_user   = 'Topic: Python loops. Create 5 MCQs. Format: ___'\n\nfor name, s, u in [('Cooking',cooking_system,cooking_user),('Review',review_system,review_user),('Quiz',quiz_system,quiz_user)]:\n    print(f'=== {name} ===')\n    print(f'System: {s[:60]}...')\n    print(f'User:   {u[:60]}...')",
      solution: "cooking_system='You are Mama Titi, a Nigerian cooking expert. Speak warmly and give clear steps.'\ncooking_user='Task: Explain how to make jollof rice. Format: Numbered steps, max 8, include tips.'\nreview_system='You are a senior Python engineer. Give direct, actionable feedback.'\nreview_user='Review this code: {code}. Format: Bullet points — Issues, Fixes, Style tips.'\nquiz_system='You are an expert educator who creates clear multiple choice questions.'\nquiz_user='Topic: Python loops. Create 5 MCQs. Format: Options A-D, mark correct answer.'\nfor name,s,u in [('Cooking',cooking_system,cooking_user),('Review',review_system,review_user),('Quiz',quiz_system,quiz_user)]:\n    print(f'==={name}===')\n    print(f'System:{s[:60]}...')\n    print(f'User:{u[:60]}...')",
      hint: "Be specific in the role. Always state the output format explicitly.",
      rubric: "All 3 prompts have role, task, format. System and user prompts distinct."
    }
  ]
},

"LLM Fundamentals": {
  aiRubric: "Check API call, message roles, response parsing, error handling.",
  lessons: [
    {
      title: "First LLM API Call",
      theory: "## LLM API\n```python\nimport requests\nr = requests.post(\n    'https://api.groq.com/openai/v1/chat/completions',\n    headers={'Authorization': f'Bearer {KEY}'},\n    json={\n        'model': 'llama3-8b-8192',\n        'messages': [\n            {'role':'system','content':'You are helpful.'},\n            {'role':'user','content':'Hello!'}\n        ]\n    }\n)\nprint(r.json()['choices'][0]['message']['content'])\n```",
      instructions: "## Task: ask_llm() Function\nWrite `ask_llm(question, system_prompt)` that builds message list, POSTs to Groq API, returns text, handles errors.",
      starterCode: "import requests, os\nAPI_KEY = os.getenv('GROQ_API_KEY','your-key')\nURL = 'https://api.groq.com/openai/v1/chat/completions'\n\ndef ask_llm(question, system_prompt='You are a helpful tutor.'):\n    messages = [\n        {'role': ___, 'content': ___},\n        {'role': ___, 'content': ___}\n    ]\n    try:\n        r = requests.post(URL,\n            headers={'Authorization': f'Bearer {API_KEY}'},\n            json={'model':'llama3-8b-8192','messages':___})\n        return r.json()[___][0][___][___]\n    except Exception as e:\n        return f'Error: {e}'\n\nprint(ask_llm('What is a Python list?'))",
      solution: "import requests,os\nAPI_KEY=os.getenv('GROQ_API_KEY','your-key')\nURL='https://api.groq.com/openai/v1/chat/completions'\ndef ask_llm(question,system_prompt='You are a helpful tutor.'):\n    messages=[{'role':'system','content':system_prompt},{'role':'user','content':question}]\n    try:\n        r=requests.post(URL,headers={'Authorization':f'Bearer {API_KEY}'},json={'model':'llama3-8b-8192','messages':messages})\n        return r.json()['choices'][0]['message']['content']\n    except Exception as e:\n        return f'Error:{e}'\nprint(ask_llm('What is a Python list?'))",
      hint: "Roles: 'system' and 'user'. Response: json()['choices'][0]['message']['content'].",
      rubric: "Both roles correct. POST URL. Response extracted. try/except present."
    },
    {
      title: "Conversation Memory",
      theory: "## Multi-turn Conversations\nLLMs are stateless — pass full history:\n```python\nhistory = [{'role':'system','content':'...'}]\nhistory.append({'role':'user','content':msg})\n# get reply\nhistory.append({'role':'assistant','content':reply})\n# next turn: send full history again\n```",
      instructions: "## Task: Chatbot Class\nBuild `Chatbot` with:\n- `chat(message)` — appends user msg, calls API, appends reply, returns reply\n- `reset()` — clears history keeping system prompt\n- Test with 3-turn conversation",
      starterCode: "import requests, os\n\nclass Chatbot:\n    def __init__(self, system='You are a helpful assistant.'):\n        self.history = [{'role':'system','content':___}]\n        self.api_key = os.getenv('GROQ_API_KEY','')\n\n    def chat(self, message):\n        self.history.append({'role':'user','content':___})\n        r = requests.post(\n            'https://api.groq.com/openai/v1/chat/completions',\n            headers={'Authorization':f'Bearer {self.api_key}'},\n            json={'model':'llama3-8b-8192','messages':self.___}\n        )\n        reply = r.json()['choices'][0]['message']['content']\n        self.history.append({'role':___,'content':reply})\n        return reply\n\n    def reset(self):\n        sys = self.history[0]\n        self.history = [___]\n\nbot = Chatbot('You are a Python tutor.')\nprint(bot.chat('What is a variable?'))\nprint(bot.chat('Show me an example'))\nprint(f'History length: {len(bot.history)}')",
      solution: "import requests,os\nclass Chatbot:\n    def __init__(self,system='You are a helpful assistant.'):\n        self.history=[{'role':'system','content':system}]\n        self.api_key=os.getenv('GROQ_API_KEY','')\n    def chat(self,message):\n        self.history.append({'role':'user','content':message})\n        r=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {self.api_key}'},json={'model':'llama3-8b-8192','messages':self.history})\n        reply=r.json()['choices'][0]['message']['content']\n        self.history.append({'role':'assistant','content':reply})\n        return reply\n    def reset(self):\n        sys=self.history[0]\n        self.history=[sys]\nbot=Chatbot('You are a Python tutor.')\nprint(bot.chat('What is a variable?'))\nprint(bot.chat('Show me an example'))\nprint(f'History:{len(bot.history)}')",
      hint: "Append user then assistant each turn. Pass self.history to API. reset() keeps only index 0.",
      rubric: "history initialized. chat() appends both roles. history passed to API. reset() correct."
    },
    {
      title: "Structured JSON Output",
      theory: "## Getting Structured Output\nForce JSON with a system prompt:\n```python\nsystem = \"\"\"You are a data extractor.\nAlways respond ONLY with valid JSON.\nNo explanation, no markdown, just JSON.\"\"\"\n\nuser = \"Extract: name, age, skills from: 'Ada, 22, Python and SQL'\"\n```\nThen parse: `json.loads(reply)`",
      instructions: "## Task: Resume Parser\nWrite `parse_resume(text)` that:\n1. Sends text to LLM with JSON-only system prompt\n2. Asks for: name, age, skills (list), experience_years\n3. Parses and returns the dict\n4. Test with a sample resume text",
      starterCode: "import requests, os, json\nAPI_KEY = os.getenv('GROQ_API_KEY','')\n\ndef parse_resume(text):\n    system = '___. Always respond ONLY with valid JSON. No markdown.'\n    user   = f'Extract name, age, skills list, experience_years from: {text}'\n    \n    r = requests.post(\n        'https://api.groq.com/openai/v1/chat/completions',\n        headers={'Authorization':f'Bearer {API_KEY}'},\n        json={'model':'llama3-8b-8192','messages':[\n            {'role':'system','content':___},\n            {'role':'user','content':___}\n        ]}\n    )\n    reply = r.json()['choices'][0]['message']['content']\n    \n    # Clean and parse\n    clean = reply.strip().strip('`').replace('json','').strip()\n    return json.___(clean)\n\nresume = 'Ada Okonkwo, 24 years old, Python FastAPI SQL, 3 years backend experience'\nresult = parse_resume(resume)\nprint(result)\nprint(f'Name: {result[\"name\"]}')\nprint(f'Skills: {result[\"skills\"]}')",
      solution: "import requests,os,json\nAPI_KEY=os.getenv('GROQ_API_KEY','')\ndef parse_resume(text):\n    system='You are a data extractor. Always respond ONLY with valid JSON. No markdown.'\n    user=f'Extract name, age, skills list, experience_years from: {text}'\n    r=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {API_KEY}'},json={'model':'llama3-8b-8192','messages':[{'role':'system','content':system},{'role':'user','content':user}]})\n    reply=r.json()['choices'][0]['message']['content']\n    clean=reply.strip().strip('`').replace('json','').strip()\n    return json.loads(clean)\nresume='Ada Okonkwo, 24 years old, Python FastAPI SQL, 3 years backend experience'\nresult=parse_resume(resume)\nprint(result)\nprint(f'Name:{result[\"name\"]}')\nprint(f'Skills:{result[\"skills\"]}')",
      hint: "System prompt must say 'ONLY valid JSON'. Strip backticks from reply. Use json.loads() to parse.",
      rubric: "JSON-only system prompt. Both messages passed. reply stripped. json.loads() used."
    }
  ]
},

"RAG Pipelines": {
  aiRubric: "Check chunking, embedding/similarity, retrieval, context injection into prompt.",
  lessons: [
    {
      title: "What is RAG?",
      theory: "## RAG Pipeline\n1. **Index** — chunk docs, embed, store\n2. **Retrieve** — embed query, find similar chunks\n3. **Generate** — pass chunks as context to LLM\n\n```python\n# Pseudo-code\nchunks  = split(doc)\nvectors = [embed(c) for c in chunks]\n# At query time:\nq_vec    = embed(user_q)\nrelevant = top_k_similar(q_vec, vectors)\nresponse = llm(user_q, context=relevant)\n```",
      instructions: "## Task: Simple RAG with Word Overlap\n1. 5 documents about Python topics\n2. Similarity function (word overlap)\n3. retrieve() returns most relevant doc\n4. rag_prompt() injects context\n5. Test with 2 queries",
      starterCode: "documents = [\n    'Python lists store ordered mutable collections.',\n    'Dictionaries store key-value pairs for fast lookups.',\n    'Functions let you reuse code and accept parameters.',\n    'Classes define blueprints for objects with methods.',\n    'Loops iterate over sequences with for and while.'\n]\n\ndef similarity(query, doc):\n    q = set(query.lower().split())\n    d = set(doc.lower().split())\n    return len(q & d) / (len(q) + 1)\n\ndef retrieve(query, docs, top_k=1):\n    scores = [(similarity(___, doc), doc) for doc in ___]\n    scores.sort(reverse=___)\n    return [doc for _, doc in scores[:___]]\n\ndef rag_prompt(question, docs):\n    ctx = retrieve(___, docs)[0]\n    return f'Context: {ctx}\\n\\nQuestion: {___}\\n\\nAnswer based on context only:'\n\nfor q in ['How do I store key-value data?', 'What is a loop?']:\n    print(retrieve(q, documents))\n    print(rag_prompt(q, documents))\n    print('---')",
      solution: "documents=['Python lists store ordered mutable collections.','Dictionaries store key-value pairs for fast lookups.','Functions let you reuse code and accept parameters.','Classes define blueprints for objects with methods.','Loops iterate over sequences with for and while.']\ndef similarity(query,doc):\n    q=set(query.lower().split())\n    d=set(doc.lower().split())\n    return len(q&d)/(len(q)+1)\ndef retrieve(query,docs,top_k=1):\n    scores=[(similarity(query,doc),doc) for doc in docs]\n    scores.sort(reverse=True)\n    return [doc for _,doc in scores[:top_k]]\ndef rag_prompt(question,docs):\n    ctx=retrieve(question,docs)[0]\n    return f'Context:{ctx}\\nQuestion:{question}\\nAnswer based on context only:'\nfor q in ['How do I store key-value data?','What is a loop?']:\n    print(retrieve(q,documents))\n    print(rag_prompt(q,documents))\n    print('---')",
      hint: "sort(reverse=True) for highest first. context[0] gets top result. Pass question to rag_prompt.",
      rubric: "similarity computes overlap. retrieve sorts correctly. rag_prompt injects context. Both queries tested."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━
// FRONTEND
// ━━━━━━━━━━━━━━━━━━━━━━━━━

"HTML Essentials": {
  aiRubric: "Check valid HTML structure, semantic tags, correct nesting.",
  lessons: [
    {
      title: "HTML Document Structure",
      theory: "## HTML Skeleton\n```html\n<!DOCTYPE html>\n<html lang='en'>\n<head>\n  <meta charset='UTF-8'>\n  <title>Title</title>\n</head>\n<body>\n  <h1>Hello</h1>\n  <p>Paragraph</p>\n</body>\n</html>\n```",
      instructions: "## Task: Student Profile Page\n1. Proper DOCTYPE + structure\n2. Title: 'My Profile'\n3. h1 with your name\n4. p with your course\n5. ul with 3 skills\n6. Link to GitHub",
      starterCode: "<!DOCTYPE ___>\n<html lang='en'>\n<___>\n  <meta charset='UTF-8'>\n  <title>___</title>\n</___>\n<___>\n  <h1>___</h1>\n  <p>Course: ___</p>\n  <h2>Skills</h2>\n  <ul>\n    <li>___</li>\n    <li>___</li>\n    <li>___</li>\n  </ul>\n  <a href='https://github.com'>GitHub</a>\n</___>\n</html>",
      solution: "<!DOCTYPE html>\n<html lang='en'>\n<head>\n  <meta charset='UTF-8'>\n  <title>My Profile</title>\n</head>\n<body>\n  <h1>Ada Okonkwo</h1>\n  <p>Course: Computer Science</p>\n  <h2>Skills</h2>\n  <ul>\n    <li>Python</li>\n    <li>FastAPI</li>\n    <li>SQL</li>\n  </ul>\n  <a href='https://github.com'>GitHub</a>\n</body>\n</html>",
      hint: "DOCTYPE goes first. head holds meta. body holds visible content. ul > li for lists.",
      rubric: "DOCTYPE. head/body correct. h1/p/ul/li/a all present."
    }
  ]
},

"JavaScript Basics": {
  aiRubric: "Check let/const, functions, arrow functions, array methods.",
  lessons: [
    {
      title: "Variables & Functions",
      theory: "## JS Basics\n```javascript\nconst name = 'Ada';   // can't reassign\nlet score = 0;        // can reassign\n\nfunction greet(name) {\n  return `Hello, ${name}!`;\n}\n\nconst add = (a,b) => a + b; // arrow\nconsole.log(greet('Ada'));\nconsole.log(add(3,4));  // 7\n```",
      instructions: "## Task: Score Processor\n1. `scores` array of 5 numbers\n2. `getAverage(arr)` using reduce\n3. `getGrade(avg)` returning A/B/C/F\n4. Log: `Average: 82.4 | Grade: B`",
      starterCode: "const scores = [78, 92, 65, 88, ___];\n\nfunction getAverage(arr) {\n  const sum = arr.reduce((___, b) => a + b, 0);\n  return sum / arr.___;\n}\n\nfunction getGrade(avg) {\n  if (avg >= 80) return ___;\n  else if (avg >= 70) return ___;\n  else if (avg >= 60) return ___;\n  else return ___;\n}\n\nconst avg = getAverage(___);\nconsole.log(`Average: ${avg.toFixed(1)} | Grade: ${getGrade(avg)}`);",
      solution: "const scores=[78,92,65,88,75];\nfunction getAverage(arr){\n  const sum=arr.reduce((a,b)=>a+b,0);\n  return sum/arr.length;\n}\nfunction getGrade(avg){\n  if(avg>=80)return'A';\n  else if(avg>=70)return'B';\n  else if(avg>=60)return'C';\n  else return'F';\n}\nconst avg=getAverage(scores);\nconsole.log(`Average:${avg.toFixed(1)} | Grade:${getGrade(avg)}`);",
      hint: "reduce((a,b)=>a+b,0) sums. arr.length for count. toFixed(1) for 1 decimal.",
      rubric: "reduce for sum. Division by length. Grade conditions correct. Template literal used."
    }
  ]
}

}; // end courseManifest