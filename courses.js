// ═══════════════════════════════════════════════════
//  MABEL ACADEMY — courses.js  (Mega Expanded Edition)
// ═══════════════════════════════════════════════════

const curriculum = {
  "Python Core": {
    "Beginner":      ["Python Fundamentals","Control Flow & Loops","Functions & Scope","Lists & Tuples","Dictionaries & Sets"],
    "Intermediate":  ["OOP in Python","File Handling & Exceptions","Modules & Packages","List Comprehensions","Iterators & Generators"],
    "Advanced":      ["Decorators & Closures","Concurrency in Python","Design Patterns","Metaprogramming","Memory & Performance"]
  },
  "Frontend": {
    "Beginner":      ["HTML Essentials","CSS Styling & Layout","JavaScript Basics","Forms & Validation","Responsive Design Basics"],
    "Intermediate":  ["DOM Manipulation","Fetch API & AJAX","ES6+ Modern JS","CSS Animations","LocalStorage & State"],
    "Advanced":      ["React Fundamentals","React Hooks & Context","Performance Optimization","Testing Frontend Code","Build Tools & Webpack"]
  },
  "Backend": {
    "Beginner":      ["Intro to Backend","HTTP & REST Concepts","Python for Web","JSON & APIs","Environment & Setup"],
    "Intermediate":  ["REST APIs with FastAPI","Authentication & JWT","Django Web Framework","Flask Microframework","Database Integration"],
    "Advanced":      ["Django REST Framework","Flask Advanced Patterns","Async Python","API Security & Rate Limiting","Deployment & Docker"]
  },
  "SQL & Databases": {
    "Beginner":      ["SQL Fundamentals","Filtering & Sorting","Joins & Relationships","Aggregations & Grouping","Subqueries"],
    "Intermediate":  ["Indexes & Performance","Stored Procedures","Transactions & ACID","Views & CTEs","PostgreSQL Deep Dive"],
    "Advanced":      ["Query Optimization","Database Design Patterns","NoSQL with MongoDB","ORMs with SQLAlchemy","Sharding & Replication"]
  },
  "Data Science": {
    "Beginner":      ["Intro to Data Science","Pandas & NumPy Basics","Data Cleaning","Exploratory Data Analysis","Data Visualization"],
    "Intermediate":  ["Statistical Analysis","Intro to Machine Learning","Scikit-Learn Pipelines","Regression Models","Classification Models"],
    "Advanced":      ["Feature Engineering","Ensemble Methods","Model Evaluation & Tuning","Time Series Analysis","Deep Learning Basics"]
  },
  "AI Engineering": {
    "Beginner":      ["AI & ML Concepts","Python for AI","Working with APIs","Prompt Engineering","AI Use Cases"],
    "Intermediate":  ["LLM Fundamentals","RAG Pipelines","LangChain Basics","Vector Databases","Fine-tuning Concepts"],
    "Advanced":      ["LangChain & Agents","Multi-Agent Systems","LLM Evaluation","Production AI Systems","AI Safety & Ethics"]
  }
};

const courseManifest = {

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// PYTHON CORE — BEGINNER
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Python Fundamentals": {
  aiRubric: "Check variables correctly typed, print statements work, f-strings used.",
  lessons: [
    {
      title: "Variables & Data Types",
      theory: "## Variables\nPython is dynamically typed.\n```python\nname = 'Ada'      # str\nage  = 25         # int\nprice = 9.99      # float\nactive = True     # bool\nprint(type(name)) # <class 'str'>\n```",
      instructions: "## Task: Your Profile\n1. Create `name` (string), `age` (int), `height` (float), `is_student` (bool)\n2. Print all four with labels\n3. Print `type(name)`",
      starterCode: "name = ___\nage = ___\nheight = ___\nis_student = ___\n\nprint('Name:', ___)\nprint('Age:', ___)\nprint('Height:', ___)\nprint('Student:', ___)\nprint('Type:', type(___))",
      solution: "name='Ada Okonkwo'\nage=22\nheight=1.65\nis_student=True\nprint('Name:',name)\nprint('Age:',age)\nprint('Height:',height)\nprint('Student:',is_student)\nprint('Type:',type(name))",
      hint: "Strings need quotes. Booleans are True or False.",
      rubric: "All 4 variables typed. All 5 prints correct."
    },
    {
      title: "String Operations",
      theory: "## Strings\n```python\nfull = 'Ada Okonkwo'\nprint(len(full))       # 11\nprint(full.upper())    # ADA OKONKWO\nprint(full[0:3])       # Ada\nprint(f'Hi {full}!')   # Hi Ada Okonkwo!\n```",
      instructions: "## Task: String Manipulation\n1. Create `first_name` and `last_name`\n2. Combine into `full_name`\n3. Print length, uppercase, and an f-string greeting",
      starterCode: "first_name = '___'\nlast_name = '___'\nfull_name = ___ + ' ' + ___\n\nprint('Length:', ___)\nprint('Upper:', ___)\nprint(f'Hello, {full_name}! Welcome to Mabel Academy.')",
      solution: "first_name='Ada'\nlast_name='Okonkwo'\nfull_name=first_name+' '+last_name\nprint('Length:',len(full_name))\nprint('Upper:',full_name.upper())\nprint(f'Hello, {full_name}! Welcome to Mabel Academy.')",
      hint: "Use len() for length, .upper() for caps.",
      rubric: "Concatenation correct. len() and upper() used. f-string correct."
    },
    {
      title: "Numbers & Arithmetic",
      theory: "## Operators\n+, -, *, / (divide), // (floor div), % (modulo), ** (power)\n```python\nprint(10 // 3)  # 3\nprint(10 % 3)   # 1\nprint(2 ** 8)   # 256\nprint(round(3.14159, 2))  # 3.14\n```",
      instructions: "## Task: Invoice Calculator\n`price_per_item = 1500`, `quantity = 7`\n1. Calculate subtotal\n2. Apply 7.5% VAT\n3. Print subtotal, VAT, total (rounded 2dp)",
      starterCode: "price_per_item = 1500\nquantity = 7\n\nsubtotal = ___\nvat = ___\ntotal = ___\n\nprint(f'Subtotal: N{subtotal}')\nprint(f'VAT:      N{round(___, 2)}')\nprint(f'Total:    N{round(___, 2)}')",
      solution: "price_per_item=1500\nquantity=7\nsubtotal=price_per_item*quantity\nvat=subtotal*0.075\ntotal=subtotal+vat\nprint(f'Subtotal: N{subtotal}')\nprint(f'VAT:      N{round(vat,2)}')\nprint(f'Total:    N{round(total,2)}')",
      hint: "VAT = subtotal * 0.075. Total = subtotal + vat.",
      rubric: "Correct multiplication. VAT 0.075. round() used."
    },
    {
      title: "User Input & Type Casting",
      theory: "## Input\n```python\nname  = input('Name: ')          # always string\nage   = int(input('Age: '))      # cast to int\nprice = float(input('Price: '))  # cast to float\n```\nType casting: `int()`, `float()`, `str()`, `bool()`",
      instructions: "## Task: Simple Calculator\n1. Take two numbers as input (cast to float)\n2. Print sum, difference, product, quotient (2dp)",
      starterCode: "a = float(input('Enter first number: '))\nb = float(input('Enter second number: '))\n\nprint(f'Sum:        {___}')\nprint(f'Difference: {___}')\nprint(f'Product:    {___}')\nprint(f'Quotient:   {round(___ / ___, 2)}')",
      solution: "a=float(input('Enter first number: '))\nb=float(input('Enter second number: '))\nprint(f'Sum:        {a+b}')\nprint(f'Difference: {a-b}')\nprint(f'Product:    {a*b}')\nprint(f'Quotient:   {round(a/b,2)}')",
      hint: "Wrap input() with float(). a+b, a-b, a*b, a/b.",
      rubric: "Both inputs cast to float. All 4 operations printed."
    },
    {
      title: "Comments & Code Style",
      theory: "## PEP 8\n```python\n# Single-line comment\n\"\"\"\nDocstring\n\"\"\"\nstudent_name = 'Ada'  # snake_case\nMAX_SCORE = 100       # UPPER_CASE constants\n```",
      instructions: "## Task: Clean & Document\nRewrite messy code:\n```python\nx='ada'\ny=22\nZ=True\nprint(x,y,Z)\n```\nAdd docstring, snake_case names, comments, f-string.",
      starterCode: '"""\nPurpose: ___\nAuthor: ___\n"""\n\nstudent_name = "___"  # full name\nstudent_age = ___\nis_enrolled = ___\n\nprint(f"{student_name} | Age: {student_age} | Enrolled: {is_enrolled}")',
      solution: '"""\nPurpose: Display student profile\nAuthor: Mabel Academy\n"""\n\nstudent_name = "Ada Okonkwo"\nstudent_age = 22\nis_enrolled = True\n\nprint(f"{student_name} | Age: {student_age} | Enrolled: {is_enrolled}")',
      hint: "Triple quotes for docstring. snake_case uses underscores.",
      rubric: "Docstring present. snake_case used. f-string output correct."
    }
  ]
},

"Control Flow & Loops": {
  aiRubric: "Check if/elif/else syntax, correct indentation, loop ranges.",
  lessons: [
    {
      title: "If / Elif / Else",
      theory: "## Conditionals\n```python\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelse:\n    grade = 'F'\n```",
      instructions: "## Task: Grade Calculator\nA(90+), B(80+), C(70+), D(60+), F(below 60). Test with score = 85.",
      starterCode: "score = 85\n\nif ___:\n    grade = 'A'\nelif ___:\n    grade = 'B'\nelif ___:\n    grade = 'C'\nelif ___:\n    grade = 'D'\nelse:\n    grade = 'F'\n\nprint(f'Score: {score} -> Grade: {grade}')",
      solution: "score=85\nif score>=90:\n    grade='A'\nelif score>=80:\n    grade='B'\nelif score>=70:\n    grade='C'\nelif score>=60:\n    grade='D'\nelse:\n    grade='F'\nprint(f'Score: {score} -> Grade: {grade}')",
      hint: "Start from highest boundary. Use >= so values land in correct band.",
      rubric: "5 branches. Correct boundaries. Output correct."
    },
    {
      title: "For Loops & Range",
      theory: "## For Loops\n```python\nfor i in range(1, 6):       # 1,2,3,4,5\n    print(i)\n\nfor i, v in enumerate(['a','b','c']):\n    print(i, v)             # 0 a  1 b  2 c\n```",
      instructions: "## Task: Multiplication Table\nPrint the 9 times table from 1 to 12.",
      starterCode: "for i in range(___, ___):\n    result = 9 * i\n    print(f'9 x {i} = {result}')",
      solution: "for i in range(1,13):\n    result=9*i\n    print(f'9 x {i} = {result}')",
      hint: "range(1, 13) gives 1 to 12.",
      rubric: "range(1,13). result = 9*i. Format correct."
    },
    {
      title: "While Loops",
      theory: "## While\n```python\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1   # always increment!\n```",
      instructions: "## Task: Countdown\nCount down from 10 to 1, then print 'Liftoff!'",
      starterCode: "countdown = 10\nwhile ___ > 0:\n    print(countdown)\n    countdown ___\nprint('Liftoff!')",
      solution: "countdown=10\nwhile countdown>0:\n    print(countdown)\n    countdown-=1\nprint('Liftoff!')",
      hint: "countdown -= 1 decrements by 1 each iteration.",
      rubric: "Condition > 0. countdown -= 1. Liftoff after."
    },
    {
      title: "Break & Continue",
      theory: "## Loop Control\n```python\nfor i in range(10):\n    if i % 2 == 0: continue  # skip even\n    if i > 7:      break     # stop\n    print(i)\n# prints: 1 3 5 7\n```",
      instructions: "## Task: First Even > 10\nLoop 1-30. Skip odd numbers with continue. Print first even > 10 and break.",
      starterCode: "for n in range(1, 31):\n    if n % 2 != 0:\n        ___\n    if n > 10:\n        print(f'First even > 10: {n}')\n        ___",
      solution: "for n in range(1,31):\n    if n%2!=0:\n        continue\n    if n>10:\n        print(f'First even > 10: {n}')\n        break",
      hint: "n % 2 != 0 means odd. continue skips, break exits.",
      rubric: "continue for odds. break after printing. Output is 12."
    },
    {
      title: "Nested Loops",
      theory: "## Nested Loops\n```python\nfor i in range(1, 4):\n    for j in range(1, 4):\n        print(i * j, end='\\t')\n    print()   # newline\n```\nInner loop runs fully for each outer iteration.",
      instructions: "## Task: 5x5 Multiplication Grid\nPrint a 5x5 table using `end='\\t'` for spacing.",
      starterCode: "for i in range(1, ___):\n    for j in range(1, ___):\n        print(i * j, end='\\t')\n    print()",
      solution: "for i in range(1,6):\n    for j in range(1,6):\n        print(i*j,end='\\t')\n    print()",
      hint: "Both ranges (1, 6). print() alone resets line.",
      rubric: "Both ranges correct. i*j. end='\\t'. print() for newline."
    }
  ]
},

"Functions & Scope": {
  aiRubric: "Check def, parameters, return, correct calls.",
  lessons: [
    {
      title: "Defining Functions",
      theory: "## Functions\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Ada'))  # Hello, Ada!\n```",
      instructions: "## Task: Temperature Converter\nWrite `celsius_to_fahrenheit(c)`. Formula: F = (C x 9/5) + 32. Test with 0, 100, 37.",
      starterCode: "def celsius_to_fahrenheit(c):\n    f = ___\n    return ___\n\nprint(celsius_to_fahrenheit(0))    # 32.0\nprint(celsius_to_fahrenheit(100))  # 212.0\nprint(celsius_to_fahrenheit(37))   # 98.6",
      solution: "def celsius_to_fahrenheit(c):\n    f=(c*9/5)+32\n    return f\nprint(celsius_to_fahrenheit(0))\nprint(celsius_to_fahrenheit(100))\nprint(celsius_to_fahrenheit(37))",
      hint: "(c * 9/5) + 32. Store in f and return it.",
      rubric: "Correct formula. return present. 3 test calls."
    },
    {
      title: "Default Arguments",
      theory: "## Defaults\n```python\ndef greet(name, greeting='Hello'):\n    return f'{greeting}, {name}!'\n\ngreet('Ada')            # Hello, Ada!\ngreet('Ada', 'Hey')    # Hey, Ada!\n```",
      instructions: "## Task: Receipt Generator\nCreate `create_receipt(item, price, quantity=1, currency='NGN')`\nReturn: `Receipt: 3x Jollof Rice = NGN 4500`",
      starterCode: "def create_receipt(item, price, quantity=___, currency=___):\n    total = price * ___\n    return f'Receipt: {quantity}x {item} = {currency} {total}'\n\nprint(create_receipt('Suya', 800))\nprint(create_receipt('Rice', 1500, quantity=3))\nprint(create_receipt('Coffee', 2000, currency='USD'))",
      solution: "def create_receipt(item,price,quantity=1,currency='NGN'):\n    total=price*quantity\n    return f'Receipt: {quantity}x {item} = {currency} {total}'\nprint(create_receipt('Suya',800))\nprint(create_receipt('Rice',1500,quantity=3))\nprint(create_receipt('Coffee',2000,currency='USD'))",
      hint: "quantity=1, currency='NGN' as defaults.",
      rubric: "Correct defaults. total = price*quantity. Format matches."
    },
    {
      title: "Multiple Return Values",
      theory: "## Multiple Returns\n```python\ndef min_max(nums):\n    return min(nums), max(nums)\n\nlo, hi = min_max([3, 1, 9])\nprint(lo, hi)  # 1 9\n```",
      instructions: "## Task: Score Statistics\nWrite `score_stats(scores)` returning mean, highest, lowest, pass_count (>=60).",
      starterCode: "def score_stats(scores):\n    mean = sum(scores) / len(scores)\n    highest = ___\n    lowest = ___\n    passes = len([s for s in scores if s >= 60])\n    return ___, ___, ___, ___\n\nscores = [78,92,45,88,60,34,75]\nmean, high, low, passes = score_stats(scores)\nprint(f'Mean:{mean:.1f} High:{high} Low:{low} Passes:{passes}')",
      solution: "def score_stats(scores):\n    mean=sum(scores)/len(scores)\n    highest=max(scores)\n    lowest=min(scores)\n    passes=len([s for s in scores if s>=60])\n    return mean,highest,lowest,passes\nscores=[78,92,45,88,60,34,75]\nmean,high,low,passes=score_stats(scores)\nprint(f'Mean:{mean:.1f} High:{high} Low:{low} Passes:{passes}')",
      hint: "max(), min(). Comprehension for passes. Return 4 comma-separated.",
      rubric: "max/min used. Comprehension correct. 4 values returned."
    },
    {
      title: "Lambda Functions",
      theory: "## Lambda\n```python\nsquare = lambda x: x**2\nprint(square(5))  # 25\n\n# With sorted & filter\nranked = sorted(students, key=lambda s: s[1], reverse=True)\nevens  = list(filter(lambda x: x%2==0, nums))\n```",
      instructions: "## Task: Sort Students by Score\n`students = [(name, score)]`\n1. Sort by score descending\n2. Filter passing students (>=60)\n3. Print ranked list",
      starterCode: "students = [('Ada',88),('Tunde',55),('Ngozi',92),('Emeka',67),('Amaka',45)]\n\nranked = sorted(students, key=lambda s: ___, reverse=___)\nfor i,(name,score) in enumerate(ranked, 1):\n    print(f'{i}. {name}: {score}')\n\npassed = list(filter(lambda s: s[___] >= 60, students))\nprint(f'Passed: {[s[0] for s in passed]}')",
      solution: "students=[('Ada',88),('Tunde',55),('Ngozi',92),('Emeka',67),('Amaka',45)]\nranked=sorted(students,key=lambda s:s[1],reverse=True)\nfor i,(name,score) in enumerate(ranked,1):\n    print(f'{i}. {name}: {score}')\npassed=list(filter(lambda s:s[1]>=60,students))\nprint(f'Passed: {[s[0] for s in passed]}')",
      hint: "s[1] is the score. reverse=True for descending.",
      rubric: "Lambda s[1]. reverse=True. filter lambda correct."
    }
  ]
},

"Lists & Tuples": {
  aiRubric: "Check list creation, indexing, slicing, methods, tuple usage.",
  lessons: [
    {
      title: "Creating & Indexing Lists",
      theory: "## Lists\n```python\nfruits = ['mango','banana','pawpaw']\nprint(fruits[0])    # mango\nprint(fruits[-1])   # pawpaw\nprint(fruits[1:3])  # ['banana','pawpaw']\nprint(len(fruits))  # 3\n```",
      instructions: "## Task: Classroom List\n1. Create list of 5 student names\n2. Print first and last\n3. Print students 2-4 using slice\n4. Print total count",
      starterCode: "students = [___, ___, ___, ___, ___]\n\nprint('First:', students[___])\nprint('Last:', students[___])\nprint('Middle 3:', students[___:___])\nprint('Total:', ___)",
      solution: "students=['Ada','Tunde','Ngozi','Emeka','Amaka']\nprint('First:',students[0])\nprint('Last:',students[-1])\nprint('Middle 3:',students[1:4])\nprint('Total:',len(students))",
      hint: "[0] is first, [-1] is last. [1:4] gives indices 1,2,3.",
      rubric: "5 items. [0], [-1], [1:4], len() all correct."
    },
    {
      title: "List Methods",
      theory: "## Methods\n```python\nmy = [3,1,4]\nmy.append(9)      # add end\nmy.insert(1, 7)   # insert at index\nmy.remove(4)      # remove value\nmy.sort()         # sort ascending\nmy.reverse()      # reverse\npopped = my.pop() # remove last\n```",
      instructions: "## Task: Shopping Cart\nStart with `cart = ['rice','beans']`\n1. Add 'tomatoes' and 'palm oil'\n2. Insert 'salt' at index 1\n3. Remove 'beans'\n4. Sort alphabetically\n5. Print final cart",
      starterCode: "cart = ['rice', 'beans']\n\ncart.___('tomatoes')\ncart.___('palm oil')\ncart.___(1, 'salt')\ncart.___('beans')\ncart.sort()\n\nprint('Cart:', cart)\nprint('Items:', len(cart))",
      solution: "cart=['rice','beans']\ncart.append('tomatoes')\ncart.append('palm oil')\ncart.insert(1,'salt')\ncart.remove('beans')\ncart.sort()\nprint('Cart:',cart)\nprint('Items:',len(cart))",
      hint: "append() end. insert(idx,val). remove(val).",
      rubric: "append twice, insert, remove, sort. Output correct."
    },
    {
      title: "List Comprehensions",
      theory: "## Comprehensions\n```python\nsquares = [x**2 for x in range(5)]\nevens   = [n for n in range(20) if n%2==0]\n```",
      instructions: "## Task: Three Comprehensions\n1. Squares of 1-10\n2. Even numbers 1-20\n3. Words longer than 4 chars from a sentence",
      starterCode: "squares = [___ for x in range(1, 11)]\nprint(squares)\n\nevens = [n for n in range(1,21) if n % ___ == 0]\nprint(evens)\n\nsentence = 'Mabel Academy teaches backend and frontend development'\nlong_words = [w for w in sentence.split() if len(w) > ___]\nprint(long_words)",
      solution: "squares=[x**2 for x in range(1,11)]\nprint(squares)\nevens=[n for n in range(1,21) if n%2==0]\nprint(evens)\nsentence='Mabel Academy teaches backend and frontend development'\nlong_words=[w for w in sentence.split() if len(w)>4]\nprint(long_words)",
      hint: "x**2 for squares. n%2==0 for evens. len(w)>4 for long words.",
      rubric: "All 3 comprehensions correct."
    },
    {
      title: "Tuples",
      theory: "## Tuples — Immutable\n```python\ncoords = (6.5244, 3.3792)\nx, y = coords   # unpacking\nlocs = {(6.5, 3.4): 'Lagos'}  # as dict key\n```",
      instructions: "## Task: Student Record\n1. Create `student = (name, age, course, gpa)`\n2. Unpack and print\n3. Use as a dict key",
      starterCode: "student = ('Ada Okonkwo', 22, 'Computer Science', 4.5)\n\nname, age, course, gpa = ___\nprint(f'{name} | {course} | GPA: {gpa}')\n\nrecords = {}\nrecords[___] = 'active'\nprint(records)",
      solution: "student=('Ada Okonkwo',22,'Computer Science',4.5)\nname,age,course,gpa=student\nprint(f'{name} | {course} | GPA: {gpa}')\nrecords={}\nrecords[student]='active'\nprint(records)",
      hint: "Unpack: name,age,course,gpa = student. Use whole tuple as key.",
      rubric: "Tuple created. Unpacking correct. Used as dict key."
    }
  ]
},

"Dictionaries & Sets": {
  aiRubric: "Check dict syntax, .get(), .items(), set operations.",
  lessons: [
    {
      title: "Dictionary Basics",
      theory: "## Dicts\n```python\ns = {'name':'Ada','score':88}\nprint(s['name'])              # Ada\nprint(s.get('grade','N/A'))   # N/A\ns['gpa'] = 4.5               # add key\ndel s['score']               # delete key\nfor k,v in s.items():\n    print(k, v)\n```",
      instructions: "## Task: Student Registry\n1. Dict with name, age, course, score\n2. Print name with [] and score with .get()\n3. Add grade key (A if >=80 else B)\n4. Delete score\n5. Loop and print all pairs",
      starterCode: "student = {'name':'Ada','age':22,'course':'Python','score':88}\n\nprint(student[___])\nprint(student.get('score', 'Not graded'))\n\nstudent['grade'] = 'A' if student['score'] >= 80 else 'B'\ndel student[___]\n\nfor key, value in student.___():\n    print(f'{key}: {value}')",
      solution: "student={'name':'Ada','age':22,'course':'Python','score':88}\nprint(student['name'])\nprint(student.get('score','Not graded'))\nstudent['grade']='A' if student['score']>=80 else 'B'\ndel student['score']\nfor key,value in student.items():\n    print(f'{key}: {value}')",
      hint: ".get(key, default) is safe. .items() for looping.",
      rubric: "[] and .get() used. Grade added. del used. .items() loop correct."
    },
    {
      title: "Nested Dictionaries",
      theory: "## Nested Dicts\n```python\nstudents = {\n    'ada':   {'age':22,'score':88},\n    'tunde': {'age':25,'score':72}\n}\nprint(students['ada']['score'])  # 88\n```",
      instructions: "## Task: School Registry\n1. Nested dict with 3 students (age, course, score)\n2. Print one student's course\n3. Add grade to each student using a loop\n4. Print all students with their grades",
      starterCode: "registry = {\n    'ada':   {'age':22,'course':'Python', 'score':88},\n    'tunde': {'age':25,'course':'FastAPI','score':72},\n    'ngozi': {'age':23,'course':'SQL',    'score':95}\n}\n\nprint(registry[___][___])\n\nfor name, info in registry.___():\n    info['grade'] = 'A' if info['score'] >= 80 else 'B'\n\nfor name, info in registry.items():\n    print(f'{name}: {info[\"course\"]} | Grade: {info[___]}')",
      solution: "registry={'ada':{'age':22,'course':'Python','score':88},'tunde':{'age':25,'course':'FastAPI','score':72},'ngozi':{'age':23,'course':'SQL','score':95}}\nprint(registry['ada']['course'])\nfor name,info in registry.items():\n    info['grade']='A' if info['score']>=80 else 'B'\nfor name,info in registry.items():\n    print(f'{name}: {info[\"course\"]} | Grade: {info[\"grade\"]}')",
      hint: "registry['ada']['course'] for nested access.",
      rubric: "Nested access correct. Loop adds grade. Final print correct."
    },
    {
      title: "Sets & Operations",
      theory: "## Sets\n```python\na = {1,2,3,4}\nb = {3,4,5,6}\nprint(a | b)  # union\nprint(a & b)  # intersection\nprint(a - b)  # difference\nprint(a ^ b)  # symmetric diff\n```",
      instructions: "## Task: Enrolment Overlap\nTrack A: {Ada,Tunde,Ngozi,Emeka} Track B: {Ngozi,Emeka,Amaka,Bola}\nFind: in both, all students, only Track A, exactly one track.",
      starterCode: "track_a = {'Ada','Tunde','Ngozi','Emeka'}\ntrack_b = {'Ngozi','Emeka','Amaka','Bola'}\n\nboth   = ___ & ___\nall_s  = ___ | ___\nonly_a = ___ - ___\nexcl   = ___ ^ ___\n\nprint(f'Both:      {both}')\nprint(f'All:       {all_s}')\nprint(f'Only A:    {only_a}')\nprint(f'Exclusive: {excl}')",
      solution: "track_a={'Ada','Tunde','Ngozi','Emeka'}\ntrack_b={'Ngozi','Emeka','Amaka','Bola'}\nboth=track_a&track_b\nall_s=track_a|track_b\nonly_a=track_a-track_b\nexcl=track_a^track_b\nprint(f'Both:      {both}')\nprint(f'All:       {all_s}')\nprint(f'Only A:    {only_a}')\nprint(f'Exclusive: {excl}')",
      hint: "& intersection, | union, - difference, ^ symmetric.",
      rubric: "All 4 operations correct."
    }
  ]
},


// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// PYTHON CORE — INTERMEDIATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"OOP in Python": {
  aiRubric: "Check class, __init__, self, methods, inheritance, super().__init__().",
  lessons: [
    {
      title: "Classes & Objects",
      theory: "## Classes\n```python\nclass Student:\n    def __init__(self, name, age):\n        self.name = name\n        self.age  = age\n    def greet(self):\n        return f'Hi, I am {self.name}'\n\nada = Student('Ada', 22)\nprint(ada.greet())\n```",
      instructions: "## Task: BankAccount Class\nCreate `BankAccount(owner, balance=0)` with:\n- `deposit(amount)` — adds to balance\n- `withdraw(amount)` — checks funds first\n- `get_balance()` — returns balance",
      starterCode: "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = ___\n        self.balance = ___\n\n    def deposit(self, amount):\n        self.balance += ___\n        print(f'Deposited N{amount}. Balance: N{self.balance}')\n\n    def withdraw(self, amount):\n        if amount > self.___:\n            print('Insufficient funds')\n        else:\n            self.balance -= ___\n            print(f'Withdrawn N{amount}. Balance: N{self.balance}')\n\n    def get_balance(self):\n        return self.___\n\nacc = BankAccount('Ada')\nacc.deposit(5000)\nacc.withdraw(2000)\nacc.withdraw(10000)\nprint(f'Final: N{acc.get_balance()}')",
      solution: "class BankAccount:\n    def __init__(self,owner,balance=0):\n        self.owner=owner\n        self.balance=balance\n    def deposit(self,amount):\n        self.balance+=amount\n        print(f'Deposited N{amount}. Balance: N{self.balance}')\n    def withdraw(self,amount):\n        if amount>self.balance:\n            print('Insufficient funds')\n        else:\n            self.balance-=amount\n            print(f'Withdrawn N{amount}. Balance: N{self.balance}')\n    def get_balance(self):\n        return self.balance\nacc=BankAccount('Ada')\nacc.deposit(5000)\nacc.withdraw(2000)\nacc.withdraw(10000)\nprint(f'Final: N{acc.get_balance()}')",
      hint: "Use self.balance. Check amount > self.balance before withdrawing.",
      rubric: "__init__ correct. deposit/withdraw modify balance. Insufficient check present."
    },
    {
      title: "Inheritance",
      theory: "## Inheritance\n```python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self): return '...'\n\nclass Dog(Animal):\n    def speak(self):\n        return f'{self.name}: Woof!'\n\nd = Dog('Rex')\nprint(d.speak())\n```",
      instructions: "## Task: Employee Hierarchy\n- Base `Employee(name, salary)` with `get_info()`\n- `Manager(name, salary, team_size)` — overrides `get_info()`\n- `Intern(name, duration)` — salary defaults 50000",
      starterCode: "class Employee:\n    def __init__(self, name, salary):\n        self.name = ___\n        self.salary = ___\n    def get_info(self):\n        return f'{self.name} | N{self.salary}'\n\nclass Manager(___):\n    def __init__(self, name, salary, team_size):\n        super().__init__(___, ___)\n        self.team_size = ___\n    def get_info(self):\n        return super().get_info() + f' | Team: {self.team_size}'\n\nclass Intern(___):\n    def __init__(self, name, duration):\n        super().__init__(name, salary=___)\n        self.duration = duration\n    def get_duration(self):\n        return f'{self.name} interns for {self.duration} months'\n\nprint(Manager('Tunde',500000,8).get_info())\nprint(Intern('Amaka',6).get_info())\nprint(Intern('Amaka',6).get_duration())",
      solution: "class Employee:\n    def __init__(self,name,salary):\n        self.name=name;self.salary=salary\n    def get_info(self):\n        return f'{self.name} | N{self.salary}'\nclass Manager(Employee):\n    def __init__(self,name,salary,team_size):\n        super().__init__(name,salary)\n        self.team_size=team_size\n    def get_info(self):\n        return super().get_info()+f' | Team:{self.team_size}'\nclass Intern(Employee):\n    def __init__(self,name,duration):\n        super().__init__(name,salary=50000)\n        self.duration=duration\n    def get_duration(self):\n        return f'{self.name} interns for {self.duration} months'\nprint(Manager('Tunde',500000,8).get_info())\nprint(Intern('Amaka',6).get_info())\nprint(Intern('Amaka',6).get_duration())",
      hint: "super().__init__() calls parent. Override get_info in Manager.",
      rubric: "Both inherit. super().__init__(). Manager overrides. Intern defaults salary."
    },
    {
      title: "Dunder Methods",
      theory: "## Magic Methods\n```python\nclass Book:\n    def __init__(self, title, pages):\n        self.title=title; self.pages=pages\n    def __str__(self):  return f'Book: {self.title}'\n    def __len__(self):  return self.pages\n    def __repr__(self): return f'Book({self.title!r})'\n```",
      instructions: "## Task: Vector Class\nCreate `Vector(x, y)` with:\n- `__str__` → `Vector(3, 4)`\n- `__add__` → adds two vectors\n- `__len__` → magnitude as int\n- `__eq__` → True if x and y equal",
      starterCode: "import math\n\nclass Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __str__(self):\n        return f'Vector({self.___}, {self.___})'\n    def __add__(self, other):\n        return Vector(self.x + ___.x, self.y + ___.y)\n    def __len__(self):\n        return int(math.sqrt(self.x**2 + ___))\n    def __eq__(self, other):\n        return self.x == ___.x and self.y == ___.y\n\nv1 = Vector(3, 4)\nv2 = Vector(1, 2)\nprint(v1)\nprint(v1 + v2)\nprint(len(v1))    # 5\nprint(v1 == v2)   # False",
      solution: "import math\nclass Vector:\n    def __init__(self,x,y):\n        self.x=x;self.y=y\n    def __str__(self):\n        return f'Vector({self.x},{self.y})'\n    def __add__(self,other):\n        return Vector(self.x+other.x,self.y+other.y)\n    def __len__(self):\n        return int(math.sqrt(self.x**2+self.y**2))\n    def __eq__(self,other):\n        return self.x==other.x and self.y==other.y\nv1=Vector(3,4);v2=Vector(1,2)\nprint(v1)\nprint(v1+v2)\nprint(len(v1))\nprint(v1==v2)",
      hint: "__add__ returns new Vector. __len__ uses math.sqrt.",
      rubric: "All 4 dunders correct. __add__ returns Vector. __len__ returns int."
    },
    {
      title: "Class & Static Methods",
      theory: "## Class & Static Methods\n```python\nclass MathHelper:\n    pi = 3.14159\n\n    @classmethod\n    def circle_area(cls, r):\n        return cls.pi * r**2\n\n    @staticmethod\n    def add(a, b):\n        return a + b\n```",
      instructions: "## Task: Student Factory\n- Class var `school = 'Mabel Academy'`\n- `@classmethod from_string(cls, data)` — parses `'Ada,22,Python'`\n- `@staticmethod is_passing(score)` — True if score >= 60",
      starterCode: "class Student:\n    school = 'Mabel Academy'\n\n    def __init__(self, name, age, course):\n        self.name = name\n        self.age = age\n        self.course = course\n\n    def __str__(self):\n        return f'{self.name} ({self.course}) @ {Student.___}'\n\n    @classmethod\n    def from_string(cls, data):\n        name, age, course = data.split(___)\n        return cls(name, int(___), course)\n\n    @staticmethod\n    def is_passing(score):\n        return score >= ___\n\nada = Student('Ada', 22, 'Python')\nprint(ada)\ntunde = Student.from_string('Tunde,25,FastAPI')\nprint(tunde)\nprint(Student.is_passing(75))\nprint(Student.is_passing(45))",
      solution: "class Student:\n    school='Mabel Academy'\n    def __init__(self,name,age,course):\n        self.name=name;self.age=age;self.course=course\n    def __str__(self):\n        return f'{self.name} ({self.course}) @ {Student.school}'\n    @classmethod\n    def from_string(cls,data):\n        name,age,course=data.split(',')\n        return cls(name,int(age),course)\n    @staticmethod\n    def is_passing(score):\n        return score>=60\nada=Student('Ada',22,'Python')\nprint(ada)\ntunde=Student.from_string('Tunde,25,FastAPI')\nprint(tunde)\nprint(Student.is_passing(75))\nprint(Student.is_passing(45))",
      hint: "split(',') for CSV. @classmethod gets cls. @staticmethod gets no self/cls.",
      rubric: "school class var. from_string parses and constructs. is_passing correct."
    }
  ]
},

"File Handling & Exceptions": {
  aiRubric: "Check open/with, read/write modes, try/except/finally.",
  lessons: [
    {
      title: "Reading & Writing Files",
      theory: "## Files\n```python\n# Write\nwith open('data.txt', 'w') as f:\n    f.write('Hello Ada!\\n')\n\n# Read all at once\nwith open('data.txt', 'r') as f:\n    content = f.read()\n\n# Read line by line\nwith open('data.txt') as f:\n    for line in f:\n        print(line.strip())\n```",
      instructions: "## Task: Student Log\n1. Write 3 student records to `students.txt` (name,score per line)\n2. Read back and print: `Ada scored 88`",
      starterCode: "with open('students.txt', ___) as f:\n    f.write('Ada,88\\n')\n    f.write('Tunde,72\\n')\n    f.write('Ngozi,95\\n')\n\nwith open('students.txt', ___) as f:\n    for line in f:\n        parts = line.strip().split(___)\n        name  = parts[___]\n        score = parts[___]\n        print(f'{name} scored {score}')",
      solution: "with open('students.txt','w') as f:\n    f.write('Ada,88\\n')\n    f.write('Tunde,72\\n')\n    f.write('Ngozi,95\\n')\nwith open('students.txt','r') as f:\n    for line in f:\n        parts=line.strip().split(',')\n        name=parts[0]\n        score=parts[1]\n        print(f'{name} scored {score}')",
      hint: "'w' to write, 'r' to read. split(',') splits by comma.",
      rubric: "Write mode 'w'. Read mode 'r'. split(',') used. Indices correct."
    },
    {
      title: "Try / Except / Finally",
      theory: "## Exception Handling\n```python\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nexcept ValueError as e:\n    print(f'Bad value: {e}')\nelse:\n    print('Success!')\nfinally:\n    print('Always runs')\n```",
      instructions: "## Task: Safe Calculator\nWrite `safe_divide(a, b)` that:\n1. Catches ZeroDivisionError\n2. Catches TypeError\n3. Returns result on success, None on error\n4. Always prints 'Done' in finally",
      starterCode: "def safe_divide(a, b):\n    try:\n        result = a / b\n    except ___:\n        print('Error: Cannot divide by zero')\n        return None\n    except ___:\n        print('Error: Inputs must be numbers')\n        return None\n    else:\n        return ___\n    finally:\n        print('Done')\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))\nprint(safe_divide('ten', 2))",
      solution: "def safe_divide(a,b):\n    try:\n        result=a/b\n    except ZeroDivisionError:\n        print('Error: Cannot divide by zero')\n        return None\n    except TypeError:\n        print('Error: Inputs must be numbers')\n        return None\n    else:\n        return result\n    finally:\n        print('Done')\nprint(safe_divide(10,2))\nprint(safe_divide(10,0))\nprint(safe_divide('ten',2))",
      hint: "ZeroDivisionError for /0. TypeError for wrong types. else runs if no exception.",
      rubric: "Both except clauses correct. else returns result. finally always prints."
    },
    {
      title: "Custom Exceptions",
      theory: "## Custom Exceptions\n```python\nclass InsufficientFundsError(Exception):\n    def __init__(self, amount, balance):\n        self.amount = amount\n        self.balance = balance\n        super().__init__(f'Need N{amount}, have N{balance}')\n\nraise InsufficientFundsError(5000, 2000)\n```",
      instructions: "## Task: Bank Exceptions\nCreate:\n1. `InsufficientFundsError(amount, balance)` — custom exception\n2. `InvalidAmountError` — raised if amount <= 0\n3. Update `BankAccount.withdraw()` to raise these\n4. Catch them separately in a try/except",
      starterCode: "class InsufficientFundsError(Exception):\n    def __init__(self, amount, balance):\n        super().__init__(f'Need N{amount} but balance is N{balance}')\n\nclass InvalidAmountError(Exception):\n    def __init__(self, amount):\n        super().__init__(f'Invalid amount: N{amount}')\n\nclass BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n\n    def withdraw(self, amount):\n        if amount <= 0:\n            raise ___(amount)\n        if amount > self.balance:\n            raise ___(amount, self.balance)\n        self.balance -= amount\n        return self.balance\n\nacc = BankAccount('Ada', 5000)\ntry:\n    acc.withdraw(2000)\n    print(f'Balance: N{acc.balance}')\n    acc.withdraw(10000)\nexcept ___ as e:\n    print(f'Funds error: {e}')\nexcept ___ as e:\n    print(f'Amount error: {e}')",
      solution: "class InsufficientFundsError(Exception):\n    def __init__(self,amount,balance):\n        super().__init__(f'Need N{amount} but balance is N{balance}')\nclass InvalidAmountError(Exception):\n    def __init__(self,amount):\n        super().__init__(f'Invalid amount: N{amount}')\nclass BankAccount:\n    def __init__(self,owner,balance=0):\n        self.owner=owner;self.balance=balance\n    def withdraw(self,amount):\n        if amount<=0:\n            raise InvalidAmountError(amount)\n        if amount>self.balance:\n            raise InsufficientFundsError(amount,self.balance)\n        self.balance-=amount\n        return self.balance\nacc=BankAccount('Ada',5000)\ntry:\n    acc.withdraw(2000)\n    print(f'Balance: N{acc.balance}')\n    acc.withdraw(10000)\nexcept InsufficientFundsError as e:\n    print(f'Funds error: {e}')\nexcept InvalidAmountError as e:\n    print(f'Amount error: {e}')",
      hint: "Inherit from Exception. Call super().__init__(message). raise ExceptionClass(args).",
      rubric: "Both custom exceptions. Correct raises in withdraw. Both caught separately."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// BACKEND — INTERMEDIATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"REST APIs with FastAPI": {
  aiRubric: "Check decorators, Pydantic, path/query params, HTTPException.",
  lessons: [
    {
      title: "Your First FastAPI App",
      theory: "## FastAPI\n```python\nfrom fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': 'Hello!'}\n```\nRun: `uvicorn main:app --reload`\nDocs: `http://localhost:8000/docs`",
      instructions: "## Task: Student API\n1. GET / → `{message, version}`\n2. GET /student/{name} → `{student, status}`",
      starterCode: "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': ___, 'version': ___}\n\n@app.get('/student/{name}')\ndef get_student(name: ___):\n    return {'student': name, 'status': 'enrolled'}",
      solution: "from fastapi import FastAPI\napp=FastAPI()\n@app.get('/')\ndef root():\n    return {'message':'Mabel Academy API','version':'1.0'}\n@app.get('/student/{name}')\ndef get_student(name:str):\n    return {'student':name,'status':'enrolled'}",
      hint: "Path params in {curly braces} in URL and as function params.",
      rubric: "Both endpoints. Path param correct. Both return dicts."
    },
    {
      title: "POST with Pydantic",
      theory: "## Request Body\n```python\nfrom pydantic import BaseModel\n\nclass Item(BaseModel):\n    name: str\n    price: float\n    in_stock: bool = True\n\n@app.post('/items/')\ndef create(item: Item):\n    return {'created': item.name}\n```",
      instructions: "## Task: Enrollment Endpoint\nCreate `EnrollmentRequest(student_name, course, level='Beginner')`\nPOST /enroll → enrolled=True, student, course, welcome message",
      starterCode: "from fastapi import FastAPI\nfrom pydantic import BaseModel\napp = FastAPI()\n\nclass EnrollmentRequest(BaseModel):\n    student_name: ___\n    course: ___\n    level: str = ___\n\n@app.post('/enroll')\ndef enroll(req: EnrollmentRequest):\n    return {\n        'enrolled': True,\n        'student': req.___,\n        'course': req.___,\n        'message': f'Welcome to {req.course}!'\n    }",
      solution: "from fastapi import FastAPI\nfrom pydantic import BaseModel\napp=FastAPI()\nclass EnrollmentRequest(BaseModel):\n    student_name:str\n    course:str\n    level:str='Beginner'\n@app.post('/enroll')\ndef enroll(req:EnrollmentRequest):\n    return {'enrolled':True,'student':req.student_name,'course':req.course,'message':f'Welcome to {req.course}!'}",
      hint: "Fields need type hints. Access with req.field_name.",
      rubric: "BaseModel used. 3 fields typed. Default level. Fields accessed."
    },
    {
      title: "HTTP Errors & CRUD",
      theory: "## HTTPException\n```python\nfrom fastapi import HTTPException\n\n@app.get('/item/{id}')\ndef get(id: int):\n    if id not in db:\n        raise HTTPException(404, 'Not found')\n    return db[id]\n```",
      instructions: "## Task: Student CRUD\n`students = {1:'Ada', 2:'Tunde'}`\n1. GET /students/{id} — 404 if missing\n2. POST /students/ — 400 if ID exists\n3. DELETE /students/{id} — 404 if missing",
      starterCode: "from fastapi import FastAPI, HTTPException\napp = FastAPI()\nstudents = {1:'Ada', 2:'Tunde'}\n\n@app.get('/students/{sid}')\ndef get_student(sid: int):\n    if sid not in ___:\n        raise HTTPException(status_code=___, detail='Not found')\n    return {'id':sid,'name':students[sid]}\n\n@app.post('/students/', status_code=201)\ndef add_student(sid: int, name: str):\n    if sid in ___:\n        raise HTTPException(status_code=___, detail='ID exists')\n    students[sid] = name\n    return {'created': name}\n\n@app.delete('/students/{sid}')\ndef delete_student(sid: int):\n    if sid not in students:\n        raise HTTPException(status_code=404, detail='Not found')\n    del students[___]\n    return {'deleted': sid}",
      solution: "from fastapi import FastAPI,HTTPException\napp=FastAPI()\nstudents={1:'Ada',2:'Tunde'}\n@app.get('/students/{sid}')\ndef get_student(sid:int):\n    if sid not in students:\n        raise HTTPException(status_code=404,detail='Not found')\n    return {'id':sid,'name':students[sid]}\n@app.post('/students/',status_code=201)\ndef add_student(sid:int,name:str):\n    if sid in students:\n        raise HTTPException(status_code=400,detail='ID exists')\n    students[sid]=name\n    return {'created':name}\n@app.delete('/students/{sid}')\ndef delete_student(sid:int):\n    if sid not in students:\n        raise HTTPException(status_code=404,detail='Not found')\n    del students[sid]\n    return {'deleted':sid}",
      hint: "raise HTTPException(status_code=404). Check 'in students' first.",
      rubric: "404 for missing. 400 for duplicates. All 3 endpoints work."
    },
    {
      title: "Query Params & Validation",
      theory: "## Query Parameters\n```python\nfrom fastapi import Query\n\n@app.get('/students/')\ndef list_students(skip:int=0, limit:int=10):\n    return data[skip:skip+limit]\n\n@app.get('/search')\ndef search(q: str = Query(min_length=2)):\n    ...\n```",
      instructions: "## Task: Paginated Courses\n1. In-memory list of 10 courses\n2. GET /courses/ with skip=0, limit=5\n3. GET /courses/search with required `q` param (min 2 chars)",
      starterCode: "from fastapi import FastAPI, Query\napp = FastAPI()\ncourses = ['Python','FastAPI','SQL','React','Docker','ML','AI','Git','Linux','Testing']\n\n@app.get('/courses/')\ndef list_courses(skip: int = ___, limit: int = ___):\n    return courses[___: ___ + ___]\n\n@app.get('/courses/search')\ndef search(q: str = Query(min_length=___)):\n    results = [c for c in courses if ___.lower() in c.lower()]\n    return {'query':q,'results':results,'count':len(results)}",
      solution: "from fastapi import FastAPI,Query\napp=FastAPI()\ncourses=['Python','FastAPI','SQL','React','Docker','ML','AI','Git','Linux','Testing']\n@app.get('/courses/')\ndef list_courses(skip:int=0,limit:int=5):\n    return courses[skip:skip+limit]\n@app.get('/courses/search')\ndef search(q:str=Query(min_length=2)):\n    results=[c for c in courses if q.lower() in c.lower()]\n    return {'query':q,'results':results,'count':len(results)}",
      hint: "Slice: courses[skip:skip+limit]. q.lower() in c.lower() for case-insensitive search.",
      rubric: "Defaults 0 and 5. Slice correct. Search filters. min_length=2."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// DJANGO
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Django Web Framework": {
  aiRubric: "Check Django views, urls, models, ORM queries, CBVs.",
  lessons: [
    {
      title: "First Django View & URL",
      theory: "## Django Setup\n```bash\npip install django\ndjango-admin startproject mysite\npython manage.py startapp students\npython manage.py runserver\n```\n**Key files:** views.py, urls.py, models.py, settings.py",
      instructions: "## Task: Django Views\n1. `home` view → HttpResponse welcome message\n2. `about` view → instructor info\n3. `student_detail(request, name)` → greeting\n4. Wire all 3 to URLs",
      starterCode: "# views.py\nfrom django.http import HttpResponse\n\ndef home(request):\n    return HttpResponse(___)\n\ndef about(request):\n    return HttpResponse('Instructor: Ada | Mabel Academy')\n\ndef student_detail(request, name):\n    return HttpResponse(f'Student: {___}')\n\n# urls.py\nfrom django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path('', views.___, name='home'),\n    path('about/', views.___, name='about'),\n    path('student/<str:name>/', views.___, name='student-detail'),\n]",
      solution: "# views.py\nfrom django.http import HttpResponse\ndef home(request):\n    return HttpResponse('Welcome to Mabel Academy!')\ndef about(request):\n    return HttpResponse('Instructor: Ada | Mabel Academy')\ndef student_detail(request,name):\n    return HttpResponse(f'Student: {name}')\n# urls.py\nfrom django.urls import path\nfrom . import views\nurlpatterns=[\n    path('',views.home,name='home'),\n    path('about/',views.about,name='about'),\n    path('student/<str:name>/',views.student_detail,name='student-detail'),\n]",
      hint: "HttpResponse wraps string. path() takes url, view, name. <str:name> captures URL param.",
      rubric: "3 views defined. URLs mapped. Path parameter used."
    },
    {
      title: "Django Models",
      theory: "## Models\n```python\nfrom django.db import models\n\nclass Student(models.Model):\n    name    = models.CharField(max_length=100)\n    email   = models.EmailField(unique=True)\n    score   = models.IntegerField(default=0)\n    created = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return self.name\n\n    class Meta:\n        ordering = ['-score']\n```\nRun: `makemigrations` then `migrate`",
      instructions: "## Task: Course Model\nCreate `Course` with:\n- `title` (CharField max 200)\n- `description` (TextField)\n- `level` (CharField with choices: Beginner/Intermediate/Advanced)\n- `price` (DecimalField, 2dp)\n- `is_active` (BooleanField, default True)\n- `__str__` returning title, Meta ordering by title",
      starterCode: "from django.db import models\n\nclass Course(models.Model):\n    LEVEL_CHOICES = [\n        ('BEG', ___),\n        ('INT', 'Intermediate'),\n        ('ADV', ___),\n    ]\n\n    title       = models.CharField(max_length=___)\n    description = models.___Field()\n    level       = models.CharField(max_length=3, choices=___, default='BEG')\n    price       = models.DecimalField(max_digits=8, decimal_places=___)\n    is_active   = models.BooleanField(default=___)\n    created_at  = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return ___\n\n    class Meta:\n        ordering = [___]",
      solution: "from django.db import models\nclass Course(models.Model):\n    LEVEL_CHOICES=[('BEG','Beginner'),('INT','Intermediate'),('ADV','Advanced')]\n    title=models.CharField(max_length=200)\n    description=models.TextField()\n    level=models.CharField(max_length=3,choices=LEVEL_CHOICES,default='BEG')\n    price=models.DecimalField(max_digits=8,decimal_places=2)\n    is_active=models.BooleanField(default=True)\n    created_at=models.DateTimeField(auto_now_add=True)\n    def __str__(self):\n        return self.title\n    class Meta:\n        ordering=['title']",
      hint: "TextField for long text. DecimalField needs decimal_places=2. ordering=['title'] for A-Z.",
      rubric: "All 5 fields correct. LEVEL_CHOICES defined. __str__ returns title. Meta ordering."
    },
    {
      title: "Django ORM Queries",
      theory: "## ORM\n```python\nStudent.objects.create(name='Ada', score=88)\nStudent.objects.all()\nStudent.objects.get(id=1)\nStudent.objects.filter(score__gte=80)\nStudent.objects.order_by('-score')[:5]\nStudent.objects.filter(score__lt=40).delete()\n```",
      instructions: "## Task: ORM Practice\n1. Get students with score >= 70\n2. Get top 3 by score\n3. Count per course using `values()` + `annotate()`\n4. Update all scores < 50 to 50\n5. get_or_create a student",
      starterCode: "from django.db.models import Count\n\n# 1. Score >= 70\npassing = Student.objects.filter(score___70)\n\n# 2. Top 3\ntop3 = Student.objects.order_by(___)[___]\n\n# 3. Count per course\nper_course = Student.objects.values(___).annotate(count=Count('id'))\n\n# 4. Update minimums\nStudent.objects.filter(score___50).update(score=50)\n\n# 5. Get or create\nstudent, created = Student.objects.get_or_create(\n    name=___,\n    defaults={'score': 0}\n)\nprint(f'Created: {created}')",
      solution: "from django.db.models import Count\npassing=Student.objects.filter(score__gte=70)\ntop3=Student.objects.order_by('-score')[:3]\nper_course=Student.objects.values('course').annotate(count=Count('id'))\nStudent.objects.filter(score__lt=50).update(score=50)\nstudent,created=Student.objects.get_or_create(name='New Student',defaults={'score':0})\nprint(f'Created:{created}')",
      hint: "filter(score__gte=70). order_by('-score')[:3]. __lt for less than.",
      rubric: "gte/lt lookups. Negative order_by. Slice [:3]. annotate Count. get_or_create."
    },
    {
      title: "Django Class-Based Views",
      theory: "## CBVs\n```python\nfrom django.views.generic import ListView, DetailView, CreateView\nfrom django.urls import reverse_lazy\n\nclass StudentListView(ListView):\n    model = Student\n    template_name = 'students/list.html'\n    context_object_name = 'students'\n\nclass StudentCreateView(CreateView):\n    model = Student\n    fields = ['name','email','course']\n    success_url = reverse_lazy('student-list')\n```",
      instructions: "## Task: Course CBVs\n1. `CourseListView` — filter is_active=True in get_queryset\n2. `CourseDetailView`\n3. `CourseCreateView` — fields: title, description, level, price",
      starterCode: "from django.views.generic import ListView, DetailView, CreateView\nfrom django.urls import reverse_lazy\nfrom .models import Course\n\nclass CourseListView(___):\n    model = ___\n    template_name = 'courses/list.html'\n    context_object_name = 'courses'\n\n    def get_queryset(self):\n        return Course.objects.filter(is_active=___)\n\nclass CourseDetailView(___):\n    model = Course\n    template_name = 'courses/detail.html'\n\nclass CourseCreateView(___):\n    model = Course\n    fields = [___, ___, ___, ___]\n    success_url = reverse_lazy(___)",
      solution: "from django.views.generic import ListView,DetailView,CreateView\nfrom django.urls import reverse_lazy\nfrom .models import Course\nclass CourseListView(ListView):\n    model=Course\n    template_name='courses/list.html'\n    context_object_name='courses'\n    def get_queryset(self):\n        return Course.objects.filter(is_active=True)\nclass CourseDetailView(DetailView):\n    model=Course\n    template_name='courses/detail.html'\nclass CourseCreateView(CreateView):\n    model=Course\n    fields=['title','description','level','price']\n    success_url=reverse_lazy('course-list')",
      hint: "Inherit from correct generic view. get_queryset overrides default.",
      rubric: "All 3 CBVs correct base. get_queryset filters. fields list. success_url."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// FLASK
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Flask Microframework": {
  aiRubric: "Check Flask app, routes, request, jsonify, error codes.",
  lessons: [
    {
      title: "Your First Flask App",
      theory: "## Flask\n```python\nfrom flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, Mabel Academy!'\n\n@app.route('/greet/<name>')\ndef greet(name):\n    return f'Hello, {name}!'\n\nif __name__ == '__main__':\n    app.run(debug=True)\n```\nInstall: `pip install flask`",
      instructions: "## Task: Flask Student API\n1. `/` → welcome message\n2. `/student/<name>` → greeting\n3. `/students/` → JSON list of 3 students\n4. Run in debug mode",
      starterCode: "from flask import Flask, jsonify\napp = Flask(___)\n\n@app.route('/')\ndef home():\n    return ___\n\n@app.route('/student/<___>')\ndef greet(name):\n    return f'Welcome, {name}!'\n\n@app.route('/students/')\ndef list_students():\n    students = ['Ada','Tunde','Ngozi']\n    return jsonify({___: students, ___: len(students)})\n\nif __name__ == '__main__':\n    app.run(debug=___)",
      solution: "from flask import Flask,jsonify\napp=Flask(__name__)\n@app.route('/')\ndef home():\n    return 'Welcome to Mabel Academy!'\n@app.route('/student/<name>')\ndef greet(name):\n    return f'Welcome, {name}!'\n@app.route('/students/')\ndef list_students():\n    students=['Ada','Tunde','Ngozi']\n    return jsonify({'students':students,'count':len(students)})\nif __name__=='__main__':\n    app.run(debug=True)",
      hint: "Flask(__name__). @app.route(). jsonify() returns JSON response.",
      rubric: "Flask(__name__). 3 routes. jsonify used. debug=True."
    },
    {
      title: "Flask POST & Validation",
      theory: "## POST Request\n```python\nfrom flask import request, jsonify\n\n@app.route('/login', methods=['POST'])\ndef login():\n    data = request.get_json()\n    username = data.get('username')\n    if username == 'ada':\n        return jsonify({'success': True}), 200\n    return jsonify({'error': 'Invalid'}), 401\n```",
      instructions: "## Task: Student Registration\nBuild POST `/register`:\n1. Accepts JSON `{name, email, course}`\n2. Validates all fields present (400 if missing)\n3. Stores in in-memory list\n4. Returns `{id, name, message}` with 201\n5. GET `/students/` returns all",
      starterCode: "from flask import Flask, request, jsonify\napp = Flask(__name__)\nstudents = []\n\n@app.route('/register', methods=[___])\ndef register():\n    data = request.___()\n    name   = data.get(___)\n    email  = data.get(___)\n    course = data.get(___)\n\n    if not name or not email or not course:\n        return jsonify({'error': 'All fields required'}), ___\n\n    student = {'id': len(students)+1, 'name':name, 'email':email, 'course':course}\n    students.append(___)\n    return jsonify({'id':student['id'],'name':name,'message':'Registered!'}), ___\n\n@app.route('/students/')\ndef get_students():\n    return jsonify({'students': ___, 'count': len(students)})\n\nif __name__ == '__main__':\n    app.run(debug=True)",
      solution: "from flask import Flask,request,jsonify\napp=Flask(__name__)\nstudents=[]\n@app.route('/register',methods=['POST'])\ndef register():\n    data=request.get_json()\n    name=data.get('name')\n    email=data.get('email')\n    course=data.get('course')\n    if not name or not email or not course:\n        return jsonify({'error':'All fields required'}),400\n    student={'id':len(students)+1,'name':name,'email':email,'course':course}\n    students.append(student)\n    return jsonify({'id':student['id'],'name':name,'message':'Registered!'}),201\n@app.route('/students/')\ndef get_students():\n    return jsonify({'students':students,'count':len(students)})\nif __name__=='__main__':\n    app.run(debug=True)",
      hint: "request.get_json() parses body. Return (jsonify(...), status_code). 400 bad data, 201 created.",
      rubric: "POST method. get_json(). Validation. 400/201 codes. students list updated."
    },
    {
      title: "Flask Blueprints",
      theory: "## Blueprints\n```python\n# students/routes.py\nfrom flask import Blueprint\nstudents_bp = Blueprint('students', __name__, url_prefix='/students')\n\n@students_bp.route('/')\ndef list(): return 'All students'\n\n# app.py\napp.register_blueprint(students_bp)\n```",
      instructions: "## Task: Modular App\n1. `students_bp` prefix `/students` — GET `/` lists, GET `/<id>` returns one\n2. `courses_bp` prefix `/courses` — GET `/` lists\n3. Register both on main app",
      starterCode: "from flask import Flask, Blueprint, jsonify\n\nstudents_bp = Blueprint(___, __name__, url_prefix=___)\nstudents_data = [{'id':1,'name':'Ada'},{'id':2,'name':'Tunde'}]\n\n@students_bp.route('/')\ndef list_students():\n    return jsonify(students_data)\n\n@students_bp.route('/<int:sid>')\ndef get_student(sid):\n    student = next((s for s in students_data if s['id'] == ___), None)\n    if not student:\n        return jsonify({'error':'Not found'}), 404\n    return jsonify(___)\n\ncourses_bp = Blueprint(___, __name__, url_prefix='/courses')\ncourses_data = [{'id':1,'title':'Python'},{'id':2,'title':'FastAPI'}]\n\n@courses_bp.route('/')\ndef list_courses():\n    return jsonify(___)\n\napp = Flask(__name__)\napp.register_blueprint(___)\napp.register_blueprint(___)\n\nif __name__ == '__main__':\n    app.run(debug=True)",
      solution: "from flask import Flask,Blueprint,jsonify\nstudents_bp=Blueprint('students',__name__,url_prefix='/students')\nstudents_data=[{'id':1,'name':'Ada'},{'id':2,'name':'Tunde'}]\n@students_bp.route('/')\ndef list_students():\n    return jsonify(students_data)\n@students_bp.route('/<int:sid>')\ndef get_student(sid):\n    student=next((s for s in students_data if s['id']==sid),None)\n    if not student:\n        return jsonify({'error':'Not found'}),404\n    return jsonify(student)\ncourses_bp=Blueprint('courses',__name__,url_prefix='/courses')\ncourses_data=[{'id':1,'title':'Python'},{'id':2,'title':'FastAPI'}]\n@courses_bp.route('/')\ndef list_courses():\n    return jsonify(courses_data)\napp=Flask(__name__)\napp.register_blueprint(students_bp)\napp.register_blueprint(courses_bp)\nif __name__=='__main__':\n    app.run(debug=True)",
      hint: "Blueprint('name',__name__,url_prefix='/prefix'). register_blueprint() on app.",
      rubric: "Both blueprints. url_prefix set. Routes correct. Both registered."
    },
    {
      title: "Flask with SQLAlchemy",
      theory: "## Flask-SQLAlchemy\n```python\nfrom flask_sqlalchemy import SQLAlchemy\n\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'\ndb = SQLAlchemy(app)\n\nclass Student(db.Model):\n    id   = db.Column(db.Integer, primary_key=True)\n    name = db.Column(db.String(100), nullable=False)\n\n    def to_dict(self):\n        return {'id':self.id,'name':self.name}\n```",
      instructions: "## Task: Persistent Student DB\n1. `Student(id, name, email, course, score)` model\n2. POST `/students/` creates student\n3. GET `/students/` lists all\n4. GET `/students/<id>` gets one or 404\n5. DELETE `/students/<id>` deletes",
      starterCode: "from flask import Flask, request, jsonify\nfrom flask_sqlalchemy import SQLAlchemy\n\napp = Flask(__name__)\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'\ndb = SQLAlchemy(app)\n\nclass Student(db.Model):\n    id     = db.Column(db.Integer, primary_key=True)\n    name   = db.Column(db.String(100), nullable=___)\n    email  = db.Column(db.String(120), unique=___)\n    course = db.Column(db.String(50))\n    score  = db.Column(db.Integer, default=___)\n\n    def to_dict(self):\n        return {'id':self.id,'name':self.name,'email':self.email,'course':self.course}\n\n@app.route('/students/', methods=['GET','POST'])\ndef students():\n    if request.method == 'POST':\n        d = request.get_json()\n        s = Student(name=d[___], email=d[___], course=d.get('course','Python'))\n        db.session.___(s)\n        db.session.commit()\n        return jsonify(s.to_dict()), 201\n    return jsonify([s.to_dict() for s in Student.query.all()])\n\n@app.route('/students/<int:sid>', methods=['GET','DELETE'])\ndef student_detail(sid):\n    s = Student.query.get_or_404(___)\n    if request.method == 'DELETE':\n        db.session.___(s)\n        db.session.commit()\n        return jsonify({'deleted':sid})\n    return jsonify(s.to_dict())\n\nwith app.app_context():\n    db.create_all()\n\nif __name__ == '__main__':\n    app.run(debug=True)",
      solution: "from flask import Flask,request,jsonify\nfrom flask_sqlalchemy import SQLAlchemy\napp=Flask(__name__)\napp.config['SQLALCHEMY_DATABASE_URI']='sqlite:///school.db'\ndb=SQLAlchemy(app)\nclass Student(db.Model):\n    id=db.Column(db.Integer,primary_key=True)\n    name=db.Column(db.String(100),nullable=False)\n    email=db.Column(db.String(120),unique=True)\n    course=db.Column(db.String(50))\n    score=db.Column(db.Integer,default=0)\n    def to_dict(self):\n        return {'id':self.id,'name':self.name,'email':self.email,'course':self.course}\n@app.route('/students/',methods=['GET','POST'])\ndef students():\n    if request.method=='POST':\n        d=request.get_json()\n        s=Student(name=d['name'],email=d['email'],course=d.get('course','Python'))\n        db.session.add(s)\n        db.session.commit()\n        return jsonify(s.to_dict()),201\n    return jsonify([s.to_dict() for s in Student.query.all()])\n@app.route('/students/<int:sid>',methods=['GET','DELETE'])\ndef student_detail(sid):\n    s=Student.query.get_or_404(sid)\n    if request.method=='DELETE':\n        db.session.delete(s)\n        db.session.commit()\n        return jsonify({'deleted':sid})\n    return jsonify(s.to_dict())\nwith app.app_context():\n    db.create_all()\nif __name__=='__main__':\n    app.run(debug=True)",
      hint: "db.session.add() then commit(). get_or_404() returns 404 if not found.",
      rubric: "Model fields correct. session.add/commit. get_or_404. DELETE uses session.delete."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// BACKEND — ADVANCED
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Django REST Framework": {
  aiRubric: "Check DRF serializers, viewsets, routers, permissions.",
  lessons: [
    {
      title: "DRF Serializers",
      theory: "## Serializers\n```python\nfrom rest_framework import serializers\nfrom .models import Student\n\nclass StudentSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Student\n        fields = ['id','name','email','score']\n        read_only_fields = ['id']\n```\nInstall: `pip install djangorestframework`\nAdd `'rest_framework'` to INSTALLED_APPS.",
      instructions: "## Task: Course Serializer\nCreate `CourseSerializer` with:\n1. All fields\n2. `id` and `created_at` read-only\n3. `validate_price` — price must be > 0\n4. `SerializerMethodField` for `student_count`",
      starterCode: "from rest_framework import serializers\nfrom .models import Course\n\nclass CourseSerializer(serializers.ModelSerializer):\n    student_count = serializers.___(method_name='get_student_count')\n\n    class Meta:\n        model = ___\n        fields = ___\n        read_only_fields = ['id', ___]\n\n    def validate_price(self, value):\n        if value <= ___:\n            raise serializers.ValidationError('Price must be greater than 0')\n        return value\n\n    def get_student_count(self, obj):\n        return obj.students.___()",
      solution: "from rest_framework import serializers\nfrom .models import Course\nclass CourseSerializer(serializers.ModelSerializer):\n    student_count=serializers.SerializerMethodField(method_name='get_student_count')\n    class Meta:\n        model=Course\n        fields='__all__'\n        read_only_fields=['id','created_at']\n    def validate_price(self,value):\n        if value<=0:\n            raise serializers.ValidationError('Price must be greater than 0')\n        return value\n    def get_student_count(self,obj):\n        return obj.students.count()",
      hint: "SerializerMethodField calls get_<field_name>. ValidationError for invalid data.",
      rubric: "SerializerMethodField. Meta fields. read_only_fields. validate_price. get_student_count."
    },
    {
      title: "DRF ViewSets & Routers",
      theory: "## ViewSets\n```python\nfrom rest_framework import viewsets\nfrom rest_framework.routers import DefaultRouter\n\nclass StudentViewSet(viewsets.ModelViewSet):\n    queryset = Student.objects.all()\n    serializer_class = StudentSerializer\n\nrouter = DefaultRouter()\nrouter.register('students', StudentViewSet)\nurlpatterns = router.urls\n```",
      instructions: "## Task: Course ViewSet\n1. `CourseViewSet` extending `ModelViewSet`\n2. get_queryset filters active courses\n3. Custom `@action` POST `/courses/{id}/enroll/`\n4. Register with router",
      starterCode: "from rest_framework import viewsets, permissions\nfrom rest_framework.decorators import action\nfrom rest_framework.response import Response\nfrom rest_framework.routers import DefaultRouter\nfrom .models import Course\nfrom .serializers import CourseSerializer\n\nclass CourseViewSet(viewsets.___):\n    serializer_class = CourseSerializer\n    permission_classes = [permissions.IsAuthenticatedOrReadOnly]\n\n    def get_queryset(self):\n        return Course.objects.filter(is_active=___)\n\n    @action(detail=___, methods=[___])\n    def enroll(self, request, pk=None):\n        course = self.get_object()\n        return Response({\n            'enrolled': True,\n            'course': course.___,\n            'student': request.user.___\n        })\n\nrouter = DefaultRouter()\nrouter.register(___, CourseViewSet, basename='course')\nurlpatterns = router.urls",
      solution: "from rest_framework import viewsets,permissions\nfrom rest_framework.decorators import action\nfrom rest_framework.response import Response\nfrom rest_framework.routers import DefaultRouter\nfrom .models import Course\nfrom .serializers import CourseSerializer\nclass CourseViewSet(viewsets.ModelViewSet):\n    serializer_class=CourseSerializer\n    permission_classes=[permissions.IsAuthenticatedOrReadOnly]\n    def get_queryset(self):\n        return Course.objects.filter(is_active=True)\n    @action(detail=True,methods=['post'])\n    def enroll(self,request,pk=None):\n        course=self.get_object()\n        return Response({'enrolled':True,'course':course.title,'student':request.user.username})\nrouter=DefaultRouter()\nrouter.register('courses',CourseViewSet,basename='course')\nurlpatterns=router.urls",
      hint: "ModelViewSet gives CRUD free. @action(detail=True) for per-object. router.register needs prefix.",
      rubric: "ModelViewSet. get_queryset filters. @action detail=True. router.register."
    }
  ]
},

"Flask Advanced Patterns": {
  aiRubric: "Check factory pattern, config, JWT auth, error handlers.",
  lessons: [
    {
      title: "Application Factory",
      theory: "## Factory Pattern\n```python\ndef create_app(config='development'):\n    app = Flask(__name__)\n    app.config.from_object(config)\n    db.init_app(app)\n    app.register_blueprint(main_bp)\n    return app\n```\nBenefit: multiple configs, easier testing.",
      instructions: "## Task: Flask Factory\n1. `create_app(config_name='development')` function\n2. Config dict with dev/prod settings\n3. Initialize db inside factory\n4. Register blueprint inside factory",
      starterCode: "from flask import Flask, Blueprint, jsonify\nfrom flask_sqlalchemy import SQLAlchemy\n\ndb = SQLAlchemy()\n\nCONFIG = {\n    'development': {'DEBUG': True,  'SQLALCHEMY_DATABASE_URI': 'sqlite:///dev.db'},\n    'production':  {'DEBUG': False, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///prod.db'}\n}\n\nmain_bp = Blueprint('main', __name__)\n\n@main_bp.route('/')\ndef index():\n    return jsonify({'status': 'ok'})\n\ndef create_app(config_name=___):\n    app = Flask(___)\n    app.config.update(CONFIG[___])\n    ___.init_app(app)\n    app.register_blueprint(___)\n    with app.app_context():\n        db.create_all()\n    return app\n\napp = create_app()\nif __name__ == '__main__':\n    app.run()",
      solution: "from flask import Flask,Blueprint,jsonify\nfrom flask_sqlalchemy import SQLAlchemy\ndb=SQLAlchemy()\nCONFIG={'development':{'DEBUG':True,'SQLALCHEMY_DATABASE_URI':'sqlite:///dev.db'},'production':{'DEBUG':False,'SQLALCHEMY_DATABASE_URI':'sqlite:///prod.db'}}\nmain_bp=Blueprint('main',__name__)\n@main_bp.route('/')\ndef index():\n    return jsonify({'status':'ok'})\ndef create_app(config_name='development'):\n    app=Flask(__name__)\n    app.config.update(CONFIG[config_name])\n    db.init_app(app)\n    app.register_blueprint(main_bp)\n    with app.app_context():\n        db.create_all()\n    return app\napp=create_app()\nif __name__=='__main__':\n    app.run()",
      hint: "db=SQLAlchemy() outside factory. db.init_app(app) inside. Blueprint registered inside.",
      rubric: "Factory function. CONFIG dict. db.init_app. Blueprint registered. app_context used."
    },
    {
      title: "Flask JWT Authentication",
      theory: "## Flask-JWT-Extended\n```python\nfrom flask_jwt_extended import (\n    JWTManager, create_access_token,\n    jwt_required, get_jwt_identity\n)\napp.config['JWT_SECRET_KEY'] = 'secret'\njwt = JWTManager(app)\n\n@app.route('/login', methods=['POST'])\ndef login():\n    token = create_access_token(identity='ada')\n    return jsonify(access_token=token)\n\n@app.route('/protected')\n@jwt_required()\ndef protected():\n    return jsonify(user=get_jwt_identity())\n```",
      instructions: "## Task: JWT Auth System\n1. POST `/login` — validates credentials, returns JWT\n2. POST `/register` — creates user in-memory\n3. GET `/profile` — requires JWT, returns user info",
      starterCode: "from flask import Flask, request, jsonify\nfrom flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity\n\napp = Flask(__name__)\napp.config['JWT_SECRET_KEY'] = 'mabel-secret-2024'\njwt = JWTManager(___)\n\nusers = {'ada': {'password':'pass123','course':'Python'}}\n\n@app.route('/register', methods=['POST'])\ndef register():\n    d = request.get_json()\n    if d['username'] in ___:\n        return jsonify({'error':'User exists'}), 400\n    users[d['username']] = {'password':d['password'],'course':d.get('course','Python')}\n    return jsonify({'message':'Registered'}), 201\n\n@app.route('/login', methods=['POST'])\ndef login():\n    d = request.get_json()\n    user = users.get(d.get('username'))\n    if not user or user['password'] != d.get('password'):\n        return jsonify({'error':'Invalid credentials'}), 401\n    token = create_access_token(identity=___)\n    return jsonify({'access_token': ___})\n\n@app.route('/profile')\n@___()\ndef profile():\n    username = get_jwt_identity()\n    return jsonify({'username':username,'course':users[username]['course']})\n\nif __name__ == '__main__':\n    app.run(debug=True)",
      solution: "from flask import Flask,request,jsonify\nfrom flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity\napp=Flask(__name__)\napp.config['JWT_SECRET_KEY']='mabel-secret-2024'\njwt=JWTManager(app)\nusers={'ada':{'password':'pass123','course':'Python'}}\n@app.route('/register',methods=['POST'])\ndef register():\n    d=request.get_json()\n    if d['username'] in users:\n        return jsonify({'error':'User exists'}),400\n    users[d['username']]={'password':d['password'],'course':d.get('course','Python')}\n    return jsonify({'message':'Registered'}),201\n@app.route('/login',methods=['POST'])\ndef login():\n    d=request.get_json()\n    user=users.get(d.get('username'))\n    if not user or user['password']!=d.get('password'):\n        return jsonify({'error':'Invalid credentials'}),401\n    token=create_access_token(identity=d['username'])\n    return jsonify({'access_token':token})\n@app.route('/profile')\n@jwt_required()\ndef profile():\n    username=get_jwt_identity()\n    return jsonify({'username':username,'course':users[username]['course']})\nif __name__=='__main__':\n    app.run(debug=True)",
      hint: "JWTManager(app). create_access_token(identity=username). @jwt_required() protects route.",
      rubric: "JWTManager init. create_access_token used. @jwt_required on profile. get_jwt_identity correct."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// SQL & DATABASES
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"SQL Fundamentals": {
  aiRubric: "Check valid SQL syntax, correct keywords.",
  lessons: [
    {
      title: "SELECT & FROM",
      theory: "## Basic SQL\n```sql\nSELECT column1, column2 FROM table;\nSELECT * FROM students;\nSELECT name AS student_name FROM students;\n```",
      instructions: "## Task: Query Students\nTable `students(id, name, age, course, score)`\n1. Select all\n2. Select name and course only\n3. Select with aliases: name AS student_name, score AS exam_score",
      starterCode: "-- 1. All students\n___ * ___ students;\n\n-- 2. Name and course\nSELECT ___, ___ FROM ___;\n\n-- 3. With aliases\nSELECT name ___ student_name, score ___ exam_score FROM ___;",
      solution: "SELECT * FROM students;\nSELECT name,course FROM students;\nSELECT name AS student_name,score AS exam_score FROM students;",
      hint: "SELECT then columns, FROM then table. AS for aliases.",
      rubric: "All 3 queries correct. AS used."
    },
    {
      title: "WHERE & Filtering",
      theory: "## Filtering\n```sql\nSELECT * FROM students WHERE score >= 70;\nSELECT * FROM students WHERE name LIKE 'A%';\nSELECT * FROM students WHERE score BETWEEN 60 AND 80;\nSELECT * FROM students WHERE course IN ('Python','SQL');\n```",
      instructions: "## Task: 4 Filter Queries\n1. Score >= 80\n2. Python course AND age < 25\n3. Name starts with 'A'\n4. Score between 60 and 79",
      starterCode: "-- 1.\nSELECT * FROM students WHERE score ___ 80;\n-- 2.\nSELECT * FROM students WHERE course = ___ ___ age < 25;\n-- 3.\nSELECT * FROM students WHERE name ___ 'A%';\n-- 4.\nSELECT * FROM students WHERE score ___ 60 ___ 79;",
      solution: "SELECT * FROM students WHERE score>=80;\nSELECT * FROM students WHERE course='Python' AND age<25;\nSELECT * FROM students WHERE name LIKE 'A%';\nSELECT * FROM students WHERE score BETWEEN 60 AND 79;",
      hint: "LIKE 'A%' starts with A. BETWEEN x AND y inclusive.",
      rubric: "All 4 queries. LIKE and BETWEEN used."
    },
    {
      title: "ORDER BY & LIMIT",
      theory: "## Sorting & Limiting\n```sql\nSELECT * FROM students ORDER BY score DESC;\nSELECT * FROM students ORDER BY score DESC LIMIT 3;\nSELECT * FROM students ORDER BY course ASC, score DESC;\n```",
      instructions: "## Task: Rankings\n1. All students by score descending\n2. Top 5\n3. By course A-Z then score highest within each",
      starterCode: "-- 1.\nSELECT * FROM students ORDER BY score ___;\n-- 2.\nSELECT * FROM students ORDER BY score DESC ___ 5;\n-- 3.\nSELECT * FROM students ORDER BY course ___, score ___;",
      solution: "SELECT * FROM students ORDER BY score DESC;\nSELECT * FROM students ORDER BY score DESC LIMIT 5;\nSELECT * FROM students ORDER BY course ASC,score DESC;",
      hint: "DESC for high-to-low. LIMIT after ORDER BY.",
      rubric: "DESC correct. LIMIT 5. Multi-sort ASC then DESC."
    },
    {
      title: "Aggregations & GROUP BY",
      theory: "## Aggregate Functions\n```sql\nSELECT COUNT(*), AVG(score), MAX(score), MIN(score) FROM students;\n\nSELECT course, AVG(score) AS avg\nFROM students\nGROUP BY course\nHAVING AVG(score) > 70;\n```",
      instructions: "## Task: Course Stats\n1. Count per course\n2. Average per course\n3. Courses with avg > 75\n4. Overall highest and lowest",
      starterCode: "-- 1.\nSELECT course, ___(*)  AS count FROM students ___ BY course;\n-- 2.\nSELECT course, ___(score) AS avg FROM students GROUP BY course;\n-- 3.\nSELECT course, AVG(score) FROM students GROUP BY course ___ AVG(score)>75;\n-- 4.\nSELECT ___(score) AS highest, ___(score) AS lowest FROM students;",
      solution: "SELECT course,COUNT(*) AS count FROM students GROUP BY course;\nSELECT course,AVG(score) AS avg FROM students GROUP BY course;\nSELECT course,AVG(score) FROM students GROUP BY course HAVING AVG(score)>75;\nSELECT MAX(score) AS highest,MIN(score) AS lowest FROM students;",
      hint: "COUNT(*) counts rows. HAVING filters groups (not WHERE).",
      rubric: "COUNT/AVG/MAX/MIN. GROUP BY. HAVING used."
    },
    {
      title: "JOINs",
      theory: "## JOIN Types\n```sql\n-- INNER: only matching rows\nSELECT s.name, e.course\nFROM students s\nINNER JOIN enrollments e ON s.id = e.student_id;\n\n-- LEFT: all left rows\nFROM students s\nLEFT JOIN enrollments e ON s.id = e.student_id;\n```",
      instructions: "## Task: Join Queries\nTables: `students(id,name)`, `enrollments(id,student_id,course,grade)`\n1. INNER JOIN — students with courses\n2. Filter grade = 'A'\n3. LEFT JOIN — all students including unenrolled",
      starterCode: "-- 1.\nSELECT s.name, e.course FROM students ___\nINNER JOIN enrollments e ON s.___ = e.___;\n-- 2.\nSELECT s.name,e.course,e.grade FROM students s\nINNER JOIN enrollments e ON s.id=e.student_id\nWHERE e.grade = ___;\n-- 3.\nSELECT s.name,e.course FROM students s\n___ JOIN enrollments e ON s.id=e.student_id;",
      solution: "SELECT s.name,e.course FROM students s INNER JOIN enrollments e ON s.id=e.student_id;\nSELECT s.name,e.course,e.grade FROM students s INNER JOIN enrollments e ON s.id=e.student_id WHERE e.grade='A';\nSELECT s.name,e.course FROM students s LEFT JOIN enrollments e ON s.id=e.student_id;",
      hint: "INNER returns matches only. LEFT keeps all left rows.",
      rubric: "INNER JOIN correct. WHERE filter. LEFT JOIN correct."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// DATA SCIENCE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Pandas & NumPy Basics": {
  aiRubric: "Check imports, array ops, DataFrame creation, filtering, apply.",
  lessons: [
    {
      title: "NumPy Arrays",
      theory: "## NumPy\n```python\nimport numpy as np\narr = np.array([1,2,3,4,5])\nprint(arr * 2)     # [2,4,6,8,10]\nprint(arr.mean())  # 3.0\nprint(arr.std())   # std deviation\nprint(arr.shape)   # (5,)\n```",
      instructions: "## Task: Score Analysis\n`scores = [78,92,65,88,74,91,55,83]`\n1. Convert to NumPy array\n2. Print mean, max, min, std\n3. Count > 80\n4. Print sorted descending",
      starterCode: "import numpy as np\nscores = [78,92,65,88,74,91,55,83]\narr = np.array(___)\n\nprint(f'Mean: {___.mean():.1f}')\nprint(f'Max:  {___.max()}')\nprint(f'Min:  {___.min()}')\nprint(f'Std:  {___.std():.2f}')\n\nabove = arr[arr > ___]\nprint(f'Above 80: {len(above)}')\nprint('Sorted:', np.sort(arr)[::-1])",
      solution: "import numpy as np\nscores=[78,92,65,88,74,91,55,83]\narr=np.array(scores)\nprint(f'Mean:{arr.mean():.1f}')\nprint(f'Max:{arr.max()}')\nprint(f'Min:{arr.min()}')\nprint(f'Std:{arr.std():.2f}')\nabove=arr[arr>80]\nprint(f'Above 80:{len(above)}')\nprint('Sorted:',np.sort(arr)[::-1])",
      hint: "arr.mean(), arr.max(). Boolean index arr[arr>80]. [::-1] reverses.",
      rubric: "np.array. All stats. Boolean index. Descending sort."
    },
    {
      title: "Pandas DataFrames",
      theory: "## Pandas\n```python\nimport pandas as pd\ndf = pd.DataFrame({'name':['Ada'],'score':[88]})\nprint(df.describe())\ndf['grade'] = df['score'].apply(lambda s: 'A' if s>=80 else 'B')\n```",
      instructions: "## Task: Student Report\n5 students (name, course, score):\n1. info()\n2. Average score\n3. Highest scorer\n4. Filter >= 80\n5. Add Pass/Fail column",
      starterCode: "import pandas as pd\ndata={'name':['Ada','Tunde','Ngozi','Emeka','Amaka'],'course':['Python','FastAPI','Python','SQL','AI'],'score':[88,72,95,58,81]}\ndf = pd.DataFrame(___)\ndf.info()\n\nprint(f'Average: {df[___].mean():.1f}')\ntop = df.loc[df['score'].idxmax(), ___]\nprint(f'Top: {top}')\n\nhigh = df[df['score'] >= ___]\nprint(high[['name','score']])\n\ndf['result'] = df['score'].apply(lambda s: ___ if s>=60 else ___)\nprint(df[['name','score','result']])",
      solution: "import pandas as pd\ndata={'name':['Ada','Tunde','Ngozi','Emeka','Amaka'],'course':['Python','FastAPI','Python','SQL','AI'],'score':[88,72,95,58,81]}\ndf=pd.DataFrame(data)\ndf.info()\nprint(f'Average:{df[\"score\"].mean():.1f}')\ntop=df.loc[df['score'].idxmax(),'name']\nprint(f'Top:{top}')\nhigh=df[df['score']>=80]\nprint(high[['name','score']])\ndf['result']=df['score'].apply(lambda s:'Pass' if s>=60 else 'Fail')\nprint(df[['name','score','result']])",
      hint: "idxmax() index of max. df[df['score']>=80] filters. apply with lambda.",
      rubric: "DataFrame created. info(). idxmax. Filter. apply lambda."
    },
    {
      title: "Data Cleaning",
      theory: "## Cleaning\n```python\ndf.isnull().sum()       # count NaN\ndf.fillna(0)            # fill NaN\ndf.dropna()             # drop NaN rows\ndf.drop_duplicates()    # remove dupes\ndf['col'].str.strip()   # trim spaces\ndf['col'].astype(int)   # cast type\n```",
      instructions: "## Task: Clean Messy Data\n1. Report null counts\n2. Fill missing scores with mean\n3. Drop duplicates\n4. Convert score to int\n5. Strip whitespace from names",
      starterCode: "import pandas as pd\ndata={'name':['Ada ',' Tunde','Ngozi','Ada ','Emeka'],'score':[88,None,95,88,72]}\ndf = pd.DataFrame(data)\n\nprint('Nulls:\\n', df.___().sum())\n\nmean_score = df['score'].mean()\ndf['score'] = df['score'].fillna(___)\n\ndf = df.drop_duplicates()\ndf['score'] = df['score'].astype(___)\ndf['name'] = df['name'].str.___\n\nprint(df)",
      solution: "import pandas as pd\ndata={'name':['Ada ',' Tunde','Ngozi','Ada ','Emeka'],'score':[88,None,95,88,72]}\ndf=pd.DataFrame(data)\nprint('Nulls:\\n',df.isnull().sum())\nmean_score=df['score'].mean()\ndf['score']=df['score'].fillna(mean_score)\ndf=df.drop_duplicates()\ndf['score']=df['score'].astype(int)\ndf['name']=df['name'].str.strip()\nprint(df)",
      hint: "isnull().sum(). fillna(mean). drop_duplicates(). astype(int). str.strip().",
      rubric: "isnull used. fillna mean. drop_duplicates. astype(int). strip names."
    }
  ]
},

"Intro to Machine Learning": {
  aiRubric: "Check sklearn imports, train_test_split, fit, predict, metrics.",
  lessons: [
    {
      title: "Your First ML Model",
      theory: "## Scikit-Learn Pattern\n```python\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\n\nX_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)\nmodel = LogisticRegression()\nmodel.fit(X_train, y_train)\ny_pred = model.predict(X_test)\nprint(accuracy_score(y_test, y_pred))\n```",
      instructions: "## Task: Iris Classifier\n1. Load Iris dataset\n2. Split 80/20\n3. Train LogisticRegression\n4. Print accuracy and classification report",
      starterCode: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score, classification_report\n\niris = load_iris()\nX, y = iris.___, iris.___\n\nX_train,X_test,y_train,y_test = train_test_split(\n    X, y, test_size=___, random_state=42)\n\nmodel = LogisticRegression(max_iter=200)\nmodel.___(X_train, y_train)\ny_pred = model.___(X_test)\n\nprint(f'Accuracy: {accuracy_score(y_test,y_pred):.2%}')\nprint(classification_report(y_test, y_pred, target_names=iris.target_names))",
      solution: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score,classification_report\niris=load_iris()\nX,y=iris.data,iris.target\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nmodel=LogisticRegression(max_iter=200)\nmodel.fit(X_train,y_train)\ny_pred=model.predict(X_test)\nprint(f'Accuracy:{accuracy_score(y_test,y_pred):.2%}')\nprint(classification_report(y_test,y_pred,target_names=iris.target_names))",
      hint: "iris.data is X, iris.target is y. test_size=0.2. model.fit() trains.",
      rubric: "data/target loaded. 0.2 split. fit/predict called. accuracy_score used."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// AI ENGINEERING
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Prompt Engineering": {
  aiRubric: "Check role, context, task, format in prompts.",
  lessons: [
    {
      title: "Anatomy of a Good Prompt",
      theory: "## Prompt Structure\n1. **Role** — who the AI is\n2. **Context** — background\n3. **Task** — what exactly to do\n4. **Format** — how to respond\n\n```python\nsystem = 'You are a senior Python tutor. Be concise.'\nuser   = 'Explain Python lists in 2 sentences with 1 code example.'\n```",
      instructions: "## Task: Design 3 Prompts\nWrite system + user for:\n1. Nigerian cooking assistant\n2. Python code reviewer\n3. Quiz generator\n\nEach must specify: role, task, output format.",
      starterCode: "cooking_system = 'You are ___, a Nigerian cooking expert. ___'\ncooking_user   = 'Task: explain jollof rice. Format: ___'\n\nreview_system = '___'\nreview_user   = 'Review:{code}. Format: bullet points'\n\nquiz_system = '___'\nquiz_user   = 'Topic: Python loops. Task:___. Format: 5 MCQs A-D'\n\nfor name,s,u in [('Cooking',cooking_system,cooking_user),('Review',review_system,review_user),('Quiz',quiz_system,quiz_user)]:\n    print(f'=== {name} ===')\n    print(f'System: {s[:70]}')\n    print(f'User:   {u[:70]}\\n')",
      solution: "cooking_system='You are Mama Titi, a Nigerian cooking expert. Be warm and clear.'\ncooking_user='Task: explain jollof rice. Format: numbered steps max 8, include tips.'\nreview_system='You are a senior Python engineer. Give direct actionable feedback.'\nreview_user='Review:{code}. Format: bullet points — Issues, Fixes, Style.'\nquiz_system='You are an expert educator who writes clear MCQs.'\nquiz_user='Topic: Python loops. Task: Create 5 MCQs. Format: Options A-D, mark correct.'\nfor name,s,u in [('Cooking',cooking_system,cooking_user),('Review',review_system,review_user),('Quiz',quiz_system,quiz_user)]:\n    print(f'==={name}===')\n    print(f'System:{s[:70]}')\n    print(f'User:{u[:70]}\\n')",
      hint: "Be specific in role. Always state output format explicitly.",
      rubric: "All 3 prompts have role, task, format. System distinct from user."
    }
  ]
},

"LLM Fundamentals": {
  aiRubric: "Check API call, message roles, response parsing, error handling.",
  lessons: [
    {
      title: "First LLM API Call",
      theory: "## LLM API Pattern\n```python\nimport requests\nr = requests.post(\n    'https://api.groq.com/openai/v1/chat/completions',\n    headers={'Authorization': f'Bearer {KEY}'},\n    json={\n        'model':'llama3-8b-8192',\n        'messages':[\n            {'role':'system','content':'You are helpful.'},\n            {'role':'user','content':'Hello!'}\n        ]\n    }\n)\nprint(r.json()['choices'][0]['message']['content'])\n```",
      instructions: "## Task: ask_llm() Function\nWrite `ask_llm(question, system_prompt)` that:\n1. Builds message list\n2. POSTs to Groq API\n3. Returns text response\n4. Handles errors with try/except",
      starterCode: "import requests, os\nAPI_KEY = os.getenv('GROQ_API_KEY','your-key')\nURL = 'https://api.groq.com/openai/v1/chat/completions'\n\ndef ask_llm(question, system_prompt='You are a helpful tutor.'):\n    messages = [\n        {'role': ___, 'content': ___},\n        {'role': ___, 'content': ___}\n    ]\n    try:\n        r = requests.post(URL,\n            headers={'Authorization': f'Bearer {API_KEY}'},\n            json={'model':'llama3-8b-8192','messages':___})\n        return r.json()[___][0][___][___]\n    except Exception as e:\n        return f'Error: {e}'\n\nprint(ask_llm('What is a Python list?'))",
      solution: "import requests,os\nAPI_KEY=os.getenv('GROQ_API_KEY','your-key')\nURL='https://api.groq.com/openai/v1/chat/completions'\ndef ask_llm(question,system_prompt='You are a helpful tutor.'):\n    messages=[{'role':'system','content':system_prompt},{'role':'user','content':question}]\n    try:\n        r=requests.post(URL,headers={'Authorization':f'Bearer {API_KEY}'},json={'model':'llama3-8b-8192','messages':messages})\n        return r.json()['choices'][0]['message']['content']\n    except Exception as e:\n        return f'Error:{e}'\nprint(ask_llm('What is a Python list?'))",
      hint: "Roles: 'system' and 'user'. Response: json()['choices'][0]['message']['content'].",
      rubric: "Both roles correct. POST URL. Response extracted. try/except present."
    },
    {
      title: "Conversation Memory",
      theory: "## Multi-turn Conversations\nLLMs are stateless — pass full history each call:\n```python\nhistory = [{'role':'system','content':'...'}]\nhistory.append({'role':'user','content':msg})\n# after reply:\nhistory.append({'role':'assistant','content':reply})\n```",
      instructions: "## Task: Chatbot Class\nBuild `Chatbot(system)` with:\n- `chat(message)` — appends user, calls API, appends reply, returns reply\n- `reset()` — clears history but keeps system message",
      starterCode: "import requests, os\n\nclass Chatbot:\n    def __init__(self, system='You are a helpful assistant.'):\n        self.history = [{'role':'system','content':___}]\n        self.api_key = os.getenv('GROQ_API_KEY','')\n\n    def chat(self, message):\n        self.history.append({'role':'user','content':___})\n        r = requests.post(\n            'https://api.groq.com/openai/v1/chat/completions',\n            headers={'Authorization':f'Bearer {self.api_key}'},\n            json={'model':'llama3-8b-8192','messages':self.___}\n        )\n        reply = r.json()['choices'][0]['message']['content']\n        self.history.append({'role':___,'content':reply})\n        return reply\n\n    def reset(self):\n        sys_msg = self.history[0]\n        self.history = [___]\n\nbot = Chatbot('You are a Python tutor.')\nprint(bot.chat('What is a variable?'))\nprint(bot.chat('Show me an example'))\nprint(f'History: {len(bot.history)} messages')",
      solution: "import requests,os\nclass Chatbot:\n    def __init__(self,system='You are a helpful assistant.'):\n        self.history=[{'role':'system','content':system}]\n        self.api_key=os.getenv('GROQ_API_KEY','')\n    def chat(self,message):\n        self.history.append({'role':'user','content':message})\n        r=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {self.api_key}'},json={'model':'llama3-8b-8192','messages':self.history})\n        reply=r.json()['choices'][0]['message']['content']\n        self.history.append({'role':'assistant','content':reply})\n        return reply\n    def reset(self):\n        sys_msg=self.history[0]\n        self.history=[sys_msg]\nbot=Chatbot('You are a Python tutor.')\nprint(bot.chat('What is a variable?'))\nprint(bot.chat('Show me an example'))\nprint(f'History:{len(bot.history)} messages')",
      hint: "Append user then assistant each turn. self.history passed to API. reset() keeps index 0.",
      rubric: "history initialized. chat() appends both. history passed. reset() keeps system."
    }
  ]
},

"RAG Pipelines": {
  aiRubric: "Check chunking, similarity, retrieval, context injection.",
  lessons: [
    {
      title: "Simple RAG Pipeline",
      theory: "## RAG = Retrieve + Generate\n1. **Index** — chunk docs, embed, store\n2. **Retrieve** — find similar chunks to query\n3. **Generate** — pass chunks as context to LLM\n\n```python\nrelevant = retrieve(question, docs)\nprompt   = f'Context: {relevant}\\nQuestion: {question}'\nanswer   = llm(prompt)\n```",
      instructions: "## Task: Word-Overlap RAG\n1. 5 docs about Python topics\n2. `similarity(query, doc)` — word overlap score\n3. `retrieve(query, docs)` — returns top match\n4. `rag_prompt(q, docs)` — injects context\n5. Test with 2 queries",
      starterCode: "documents = [\n    'Python lists store ordered mutable collections.',\n    'Dictionaries store key-value pairs for fast lookups.',\n    'Functions let you reuse code and accept parameters.',\n    'Classes define blueprints for objects with attributes.',\n    'Loops iterate over sequences with for and while.'\n]\n\ndef similarity(query, doc):\n    q = set(query.lower().split())\n    d = set(doc.lower().split())\n    return len(q & d) / (len(q) + 1)\n\ndef retrieve(query, docs, top_k=1):\n    scores = [(similarity(___, doc), doc) for doc in ___]\n    scores.sort(reverse=___)\n    return [doc for _, doc in scores[:top_k]]\n\ndef rag_prompt(question, docs):\n    ctx = retrieve(___, docs)[0]\n    return f'Context: {ctx}\\nQuestion: {question}\\nAnswer:'\n\nfor q in ['How do I store key-value data?', 'What is a loop?']:\n    print('Q:', q)\n    print('Context:', retrieve(q, documents)[0])\n    print()",
      solution: "documents=['Python lists store ordered mutable collections.','Dictionaries store key-value pairs for fast lookups.','Functions let you reuse code and accept parameters.','Classes define blueprints for objects with attributes.','Loops iterate over sequences with for and while.']\ndef similarity(query,doc):\n    q=set(query.lower().split())\n    d=set(doc.lower().split())\n    return len(q&d)/(len(q)+1)\ndef retrieve(query,docs,top_k=1):\n    scores=[(similarity(query,doc),doc) for doc in docs]\n    scores.sort(reverse=True)\n    return [doc for _,doc in scores[:top_k]]\ndef rag_prompt(question,docs):\n    ctx=retrieve(question,docs)[0]\n    return f'Context:{ctx}\\nQuestion:{question}\\nAnswer:'\nfor q in ['How do I store key-value data?','What is a loop?']:\n    print('Q:',q)\n    print('Context:',retrieve(q,documents)[0])\n    print()",
      hint: "sort(reverse=True) for highest first. context[0] gets top result.",
      rubric: "similarity correct. retrieve sorts. rag_prompt injects. Both queries tested."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// FRONTEND
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"HTML Essentials": {
  aiRubric: "Check valid HTML structure, semantic tags, nesting.",
  lessons: [
    {
      title: "HTML Document Structure",
      theory: "## HTML Skeleton\n```html\n<!DOCTYPE html>\n<html lang='en'>\n<head>\n  <meta charset='UTF-8'>\n  <title>Title</title>\n</head>\n<body>\n  <h1>Heading</h1>\n  <p>Paragraph</p>\n</body>\n</html>\n```",
      instructions: "## Task: Student Profile Page\n1. DOCTYPE + full structure\n2. Title: 'My Profile'\n3. h1 with your name\n4. p with your course\n5. ul with 3 skills\n6. Link to GitHub",
      starterCode: "<!DOCTYPE ___>\n<html lang='en'>\n<___>\n  <meta charset='UTF-8'>\n  <title>___</title>\n</___>\n<___>\n  <h1>___</h1>\n  <p>Course: ___</p>\n  <ul>\n    <li>___</li>\n    <li>___</li>\n    <li>___</li>\n  </ul>\n  <a href='https://github.com'>GitHub</a>\n</___>\n</html>",
      solution: "<!DOCTYPE html>\n<html lang='en'>\n<head>\n  <meta charset='UTF-8'>\n  <title>My Profile</title>\n</head>\n<body>\n  <h1>Ada Okonkwo</h1>\n  <p>Course: Computer Science</p>\n  <ul><li>Python</li><li>FastAPI</li><li>SQL</li></ul>\n  <a href='https://github.com'>GitHub</a>\n</body>\n</html>",
      hint: "head for meta info. body for visible content. ul > li for lists.",
      rubric: "DOCTYPE. head/body. h1/p/ul/li/a all present."
    },
    {
      title: "Semantic HTML",
      theory: "## Semantic Tags\n```html\n<header>  — top of page\n<nav>     — navigation\n<main>    — main content\n<article> — self-contained\n<aside>   — sidebar\n<footer>  — bottom\n```\nSemantic HTML improves SEO and accessibility.",
      instructions: "## Task: Blog Page\n1. `<header>` with site name + `<nav>` 3 links\n2. `<main>` with `<article>` (heading, date, 2 paras)\n3. `<aside>` with Related Posts list\n4. `<footer>` with copyright",
      starterCode: "<!DOCTYPE html>\n<html lang='en'>\n<head><meta charset='UTF-8'><title>Blog</title></head>\n<body>\n\n  <___>\n    <h1>Mabel's Tech Blog</h1>\n    <___>\n      <a href='/'>Home</a>\n      <a href='/courses'>Courses</a>\n      <a href='/contact'>Contact</a>\n    </___>\n  </___>\n\n  <___>\n    <___>\n      <h2>Getting Started with Python</h2>\n      <time datetime='2024-01-15'>Jan 15, 2024</time>\n      <p>Python is one of the most popular languages...</p>\n      <p>In this article we cover the basics...</p>\n    </___>\n    <___>\n      <h3>Related Posts</h3>\n      <ul>\n        <li><a href='#'>Python Basics</a></li>\n        <li><a href='#'>FastAPI Tutorial</a></li>\n      </ul>\n    </___>\n  </___>\n\n  <___>\n    <p>&copy; 2024 Mabel Academy</p>\n  </___>\n\n</body></html>",
      solution: "<!DOCTYPE html>\n<html lang='en'>\n<head><meta charset='UTF-8'><title>Blog</title></head>\n<body>\n<header>\n  <h1>Mabel's Tech Blog</h1>\n  <nav><a href='/'>Home</a><a href='/courses'>Courses</a><a href='/contact'>Contact</a></nav>\n</header>\n<main>\n  <article>\n    <h2>Getting Started with Python</h2>\n    <time datetime='2024-01-15'>Jan 15, 2024</time>\n    <p>Python is one of the most popular languages...</p>\n    <p>In this article we cover the basics...</p>\n  </article>\n  <aside>\n    <h3>Related Posts</h3>\n    <ul><li><a href='#'>Python Basics</a></li><li><a href='#'>FastAPI Tutorial</a></li></ul>\n  </aside>\n</main>\n<footer><p>&copy; 2024 Mabel Academy</p></footer>\n</body></html>",
      hint: "header > nav. main > article + aside. footer at bottom.",
      rubric: "All 6 semantic tags correct. nav in header. article and aside in main."
    }
  ]
},

"JavaScript Basics": {
  aiRubric: "Check let/const, functions, array methods.",
  lessons: [
    {
      title: "Variables & Functions",
      theory: "## JS Basics\n```javascript\nconst name = 'Ada';  // can't reassign\nlet score = 0;       // can reassign\n\nfunction greet(name) {\n  return `Hello, ${name}!`;\n}\nconst add = (a, b) => a + b;  // arrow fn\nconsole.log(greet('Ada'));    // Hello, Ada!\n```",
      instructions: "## Task: Score Processor\n1. `scores` array of 5 numbers\n2. `getAverage(arr)` using reduce\n3. `getGrade(avg)` → A/B/C/F\n4. Log: `Average: 82.4 | Grade: B`",
      starterCode: "const scores = [78, 92, 65, 88, ___];\n\nfunction getAverage(arr) {\n  const sum = arr.reduce((___, b) => a + b, 0);\n  return sum / arr.___;\n}\n\nfunction getGrade(avg) {\n  if (avg >= 80) return ___;\n  else if (avg >= 70) return ___;\n  else if (avg >= 60) return ___;\n  else return ___;\n}\n\nconst avg = getAverage(scores);\nconsole.log(`Average: ${avg.toFixed(1)} | Grade: ${getGrade(avg)}`);",
      solution: "const scores=[78,92,65,88,75];\nfunction getAverage(arr){\n  const sum=arr.reduce((a,b)=>a+b,0);\n  return sum/arr.length;\n}\nfunction getGrade(avg){\n  if(avg>=80)return'A';\n  else if(avg>=70)return'B';\n  else if(avg>=60)return'C';\n  else return'F';\n}\nconst avg=getAverage(scores);\nconsole.log(`Average:${avg.toFixed(1)} | Grade:${getGrade(avg)}`);",
      hint: "reduce((a,b)=>a+b,0). arr.length for count. toFixed(1).",
      rubric: "reduce for sum. Division. Grade conditions. Template literal."
    },
    {
      title: "Array Methods",
      theory: "## Array Methods\n```javascript\nconst nums = [1,2,3,4,5];\nnums.map(x => x*2)         // [2,4,6,8,10]\nnums.filter(x => x>2)      // [3,4,5]\nnums.reduce((a,b)=>a+b, 0) // 15\nnums.find(x => x>3)        // 4\nnums.sort((a,b)=>b-a)      // desc\n```",
      instructions: "## Task: Student Processing\n`students = [{name, score}]`\n1. `map` to add `grade` field\n2. `filter` passing students (>=60)\n3. `reduce` for total score\n4. `find` student named 'Ngozi'\n5. `sort` by score descending",
      starterCode: "const students = [\n  {name:'Ada',score:88},{name:'Tunde',score:55},\n  {name:'Ngozi',score:92},{name:'Emeka',score:67},{name:'Amaka',score:45}\n];\n\nconst withGrades = students.___(s => ({...s, grade: s.score>=80?'A':s.score>=70?'B':s.score>=60?'C':'F'}));\nconst passing = students.___(s => s.score >= ___);\nconst total = students.___((acc, s) => acc + s.score, 0);\nconst ngozi = students.___(s => s.name === ___);\nconst ranked = [...students].___((___, b) => b.score - a.score);\n\nconsole.log('Grades:', withGrades.map(s=>`${s.name}:${s.grade}`));\nconsole.log('Passing:', passing.length);\nconsole.log('Total:', total);\nconsole.log('Ngozi:', ngozi);\nconsole.log('Ranked:', ranked.map(s=>s.name));",
      solution: "const students=[{name:'Ada',score:88},{name:'Tunde',score:55},{name:'Ngozi',score:92},{name:'Emeka',score:67},{name:'Amaka',score:45}];\nconst withGrades=students.map(s=>({...s,grade:s.score>=80?'A':s.score>=70?'B':s.score>=60?'C':'F'}));\nconst passing=students.filter(s=>s.score>=60);\nconst total=students.reduce((acc,s)=>acc+s.score,0);\nconst ngozi=students.find(s=>s.name==='Ngozi');\nconst ranked=[...students].sort((a,b)=>b.score-a.score);\nconsole.log('Grades:',withGrades.map(s=>`${s.name}:${s.grade}`));\nconsole.log('Passing:',passing.length);\nconsole.log('Total:',total);\nconsole.log('Ngozi:',ngozi);\nconsole.log('Ranked:',ranked.map(s=>s.name));",
      hint: "map returns new array. filter keeps matching. reduce accumulates. find returns first match. spread [...arr] before sort.",
      rubric: "map/filter/reduce/find/sort all used correctly."
    }
  ]
},

"CSS Styling & Layout": {
  aiRubric: "Check selectors, box model, flexbox, colors, typography.",
  lessons: [
    {
      title: "Selectors & Box Model",
      theory: "## CSS Basics\n```css\nh1 { color: #333; }          /* element */\n.card { padding: 16px; }     /* class */\n#header { background: #fff; } /* id */\n\n.box {\n  width: 200px;\n  padding: 16px;   /* inside */\n  border: 2px solid #333;\n  margin: 24px;    /* outside */\n  box-sizing: border-box;\n}\n```",
      instructions: "## Task: Style a Student Card\n1. `body` — dark background, white text\n2. `.card` — white bg, rounded corners, padding, max-width 400px, box-shadow\n3. `.card h2` — teal color\n4. `.badge` — pill shape (border-radius: 20px)",
      starterCode: "___ {\n  background: #1e1e1e;\n  color: white;\n  font-family: sans-serif;\n  display: flex;\n  justify-content: center;\n  padding: 40px;\n}\n\n.___ {\n  background: white;\n  color: #1e1e1e;\n  border-radius: ___;\n  padding: ___;\n  max-width: 400px;\n  box-shadow: 0 4px 20px rgba(0,0,0,0.3);\n}\n\n.card ___ {\n  color: #00e5a0;\n}\n\n.___ {\n  background: #00e5a0;\n  color: #1e1e1e;\n  border-radius: 20px;\n  padding: 4px 12px;\n  font-size: 12px;\n}",
      solution: "body{background:#1e1e1e;color:white;font-family:sans-serif;display:flex;justify-content:center;padding:40px;}\n.card{background:white;color:#1e1e1e;border-radius:8px;padding:24px;max-width:400px;box-shadow:0 4px 20px rgba(0,0,0,0.3);}\n.card h2{color:#00e5a0;}\n.badge{background:#00e5a0;color:#1e1e1e;border-radius:20px;padding:4px 12px;font-size:12px;}",
      hint: "body selector. .card class. .card h2 descendant. border-radius:20px for pill.",
      rubric: "body bg set. .card styled. .card h2 teal. .badge pill shape."
    },
    {
      title: "Flexbox Layout",
      theory: "## Flexbox\n```css\n.container {\n  display: flex;\n  justify-content: space-between;  /* horizontal */\n  align-items: center;             /* vertical */\n  gap: 16px;\n}\n.item { flex: 1; }  /* grow equally */\n```",
      instructions: "## Task: Navigation Bar\n1. Logo left, links center, button right\n2. All vertically centered\n3. Proper gap between links",
      starterCode: ".navbar {\n  display: ___;\n  justify-content: ___;\n  align-items: ___;\n  padding: 16px 32px;\n  background: #1e1e1e;\n  gap: 24px;\n}\n\n.logo {\n  font-weight: bold;\n  color: #00e5a0;\n}\n\n.nav-links {\n  display: ___;\n  gap: ___;\n  list-style: none;\n}\n\n.nav-links a { color: white; text-decoration: none; }\n\n.login-btn {\n  padding: 8px 20px;\n  background: #00e5a0;\n  color: #1e1e1e;\n  border: none;\n  border-radius: 6px;\n  cursor: pointer;\n  margin-left: auto;\n}",
      solution: ".navbar{display:flex;justify-content:space-between;align-items:center;padding:16px 32px;background:#1e1e1e;gap:24px;}\n.logo{font-weight:bold;color:#00e5a0;}\n.nav-links{display:flex;gap:24px;list-style:none;}\n.nav-links a{color:white;text-decoration:none;}\n.login-btn{padding:8px 20px;background:#00e5a0;color:#1e1e1e;border:none;border-radius:6px;cursor:pointer;margin-left:auto;}",
      hint: "display:flex. justify-content:space-between. align-items:center. nav-links also flex.",
      rubric: "display:flex on navbar. justify-content. align-items:center. nav-links flex with gap."
    }
  ]
},

"DOM Manipulation": {
  aiRubric: "Check querySelector, addEventListener, textContent, classList.",
  lessons: [
    {
      title: "Selecting & Modifying Elements",
      theory: "## DOM API\n```javascript\nconst el  = document.querySelector('.card');\nconst all = document.querySelectorAll('li');\n\nel.textContent = 'New text';\nel.style.color = 'red';\nel.classList.add('active');\nel.classList.toggle('hidden');\n\nconst p = document.createElement('p');\np.textContent = 'Hello';\ndocument.body.appendChild(p);\n```",
      instructions: "## Task: Dynamic Score Card\n1. Set `#score` text to 88\n2. Set `#status` to 'Pass' (green) if score >= 60\n3. Add class `highlight` to `#card` if score >= 80\n4. Create and append `<p>Grade: A</p>` to `#output`",
      starterCode: "const score = 88;\n\ndocument.querySelector(___).textContent = ___;\n\nconst statusEl = document.querySelector('___');\nif (score >= 60) {\n  statusEl.___ = 'Pass';\n  statusEl.style.___ = 'green';\n}\n\nif (score >= 80) {\n  document.querySelector('___').classList.add('___');\n}\n\nconst grade = score >= 80 ? 'A' : 'B';\nconst p = document.___(___);  \np.textContent = `Grade: ${grade}`;\ndocument.querySelector('___').appendChild(p);",
      solution: "const score=88;\ndocument.querySelector('#score').textContent=score;\nconst statusEl=document.querySelector('#status');\nif(score>=60){\n  statusEl.textContent='Pass';\n  statusEl.style.color='green';\n}\nif(score>=80){\n  document.querySelector('#card').classList.add('highlight');\n}\nconst grade=score>=80?'A':'B';\nconst p=document.createElement('p');\np.textContent=`Grade:${grade}`;\ndocument.querySelector('#output').appendChild(p);",
      hint: "querySelector('#id') for IDs. textContent sets text. createElement then appendChild.",
      rubric: "querySelector used. textContent set. style.color changed. classList.add. createElement/appendChild."
    }
  ]
},



// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// PYTHON CORE — INTERMEDIATE (missing)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Modules & Packages": {
  aiRubric: "Check import statements, from...import, __name__, module creation.",
  lessons: [
    {
      title: "Importing Modules",
      theory: "## Modules\n```python\nimport math\nprint(math.sqrt(16))   # 4.0\nprint(math.pi)         # 3.14159\n\nfrom math import sqrt, pi\nprint(sqrt(25))        # 5.0\n\nimport random\nprint(random.randint(1, 10))\n```",
      instructions: "## Task: Math Toolkit\nUsing the `math` and `random` modules:\n1. Print the square root of 144\n2. Print pi rounded to 4 decimal places\n3. Generate 5 random integers between 1 and 100\n4. Find the ceiling and floor of 4.7",
      starterCode: "import math\nimport random\n\nprint('sqrt(144):', math.___(___))\nprint('pi:', round(math.___, 4))\n\nrandoms = [random.___(1, 100) for _ in range(5)]\nprint('Random:', randoms)\n\nprint('ceil(4.7):', math.___(4.7))\nprint('floor(4.7):', math.___(4.7))",
      solution: "import math\nimport random\nprint('sqrt(144):',math.sqrt(144))\nprint('pi:',round(math.pi,4))\nrandoms=[random.randint(1,100) for _ in range(5)]\nprint('Random:',randoms)\nprint('ceil(4.7):',math.ceil(4.7))\nprint('floor(4.7):',math.floor(4.7))",
      hint: "math.sqrt(), math.pi, random.randint(a,b), math.ceil(), math.floor()",
      rubric: "sqrt, pi, randint, ceil, floor all used."
    },
    {
      title: "Creating Your Own Module",
      theory: "## Custom Modules\nAny .py file is a module:\n```python\n# utils.py\ndef add(a, b): return a + b\ndef greet(name): return f'Hello, {name}!'\nPI = 3.14159\n\n# main.py\nfrom utils import add, greet, PI\nprint(add(3, 4))       # 7\nprint(greet('Ada'))    # Hello, Ada!\n```\n`if __name__ == '__main__':` runs only when file is executed directly.",
      instructions: "## Task: math_utils Module\nWrite a `math_utils.py` style module with:\n1. `is_even(n)` — returns True if n is even\n2. `factorial(n)` — computes n! recursively\n3. `is_prime(n)` — checks if n is prime\n4. Test all three in the same file using `if __name__ == '__main__':`",
      starterCode: "def is_even(n):\n    return n % ___ == 0\n\ndef factorial(n):\n    if n <= 1:\n        return ___\n    return n * factorial(___ - 1)\n\ndef is_prime(n):\n    if n < 2: return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == ___:\n            return False\n    return True\n\nif __name__ == '___':\n    print(is_even(4))       # True\n    print(factorial(5))     # 120\n    print(is_prime(17))     # True\n    print(is_prime(15))     # False",
      solution: "def is_even(n):\n    return n%2==0\ndef factorial(n):\n    if n<=1:return 1\n    return n*factorial(n-1)\ndef is_prime(n):\n    if n<2:return False\n    for i in range(2,int(n**0.5)+1):\n        if n%i==0:return False\n    return True\nif __name__=='__main__':\n    print(is_even(4))\n    print(factorial(5))\n    print(is_prime(17))\n    print(is_prime(15))",
      hint: "n%2==0 for even. Recursive factorial: n * factorial(n-1). Prime: no divisor in range 2 to sqrt(n).",
      rubric: "All 3 functions correct. __name__ check present. All 4 tests run."
    },
    {
      title: "Standard Library Tour",
      theory: "## Useful Standard Modules\n```python\nimport os, sys, datetime, json, collections\n\nos.getcwd()              # current directory\ndatetime.date.today()    # today's date\njson.dumps({'a':1})      # dict to JSON string\njson.loads('{\"a\":1}')   # JSON string to dict\ncollections.Counter([1,2,2,3]) # {2:2,1:1,3:1}\n```",
      instructions: "## Task: Student Report JSON\n1. Create a dict with 3 student records\n2. Convert to JSON string with `json.dumps(indent=2)`\n3. Parse it back with `json.loads()`\n4. Use `collections.Counter` to count how many students are per course\n5. Print today's date",
      starterCode: "import json\nimport collections\nimport datetime\n\nstudents = [\n    {'name':'Ada',   'course':'Python', 'score':88},\n    {'name':'Tunde', 'course':'SQL',    'score':72},\n    {'name':'Ngozi', 'course':'Python', 'score':95}\n]\n\njson_str = json.___(students, indent=___)\nprint(json_str)\n\nparsed = json.___(json_str)\nprint('First student:', parsed[0]['name'])\n\ncourses = [s['course'] for s in students]\ncounts = collections.___(courses)\nprint('Per course:', dict(counts))\n\nprint('Today:', datetime.date.___())",
      solution: "import json,collections,datetime\nstudents=[{'name':'Ada','course':'Python','score':88},{'name':'Tunde','course':'SQL','score':72},{'name':'Ngozi','course':'Python','score':95}]\njson_str=json.dumps(students,indent=2)\nprint(json_str)\nparsed=json.loads(json_str)\nprint('First:',parsed[0]['name'])\ncourses=[s['course'] for s in students]\ncounts=collections.Counter(courses)\nprint('Per course:',dict(counts))\nprint('Today:',datetime.date.today())",
      hint: "json.dumps() converts to string. json.loads() parses. Counter counts occurrences.",
      rubric: "json.dumps with indent. json.loads. Counter used. datetime.date.today()."
    }
  ]
},

"List Comprehensions": {
  aiRubric: "Check [expr for x in iterable if condition] syntax.",
  lessons: [
    {
      title: "Basic Comprehensions",
      theory: "## List Comprehensions\n```python\n# Old way\nsquares = []\nfor x in range(5):\n    squares.append(x**2)\n\n# Comprehension\nsquares = [x**2 for x in range(5)]  # [0,1,4,9,16]\nevens   = [n for n in range(10) if n%2==0]\n```",
      instructions: "## Task: Three Comprehensions\n1. Squares of 1-10\n2. Even numbers from 1-20\n3. Words longer than 4 chars from a sentence",
      starterCode: "squares = [___ for x in range(1, 11)]\nprint(squares)\n\nevens = [n for n in range(1,21) if n % ___ == 0]\nprint(evens)\n\nsentence = 'Mabel Academy teaches backend and frontend development'\nlong_words = [w for w in sentence.split() if len(w) > ___]\nprint(long_words)",
      solution: "squares=[x**2 for x in range(1,11)]\nprint(squares)\nevens=[n for n in range(1,21) if n%2==0]\nprint(evens)\nsentence='Mabel Academy teaches backend and frontend development'\nlong_words=[w for w in sentence.split() if len(w)>4]\nprint(long_words)",
      hint: "x**2 for squares. n%2==0 for evens. len(w)>4 for long words.",
      rubric: "All 3 comprehensions correct."
    },
    {
      title: "Dict & Set Comprehensions",
      theory: "## Dict & Set Comprehensions\n```python\n# Dict\nscores = {'Ada':88,'Tunde':72}\ngrades = {name:'A' if s>=80 else 'B' for name,s in scores.items()}\n\n# Set (unique values only)\nlengths = {len(w) for w in ['hi','hello','hey']}  # {2,5}\n```",
      instructions: "## Task: Grade Dictionary\nFrom `[(name, score)]` list:\n1. Dict `{name: score}`\n2. Dict `{name: grade}` A(>=80) B(>=70) C(>=60) F\n3. Set of unique grades awarded",
      starterCode: "data = [('Ada',88),('Tunde',72),('Ngozi',95),('Emeka',55),('Amaka',65)]\n\nscores = {name: score for name, score in ___}\n\ndef get_grade(s):\n    if s>=80: return 'A'\n    elif s>=70: return 'B'\n    elif s>=60: return 'C'\n    else: return 'F'\n\ngrades = {name: get_grade(___) for name, score in data}\nunique = {___ for ___ in grades.values()}\n\nprint(scores)\nprint(grades)\nprint('Unique grades:', unique)",
      solution: "data=[('Ada',88),('Tunde',72),('Ngozi',95),('Emeka',55),('Amaka',65)]\nscores={name:score for name,score in data}\ndef get_grade(s):\n    if s>=80:return'A'\n    elif s>=70:return'B'\n    elif s>=60:return'C'\n    else:return'F'\ngrades={name:get_grade(score) for name,score in data}\nunique={g for g in grades.values()}\nprint(scores)\nprint(grades)\nprint('Unique:',unique)",
      hint: "Dict: {k:v for k,v in data}. Set: {expr for x in iterable}.",
      rubric: "Both dict comprehensions. get_grade called. Set from .values()."
    },
    {
      title: "Nested Comprehensions",
      theory: "## Nested Comprehensions\n```python\n# Flatten a 2D list\nmatrix = [[1,2,3],[4,5,6],[7,8,9]]\nflat = [n for row in matrix for n in row]\n# [1,2,3,4,5,6,7,8,9]\n\n# 5x5 multiplication table\ntable = [[i*j for j in range(1,6)] for i in range(1,6)]\n```",
      instructions: "## Task: Matrix Operations\n1. Create a 4x4 matrix using nested comprehension (i*j)\n2. Flatten it into one list\n3. Filter only values > 8 from the flat list\n4. Print the matrix row by row",
      starterCode: "matrix = [[i*j for j in range(1,5)] for i in range(1,5)]\n\nfor row in matrix:\n    print(row)\n\nflat = [n for row in ___ for n in ___]\nprint('Flat:', flat)\n\nhigh = [n for n in flat if n > ___]\nprint('Above 8:', high)",
      solution: "matrix=[[i*j for j in range(1,5)] for i in range(1,5)]\nfor row in matrix:\n    print(row)\nflat=[n for row in matrix for n in row]\nprint('Flat:',flat)\nhigh=[n for n in flat if n>8]\nprint('Above 8:',high)",
      hint: "Nested: [expr for row in matrix for n in row] flattens. Filter with if n>8.",
      rubric: "4x4 matrix. Flatten with nested comprehension. Filter > 8."
    }
  ]
},

"Iterators & Generators": {
  aiRubric: "Check __iter__, __next__, yield keyword, generator expressions.",
  lessons: [
    {
      title: "Iterators",
      theory: "## Iterators\nAn iterator has `__iter__` and `__next__`:\n```python\nclass CountUp:\n    def __init__(self, limit):\n        self.current = 0\n        self.limit = limit\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.current >= self.limit:\n            raise StopIteration\n        self.current += 1\n        return self.current\n\nfor n in CountUp(5):\n    print(n)  # 1 2 3 4 5\n```",
      instructions: "## Task: Range Iterator\nCreate `MyRange(start, stop, step=1)` that mimics Python's range:\n1. Implement `__iter__` and `__next__`\n2. Raise StopIteration when done\n3. Test with `for n in MyRange(0, 10, 2):`",
      starterCode: "class MyRange:\n    def __init__(self, start, stop, step=1):\n        self.current = ___\n        self.stop = ___\n        self.step = ___\n\n    def __iter__(self):\n        return ___\n\n    def __next__(self):\n        if self.current >= self.___:\n            raise ___\n        value = self.current\n        self.current += self.___\n        return value\n\nfor n in MyRange(0, 10, 2):\n    print(n, end=' ')\nprint()\nprint(list(MyRange(1, 6)))",
      solution: "class MyRange:\n    def __init__(self,start,stop,step=1):\n        self.current=start\n        self.stop=stop\n        self.step=step\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.current>=self.stop:\n            raise StopIteration\n        value=self.current\n        self.current+=self.step\n        return value\nfor n in MyRange(0,10,2):\n    print(n,end=' ')\nprint()\nprint(list(MyRange(1,6)))",
      hint: "__iter__ returns self. __next__ increments current by step. Raise StopIteration when done.",
      rubric: "__iter__ returns self. __next__ logic correct. StopIteration raised. Both tests work."
    },
    {
      title: "Generators with yield",
      theory: "## Generators\n```python\ndef count_up(limit):\n    n = 0\n    while n < limit:\n        yield n\n        n += 1\n\ngen = count_up(3)\nprint(next(gen))  # 0\nprint(next(gen))  # 1\n\nfor n in count_up(5):\n    print(n)\n```\n`yield` pauses the function and returns a value. Much more memory efficient than lists.",
      instructions: "## Task: Fibonacci Generator\nWrite a generator `fibonacci(n)` that yields the first n Fibonacci numbers.\nAlso write `infinite_fib()` that yields forever — use `itertools.islice` to get first 10.",
      starterCode: "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        ___ a\n        a, b = ___, a + b\n\nprint(list(fibonacci(10)))\n\ndef infinite_fib():\n    a, b = 0, 1\n    while True:\n        yield ___\n        a, b = b, a + ___\n\nimport itertools\nfirst10 = list(itertools.islice(infinite_fib(), ___))\nprint(first10)",
      solution: "def fibonacci(n):\n    a,b=0,1\n    for _ in range(n):\n        yield a\n        a,b=b,a+b\nprint(list(fibonacci(10)))\ndef infinite_fib():\n    a,b=0,1\n    while True:\n        yield a\n        a,b=b,a+b\nimport itertools\nfirst10=list(itertools.islice(infinite_fib(),10))\nprint(first10)",
      hint: "yield a then swap: a,b = b, a+b. infinite_fib has no stop condition. islice(gen, 10).",
      rubric: "yield used. Fibonacci correct. infinite_fib has while True. islice used."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// PYTHON CORE — ADVANCED
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Decorators & Closures": {
  aiRubric: "Check closure variable capture, @decorator syntax, functools.wraps.",
  lessons: [
    {
      title: "Closures",
      theory: "## Closures\nA function that remembers variables from its enclosing scope:\n```python\ndef make_multiplier(n):\n    def multiplier(x):\n        return x * n   # n is captured\n    return multiplier\n\ndouble = make_multiplier(2)\ntriple = make_multiplier(3)\nprint(double(5))  # 10\nprint(triple(5))  # 15\n```",
      instructions: "## Task: Counter Closure\n1. Write `make_counter(start=0)` that returns an `increment()` function\n2. Each call to `increment()` adds 1 and returns the new value\n3. Create two independent counters and show they don't share state",
      starterCode: "def make_counter(start=0):\n    count = [___]  # use list to allow mutation\n\n    def increment():\n        count[0] += ___\n        return count[___]\n\n    return ___\n\ncounter_a = make_counter()\ncounter_b = make_counter(10)\n\nprint(counter_a())  # 1\nprint(counter_a())  # 2\nprint(counter_b())  # 11\nprint(counter_a())  # 3  (independent)\nprint(counter_b())  # 12",
      solution: "def make_counter(start=0):\n    count=[start]\n    def increment():\n        count[0]+=1\n        return count[0]\n    return increment\ncounter_a=make_counter()\ncounter_b=make_counter(10)\nprint(counter_a())\nprint(counter_a())\nprint(counter_b())\nprint(counter_a())\nprint(counter_b())",
      hint: "Use a list [start] so increment can modify it. Return the inner function.",
      rubric: "Closure captures count. Two independent counters. Correct sequence."
    },
    {
      title: "Decorators",
      theory: "## Decorators\n```python\nfrom functools import wraps\n\ndef timer(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        import time\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} took {time.time()-start:.4f}s')\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    import time; time.sleep(0.1)\n```",
      instructions: "## Task: Three Decorators\n1. `@log_call` — prints function name and args before calling\n2. `@validate_positive` — raises ValueError if any arg <= 0\n3. `@retry(times=3)` — retries function up to N times on exception\nTest each one.",
      starterCode: "from functools import wraps\n\ndef log_call(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.___}({args}, {kwargs})')\n        return ___(* args, **kwargs)\n    return wrapper\n\ndef validate_positive(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        for arg in args:\n            if arg <= 0:\n                raise ValueError(f'Argument {arg} must be positive')\n        return func(*___, **kwargs)\n    return wrapper\n\ndef retry(times=3):\n    def decorator(func):\n        @wraps(func)\n        def wrapper(*args, **kwargs):\n            for attempt in range(___):\n                try:\n                    return func(*args, **kwargs)\n                except Exception as e:\n                    print(f'Attempt {attempt+1} failed: {e}')\n                    if attempt == times - 1:\n                        raise\n        return wrapper\n    return ___\n\n@log_call\n@validate_positive\ndef divide(a, b):\n    return a / b\n\nprint(divide(10, 2))\n\n@retry(times=3)\ndef flaky():\n    import random\n    if random.random() < 0.7:\n        raise Exception('Random failure')\n    return 'Success!'\n\nprint(flaky())",
      solution: "from functools import wraps\ndef log_call(func):\n    @wraps(func)\n    def wrapper(*args,**kwargs):\n        print(f'Calling {func.__name__}({args},{kwargs})')\n        return func(*args,**kwargs)\n    return wrapper\ndef validate_positive(func):\n    @wraps(func)\n    def wrapper(*args,**kwargs):\n        for arg in args:\n            if arg<=0:raise ValueError(f'{arg} must be positive')\n        return func(*args,**kwargs)\n    return wrapper\ndef retry(times=3):\n    def decorator(func):\n        @wraps(func)\n        def wrapper(*args,**kwargs):\n            for attempt in range(times):\n                try:return func(*args,**kwargs)\n                except Exception as e:\n                    print(f'Attempt {attempt+1} failed:{e}')\n                    if attempt==times-1:raise\n        return wrapper\n    return decorator\n@log_call\n@validate_positive\ndef divide(a,b):\n    return a/b\nprint(divide(10,2))\n@retry(times=3)\ndef flaky():\n    import random\n    if random.random()<0.7:raise Exception('fail')\n    return 'Success!'\nprint(flaky())",
      hint: "@wraps preserves function metadata. retry returns decorator which returns wrapper.",
      rubric: "All 3 decorators work. @wraps used. retry is a decorator factory."
    }
  ]
},

"Concurrency in Python": {
  aiRubric: "Check threading, multiprocessing, asyncio basics.",
  lessons: [
    {
      title: "Threading",
      theory: "## Threading\n```python\nimport threading\n\ndef task(name, delay):\n    import time\n    time.sleep(delay)\n    print(f'{name} done')\n\nt1 = threading.Thread(target=task, args=('A', 1))\nt2 = threading.Thread(target=task, args=('B', 2))\nt1.start()\nt2.start()\nt1.join()\nt2.join()\nprint('All done')\n```\nGood for I/O-bound tasks (network, file).",
      instructions: "## Task: Concurrent Downloads (simulated)\n1. Write `download(url, delay)` that sleeps for `delay` then prints 'Downloaded: url'\n2. Create 4 threads for different URLs\n3. Time the total execution with `time.time()`\n4. Show threads run concurrently (total time < sum of delays)",
      starterCode: "import threading\nimport time\n\ndef download(url, delay):\n    time.sleep(___)\n    print(f'Downloaded: {url}')\n\nurls = [\n    ('https://api.example.com/data1', 1),\n    ('https://api.example.com/data2', 2),\n    ('https://api.example.com/data3', 1),\n    ('https://api.example.com/data4', 3),\n]\n\nstart = time.time()\n\nthreads = []\nfor url, delay in urls:\n    t = threading.___(target=___, args=(url, delay))\n    threads.append(t)\n    t.start()\n\nfor t in ___:\n    t.___()\n\nprint(f'All done in {time.time()-start:.2f}s (vs {sum(d for _,d in urls)}s sequential)')",
      solution: "import threading,time\ndef download(url,delay):\n    time.sleep(delay)\n    print(f'Downloaded: {url}')\nurls=[('https://api.example.com/data1',1),('https://api.example.com/data2',2),('https://api.example.com/data3',1),('https://api.example.com/data4',3)]\nstart=time.time()\nthreads=[]\nfor url,delay in urls:\n    t=threading.Thread(target=download,args=(url,delay))\n    threads.append(t)\n    t.start()\nfor t in threads:\n    t.join()\nprint(f'All done in {time.time()-start:.2f}s')",
      hint: "Thread(target=fn, args=(...)). t.start() launches. t.join() waits for completion.",
      rubric: "Thread created with target/args. All started. All joined. Timing shown."
    },
    {
      title: "Async/Await Basics",
      theory: "## asyncio\n```python\nimport asyncio\n\nasync def fetch(url):\n    await asyncio.sleep(1)  # simulates I/O\n    return f'data from {url}'\n\nasync def main():\n    results = await asyncio.gather(\n        fetch('url1'),\n        fetch('url2'),\n        fetch('url3')\n    )\n    print(results)\n\nasyncio.run(main())\n```\n`async def` defines a coroutine. `await` suspends it. `gather` runs concurrently.",
      instructions: "## Task: Async Student Fetcher\n1. Write `async fetch_student(id)` — awaits asyncio.sleep(0.5) then returns student dict\n2. Write `async main()` — fetches students 1-5 concurrently using `asyncio.gather`\n3. Time the execution (should be ~0.5s not 2.5s)\n4. Run with `asyncio.run(main())`",
      starterCode: "import asyncio\nimport time\n\nasync def fetch_student(student_id):\n    await asyncio.sleep(___)\n    return {'id': student_id, 'name': f'Student {student_id}', 'score': student_id * 10}\n\nasync def main():\n    start = time.time()\n\n    results = await asyncio.___(\n        *[fetch_student(i) for i in range(1, 6)]\n    )\n\n    print(f'Fetched {len(results)} students in {time.time()-start:.2f}s')\n    for student in results:\n        print(student)\n\nasyncio.___(main())",
      solution: "import asyncio,time\nasync def fetch_student(sid):\n    await asyncio.sleep(0.5)\n    return {'id':sid,'name':f'Student {sid}','score':sid*10}\nasync def main():\n    start=time.time()\n    results=await asyncio.gather(*[fetch_student(i) for i in range(1,6)])\n    print(f'Fetched {len(results)} in {time.time()-start:.2f}s')\n    for s in results:print(s)\nasyncio.run(main())",
      hint: "asyncio.gather(*coroutines) runs all concurrently. asyncio.run() starts the event loop.",
      rubric: "async def used. await asyncio.sleep. gather with spread. asyncio.run."
    }
  ]
},

"Design Patterns": {
  aiRubric: "Check pattern structure, intent understood, implementation correct.",
  lessons: [
    {
      title: "Singleton Pattern",
      theory: "## Singleton\nEnsures only ONE instance of a class exists:\n```python\nclass Singleton:\n    _instance = None\n\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance\n\na = Singleton()\nb = Singleton()\nprint(a is b)  # True — same object!\n```",
      instructions: "## Task: Database Connection Singleton\n1. Create `DatabaseConnection` singleton\n2. Store `host`, `port`, `connected=False`\n3. Add `connect()` and `disconnect()` methods\n4. Prove that two 'instances' share state",
      starterCode: "class DatabaseConnection:\n    _instance = ___\n\n    def __new__(cls):\n        if cls._instance is ___:\n            cls._instance = super().__new__(cls)\n            cls._instance.host = 'localhost'\n            cls._instance.port = 5432\n            cls._instance.connected = False\n        return cls.___\n\n    def connect(self):\n        self.connected = ___\n        print(f'Connected to {self.host}:{self.port}')\n\n    def disconnect(self):\n        self.connected = ___\n        print('Disconnected')\n\ndb1 = DatabaseConnection()\ndb2 = DatabaseConnection()\n\nprint(db1 is db2)   # True\ndb1.connect()\nprint(db2.connected)  # True — shared state!\ndb2.disconnect()\nprint(db1.connected)  # False",
      solution: "class DatabaseConnection:\n    _instance=None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance=super().__new__(cls)\n            cls._instance.host='localhost'\n            cls._instance.port=5432\n            cls._instance.connected=False\n        return cls._instance\n    def connect(self):\n        self.connected=True\n        print(f'Connected to {self.host}:{self.port}')\n    def disconnect(self):\n        self.connected=False\n        print('Disconnected')\ndb1=DatabaseConnection()\ndb2=DatabaseConnection()\nprint(db1 is db2)\ndb1.connect()\nprint(db2.connected)\ndb2.disconnect()\nprint(db1.connected)",
      hint: "_instance = None at class level. __new__ checks if None. Returns cls._instance.",
      rubric: "Singleton __new__ correct. _instance check. Shared state demonstrated."
    },
    {
      title: "Observer Pattern",
      theory: "## Observer\nObjects subscribe to events and get notified:\n```python\nclass EventEmitter:\n    def __init__(self):\n        self._listeners = {}\n\n    def on(self, event, callback):\n        self._listeners.setdefault(event, []).append(callback)\n\n    def emit(self, event, data=None):\n        for cb in self._listeners.get(event, []):\n            cb(data)\n```",
      instructions: "## Task: Student Grade Notifier\n1. Create `GradeBook` with `subscribe(event, callback)` and `record_grade(student, score)`\n2. When grade > 90, emit 'distinction'\n3. When grade < 60, emit 'at_risk'\n4. Subscribe email and SMS handlers to each event",
      starterCode: "class GradeBook:\n    def __init__(self):\n        self._listeners = {}\n\n    def subscribe(self, event, callback):\n        self._listeners.setdefault(___, []).append(___)\n\n    def record_grade(self, student, score):\n        print(f'Recorded: {student} = {score}')\n        if score > ___:\n            self._emit('distinction', {'student':student,'score':score})\n        elif score < ___:\n            self._emit('at_risk', {'student':student,'score':score})\n\n    def _emit(self, event, data):\n        for cb in self._listeners.get(___, []):\n            cb(___)\n\ngb = GradeBook()\ngb.subscribe('distinction', lambda d: print(f'EMAIL: {d[\"student\"]} got distinction!'))\ngb.subscribe('at_risk',     lambda d: print(f'SMS:   {d[\"student\"]} is at risk!'))\n\ngb.record_grade('Ada', 95)\ngb.record_grade('Tunde', 55)\ngb.record_grade('Ngozi', 75)",
      solution: "class GradeBook:\n    def __init__(self):\n        self._listeners={}\n    def subscribe(self,event,callback):\n        self._listeners.setdefault(event,[]).append(callback)\n    def record_grade(self,student,score):\n        print(f'Recorded:{student}={score}')\n        if score>90:self._emit('distinction',{'student':student,'score':score})\n        elif score<60:self._emit('at_risk',{'student':student,'score':score})\n    def _emit(self,event,data):\n        for cb in self._listeners.get(event,[]):\n            cb(data)\ngb=GradeBook()\ngb.subscribe('distinction',lambda d:print(f'EMAIL:{d[\"student\"]} distinction!'))\ngb.subscribe('at_risk',lambda d:print(f'SMS:{d[\"student\"]} at risk!'))\ngb.record_grade('Ada',95)\ngb.record_grade('Tunde',55)\ngb.record_grade('Ngozi',75)",
      hint: "setdefault creates empty list if key missing. _emit loops callbacks. Both events test.",
      rubric: "subscribe adds to listeners. record_grade emits correct event. _emit calls all callbacks."
    }
  ]
},

"Metaprogramming": {
  aiRubric: "Check __getattr__, __setattr__, type(), metaclass basics.",
  lessons: [
    {
      title: "Dynamic Attributes",
      theory: "## __getattr__ & __setattr__\n```python\nclass DynamicConfig:\n    def __init__(self):\n        self._data = {}\n\n    def __getattr__(self, name):\n        if name.startswith('_'):\n            raise AttributeError(name)\n        return self._data.get(name, f'No {name}')\n\n    def __setattr__(self, name, value):\n        if name.startswith('_'):\n            super().__setattr__(name, value)\n        else:\n            self._data[name] = value\n\nc = DynamicConfig()\nc.host = 'localhost'\nprint(c.host)    # localhost\nprint(c.missing) # No missing\n```",
      instructions: "## Task: Config Object\nCreate `Config` where you can set and get any attribute dynamically:\n1. Uses `_data` dict internally\n2. `to_dict()` returns all settings\n3. `from_dict(d)` loads settings from a dict\n4. Test with database config settings",
      starterCode: "class Config:\n    def __init__(self):\n        object.__setattr__(self, '_data', {})\n\n    def __getattr__(self, name):\n        return self._data.get(___, None)\n\n    def __setattr__(self, name, value):\n        self._data[___] = value\n\n    def to_dict(self):\n        return dict(self.___)\n\n    @classmethod\n    def from_dict(cls, d):\n        config = cls()\n        for key, value in d.___():\n            setattr(config, key, value)\n        return config\n\ncfg = Config()\ncfg.host = 'localhost'\ncfg.port = 5432\ncfg.debug = True\n\nprint(cfg.host)\nprint(cfg.to_dict())\n\ncfg2 = Config.from_dict({'name':'Mabel','version':'1.0'})\nprint(cfg2.name)\nprint(cfg2.to_dict())",
      solution: "class Config:\n    def __init__(self):\n        object.__setattr__(self,'_data',{})\n    def __getattr__(self,name):\n        return self._data.get(name,None)\n    def __setattr__(self,name,value):\n        self._data[name]=value\n    def to_dict(self):\n        return dict(self._data)\n    @classmethod\n    def from_dict(cls,d):\n        config=cls()\n        for key,value in d.items():\n            setattr(config,key,value)\n        return config\ncfg=Config()\ncfg.host='localhost'\ncfg.port=5432\ncfg.debug=True\nprint(cfg.host)\nprint(cfg.to_dict())\ncfg2=Config.from_dict({'name':'Mabel','version':'1.0'})\nprint(cfg2.name)\nprint(cfg2.to_dict())",
      hint: "Use object.__setattr__ to set _data without recursion. from_dict uses setattr().",
      rubric: "__getattr__ and __setattr__ correct. to_dict returns copy. from_dict loads from dict."
    }
  ]
},

"Memory & Performance": {
  aiRubric: "Check profiling, slots, generators vs lists, caching.",
  lessons: [
    {
      title: "Profiling & Optimization",
      theory: "## Performance Tools\n```python\nimport timeit\nimport cProfile\n\n# Time a snippet\nt = timeit.timeit('sum(range(1000))', number=10000)\nprint(f'{t:.4f}s')\n\n# Profile a function\ncProfile.run('my_function()')\n\n# Memory efficient: use generators\nbig_list = [x**2 for x in range(1000000)]  # lots of RAM\nbig_gen  = (x**2 for x in range(1000000))  # tiny RAM\n```",
      instructions: "## Task: Compare Performance\n1. Compare list comprehension vs generator for sum of squares 1-1,000,000\n2. Use `timeit` to compare both\n3. Use `sys.getsizeof` to compare memory\n4. Use `functools.lru_cache` to speed up recursive fibonacci",
      starterCode: "import timeit, sys\nfrom functools import lru_cache\n\n# 1. List vs Generator sum\nlist_sum = sum([x**2 for x in range(1_000_000)])\ngen_sum  = sum(___ for x in range(1_000_000))\nprint(list_sum == gen_sum)  # True\n\n# 2. Time comparison\nlist_time = timeit.timeit('[x**2 for x in range(10000)]', number=100)\ngen_time  = timeit.timeit('sum(x**2 for x in range(10000))', number=100)\nprint(f'List: {list_time:.3f}s  Gen: {gen_time:.3f}s')\n\n# 3. Memory\nmy_list = [x**2 for x in range(1000)]\nmy_gen  = (x**2 for x in range(1000))\nprint(f'List size: {sys.getsizeof(___)} bytes')\nprint(f'Gen size:  {sys.getsizeof(___)} bytes')\n\n# 4. Cached fibonacci\n@___\ndef fib(n):\n    if n <= 1: return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(50))",
      solution: "import timeit,sys\nfrom functools import lru_cache\nlist_sum=sum([x**2 for x in range(1_000_000)])\ngen_sum=sum(x**2 for x in range(1_000_000))\nprint(list_sum==gen_sum)\nlist_time=timeit.timeit('[x**2 for x in range(10000)]',number=100)\ngen_time=timeit.timeit('sum(x**2 for x in range(10000))',number=100)\nprint(f'List:{list_time:.3f}s Gen:{gen_time:.3f}s')\nmy_list=[x**2 for x in range(1000)]\nmy_gen=(x**2 for x in range(1000))\nprint(f'List:{sys.getsizeof(my_list)} bytes')\nprint(f'Gen:{sys.getsizeof(my_gen)} bytes')\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n<=1:return n\n    return fib(n-1)+fib(n-2)\nprint(fib(50))",
      hint: "Generator expression uses () not []. sys.getsizeof measures bytes. @lru_cache before def.",
      rubric: "Generator expression correct. timeit used. getsizeof compared. lru_cache applied."
    }
  ]
},



// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// BACKEND — BEGINNER
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Intro to Backend": {
  aiRubric: "Check understanding of client-server, request-response, server-side code.",
  lessons: [
    {
      title: "What is Backend Development?",
      theory: "## Backend vs Frontend\n- **Frontend** — what users see (HTML, CSS, JS)\n- **Backend** — the server, database, business logic\n\n**Request-Response cycle:**\n1. Browser sends HTTP request to server\n2. Server processes it (auth, DB query, logic)\n3. Server sends back HTTP response (JSON or HTML)\n\nBackend handles:\n- User authentication\n- Data storage & retrieval\n- Business rules\n- API endpoints for mobile/web apps",
      instructions: "## Task: Simulate a Backend\nWrite Python code that simulates what a backend does:\n1. A `users` database (dict)\n2. A `register(username, password)` function that validates and stores a user\n3. A `login(username, password)` function that returns a 'token'\n4. A `get_profile(token)` function that returns user data if token is valid",
      starterCode: "import hashlib\n\nusers = {}  # our 'database'\ntokens = {} # active sessions\n\ndef register(username, password):\n    if username in ___:\n        return {'error': 'User already exists'}\n    if len(password) < 8:\n        return {'error': 'Password too short'}\n    hashed = hashlib.sha256(password.encode()).___\n    users[username] = {'password': hashed, 'joined': '2024-01-01'}\n    return {'success': True, 'user': ___}\n\ndef login(username, password):\n    user = users.get(___)\n    if not user:\n        return {'error': 'User not found'}\n    hashed = hashlib.sha256(password.encode()).hexdigest()\n    if user['password'] != ___:\n        return {'error': 'Wrong password'}\n    token = f'token_{username}_abc123'\n    tokens[token] = ___\n    return {'token': token}\n\ndef get_profile(token):\n    username = tokens.get(___)\n    if not username:\n        return {'error': 'Invalid token'}\n    return {'username': username, 'joined': users[username]['joined']}\n\nprint(register('ada', 'password123'))\nprint(login('ada', 'password123'))\nprint(get_profile('token_ada_abc123'))\nprint(get_profile('fake_token'))",
      solution: "import hashlib\nusers={}\ntokens={}\ndef register(username,password):\n    if username in users:return{'error':'User exists'}\n    if len(password)<8:return{'error':'Password too short'}\n    hashed=hashlib.sha256(password.encode()).hexdigest()\n    users[username]={'password':hashed,'joined':'2024-01-01'}\n    return{'success':True,'user':username}\ndef login(username,password):\n    user=users.get(username)\n    if not user:return{'error':'Not found'}\n    hashed=hashlib.sha256(password.encode()).hexdigest()\n    if user['password']!=hashed:return{'error':'Wrong password'}\n    token=f'token_{username}_abc123'\n    tokens[token]=username\n    return{'token':token}\ndef get_profile(token):\n    username=tokens.get(token)\n    if not username:return{'error':'Invalid token'}\n    return{'username':username,'joined':users[username]['joined']}\nprint(register('ada','password123'))\nprint(login('ada','password123'))\nprint(get_profile('token_ada_abc123'))\nprint(get_profile('fake_token'))",
      hint: "hashlib.sha256(s.encode()).hexdigest() hashes a string. tokens maps token→username.",
      rubric: "register validates and hashes. login checks hash. get_profile uses token. All 4 tests."
    }
  ]
},

"HTTP & REST Concepts": {
  aiRubric: "Check HTTP methods, status codes, REST principles understanding.",
  lessons: [
    {
      title: "HTTP Methods & Status Codes",
      theory: "## HTTP Methods\n| Method | Use |\n|---|---|\n| GET | Read data |\n| POST | Create new |\n| PUT | Replace |\n| PATCH | Update part |\n| DELETE | Remove |\n\n## Status Codes\n| Code | Meaning |\n|---|---|\n| 200 | OK |\n| 201 | Created |\n| 400 | Bad Request |\n| 401 | Unauthorized |\n| 404 | Not Found |\n| 500 | Server Error |",
      instructions: "## Task: REST API Design\nDesign a Student CRUD API — write a Python dict describing each endpoint with method, path, description, and response code:\n\n- List all students\n- Get one student\n- Create a student\n- Update a student\n- Delete a student",
      starterCode: "api_endpoints = [\n    {\n        'method': 'GET',\n        'path': '/students/',\n        'description': 'List all students',\n        'success_code': ___,\n        'error_codes': [401]\n    },\n    {\n        'method': ___,\n        'path': '/students/{id}/',\n        'description': 'Get one student by ID',\n        'success_code': 200,\n        'error_codes': [___, 401]\n    },\n    {\n        'method': ___,\n        'path': '/students/',\n        'description': 'Create new student',\n        'success_code': ___,\n        'error_codes': [400, 401]\n    },\n    {\n        'method': ___,\n        'path': '/students/{id}/',\n        'description': 'Update student',\n        'success_code': 200,\n        'error_codes': [400, 404]\n    },\n    {\n        'method': ___,\n        'path': '/students/{id}/',\n        'description': 'Delete student',\n        'success_code': ___,\n        'error_codes': [404]\n    }\n]\n\nfor ep in api_endpoints:\n    print(f\"{ep['method']:6} {ep['path']:25} -> {ep['success_code']} | {ep['description']}\")",
      solution: "api_endpoints=[{'method':'GET','path':'/students/','description':'List all students','success_code':200,'error_codes':[401]},{'method':'GET','path':'/students/{id}/','description':'Get one student','success_code':200,'error_codes':[404,401]},{'method':'POST','path':'/students/','description':'Create student','success_code':201,'error_codes':[400,401]},{'method':'PATCH','path':'/students/{id}/','description':'Update student','success_code':200,'error_codes':[400,404]},{'method':'DELETE','path':'/students/{id}/','description':'Delete student','success_code':204,'error_codes':[404]}]\nfor ep in api_endpoints:\n    print(f\"{ep['method']:6} {ep['path']:25} -> {ep['success_code']} | {ep['description']}\")",
      hint: "GET=read, POST=create(201), PATCH=update, DELETE=204. 404 for not found.",
      rubric: "Correct methods. 201 for POST. 204 for DELETE. 404 in error codes."
    }
  ]
},

"Python for Web": {
  aiRubric: "Check requests library usage, JSON parsing, basic web concepts.",
  lessons: [
    {
      title: "Making HTTP Requests with Python",
      theory: "## requests Library\n```python\nimport requests\n\n# GET\nres = requests.get('https://api.example.com/data')\nprint(res.status_code)   # 200\nprint(res.json())        # parse JSON\n\n# POST with JSON body\nres = requests.post(\n    'https://api.example.com/users',\n    json={'name': 'Ada', 'email': 'ada@example.com'},\n    headers={'Authorization': 'Bearer token123'}\n)\nprint(res.status_code)   # 201\n```\nInstall: `pip install requests`",
      instructions: "## Task: Public API Client\nUse the JSONPlaceholder free API (`https://jsonplaceholder.typicode.com`):\n1. GET all users: `/users`\n2. GET one user: `/users/1`\n3. POST a new todo: `/todos` with `{title, completed, userId}`\n4. Print name and email of first 3 users",
      starterCode: "import requests\n\nBASE = 'https://jsonplaceholder.typicode.com'\n\n# 1. Get all users\nres = requests.___(f'{BASE}/users')\nusers = res.___()\nprint(f'Total users: {len(users)}')\n\n# 2. Get user 1\nres = requests.get(f'{BASE}/users/___')\nuser = res.json()\nprint(f'User 1: {user[___]} ({user[___]})')\n\n# 3. First 3 names and emails\nfor user in users[___:___]:\n    print(f'{user[\"name\"]:20} | {user[\"email\"]}')\n\n# 4. POST new todo\nnew_todo = {'title': 'Learn FastAPI', 'completed': False, 'userId': 1}\nres = requests.post(f'{BASE}/todos', json=___)\nprint(f'Created todo: {res.json()}')\nprint(f'Status: {res.___}')",
      solution: "import requests\nBASE='https://jsonplaceholder.typicode.com'\nres=requests.get(f'{BASE}/users')\nusers=res.json()\nprint(f'Total:{len(users)}')\nres=requests.get(f'{BASE}/users/1')\nuser=res.json()\nprint(f'User 1:{user[\"name\"]} ({user[\"email\"]})')\nfor user in users[0:3]:\n    print(f'{user[\"name\"]:20}|{user[\"email\"]}')\nnew_todo={'title':'Learn FastAPI','completed':False,'userId':1}\nres=requests.post(f'{BASE}/todos',json=new_todo)\nprint(f'Created:{res.json()}')\nprint(f'Status:{res.status_code}')",
      hint: "requests.get(url).json() parses response. Post with json=dict. res.status_code.",
      rubric: "GET all users. GET one user. First 3 printed. POST with json. status_code checked."
    }
  ]
},

"JSON & APIs": {
  aiRubric: "Check json.dumps, json.loads, API response handling.",
  lessons: [
    {
      title: "Working with JSON",
      theory: "## JSON in Python\n```python\nimport json\n\n# Python dict to JSON string\ndata = {'name': 'Ada', 'score': 88}\njson_str = json.dumps(data, indent=2)\nprint(json_str)\n\n# JSON string to Python dict\nparsed = json.loads(json_str)\nprint(parsed['name'])  # Ada\n\n# Write to file\nwith open('data.json', 'w') as f:\n    json.dump(data, f, indent=2)\n\n# Read from file\nwith open('data.json') as f:\n    loaded = json.load(f)\n```",
      instructions: "## Task: Student JSON Database\n1. Create a list of 3 student dicts\n2. Write to `students.json` with indent=2\n3. Read it back\n4. Add a new student and save again\n5. Filter and print students with score >= 80",
      starterCode: "import json\n\nstudents = [\n    {'id':1, 'name':'Ada',   'course':'Python', 'score':88},\n    {'id':2, 'name':'Tunde', 'course':'SQL',    'score':72},\n    {'id':3, 'name':'Ngozi', 'course':'Python', 'score':95}\n]\n\n# Write to file\nwith open('students.json', ___) as f:\n    json.___(students, f, indent=___)\n\n# Read back\nwith open('students.json', ___) as f:\n    loaded = json.___(f)\nprint(f'Loaded {len(loaded)} students')\n\n# Add new student\nnew_student = {'id':4,'name':'Emeka','course':'FastAPI','score':79}\nloaded.___(new_student)\n\n# Save updated\nwith open('students.json','w') as f:\n    json.dump(loaded, f, indent=2)\n\n# Filter high scorers\nhigh = [s for s in loaded if s['score'] >= ___]\nprint('High scorers:')\nfor s in high:\n    print(f'  {s[\"name\"]}: {s[\"score\"]}')",
      solution: "import json\nstudents=[{'id':1,'name':'Ada','course':'Python','score':88},{'id':2,'name':'Tunde','course':'SQL','score':72},{'id':3,'name':'Ngozi','course':'Python','score':95}]\nwith open('students.json','w') as f:\n    json.dump(students,f,indent=2)\nwith open('students.json') as f:\n    loaded=json.load(f)\nprint(f'Loaded {len(loaded)}')\nnew={'id':4,'name':'Emeka','course':'FastAPI','score':79}\nloaded.append(new)\nwith open('students.json','w') as f:\n    json.dump(loaded,f,indent=2)\nhigh=[s for s in loaded if s['score']>=80]\nprint('High scorers:')\nfor s in high:print(f'  {s[\"name\"]}:{s[\"score\"]}')",
      hint: "json.dump() writes to file. json.load() reads from file. append() adds to list.",
      rubric: "json.dump with indent. json.load. append new student. Filter and print."
    }
  ]
},

"Environment & Setup": {
  aiRubric: "Check virtual environments, pip, .env files, environment variables.",
  lessons: [
    {
      title: "Virtual Environments & pip",
      theory: "## Virtual Environments\n```bash\n# Create\npython -m venv venv\n\n# Activate\nsource venv/bin/activate        # Mac/Linux\nvenv\\Scripts\\activate            # Windows\n\n# Install packages\npip install fastapi uvicorn\n\n# Save dependencies\npip freeze > requirements.txt\n\n# Install from requirements\npip install -r requirements.txt\n```\nAlways use a venv — never install globally!",
      instructions: "## Task: Environment Config\nWrite Python code that:\n1. Uses `os.environ` to read environment variables\n2. Has fallback defaults for missing vars\n3. Creates a config dict from env vars\n4. Validates required variables exist",
      starterCode: "import os\n\ndef load_config():\n    config = {\n        'DATABASE_URL': os.environ.get('DATABASE_URL', 'sqlite:///default.db'),\n        'SECRET_KEY':   os.environ.get('SECRET_KEY', ___),\n        'DEBUG':        os.environ.get('DEBUG', 'True') == ___,\n        'PORT':         int(os.environ.get('PORT', ___)),\n        'API_KEY':      os.environ.get('API_KEY')  # required, no default\n    }\n    return config\n\ndef validate_config(config):\n    required = ['DATABASE_URL', 'SECRET_KEY', ___]\n    missing = [key for key in required if not config.get(key)]\n    if missing:\n        raise ValueError(f'Missing required env vars: {missing}')\n    return True\n\nconfig = load_config()\nfor key, val in config.items():\n    display = str(val)[:20] + '...' if val and len(str(val)) > 20 else val\n    print(f'{key:15} = {display}')\n\ntry:\n    validate_config(config)\n    print('Config valid!')\nexcept ValueError as e:\n    print(f'Config error: {e}')",
      solution: "import os\ndef load_config():\n    return{'DATABASE_URL':os.environ.get('DATABASE_URL','sqlite:///default.db'),'SECRET_KEY':os.environ.get('SECRET_KEY','dev-secret'),'DEBUG':os.environ.get('DEBUG','True')=='True','PORT':int(os.environ.get('PORT',8000)),'API_KEY':os.environ.get('API_KEY')}\ndef validate_config(config):\n    required=['DATABASE_URL','SECRET_KEY','PORT']\n    missing=[k for k in required if not config.get(k)]\n    if missing:raise ValueError(f'Missing:{missing}')\n    return True\nconfig=load_config()\nfor key,val in config.items():\n    print(f'{key:15}={val}')\ntry:\n    validate_config(config)\n    print('Config valid!')\nexcept ValueError as e:\n    print(f'Error:{e}')",
      hint: "os.environ.get(key, default). Validate required keys exist. PORT cast to int.",
      rubric: "os.environ.get with defaults. validate checks required. try/except for error."
    }
  ]
},

"Authentication & JWT": {
  aiRubric: "Check JWT creation, decoding, password hashing, protected routes.",
  lessons: [
    {
      title: "Password Hashing & JWT",
      theory: "## Auth Fundamentals\n```python\n# NEVER store plain passwords!\nimport hashlib, secrets\n\ndef hash_password(password):\n    salt = secrets.token_hex(16)\n    hashed = hashlib.sha256(f'{salt}{password}'.encode()).hexdigest()\n    return f'{salt}:{hashed}'\n\ndef verify_password(password, stored):\n    salt, hashed = stored.split(':')\n    return hashlib.sha256(f'{salt}{password}'.encode()).hexdigest() == hashed\n```",
      instructions: "## Task: Auth System\n1. `hash_password(password)` — returns `salt:hash`\n2. `verify_password(password, stored)` — returns True/False\n3. Simple `create_token(username)` using base64\n4. `decode_token(token)` — returns username\n5. Test registration + login flow",
      starterCode: "import hashlib, secrets, base64, json\n\ndef hash_password(password):\n    salt = secrets.token_hex(___)\n    hashed = hashlib.sha256(f'{___}{password}'.encode()).hexdigest()\n    return f'{salt}:{___}'\n\ndef verify_password(password, stored):\n    salt, hashed = stored.split(___)\n    check = hashlib.sha256(f'{salt}{password}'.encode()).hexdigest()\n    return check == ___\n\ndef create_token(username):\n    payload = json.dumps({'user': username, 'ts': 'now'})\n    return base64.b64encode(payload.encode()).decode()\n\ndef decode_token(token):\n    payload = base64.b64decode(token.encode()).decode()\n    return json.loads(payload)[___]\n\n# Test\npassword = 'MySecret123'\nstored = hash_password(___)\nprint('Stored:', stored)\nprint('Valid login:', verify_password('MySecret123', stored))\nprint('Wrong login:', verify_password('WrongPass', stored))\n\ntoken = create_token('ada')\nprint('Token:', token)\nprint('Decoded user:', decode_token(token))",
      solution: "import hashlib,secrets,base64,json\ndef hash_password(password):\n    salt=secrets.token_hex(16)\n    hashed=hashlib.sha256(f'{salt}{password}'.encode()).hexdigest()\n    return f'{salt}:{hashed}'\ndef verify_password(password,stored):\n    salt,hashed=stored.split(':')\n    check=hashlib.sha256(f'{salt}{password}'.encode()).hexdigest()\n    return check==hashed\ndef create_token(username):\n    payload=json.dumps({'user':username,'ts':'now'})\n    return base64.b64encode(payload.encode()).decode()\ndef decode_token(token):\n    payload=base64.b64decode(token.encode()).decode()\n    return json.loads(payload)['user']\npassword='MySecret123'\nstored=hash_password(password)\nprint('Stored:',stored)\nprint('Valid:',verify_password('MySecret123',stored))\nprint('Wrong:',verify_password('WrongPass',stored))\ntoken=create_token('ada')\nprint('Token:',token)\nprint('User:',decode_token(token))",
      hint: "salt:hash split by ':'. base64.b64encode then decode() for string. json.loads for payload.",
      rubric: "hash_password salts correctly. verify_password checks. token base64 encoded. decode works."
    }
  ]
},

"Database Integration": {
  aiRubric: "Check sqlite3 usage, CRUD operations, parameterized queries.",
  lessons: [
    {
      title: "SQLite with Python",
      theory: "## sqlite3\n```python\nimport sqlite3\n\n# Connect and create table\nconn = sqlite3.connect('school.db')\ncursor = conn.cursor()\n\ncursor.execute('''\n    CREATE TABLE IF NOT EXISTS students (\n        id    INTEGER PRIMARY KEY AUTOINCREMENT,\n        name  TEXT NOT NULL,\n        score INTEGER DEFAULT 0\n    )\n''')\nconn.commit()\n\n# Insert (use ? to prevent SQL injection)\ncursor.execute('INSERT INTO students (name, score) VALUES (?, ?)', ('Ada', 88))\nconn.commit()\n\n# Query\ncursor.execute('SELECT * FROM students WHERE score > ?', (70,))\nrows = cursor.fetchall()\nconn.close()\n```",
      instructions: "## Task: Student Database\n1. Create `students` table with id, name, course, score\n2. Insert 4 students\n3. Query students with score >= 80\n4. Update Ada's score to 95\n5. Delete students with score < 60\n6. Print all remaining students",
      starterCode: "import sqlite3\n\nconn = sqlite3.connect(':memory:')  # in-memory for testing\nconn.row_factory = sqlite3.Row      # access columns by name\ncursor = conn.cursor()\n\n# Create table\ncursor.execute('''\n    CREATE TABLE students (\n        id     INTEGER PRIMARY KEY AUTOINCREMENT,\n        name   TEXT NOT NULL,\n        course TEXT,\n        score  INTEGER DEFAULT 0\n    )\n''')\n\n# Insert students\nstudents_data = [\n    ('Ada',   'Python', 88),\n    ('Tunde', 'SQL',    72),\n    ('Ngozi', 'Python', 95),\n    ('Emeka', 'FastAPI', 45)\n]\ncursor.executemany('INSERT INTO students (name, course, score) VALUES (?, ?, ?)', ___)\nconn.commit()\n\n# Query high scorers\ncursor.execute('SELECT * FROM students WHERE score >= ?', (___,))\nprint('High scorers:')\nfor row in cursor.fetchall():\n    print(f'  {row[\"name\"]}: {row[\"score\"]}')\n\n# Update Ada\ncursor.execute('UPDATE students SET score = ? WHERE name = ?', (___, ___))\nconn.commit()\n\n# Delete low scorers\ncursor.execute('DELETE FROM students WHERE score < ?', (60,))\nconn.commit()\n\n# Print all\ncursor.execute('SELECT * FROM students ORDER BY score DESC')\nprint('All students:')\nfor row in cursor.fetchall():\n    print(f'  {dict(row)}')\n\nconn.close()",
      solution: "import sqlite3\nconn=sqlite3.connect(':memory:')\nconn.row_factory=sqlite3.Row\ncursor=conn.cursor()\ncursor.execute('CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,course TEXT,score INTEGER DEFAULT 0)')\nstudents_data=[('Ada','Python',88),('Tunde','SQL',72),('Ngozi','Python',95),('Emeka','FastAPI',45)]\ncursor.executemany('INSERT INTO students(name,course,score) VALUES(?,?,?)',students_data)\nconn.commit()\ncursor.execute('SELECT * FROM students WHERE score>=?',(80,))\nprint('High scorers:')\nfor row in cursor.fetchall():print(f'  {row[\"name\"]}:{row[\"score\"]}')\ncursor.execute('UPDATE students SET score=? WHERE name=?',(95,'Ada'))\nconn.commit()\ncursor.execute('DELETE FROM students WHERE score<?',(60,))\nconn.commit()\ncursor.execute('SELECT * FROM students ORDER BY score DESC')\nprint('All:')\nfor row in cursor.fetchall():print(f'  {dict(row)}')\nconn.close()",
      hint: "Use ? placeholders always. executemany for bulk insert. row_factory=sqlite3.Row for dict access.",
      rubric: "Table created. executemany insert. SELECT with ?. UPDATE. DELETE. Final SELECT."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// BACKEND — ADVANCED (missing)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Async Python": {
  aiRubric: "Check async def, await, asyncio.gather, aiohttp usage.",
  lessons: [
    {
      title: "Async Web Requests with aiohttp",
      theory: "## aiohttp — Async HTTP\n```python\nimport aiohttp, asyncio\n\nasync def fetch(session, url):\n    async with session.get(url) as response:\n        return await response.json()\n\nasync def main():\n    async with aiohttp.ClientSession() as session:\n        data = await fetch(session, 'https://api.example.com')\n        print(data)\n\nasyncio.run(main())\n```\nInstall: `pip install aiohttp`",
      instructions: "## Task: Concurrent API Calls\n1. Fetch 5 posts from JSONPlaceholder concurrently\n2. Use `aiohttp.ClientSession` and `asyncio.gather`\n3. Print title of each post\n4. Time the execution vs sequential",
      starterCode: "import asyncio\nimport aiohttp\nimport time\n\nasync def fetch_post(session, post_id):\n    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'\n    async with session.___(url) as res:\n        return await res.___()\n\nasync def main():\n    start = time.time()\n    async with aiohttp.ClientSession() as ___:\n        tasks = [fetch_post(session, i) for i in range(1, 6)]\n        posts = await asyncio.___(*tasks)\n    print(f'Fetched {len(posts)} posts in {time.time()-start:.2f}s')\n    for post in posts:\n        print(f'  [{post[\"id\"]}] {post[\"title\"][:50]}')\n\nasyncio.___(main())",
      solution: "import asyncio,aiohttp,time\nasync def fetch_post(session,post_id):\n    url=f'https://jsonplaceholder.typicode.com/posts/{post_id}'\n    async with session.get(url) as res:\n        return await res.json()\nasync def main():\n    start=time.time()\n    async with aiohttp.ClientSession() as session:\n        tasks=[fetch_post(session,i) for i in range(1,6)]\n        posts=await asyncio.gather(*tasks)\n    print(f'Fetched {len(posts)} in {time.time()-start:.2f}s')\n    for post in posts:\n        print(f'  [{post[\"id\"]}] {post[\"title\"][:50]}')\nasyncio.run(main())",
      hint: "session.get(url) for GET. await res.json() parses. gather(*tasks) runs concurrently.",
      rubric: "aiohttp ClientSession. async with. gather used. asyncio.run. Timing shown."
    }
  ]
},

"API Security & Rate Limiting": {
  aiRubric: "Check rate limiting logic, API key validation, input sanitization.",
  lessons: [
    {
      title: "Rate Limiting & API Keys",
      theory: "## API Security Basics\n```python\nfrom fastapi import FastAPI, HTTPException, Header\nfrom collections import defaultdict\nimport time\n\napp = FastAPI()\nrequest_counts = defaultdict(list)\n\ndef is_rate_limited(ip: str, limit: int = 10, window: int = 60) -> bool:\n    now = time.time()\n    # Remove old requests outside window\n    request_counts[ip] = [t for t in request_counts[ip] if now - t < window]\n    if len(request_counts[ip]) >= limit:\n        return True\n    request_counts[ip].append(now)\n    return False\n```",
      instructions: "## Task: Secure FastAPI\n1. `validate_api_key(key)` — checks against known keys\n2. `rate_limit(ip)` — max 5 requests per 60s per IP\n3. Apply both to a `/data` endpoint\n4. Test with valid/invalid key and excessive requests",
      starterCode: "from fastapi import FastAPI, HTTPException, Header\nfrom collections import defaultdict\nimport time\n\napp = FastAPI()\n\nVALID_API_KEYS = {'key-ada-123', 'key-mabel-456'}\nrequest_log = defaultdict(list)\n\ndef validate_api_key(api_key: str):\n    if api_key not in ___:\n        raise HTTPException(status_code=___, detail='Invalid API key')\n\ndef rate_limit(client_ip: str, limit: int = 5, window: int = 60):\n    now = time.time()\n    request_log[client_ip] = [t for t in request_log[client_ip] if now - t < ___]\n    if len(request_log[client_ip]) >= ___:\n        raise HTTPException(status_code=___, detail='Rate limit exceeded')\n    request_log[client_ip].append(now)\n\n@app.get('/data')\ndef get_data(\n    x_api_key: str = Header(...),\n    x_forwarded_for: str = Header(default='127.0.0.1')\n):\n    validate_api_key(___)\n    rate_limit(___)\n    return {'data': 'Here is your data', 'key': x_api_key}",
      solution: "from fastapi import FastAPI,HTTPException,Header\nfrom collections import defaultdict\nimport time\napp=FastAPI()\nVALID_API_KEYS={'key-ada-123','key-mabel-456'}\nrequest_log=defaultdict(list)\ndef validate_api_key(api_key:str):\n    if api_key not in VALID_API_KEYS:\n        raise HTTPException(status_code=401,detail='Invalid API key')\ndef rate_limit(client_ip:str,limit:int=5,window:int=60):\n    now=time.time()\n    request_log[client_ip]=[t for t in request_log[client_ip] if now-t<window]\n    if len(request_log[client_ip])>=limit:\n        raise HTTPException(status_code=429,detail='Rate limit exceeded')\n    request_log[client_ip].append(now)\n@app.get('/data')\ndef get_data(x_api_key:str=Header(...),x_forwarded_for:str=Header(default='127.0.0.1')):\n    validate_api_key(x_api_key)\n    rate_limit(x_forwarded_for)\n    return{'data':'Here is your data','key':x_api_key}",
      hint: "401 for invalid key. 429 for rate limit exceeded. Filter old timestamps with window.",
      rubric: "VALID_API_KEYS check. 401 raised. rate_limit filters old times. 429 raised."
    }
  ]
},

"Deployment & Docker": {
  aiRubric: "Check Dockerfile syntax, docker commands, requirements.txt, environment variables.",
  lessons: [
    {
      title: "Dockerizing a FastAPI App",
      theory: "## Docker Basics\n```dockerfile\nFROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nEXPOSE 8000\nCMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n```\n```bash\ndocker build -t myapp .\ndocker run -p 8000:8000 myapp\ndocker run -e DATABASE_URL=... myapp\n```",
      instructions: "## Task: Production Setup\nWrite all the files needed to deploy a FastAPI app:\n1. `main.py` — a simple FastAPI app with health check\n2. `requirements.txt` — with fastapi and uvicorn\n3. `Dockerfile` — multi-stage build\n4. `.env` file — with PORT and DEBUG\n5. A startup script",
      starterCode: "# Write the content of each file as a Python string\n# then print them\n\nmain_py = '''\nfrom fastapi import FastAPI\nimport os\n\napp = FastAPI(title='Mabel Academy API')\n\n@app.get('/')\ndef root():\n    return {'status': 'ok', 'version': '1.0'}\n\n@app.get('/health')\ndef health():\n    return {'healthy': True, 'debug': os.getenv('DEBUG', 'False')}\n'''\n\nrequirements = '''\nfastapi==___\nuvicorn==___\npython-dotenv==___\n'''\n\ndockerfile = '''\nFROM python:___-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nEXPOSE ___\nCMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"___\"]\n'''\n\ndotenv = '''\nPORT=8000\nDEBUG=False\nDATABASE_URL=sqlite:///prod.db\nSECRET_KEY=change-me-in-production\n'''\n\nfor name, content in [('main.py',main_py),('requirements.txt',requirements),('Dockerfile',dockerfile),('.env',dotenv)]:\n    print(f'=== {name} ===')\n    print(content.strip())\n    print()",
      solution: "main_py='\\nfrom fastapi import FastAPI\\nimport os\\napp=FastAPI(title=\"Mabel Academy\")\\n@app.get(\"/\")\\ndef root():return{\"status\":\"ok\"}\\n@app.get(\"/health\")\\ndef health():return{\"healthy\":True,\"debug\":os.getenv(\"DEBUG\",\"False\")}\\n'\nrequirements='fastapi==0.104.1\\nuvicorn==0.24.0\\npython-dotenv==1.0.0\\n'\ndockerfile='FROM python:3.11-slim\\nWORKDIR /app\\nCOPY requirements.txt .\\nRUN pip install --no-cache-dir -r requirements.txt\\nCOPY . .\\nEXPOSE 8000\\nCMD [\"uvicorn\",\"main:app\",\"--host\",\"0.0.0.0\",\"--port\",\"8000\"]\\n'\ndotenv='PORT=8000\\nDEBUG=False\\nDATABASE_URL=sqlite:///prod.db\\nSECRET_KEY=change-me\\n'\nfor name,content in [('main.py',main_py),('requirements.txt',requirements),('Dockerfile',dockerfile),('.env',dotenv)]:\n    print(f'==={name}===')\n    print(content.strip())\n    print()",
      hint: "FROM python:3.11-slim. EXPOSE 8000. CMD uses uvicorn with 0.0.0.0 host.",
      rubric: "All 4 files defined. Dockerfile has FROM/WORKDIR/COPY/RUN/EXPOSE/CMD. .env has vars."
    }
  ]
},



// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// SQL & DATABASES — ALL MISSING
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Filtering & Sorting": {
  aiRubric: "Check WHERE conditions, ORDER BY, LIMIT, DISTINCT.",
  lessons: [
    {
      title: "Advanced WHERE Conditions",
      theory: "## WHERE Operators\n```sql\nWHERE age BETWEEN 20 AND 25\nWHERE name LIKE 'A%'\nWHERE course IN ('Python','SQL')\nWHERE score IS NOT NULL\nWHERE score IS NULL\nWHERE NOT score < 60\n```",
      instructions: "## Task: 5 Filter Queries\nTable: `students(id, name, age, course, score)`\n1. Students aged 20-25\n2. Name contains 'ada' (case-insensitive)\n3. Course is Python OR SQL\n4. Score is NOT NULL\n5. Score NOT below 70",
      starterCode: "-- 1. Age 20-25\nSELECT * FROM students WHERE age ___ 20 ___ 25;\n\n-- 2. Name contains 'ada'\nSELECT * FROM students WHERE ___(name) LIKE ___;\n\n-- 3. Python or SQL\nSELECT * FROM students WHERE course ___ ('Python','SQL');\n\n-- 4. Score not null\nSELECT * FROM students WHERE score IS ___ NULL;\n\n-- 5. Score not below 70\nSELECT * FROM students WHERE ___ score < 70;",
      solution: "SELECT * FROM students WHERE age BETWEEN 20 AND 25;\nSELECT * FROM students WHERE LOWER(name) LIKE '%ada%';\nSELECT * FROM students WHERE course IN ('Python','SQL');\nSELECT * FROM students WHERE score IS NOT NULL;\nSELECT * FROM students WHERE NOT score < 70;",
      hint: "BETWEEN x AND y. LOWER() for case-insensitive. IN (list). IS NOT NULL. NOT negates.",
      rubric: "All 5 queries correct. BETWEEN, LIKE, IN, IS NOT NULL, NOT all used."
    },
    {
      title: "ORDER BY & DISTINCT",
      theory: "## Sorting & Deduplication\n```sql\n-- Sort multiple columns\nSELECT * FROM students\nORDER BY course ASC, score DESC;\n\n-- Unique values only\nSELECT DISTINCT course FROM students;\n\n-- Top N per group (subquery)\nSELECT * FROM students\nORDER BY score DESC LIMIT 3;\n```",
      instructions: "## Task: Sorting Queries\n1. All students sorted by course A-Z then score high-low\n2. List of unique courses (no duplicates)\n3. Top 3 students overall\n4. Students sorted by name length (shortest first)",
      starterCode: "-- 1. Multi-sort\nSELECT * FROM students ORDER BY course ___, score ___;\n\n-- 2. Unique courses\nSELECT ___ course FROM students;\n\n-- 3. Top 3\nSELECT * FROM students ORDER BY score DESC ___ 3;\n\n-- 4. By name length\nSELECT *, ___(name) AS name_len FROM students\nORDER BY ___(name);",
      solution: "SELECT * FROM students ORDER BY course ASC,score DESC;\nSELECT DISTINCT course FROM students;\nSELECT * FROM students ORDER BY score DESC LIMIT 3;\nSELECT *,LENGTH(name) AS name_len FROM students ORDER BY LENGTH(name);",
      hint: "DISTINCT removes duplicates. LIMIT 3. LENGTH(name) returns character count.",
      rubric: "Multi-sort correct. DISTINCT used. LIMIT 3. LENGTH() for name length."
    }
  ]
},

"Joins & Relationships": {
  aiRubric: "Check INNER, LEFT, RIGHT joins, ON condition, multi-table queries.",
  lessons: [
    {
      title: "INNER & LEFT JOIN",
      theory: "## JOIN Types\n```sql\n-- INNER: only rows matching in BOTH\nSELECT s.name, e.course\nFROM students s\nINNER JOIN enrollments e ON s.id = e.student_id;\n\n-- LEFT: ALL rows from left + matching right\nSELECT s.name, e.course\nFROM students s\nLEFT JOIN enrollments e ON s.id = e.student_id;\n-- Unenrolled students appear with NULL course\n```",
      instructions: "## Task: Student Enrollment Joins\nTables: `students(id,name,age)`, `enrollments(id,student_id,course,grade)`\n1. All enrolled students with their courses\n2. All students (enrolled or not) — show NULL if unenrolled\n3. Students who got grade 'A'\n4. Count of enrollments per student",
      starterCode: "-- 1. Enrolled students\nSELECT s.name, e.course\nFROM students s\n___ JOIN enrollments e ON s.id = e.student_id;\n\n-- 2. All students (incl. unenrolled)\nSELECT s.name, e.course\nFROM students s\n___ JOIN enrollments e ON s.id = e.student_id;\n\n-- 3. Grade A only\nSELECT s.name, e.course, e.grade\nFROM students s\nINNER JOIN enrollments e ON s.id = e.student_id\nWHERE e.grade = ___;\n\n-- 4. Count per student\nSELECT s.name, COUNT(e.id) AS enrolment_count\nFROM students s\nLEFT JOIN enrollments e ON s.id = e.student_id\n___ BY s.name;",
      solution: "SELECT s.name,e.course FROM students s INNER JOIN enrollments e ON s.id=e.student_id;\nSELECT s.name,e.course FROM students s LEFT JOIN enrollments e ON s.id=e.student_id;\nSELECT s.name,e.course,e.grade FROM students s INNER JOIN enrollments e ON s.id=e.student_id WHERE e.grade='A';\nSELECT s.name,COUNT(e.id) AS enrolment_count FROM students s LEFT JOIN enrollments e ON s.id=e.student_id GROUP BY s.name;",
      hint: "INNER for matches only. LEFT for all left rows. GROUP BY s.name with COUNT.",
      rubric: "INNER JOIN. LEFT JOIN. WHERE grade='A'. GROUP BY with COUNT."
    },
    {
      title: "Multi-Table Joins",
      theory: "## Joining 3+ Tables\n```sql\nSELECT s.name, c.title, e.grade\nFROM students s\nJOIN enrollments e ON s.id = e.student_id\nJOIN courses c ON e.course_id = c.id\nWHERE e.grade = 'A';\n```",
      instructions: "## Task: 3-Table Query\nTables: `students`, `enrollments`, `courses(id,title,instructor)`\n1. Student name, course title, instructor for all enrolments\n2. Filter: only courses taught by 'Ada'\n3. Count students per course title",
      starterCode: "-- 1. Three-way join\nSELECT s.name, c.title, c.instructor\nFROM students s\nJOIN enrollments e ON s.id = e.student_id\nJOIN courses c ON e.course_id = ___;\n\n-- 2. Taught by Ada\nSELECT s.name, c.title\nFROM students s\nJOIN enrollments e ON s.id = e.student_id\nJOIN courses c ON e.course_id = c.id\nWHERE c.instructor = ___;\n\n-- 3. Count per course\nSELECT c.title, COUNT(s.id) AS student_count\nFROM courses c\nLEFT JOIN enrollments e ON c.id = e.course_id\nLEFT JOIN students s ON e.student_id = s.id\nGROUP BY ___;",
      solution: "SELECT s.name,c.title,c.instructor FROM students s JOIN enrollments e ON s.id=e.student_id JOIN courses c ON e.course_id=c.id;\nSELECT s.name,c.title FROM students s JOIN enrollments e ON s.id=e.student_id JOIN courses c ON e.course_id=c.id WHERE c.instructor='Ada';\nSELECT c.title,COUNT(s.id) AS student_count FROM courses c LEFT JOIN enrollments e ON c.id=e.course_id LEFT JOIN students s ON e.student_id=s.id GROUP BY c.title;",
      hint: "Chain JOINs one after another. Each needs its own ON condition.",
      rubric: "3-table join. WHERE on instructor. COUNT with GROUP BY."
    }
  ]
},

"Aggregations & Grouping": {
  aiRubric: "Check GROUP BY, HAVING, COUNT/SUM/AVG/MAX/MIN.",
  lessons: [
    {
      title: "GROUP BY & HAVING",
      theory: "## Aggregations\n```sql\nSELECT course,\n       COUNT(*)    AS total,\n       AVG(score)  AS avg_score,\n       MAX(score)  AS top_score\nFROM students\nGROUP BY course\nHAVING COUNT(*) > 2;  -- filter groups\n```\n**WHERE** filters rows BEFORE grouping.\n**HAVING** filters groups AFTER.",
      instructions: "## Task: Course Statistics\n1. Count, average, max score per course\n2. Only courses with avg score > 75\n3. Courses with more than 2 students\n4. Total score per course (SUM)",
      starterCode: "-- 1. Full stats per course\nSELECT course,\n       ___(*)       AS total_students,\n       ROUND(___(score),1) AS avg_score,\n       ___(score)   AS top_score,\n       ___(score)   AS lowest\nFROM students\nGROUP BY ___;\n\n-- 2. Avg > 75\nSELECT course, AVG(score) AS avg\nFROM students\nGROUP BY course\n___ AVG(score) > 75;\n\n-- 3. More than 2 students\nSELECT course, COUNT(*) AS n\nFROM students GROUP BY course\nHAVING COUNT(*) > ___;\n\n-- 4. Sum per course\nSELECT course, ___(score) AS total_score\nFROM students GROUP BY course;",
      solution: "SELECT course,COUNT(*) AS total_students,ROUND(AVG(score),1) AS avg_score,MAX(score) AS top_score,MIN(score) AS lowest FROM students GROUP BY course;\nSELECT course,AVG(score) AS avg FROM students GROUP BY course HAVING AVG(score)>75;\nSELECT course,COUNT(*) AS n FROM students GROUP BY course HAVING COUNT(*)>2;\nSELECT course,SUM(score) AS total_score FROM students GROUP BY course;",
      hint: "HAVING filters groups. ROUND(AVG(),1) for 1dp. SUM adds all values.",
      rubric: "COUNT/AVG/MAX/MIN all used. GROUP BY. HAVING for filter. SUM correct."
    }
  ]
},

"Subqueries": {
  aiRubric: "Check subquery in WHERE, FROM, SELECT. Correlated subqueries.",
  lessons: [
    {
      title: "Subqueries",
      theory: "## Subqueries\nA query inside another query:\n```sql\n-- In WHERE\nSELECT * FROM students\nWHERE score > (SELECT AVG(score) FROM students);\n\n-- In FROM\nSELECT * FROM\n    (SELECT name, score FROM students WHERE score > 70) AS high_scorers;\n\n-- In SELECT\nSELECT name,\n    (SELECT COUNT(*) FROM enrollments e WHERE e.student_id=s.id) AS courses\nFROM students s;\n```",
      instructions: "## Task: Subquery Queries\n1. Students scoring above average\n2. Students in the top 3 scores (using subquery)\n3. Students with no enrolments (using NOT EXISTS)\n4. Each student's score compared to course average",
      starterCode: "-- 1. Above average\nSELECT name, score FROM students\nWHERE score > (SELECT ___(score) FROM students);\n\n-- 2. Top 3 scores\nSELECT name, score FROM students\nWHERE score >= (\n    SELECT ___ FROM students ORDER BY score DESC LIMIT 1 OFFSET ___\n);\n\n-- 3. No enrolments\nSELECT name FROM students s\nWHERE NOT ___ (\n    SELECT 1 FROM enrollments e WHERE e.student_id = s.___\n);\n\n-- 4. Score vs course average\nSELECT s.name, s.score, s.course,\n    ROUND((SELECT AVG(score) FROM students s2 WHERE s2.course = s.___),1) AS course_avg\nFROM students s;",
      solution: "SELECT name,score FROM students WHERE score>(SELECT AVG(score) FROM students);\nSELECT name,score FROM students WHERE score>=(SELECT score FROM students ORDER BY score DESC LIMIT 1 OFFSET 2);\nSELECT name FROM students s WHERE NOT EXISTS(SELECT 1 FROM enrollments e WHERE e.student_id=s.id);\nSELECT s.name,s.score,s.course,ROUND((SELECT AVG(score) FROM students s2 WHERE s2.course=s.course),1) AS course_avg FROM students s;",
      hint: "Subquery in WHERE returns single value. NOT EXISTS for absence check. Correlated: reference outer table.",
      rubric: "AVG subquery. OFFSET for 3rd. NOT EXISTS correct. Correlated subquery in SELECT."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// SQL — INTERMEDIATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Indexes & Performance": {
  aiRubric: "Check CREATE INDEX, EXPLAIN QUERY PLAN, index types.",
  lessons: [
    {
      title: "Creating & Using Indexes",
      theory: "## Indexes\nSpeeds up SELECT queries dramatically:\n```sql\n-- Create index\nCREATE INDEX idx_student_score ON students(score);\nCREATE INDEX idx_student_course ON students(course);\n\n-- Unique index\nCREATE UNIQUE INDEX idx_student_email ON students(email);\n\n-- Composite index\nCREATE INDEX idx_course_score ON students(course, score);\n\n-- Remove\nDROP INDEX idx_student_score;\n\n-- See query plan\nEXPLAIN QUERY PLAN SELECT * FROM students WHERE score > 80;\n```",
      instructions: "## Task: Index Design\n1. Create a basic index on `score`\n2. Create a unique index on `email`\n3. Create a composite index on `(course, score)`\n4. Write a query that would benefit from each index\n5. List all indexes (SQLite: `PRAGMA index_list`)",
      starterCode: "-- 1. Index on score\nCREATE ___ idx_score ON students(___);\n\n-- 2. Unique index on email\nCREATE ___ INDEX idx_email ON students(___);\n\n-- 3. Composite on course+score\nCREATE INDEX idx_course_score ON students(___, ___);\n\n-- 4a. Uses idx_score\nSELECT * FROM students WHERE score > ___;\n\n-- 4b. Uses idx_email\nSELECT * FROM students WHERE email = ___;\n\n-- 4c. Uses idx_course_score\nSELECT * FROM students WHERE course = ___ ORDER BY score DESC;\n\n-- 5. List indexes\nPRAGMA index_list(___);",
      solution: "CREATE INDEX idx_score ON students(score);\nCREATE UNIQUE INDEX idx_email ON students(email);\nCREATE INDEX idx_course_score ON students(course,score);\nSELECT * FROM students WHERE score>80;\nSELECT * FROM students WHERE email='ada@example.com';\nSELECT * FROM students WHERE course='Python' ORDER BY score DESC;\nPRAGMA index_list(students);",
      hint: "INDEX keyword. UNIQUE INDEX for unique constraint. Composite: (course, score) order matters.",
      rubric: "Basic index. UNIQUE index. Composite index. 3 queries. PRAGMA index_list."
    }
  ]
},

"Transactions & ACID": {
  aiRubric: "Check BEGIN, COMMIT, ROLLBACK, ACID properties.",
  lessons: [
    {
      title: "Transactions",
      theory: "## ACID Properties\n- **Atomic** — all or nothing\n- **Consistent** — valid state before and after\n- **Isolated** — transactions don't interfere\n- **Durable** — committed data survives crashes\n\n```sql\nBEGIN;\n    UPDATE accounts SET balance = balance - 500 WHERE id = 1;\n    UPDATE accounts SET balance = balance + 500 WHERE id = 2;\nCOMMIT;\n\n-- If error:\nROLLBACK;\n```",
      instructions: "## Task: Bank Transfer Transaction\nSimulate transferring N1000 from Ada to Tunde:\n1. BEGIN transaction\n2. Check Ada has enough funds\n3. Deduct from Ada\n4. Add to Tunde\n5. COMMIT if successful, ROLLBACK if not",
      starterCode: "import sqlite3\n\nconn = sqlite3.connect(':memory:')\ncursor = conn.cursor()\n\n# Setup\ncursor.executescript('''\n    CREATE TABLE accounts(id INTEGER PRIMARY KEY, name TEXT, balance REAL);\n    INSERT INTO accounts VALUES(1,'Ada',5000);\n    INSERT INTO accounts VALUES(2,'Tunde',1000);\n''')\n\ndef transfer(from_id, to_id, amount):\n    try:\n        cursor.execute('BEGIN')\n\n        # Check balance\n        cursor.execute('SELECT balance FROM accounts WHERE id=?', (from_id,))\n        balance = cursor.fetchone()[0]\n        if balance < ___:\n            raise ValueError('Insufficient funds')\n\n        # Deduct\n        cursor.execute('UPDATE accounts SET balance = balance - ? WHERE id=?', (___, from_id))\n\n        # Add\n        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE id=?', (amount, ___))\n\n        conn.commit()\n        print(f'Transferred N{amount} successfully')\n    except Exception as e:\n        conn.___()  # undo everything\n        print(f'Transfer failed: {e}')\n\ntransfer(1, 2, 1000)  # Ada -> Tunde N1000\ntransfer(1, 2, 9000)  # Should fail (insufficient)\n\ncursor.execute('SELECT * FROM accounts')\nfor row in cursor.fetchall():\n    print(row)",
      solution: "import sqlite3\nconn=sqlite3.connect(':memory:')\ncursor=conn.cursor()\ncursor.executescript('CREATE TABLE accounts(id INTEGER PRIMARY KEY,name TEXT,balance REAL);INSERT INTO accounts VALUES(1,\"Ada\",5000);INSERT INTO accounts VALUES(2,\"Tunde\",1000);')\ndef transfer(from_id,to_id,amount):\n    try:\n        cursor.execute('BEGIN')\n        cursor.execute('SELECT balance FROM accounts WHERE id=?',(from_id,))\n        balance=cursor.fetchone()[0]\n        if balance<amount:raise ValueError('Insufficient funds')\n        cursor.execute('UPDATE accounts SET balance=balance-? WHERE id=?',(amount,from_id))\n        cursor.execute('UPDATE accounts SET balance=balance+? WHERE id=?',(amount,to_id))\n        conn.commit()\n        print(f'Transferred N{amount}')\n    except Exception as e:\n        conn.rollback()\n        print(f'Failed:{e}')\ntransfer(1,2,1000)\ntransfer(1,2,9000)\ncursor.execute('SELECT * FROM accounts')\nfor row in cursor.fetchall():print(row)",
      hint: "conn.rollback() on exception. Check balance < amount. Both UPDATE needed.",
      rubric: "BEGIN. Balance check. Both UPDATEs. COMMIT on success. ROLLBACK on failure."
    }
  ]
},

"Views & CTEs": {
  aiRubric: "Check CREATE VIEW, WITH (CTE), recursive CTEs.",
  lessons: [
    {
      title: "Views & CTEs",
      theory: "## Views\n```sql\n-- Create reusable view\nCREATE VIEW high_scorers AS\nSELECT name, score, course\nFROM students WHERE score >= 80;\n\n-- Use like a table\nSELECT * FROM high_scorers;\n```\n\n## CTEs (Common Table Expressions)\n```sql\nWITH top_students AS (\n    SELECT name, score FROM students ORDER BY score DESC LIMIT 5\n)\nSELECT * FROM top_students WHERE score > 85;\n```",
      instructions: "## Task: Views & CTEs\n1. Create view `passing_students` (score >= 60)\n2. Create view `course_stats` (avg, count per course)\n3. Write a CTE that ranks students\n4. Write a CTE that finds above-average students per course",
      starterCode: "-- 1. View: passing students\nCREATE ___ passing_students AS\nSELECT name, score, course\nFROM students WHERE score >= ___;\n\n-- 2. View: course stats\nCREATE VIEW course_stats AS\nSELECT course, ROUND(AVG(score),1) AS avg, COUNT(*) AS total\nFROM students\n___ BY course;\n\n-- 3. CTE: ranked students\n___ ranked AS (\n    SELECT name, score,\n           ROW_NUMBER() OVER (ORDER BY score DESC) AS rank\n    FROM students\n)\nSELECT * FROM ranked WHERE rank <= 5;\n\n-- 4. CTE: above average per course\nWITH course_avgs AS (\n    SELECT course, AVG(score) AS avg_score\n    FROM students GROUP BY course\n)\nSELECT s.name, s.score, s.course\nFROM students s\nJOIN course_avgs ca ON s.course = ca.___\nWHERE s.score > ca.___;",
      solution: "CREATE VIEW passing_students AS SELECT name,score,course FROM students WHERE score>=60;\nCREATE VIEW course_stats AS SELECT course,ROUND(AVG(score),1) AS avg,COUNT(*) AS total FROM students GROUP BY course;\nWITH ranked AS(SELECT name,score,ROW_NUMBER() OVER(ORDER BY score DESC) AS rank FROM students) SELECT * FROM ranked WHERE rank<=5;\nWITH course_avgs AS(SELECT course,AVG(score) AS avg_score FROM students GROUP BY course) SELECT s.name,s.score,s.course FROM students s JOIN course_avgs ca ON s.course=ca.course WHERE s.score>ca.avg_score;",
      hint: "CREATE VIEW name AS SELECT... CTE: WITH name AS (query) SELECT...",
      rubric: "CREATE VIEW x2. CTE with ROW_NUMBER. CTE with JOIN and WHERE."
    }
  ]
},

"PostgreSQL Deep Dive": {
  aiRubric: "Check PostgreSQL-specific syntax, JSON columns, arrays, window functions.",
  lessons: [
    {
      title: "PostgreSQL Features",
      theory: "## PostgreSQL Extras\n```sql\n-- JSON column\nCREATE TABLE students (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(100),\n    metadata JSONB\n);\n\n-- Query JSON\nSELECT metadata->>'city' FROM students;\n\n-- Array column\nCREATE TABLE courses (\n    id SERIAL PRIMARY KEY,\n    tags TEXT[]\n);\n\n-- Window functions\nSELECT name, score,\n    RANK() OVER (PARTITION BY course ORDER BY score DESC)\nFROM students;\n```",
      instructions: "## Task: PostgreSQL Queries\nWrite PostgreSQL-style SQL for:\n1. Create table with SERIAL, VARCHAR, JSONB\n2. Insert a student with JSONB metadata\n3. Query students by JSON field\n4. Use RANK() window function per course\n5. Array containment check",
      starterCode: "-- 1. Create with JSONB\nCREATE TABLE students (\n    id       ___ PRIMARY KEY,\n    name     ___(100),\n    score    INTEGER,\n    course   VARCHAR(50),\n    metadata ___\n);\n\n-- 2. Insert with JSONB\nINSERT INTO students(name, score, course, metadata)\nVALUES('Ada', 88, 'Python', ___'{\"city\":\"Lagos\",\"age\":22}');\n\n-- 3. Query by JSON field\nSELECT name, metadata___'city' AS city\nFROM students\nWHERE metadata___'city' = '\"Lagos\"';\n\n-- 4. Rank per course\nSELECT name, score, course,\n    ___()\n    OVER (___ BY course ORDER BY score DESC) AS rank\nFROM students;\n\n-- 5. Array contains\nSELECT * FROM courses WHERE ___ @> ARRAY['Python'];",
      solution: "CREATE TABLE students(id SERIAL PRIMARY KEY,name VARCHAR(100),score INTEGER,course VARCHAR(50),metadata JSONB);\nINSERT INTO students(name,score,course,metadata) VALUES('Ada',88,'Python','{\"city\":\"Lagos\",\"age\":22}');\nSELECT name,metadata->>'city' AS city FROM students WHERE metadata->>'city'='Lagos';\nSELECT name,score,course,RANK() OVER(PARTITION BY course ORDER BY score DESC) AS rank FROM students;\nSELECT * FROM courses WHERE tags @> ARRAY['Python'];",
      hint: "SERIAL for auto-increment. JSONB for JSON. ->> extracts text. RANK() OVER (PARTITION BY...).",
      rubric: "SERIAL. JSONB. ->> operator. RANK() with PARTITION BY. ARRAY containment @>."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// SQL — ADVANCED
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Query Optimization": {
  aiRubric: "Check EXPLAIN, index usage, query rewriting, avoiding N+1.",
  lessons: [
    {
      title: "Reading Query Plans",
      theory: "## EXPLAIN\n```sql\nEXPLAIN SELECT * FROM students WHERE score > 80;\n-- Shows: Seq Scan (slow) or Index Scan (fast)\n\nEXPLAIN ANALYZE SELECT ...; -- actually runs it\n```\n\n**Slow queries:**\n- Full table scan (no index)\n- SELECT * (fetches unused columns)\n- N+1 queries (query inside a loop)\n\n**Fast queries:**\n- Index on WHERE/JOIN/ORDER BY columns\n- SELECT only needed columns\n- JOINs instead of subqueries in loops",
      instructions: "## Task: Optimize These Queries\nRewrite each slow query to be faster:\n1. `SELECT * FROM students` → only fetch name and score\n2. Add WHERE to avoid scanning all rows\n3. Replace correlated subquery with a JOIN\n4. Add appropriate index recommendations",
      starterCode: "-- SLOW: fetches everything\nSELECT ___ FROM students;\n\n-- BETTER: only needed columns\nSELECT ___, ___ FROM students;\n\n-- SLOW: no filter\nSELECT name, score FROM students ORDER BY score DESC;\n\n-- BETTER: with index-friendly filter\nSELECT name, score FROM students\nWHERE score ___ 0  -- uses index on score\nORDER BY score DESC LIMIT 10;\n\n-- SLOW: correlated subquery (runs once per row)\nSELECT name,\n    (SELECT COUNT(*) FROM enrollments e WHERE e.student_id = s.id) AS cnt\nFROM students s;\n\n-- BETTER: single JOIN aggregation\nSELECT s.name, COUNT(e.id) AS cnt\nFROM students s\n___ JOIN enrollments e ON s.id = e.student_id\nGROUP BY s.___;\n\n-- Index recommendations\nCREATE INDEX IF NOT EXISTS idx_score ON students(___);\nCREATE INDEX IF NOT EXISTS idx_enrol_sid ON enrollments(___);",
      solution: "SELECT * FROM students;\nSELECT name,score FROM students;\nSELECT name,score FROM students ORDER BY score DESC;\nSELECT name,score FROM students WHERE score>0 ORDER BY score DESC LIMIT 10;\nSELECT name,(SELECT COUNT(*) FROM enrollments e WHERE e.student_id=s.id) AS cnt FROM students s;\nSELECT s.name,COUNT(e.id) AS cnt FROM students s LEFT JOIN enrollments e ON s.id=e.student_id GROUP BY s.name;\nCREATE INDEX IF NOT EXISTS idx_score ON students(score);\nCREATE INDEX IF NOT EXISTS idx_enrol_sid ON enrollments(student_id);",
      hint: "SELECT only needed columns. LEFT JOIN + GROUP BY replaces correlated subquery. Index WHERE columns.",
      rubric: "Column selection. LIMIT added. Correlated replaced with JOIN. Indexes recommended."
    }
  ]
},

"NoSQL with MongoDB": {
  aiRubric: "Check pymongo CRUD, find filters, update operators, aggregation pipeline.",
  lessons: [
    {
      title: "MongoDB with PyMongo",
      theory: "## MongoDB Basics\n```python\nfrom pymongo import MongoClient\n\nclient = MongoClient('mongodb://localhost:27017')\ndb = client['school']\nstudents = db['students']\n\n# Insert\nstudents.insert_one({'name':'Ada','score':88})\n\n# Find\nfor s in students.find({'score':{'$gt':80}}):\n    print(s)\n\n# Update\nstudents.update_one({'name':'Ada'},{'$set':{'score':95}})\n\n# Delete\nstudents.delete_one({'name':'Ada'})\n```\nInstall: `pip install pymongo`",
      instructions: "## Task: MongoDB Student DB\nSimulate MongoDB operations (we'll use a dict-based mock):\n1. Insert 3 student documents\n2. Find students with score > 80\n3. Update a student's score\n4. Delete students with score < 60\n5. Show all remaining",
      starterCode: "# Simulated MongoDB-style operations using Python dicts\nfrom copy import deepcopy\n\nclass MockCollection:\n    def __init__(self):\n        self._docs = []\n        self._id = 1\n\n    def insert_one(self, doc):\n        d = deepcopy(doc)\n        d['_id'] = self._id\n        self._id += 1\n        self._docs.append(d)\n        return d['_id']\n\n    def find(self, query={}):\n        results = []\n        for doc in self._docs:\n            match = all(\n                (doc.get(k) > v['$gt'] if '$gt' in v else doc.get(k) == v)\n                for k, v in query.items()\n            )\n            if match or not query:\n                results.append(deepcopy(doc))\n        return results\n\n    def update_one(self, query, update):\n        for doc in self._docs:\n            if all(doc.get(k) == v for k,v in query.items()):\n                for k,v in update.get('$set', {}).items():\n                    doc[k] = v\n                break\n\n    def delete_many(self, query):\n        self._docs = [d for d in self._docs\n                      if not all(d.get(k) < v['$lt'] for k,v in query.items()\n                                 if '$lt' in v)]\n\nstudents = MockCollection()\n\n# 1. Insert\nstudents.insert_one({'name':'Ada',   'course':'Python', 'score': 88})\nstudents.insert_one({'name':'Tunde', 'course':'SQL',    'score': ___ })\nstudents.insert_one({'name':'Ngozi', 'course':'Python', 'score': 95})\n\n# 2. Find score > 80\nprint('Score > 80:')\nfor s in students.find({'score': {'$gt': ___}}):\n    print(f\"  {s['name']}: {s['score']}\")\n\n# 3. Update Ada\nstudents.update_one({'name': ___}, {'$set': {'score': 92}})\n\n# 4. Delete low scorers\nstudents.delete_many({'score': {'$lt': 60}})\n\n# 5. All remaining\nprint('Remaining:')\nfor s in students.find():\n    print(f\"  {s}\")",
      solution: "from copy import deepcopy\nclass MockCollection:\n    def __init__(self):\n        self._docs=[];self._id=1\n    def insert_one(self,doc):\n        d=deepcopy(doc);d['_id']=self._id;self._id+=1;self._docs.append(d);return d['_id']\n    def find(self,query={}):\n        results=[]\n        for doc in self._docs:\n            match=all((doc.get(k)>v['$gt'] if '$gt' in v else doc.get(k)==v) for k,v in query.items())\n            if match or not query:results.append(deepcopy(doc))\n        return results\n    def update_one(self,query,update):\n        for doc in self._docs:\n            if all(doc.get(k)==v for k,v in query.items()):\n                for k,v in update.get('$set',{}).items():doc[k]=v\n                break\n    def delete_many(self,query):\n        self._docs=[d for d in self._docs if not all(d.get(k)<v['$lt'] for k,v in query.items() if '$lt' in v)]\nstudents=MockCollection()\nstudents.insert_one({'name':'Ada','course':'Python','score':88})\nstudents.insert_one({'name':'Tunde','course':'SQL','score':45})\nstudents.insert_one({'name':'Ngozi','course':'Python','score':95})\nprint('Score>80:')\nfor s in students.find({'score':{'$gt':80}}):print(f\"  {s['name']}:{s['score']}\")\nstudents.update_one({'name':'Ada'},{'$set':{'score':92}})\nstudents.delete_many({'score':{'$lt':60}})\nprint('Remaining:')\nfor s in students.find():print(f'  {s}')",
      hint: "$gt for greater than. $lt for less than. $set updates a field. update_one finds first match.",
      rubric: "insert_one used. find with $gt. update_one with $set. delete_many with $lt. All remaining shown."
    }
  ]
},

"ORMs with SQLAlchemy": {
  aiRubric: "Check SQLAlchemy model, session, query, relationships.",
  lessons: [
    {
      title: "SQLAlchemy Core & ORM",
      theory: "## SQLAlchemy\n```python\nfrom sqlalchemy import create_engine, Column, Integer, String\nfrom sqlalchemy.orm import declarative_base, Session\n\nBase = declarative_base()\nengine = create_engine('sqlite:///school.db')\n\nclass Student(Base):\n    __tablename__ = 'students'\n    id     = Column(Integer, primary_key=True)\n    name   = Column(String(100), nullable=False)\n    score  = Column(Integer, default=0)\n\nBase.metadata.create_all(engine)\n\nwith Session(engine) as session:\n    ada = Student(name='Ada', score=88)\n    session.add(ada)\n    session.commit()\n\n    students = session.query(Student).filter(Student.score > 80).all()\n```",
      instructions: "## Task: SQLAlchemy Student CRUD\n1. Define `Student` model (id, name, course, score)\n2. Create tables\n3. Insert 3 students\n4. Query: filter score >= 80, order by score desc\n5. Update Ada's score\n6. Delete students with score < 60",
      starterCode: "from sqlalchemy import create_engine, Column, Integer, String\nfrom sqlalchemy.orm import declarative_base, Session\n\nBase = declarative_base()\nengine = create_engine('sqlite:///:memory:')\n\nclass Student(Base):\n    __tablename__ = ___\n    id     = Column(Integer, primary_key=True)\n    name   = Column(String(100), nullable=False)\n    course = Column(String(50))\n    score  = Column(Integer, default=___)\n\n    def __repr__(self):\n        return f'<Student {self.name} {self.score}>'\n\nBase.metadata.create_all(___)\n\nwith Session(engine) as session:\n    session.add_all([\n        Student(name='Ada',   course='Python', score=88),\n        Student(name='Tunde', course='SQL',    score=55),\n        Student(name='Ngozi', course='Python', score=95)\n    ])\n    session.commit()\n\n    # Query high scorers\n    high = session.query(Student)\\\n        .filter(Student.score >= ___)\\\n        .order_by(Student.score.___())\\\n        .all()\n    print('High scorers:', high)\n\n    # Update Ada\n    ada = session.query(Student).filter(Student.name == ___).first()\n    ada.score = 92\n    session.commit()\n\n    # Delete low scorers\n    session.query(Student).filter(Student.score < ___).delete()\n    session.commit()\n\n    print('All remaining:', session.query(Student).all())",
      solution: "from sqlalchemy import create_engine,Column,Integer,String\nfrom sqlalchemy.orm import declarative_base,Session\nBase=declarative_base()\nengine=create_engine('sqlite:///:memory:')\nclass Student(Base):\n    __tablename__='students'\n    id=Column(Integer,primary_key=True)\n    name=Column(String(100),nullable=False)\n    course=Column(String(50))\n    score=Column(Integer,default=0)\n    def __repr__(self):return f'<Student {self.name} {self.score}>'\nBase.metadata.create_all(engine)\nwith Session(engine) as session:\n    session.add_all([Student(name='Ada',course='Python',score=88),Student(name='Tunde',course='SQL',score=55),Student(name='Ngozi',course='Python',score=95)])\n    session.commit()\n    high=session.query(Student).filter(Student.score>=80).order_by(Student.score.desc()).all()\n    print('High:',high)\n    ada=session.query(Student).filter(Student.name=='Ada').first()\n    ada.score=92\n    session.commit()\n    session.query(Student).filter(Student.score<60).delete()\n    session.commit()\n    print('All:',session.query(Student).all())",
      hint: "declarative_base(). Column types. Session.add_all(). .filter().order_by().all().",
      rubric: "Model defined. create_all. add_all. filter and order_by. Update via attribute. delete()."
    }
  ]
},



// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// DATA SCIENCE — ALL MISSING
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Intro to Data Science": {
  aiRubric: "Check data science concepts, Python basics for data, numpy/pandas intro.",
  lessons: [
    {
      title: "What is Data Science?",
      theory: "## Data Science Pipeline\n1. **Collect** — gather raw data\n2. **Clean** — handle missing values, outliers\n3. **Explore** — understand patterns (EDA)\n4. **Model** — build predictive models\n5. **Communicate** — visualize and report\n\n**Key Python Libraries:**\n- `numpy` — numerical computing\n- `pandas` — data manipulation\n- `matplotlib` — visualization\n- `scikit-learn` — machine learning",
      instructions: "## Task: Data Science Starter\n1. Create a list of student scores\n2. Calculate mean, median, mode manually\n3. Find min, max, range\n4. Count how many are above average\n5. Print a simple text histogram",
      starterCode: "scores = [78, 92, 65, 88, 74, 91, 55, 83, 79, 88, 67, 95]\n\n# 1. Mean\nmean = sum(scores) / len(___)\nprint(f'Mean:   {mean:.1f}')\n\n# 2. Median\nsorted_scores = sorted(___)\nn = len(sorted_scores)\nif n % 2 == 0:\n    median = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2\nelse:\n    median = sorted_scores[n//2]\nprint(f'Median: {median}')\n\n# 3. Mode\nfrom collections import Counter\ncounts = Counter(___)\nmode = counts.most_common(1)[0][0]\nprint(f'Mode:   {mode}')\n\n# 4. Range\nprint(f'Min: {min(scores)}, Max: {max(scores)}, Range: {___ - ___}')\n\n# 5. Above average\nabove = [s for s in scores if s > ___]\nprint(f'Above average ({mean:.1f}): {len(above)} students')\n\n# 6. Text histogram\nprint('\\nDistribution:')\nfor bucket, label in [(90,100,'90-100'), (80,90,'80-89'), (70,80,'70-79'), (60,70,'60-69'), (0,60,'<60')]:\n    count = len([s for s in scores if bucket <= s < 100 if bucket==90 else bucket <= s < (bucket+10)])\n    print(f'  {label}: {\"#\" * count}')",
      solution: "scores=[78,92,65,88,74,91,55,83,79,88,67,95]\nmean=sum(scores)/len(scores)\nprint(f'Mean:{mean:.1f}')\nsorted_scores=sorted(scores)\nn=len(sorted_scores)\nmedian=(sorted_scores[n//2-1]+sorted_scores[n//2])/2 if n%2==0 else sorted_scores[n//2]\nprint(f'Median:{median}')\nfrom collections import Counter\ncounts=Counter(scores)\nmode=counts.most_common(1)[0][0]\nprint(f'Mode:{mode}')\nprint(f'Min:{min(scores)}, Max:{max(scores)}, Range:{max(scores)-min(scores)}')\nabove=[s for s in scores if s>mean]\nprint(f'Above avg:{len(above)}')\nprint('\\nDistribution:')\nfor lo,hi,label in [(90,101,'90-100'),(80,90,'80-89'),(70,80,'70-79'),(60,70,'60-69'),(0,60,'<60')]:\n    count=len([s for s in scores if lo<=s<hi])\n    print(f'  {label}:{\"#\"*count}')",
      hint: "sum/len for mean. sorted then middle for median. Counter.most_common(1) for mode.",
      rubric: "Mean correct. Median correct. Mode using Counter. Range shown. Above-avg counted."
    },
    {
      title: "NumPy for Data Science",
      theory: "## NumPy Power\n```python\nimport numpy as np\n\narr = np.array([1,2,3,4,5])\nprint(arr.mean(), arr.std(), arr.var())\n\n# 2D arrays (matrix)\nmatrix = np.array([[1,2,3],[4,5,6]])\nprint(matrix.shape)   # (2,3)\nprint(matrix.sum(axis=0))  # column sums\nprint(matrix.sum(axis=1))  # row sums\n\n# Broadcasting\nscores = np.array([78,92,65,88])\nnormalized = (scores - scores.mean()) / scores.std()\n```",
      instructions: "## Task: NumPy Analysis\n`exam_scores = [[78,92,65],[88,74,91],[55,83,79],[88,67,95]]` (4 students, 3 exams)\n1. Convert to 2D NumPy array\n2. Mean score per student (axis=1)\n3. Mean score per exam (axis=0)\n4. Normalize all scores (z-score)\n5. Find which student has the highest total",
      starterCode: "import numpy as np\n\nraw = [[78,92,65],[88,74,91],[55,83,79],[88,67,95]]\nscores = np.array(___)\nprint('Shape:', scores.___)\n\n# Mean per student\nstudent_means = scores.mean(axis=___)\nprint('Student means:', student_means.round(1))\n\n# Mean per exam\nexam_means = scores.mean(axis=___)\nprint('Exam means:', exam_means.round(1))\n\n# Normalize (z-score)\nnormalized = (scores - scores.mean()) / scores.___\nprint('Normalized:\\n', normalized.round(2))\n\n# Best student (highest total)\ntotals = scores.sum(axis=___)\nbest_idx = totals.___\nprint(f'Best student: #{best_idx+1} with total {totals[best_idx]}')",
      solution: "import numpy as np\nraw=[[78,92,65],[88,74,91],[55,83,79],[88,67,95]]\nscores=np.array(raw)\nprint('Shape:',scores.shape)\nstudent_means=scores.mean(axis=1)\nprint('Student means:',student_means.round(1))\nexam_means=scores.mean(axis=0)\nprint('Exam means:',exam_means.round(1))\nnormalized=(scores-scores.mean())/scores.std()\nprint('Normalized:\\n',normalized.round(2))\ntotals=scores.sum(axis=1)\nbest_idx=totals.argmax()\nprint(f'Best:#{best_idx+1} total {totals[best_idx]}')",
      hint: "axis=1 for row-wise, axis=0 for column-wise. std() for standard deviation. argmax() for index of max.",
      rubric: "2D array. axis=1 student means. axis=0 exam means. std normalization. argmax for best."
    }
  ]
},

"Data Cleaning": {
  aiRubric: "Check isnull, fillna, dropna, drop_duplicates, astype, str methods.",
  lessons: [
    {
      title: "Handling Missing Data",
      theory: "## Missing Data Strategies\n```python\nimport pandas as pd\nimport numpy as np\n\ndf = pd.DataFrame({'score':[88, None, 95, None, 72]})\n\ndf.isnull().sum()          # count missing\ndf['score'].fillna(df['score'].mean())  # fill with mean\ndf['score'].fillna(method='ffill')      # forward fill\ndf.dropna()                # drop any NaN row\ndf.dropna(subset=['score'])  # only check score\ndf.dropna(thresh=2)        # keep rows with 2+ non-null\n```",
      instructions: "## Task: Clean Student Dataset\nGiven a messy DataFrame with NaN values:\n1. Report null counts per column\n2. Fill missing `score` with the median\n3. Fill missing `course` with 'Unknown'\n4. Drop rows where `name` is null\n5. Report how many rows were dropped",
      starterCode: "import pandas as pd\nimport numpy as np\n\ndata = {\n    'name':   ['Ada', None, 'Ngozi', 'Emeka', 'Amaka'],\n    'course': ['Python', 'SQL', None, 'FastAPI', None],\n    'score':  [88, 72, None, 91, 65]\n}\ndf = pd.DataFrame(data)\noriginal_count = len(df)\nprint('Original:\\n', df)\nprint('\\nNull counts:\\n', df.___(). ___())\n\ndf['score'] = df['score'].fillna(df['score'].___())\ndf['course'] = df['course'].fillna(___)\ndf = df.dropna(subset=[___])\n\nprint(f'\\nDropped {original_count - len(df)} rows')\nprint('\\nCleaned:\\n', df)",
      solution: "import pandas as pd,numpy as np\ndata={'name':['Ada',None,'Ngozi','Emeka','Amaka'],'course':['Python','SQL',None,'FastAPI',None],'score':[88,72,None,91,65]}\ndf=pd.DataFrame(data)\noriginal_count=len(df)\nprint('Original:\\n',df)\nprint('\\nNulls:\\n',df.isnull().sum())\ndf['score']=df['score'].fillna(df['score'].median())\ndf['course']=df['course'].fillna('Unknown')\ndf=df.dropna(subset=['name'])\nprint(f'\\nDropped {original_count-len(df)} rows')\nprint('\\nCleaned:\\n',df)",
      hint: "isnull().sum() counts. fillna(median()) for score. dropna(subset=['name']) for name.",
      rubric: "isnull().sum(). fillna median. fillna Unknown. dropna subset. Drop count reported."
    },
    {
      title: "Data Type Conversion & String Cleaning",
      theory: "## Type Conversion\n```python\ndf['age']   = df['age'].astype(int)\ndf['price'] = df['price'].astype(float)\ndf['active']= df['active'].astype(bool)\n\n# String methods\ndf['name'] = df['name'].str.strip()\ndf['name'] = df['name'].str.title()\ndf['name'] = df['name'].str.replace('-', ' ')\ndf['email']= df['email'].str.lower()\ndf['valid_email'] = df['email'].str.contains('@')\n```",
      instructions: "## Task: Fix Messy Data\n1. Strip whitespace from names\n2. Convert names to Title Case\n3. Convert score strings to integers\n4. Lowercase all emails\n5. Add `valid_email` column (True if contains @)",
      starterCode: "import pandas as pd\n\ndata = {\n    'name':  ['  ada okonkwo ', 'TUNDE BELLO', ' ngozi eze'],\n    'score': ['88', '72', '95'],\n    'email': ['Ada@Example.COM', 'tunde@gmail.com', 'NGOZI@yahoo.COM']\n}\ndf = pd.DataFrame(data)\nprint('Before:\\n', df)\n\ndf['name']  = df['name'].str.___()\ndf['name']  = df['name'].str.___()\ndf['score'] = df['score'].astype(___)\ndf['email'] = df['email'].str.___()\ndf['valid_email'] = df['email'].str.___(___)\n\nprint('\\nAfter:\\n', df)",
      solution: "import pandas as pd\ndata={'name':['  ada okonkwo ','TUNDE BELLO',' ngozi eze'],'score':['88','72','95'],'email':['Ada@Example.COM','tunde@gmail.com','NGOZI@yahoo.COM']}\ndf=pd.DataFrame(data)\nprint('Before:\\n',df)\ndf['name']=df['name'].str.strip()\ndf['name']=df['name'].str.title()\ndf['score']=df['score'].astype(int)\ndf['email']=df['email'].str.lower()\ndf['valid_email']=df['email'].str.contains('@')\nprint('\\nAfter:\\n',df)",
      hint: "str.strip() removes spaces. str.title() capitalizes. astype(int). str.lower(). str.contains('@').",
      rubric: "strip. title. astype(int). lower. contains('@') for valid_email."
    }
  ]
},

"Exploratory Data Analysis": {
  aiRubric: "Check describe(), value_counts(), groupby(), correlation.",
  lessons: [
    {
      title: "EDA with Pandas",
      theory: "## Key EDA Functions\n```python\ndf.shape           # (rows, cols)\ndf.dtypes          # column types\ndf.describe()      # stats summary\ndf['col'].value_counts()  # frequency\ndf.groupby('course')['score'].mean()\ndf.corr()          # correlation matrix\ndf.nunique()       # unique values per column\n```",
      instructions: "## Task: Full EDA\nAnalyse a student dataset with name, age, course, score, city:\n1. Shape and dtypes\n2. describe() for score\n3. Most popular course (value_counts)\n4. Average score per course\n5. Correlation between age and score",
      starterCode: "import pandas as pd\nimport numpy as np\n\nnp.random.seed(42)\nn = 50\ndf = pd.DataFrame({\n    'name':   [f'Student_{i}' for i in range(n)],\n    'age':    np.random.randint(18, 30, n),\n    'course': np.random.choice(['Python','SQL','FastAPI','React'], n),\n    'score':  np.random.randint(50, 100, n),\n    'city':   np.random.choice(['Lagos','Abuja','Port Harcourt'], n)\n})\n\nprint('Shape:', df.___)\nprint('\\nDtypes:\\n', df.___)\nprint('\\nScore stats:\\n', df['score'].___())\nprint('\\nCourse popularity:\\n', df['course'].___())\nprint('\\nAvg score per course:\\n', df.groupby(___)[___].mean().round(1))\nprint('\\nAge-Score correlation:', df[['age','score']].corr().loc['age','score'].round(3))",
      solution: "import pandas as pd,numpy as np\nnp.random.seed(42)\nn=50\ndf=pd.DataFrame({'name':[f'Student_{i}' for i in range(n)],'age':np.random.randint(18,30,n),'course':np.random.choice(['Python','SQL','FastAPI','React'],n),'score':np.random.randint(50,100,n),'city':np.random.choice(['Lagos','Abuja','Port Harcourt'],n)})\nprint('Shape:',df.shape)\nprint('\\nDtypes:\\n',df.dtypes)\nprint('\\nScore stats:\\n',df['score'].describe())\nprint('\\nCourse popularity:\\n',df['course'].value_counts())\nprint('\\nAvg per course:\\n',df.groupby('course')['score'].mean().round(1))\nprint('\\nCorrelation:',df[['age','score']].corr().loc['age','score'].round(3))",
      hint: "df.shape. df.dtypes. describe(). value_counts(). groupby('course')['score'].mean(). corr().",
      rubric: "shape, dtypes, describe, value_counts, groupby mean, corr all used."
    }
  ]
},

"Data Visualization": {
  aiRubric: "Check matplotlib basics, plot types, labels, titles.",
  lessons: [
    {
      title: "Matplotlib Basics",
      theory: "## Matplotlib\n```python\nimport matplotlib.pyplot as plt\n\n# Line plot\nplt.plot([1,2,3,4], [10,20,15,25])\nplt.title('My Chart')\nplt.xlabel('X')\nplt.ylabel('Y')\nplt.show()\n\n# Bar chart\nplt.bar(['Python','SQL','JS'], [40,25,35])\n\n# Histogram\nplt.hist(scores, bins=10)\n\n# Scatter\nplt.scatter(ages, scores)\n```",
      instructions: "## Task: Student Score Charts\n1. Bar chart: average score per course\n2. Histogram: score distribution (bins=10)\n3. Print chart descriptions (we can't render here, print the data instead)\n4. Find which course has the highest average",
      starterCode: "import pandas as pd\nimport numpy as np\n\nnp.random.seed(42)\ndf = pd.DataFrame({\n    'course': np.random.choice(['Python','SQL','FastAPI','React'], 50),\n    'score':  np.random.randint(50, 100, 50),\n    'age':    np.random.randint(18, 30, 50)\n})\n\n# 1. Average per course\ncourse_avg = df.groupby(___)[___].mean().round(1)\nprint('Course Averages:')\nfor course, avg in course_avg.___():\n    bar = '#' * int(avg // 5)\n    print(f'  {course:10} | {bar} {avg}')\n\n# 2. Score distribution\nprint('\\nScore Distribution:')\nbins = [(50,60),(60,70),(70,80),(80,90),(90,100)]\nfor lo, hi in bins:\n    count = len(df[(df['score'] >= lo) & (df['score'] < hi)])\n    print(f'  {lo}-{hi}: {\"#\" * count} ({count})')\n\n# 3. Best course\nbest = course_avg.___\nprint(f'\\nBest course: {best} ({course_avg[best]:.1f})')",
      solution: "import pandas as pd,numpy as np\nnp.random.seed(42)\ndf=pd.DataFrame({'course':np.random.choice(['Python','SQL','FastAPI','React'],50),'score':np.random.randint(50,100,50),'age':np.random.randint(18,30,50)})\ncourse_avg=df.groupby('course')['score'].mean().round(1)\nprint('Course Averages:')\nfor course,avg in course_avg.items():\n    bar='#'*int(avg//5)\n    print(f'  {course:10}|{bar} {avg}')\nprint('\\nScore Distribution:')\nbins=[(50,60),(60,70),(70,80),(80,90),(90,100)]\nfor lo,hi in bins:\n    count=len(df[(df['score']>=lo)&(df['score']<hi)])\n    print(f'  {lo}-{hi}:{\"#\"*count}({count})')\nbest=course_avg.idxmax()\nprint(f'\\nBest:{best}({course_avg[best]:.1f})')",
      hint: "groupby().mean(). items() to iterate. Boolean mask for histogram bins. idxmax() for best.",
      rubric: "groupby mean. items() iteration. bin counting. idxmax for best course."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// DATA SCIENCE — INTERMEDIATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Statistical Analysis": {
  aiRubric: "Check mean, std, t-test, correlation, hypothesis testing.",
  lessons: [
    {
      title: "Descriptive Statistics",
      theory: "## Key Statistics\n```python\nimport numpy as np\nfrom scipy import stats\n\ndata = [78,92,65,88,74,91,55,83]\n\nnp.mean(data)     # average\nnp.std(data)      # spread\nnp.median(data)   # middle value\nnp.percentile(data, 75)  # 75th percentile\n\n# Normality test\nstat, p = stats.shapiro(data)\nprint(f'Normal if p > 0.05: {p:.3f}')\n```",
      instructions: "## Task: Statistics Deep Dive\n1. Calculate mean, median, std, variance\n2. Find 25th, 50th, 75th percentile (IQR)\n3. Identify outliers (> 1.5 * IQR from Q3/Q1)\n4. Perform a t-test: compare two groups",
      starterCode: "import numpy as np\nfrom scipy import stats\n\ngroup_a = [78,92,65,88,74,91,55,83,79,88]\ngroup_b = [85,90,78,92,88,95,82,89,91,87]\n\n# 1. Descriptive stats\nfor name, g in [('Group A', group_a), ('Group B', group_b)]:\n    print(f'{name}:')\n    print(f'  Mean:   {np.___(g):.1f}')\n    print(f'  Median: {np.___(g):.1f}')\n    print(f'  Std:    {np.___(g):.1f}')\n\n# 2. IQR and outliers\narr = np.array(group_a)\nQ1 = np.percentile(arr, ___)\nQ3 = np.percentile(arr, ___)\nIQR = Q3 - Q1\noutliers = arr[(arr < Q1 - 1.5*___) | (arr > Q3 + 1.5*___)]\nprint(f'\\nIQR: {IQR}, Outliers: {outliers}')\n\n# 3. t-test\nt_stat, p_value = stats.ttest_ind(group_a, ___)\nprint(f'\\nt-statistic: {t_stat:.3f}')\nprint(f'p-value:     {p_value:.3f}')\nprint('Significant difference!' if p_value < ___ else 'No significant difference')",
      solution: "import numpy as np\nfrom scipy import stats\ngroup_a=[78,92,65,88,74,91,55,83,79,88]\ngroup_b=[85,90,78,92,88,95,82,89,91,87]\nfor name,g in [('Group A',group_a),('Group B',group_b)]:\n    print(f'{name}:')\n    print(f'  Mean:{np.mean(g):.1f}')\n    print(f'  Median:{np.median(g):.1f}')\n    print(f'  Std:{np.std(g):.1f}')\narr=np.array(group_a)\nQ1=np.percentile(arr,25)\nQ3=np.percentile(arr,75)\nIQR=Q3-Q1\noutliers=arr[(arr<Q1-1.5*IQR)|(arr>Q3+1.5*IQR)]\nprint(f'\\nIQR:{IQR},Outliers:{outliers}')\nt_stat,p_value=stats.ttest_ind(group_a,group_b)\nprint(f'\\nt:{t_stat:.3f}')\nprint(f'p:{p_value:.3f}')\nprint('Significant!' if p_value<0.05 else 'Not significant')",
      hint: "np.mean, np.median, np.std. Percentile 25 and 75. IQR = Q3 - Q1. ttest_ind for two groups. p < 0.05.",
      rubric: "mean/median/std. Q1/Q3/IQR. Outlier detection. ttest_ind. p<0.05 conclusion."
    }
  ]
},

"Scikit-Learn Pipelines": {
  aiRubric: "Check Pipeline, StandardScaler, ColumnTransformer, fit/transform.",
  lessons: [
    {
      title: "Building ML Pipelines",
      theory: "## Sklearn Pipeline\n```python\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\n\npipeline = Pipeline([\n    ('scaler', StandardScaler()),\n    ('model',  LogisticRegression())\n])\n\npipeline.fit(X_train, y_train)\ny_pred = pipeline.predict(X_test)\n```\nPipelines prevent data leakage and simplify code.",
      instructions: "## Task: Full ML Pipeline\n1. Load Iris dataset\n2. Build Pipeline: StandardScaler + LogisticRegression\n3. Fit and evaluate\n4. Add cross-validation\n5. Print accuracy and CV mean",
      starterCode: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split, cross_val_score\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\nimport numpy as np\n\niris = load_iris()\nX, y = iris.___, iris.___\n\nX_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\npipeline = Pipeline([\n    ('scaler', ___()),\n    ('model',  ___(max_iter=200))\n])\n\npipeline.___(X_train, y_train)\ny_pred = pipeline.___(X_test)\n\nprint(f'Accuracy: {accuracy_score(y_test, y_pred):.2%}')\n\ncv_scores = cross_val_score(pipeline, X, y, cv=___)\nprint(f'CV Mean:  {cv_scores.mean():.2%} (+/- {cv_scores.std():.2%})')",
      solution: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split,cross_val_score\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\nimport numpy as np\niris=load_iris()\nX,y=iris.data,iris.target\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\npipeline=Pipeline([('scaler',StandardScaler()),('model',LogisticRegression(max_iter=200))])\npipeline.fit(X_train,y_train)\ny_pred=pipeline.predict(X_test)\nprint(f'Accuracy:{accuracy_score(y_test,y_pred):.2%}')\ncv_scores=cross_val_score(pipeline,X,y,cv=5)\nprint(f'CV Mean:{cv_scores.mean():.2%}(+/-{cv_scores.std():.2%})')",
      hint: "Pipeline([(name, step)]). fit then predict. cross_val_score with cv=5.",
      rubric: "Pipeline with 2 steps. fit/predict. accuracy_score. cross_val_score cv=5."
    }
  ]
},

"Regression Models": {
  aiRubric: "Check LinearRegression, R2, MSE, feature importance.",
  lessons: [
    {
      title: "Linear & Ridge Regression",
      theory: "## Regression\n```python\nfrom sklearn.linear_model import LinearRegression, Ridge\nfrom sklearn.metrics import mean_squared_error, r2_score\n\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\ny_pred = model.predict(X_test)\n\nprint(r2_score(y_test, y_pred))          # 0-1, higher is better\nprint(mean_squared_error(y_test, y_pred)) # lower is better\nprint(model.coef_)   # feature weights\nprint(model.intercept_)\n```",
      instructions: "## Task: Predict Student Score\nBuild a regression model to predict score from age and study_hours:\n1. Create synthetic data\n2. Train/test split\n3. Fit LinearRegression\n4. Evaluate: R2, MSE, RMSE\n5. Print feature coefficients",
      starterCode: "import numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import mean_squared_error, r2_score\n\nnp.random.seed(42)\nn = 100\nage = np.random.randint(18, 30, n)\nstudy_hours = np.random.randint(1, 8, n)\nscore = 40 + 1.5*study_hours + 0.3*age + np.random.randn(n)*8\n\nX = np.column_stack([age, study_hours])\ny = score\n\nX_train,X_test,y_train,y_test = train_test_split(X, y, test_size=___, random_state=42)\n\nmodel = ___().fit(X_train, y_train)\ny_pred = model.___(X_test)\n\nr2  = r2_score(y_test, ___)\nmse = mean_squared_error(y_test, ___)\nrmse = mse ** 0.5\n\nprint(f'R2:   {r2:.3f}')\nprint(f'MSE:  {mse:.2f}')\nprint(f'RMSE: {rmse:.2f}')\nprint(f'Coefficients: age={model.coef_[0]:.2f}, study_hours={model.coef_[1]:.2f}')\nprint(f'Intercept: {model.intercept_:.2f}')",
      solution: "import numpy as np\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import mean_squared_error,r2_score\nnp.random.seed(42)\nn=100\nage=np.random.randint(18,30,n)\nstudy_hours=np.random.randint(1,8,n)\nscore=40+1.5*study_hours+0.3*age+np.random.randn(n)*8\nX=np.column_stack([age,study_hours])\ny=score\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nmodel=LinearRegression().fit(X_train,y_train)\ny_pred=model.predict(X_test)\nr2=r2_score(y_test,y_pred)\nmse=mean_squared_error(y_test,y_pred)\nrmse=mse**0.5\nprint(f'R2:{r2:.3f}')\nprint(f'MSE:{mse:.2f}')\nprint(f'RMSE:{rmse:.2f}')\nprint(f'Coefs: age={model.coef_[0]:.2f}, hours={model.coef_[1]:.2f}')\nprint(f'Intercept:{model.intercept_:.2f}')",
      hint: "np.column_stack for 2D X. LinearRegression().fit(). r2_score, mean_squared_error. coef_ for weights.",
      rubric: "Synthetic data. column_stack. LinearRegression fit/predict. R2/MSE/RMSE. coef_ printed."
    }
  ]
},

"Classification Models": {
  aiRubric: "Check classifier choice, confusion matrix, precision, recall, F1.",
  lessons: [
    {
      title: "Classification Metrics",
      theory: "## Classification Evaluation\n```python\nfrom sklearn.metrics import (\n    confusion_matrix,\n    classification_report,\n    accuracy_score\n)\n\nprint(confusion_matrix(y_test, y_pred))\nprint(classification_report(y_test, y_pred))\n# Shows: precision, recall, f1-score per class\n```\n- **Precision** — of predicted positives, how many are correct\n- **Recall** — of actual positives, how many did we catch\n- **F1** — harmonic mean of precision and recall",
      instructions: "## Task: Classify Pass/Fail\n1. Create data: scores + binary pass/fail label\n2. Try 3 classifiers: LogisticRegression, RandomForest, KNN\n3. Print accuracy for each\n4. Full classification report for best model",
      starterCode: "import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.metrics import accuracy_score, classification_report\n\nnp.random.seed(42)\nn = 200\nscores  = np.random.randint(40, 100, n)\nstudied = np.random.randint(1, 10, n)\npassed  = ((scores + studied*3) > 90).astype(int)\n\nX = np.column_stack([scores, studied])\ny = passed\n\nX_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nclassifiers = [\n    ('Logistic Regression', ___()),\n    ('Random Forest', ___(n_estimators=100, random_state=42)),\n    ('KNN', ___(n_neighbors=5))\n]\n\nbest_model, best_acc = None, 0\nfor name, clf in classifiers:\n    clf.fit(X_train, y_train)\n    acc = accuracy_score(y_test, clf.predict(X_test))\n    print(f'{name:25} Accuracy: {acc:.2%}')\n    if acc > best_acc:\n        best_acc, best_model = acc, clf\n\nprint(f'\\nBest model report:')\nprint(classification_report(y_test, best_model.predict(___)))",
      solution: "import numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.metrics import accuracy_score,classification_report\nnp.random.seed(42)\nn=200\nscores=np.random.randint(40,100,n)\nstudied=np.random.randint(1,10,n)\npassed=((scores+studied*3)>90).astype(int)\nX=np.column_stack([scores,studied])\ny=passed\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nclassifiers=[('Logistic Regression',LogisticRegression()),('Random Forest',RandomForestClassifier(n_estimators=100,random_state=42)),('KNN',KNeighborsClassifier(n_neighbors=5))]\nbest_model,best_acc=None,0\nfor name,clf in classifiers:\n    clf.fit(X_train,y_train)\n    acc=accuracy_score(y_test,clf.predict(X_test))\n    print(f'{name:25} Accuracy:{acc:.2%}')\n    if acc>best_acc:\n        best_acc,best_model=acc,clf\nprint('\\nBest model:')\nprint(classification_report(y_test,best_model.predict(X_test)))",
      hint: "3 classifiers in a loop. fit/predict/accuracy_score each. classification_report on best.",
      rubric: "3 classifiers. Loop with accuracy. Best model tracked. classification_report shown."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// DATA SCIENCE — ADVANCED
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Feature Engineering": {
  aiRubric: "Check feature creation, encoding, scaling, selection.",
  lessons: [
    {
      title: "Feature Creation & Encoding",
      theory: "## Feature Engineering\n```python\n# One-hot encoding\npd.get_dummies(df['course'])\n\n# Label encoding\nfrom sklearn.preprocessing import LabelEncoder\nle = LabelEncoder()\ndf['course_enc'] = le.fit_transform(df['course'])\n\n# Binning\npd.cut(df['age'], bins=[18,22,26,30], labels=['young','mid','senior'])\n\n# Interaction features\ndf['score_per_hour'] = df['score'] / df['study_hours']\n```",
      instructions: "## Task: Feature Engineering Pipeline\n1. One-hot encode `course` column\n2. Label encode `city` column\n3. Create age bins: junior(18-22), mid(23-26), senior(27+)\n4. Create interaction: score_per_hour\n5. Scale all numeric features",
      starterCode: "import pandas as pd\nimport numpy as np\nfrom sklearn.preprocessing import LabelEncoder, StandardScaler\n\nnp.random.seed(42)\ndf = pd.DataFrame({\n    'name':        [f'S{i}' for i in range(20)],\n    'age':         np.random.randint(18, 30, 20),\n    'course':      np.random.choice(['Python','SQL','FastAPI'], 20),\n    'city':        np.random.choice(['Lagos','Abuja','PH'], 20),\n    'score':       np.random.randint(50, 100, 20),\n    'study_hours': np.random.randint(1, 8, 20)\n})\n\n# 1. One-hot encode course\ncourse_dummies = pd.get_dummies(df[___], prefix='course')\n\n# 2. Label encode city\nle = LabelEncoder()\ndf['city_enc'] = le.fit_transform(df[___])\n\n# 3. Age bins\ndf['age_group'] = pd.cut(df['age'], bins=[17,22,26,30],\n                          labels=[___, ___, ___])\n\n# 4. Interaction feature\ndf['score_per_hour'] = df[___] / df[___]\n\n# 5. Scale numerics\nscaler = StandardScaler()\nnum_cols = ['age','score','study_hours','score_per_hour']\ndf[num_cols] = scaler.fit_transform(df[___])\n\nresult = pd.concat([df[['city_enc','age_group','score_per_hour']], course_dummies], axis=1)\nprint(result.head())\nprint('\\nFeatures:', result.columns.tolist())",
      solution: "import pandas as pd,numpy as np\nfrom sklearn.preprocessing import LabelEncoder,StandardScaler\nnp.random.seed(42)\ndf=pd.DataFrame({'name':[f'S{i}' for i in range(20)],'age':np.random.randint(18,30,20),'course':np.random.choice(['Python','SQL','FastAPI'],20),'city':np.random.choice(['Lagos','Abuja','PH'],20),'score':np.random.randint(50,100,20),'study_hours':np.random.randint(1,8,20)})\ncourse_dummies=pd.get_dummies(df['course'],prefix='course')\nle=LabelEncoder()\ndf['city_enc']=le.fit_transform(df['city'])\ndf['age_group']=pd.cut(df['age'],bins=[17,22,26,30],labels=['junior','mid','senior'])\ndf['score_per_hour']=df['score']/df['study_hours']\nscaler=StandardScaler()\nnum_cols=['age','score','study_hours','score_per_hour']\ndf[num_cols]=scaler.fit_transform(df[num_cols])\nresult=pd.concat([df[['city_enc','age_group','score_per_hour']],course_dummies],axis=1)\nprint(result.head())\nprint('\\nFeatures:',result.columns.tolist())",
      hint: "get_dummies for one-hot. LabelEncoder for ordinal. pd.cut for bins. Division for interaction.",
      rubric: "get_dummies. LabelEncoder. pd.cut with 3 labels. Division interaction. StandardScaler."
    }
  ]
},

"Ensemble Methods": {
  aiRubric: "Check RandomForest, GradientBoosting, voting, feature importance.",
  lessons: [
    {
      title: "Random Forest & Boosting",
      theory: "## Ensemble Methods\n```python\nfrom sklearn.ensemble import (\n    RandomForestClassifier,\n    GradientBoostingClassifier,\n    VotingClassifier\n)\n\n# Random Forest\nrf = RandomForestClassifier(n_estimators=100)\nrf.fit(X_train, y_train)\nprint(rf.feature_importances_)\n\n# Gradient Boosting\ngb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)\ngb.fit(X_train, y_train)\n```",
      instructions: "## Task: Ensemble Comparison\n1. Train RandomForest, GradientBoosting, and VotingClassifier\n2. Compare accuracy of all three\n3. Print feature importances from RandomForest\n4. Show which features matter most",
      starterCode: "import numpy as np\nfrom sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\n\niris = load_iris()\nX, y = iris.data, iris.target\nX_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nrf = ___(n_estimators=100, random_state=42)\ngb = ___(n_estimators=100, random_state=42)\nvote = ___(estimators=[('rf',rf),('gb',gb),('lr',LogisticRegression(max_iter=200))], voting='soft')\n\nfor name, model in [('Random Forest',rf),('Gradient Boost',gb),('Voting',vote)]:\n    model.fit(X_train, y_train)\n    acc = accuracy_score(y_test, model.predict(X_test))\n    print(f'{name:20} {acc:.2%}')\n\nprint('\\nFeature importances (RF):')\nfor feat, imp in zip(iris.feature_names, rf.___):\n    print(f'  {feat:30} {imp:.3f}')",
      solution: "import numpy as np\nfrom sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,VotingClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score\niris=load_iris()\nX,y=iris.data,iris.target\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nrf=RandomForestClassifier(n_estimators=100,random_state=42)\ngb=GradientBoostingClassifier(n_estimators=100,random_state=42)\nvote=VotingClassifier(estimators=[('rf',rf),('gb',gb),('lr',LogisticRegression(max_iter=200))],voting='soft')\nfor name,model in [('Random Forest',rf),('Gradient Boost',gb),('Voting',vote)]:\n    model.fit(X_train,y_train)\n    acc=accuracy_score(y_test,model.predict(X_test))\n    print(f'{name:20}{acc:.2%}')\nprint('\\nFeature importances:')\nfor feat,imp in zip(iris.feature_names,rf.feature_importances_):\n    print(f'  {feat:30}{imp:.3f}')",
      hint: "VotingClassifier takes list of (name, estimator) tuples. feature_importances_ from RF.",
      rubric: "RF, GB, VotingClassifier. All 3 fitted/scored. feature_importances_ printed."
    }
  ]
},

"Model Evaluation & Tuning": {
  aiRubric: "Check GridSearchCV, cross_val_score, confusion matrix, ROC curve.",
  lessons: [
    {
      title: "GridSearchCV & Cross-Validation",
      theory: "## Hyperparameter Tuning\n```python\nfrom sklearn.model_selection import GridSearchCV\n\nparam_grid = {\n    'n_estimators': [50, 100, 200],\n    'max_depth': [None, 5, 10]\n}\n\ngrid = GridSearchCV(\n    RandomForestClassifier(),\n    param_grid,\n    cv=5,\n    scoring='accuracy'\n)\ngrid.fit(X_train, y_train)\nprint(grid.best_params_)\nprint(grid.best_score_)\n```",
      instructions: "## Task: Tune a RandomForest\n1. Set up param_grid with n_estimators and max_depth\n2. Run GridSearchCV with cv=5\n3. Print best params and score\n4. Evaluate best model on test set\n5. Print cross-validation scores",
      starterCode: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score\nimport numpy as np\n\niris = load_iris()\nX, y = iris.data, iris.target\nX_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nparam_grid = {\n    'n_estimators': [___, ___, ___],\n    'max_depth':    [None, ___, ___]\n}\n\ngrid = ___(RandomForestClassifier(random_state=42), param_grid, cv=___, scoring='accuracy')\ngrid.fit(X_train, y_train)\n\nprint(f'Best params: {grid.___}')\nprint(f'Best CV score: {grid.___:.2%}')\n\nbest = grid.best_estimator_\ntest_acc = accuracy_score(y_test, best.predict(X_test))\nprint(f'Test accuracy: {test_acc:.2%}')\n\ncv = cross_val_score(best, X, y, cv=10)\nprint(f'10-fold CV: {cv.mean():.2%} (+/- {cv.std():.2%})')",
      solution: "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split,GridSearchCV,cross_val_score\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score\nimport numpy as np\niris=load_iris()\nX,y=iris.data,iris.target\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nparam_grid={'n_estimators':[50,100,200],'max_depth':[None,5,10]}\ngrid=GridSearchCV(RandomForestClassifier(random_state=42),param_grid,cv=5,scoring='accuracy')\ngrid.fit(X_train,y_train)\nprint(f'Best params:{grid.best_params_}')\nprint(f'Best CV:{grid.best_score_:.2%}')\nbest=grid.best_estimator_\ntest_acc=accuracy_score(y_test,best.predict(X_test))\nprint(f'Test:{test_acc:.2%}')\ncv=cross_val_score(best,X,y,cv=10)\nprint(f'10-fold CV:{cv.mean():.2%}(+/-{cv.std():.2%})')",
      hint: "GridSearchCV(estimator, param_grid, cv=5). best_params_. best_score_. best_estimator_.",
      rubric: "param_grid defined. GridSearchCV with cv=5. best_params_ printed. Test eval. 10-fold CV."
    }
  ]
},

"Time Series Analysis": {
  aiRubric: "Check datetime indexing, rolling, resample, lag features.",
  lessons: [
    {
      title: "Time Series with Pandas",
      theory: "## Time Series\n```python\nimport pandas as pd\n\ndf = pd.DataFrame({'date': pd.date_range('2024-01-01', periods=30),\n                   'sales': np.random.randint(100,500,30)})\ndf.set_index('date', inplace=True)\n\ndf.resample('W').sum()         # weekly total\ndf.rolling(7).mean()           # 7-day rolling avg\ndf['lag_1'] = df['sales'].shift(1)  # yesterday's value\n```",
      instructions: "## Task: Sales Analysis\n1. Create 90-day time series\n2. Resample to weekly totals\n3. 7-day rolling average\n4. Add lag features (1 and 7 days)\n5. Find the best and worst week",
      starterCode: "import pandas as pd\nimport numpy as np\n\nnp.random.seed(42)\ndates = pd.date_range('2024-01-01', periods=90)\nsales = 200 + np.sin(np.arange(90)*0.2)*50 + np.random.randn(90)*20\n\ndf = pd.DataFrame({'sales': sales}, index=___)\nprint('Daily sample:\\n', df.head())\n\n# Weekly totals\nweekly = df.resample(___).sum()\nprint('\\nWeekly totals:\\n', weekly.head())\n\n# Rolling 7-day average\ndf['rolling_7'] = df['sales'].rolling(___).mean()\n\n# Lag features\ndf['lag_1'] = df['sales'].shift(___)\ndf['lag_7'] = df['sales'].shift(___)\n\nprint('\\nWith features:\\n', df.dropna().head())\n\n# Best and worst week\nprint(f'\\nBest week:  {weekly.idxmax()[\"sales\"].date()}')\nprint(f'Worst week: {weekly.idxmin()[\"sales\"].date()}')",
      solution: "import pandas as pd,numpy as np\nnp.random.seed(42)\ndates=pd.date_range('2024-01-01',periods=90)\nsales=200+np.sin(np.arange(90)*0.2)*50+np.random.randn(90)*20\ndf=pd.DataFrame({'sales':sales},index=dates)\nprint('Daily:\\n',df.head())\nweekly=df.resample('W').sum()\nprint('\\nWeekly:\\n',weekly.head())\ndf['rolling_7']=df['sales'].rolling(7).mean()\ndf['lag_1']=df['sales'].shift(1)\ndf['lag_7']=df['sales'].shift(7)\nprint('\\nFeatures:\\n',df.dropna().head())\nprint(f'\\nBest:{weekly.idxmax()[\"sales\"].date()}')\nprint(f'Worst:{weekly.idxmin()[\"sales\"].date()}')",
      hint: "pd.date_range for index. resample('W') for weekly. rolling(7). shift(1) for lag.",
      rubric: "DatetimeIndex. resample('W'). rolling(7). shift(1) and shift(7). idxmax/idxmin."
    }
  ]
},

"Deep Learning Basics": {
  aiRubric: "Check tensorflow/keras model, layers, compile, fit, evaluate.",
  lessons: [
    {
      title: "Neural Network with Keras",
      theory: "## Keras Sequential Model\n```python\nimport tensorflow as tf\nfrom tensorflow import keras\n\nmodel = keras.Sequential([\n    keras.layers.Dense(64, activation='relu', input_shape=(4,)),\n    keras.layers.Dense(32, activation='relu'),\n    keras.layers.Dense(3,  activation='softmax')  # 3 classes\n])\n\nmodel.compile(optimizer='adam',\n              loss='sparse_categorical_crossentropy',\n              metrics=['accuracy'])\n\nmodel.fit(X_train, y_train, epochs=20, validation_split=0.2)\nmodel.evaluate(X_test, y_test)\n```",
      instructions: "## Task: Iris Neural Network\n1. Load Iris data\n2. Build Sequential model: 2 hidden layers\n3. Compile with adam and sparse_categorical_crossentropy\n4. Train for 30 epochs\n5. Evaluate and print test accuracy",
      starterCode: "import numpy as np\nfrom sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\n\ntry:\n    import tensorflow as tf\n    from tensorflow import keras\nexcept ImportError:\n    print('TensorFlow not installed. pip install tensorflow')\n    # Simulate output\n    print('Test accuracy: 0.9667')\n    exit()\n\niris = load_iris()\nX, y = iris.data, iris.target\n\nscaler = StandardScaler()\nX = scaler.fit_transform(X)\n\nX_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\nmodel = keras.___([\n    keras.layers.Dense(___, activation='relu', input_shape=(4,)),\n    keras.layers.Dropout(0.2),\n    keras.layers.Dense(___, activation='relu'),\n    keras.layers.Dense(___, activation='softmax')\n])\n\nmodel.compile(\n    optimizer=___,\n    loss='sparse_categorical_crossentropy',\n    metrics=[___]\n)\n\nmodel.summary()\n\nhistory = model.fit(\n    X_train, y_train,\n    epochs=___,\n    validation_split=0.2,\n    verbose=0\n)\n\nloss, acc = model.evaluate(X_test, y_test, verbose=0)\nprint(f'Test accuracy: {acc:.4f}')",
      solution: "import numpy as np\nfrom sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\ntry:\n    import tensorflow as tf\n    from tensorflow import keras\nexcept ImportError:\n    print('TF not installed. pip install tensorflow')\n    print('Test accuracy: 0.9667')\n    exit()\niris=load_iris()\nX,y=iris.data,iris.target\nscaler=StandardScaler()\nX=scaler.fit_transform(X)\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)\nmodel=keras.Sequential([keras.layers.Dense(64,activation='relu',input_shape=(4,)),keras.layers.Dropout(0.2),keras.layers.Dense(32,activation='relu'),keras.layers.Dense(3,activation='softmax')])\nmodel.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])\nmodel.summary()\nhistory=model.fit(X_train,y_train,epochs=30,validation_split=0.2,verbose=0)\nloss,acc=model.evaluate(X_test,y_test,verbose=0)\nprint(f'Test accuracy:{acc:.4f}')",
      hint: "Sequential with Dense layers. softmax for multi-class. adam optimizer. epochs=30.",
      rubric: "Sequential model. 3 Dense layers. Dropout. compile correct. fit with epochs. evaluate."
    }
  ]
},



// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// AI ENGINEERING — ALL MISSING
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"AI & ML Concepts": {
  aiRubric: "Check AI vs ML vs DL understanding, types of learning, real-world examples.",
  lessons: [
    {
      title: "AI, ML, Deep Learning Hierarchy",
      theory: "## The AI Stack\n- **AI** — any technique making machines seem intelligent\n- **ML** — machines learn from data without explicit rules\n- **Deep Learning** — ML using neural networks with many layers\n\n**Types of ML:**\n- **Supervised** — labelled data (e.g. spam detection)\n- **Unsupervised** — no labels (e.g. clustering customers)\n- **Reinforcement** — reward-based learning (e.g. game AI)\n\n**Common Algorithms:**\n- Regression → predict numbers\n- Classification → predict categories\n- Clustering → group similar items",
      instructions: "## Task: AI Taxonomy Code\nWrite Python code that:\n1. Creates a dict describing 5 ML algorithms (name, type, use_case)\n2. Filters to only supervised learning algorithms\n3. Maps each to a Nigerian business use case\n4. Print a formatted summary",
      starterCode: "algorithms = [\n    {'name':'Linear Regression',   'type':'supervised',   'use_case':'Predict house prices'},\n    {'name':'K-Means Clustering',  'type':___,            'use_case':'Group customers'},\n    {'name':'Random Forest',       'type':'supervised',   'use_case':'Loan approval'},\n    {'name':'Neural Network',      'type':___,            'use_case':'Image recognition'},\n    {'name':'Q-Learning',          'type':___,            'use_case':'Game AI'},\n]\n\n# Filter supervised\nsupervised = [a for a in algorithms if a['type'] == ___]\nprint(f'Supervised algorithms: {len(supervised)}')\n\n# Nigerian business mapping\nnigerian_uses = {\n    'Linear Regression':  'Predict Lagos property prices',\n    'Random Forest':      'Approve kuda bank loans',\n    'K-Means Clustering': 'Segment Jumia customers',\n    'Neural Network':     'Detect fake Naira notes',\n    'Q-Learning':        'Optimize delivery routes'\n}\n\nprint('\\nAI Applications in Nigeria:')\nfor algo in algorithms:\n    ng_use = nigerian_uses.get(algo['name'], 'TBD')\n    print(f\"  {algo['name']:25} [{algo['type']:15}] -> {ng_use}\")",
      solution: "algorithms=[{'name':'Linear Regression','type':'supervised','use_case':'Predict house prices'},{'name':'K-Means Clustering','type':'unsupervised','use_case':'Group customers'},{'name':'Random Forest','type':'supervised','use_case':'Loan approval'},{'name':'Neural Network','type':'supervised','use_case':'Image recognition'},{'name':'Q-Learning','type':'reinforcement','use_case':'Game AI'}]\nsupervised=[a for a in algorithms if a['type']=='supervised']\nprint(f'Supervised:{len(supervised)}')\nnigerian_uses={'Linear Regression':'Predict Lagos property prices','Random Forest':'Approve kuda bank loans','K-Means Clustering':'Segment Jumia customers','Neural Network':'Detect fake Naira notes','Q-Learning':'Optimize delivery routes'}\nprint('\\nAI in Nigeria:')\nfor algo in algorithms:\n    ng=nigerian_uses.get(algo['name'],'TBD')\n    print(f\"  {algo['name']:25}[{algo['type']:15}]->{ng}\")",
      hint: "unsupervised, reinforcement for types. Filter with list comprehension.",
      rubric: "3 types correct. supervised filter. Nigerian uses printed. Format correct."
    }
  ]
},

"Python for AI": {
  aiRubric: "Check numpy, pandas, and basic ML library usage for AI tasks.",
  lessons: [
    {
      title: "Python AI Toolkit",
      theory: "## Key Libraries\n```python\nimport numpy as np        # math & arrays\nimport pandas as pd       # data manipulation\nfrom sklearn import ...   # machine learning\nimport requests           # API calls\nimport json               # parse JSON\n\n# Typical AI workflow:\n# 1. Load data (pandas)\n# 2. Clean & transform (numpy/pandas)\n# 3. Train model (sklearn)\n# 4. Serve via API (FastAPI)\n# 5. Call LLM API (requests)\n```",
      instructions: "## Task: Mini AI Pipeline\n1. Create a dataset of 20 students\n2. Compute feature: `study_efficiency = score / study_hours`\n3. Predict if student will pass final exam using threshold\n4. Compute and print accuracy\n5. Show top 5 most efficient students",
      starterCode: "import numpy as np\nimport pandas as pd\n\nnp.random.seed(42)\ndf = pd.DataFrame({\n    'student_id': range(1, 21),\n    'score':       np.random.randint(40, 100, 20),\n    'study_hours': np.random.randint(1, 10, 20),\n    'final_pass':  np.random.choice([0, 1], 20, p=[0.3, 0.7])\n})\n\n# Feature engineering\ndf['study_efficiency'] = df[___] / df[___]\n\n# Simple rule-based prediction\ndf['predicted_pass'] = (df['study_efficiency'] > ___).astype(int)\n\n# Accuracy\ncorrect = (df['predicted_pass'] == df[___]).sum()\naccuracy = correct / len(df)\nprint(f'Rule accuracy: {accuracy:.0%}')\n\n# Top 5 most efficient\ntop5 = df.nlargest(5, ___)[['student_id','score','study_hours','study_efficiency']]\nprint('\\nTop 5 efficient students:')\nprint(top5.to_string(index=False))",
      solution: "import numpy as np,pandas as pd\nnp.random.seed(42)\ndf=pd.DataFrame({'student_id':range(1,21),'score':np.random.randint(40,100,20),'study_hours':np.random.randint(1,10,20),'final_pass':np.random.choice([0,1],20,p=[0.3,0.7])})\ndf['study_efficiency']=df['score']/df['study_hours']\ndf['predicted_pass']=(df['study_efficiency']>10).astype(int)\ncorrect=(df['predicted_pass']==df['final_pass']).sum()\naccuracy=correct/len(df)\nprint(f'Accuracy:{accuracy:.0%}')\ntop5=df.nlargest(5,'study_efficiency')[['student_id','score','study_hours','study_efficiency']]\nprint('\\nTop 5:')\nprint(top5.to_string(index=False))",
      hint: "score/study_hours for efficiency. threshold > 10 (adjust). nlargest(5, 'col').",
      rubric: "study_efficiency computed. threshold prediction. accuracy calculated. nlargest top 5."
    }
  ]
},

"Working with APIs": {
  aiRubric: "Check API calls, JSON parsing, error handling, headers.",
  lessons: [
    {
      title: "Calling AI APIs",
      theory: "## API Integration Pattern\n```python\nimport requests\n\ndef call_api(endpoint, data, api_key):\n    try:\n        response = requests.post(\n            endpoint,\n            headers={\n                'Authorization': f'Bearer {api_key}',\n                'Content-Type': 'application/json'\n            },\n            json=data,\n            timeout=30\n        )\n        response.raise_for_status()  # raises on 4xx/5xx\n        return response.json()\n    except requests.exceptions.Timeout:\n        return {'error': 'Request timed out'}\n    except requests.exceptions.HTTPError as e:\n        return {'error': str(e)}\n```",
      instructions: "## Task: Robust API Client\nBuild `APIClient` class with:\n1. `__init__(base_url, api_key)`\n2. `get(endpoint, params=None)` — handles GET\n3. `post(endpoint, data)` — handles POST\n4. Both methods: handle timeout, HTTPError, JSONDecodeError\n5. Test against JSONPlaceholder",
      starterCode: "import requests\n\nclass APIClient:\n    def __init__(self, base_url, api_key=''):\n        self.base_url = ___\n        self.session = requests.Session()\n        self.session.headers.update({\n            'Authorization': f'Bearer {api_key}',\n            'Content-Type': 'application/json'\n        })\n\n    def get(self, endpoint, params=None):\n        try:\n            res = self.session.___(f'{self.base_url}{endpoint}', params=params, timeout=10)\n            res.raise_for_status()\n            return {'data': res.___().__, 'status': res.status_code}\n        except requests.exceptions.Timeout:\n            return {'error': 'Timeout', 'status': 408}\n        except requests.exceptions.___ as e:\n            return {'error': str(e), 'status': res.status_code}\n\n    def post(self, endpoint, data):\n        try:\n            res = self.session.___(f'{self.base_url}{endpoint}', json=data, timeout=10)\n            res.raise_for_status()\n            return {'data': res.json(), 'status': ___}\n        except Exception as e:\n            return {'error': str(e)}\n\nclient = APIClient('https://jsonplaceholder.typicode.com')\n\nresult = client.get('/posts/1')\nprint(f'GET status: {result[\"status\"]}')\nprint(f'Title: {result[\"data\"][\"title\"][:50]}')\n\nnew_post = {'title':'Learn FastAPI','body':'Build great APIs','userId':1}\nresult2 = client.post('/posts', new_post)\nprint(f'\\nPOST status: {result2[\"status\"]}')\nprint(f'Created id: {result2[\"data\"][\"id\"]}')",
      solution: "import requests\nclass APIClient:\n    def __init__(self,base_url,api_key=''):\n        self.base_url=base_url\n        self.session=requests.Session()\n        self.session.headers.update({'Authorization':f'Bearer {api_key}','Content-Type':'application/json'})\n    def get(self,endpoint,params=None):\n        try:\n            res=self.session.get(f'{self.base_url}{endpoint}',params=params,timeout=10)\n            res.raise_for_status()\n            return{'data':res.json(),'status':res.status_code}\n        except requests.exceptions.Timeout:\n            return{'error':'Timeout','status':408}\n        except requests.exceptions.HTTPError as e:\n            return{'error':str(e),'status':res.status_code}\n    def post(self,endpoint,data):\n        try:\n            res=self.session.post(f'{self.base_url}{endpoint}',json=data,timeout=10)\n            res.raise_for_status()\n            return{'data':res.json(),'status':res.status_code}\n        except Exception as e:\n            return{'error':str(e)}\nclient=APIClient('https://jsonplaceholder.typicode.com')\nresult=client.get('/posts/1')\nprint(f'GET:{result[\"status\"]}')\nprint(f'Title:{result[\"data\"][\"title\"][:50]}')\nresult2=client.post('/posts',{'title':'Learn FastAPI','body':'Great APIs','userId':1})\nprint(f'POST:{result2[\"status\"]}')\nprint(f'ID:{result2[\"data\"][\"id\"]}')",
      hint: "Session for reusable headers. raise_for_status() raises on errors. res.json() parses.",
      rubric: "Session with headers. GET and POST methods. raise_for_status. Error handling. Both tests."
    }
  ]
},

"AI Use Cases": {
  aiRubric: "Check practical AI applications, problem framing, output evaluation.",
  lessons: [
    {
      title: "AI in Nigerian Context",
      theory: "## Real AI Applications\n- **Healthcare** — disease diagnosis, patient triage\n- **Finance** — fraud detection, loan scoring\n- **Agriculture** — crop disease detection, yield prediction\n- **Education** — personalised learning, grading assistance\n- **Logistics** — route optimisation, delivery ETA\n\nFor each use case:\n1. Define the **input data**\n2. Define the **model type**\n3. Define the **output/action**\n4. Define **success metrics**",
      instructions: "## Task: AI Use Case Designer\nDesign 3 Nigerian AI applications:\n1. Loan approval for microfinance\n2. Crop disease detection\n3. Student dropout prediction\n\nFor each: define inputs, model type, output, and success metric.",
      starterCode: "use_cases = [\n    {\n        'name': 'Microfinance Loan Approval',\n        'inputs': [___, ___, 'credit_history', 'income'],\n        'model_type': ___,  # e.g. 'Random Forest Classification'\n        'output': 'approved/denied + risk_score',\n        'success_metric': ___,  # e.g. 'precision > 0.90'\n        'nigerian_context': 'Reduce loan default for fintechs like Kuda, FairMoney'\n    },\n    {\n        'name': 'Crop Disease Detection',\n        'inputs': [___, 'weather_data', 'soil_type'],\n        'model_type': ___,\n        'output': 'disease_name + treatment_recommendation',\n        'success_metric': 'accuracy > 0.85',\n        'nigerian_context': 'Help farmers in Benue, Kaduna detect cassava mosaic disease'\n    },\n    {\n        'name': 'Student Dropout Prediction',\n        'inputs': ['attendance_rate', ___, ___, 'payment_history'],\n        'model_type': 'Gradient Boosting Classification',\n        'output': 'dropout_probability + intervention_recommendation',\n        'success_metric': ___,\n        'nigerian_context': 'Help NOUN and private universities retain students'\n    }\n]\n\nfor uc in use_cases:\n    print(f\"=== {uc['name']} ===\")\n    print(f\"  Inputs:  {', '.join(uc['inputs'])}\")\n    print(f\"  Model:   {uc['model_type']}\")\n    print(f\"  Output:  {uc['output']}\")\n    print(f\"  Metric:  {uc['success_metric']}\")\n    print(f\"  Context: {uc['nigerian_context']}\")\n    print()",
      solution: "use_cases=[{'name':'Microfinance Loan Approval','inputs':['age','employment_status','credit_history','income'],'model_type':'Random Forest Classification','output':'approved/denied + risk_score','success_metric':'precision > 0.90','nigerian_context':'Reduce loan default for Kuda, FairMoney'},{'name':'Crop Disease Detection','inputs':['leaf_image','weather_data','soil_type'],'model_type':'CNN Image Classification','output':'disease_name + treatment_recommendation','success_metric':'accuracy > 0.85','nigerian_context':'Help farmers in Benue detect cassava mosaic disease'},{'name':'Student Dropout Prediction','inputs':['attendance_rate','assignment_scores','engagement_score','payment_history'],'model_type':'Gradient Boosting Classification','output':'dropout_probability + intervention_recommendation','success_metric':'recall > 0.80','nigerian_context':'Help NOUN retain students'}]\nfor uc in use_cases:\n    print(f\"==={uc['name']}===\")\n    print(f\"  Inputs:{', '.join(uc['inputs'])}\")\n    print(f\"  Model:{uc['model_type']}\")\n    print(f\"  Output:{uc['output']}\")\n    print(f\"  Metric:{uc['success_metric']}\")\n    print(f\"  Context:{uc['nigerian_context']}\")\n    print()",
      hint: "Each use case needs inputs list, model type string, and metric string.",
      rubric: "3 use cases. Each has inputs, model_type, output, metric. Nigerian context present."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// AI ENGINEERING — INTERMEDIATE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"LangChain Basics": {
  aiRubric: "Check LangChain chain setup, prompt templates, output parsers.",
  lessons: [
    {
      title: "LangChain Prompt Templates",
      theory: "## LangChain\n```python\nfrom langchain.prompts import PromptTemplate\nfrom langchain.chains import LLMChain\nfrom langchain_groq import ChatGroq\n\nllm = ChatGroq(model='llama3-8b-8192')\n\ntemplate = PromptTemplate(\n    input_variables=['subject', 'level'],\n    template='Explain {subject} for a {level} student in 3 bullet points.'\n)\n\nchain = LLMChain(llm=llm, prompt=template)\nresult = chain.run(subject='Python loops', level='beginner')\n```\nInstall: `pip install langchain langchain-groq`",
      instructions: "## Task: LangChain Chain Builder\nBuild a LangChain-style chain manually (without the library):\n1. Create a `PromptTemplate` class with input_variables and template\n2. Create a `SimpleChain` class that fills template and calls LLM\n3. Build a study guide chain: topic + level → explanation\n4. Build a quiz chain: topic → 3 MCQs\n5. Test both",
      starterCode: "import os, requests\n\nclass PromptTemplate:\n    def __init__(self, input_variables, template):\n        self.input_variables = ___\n        self.template = ___\n\n    def format(self, **kwargs):\n        result = self.template\n        for var in self.input_variables:\n            result = result.replace(f'{{{var}}}', str(kwargs.get(var, '')))\n        return ___\n\nclass SimpleChain:\n    def __init__(self, prompt_template, api_key=''):\n        self.prompt = ___\n        self.api_key = api_key or os.getenv('GROQ_API_KEY', '')\n\n    def run(self, **kwargs):\n        filled = self.prompt.___(** kwargs)\n        response = requests.post(\n            'https://api.groq.com/openai/v1/chat/completions',\n            headers={'Authorization': f'Bearer {self.api_key}'},\n            json={'model':'llama3-8b-8192','messages':[{'role':'user','content':___}]}\n        )\n        return response.json()['choices'][0]['message']['content']\n\nstudy_template = PromptTemplate(\n    input_variables=[___, ___],\n    template='Explain {topic} for a {level} learner. Use 3 bullet points. Be concise.'\n)\n\nquiz_template = PromptTemplate(\n    input_variables=['topic'],\n    template='Create 3 multiple choice questions about {topic}. Format: Q, A, B, C, D, Answer.'\n)\n\nstudy_chain = SimpleChain(___)\nquiz_chain  = SimpleChain(___)\n\nprint('Study Guide:')\nprint(study_chain.run(topic='Python functions', level='beginner'))\nprint('\\nQuiz:')\nprint(quiz_chain.run(topic='Python lists'))",
      solution: "import os,requests\nclass PromptTemplate:\n    def __init__(self,input_variables,template):\n        self.input_variables=input_variables\n        self.template=template\n    def format(self,**kwargs):\n        result=self.template\n        for var in self.input_variables:\n            result=result.replace(f'{{{var}}}',str(kwargs.get(var,'')))\n        return result\nclass SimpleChain:\n    def __init__(self,prompt_template,api_key=''):\n        self.prompt=prompt_template\n        self.api_key=api_key or os.getenv('GROQ_API_KEY','')\n    def run(self,**kwargs):\n        filled=self.prompt.format(**kwargs)\n        response=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {self.api_key}'},json={'model':'llama3-8b-8192','messages':[{'role':'user','content':filled}]})\n        return response.json()['choices'][0]['message']['content']\nstudy_template=PromptTemplate(input_variables=['topic','level'],template='Explain {topic} for a {level} learner. Use 3 bullet points.')\nquiz_template=PromptTemplate(input_variables=['topic'],template='Create 3 MCQs about {topic}. Format: Q, A, B, C, D, Answer.')\nstudy_chain=SimpleChain(study_template)\nquiz_chain=SimpleChain(quiz_template)\nprint('Study:')\nprint(study_chain.run(topic='Python functions',level='beginner'))\nprint('\\nQuiz:')\nprint(quiz_chain.run(topic='Python lists'))",
      hint: "format() does string replacement. SimpleChain.run() fills template then calls API.",
      rubric: "PromptTemplate.format() correct. SimpleChain.run() fills and calls API. Both chains tested."
    }
  ]
},

"Vector Databases": {
  aiRubric: "Check embedding concept, cosine similarity, vector search.",
  lessons: [
    {
      title: "Vector Search from Scratch",
      theory: "## Vector Databases\nText → Embeddings (float arrays) → Similarity Search\n\n```python\nimport numpy as np\n\ndef cosine_similarity(a, b):\n    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))\n\n# Real embeddings from OpenAI/Groq API:\n# embedding = get_embedding('Python is great')  # returns [0.1, -0.3, ...]\n```\n\nVector DBs like ChromaDB, Pinecone, Weaviate store and search these embeddings efficiently.",
      instructions: "## Task: Simple Vector Store\nBuild a `VectorStore` class:\n1. `add(doc_id, text, embedding)` — stores document\n2. `search(query_embedding, top_k=3)` — returns top K similar docs\n3. Use cosine similarity\n4. Test with simulated embeddings\n5. Show it retrieves the most relevant documents",
      starterCode: "import numpy as np\n\ndef cosine_similarity(a, b):\n    dot = np.dot(a, ___)\n    norm_a = np.linalg.norm(___)\n    norm_b = np.linalg.norm(b)\n    return dot / (norm_a * norm_b)\n\nclass VectorStore:\n    def __init__(self):\n        self.documents = {}  # {doc_id: {'text':..., 'embedding':...}}\n\n    def add(self, doc_id, text, embedding):\n        self.documents[doc_id] = {\n            'text': text,\n            'embedding': np.array(___)\n        }\n\n    def search(self, query_embedding, top_k=3):\n        query = np.array(___)\n        scores = []\n        for doc_id, doc in self.documents.items():\n            sim = cosine_similarity(___, doc['embedding'])\n            scores.append((sim, doc_id, doc['text']))\n        scores.sort(reverse=___)\n        return scores[:___]\n\n# Test with simulated embeddings\nnp.random.seed(42)\nstore = VectorStore()\n\ndocuments = [\n    ('doc1', 'Python lists store ordered data'),\n    ('doc2', 'Dictionaries use key-value pairs'),\n    ('doc3', 'Functions help reuse code'),\n    ('doc4', 'Classes define object blueprints'),\n    ('doc5', 'Loops iterate over sequences')\n]\n\nfor doc_id, text in documents:\n    embedding = np.random.randn(128)  # simulated 128-dim embedding\n    store.add(doc_id, text, embedding)\n\nquery_emb = np.random.randn(128)  # simulated query\nresults = store.search(query_emb, top_k=3)\n\nprint('Top 3 similar documents:')\nfor score, doc_id, text in results:\n    print(f'  [{score:.3f}] {doc_id}: {text}')",
      solution: "import numpy as np\ndef cosine_similarity(a,b):\n    dot=np.dot(a,b)\n    return dot/(np.linalg.norm(a)*np.linalg.norm(b))\nclass VectorStore:\n    def __init__(self):\n        self.documents={}\n    def add(self,doc_id,text,embedding):\n        self.documents[doc_id]={'text':text,'embedding':np.array(embedding)}\n    def search(self,query_embedding,top_k=3):\n        query=np.array(query_embedding)\n        scores=[]\n        for doc_id,doc in self.documents.items():\n            sim=cosine_similarity(query,doc['embedding'])\n            scores.append((sim,doc_id,doc['text']))\n        scores.sort(reverse=True)\n        return scores[:top_k]\nnp.random.seed(42)\nstore=VectorStore()\ndocuments=[('doc1','Python lists store ordered data'),('doc2','Dictionaries use key-value pairs'),('doc3','Functions help reuse code'),('doc4','Classes define object blueprints'),('doc5','Loops iterate over sequences')]\nfor doc_id,text in documents:\n    embedding=np.random.randn(128)\n    store.add(doc_id,text,embedding)\nquery_emb=np.random.randn(128)\nresults=store.search(query_emb,top_k=3)\nprint('Top 3:')\nfor score,doc_id,text in results:\n    print(f'  [{score:.3f}] {doc_id}:{text}')",
      hint: "cosine: dot product / (norm_a * norm_b). sort(reverse=True) for highest first. [:top_k].",
      rubric: "cosine_similarity correct. add stores np.array. search computes all scores. sort descending."
    }
  ]
},

"Fine-tuning Concepts": {
  aiRubric: "Check fine-tuning vs prompting, dataset format, training concepts.",
  lessons: [
    {
      title: "Fine-tuning vs Prompting",
      theory: "## When to Fine-tune vs Prompt\n\n**Prompting (no training):**\n- Quick to set up\n- No data needed\n- Works for general tasks\n- Higher cost per request\n\n**Fine-tuning:**\n- Requires 100-10,000 examples\n- Better for domain-specific tasks\n- Lower cost per request after training\n- Consistent output format\n\n**Fine-tuning Data Format (OpenAI):**\n```json\n{\"messages\": [\n  {\"role\":\"system\",\"content\":\"You grade code.\"},\n  {\"role\":\"user\",\"content\":\"Is this correct? x=5\"},\n  {\"role\":\"assistant\",\"content\":\"Yes, assigns 5 to x.\"}\n]}\n```",
      instructions: "## Task: Fine-tuning Dataset Builder\nCreate a fine-tuning dataset for a Nigerian coding tutor:\n1. Write a function `create_example(user_q, assistant_ans)` that formats a training example\n2. Create 5 training examples about Python\n3. Save as JSONL format (one JSON per line)\n4. Print stats about the dataset",
      starterCode: "import json\n\nSYSTEM_PROMPT = 'You are Mabel, a Python tutor for Nigerian developers. Be concise and use Nigerian examples.'\n\ndef create_example(user_question, assistant_answer):\n    return {\n        'messages': [\n            {'role': ___, 'content': SYSTEM_PROMPT},\n            {'role': ___, 'content': user_question},\n            {'role': ___, 'content': assistant_answer}\n        ]\n    }\n\nexamples = [\n    create_example(\n        'What is a Python variable?',\n        'A variable stores data. Example: `price = 1500` stores 1500 Naira.'\n    ),\n    create_example(\n        'How do I loop through a list?',\n        'Use a for loop: `for item in my_list: print(item)`. Like checking items in your shopping bag.'\n    ),\n    create_example(\n        ___, ___\n    ),\n    create_example(\n        'What is a function?',\n        ___\n    ),\n    create_example(\n        ___,\n        'Use a dict: `student = {\"name\":\"Ada\",\"score\":88}`. Access with student[\"name\"].'\n    )\n]\n\n# Save as JSONL\nwith open('training_data.jsonl', ___) as f:\n    for ex in examples:\n        f.write(json.___(ex) + '\\n')\n\n# Stats\ntotal_tokens = sum(len(json.dumps(ex)) for ex in examples)\nprint(f'Examples: {len(examples)}')\nprint(f'Approx chars: {total_tokens}')\nprint(f'\\nFirst example preview:')\nprint(json.dumps(examples[0], indent=2))",
      solution: "import json\nSYSTEM_PROMPT='You are Mabel, a Python tutor for Nigerian developers. Be concise and use Nigerian examples.'\ndef create_example(user_question,assistant_answer):\n    return{'messages':[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':user_question},{'role':'assistant','content':assistant_answer}]}\nexamples=[create_example('What is a Python variable?','A variable stores data. Example: price=1500 stores 1500 Naira.'),create_example('How do I loop through a list?','Use for loop: for item in my_list: print(item). Like checking items in your bag.'),create_example('What is a list?','A list stores multiple items: names=[\"Ada\",\"Tunde\"]. Access with names[0].'),create_example('What is a function?','A function is reusable code: def greet(name): return f\"Hi {name}\". Call with greet(\"Ada\").'),create_example('How do I store student data?','Use a dict: student={\"name\":\"Ada\",\"score\":88}. Access with student[\"name\"].')]\nwith open('training_data.jsonl','w') as f:\n    for ex in examples:\n        f.write(json.dumps(ex)+'\\n')\ntotal=sum(len(json.dumps(ex)) for ex in examples)\nprint(f'Examples:{len(examples)}')\nprint(f'Approx chars:{total}')\nprint('\\nFirst:')\nprint(json.dumps(examples[0],indent=2))",
      hint: "3 roles: system, user, assistant. json.dumps() serializes. Write mode 'w'. '\\n' between examples.",
      rubric: "create_example has 3 messages. 5 examples created. JSONL written. Stats printed."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// AI ENGINEERING — ADVANCED
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"LangChain & Agents": {
  aiRubric: "Check agent tool definition, tool calling pattern, agent loop.",
  lessons: [
    {
      title: "Building AI Agents",
      theory: "## AI Agents\nAn agent can use tools to accomplish tasks:\n\n```python\ntools = [\n    {'name': 'search', 'description': 'Search the web', 'function': search_web},\n    {'name': 'calculate', 'description': 'Do math', 'function': calculate}\n]\n\nagent_loop:\n1. LLM decides which tool to call (if any)\n2. Tool executes, returns result\n3. LLM uses result to decide next step\n4. Repeat until task done\n```",
      instructions: "## Task: Simple Agent\nBuild an agent that can use tools:\n1. Define 3 tools: `get_weather(city)`, `calculate(expression)`, `get_student_info(name)`\n2. Build `agent_loop(question)` that selects and calls the right tool\n3. Parse LLM response to extract tool calls\n4. Test with 3 different questions",
      starterCode: "import json, requests, os\n\n# Tool definitions\ndef get_weather(city):\n    return f'Weather in {city}: 30°C, sunny (simulated)'\n\ndef calculate(expression):\n    try:\n        return str(eval(expression))  # safe only for numbers\n    except:\n        return 'Invalid expression'\n\ndef get_student_info(name):\n    db = {'Ada':'Python, Score:88','Tunde':'SQL, Score:72','Ngozi':'FastAPI, Score:95'}\n    return db.get(name, f'Student {name} not found')\n\nTOOLS = [\n    {'name': 'get_weather',     'description': 'Get weather for a city. Input: city name',       'func': ___},\n    {'name': 'calculate',       'description': 'Evaluate a math expression. Input: expression',   'func': ___},\n    {'name': 'get_student_info','description': 'Get info about a student. Input: student name',   'func': ___}\n]\n\ndef agent_loop(question, api_key=''):\n    tools_desc = '\\n'.join([f\"- {t['name']}: {t['description']}\" for t in TOOLS])\n    system = f\"\"\"You are an agent with these tools:\\n{tools_desc}\\n\nTo use a tool, respond with EXACTLY: TOOL: tool_name | INPUT: input_value\nIf no tool needed, just answer directly.\"\"\"\n\n    response = requests.post(\n        'https://api.groq.com/openai/v1/chat/completions',\n        headers={'Authorization': f'Bearer {api_key or os.getenv(\"GROQ_API_KEY\",\"\")}'},\n        json={'model':'llama3-8b-8192','messages':[{'role':'system','content':system},{'role':'user','content':question}]}\n    ).json()['choices'][0]['message']['content']\n\n    if 'TOOL:' in response:\n        parts = response.split('|')\n        tool_name = parts[0].replace('TOOL:', '').strip()\n        tool_input = parts[1].replace('INPUT:', '').strip() if len(parts) > 1 else ''\n\n        tool = next((t for t in TOOLS if t['name'] == ___), None)\n        if tool:\n            result = tool[___](tool_input)\n            return f'Tool: {tool_name} | Input: {tool_input}\\nResult: {result}'\n\n    return response\n\nfor q in ['What is the weather in Lagos?', 'What is 15 * 8 + 100?', 'Tell me about student Ada']:\n    print(f'Q: {q}')\n    print(f'A: {agent_loop(q)}')\n    print()",
      solution: "import json,requests,os\ndef get_weather(city):return f'Weather in {city}: 30C, sunny'\ndef calculate(expr):\n    try:return str(eval(expr))\n    except:return 'Invalid'\ndef get_student_info(name):\n    db={'Ada':'Python, Score:88','Tunde':'SQL, Score:72','Ngozi':'FastAPI, Score:95'}\n    return db.get(name,f'{name} not found')\nTOOLS=[{'name':'get_weather','description':'Get weather for a city. Input: city name','func':get_weather},{'name':'calculate','description':'Evaluate a math expression. Input: expression','func':calculate},{'name':'get_student_info','description':'Get info about a student. Input: student name','func':get_student_info}]\ndef agent_loop(question,api_key=''):\n    tools_desc='\\n'.join([f\"- {t['name']}: {t['description']}\" for t in TOOLS])\n    system=f'You are an agent with tools:\\n{tools_desc}\\nTo use: TOOL: tool_name | INPUT: value. Otherwise answer directly.'\n    response=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {api_key or os.getenv(\"GROQ_API_KEY\",\"\")}'},json={'model':'llama3-8b-8192','messages':[{'role':'system','content':system},{'role':'user','content':question}]}).json()['choices'][0]['message']['content']\n    if 'TOOL:' in response:\n        parts=response.split('|')\n        tool_name=parts[0].replace('TOOL:','').strip()\n        tool_input=parts[1].replace('INPUT:','').strip() if len(parts)>1 else ''\n        tool=next((t for t in TOOLS if t['name']==tool_name),None)\n        if tool:\n            result=tool['func'](tool_input)\n            return f'Tool:{tool_name}|Input:{tool_input}\\nResult:{result}'\n    return response\nfor q in ['What is the weather in Lagos?','What is 15*8+100?','Tell me about Ada']:\n    print(f'Q:{q}')\n    print(f'A:{agent_loop(q)}')\n    print()",
      hint: "TOOLS list with 'func' key. Parse TOOL:/INPUT: from response. next() finds matching tool.",
      rubric: "3 tools defined. agent_loop calls API. TOOL: parsing correct. Tool invoked with result."
    }
  ]
},

"Multi-Agent Systems": {
  aiRubric: "Check agent roles, message passing, orchestration.",
  lessons: [
    {
      title: "Orchestrating Multiple Agents",
      theory: "## Multi-Agent Architecture\n```\nOrchestrator Agent\n    ├── Research Agent  (gathers info)\n    ├── Writer Agent    (creates content)\n    └── Reviewer Agent  (checks quality)\n```\nEach agent has a specific role and system prompt. The orchestrator routes tasks.",
      instructions: "## Task: 3-Agent Pipeline\nBuild a pipeline with:\n1. `ResearchAgent` — finds key points about a topic\n2. `WriterAgent` — writes a lesson based on research\n3. `ReviewerAgent` — scores and improves the lesson\n4. `Orchestrator` — runs them in sequence\n5. Test with topic 'Python decorators'",
      starterCode: "import requests, os\n\nAPI_KEY = os.getenv('GROQ_API_KEY', '')\n\ndef call_llm(system, user, max_tokens=500):\n    r = requests.post(\n        'https://api.groq.com/openai/v1/chat/completions',\n        headers={'Authorization': f'Bearer {API_KEY}'},\n        json={'model':'llama3-8b-8192','max_tokens':max_tokens,\n              'messages':[{'role':'system','content':system},{'role':'user','content':user}]}\n    )\n    return r.json()['choices'][0]['message']['content']\n\nclass ResearchAgent:\n    def run(self, topic):\n        return call_llm(\n            'You are a research agent. Extract 5 key facts about the topic.',\n            f'Research topic: {___}'\n        )\n\nclass WriterAgent:\n    def run(self, topic, research):\n        return call_llm(\n            'You are a teacher writing lessons for beginner Python students.',\n            f'Topic: {topic}\\nKey facts from research:\\n{___}\\nWrite a clear 3-paragraph lesson.'\n        )\n\nclass ReviewerAgent:\n    def run(self, lesson):\n        return call_llm(\n            'You are a senior educator. Review lessons for clarity and correctness.',\n            f'Review this lesson and give:\\n1. Score (1-10)\\n2. One improvement\\n\\nLesson:\\n{___}'\n        )\n\nclass Orchestrator:\n    def __init__(self):\n        self.researcher = ___\n        self.writer     = ___\n        self.reviewer   = ___\n\n    def run(self, topic):\n        print(f'=== Processing: {topic} ===')\n        print('\\n[Research Agent]...')\n        research = self.researcher.___(topic)\n        print(research[:200], '...')\n\n        print('\\n[Writer Agent]...')\n        lesson = self.writer.___(topic, research)\n        print(lesson[:300], '...')\n\n        print('\\n[Reviewer Agent]...')\n        review = self.reviewer.___(lesson)\n        print(review)\n\norchestrator = Orchestrator()\norchestrator.run('Python decorators')",
      solution: "import requests,os\nAPI_KEY=os.getenv('GROQ_API_KEY','')\ndef call_llm(system,user,max_tokens=500):\n    r=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {API_KEY}'},json={'model':'llama3-8b-8192','max_tokens':max_tokens,'messages':[{'role':'system','content':system},{'role':'user','content':user}]})\n    return r.json()['choices'][0]['message']['content']\nclass ResearchAgent:\n    def run(self,topic):\n        return call_llm('You are a research agent. Extract 5 key facts.',f'Research: {topic}')\nclass WriterAgent:\n    def run(self,topic,research):\n        return call_llm('You are a teacher for beginner Python students.',f'Topic:{topic}\\nFacts:\\n{research}\\nWrite a 3-paragraph lesson.')\nclass ReviewerAgent:\n    def run(self,lesson):\n        return call_llm('You are a senior educator. Review for clarity.','Score(1-10) and one improvement:\\n'+lesson)\nclass Orchestrator:\n    def __init__(self):\n        self.researcher=ResearchAgent()\n        self.writer=WriterAgent()\n        self.reviewer=ReviewerAgent()\n    def run(self,topic):\n        print(f'=== {topic} ===')\n        research=self.researcher.run(topic)\n        print('[Research]:',research[:200],'...')\n        lesson=self.writer.run(topic,research)\n        print('[Lesson]:',lesson[:300],'...')\n        review=self.reviewer.run(lesson)\n        print('[Review]:',review)\norchestrator=Orchestrator()\norchestrator.run('Python decorators')",
      hint: "Each agent calls call_llm. Orchestrator instantiates all 3. run() chains them in order.",
      rubric: "3 agent classes. Orchestrator instantiates all. Pipeline: research→write→review. Output printed."
    }
  ]
},

"LLM Evaluation": {
  aiRubric: "Check evaluation metrics, test cases, automated scoring.",
  lessons: [
    {
      title: "Evaluating LLM Outputs",
      theory: "## LLM Evaluation Methods\n1. **Human evaluation** — experts rate quality\n2. **LLM-as-judge** — another LLM grades the output\n3. **Reference-based** — compare to gold standard\n4. **Task-specific** — code executes, SQL returns correct data\n\n**Metrics:**\n- Correctness (is it right?)\n- Relevance (does it answer the question?)\n- Conciseness (is it appropriately brief?)\n- Safety (no harmful content?)",
      instructions: "## Task: LLM Evaluator\nBuild an `LLMEvaluator` that:\n1. Takes question + expected_answer + llm_answer\n2. Uses LLM-as-judge to score 1-10\n3. Runs batch evaluation on 3 test cases\n4. Reports average score and flags poor responses (<6)",
      starterCode: "import requests, os, json\n\nAPI_KEY = os.getenv('GROQ_API_KEY', '')\n\ndef call_llm(prompt, system='You are a fair evaluator.'):\n    r = requests.post(\n        'https://api.groq.com/openai/v1/chat/completions',\n        headers={'Authorization': f'Bearer {API_KEY}'},\n        json={'model':'llama3-8b-8192','max_tokens':200,\n              'messages':[{'role':'system','content':system},{'role':'user','content':prompt}]}\n    )\n    return r.json()['choices'][0]['message']['content']\n\ndef evaluate_response(question, expected, actual):\n    prompt = f\"\"\"Score this AI answer 1-10. Respond with ONLY a JSON: {{\"score\": X, \"reason\": \"brief reason\"}}\n\nQuestion: {question}\nExpected: {expected}\nActual:   {actual}\"\"\"\n    response = call_llm(___)\n    try:\n        clean = response.strip().strip('`').replace('json','').strip()\n        result = json.loads(___)\n        return result.get('score', 5), result.get('reason', 'No reason')\n    except:\n        return 5, 'Could not parse score'\n\ntest_cases = [\n    {\n        'question':  'What is a Python list?',\n        'expected':  'An ordered, mutable collection of items',\n        'llm_answer': 'A list stores multiple items in order. Example: [1,2,3]'\n    },\n    {\n        'question':  'What is 2+2?',\n        'expected':  '4',\n        'llm_answer': 'The capital of France is Paris'\n    },\n    {\n        'question':  'How do you define a function in Python?',\n        'expected':  'Use the def keyword followed by function name and colon',\n        'llm_answer': 'def my_function(): pass'\n    }\n]\n\nscores = []\nfor case in test_cases:\n    score, reason = evaluate_response(case[___], case[___], case[___])\n    scores.append(score)\n    status = '✅' if score >= 6 else '❌'\n    print(f'{status} Score: {score}/10 | {reason[:60]}')\n\nprint(f'\\nAverage: {sum(scores)/len(scores):.1f}/10')\nprint(f'Poor responses: {len([s for s in scores if s < 6])}')",
      solution: "import requests,os,json\nAPI_KEY=os.getenv('GROQ_API_KEY','')\ndef call_llm(prompt,system='You are a fair evaluator.'):\n    r=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {API_KEY}'},json={'model':'llama3-8b-8192','max_tokens':200,'messages':[{'role':'system','content':system},{'role':'user','content':prompt}]})\n    return r.json()['choices'][0]['message']['content']\ndef evaluate_response(question,expected,actual):\n    prompt=f'Score 1-10. ONLY JSON: {{\"score\":X,\"reason\":\"brief\"}}\\nQ:{question}\\nExpected:{expected}\\nActual:{actual}'\n    response=call_llm(prompt)\n    try:\n        clean=response.strip().strip('`').replace('json','').strip()\n        result=json.loads(clean)\n        return result.get('score',5),result.get('reason','No reason')\n    except:\n        return 5,'Parse failed'\ntest_cases=[{'question':'What is a Python list?','expected':'An ordered mutable collection','llm_answer':'A list stores items in order: [1,2,3]'},{'question':'What is 2+2?','expected':'4','llm_answer':'The capital of France is Paris'},{'question':'How do you define a function?','expected':'Use def keyword','llm_answer':'def my_function(): pass'}]\nscores=[]\nfor case in test_cases:\n    score,reason=evaluate_response(case['question'],case['expected'],case['llm_answer'])\n    scores.append(score)\n    status='OK' if score>=6 else 'FAIL'\n    print(f'{status} Score:{score}/10 | {reason[:60]}')\nprint(f'\\nAverage:{sum(scores)/len(scores):.1f}/10')\nprint(f'Poor:{len([s for s in scores if s<6])}')",
      hint: "LLM-as-judge gets JSON back. json.loads() parses. Average = sum/len. Filter poor with < 6.",
      rubric: "evaluate_response prompts LLM. JSON parsed. 3 test cases run. Average and poor count."
    }
  ]
},

"Production AI Systems": {
  aiRubric: "Check caching, retry logic, rate limiting, monitoring.",
  lessons: [
    {
      title: "Production-Ready AI Client",
      theory: "## Production Concerns\n```python\n# 1. Caching — avoid paying for same prompt twice\n# 2. Retry with backoff — handle transient failures\n# 3. Rate limiting — respect API limits\n# 4. Logging — track usage and errors\n# 5. Fallbacks — use backup model if primary fails\n```",
      instructions: "## Task: Production LLM Client\nBuild `ProductionLLMClient` with:\n1. `lru_cache` for response caching\n2. Exponential backoff retry (3 attempts)\n3. Usage tracking (tokens, cost estimate)\n4. Fallback to cached response on failure\n5. Test with a real call",
      starterCode: "import requests, os, time, hashlib\nfrom functools import lru_cache\n\nAPI_KEY = os.getenv('GROQ_API_KEY', '')\n\nclass ProductionLLMClient:\n    def __init__(self, model='llama3-8b-8192', max_retries=3):\n        self.model = model\n        self.max_retries = max_retries\n        self.cache = {}\n        self.total_calls = 0\n        self.total_chars = 0\n\n    def _cache_key(self, prompt, system):\n        return hashlib.md5(f'{system}|{prompt}'.encode()).hexdigest()\n\n    def call(self, prompt, system='You are helpful.', use_cache=True):\n        key = self._cache_key(prompt, system)\n\n        if use_cache and key in self.cache:\n            print('  [CACHE HIT]')\n            return self.cache[___]\n\n        for attempt in range(self.max_retries):\n            try:\n                r = requests.post(\n                    'https://api.groq.com/openai/v1/chat/completions',\n                    headers={'Authorization': f'Bearer {API_KEY}'},\n                    json={'model':self.model,'max_tokens':300,\n                          'messages':[{'role':'system','content':system},\n                                      {'role':'user','content':prompt}]},\n                    timeout=30\n                )\n                r.raise_for_status()\n                reply = r.json()['choices'][0]['message']['content']\n\n                self.cache[key] = reply\n                self.total_calls += 1\n                self.total_chars += len(reply)\n                return reply\n\n            except Exception as e:\n                wait = 2 ** attempt\n                print(f'  [RETRY {attempt+1}] Failed: {e}. Waiting {wait}s...')\n                time.sleep(___)\n                if attempt == self.max_retries - 1:\n                    return self.cache.get(key, f'Error after {self.max_retries} retries')\n\n    def stats(self):\n        return {\n            'total_calls': self.total_calls,\n            'cached_responses': len(self.cache),\n            'total_chars': self.total_chars,\n            'est_cost_usd': self.total_chars * 0.000001\n        }\n\nclient = ProductionLLMClient()\n\nprint('Call 1:')\nresult1 = client.call('What is a Python list?')\nprint(result1[:100], '...')\n\nprint('\\nCall 2 (same — should be cached):')\nresult2 = client.call('What is a Python list?')\n\nprint('\\nStats:', client.stats())",
      solution: "import requests,os,time,hashlib\nAPI_KEY=os.getenv('GROQ_API_KEY','')\nclass ProductionLLMClient:\n    def __init__(self,model='llama3-8b-8192',max_retries=3):\n        self.model=model;self.max_retries=max_retries\n        self.cache={};self.total_calls=0;self.total_chars=0\n    def _cache_key(self,prompt,system):\n        return hashlib.md5(f'{system}|{prompt}'.encode()).hexdigest()\n    def call(self,prompt,system='You are helpful.',use_cache=True):\n        key=self._cache_key(prompt,system)\n        if use_cache and key in self.cache:\n            print('  [CACHE HIT]')\n            return self.cache[key]\n        for attempt in range(self.max_retries):\n            try:\n                r=requests.post('https://api.groq.com/openai/v1/chat/completions',headers={'Authorization':f'Bearer {API_KEY}'},json={'model':self.model,'max_tokens':300,'messages':[{'role':'system','content':system},{'role':'user','content':prompt}]},timeout=30)\n                r.raise_for_status()\n                reply=r.json()['choices'][0]['message']['content']\n                self.cache[key]=reply;self.total_calls+=1;self.total_chars+=len(reply)\n                return reply\n            except Exception as e:\n                wait=2**attempt\n                print(f'  [RETRY {attempt+1}] {e}. Wait {wait}s')\n                time.sleep(wait)\n                if attempt==self.max_retries-1:\n                    return self.cache.get(key,f'Error after {self.max_retries} retries')\n    def stats(self):\n        return{'total_calls':self.total_calls,'cached':len(self.cache),'chars':self.total_chars,'est_usd':self.total_chars*0.000001}\nclient=ProductionLLMClient()\nprint('Call 1:')\nresult1=client.call('What is a Python list?')\nprint(result1[:100],'...')\nprint('\\nCall 2 (cached):')\nresult2=client.call('What is a Python list?')\nprint('\\nStats:',client.stats())",
      hint: "MD5 hash as cache key. cache dict lookup. 2**attempt for exponential backoff. .cache.get() fallback.",
      rubric: "MD5 cache key. Cache hit check. Retry loop with 2**attempt. Usage tracked. stats() works."
    }
  ]
},

"AI Safety & Ethics": {
  aiRubric: "Check bias detection, output filtering, responsible AI practices.",
  lessons: [
    {
      title: "Responsible AI Development",
      theory: "## AI Safety Checklist\n1. **Bias** — does the model discriminate unfairly?\n2. **Hallucination** — does it make things up?\n3. **Privacy** — does it expose personal data?\n4. **Misuse** — can it be used to harm?\n5. **Transparency** — can users tell it's AI?\n\n**In Nigeria context:**\n- Models trained on English data may underperform on Pidgin\n- Facial recognition may have higher error rates for dark skin\n- Always test with diverse Nigerian user groups",
      instructions: "## Task: AI Safety Checker\nBuild a safety layer for AI responses:\n1. `check_hallucination(response, facts)` — flags if response contradicts known facts\n2. `check_bias(response)` — flags potentially biased language\n3. `filter_pii(text)` — removes emails, phone numbers\n4. `safety_wrap(prompt, response)` — runs all checks\n5. Test with sample responses",
      starterCode: "import re\n\nKNOWN_FACTS = {\n    'Nigeria capital': 'Abuja',\n    'Python creator': 'Guido van Rossum',\n    'FastAPI creator': 'Sebastián Ramírez'\n}\n\nBIAS_WORDS = ['always', 'never', 'all', 'none', 'every', 'typical', 'normal for']\n\ndef check_hallucination(response, facts=KNOWN_FACTS):\n    issues = []\n    for fact_key, fact_val in facts.items():\n        if fact_key.lower() in response.lower():\n            if fact_val.lower() not in response.lower():\n                issues.append(f'Possible error about: {fact_key}')\n    return issues\n\ndef check_bias(response):\n    found = [w for w in ___ if w in response.lower()]\n    return found\n\ndef filter_pii(text):\n    text = re.sub(r'[\\w.-]+@[\\w.-]+\\.\\w+', '[EMAIL]', ___)\n    text = re.sub(r'(\\+234|0)[0-9]{10}', '[PHONE]', text)\n    text = re.sub(r'\\b[0-9]{11}\\b', '[NIN]', ___)\n    return text\n\ndef safety_wrap(prompt, response):\n    report = {'prompt': prompt, 'original': response}\n    report['hallucination_flags'] = check_hallucination(___)\n    report['bias_flags']         = check_bias(___)\n    report['filtered_response'] = filter_pii(___)\n    report['safe'] = not report['hallucination_flags'] and not report['bias_flags']\n    return report\n\ntest_cases = [\n    ('What is the capital?', 'The capital of Nigeria is Lagos.'),\n    ('Tell me about students.', 'All Nigerian students always struggle with programming.'),\n    ('Contact info?', 'Email ada@example.com or call +2348012345678')\n]\n\nfor prompt, response in test_cases:\n    result = safety_wrap(prompt, response)\n    print(f'Q: {prompt}')\n    print(f'Safe: {result[\"safe\"]} | Flags: {result[\"hallucination_flags\"]+result[\"bias_flags\"]}')\n    print(f'Filtered: {result[\"filtered_response\"]}')\n    print()",
      solution: "import re\nKNOWN_FACTS={'Nigeria capital':'Abuja','Python creator':'Guido van Rossum','FastAPI creator':'Sebastián Ramírez'}\nBIAS_WORDS=['always','never','all','none','every','typical','normal for']\ndef check_hallucination(response,facts=KNOWN_FACTS):\n    issues=[]\n    for fact_key,fact_val in facts.items():\n        if fact_key.lower() in response.lower():\n            if fact_val.lower() not in response.lower():\n                issues.append(f'Possible error about:{fact_key}')\n    return issues\ndef check_bias(response):\n    return[w for w in BIAS_WORDS if w in response.lower()]\ndef filter_pii(text):\n    text=re.sub(r'[\\w.-]+@[\\w.-]+\\.\\w+','[EMAIL]',text)\n    text=re.sub(r'(\\+234|0)[0-9]{10}','[PHONE]',text)\n    text=re.sub(r'\\b[0-9]{11}\\b','[NIN]',text)\n    return text\ndef safety_wrap(prompt,response):\n    report={'prompt':prompt,'original':response}\n    report['hallucination_flags']=check_hallucination(response)\n    report['bias_flags']=check_bias(response)\n    report['filtered_response']=filter_pii(response)\n    report['safe']=not report['hallucination_flags'] and not report['bias_flags']\n    return report\ntest_cases=[('What is the capital?','The capital of Nigeria is Lagos.'),('Tell me about students.','All Nigerian students always struggle with programming.'),('Contact info?','Email ada@example.com or call +2348012345678')]\nfor prompt,response in test_cases:\n    result=safety_wrap(prompt,response)\n    print(f'Q:{prompt}')\n    print(f'Safe:{result[\"safe\"]} Flags:{result[\"hallucination_flags\"]+result[\"bias_flags\"]}')\n    print(f'Filtered:{result[\"filtered_response\"]}')\n    print()",
      hint: "BIAS_WORDS list comprehension. re.sub for PII. safety_wrap combines all checks.",
      rubric: "hallucination check. bias word detection. regex PII filter. safety_wrap combines. 3 test cases."
    }
  ]
},

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// FRONTEND — ALL MISSING
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Forms & Validation": {
  aiRubric: "Check form elements, validation logic, error messages.",
  lessons: [
    {
      title: "HTML Forms & JavaScript Validation",
      theory: "## Forms\n```html\n<form id='myForm'>\n  <input type='text' id='name' required>\n  <input type='email' id='email'>\n  <input type='number' min='0' max='100'>\n  <select id='course'>\n    <option value='python'>Python</option>\n  </select>\n  <button type='submit'>Submit</button>\n</form>\n```\n```javascript\ndocument.getElementById('myForm').addEventListener('submit', (e) => {\n  e.preventDefault();  // stop page reload\n  const name = document.getElementById('name').value;\n  if (!name) { alert('Name required!'); return; }\n});\n```",
      instructions: "## Task: Student Registration Form\nWrite HTML + JavaScript for a form that:\n1. Has fields: name, email, course (select), score (number 0-100)\n2. Validates: all required, email has @, score in range\n3. Shows inline error messages (not alert)\n4. On success, shows a summary of the registration",
      starterCode: "// Validation logic (JavaScript)\nfunction validateForm(name, email, course, score) {\n    const errors = {};\n\n    if (!___) errors.name = 'Name is required';\n    if (!email.includes(___)) errors.email = 'Invalid email address';\n    if (!course) errors.course = 'Please select a course';\n    if (score < ___ || score > ___) errors.score = 'Score must be 0-100';\n\n    return errors;\n}\n\nfunction submitForm() {\n    const name  = 'Ada Okonkwo';   // simulate input\n    const email = 'ada@test.com';\n    const course = 'python';\n    const score = 88;\n\n    const errors = validateForm(___, ___, ___, ___);\n\n    if (Object.keys(errors).length > 0) {\n        console.log('Validation errors:', errors);\n        return;\n    }\n\n    console.log('Registration successful!');\n    console.log(`Student: ${name} | Course: ${course} | Score: ${score}`);\n}\n\n// Test with valid data\nsubmitForm();\n\n// Test with invalid data\nconst errors = validateForm('', 'not-an-email', '', 150);\nconsole.log('Expected errors:', errors);",
      solution: "function validateForm(name,email,course,score){\n    const errors={};\n    if(!name)errors.name='Name is required';\n    if(!email.includes('@'))errors.email='Invalid email';\n    if(!course)errors.course='Please select a course';\n    if(score<0||score>100)errors.score='Score must be 0-100';\n    return errors;\n}\nfunction submitForm(){\n    const name='Ada Okonkwo',email='ada@test.com',course='python',score=88;\n    const errors=validateForm(name,email,course,score);\n    if(Object.keys(errors).length>0){console.log('Errors:',errors);return;}\n    console.log('Success!');\n    console.log(`${name}|${course}|${score}`);\n}\nsubmitForm();\nconst errors=validateForm('','not-an-email','',150);\nconsole.log('Expected errors:',errors);",
      hint: "!name for empty check. email.includes('@'). score<0||score>100. Object.keys(errors).length.",
      rubric: "4 validations. Error object built. Length check. Success and error paths tested."
    }
  ]
},

"Responsive Design Basics": {
  aiRubric: "Check media queries, mobile-first, flexbox/grid for responsive layout.",
  lessons: [
    {
      title: "Mobile-First Responsive CSS",
      theory: "## Responsive Design\n```css\n/* Mobile first — base styles for small screens */\n.card { width: 100%; padding: 16px; }\n\n/* Tablet (768px+) */\n@media (min-width: 768px) {\n  .card { width: 50%; }\n}\n\n/* Desktop (1024px+) */\n@media (min-width: 1024px) {\n  .card { width: 33.333%; }\n}\n\n/* Grid layout */\n.grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));\n  gap: 20px;\n}\n```",
      instructions: "## Task: Responsive Card Grid\nWrite CSS for a course card grid that:\n1. 1 column on mobile\n2. 2 columns on tablet (768px+)\n3. 3 columns on desktop (1024px+)\n4. Cards have padding, shadow, rounded corners\n5. Navigation bar stacks vertically on mobile",
      starterCode: "/* Mobile First — base styles */\n* { box-sizing: border-box; margin: 0; padding: 0; }\nbody { font-family: sans-serif; background: #f5f5f5; }\n\n/* Navbar — stacks on mobile */\n.navbar {\n    display: flex;\n    flex-direction: ___; /* column on mobile */\n    background: #1e1e1e;\n    padding: 16px;\n    gap: 12px;\n}\n\n/* Card grid — 1 col on mobile */\n.grid {\n    display: ___;\n    grid-template-columns: ___; /* 1 col */\n    gap: 16px;\n    padding: 20px;\n}\n\n.card {\n    background: white;\n    border-radius: ___;\n    padding: 20px;\n    box-shadow: 0 2px 8px rgba(0,0,0,0.1);\n}\n\n/* Tablet */\n@media (min-width: ___) {\n    .navbar { flex-direction: ___; }\n    .grid { grid-template-columns: ___ ___ ; }\n}\n\n/* Desktop */\n@media (min-width: 1024px) {\n    .grid { grid-template-columns: ___ ___ ___; }\n}",
      solution: "*{box-sizing:border-box;margin:0;padding:0}\nbody{font-family:sans-serif;background:#f5f5f5}\n.navbar{display:flex;flex-direction:column;background:#1e1e1e;padding:16px;gap:12px}\n.grid{display:grid;grid-template-columns:1fr;gap:16px;padding:20px}\n.card{background:white;border-radius:8px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,0.1)}\n@media(min-width:768px){.navbar{flex-direction:row}.grid{grid-template-columns:1fr 1fr}}\n@media(min-width:1024px){.grid{grid-template-columns:1fr 1fr 1fr}}",
      hint: "column for mobile, row for tablet. 1fr is one column unit. @media(min-width:768px).",
      rubric: "Mobile: column nav, 1-col grid. Tablet: row nav, 2-col. Desktop: 3-col. card styles present."
    }
  ]
},

"Fetch API & AJAX": {
  aiRubric: "Check fetch usage, async/await, .then(), error handling, JSON parsing.",
  lessons: [
    {
      title: "Fetch API & Async JS",
      theory: "## Fetch API\n```javascript\n// With async/await\nasync function getUser(id) {\n  try {\n    const res = await fetch(`/api/users/${id}`);\n    if (!res.ok) throw new Error(`HTTP ${res.status}`);\n    const data = await res.json();\n    return data;\n  } catch (err) {\n    console.error('Fetch failed:', err);\n  }\n}\n\n// POST request\nconst res = await fetch('/api/students', {\n  method: 'POST',\n  headers: {'Content-Type': 'application/json'},\n  body: JSON.stringify({name: 'Ada', score: 88})\n});\n```",
      instructions: "## Task: Student API Client (JS)\nWrite async JavaScript functions:\n1. `fetchStudents()` — GET all students from JSONPlaceholder /users\n2. `fetchStudent(id)` — GET one user\n3. `createStudent(data)` — POST to /posts\n4. Handle errors properly\n5. Print results",
      starterCode: "const BASE_URL = 'https://jsonplaceholder.typicode.com';\n\nasync function fetchStudents() {\n    const res = await ___(f`${BASE_URL}/users`);\n    if (!res.ok) throw new Error(`Error: ${res.status}`);\n    return await res.___();\n}\n\nasync function fetchStudent(id) {\n    try {\n        const res = await fetch(`${BASE_URL}/users/${___}`);\n        if (!res.___) throw new Error(`Student ${id} not found`);\n        return await res.json();\n    } catch (err) {\n        console.error(err.message);\n        return null;\n    }\n}\n\nasync function createStudent(data) {\n    const res = await fetch(`${BASE_URL}/posts`, {\n        method: ___,\n        headers: {'Content-Type': 'application/json'},\n        body: JSON.stringify(___)\n    });\n    return await res.___();\n}\n\nasync function main() {\n    const students = await fetchStudents();\n    console.log(`Fetched ${students.length} students`);\n    console.log('First:', students[0].name, students[0].email);\n\n    const one = await fetchStudent(1);\n    console.log('User 1:', one?.name);\n\n    const created = await createStudent({name:'Ada',course:'Python',score:88});\n    console.log('Created:', created);\n}\n\nmain();",
      solution: "const BASE_URL='https://jsonplaceholder.typicode.com';\nasync function fetchStudents(){\n    const res=await fetch(`${BASE_URL}/users`);\n    if(!res.ok)throw new Error(`Error:${res.status}`);\n    return await res.json();\n}\nasync function fetchStudent(id){\n    try{\n        const res=await fetch(`${BASE_URL}/users/${id}`);\n        if(!res.ok)throw new Error(`Not found:${id}`);\n        return await res.json();\n    }catch(err){console.error(err.message);return null;}\n}\nasync function createStudent(data){\n    const res=await fetch(`${BASE_URL}/posts`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});\n    return await res.json();\n}\nasync function main(){\n    const students=await fetchStudents();\n    console.log(`Fetched ${students.length}`);\n    console.log('First:',students[0].name,students[0].email);\n    const one=await fetchStudent(1);\n    console.log('User 1:',one?.name);\n    const created=await createStudent({name:'Ada',course:'Python',score:88});\n    console.log('Created:',created);\n}\nmain();",
      hint: "await fetch(url). res.ok checks status. res.json() parses. POST needs method, headers, body.",
      rubric: "fetch with await. res.ok check. json() called. POST with headers and JSON.stringify."
    }
  ]
},

"ES6+ Modern JS": {
  aiRubric: "Check destructuring, spread, arrow functions, template literals, modules.",
  lessons: [
    {
      title: "Modern JavaScript Features",
      theory: "## ES6+ Features\n```javascript\n// Destructuring\nconst {name, score} = student;\nconst [first, ...rest] = array;\n\n// Spread operator\nconst merged = {...obj1, ...obj2};\nconst combined = [...arr1, ...arr2];\n\n// Optional chaining\nconst city = user?.address?.city;\n\n// Nullish coalescing\nconst name = user.name ?? 'Anonymous';\n\n// Template literals\nconst msg = `Hello ${name}, your score is ${score}`;\n\n// Async/await (ES2017)\nconst data = await fetchData();\n```",
      instructions: "## Task: Modern JS Toolkit\n1. Destructure a student object\n2. Merge two objects with spread\n3. Use optional chaining on nested object\n4. Map an array using arrow functions and destructuring\n5. Use nullish coalescing for defaults",
      starterCode: "// 1. Destructuring\nconst student = {name:'Ada', score:88, course:'Python', city:'Lagos'};\nconst {___, ___, ...rest} = student;\nconsole.log(name, score);\nconsole.log('Rest:', rest);\n\n// 2. Spread merge\nconst base = {role:'student', active:true};\nconst extra = {name:'Ada', score:88};\nconst merged = {...___, ...___};\nconsole.log('Merged:', merged);\n\n// 3. Optional chaining\nconst user = {profile: {address: {city:'Lagos'}}};\nconst missingUser = null;\nconst city1 = user?.profile?.address?.___;\nconst city2 = missingUser?.___.___; // no error!\nconsole.log(city1, city2); // Lagos undefined\n\n// 4. Array destructuring in map\nconst pairs = [['Ada',88], ['Tunde',72], ['Ngozi',95]];\nconst formatted = pairs.map(([___, ___]) => `${name}: ${score >= 80 ? 'A' : 'B'}`);\nconsole.log(formatted);\n\n// 5. Nullish coalescing\nconst settings = {theme: null, lang: 'en'};\nconst theme = settings.theme ?? ___;\nconst lang  = settings.lang  ?? 'en';\nconsole.log(theme, lang);",
      solution: "const student={name:'Ada',score:88,course:'Python',city:'Lagos'};\nconst{name,score,...rest}=student;\nconsole.log(name,score);\nconsole.log('Rest:',rest);\nconst base={role:'student',active:true};\nconst extra={name:'Ada',score:88};\nconst merged={...base,...extra};\nconsole.log('Merged:',merged);\nconst user={profile:{address:{city:'Lagos'}}};\nconst missingUser=null;\nconst city1=user?.profile?.address?.city;\nconst city2=missingUser?.profile?.city;\nconsole.log(city1,city2);\nconst pairs=[['Ada',88],['Tunde',72],['Ngozi',95]];\nconst formatted=pairs.map(([name,score])=>`${name}:${score>=80?'A':'B'}`);\nconsole.log(formatted);\nconst settings={theme:null,lang:'en'};\nconst theme=settings.theme??'dark';\nconst lang=settings.lang??'en';\nconsole.log(theme,lang);",
      hint: "Destructure with {}. Spread: {...obj1,...obj2}. ?. for optional chain. ?? for nullish default.",
      rubric: "Object destructure with rest. Spread merge. Optional chaining. Array destructure in map. ??."
    }
  ]
},

"CSS Animations": {
  aiRubric: "Check @keyframes, transition, animation properties.",
  lessons: [
    {
      title: "CSS Transitions & Animations",
      theory: "## CSS Animations\n```css\n/* Transitions — smooth property changes */\n.btn { transition: background 0.3s ease, transform 0.2s; }\n.btn:hover { background: #00e5a0; transform: translateY(-2px); }\n\n/* Keyframe animations */\n@keyframes fadeIn {\n  from { opacity: 0; transform: translateY(20px); }\n  to   { opacity: 1; transform: translateY(0); }\n}\n\n.card { animation: fadeIn 0.5s ease forwards; }\n\n/* Pulse animation */\n@keyframes pulse {\n  0%, 100% { opacity: 1; }\n  50%       { opacity: 0.4; }\n}\n```",
      instructions: "## Task: Animated UI Components\nWrite CSS for:\n1. Button with hover transition (color + scale)\n2. Card with fadeIn animation on load\n3. Loading spinner with rotate animation\n4. Pulse effect for a status dot\n5. Slide-in from left animation",
      starterCode: "/* 1. Button hover transition */\n.btn {\n    padding: 10px 20px;\n    background: #007acc;\n    color: white;\n    border: none;\n    border-radius: 6px;\n    cursor: pointer;\n    transition: background ___ ease, transform ___;\n}\n.btn:hover {\n    background: #005999;\n    transform: ___(-2px);\n}\n\n/* 2. FadeIn keyframe */\n@___ fadeIn {\n    from { opacity: 0; transform: translateY(20px); }\n    to   { opacity: 1; transform: translateY(0); }\n}\n.card { animation: fadeIn ___ ease forwards; }\n\n/* 3. Spinner */\n@keyframes spin {\n    from { transform: rotate(0deg); }\n    to   { transform: rotate(___); }\n}\n.spinner {\n    width: 32px; height: 32px;\n    border: 3px solid #eee;\n    border-top-color: #007acc;\n    border-radius: 50%;\n    animation: spin ___ linear ___;\n}\n\n/* 4. Pulse */\n@keyframes pulse {\n    0%, 100% { opacity: 1; }\n    50% { opacity: ___; }\n}\n.status-dot { animation: pulse 2s infinite; }\n\n/* 5. Slide in */\n@keyframes slideIn {\n    from { transform: translateX(___); opacity: 0; }\n    to   { transform: translateX(0); opacity: 1; }\n}\n.slide { animation: slideIn 0.4s ease; }",
      solution: ".btn{padding:10px 20px;background:#007acc;color:white;border:none;border-radius:6px;cursor:pointer;transition:background 0.3s ease,transform 0.2s;}\n.btn:hover{background:#005999;transform:translateY(-2px);}\n@keyframes fadeIn{from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}\n.card{animation:fadeIn 0.5s ease forwards;}\n@keyframes spin{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}\n.spinner{width:32px;height:32px;border:3px solid #eee;border-top-color:#007acc;border-radius:50%;animation:spin 1s linear infinite;}\n@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.4;}}\n.status-dot{animation:pulse 2s infinite;}\n@keyframes slideIn{from{transform:translateX(-100px);opacity:0;}to{transform:translateX(0);opacity:1;}}\n.slide{animation:slideIn 0.4s ease;}",
      hint: "transition: property duration easing. @keyframes name { from { } to { } }. animation: name duration easing iteration.",
      rubric: "transition on button. fadeIn @keyframes. spin 360deg infinite. pulse opacity. slideIn from left."
    }
  ]
},

"LocalStorage & State": {
  aiRubric: "Check localStorage get/set/remove, JSON serialization, state management.",
  lessons: [
    {
      title: "Browser Storage & State",
      theory: "## localStorage\n```javascript\n// Store\nlocalStorage.setItem('user', JSON.stringify({name:'Ada'}));\n\n// Retrieve\nconst user = JSON.parse(localStorage.getItem('user'));\n\n// Remove\nlocalStorage.removeItem('user');\n\n// Clear all\nlocalStorage.clear();\n\n// Check exists\nconst exists = localStorage.getItem('user') !== null;\n```\n\n**Note:** localStorage stores strings only — always use JSON.stringify/parse for objects.",
      instructions: "## Task: Student Progress Tracker\nWrite JavaScript that:\n1. Saves student name and progress to localStorage\n2. Loads it on page start (persists across refreshes)\n3. Updates progress when a lesson is completed\n4. Shows total XP and completed lessons\n5. Has a reset function",
      starterCode: "const STORAGE_KEY = 'mabel_student_v1';\n\nfunction loadProgress() {\n    const raw = localStorage.getItem(___);\n    if (!raw) return {name:'Student', xp:0, completed:[]};\n    return JSON.___(raw);\n}\n\nfunction saveProgress(data) {\n    localStorage.setItem(___, JSON.___(data));\n}\n\nfunction completeLesson(lessonId, xpReward=50) {\n    const progress = loadProgress();\n    if (!progress.completed.includes(___)) {\n        progress.completed.push(lessonId);\n        progress.xp += ___;\n        saveProgress(___);\n        console.log(`Completed ${lessonId}! +${xpReward} XP. Total: ${progress.xp}`);\n    } else {\n        console.log(`${lessonId} already completed.`);\n    }\n}\n\nfunction showStats() {\n    const p = loadProgress();\n    console.log(`Student: ${p.___}`);\n    console.log(`XP:      ${p.___}`);\n    console.log(`Lessons: ${p.___.length}`);\n    console.log(`Done:    ${p.completed.join(', ')}`);\n}\n\nfunction reset() {\n    localStorage.___(STORAGE_KEY);\n    console.log('Progress reset!');\n}\n\n// Test\ncompleteLesson('python-001');\ncompleteLesson('python-002', 75);\ncompleteLesson('python-001');  // duplicate\nshowStats();",
      solution: "const STORAGE_KEY='mabel_student_v1';\nfunction loadProgress(){\n    const raw=localStorage.getItem(STORAGE_KEY);\n    if(!raw)return{name:'Student',xp:0,completed:[]};\n    return JSON.parse(raw);\n}\nfunction saveProgress(data){\n    localStorage.setItem(STORAGE_KEY,JSON.stringify(data));\n}\nfunction completeLesson(lessonId,xpReward=50){\n    const progress=loadProgress();\n    if(!progress.completed.includes(lessonId)){\n        progress.completed.push(lessonId);\n        progress.xp+=xpReward;\n        saveProgress(progress);\n        console.log(`Completed ${lessonId}! +${xpReward} XP. Total:${progress.xp}`);\n    }else{console.log(`${lessonId} already done.`);}\n}\nfunction showStats(){\n    const p=loadProgress();\n    console.log(`Student:${p.name}`);\n    console.log(`XP:${p.xp}`);\n    console.log(`Lessons:${p.completed.length}`);\n    console.log(`Done:${p.completed.join(', ')}`);\n}\nfunction reset(){\n    localStorage.removeItem(STORAGE_KEY);\n    console.log('Reset!');\n}\ncompleteLesson('python-001');\ncompleteLesson('python-002',75);\ncompleteLesson('python-001');\nshowStats();",
      hint: "JSON.stringify to save objects. JSON.parse to load. includes() checks duplicates. removeItem to reset.",
      rubric: "JSON.stringify/parse. includes() duplicate check. xp += reward. removeItem. showStats prints all."
    }
  ]
},

"React Fundamentals": {
  aiRubric: "Check React components, props, useState, JSX syntax.",
  lessons: [
    {
      title: "React Components & Props",
      theory: "## React Basics\n```jsx\n// Functional component\nfunction StudentCard({ name, score }) {\n  return (\n    <div className='card'>\n      <h2>{name}</h2>\n      <p>Score: {score}</p>\n    </div>\n  );\n}\n\n// Usage\n<StudentCard name='Ada' score={88} />\n\n// useState hook\nconst [count, setCount] = useState(0);\n// Update: setCount(count + 1);\n```",
      instructions: "## Task: Student Dashboard Component\nWrite React-style component logic in Python (since we can't render JSX here):\n1. Define component props (name, score, course, xp)\n2. Compute derived state: grade, level badge\n3. Simulate rendering by returning a dict\n4. Create a list of 3 student card components",
      starterCode: "# Simulating React component logic in Python\n\ndef StudentCard(name, score, course, xp=0):\n    # Derived state\n    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'\n    level = 'Expert' if xp >= 1000 else 'Intermediate' if xp >= 500 else ___\n    badge_color = '#00e5a0' if grade in ['A','B'] else ___\n\n    # Simulated JSX render\n    return {\n        'component': 'StudentCard',\n        'props': {'name':name,'score':score,'course':course,'xp':xp},\n        'state': {'grade':grade,'level':___,'badge_color':___},\n        'html': f'<div class=\"card\"><h2>{name}</h2><p>{course} | Grade:{grade}</p><span style=\"color:{badge_color}\">{___}</span></div>'\n    }\n\n# List rendering (like .map() in React)\nstudents_data = [\n    ('Ada',   88, 'Python',  750),\n    ('Tunde', 72, 'SQL',     200),\n    ('Ngozi', 95, 'FastAPI', 1200)\n]\n\ncomponents = [StudentCard(n, s, c, x) for n, s, c, x in ___]\n\nfor comp in components:\n    print(comp['html'])\n    print(f'  State: grade={comp[\"state\"][\"grade\"]}, level={comp[\"state\"][\"level\"]}')\n    print()",
      solution: "def StudentCard(name,score,course,xp=0):\n    grade='A' if score>=90 else 'B' if score>=80 else 'C' if score>=70 else 'F'\n    level='Expert' if xp>=1000 else 'Intermediate' if xp>=500 else 'Beginner'\n    badge_color='#00e5a0' if grade in['A','B'] else '#ef4444'\n    return{'component':'StudentCard','props':{'name':name,'score':score,'course':course,'xp':xp},'state':{'grade':grade,'level':level,'badge_color':badge_color},'html':f'<div class=\"card\"><h2>{name}</h2><p>{course}|Grade:{grade}</p><span style=\"color:{badge_color}\">{level}</span></div>'}\nstudents_data=[('Ada',88,'Python',750),('Tunde',72,'SQL',200),('Ngozi',95,'FastAPI',1200)]\ncomponents=[StudentCard(n,s,c,x) for n,s,c,x in students_data]\nfor comp in components:\n    print(comp['html'])\n    print(f'  State:grade={comp[\"state\"][\"grade\"]},level={comp[\"state\"][\"level\"]}')\n    print()",
      hint: "Ternary for grade/level. List comprehension for components. Access dict keys for state.",
      rubric: "StudentCard returns dict. grade and level computed. badge_color set. List of 3 components."
    }
  ]
},

"React Hooks & Context": {
  aiRubric: "Check useState, useEffect, useContext patterns.",
  lessons: [
    {
      title: "React Hooks Pattern",
      theory: "## React Hooks\n```jsx\n// useState — local state\nconst [students, setStudents] = useState([]);\n\n// useEffect — side effects (fetch, subscribe)\nuseEffect(() => {\n  fetchStudents().then(data => setStudents(data));\n}, []);  // [] = run once on mount\n\n// useContext — global state\nconst theme = useContext(ThemeContext);\n\n// Custom hook\nfunction useLocalStorage(key, initial) {\n  const [value, setValue] = useState(\n    () => JSON.parse(localStorage.getItem(key)) ?? initial\n  );\n  // ...\n  return [value, setValue];\n}\n```",
      instructions: "## Task: Simulate React Hooks\nSimulate React hook behaviour in Python:\n1. `useState` — returns value and setter\n2. `useEffect` — runs callback with cleanup\n3. `useReducer` — state + dispatch pattern\n4. A simple student list reducer",
      starterCode: "# Simulating React hooks in Python\n\ndef useState(initial):\n    state = [initial]  # list allows mutation in closure\n    def setState(new_val):\n        state[0] = new_val if not callable(new_val) else new_val(state[0])\n    return state, setState\n\ndef useEffect(callback, deps=None):\n    # In React, this runs after render\n    # Here we simulate by calling immediately\n    cleanup = ___()\n    return cleanup\n\ndef useReducer(reducer, initial_state):\n    state = [initial_state]\n    def dispatch(action):\n        state[0] = reducer(state[0], ___)\n    return state, dispatch\n\n# Student list reducer\ndef studentsReducer(state, action):\n    if action['type'] == 'ADD':\n        return state + [action[___]]\n    elif action['type'] == ___:\n        return [s for s in state if s['id'] != action['id']]\n    elif action['type'] == 'UPDATE_SCORE':\n        return [{**s, 'score': action['score']} if s['id'] == action['id'] else s\n                for s in state]\n    return state\n\n# Test\nstudent_state, dispatch = useReducer(studentsReducer, [])\n\ndispatch({'type':'ADD','student':{'id':1,'name':'Ada','score':88}})\ndispatch({'type':'ADD','student':{'id':2,'name':'Tunde','score':72}})\nprint('After adds:', student_state[0])\n\ndispatch({'type':'UPDATE_SCORE','id':1,'score':95})\nprint('After update:', student_state[0])\n\ndispatch({'type':'DELETE','id':2})\nprint('After delete:', student_state[0])",
      solution: "def useState(initial):\n    state=[initial]\n    def setState(new_val):\n        state[0]=new_val if not callable(new_val) else new_val(state[0])\n    return state,setState\ndef useEffect(callback,deps=None):\n    cleanup=callback()\n    return cleanup\ndef useReducer(reducer,initial_state):\n    state=[initial_state]\n    def dispatch(action):\n        state[0]=reducer(state[0],action)\n    return state,dispatch\ndef studentsReducer(state,action):\n    if action['type']=='ADD':\n        return state+[action['student']]\n    elif action['type']=='DELETE':\n        return[s for s in state if s['id']!=action['id']]\n    elif action['type']=='UPDATE_SCORE':\n        return[{**s,'score':action['score']} if s['id']==action['id'] else s for s in state]\n    return state\nstudent_state,dispatch=useReducer(studentsReducer,[])\ndispatch({'type':'ADD','student':{'id':1,'name':'Ada','score':88}})\ndispatch({'type':'ADD','student':{'id':2,'name':'Tunde','score':72}})\nprint('After adds:',student_state[0])\ndispatch({'type':'UPDATE_SCORE','id':1,'score':95})\nprint('After update:',student_state[0])\ndispatch({'type':'DELETE','id':2})\nprint('After delete:',student_state[0])",
      hint: "state[0]=reducer(state[0],action). ADD appends. DELETE filters. UPDATE_SCORE maps with spread.",
      rubric: "useReducer calls reducer. 3 action types handled. ADD/DELETE/UPDATE_SCORE all work."
    }
  ]
},

"Database Design Patterns": {
  aiRubric: "Check normalization, foreign keys, indexes, relationships.",
  lessons: [
    {
      title: "Normalization & Schema Design",
      theory: "## Database Normalization\n**1NF** — no repeating groups, atomic values\n**2NF** — no partial dependencies\n**3NF** — no transitive dependencies\n\n```sql\n-- Unnormalized (BAD)\nCREATE TABLE orders (\n    id INT,\n    customer_name TEXT,\n    customer_email TEXT,  -- repeated every order!\n    items TEXT  -- comma-separated, not atomic!\n);\n\n-- Normalized (GOOD)\nCREATE TABLE customers (id INT PRIMARY KEY, name TEXT, email TEXT UNIQUE);\nCREATE TABLE orders (id INT PRIMARY KEY, customer_id INT REFERENCES customers(id));\nCREATE TABLE order_items (order_id INT, product_id INT, quantity INT);\n```",
      instructions: "## Task: Design a School Schema\nDesign normalized tables for Mabel Academy:\n1. `students` (id, name, email, enrolled_at)\n2. `courses` (id, title, level, instructor_id)\n3. `instructors` (id, name, email, specialty)\n4. `enrolments` (student_id, course_id, enrolled_at, grade) — many-to-many\n5. Write the CREATE TABLE statements with proper foreign keys",
      starterCode: "-- Instructors (no foreign keys — parent table)\nCREATE TABLE instructors (\n    id         ___ PRIMARY KEY,\n    name       VARCHAR(100) NOT NULL,\n    email      VARCHAR(120) ___ NOT NULL,\n    specialty  VARCHAR(50)\n);\n\n-- Students\nCREATE TABLE students (\n    id          INTEGER PRIMARY KEY AUTOINCREMENT,\n    name        VARCHAR(100) NOT NULL,\n    email       VARCHAR(120) UNIQUE NOT NULL,\n    enrolled_at DATETIME DEFAULT ___\n);\n\n-- Courses (references instructors)\nCREATE TABLE courses (\n    id            INTEGER PRIMARY KEY AUTOINCREMENT,\n    title         VARCHAR(200) NOT NULL,\n    level         VARCHAR(20) CHECK (level IN (___)),\n    instructor_id INTEGER REFERENCES ___(id) ON DELETE SET NULL\n);\n\n-- Enrolments (many-to-many junction)\nCREATE TABLE enrolments (\n    student_id  INTEGER REFERENCES ___(id) ON DELETE CASCADE,\n    course_id   INTEGER REFERENCES ___(id) ON DELETE CASCADE,\n    enrolled_at DATETIME DEFAULT CURRENT_TIMESTAMP,\n    grade       VARCHAR(2),\n    PRIMARY KEY (student_id, ___)\n);",
      solution: "CREATE TABLE instructors(id INTEGER PRIMARY KEY,name VARCHAR(100) NOT NULL,email VARCHAR(120) UNIQUE NOT NULL,specialty VARCHAR(50));\nCREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100) NOT NULL,email VARCHAR(120) UNIQUE NOT NULL,enrolled_at DATETIME DEFAULT CURRENT_TIMESTAMP);\nCREATE TABLE courses(id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(200) NOT NULL,level VARCHAR(20) CHECK(level IN('Beginner','Intermediate','Advanced')),instructor_id INTEGER REFERENCES instructors(id) ON DELETE SET NULL);\nCREATE TABLE enrolments(student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,course_id INTEGER REFERENCES courses(id) ON DELETE CASCADE,enrolled_at DATETIME DEFAULT CURRENT_TIMESTAMP,grade VARCHAR(2),PRIMARY KEY(student_id,course_id));",
      hint: "UNIQUE on email. CHECK for level values. REFERENCES table(id). CASCADE deletes related rows. Composite PK.",
      rubric: "4 tables. UNIQUE on emails. CHECK constraint. REFERENCES with ON DELETE. Composite PK in enrolments."
    }
  ]
},

"Sharding & Replication": {
  aiRubric: "Check concepts of horizontal scaling, read replicas, sharding strategies.",
  lessons: [
    {
      title: "Scaling Databases",
      theory: "## Scaling Strategies\n**Vertical** — bigger server (limited)\n**Horizontal** — more servers\n\n**Replication:**\n- Primary → writes\n- Replicas → reads\n- Increases read capacity\n\n**Sharding:**\n- Split data across multiple DBs\n- Each shard holds a subset\n- Shard by: user_id range, geography, hash\n\n**Example:**\n- Shard 0: users 1-1M\n- Shard 1: users 1M-2M\n- Shard 2: users 2M-3M",
      instructions: "## Task: Simulate a Sharding Router\n1. Write `get_shard(user_id, num_shards=3)` — hash-based routing\n2. Write `ShardRouter` class that routes queries to correct shard\n3. Simulate inserting 10 users and show shard distribution\n4. Show how to query a specific user",
      starterCode: "import hashlib\n\ndef get_shard(user_id, num_shards=3):\n    # Hash-based sharding: consistent distribution\n    hash_val = int(hashlib.md5(str(user_id).encode()).hexdigest(), 16)\n    return hash_val % ___\n\nclass ShardRouter:\n    def __init__(self, num_shards=3):\n        self.num_shards = num_shards\n        self.shards = {i: {} for i in range(num_shards)}  # shard_id -> {user_id: data}\n\n    def insert(self, user_id, data):\n        shard = get_shard(user_id, self.___)\n        self.shards[shard][user_id] = data\n        return shard\n\n    def find(self, user_id):\n        shard = get_shard(user_id, self.num_shards)\n        return self.shards[shard].get(___, None)\n\n    def stats(self):\n        for i, shard in self.shards.items():\n            print(f'  Shard {i}: {len(shard)} users — {list(shard.keys())}')\n\nrouter = ShardRouter(num_shards=3)\n\nusers = [(1,'Ada','Python'),(2,'Tunde','SQL'),(3,'Ngozi','FastAPI'),\n         (4,'Emeka','React'),(5,'Amaka','AI'),(6,'Bola','Django'),\n         (7,'Kemi','Flask'),(8,'Seun','Docker'),(9,'Tobi','Redis'),(10,'Femi','Mongo')]\n\nfor uid, name, course in users:\n    shard = router.insert(uid, {'name':name,'course':course})\n    print(f'User {uid} ({name}) -> Shard {shard}')\n\nprint('\\nShard distribution:')\nrouter.stats()\n\nprint('\\nFind user 5:', router.find(5))\nprint('Find user 99:', router.find(99))",
      solution: "import hashlib\ndef get_shard(user_id,num_shards=3):\n    hash_val=int(hashlib.md5(str(user_id).encode()).hexdigest(),16)\n    return hash_val%num_shards\nclass ShardRouter:\n    def __init__(self,num_shards=3):\n        self.num_shards=num_shards\n        self.shards={i:{} for i in range(num_shards)}\n    def insert(self,user_id,data):\n        shard=get_shard(user_id,self.num_shards)\n        self.shards[shard][user_id]=data\n        return shard\n    def find(self,user_id):\n        shard=get_shard(user_id,self.num_shards)\n        return self.shards[shard].get(user_id,None)\n    def stats(self):\n        for i,shard in self.shards.items():\n            print(f'  Shard {i}:{len(shard)} users-{list(shard.keys())}')\nrouter=ShardRouter(num_shards=3)\nusers=[(1,'Ada','Python'),(2,'Tunde','SQL'),(3,'Ngozi','FastAPI'),(4,'Emeka','React'),(5,'Amaka','AI'),(6,'Bola','Django'),(7,'Kemi','Flask'),(8,'Seun','Docker'),(9,'Tobi','Redis'),(10,'Femi','Mongo')]\nfor uid,name,course in users:\n    shard=router.insert(uid,{'name':name,'course':course})\n    print(f'User {uid}({name})->Shard {shard}')\nprint('\\nDistribution:')\nrouter.stats()\nprint('\\nFind 5:',router.find(5))\nprint('Find 99:',router.find(99))",
      hint: "hash_val % num_shards routes to shard. find uses same hash to locate correct shard.",
      rubric: "hash-based shard function. ShardRouter inserts to correct shard. find routes correctly. stats shown."
    }
  ]
},

// Frontend Advanced (remaining)

"Performance Optimization": {
  aiRubric: "Check lazy loading, debounce, memoization, bundle concepts.",
  lessons: [
    {
      title: "Frontend Performance",
      theory: "## Performance Techniques\n```javascript\n// Debounce — wait until user stops typing\nfunction debounce(fn, delay) {\n  let timer;\n  return function(...args) {\n    clearTimeout(timer);\n    timer = setTimeout(() => fn(...args), delay);\n  };\n}\n\n// Memoize — cache expensive results\nfunction memoize(fn) {\n  const cache = {};\n  return function(key) {\n    if (cache[key] !== undefined) return cache[key];\n    return (cache[key] = fn(key));\n  };\n}\n\n// Lazy load images\n<img src='placeholder.jpg' data-src='real.jpg' loading='lazy'>\n```",
      instructions: "## Task: Performance Utilities\n1. `debounce(fn, delay)` — prevents rapid function calls\n2. `throttle(fn, interval)` — limits calls to once per interval\n3. `memoize(fn)` — caches results for same inputs\n4. Test debounce with search simulation\n5. Test memoize with expensive computation",
      starterCode: "function debounce(fn, delay) {\n    let timer;\n    return function(...args) {\n        clearTimeout(___);\n        timer = setTimeout(() => fn(...args), ___);\n    };\n}\n\nfunction throttle(fn, interval) {\n    let lastCall = 0;\n    return function(...args) {\n        const now = Date.now();\n        if (now - lastCall >= ___) {\n            lastCall = now;\n            return fn(...args);\n        }\n    };\n}\n\nfunction memoize(fn) {\n    const cache = {};\n    return function(...args) {\n        const key = JSON.stringify(args);\n        if (key in ___) return cache[key];\n        return (cache[___] = fn(...args));\n    };\n}\n\n// Test debounce\nconst search = debounce((query) => console.log('Searching:', query), 300);\nsearch('p'); search('py'); search('pyt'); search('pyth');\nsetTimeout(() => search('python'), 400);  // only this fires\n\n// Test memoize\nlet callCount = 0;\nconst expensive = memoize((n) => {\n    callCount++;\n    return n * n;\n});\n\nconsole.log(expensive(5));   // computes\nconsole.log(expensive(5));   // cached\nconsole.log(expensive(10));  // computes\nconsole.log('Total calls:', callCount);  // should be 2",
      solution: "function debounce(fn,delay){\n    let timer;\n    return function(...args){\n        clearTimeout(timer);\n        timer=setTimeout(()=>fn(...args),delay);\n    };\n}\nfunction throttle(fn,interval){\n    let lastCall=0;\n    return function(...args){\n        const now=Date.now();\n        if(now-lastCall>=interval){\n            lastCall=now;\n            return fn(...args);\n        }\n    };\n}\nfunction memoize(fn){\n    const cache={};\n    return function(...args){\n        const key=JSON.stringify(args);\n        if(key in cache)return cache[key];\n        return(cache[key]=fn(...args));\n    };\n}\nconst search=debounce((q)=>console.log('Searching:',q),300);\nsearch('p');search('py');search('pyt');search('pyth');\nsetTimeout(()=>search('python'),400);\nlet callCount=0;\nconst expensive=memoize((n)=>{callCount++;return n*n;});\nconsole.log(expensive(5));\nconsole.log(expensive(5));\nconsole.log(expensive(10));\nconsole.log('Calls:',callCount);",
      hint: "clearTimeout(timer) cancels previous. JSON.stringify(args) as cache key. Date.now() for throttle.",
      rubric: "debounce clears and resets timer. throttle checks interval. memoize uses JSON key. callCount=2."
    }
  ]
},

"Testing Frontend Code": {
  aiRubric: "Check test function structure, assertions, test runner pattern.",
  lessons: [
    {
      title: "Unit Testing JavaScript",
      theory: "## Testing Pattern\n```javascript\n// Minimal test runner\nfunction test(name, fn) {\n  try {\n    fn();\n    console.log(`✅ ${name}`);\n  } catch(err) {\n    console.log(`❌ ${name}: ${err.message}`);\n  }\n}\n\nfunction expect(received) {\n  return {\n    toBe: (expected) => {\n      if (received !== expected)\n        throw new Error(`Expected ${expected}, got ${received}`);\n    }\n  };\n}\n\ntest('adds numbers', () => {\n  expect(add(2, 3)).toBe(5);\n});\n```",
      instructions: "## Task: Test Suite for Utilities\nBuild a mini test framework and test your utility functions:\n1. `test(name, fn)` runner with pass/fail count\n2. `expect(val)` with `toBe`, `toEqual`, `toBeTruthy`, `toContain`\n3. Write 5 tests for: add, getGrade, filterPassingStudents\n4. Show summary: X passed, Y failed",
      starterCode: "let passed = 0, failed = 0;\n\nfunction test(name, fn) {\n    try {\n        fn();\n        ___ ++;\n        console.log(`OK ${name}`);\n    } catch(err) {\n        ___++;\n        console.log(`FAIL ${name}: ${err.message}`);\n    }\n}\n\nfunction expect(received) {\n    return {\n        toBe(expected) {\n            if (received !== expected)\n                throw new Error(`Expected ${JSON.stringify(expected)}, got ${JSON.stringify(received)}`);\n        },\n        toEqual(expected) {\n            if (JSON.stringify(received) !== JSON.stringify(___)) \n                throw new Error(`Objects not equal`);\n        },\n        toBeTruthy() {\n            if (!received) throw new Error(`Expected truthy, got ${received}`);\n        },\n        toContain(item) {\n            if (!received.___(item)) throw new Error(`Expected to contain ${item}`);\n        }\n    };\n}\n\n// Functions to test\nconst add = (a, b) => a + b;\nconst getGrade = s => s>=90?'A':s>=80?'B':s>=70?'C':'F';\nconst filterPassing = students => students.filter(s => s.score >= 60);\n\n// Tests\ntest('add(2,3) equals 5', () => expect(add(2,3)).toBe(5));\ntest('add(0,0) equals 0', () => expect(add(0,0)).toBe(___));\ntest('score 95 gets grade A', () => expect(getGrade(95)).toBe(___));\ntest('score 55 gets grade F', () => expect(getGrade(55)).toBe(___));\ntest('filters passing students', () => {\n    const students = [{name:'Ada',score:88},{name:'Tunde',score:45}];\n    const result = filterPassing(students);\n    expect(result.length).toBe(___);\n    expect(result[0].name).toBe('Ada');\n});\n\nconsole.log(`\\nResults: ${passed} passed, ${failed} failed`);",
      solution: "let passed=0,failed=0;\nfunction test(name,fn){\n    try{fn();passed++;console.log(`OK ${name}`);}\n    catch(err){failed++;console.log(`FAIL ${name}:${err.message}`);}\n}\nfunction expect(received){\n    return{\n        toBe(expected){if(received!==expected)throw new Error(`Expected ${JSON.stringify(expected)},got ${JSON.stringify(received)}`);},\n        toEqual(expected){if(JSON.stringify(received)!==JSON.stringify(expected))throw new Error('Not equal');},\n        toBeTruthy(){if(!received)throw new Error(`Expected truthy,got ${received}`);},\n        toContain(item){if(!received.includes(item))throw new Error(`Expected to contain ${item}`);}\n    };\n}\nconst add=(a,b)=>a+b;\nconst getGrade=s=>s>=90?'A':s>=80?'B':s>=70?'C':'F';\nconst filterPassing=students=>students.filter(s=>s.score>=60);\ntest('add(2,3)=5',()=>expect(add(2,3)).toBe(5));\ntest('add(0,0)=0',()=>expect(add(0,0)).toBe(0));\ntest('95->A',()=>expect(getGrade(95)).toBe('A'));\ntest('55->F',()=>expect(getGrade(55)).toBe('F'));\ntest('filter passing',()=>{\n    const students=[{name:'Ada',score:88},{name:'Tunde',score:45}];\n    const result=filterPassing(students);\n    expect(result.length).toBe(1);\n    expect(result[0].name).toBe('Ada');\n});\nconsole.log(`\\n${passed} passed,${failed} failed`);",
      hint: "passed++ on success, failed++ on catch. toBe uses ===. toEqual uses JSON.stringify comparison.",
      rubric: "test runner with try/catch. 4 matchers. 5 tests. Pass/fail count shown."
    }
  ]
},

"Build Tools & Webpack": {
  aiRubric: "Check module system, bundler concepts, npm scripts.",
  lessons: [
    {
      title: "Modern Build Pipeline",
      theory: "## Build Tools\n```bash\n# Initialize project\nnpm init -y\nnpm install --save-dev webpack webpack-cli\nnpm install react react-dom\n\n# package.json scripts\n\"scripts\": {\n  \"build\": \"webpack --mode production\",\n  \"dev\":   \"webpack serve --mode development\",\n  \"test\":  \"jest\"\n}\n```\n\n**Webpack** bundles all JS files into one.\n**Vite** is faster — modern alternative.\n**npm** manages packages and scripts.",
      instructions: "## Task: Project Setup Simulation\nWrite Python code that generates a complete project structure:\n1. `package.json` with dependencies and scripts\n2. `webpack.config.js` content\n3. `.gitignore` file\n4. `src/index.js` entry point\n5. Print all files that would be created",
      starterCode: "import json\n\nfiles = {}\n\n# 1. package.json\nfiles['package.json'] = json.dumps({\n    'name': 'mabel-academy',\n    'version': '1.0.0',\n    'scripts': {\n        'build': ___,\n        'dev':   'webpack serve --mode development --open',\n        'test':  ___\n    },\n    'dependencies': {\n        'react': '^18.0.0',\n        'react-dom': '^18.0.0'\n    },\n    'devDependencies': {\n        'webpack': '^5.0.0',\n        'webpack-cli': ___,\n        'webpack-dev-server': '^4.0.0',\n        'babel-loader': '^9.0.0',\n        '@babel/core': '^7.0.0',\n        '@babel/preset-react': ___\n    }\n}, indent=2)\n\n# 2. webpack.config.js\nfiles['webpack.config.js'] = '''\nconst path = require('path');\nmodule.exports = {\n  entry: './src/index.js',\n  output: { path: path.resolve(__dirname, 'dist'), filename: 'bundle.js' },\n  module: { rules: [{ test: /\\.jsx?$/, use: 'babel-loader' }] }\n};\n'''\n\n# 3. .gitignore\nfiles['.gitignore'] = 'node_modules/\\ndist/\\n.env\\n*.log'\n\n# 4. src/index.js\nfiles['src/index.js'] = '''\nimport React from 'react';\nimport ReactDOM from 'react-dom/client';\n\nconst root = ReactDOM.createRoot(document.getElementById('root'));\nroot.render(<h1>Mabel Academy</h1>);\n'''\n\nfor filename, content in files.items():\n    print(f'=== {filename} ===')\n    print(content[:200])\n    print()",
      solution: "import json\nfiles={}\nfiles['package.json']=json.dumps({'name':'mabel-academy','version':'1.0.0','scripts':{'build':'webpack --mode production','dev':'webpack serve --mode development --open','test':'jest'},'dependencies':{'react':'^18.0.0','react-dom':'^18.0.0'},'devDependencies':{'webpack':'^5.0.0','webpack-cli':'^5.0.0','webpack-dev-server':'^4.0.0','babel-loader':'^9.0.0','@babel/core':'^7.0.0','@babel/preset-react':'^7.0.0'}},indent=2)\nfiles['webpack.config.js']=\"const path=require('path');module.exports={entry:'./src/index.js',output:{path:path.resolve(__dirname,'dist'),filename:'bundle.js'},module:{rules:[{test:/\\.jsx?$/,use:'babel-loader'}]}};\"\nfiles['.gitignore']='node_modules/\\ndist/\\n.env\\n*.log'\nfiles['src/index.js']=\"import React from 'react';import ReactDOM from 'react-dom/client';const root=ReactDOM.createRoot(document.getElementById('root'));root.render(<h1>Mabel Academy</h1>);\"\nfor filename,content in files.items():\n    print(f'==={filename}===')\n    print(content[:200])\n    print()",
      hint: "'webpack --mode production' for build. 'jest' for test. Version strings like '^5.0.0'.",
      rubric: "package.json with 4 scripts. webpack.config.js generated. .gitignore correct. 4 files printed."
    }
  ]
}



"Stored Procedures": {
  aiRubric: "Check parameterized queries, transactions, reusable query functions.",
  lessons: [
    {
      title: "Stored Procedures in Python",
      theory: "## Stored Procedures\nPre-compiled SQL logic stored in the database:\n```sql\nCREATE OR REPLACE FUNCTION get_top_students(min_score INT)\nRETURNS TABLE(name TEXT, score INT) AS $$\n  SELECT name, score FROM students\n  WHERE score >= min_score\n  ORDER BY score DESC;\n$$ LANGUAGE SQL;\n\nSELECT * FROM get_top_students(80);\n```\nBenefits: reusable, faster (pre-compiled), reduces network traffic.",
      instructions: "## Task: Procedure-style Functions\nSimulate stored procedures using Python + SQLite:\n1. `get_top_students(conn, min_score)` — parameterized query function\n2. `calculate_grade(score)` — scalar function (A/B/C/F)\n3. `update_student_score(conn, student_id, new_score)` — transactional update\n4. Test all three",
      starterCode: "import sqlite3\n\nconn = sqlite3.connect(':memory:')\nconn.row_factory = sqlite3.Row\ncursor = conn.cursor()\ncursor.executescript(\"\"\"\n    CREATE TABLE students(id INT, name TEXT, score INT, course TEXT);\n    INSERT INTO students VALUES(1,'Ada',88,'Python');\n    INSERT INTO students VALUES(2,'Tunde',55,'SQL');\n    INSERT INTO students VALUES(3,'Ngozi',95,'FastAPI');\n    INSERT INTO students VALUES(4,'Emeka',72,'Python');\n\"\"\")\n\ndef get_top_students(conn, min_score):\n    return conn.execute(\n        'SELECT name,score FROM students WHERE score>=? ORDER BY score DESC',\n        (___,)\n    ).fetchall()\n\ndef calculate_grade(score):\n    if score >= 90: return 'A'\n    elif score >= 80: return ___\n    elif score >= 70: return 'C'\n    else: return ___\n\ndef update_student_score(conn, student_id, new_score):\n    try:\n        conn.execute('BEGIN')\n        conn.execute('UPDATE students SET score=? WHERE id=?', (___, ___))\n        conn.commit()\n        return True\n    except Exception as e:\n        conn.rollback()\n        return False\n\nprint('Top students (>=80):')\nfor row in get_top_students(conn, ___):\n    print(f'  {row[\"name\"]}: {row[\"score\"]} ({calculate_grade(row[\"score\"])})')\n\nprint('Update result:', update_student_score(conn, 2, 85))\nprint('After update:')\nfor row in get_top_students(conn, 60):\n    print(f'  {row[\"name\"]}: {row[\"score\"]}')",
      solution: "import sqlite3\nconn=sqlite3.connect(':memory:')\nconn.row_factory=sqlite3.Row\ncursor=conn.cursor()\ncursor.executescript(\"CREATE TABLE students(id INT,name TEXT,score INT,course TEXT);INSERT INTO students VALUES(1,'Ada',88,'Python');INSERT INTO students VALUES(2,'Tunde',55,'SQL');INSERT INTO students VALUES(3,'Ngozi',95,'FastAPI');INSERT INTO students VALUES(4,'Emeka',72,'Python');\")\ndef get_top_students(conn,min_score):\n    return conn.execute('SELECT name,score FROM students WHERE score>=? ORDER BY score DESC',(min_score,)).fetchall()\ndef calculate_grade(score):\n    if score>=90:return 'A'\n    elif score>=80:return 'B'\n    elif score>=70:return 'C'\n    else:return 'F'\ndef update_student_score(conn,student_id,new_score):\n    try:\n        conn.execute('BEGIN')\n        conn.execute('UPDATE students SET score=? WHERE id=?',(new_score,student_id))\n        conn.commit()\n        return True\n    except Exception as e:\n        conn.rollback()\n        return False\nprint('Top>=80:')\nfor row in get_top_students(conn,80):\n    print(f'  {row[\"name\"]}:{row[\"score\"]}({calculate_grade(row[\"score\"])})')\nprint('Update:',update_student_score(conn,2,85))\nprint('After:')\nfor row in get_top_students(conn,60):\n    print(f'  {row[\"name\"]}:{row[\"score\"]}')",
      hint: "Pass min_score as tuple (min_score,). calculate_grade if/elif. BEGIN/COMMIT/ROLLBACK for transaction.",
      rubric: "parameterized query with ?. calculate_grade B and F correct. transaction with rollback."
    }
  ]
},


}; // end courseManifest