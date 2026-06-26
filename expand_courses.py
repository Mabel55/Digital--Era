"""
Expand Digital Era Courses — Add 3 new lessons to every course.
This script reads courses.js, finds each course's lessons array,
and injects 3 brand new interactive coding lessons.
"""
import json, re, os

# ══════════════════════════════════════════════════════
# NEW LESSONS FOR EVERY COURSE  (3 per course)
# ══════════════════════════════════════════════════════

NEW_LESSONS = {

# ─── PYTHON CORE: BEGINNER ───
"Python Fundamentals": [
  {
    "title": "String Formatting & f-Strings",
    "theory": "## f-Strings (Python 3.6+)\nf-Strings let you embed expressions directly inside strings.\n```python\nname = 'Ada'\nage = 25\nprint(f'Hello {name}, you are {age} years old!')\nprint(f'Next year you will be {age + 1}')\nprint(f'{name:>10}')  # Right-align in 10 chars\nprint(f'{3.14159:.2f}')  # 2 decimal places\n```",
    "instructions": "## Task: Student Report Card\n1. Create variables: `student = 'Mabel'`, `score = 87.5`, `grade = 'A'`\n2. Use an f-string to print: `'Student: Mabel | Score: 87.50 | Grade: A'`\n3. The score must show exactly 2 decimal places",
    "starterCode": "student = '___'\nscore = ___\ngrade = '___'\n\nreport = f'Student: {___} | Score: {___:.___} | Grade: {___}'\nprint(report)",
    "solution": "student='Mabel'\nscore=87.5\ngrade='A'\nreport=f'Student: {student} | Score: {score:.2f} | Grade: {grade}'\nprint(report)",
    "hint": "Use :.2f inside the f-string to format to 2 decimal places.",
    "rubric": "Variables assigned. f-string with :.2f formatting. Output matches expected format."
  },
  {
    "title": "Type Conversion & Input",
    "theory": "## Type Conversion\nPython has built-in functions to convert between types.\n```python\n# String to Integer\nage = int('25')  # 25\n\n# String to Float\nprice = float('19.99')  # 19.99\n\n# Number to String\ntext = str(100)  # '100'\n\n# Check type\nprint(type(age))  # <class 'int'>\n\n# Boolean conversion\nbool(0)    # False\nbool(42)   # True\nbool('')   # False\nbool('hi') # True\n```",
    "instructions": "## Task: Type Converter\n1. Convert the string `'42'` to an integer and store in `num`\n2. Convert the string `'3.14'` to a float and store in `pi`\n3. Add them together and store in `total`\n4. Convert `total` to a string and store in `result`\n5. Print the type of `result`",
    "starterCode": "num = ___(___)\npi = ___(___)\ntotal = ___ + ___\nresult = ___(total)\nprint(type(result))",
    "solution": "num=int('42')\npi=float('3.14')\ntotal=num+pi\nresult=str(total)\nprint(type(result))",
    "hint": "int() converts to integer, float() to decimal, str() to string.",
    "rubric": "int('42') conversion. float('3.14') conversion. Addition correct. str() conversion. type() printed."
  },
  {
    "title": "Basic Math Operations & Operators",
    "theory": "## Python Math Operators\n```python\na, b = 17, 5\nprint(a + b)   # 22  Addition\nprint(a - b)   # 12  Subtraction\nprint(a * b)   # 85  Multiplication\nprint(a / b)   # 3.4 Division (float)\nprint(a // b)  # 3   Floor division\nprint(a % b)   # 2   Modulus (remainder)\nprint(a ** b)  # 1419857  Exponent\n\nimport math\nprint(math.sqrt(144))  # 12.0\nprint(abs(-10))        # 10\nprint(round(3.7))      # 4\n```",
    "instructions": "## Task: Calculator\n1. Given `a = 25` and `b = 7`\n2. Calculate floor division and store in `floor_div`\n3. Calculate the remainder and store in `remainder`\n4. Calculate `a` raised to the power of 3 and store in `cube`\n5. Print all three results",
    "starterCode": "a = 25\nb = 7\n\nfloor_div = a ___ b\nremainder = a ___ b\ncube = a ___ 3\n\nprint(f'Floor: {floor_div}, Remainder: {remainder}, Cube: {cube}')",
    "solution": "a=25\nb=7\nfloor_div=a//b\nremainder=a%b\ncube=a**3\nprint(f'Floor: {floor_div}, Remainder: {remainder}, Cube: {cube}')",
    "hint": "// for floor division, % for remainder, ** for power.",
    "rubric": "Floor division with //. Modulus with %. Exponent with **. All printed."
  }
],

"Control Flow & Loops": [
  {
    "title": "Nested Loops & Patterns",
    "theory": "## Nested Loops\nA loop inside another loop. The inner loop completes fully for each iteration of the outer.\n```python\nfor i in range(3):\n    for j in range(3):\n        print(f'({i},{j})', end=' ')\n    print()  # New line\n# (0,0) (0,1) (0,2)\n# (1,0) (1,1) (1,2)\n# (2,0) (2,1) (2,2)\n```",
    "instructions": "## Task: Multiplication Table\n1. Use nested loops to print a 5x5 multiplication table\n2. Format each number to be right-aligned in 4 characters\n3. Print a header row with column numbers",
    "starterCode": "# Print header\nprint('    ', end='')\nfor col in range(1, ___):\n    print(f'{col:4}', end='')\nprint()\nprint('-' * ___)\n\n# Print rows\nfor row in range(1, ___):\n    print(f'{row:3} |', end='')\n    for col in range(1, ___):\n        print(f'{row * ___:4}', end='')\n    print()",
    "solution": "print('    ',end='')\nfor col in range(1,6):print(f'{col:4}',end='')\nprint()\nprint('-'*24)\nfor row in range(1,6):\n    print(f'{row:3} |',end='')\n    for col in range(1,6):print(f'{row*col:4}',end='')\n    print()",
    "hint": "range(1, 6) gives 1-5. Use f'{value:4}' for alignment.",
    "rubric": "Nested loops for rows and columns. Multiplication computed. Formatted output with alignment."
  },
  {
    "title": "While Loops & Break/Continue",
    "theory": "## While Loops\n```python\n# Count up\ncount = 0\nwhile count < 5:\n    print(count)\n    count += 1\n\n# Break exits the loop\nfor i in range(100):\n    if i == 5:\n        break  # Stop!\n\n# Continue skips current iteration\nfor i in range(10):\n    if i % 2 == 0:\n        continue  # Skip even numbers\n    print(i)  # Only prints odd\n```",
    "instructions": "## Task: Number Guessing Logic\n1. Create a list of guesses: `[10, 25, 42, 50, 42]`\n2. The secret number is `42`\n3. Loop through guesses with a while loop\n4. Print 'Too low' or 'Too high' for wrong guesses\n5. When found, print 'Correct!' and `break`\n6. Track the number of attempts",
    "starterCode": "guesses = [10, 25, 42, 50, 42]\nsecret = 42\nattempts = 0\ni = 0\n\nwhile i < len(___):\n    guess = guesses[___]\n    attempts += 1\n    if guess < secret:\n        print(f'Guess {guess}: Too low')\n    elif guess > ___:\n        print(f'Guess {guess}: Too high')\n    else:\n        print(f'Guess {guess}: Correct in {___} attempts!')\n        ___\n    i += 1",
    "solution": "guesses=[10,25,42,50,42]\nsecret=42\nattempts=0\ni=0\nwhile i<len(guesses):\n    guess=guesses[i]\n    attempts+=1\n    if guess<secret:print(f'Guess {guess}: Too low')\n    elif guess>secret:print(f'Guess {guess}: Too high')\n    else:\n        print(f'Guess {guess}: Correct in {attempts} attempts!')\n        break\n    i+=1",
    "hint": "Use while i < len(guesses). Break when guess equals secret.",
    "rubric": "While loop iterates guesses. Comparison logic correct. Break on match. Attempts tracked."
  },
  {
    "title": "Enumerate & Range Tricks",
    "theory": "## enumerate() & range()\n```python\n# enumerate gives index + value\nfruits = ['apple', 'banana', 'cherry']\nfor i, fruit in enumerate(fruits):\n    print(f'{i}: {fruit}')\n\n# Start from 1\nfor i, fruit in enumerate(fruits, start=1):\n    print(f'{i}. {fruit}')\n\n# range() tricks\nrange(5)        # 0,1,2,3,4\nrange(2, 8)     # 2,3,4,5,6,7\nrange(0, 10, 2) # 0,2,4,6,8 (step=2)\nrange(10, 0, -1)# 10,9,...,1 (countdown)\n```",
    "instructions": "## Task: Leaderboard\n1. Given a list of `players` with scores\n2. Sort them by score (highest first)\n3. Use `enumerate(start=1)` to print ranked leaderboard\n4. Print only the top 3",
    "starterCode": "players = [\n    ('Ada', 850), ('Tunde', 920),\n    ('Ngozi', 780), ('Kemi', 990), ('Bayo', 860)\n]\n\n# Sort by score descending\nplayers.sort(key=lambda p: p[___], reverse=___)\n\nprint('=== LEADERBOARD ===')\nfor rank, (name, score) in enumerate(___, start=___):\n    medal = ['Gold','Silver','Bronze'][rank-1] if rank <= ___ else ''\n    print(f'{rank}. {name:10} {score} pts  {medal}')\n    if rank == 3:\n        ___",
    "solution": "players=[('Ada',850),('Tunde',920),('Ngozi',780),('Kemi',990),('Bayo',860)]\nplayers.sort(key=lambda p:p[1],reverse=True)\nprint('=== LEADERBOARD ===')\nfor rank,(name,score) in enumerate(players,start=1):\n    medal=['Gold','Silver','Bronze'][rank-1] if rank<=3 else ''\n    print(f'{rank}. {name:10} {score} pts  {medal}')\n    if rank==3:break",
    "hint": "sort with key=lambda p: p[1]. enumerate(players, start=1). Break at rank 3.",
    "rubric": "Sorted descending by score. enumerate with start=1. Top 3 with medals. Break at 3."
  }
],

"Functions & Scope": [
  {
    "title": "Default Arguments & Keyword Args",
    "theory": "## Default & Keyword Arguments\n```python\ndef greet(name, greeting='Hello', punctuation='!'):\n    return f'{greeting}, {name}{punctuation}'\n\ngreet('Ada')                    # 'Hello, Ada!'\ngreet('Ada', 'Hi')              # 'Hi, Ada!'\ngreet('Ada', punctuation='.')   # 'Hello, Ada.'\n\n# *args = variable positional args\ndef add_all(*nums):\n    return sum(nums)\nadd_all(1, 2, 3, 4)  # 10\n\n# **kwargs = variable keyword args\ndef info(**data):\n    for k, v in data.items():\n        print(f'{k}: {v}')\ninfo(name='Ada', age=25)\n```",
    "instructions": "## Task: Flexible Student Creator\n1. Create `create_student(name, level='Beginner', track='Python Core', **extras)`\n2. Return a dict with name, level, track, and any extras\n3. Test with 3 students using different argument styles",
    "starterCode": "def create_student(name, level=___, track=___, **extras):\n    student = {\n        'name': name,\n        'level': ___,\n        'track': ___,\n    }\n    student.update(___)\n    return student\n\ns1 = create_student('Ada')\ns2 = create_student('Tunde', level='Intermediate')\ns3 = create_student('Ngozi', 'Advanced', 'AI', goal='Research', gpa=3.9)\n\nfor s in [s1, s2, s3]:\n    print(s)",
    "solution": "def create_student(name,level='Beginner',track='Python Core',**extras):\n    student={'name':name,'level':level,'track':track}\n    student.update(extras)\n    return student\ns1=create_student('Ada')\ns2=create_student('Tunde',level='Intermediate')\ns3=create_student('Ngozi','Advanced','AI',goal='Research',gpa=3.9)\nfor s in [s1,s2,s3]:print(s)",
    "hint": "Default params in def signature. **extras captures extra keyword args. student.update(extras) merges them.",
    "rubric": "Default arguments set. **kwargs captured. update() merges extras. 3 test cases with different styles."
  },
  {
    "title": "Lambda Functions & map/filter",
    "theory": "## Lambda, map, filter\n```python\n# Lambda = anonymous one-liner function\nsquare = lambda x: x ** 2\nprint(square(5))  # 25\n\n# map applies a function to every item\nnums = [1, 2, 3, 4]\nsquared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]\n\n# filter keeps items where function returns True\nevens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]\n\n# sorted with key\nnames = ['Zara', 'Ada', 'Mabel']\nsorted(names, key=lambda n: len(n))  # ['Ada', 'Zara', 'Mabel']\n```",
    "instructions": "## Task: Student Data Pipeline\n1. Given a list of student dicts with name and score\n2. Use `filter` to get students with score >= 70\n3. Use `map` to add a 'grade' field based on score\n4. Use `sorted` with lambda to sort by score descending\n5. Print the results",
    "starterCode": "students = [\n    {'name': 'Ada', 'score': 92},\n    {'name': 'Tunde', 'score': 55},\n    {'name': 'Ngozi', 'score': 78},\n    {'name': 'Kemi', 'score': 45},\n    {'name': 'Bayo', 'score': 88},\n]\n\n# Filter passing students (score >= 70)\npassing = list(filter(lambda s: s['score'] >= ___, students))\n\n# Map to add grade\ndef add_grade(s):\n    score = s['score']\n    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'\n    return {**s, 'grade': ___}\n\ngraded = list(map(___, passing))\n\n# Sort by score descending\nresult = sorted(graded, key=lambda s: s[___], reverse=___)\n\nfor s in result:\n    print(f\"{s['name']:10} {s['score']}  Grade: {s['grade']}\")",
    "solution": "students=[{'name':'Ada','score':92},{'name':'Tunde','score':55},{'name':'Ngozi','score':78},{'name':'Kemi','score':45},{'name':'Bayo','score':88}]\npassing=list(filter(lambda s:s['score']>=70,students))\ndef add_grade(s):\n    score=s['score']\n    grade='A' if score>=90 else 'B' if score>=80 else 'C' if score>=70 else 'F'\n    return{**s,'grade':grade}\ngraded=list(map(add_grade,passing))\nresult=sorted(graded,key=lambda s:s['score'],reverse=True)\nfor s in result:print(f\"{s['name']:10} {s['score']}  Grade: {s['grade']}\")",
    "hint": "filter(lambda, list). map(function, list). sorted(list, key=lambda, reverse=True).",
    "rubric": "filter with >= 70. map with add_grade. sorted descending by score. Output formatted."
  },
  {
    "title": "Recursion Basics",
    "theory": "## Recursion\nA function that calls itself. Every recursive function needs a base case to stop.\n```python\ndef factorial(n):\n    if n <= 1:        # Base case\n        return 1\n    return n * factorial(n - 1)  # Recursive case\n\nfactorial(5)  # 5 * 4 * 3 * 2 * 1 = 120\n\ndef countdown(n):\n    if n <= 0:\n        print('Go!')\n        return\n    print(n)\n    countdown(n - 1)\n```",
    "instructions": "## Task: Recursive Sum\n1. Write `recursive_sum(n)` that returns the sum of all numbers from 1 to n\n2. Base case: if n <= 0, return 0\n3. Recursive case: return n + recursive_sum(n-1)\n4. Test with n = 10 (should return 55)",
    "starterCode": "def recursive_sum(n):\n    if n <= ___:\n        return ___\n    return ___ + recursive_sum(___)\n\nresult = recursive_sum(10)\nprint(f'Sum of 1-10: {result}')\nassert result == 55, 'Should be 55!'",
    "solution": "def recursive_sum(n):\n    if n<=0:return 0\n    return n+recursive_sum(n-1)\nresult=recursive_sum(10)\nprint(f'Sum of 1-10: {result}')\nassert result==55,'Should be 55!'",
    "hint": "Base case: n <= 0 returns 0. Recursive: n + recursive_sum(n-1).",
    "rubric": "Base case returns 0. Recursive call with n-1. Returns sum. Assert passes."
  }
],

"Lists & Tuples": [
  {
    "title": "List Slicing Mastery",
    "theory": "## Slicing\n```python\nnums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nnums[2:5]     # [2, 3, 4]\nnums[:3]      # [0, 1, 2]\nnums[7:]      # [7, 8, 9]\nnums[::2]     # [0, 2, 4, 6, 8]  (every 2nd)\nnums[::-1]    # [9, 8, 7, ...] (reversed)\nnums[1:8:3]   # [1, 4, 7] (start:stop:step)\n\n# Slice assignment\nnums[2:4] = [20, 30]  # Replace items\n```",
    "instructions": "## Task: Slice Operations\n1. Given `data = list(range(1, 21))`\n2. Get the first 5 elements\n3. Get the last 3 elements\n4. Get every 3rd element\n5. Reverse the entire list\n6. Get elements from index 5 to 15 with step 2",
    "starterCode": "data = list(range(1, 21))\n\nfirst_five = data[:___]\nlast_three = data[___:]\nevery_third = data[::___]\nreversed_list = data[::___]\nmiddle_skip = data[___:___:___]\n\nprint(f'First 5: {first_five}')\nprint(f'Last 3: {last_three}')\nprint(f'Every 3rd: {every_third}')\nprint(f'Reversed: {reversed_list}')\nprint(f'Middle skip: {middle_skip}')",
    "solution": "data=list(range(1,21))\nfirst_five=data[:5]\nlast_three=data[-3:]\nevery_third=data[::3]\nreversed_list=data[::-1]\nmiddle_skip=data[5:15:2]\nprint(f'First 5: {first_five}')\nprint(f'Last 3: {last_three}')\nprint(f'Every 3rd: {every_third}')\nprint(f'Reversed: {reversed_list}')\nprint(f'Middle skip: {middle_skip}')",
    "hint": "[:5] for first 5. [-3:] for last 3. [::3] every 3rd. [::-1] reversed. [5:15:2] middle with step.",
    "rubric": "All 5 slicing operations correct. Negative indexing for last 3. Step parameter used."
  },
  {
    "title": "Tuple Unpacking & Named Tuples",
    "theory": "## Tuple Unpacking\n```python\n# Basic unpacking\ncoords = (10, 20)\nx, y = coords\n\n# Swap variables\na, b = b, a\n\n# Star unpacking\nfirst, *middle, last = [1, 2, 3, 4, 5]\n# first=1, middle=[2,3,4], last=5\n\n# Named tuples\nfrom collections import namedtuple\nPoint = namedtuple('Point', ['x', 'y'])\np = Point(10, 20)\nprint(p.x, p.y)\n```",
    "instructions": "## Task: Student Records\n1. Create a namedtuple `Student` with fields: name, email, score\n2. Create 3 students\n3. Use unpacking to extract the top scorer\n4. Use star unpacking to separate first and rest",
    "starterCode": "from collections import namedtuple\n\nStudent = namedtuple('Student', [___, ___, ___])\n\nstudents = [\n    Student('Ada', 'ada@mail.com', 92),\n    Student('Tunde', 'tunde@mail.com', 88),\n    Student('Ngozi', 'ngozi@mail.com', 95),\n]\n\n# Sort by score descending\nstudents.sort(key=lambda s: s.___, reverse=True)\n\n# Star unpacking\ntop, *rest = ___\n\nprint(f'Top student: {top.name} ({top.score})')\nprint(f'Others: {[s.name for s in rest]}')",
    "solution": "from collections import namedtuple\nStudent=namedtuple('Student',['name','email','score'])\nstudents=[Student('Ada','ada@mail.com',92),Student('Tunde','tunde@mail.com',88),Student('Ngozi','ngozi@mail.com',95)]\nstudents.sort(key=lambda s:s.score,reverse=True)\ntop,*rest=students\nprint(f'Top student: {top.name} ({top.score})')\nprint(f'Others: {[s.name for s in rest]}')",
    "hint": "namedtuple('Student', ['name', 'email', 'score']). Sort by s.score. top, *rest = students.",
    "rubric": "namedtuple created. 3 students instantiated. Sorted by score. Star unpacking used."
  },
  {
    "title": "Zip & List Combining",
    "theory": "## zip()\nCombines multiple iterables element-by-element.\n```python\nnames = ['Ada', 'Tunde', 'Ngozi']\nscores = [92, 88, 95]\n\n# Zip together\npairs = list(zip(names, scores))\n# [('Ada', 92), ('Tunde', 88), ('Ngozi', 95)]\n\n# Unzip\nnames2, scores2 = zip(*pairs)\n\n# Zip with enumerate\nfor i, (name, score) in enumerate(zip(names, scores), 1):\n    print(f'{i}. {name}: {score}')\n\n# dict from zip\ngrade_map = dict(zip(names, scores))\n```",
    "instructions": "## Task: Grade Report\n1. Given parallel lists of names, scores, and courses\n2. Use `zip` to combine them\n3. Create a dict mapping names to scores\n4. Find the average score using the zipped data",
    "starterCode": "names = ['Ada', 'Tunde', 'Ngozi', 'Kemi']\nscores = [92, 78, 88, 95]\ncourses = ['Python', 'SQL', 'FastAPI', 'AI']\n\n# Zip all three together\ncombined = list(zip(___, ___, ___))\n\n# Print report\nfor name, score, course in ___:\n    status = 'PASS' if score >= 70 else 'FAIL'\n    print(f'{name:10} {course:10} {score}  [{status}]')\n\n# Create name->score dict\ngrade_map = dict(zip(___, ___))\n\n# Average\navg = sum(___) / len(scores)\nprint(f'\\nAverage: {avg:.1f}')",
    "solution": "names=['Ada','Tunde','Ngozi','Kemi']\nscores=[92,78,88,95]\ncourses=['Python','SQL','FastAPI','AI']\ncombined=list(zip(names,scores,courses))\nfor name,score,course in combined:\n    status='PASS' if score>=70 else 'FAIL'\n    print(f'{name:10} {course:10} {score}  [{status}]')\ngrade_map=dict(zip(names,scores))\navg=sum(scores)/len(scores)\nprint(f'\\nAverage: {avg:.1f}')",
    "hint": "zip(names, scores, courses). dict(zip(names, scores)). sum(scores)/len(scores).",
    "rubric": "zip combines 3 lists. Loop unpacks tuple. dict from zip. Average calculated."
  }
],

"Dictionaries & Sets": [
  {
    "title": "Dictionary Comprehensions",
    "theory": "## Dict Comprehensions\n```python\n# Basic\nsquares = {x: x**2 for x in range(6)}\n# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n\n# With condition\neven_sq = {x: x**2 for x in range(10) if x % 2 == 0}\n\n# From two lists\nkeys = ['name', 'age', 'city']\nvals = ['Ada', 25, 'Lagos']\ninfo = {k: v for k, v in zip(keys, vals)}\n\n# Invert a dict\noriginal = {'a': 1, 'b': 2}\ninverted = {v: k for k, v in original.items()}\n```",
    "instructions": "## Task: Word Frequency Counter\n1. Given a sentence, split into words\n2. Use a dict comprehension to count word frequency\n3. Filter to only words appearing more than once\n4. Sort by frequency descending",
    "starterCode": "sentence = 'the cat sat on the mat and the cat slept on the mat'\nwords = sentence.split()\n\n# Count frequency\nfreq = {}\nfor word in words:\n    freq[word] = freq.get(word, ___) + ___\n\n# Filter words appearing more than once\nrepeated = {word: count for word, count in freq.___() if count > ___}\n\n# Sort by frequency\nsorted_words = sorted(repeated.items(), key=lambda x: x[___], reverse=True)\n\nfor word, count in sorted_words:\n    bar = '#' * count\n    print(f'{word:10} {count}  {bar}')",
    "solution": "sentence='the cat sat on the mat and the cat slept on the mat'\nwords=sentence.split()\nfreq={}\nfor word in words:freq[word]=freq.get(word,0)+1\nrepeated={word:count for word,count in freq.items() if count>1}\nsorted_words=sorted(repeated.items(),key=lambda x:x[1],reverse=True)\nfor word,count in sorted_words:\n    bar='#'*count\n    print(f'{word:10} {count}  {bar}')",
    "hint": "freq.get(word, 0) returns 0 if not found. freq.items() gives key-value pairs. Sort by x[1] for value.",
    "rubric": "Word splitting. Frequency counting with get(). Dict comprehension filter. Sorted by count."
  },
  {
    "title": "Set Operations for Data Analysis",
    "theory": "## Set Operations\n```python\na = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\n\na | b    # Union: {1,2,3,4,5,6,7,8}\na & b    # Intersection: {4, 5}\na - b    # Difference: {1, 2, 3}\na ^ b    # Symmetric diff: {1,2,3,6,7,8}\n\na.issubset(b)    # False\na.issuperset(b)  # False\n\n# Remove duplicates\ndupes = [1,1,2,2,3]\nunique = list(set(dupes))  # [1, 2, 3]\n```",
    "instructions": "## Task: Course Enrollment Analysis\n1. Given sets of students enrolled in Python, SQL, and AI courses\n2. Find students in ALL courses (intersection)\n3. Find students in Python but NOT SQL\n4. Find students in exactly one course\n5. Find total unique students",
    "starterCode": "python_students = {'Ada', 'Tunde', 'Ngozi', 'Kemi', 'Bayo'}\nsql_students = {'Tunde', 'Ngozi', 'Femi', 'Zara'}\nai_students = {'Ada', 'Ngozi', 'Zara', 'Tunde'}\n\n# Students in ALL courses\nall_three = python_students ___ sql_students ___ ai_students\n\n# Python but not SQL\npython_only = python_students ___ sql_students\n\n# Total unique students\nall_students = python_students ___ sql_students ___ ai_students\n\nprint(f'In all 3: {all_three}')\nprint(f'Python not SQL: {python_only}')\nprint(f'Total unique: {len(all_students)}')",
    "solution": "python_students={'Ada','Tunde','Ngozi','Kemi','Bayo'}\nsql_students={'Tunde','Ngozi','Femi','Zara'}\nai_students={'Ada','Ngozi','Zara','Tunde'}\nall_three=python_students&sql_students&ai_students\npython_only=python_students-sql_students\nall_students=python_students|sql_students|ai_students\nprint(f'In all 3: {all_three}')\nprint(f'Python not SQL: {python_only}')\nprint(f'Total unique: {len(all_students)}')",
    "hint": "& for intersection, - for difference, | for union.",
    "rubric": "Intersection with &. Difference with -. Union with |. All results printed."
  },
  {
    "title": "Nested Dictionaries & JSON-like Data",
    "theory": "## Nested Dicts\n```python\nschool = {\n    'students': {\n        'Ada': {'grade': 'A', 'courses': ['Python', 'SQL']},\n        'Tunde': {'grade': 'B', 'courses': ['Python']}\n    },\n    'total': 2\n}\n\n# Access nested\nschool['students']['Ada']['grade']  # 'A'\n\n# Safe access with .get()\nschool.get('teachers', {}).get('math', 'N/A')\n\n# Iterate nested\nfor name, info in school['students'].items():\n    print(f\"{name}: {info['grade']}\")\n```",
    "instructions": "## Task: Academy Database\n1. Build a nested dict representing a mini academy\n2. Include 3 students, each with name, scores (dict of course:score), and level\n3. Calculate each student's average score\n4. Find the student with the highest average",
    "starterCode": "academy = {\n    'Ada':   {'scores': {'Python': 92, 'SQL': 88, 'AI': 95}, 'level': 'Advanced'},\n    'Tunde': {'scores': {'Python': 75, 'SQL': 82, 'AI': 70}, 'level': 'Intermediate'},\n    'Ngozi': {'scores': {'Python': 88, 'SQL': 90, 'AI': 85}, 'level': 'Advanced'},\n}\n\n# Calculate averages\nfor name, data in academy.___():\n    scores = data['scores'].___()  # Get all score values\n    avg = sum(___) / len(list(scores))\n    data['average'] = round(avg, 1)\n    print(f\"{name}: avg = {data['average']} ({data['level']})\")\n\n# Find top student\ntop = max(academy.items(), key=lambda x: x[1][___])\nprint(f'\\nTop student: {top[0]} with {top[1][\"average\"]}')",
    "solution": "academy={'Ada':{'scores':{'Python':92,'SQL':88,'AI':95},'level':'Advanced'},'Tunde':{'scores':{'Python':75,'SQL':82,'AI':70},'level':'Intermediate'},'Ngozi':{'scores':{'Python':88,'SQL':90,'AI':85},'level':'Advanced'}}\nfor name,data in academy.items():\n    scores=list(data['scores'].values())\n    avg=sum(scores)/len(scores)\n    data['average']=round(avg,1)\n    print(f\"{name}: avg = {data['average']} ({data['level']})\")\ntop=max(academy.items(),key=lambda x:x[1]['average'])\nprint(f'\\nTop student: {top[0]} with {top[1][\"average\"]}')",
    "hint": "dict.items() for key-value pairs. dict.values() for just values. max with key lambda.",
    "rubric": "Nested dict structure. items() iteration. values() for scores. Average calculated. max() finds top."
  }
],

# ─── PYTHON CORE: INTERMEDIATE ───
"OOP in Python": [
  {
    "title": "Class Inheritance & super()",
    "theory": "## Inheritance\n```python\nclass Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return 'Some sound'\n\nclass Dog(Animal):\n    def __init__(self, name, breed):\n        super().__init__(name)  # Call parent __init__\n        self.breed = breed\n    def speak(self):\n        return 'Woof!'\n\ndog = Dog('Rex', 'Labrador')\nprint(dog.name)    # From Animal\nprint(dog.breed)   # From Dog\nprint(dog.speak()) # Overridden\n```",
    "instructions": "## Task: Course Hierarchy\n1. Create a base `Course` class with title, level\n2. Create `CodingCourse(Course)` that adds language and has a `run_code()` method\n3. Create `TheoryCourse(Course)` that adds topic and has a `take_quiz()` method\n4. Use `super()` in each child class",
    "starterCode": "class Course:\n    def __init__(self, title, level='Beginner'):\n        self.title = title\n        self.level = level\n    def describe(self):\n        return f'{self.title} ({self.level})'\n\nclass CodingCourse(___):\n    def __init__(self, title, language, level='Beginner'):\n        ___.__init__(title, level)\n        self.language = ___\n    def run_code(self, code):\n        return f'Running {self.language}: {code}'\n\nclass TheoryCourse(___):\n    def __init__(self, title, topic, level='Beginner'):\n        ___.__init__(title, level)\n        self.topic = ___\n    def take_quiz(self):\n        return f'Quiz on {self.topic} for {self.title}'\n\npy = CodingCourse('Python Fundamentals', 'Python')\nai = TheoryCourse('AI Concepts', 'Machine Learning', 'Advanced')\n\nprint(py.describe())\nprint(py.run_code('print(42)'))\nprint(ai.describe())\nprint(ai.take_quiz())",
    "solution": "class Course:\n    def __init__(self,title,level='Beginner'):\n        self.title=title;self.level=level\n    def describe(self):return f'{self.title} ({self.level})'\nclass CodingCourse(Course):\n    def __init__(self,title,language,level='Beginner'):\n        super().__init__(title,level)\n        self.language=language\n    def run_code(self,code):return f'Running {self.language}: {code}'\nclass TheoryCourse(Course):\n    def __init__(self,title,topic,level='Beginner'):\n        super().__init__(title,level)\n        self.topic=topic\n    def take_quiz(self):return f'Quiz on {self.topic} for {self.title}'\npy=CodingCourse('Python Fundamentals','Python')\nai=TheoryCourse('AI Concepts','Machine Learning','Advanced')\nprint(py.describe())\nprint(py.run_code('print(42)'))\nprint(ai.describe())\nprint(ai.take_quiz())",
    "hint": "class Child(Parent). super().__init__() calls parent constructor.",
    "rubric": "Base Course class. CodingCourse inherits. TheoryCourse inherits. super() used. Methods work."
  },
  {
    "title": "Magic Methods & Operator Overloading",
    "theory": "## Magic Methods\n```python\nclass Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f'Vector({self.x}, {self.y})'\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    def __eq__(self, other):\n        return self.x == other.x and self.y == other.y\n    def __len__(self):\n        return int((self.x**2 + self.y**2)**0.5)\n\nv1 = Vector(3, 4)\nv2 = Vector(1, 2)\nprint(v1 + v2)   # Vector(4, 6)\nprint(len(v1))    # 5\n```",
    "instructions": "## Task: Student Score Object\n1. Create `Score` class with student name and points\n2. Implement `__repr__` for display\n3. Implement `__add__` to combine scores\n4. Implement `__gt__` for comparison\n5. Implement `__len__` returning points",
    "starterCode": "class Score:\n    def __init__(self, student, points):\n        self.student = student\n        self.points = points\n    \n    def __repr__(self):\n        return f'Score({self.___}, {self.___})'\n    \n    def __add__(self, other):\n        combined = self.student + '+' + other.student\n        return Score(combined, self.___ + other.___)\n    \n    def __gt__(self, other):\n        return self.points ___ other.points\n    \n    def __len__(self):\n        return self.___\n\ns1 = Score('Ada', 92)\ns2 = Score('Tunde', 88)\n\nprint(s1)           # Score(Ada, 92)\nprint(s1 + s2)      # Score(Ada+Tunde, 180)\nprint(s1 > s2)      # True\nprint(len(s1))      # 92",
    "solution": "class Score:\n    def __init__(self,student,points):self.student=student;self.points=points\n    def __repr__(self):return f'Score({self.student}, {self.points})'\n    def __add__(self,other):return Score(self.student+'+'+other.student,self.points+other.points)\n    def __gt__(self,other):return self.points>other.points\n    def __len__(self):return self.points\ns1=Score('Ada',92)\ns2=Score('Tunde',88)\nprint(s1)\nprint(s1+s2)\nprint(s1>s2)\nprint(len(s1))",
    "hint": "__repr__ returns string. __add__ returns new Score. __gt__ compares points. __len__ returns points.",
    "rubric": "__repr__ shows name and points. __add__ combines. __gt__ compares. __len__ returns points."
  },
  {
    "title": "Properties & Encapsulation",
    "theory": "## Properties\n```python\nclass BankAccount:\n    def __init__(self, balance=0):\n        self._balance = balance  # Private convention\n    \n    @property\n    def balance(self):\n        return self._balance\n    \n    @balance.setter\n    def balance(self, value):\n        if value < 0:\n            raise ValueError('Cannot be negative')\n        self._balance = value\n    \n    def deposit(self, amount):\n        self.balance += amount  # Uses setter!\n\nacc = BankAccount(100)\nprint(acc.balance)   # 100 (uses getter)\nacc.balance = 200    # Uses setter\n```",
    "instructions": "## Task: Student Profile with Validation\n1. Create `StudentProfile` with name and _score (private)\n2. Use @property for score getter\n3. Use @score.setter that validates 0-100 range\n4. Add a `grade` property that returns letter grade based on score",
    "starterCode": "class StudentProfile:\n    def __init__(self, name, score=0):\n        self.name = name\n        self._score = score\n    \n    @property\n    def score(self):\n        return self.___\n    \n    @score.setter\n    def score(self, value):\n        if not (0 <= value <= ___):\n            raise ValueError('Score must be 0-100')\n        self.___ = value\n    \n    @property\n    def grade(self):\n        if self._score >= 90: return 'A'\n        if self._score >= 80: return '___'\n        if self._score >= 70: return 'C'\n        return 'F'\n\ns = StudentProfile('Ada', 85)\nprint(f'{s.name}: {s.score} ({s.grade})')\ns.score = 95\nprint(f'{s.name}: {s.score} ({s.grade})')",
    "solution": "class StudentProfile:\n    def __init__(self,name,score=0):self.name=name;self._score=score\n    @property\n    def score(self):return self._score\n    @score.setter\n    def score(self,value):\n        if not(0<=value<=100):raise ValueError('Score must be 0-100')\n        self._score=value\n    @property\n    def grade(self):\n        if self._score>=90:return 'A'\n        if self._score>=80:return 'B'\n        if self._score>=70:return 'C'\n        return 'F'\ns=StudentProfile('Ada',85)\nprint(f'{s.name}: {s.score} ({s.grade})')\ns.score=95\nprint(f'{s.name}: {s.score} ({s.grade})')",
    "hint": "@property decorator for getter. @score.setter for validation. Check 0-100 range.",
    "rubric": "Private _score. @property getter. @setter with validation. Grade property computed."
  }
],

"File Handling & Exceptions": [
  {
    "title": "Custom Exceptions & Error Hierarchy",
    "theory": "## Custom Exceptions\n```python\nclass AppError(Exception):\n    pass\n\nclass ValidationError(AppError):\n    def __init__(self, field, message):\n        self.field = field\n        super().__init__(f'{field}: {message}')\n\nclass NotFoundError(AppError):\n    pass\n\ntry:\n    raise ValidationError('email', 'Invalid format')\nexcept ValidationError as e:\n    print(f'Validation: {e.field} - {e}')\nexcept AppError as e:\n    print(f'App error: {e}')\n```",
    "instructions": "## Task: Academy Error System\n1. Create base `AcademyError(Exception)`\n2. Create `EnrollmentError(AcademyError)` with student and course\n3. Create `GradeError(AcademyError)` with score validation\n4. Test with try/except handling both error types",
    "starterCode": "class AcademyError(Exception):\n    pass\n\nclass EnrollmentError(___):\n    def __init__(self, student, course):\n        self.student = student\n        self.course = course\n        super().__init__(f'{student} cannot enroll in {course}')\n\nclass GradeError(___):\n    def __init__(self, score):\n        self.score = score\n        super().__init__(f'Invalid score: {score}. Must be 0-100')\n\ndef enroll(student, course, prereq_met=True):\n    if not prereq_met:\n        raise ___(student, course)\n    return f'{student} enrolled in {course}'\n\ndef assign_grade(score):\n    if not (0 <= score <= ___):\n        raise ___(score)\n    return 'A' if score >= 90 else 'B' if score >= 80 else 'C'\n\n# Test\nfor test in [('Ada', 'AI', True), ('Tunde', 'AI', False)]:\n    try:\n        print(enroll(*test))\n    except EnrollmentError as e:\n        print(f'BLOCKED: {e}')\n\nfor score in [95, 150, -10]:\n    try:\n        print(f'{score} -> {assign_grade(score)}')\n    except ___ as e:\n        print(f'ERROR: {e}')",
    "solution": "class AcademyError(Exception):pass\nclass EnrollmentError(AcademyError):\n    def __init__(self,student,course):self.student=student;self.course=course;super().__init__(f'{student} cannot enroll in {course}')\nclass GradeError(AcademyError):\n    def __init__(self,score):self.score=score;super().__init__(f'Invalid score: {score}. Must be 0-100')\ndef enroll(student,course,prereq_met=True):\n    if not prereq_met:raise EnrollmentError(student,course)\n    return f'{student} enrolled in {course}'\ndef assign_grade(score):\n    if not(0<=score<=100):raise GradeError(score)\n    return 'A' if score>=90 else 'B' if score>=80 else 'C'\nfor test in [('Ada','AI',True),('Tunde','AI',False)]:\n    try:print(enroll(*test))\n    except EnrollmentError as e:print(f'BLOCKED: {e}')\nfor score in [95,150,-10]:\n    try:print(f'{score} -> {assign_grade(score)}')\n    except GradeError as e:print(f'ERROR: {e}')",
    "hint": "Inherit from AcademyError. raise ErrorClass(args). except SpecificError as e.",
    "rubric": "Base exception class. Two child exceptions. raise in functions. try/except catches correctly."
  },
  {
    "title": "Context Managers & with Statement",
    "theory": "## Context Managers\n```python\n# Built-in file context manager\nwith open('data.txt', 'w') as f:\n    f.write('Hello')  # File auto-closes!\n\n# Custom context manager with class\nclass Timer:\n    def __enter__(self):\n        import time\n        self.start = time.time()\n        return self\n    def __exit__(self, *args):\n        self.elapsed = time.time() - self.start\n        print(f'Took {self.elapsed:.2f}s')\n\nwith Timer() as t:\n    sum(range(1000000))\n```",
    "instructions": "## Task: Logger Context Manager\n1. Create `Logger` class that acts as a context manager\n2. On __enter__: print 'Starting...' and record start time\n3. On __exit__: print 'Finished in X.XXs' and log any exceptions\n4. Test with both successful and failing code blocks",
    "starterCode": "import time\n\nclass Logger:\n    def __init__(self, task_name):\n        self.task_name = task_name\n    \n    def __enter__(self):\n        print(f'[START] {self.task_name}')\n        self.start = time.___\n        return self\n    \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        elapsed = time.time() - self.___\n        if exc_type:\n            print(f'[FAILED] {self.task_name}: {exc_val} ({elapsed:.2f}s)')\n            return ___  # True = suppress exception\n        print(f'[DONE] {self.task_name} ({elapsed:.2f}s)')\n        return False\n\n# Success\nwith Logger('Data Processing') as log:\n    total = sum(range(100000))\n    print(f'  Result: {total}')\n\n# Failure (suppressed)\nwith Logger('Risky Operation') as log:\n    result = 10 / 0",
    "solution": "import time\nclass Logger:\n    def __init__(self,task_name):self.task_name=task_name\n    def __enter__(self):\n        print(f'[START] {self.task_name}')\n        self.start=time.time()\n        return self\n    def __exit__(self,exc_type,exc_val,exc_tb):\n        elapsed=time.time()-self.start\n        if exc_type:\n            print(f'[FAILED] {self.task_name}: {exc_val} ({elapsed:.2f}s)')\n            return True\n        print(f'[DONE] {self.task_name} ({elapsed:.2f}s)')\n        return False\nwith Logger('Data Processing') as log:\n    total=sum(range(100000))\n    print(f'  Result: {total}')\nwith Logger('Risky Operation') as log:\n    result=10/0",
    "hint": "time.time() for current time. __exit__ receives exception info. Return True to suppress exceptions.",
    "rubric": "__enter__ records start time. __exit__ calculates elapsed. Exception handling. Both tests run."
  },
  {
    "title": "Reading & Writing CSV Data",
    "theory": "## CSV Files\n```python\nimport csv\nimport io\n\n# Write CSV\nwith open('students.csv', 'w', newline='') as f:\n    writer = csv.DictWriter(f, fieldnames=['name', 'score'])\n    writer.writeheader()\n    writer.writerow({'name': 'Ada', 'score': 92})\n\n# Read CSV\nwith open('students.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        print(row['name'], row['score'])\n```",
    "instructions": "## Task: CSV Report Generator\n1. Create student data as a list of dicts\n2. Write to a CSV string using io.StringIO (simulated file)\n3. Read it back and calculate statistics\n4. Print a formatted report",
    "starterCode": "import csv\nimport io\n\nstudents = [\n    {'name': 'Ada', 'course': 'Python', 'score': 92},\n    {'name': 'Tunde', 'course': 'SQL', 'score': 78},\n    {'name': 'Ngozi', 'course': 'AI', 'score': 95},\n    {'name': 'Kemi', 'course': 'Python', 'score': 88},\n]\n\n# Write to CSV string\noutput = io.StringIO()\nwriter = csv.DictWriter(output, fieldnames=[___, ___, ___])\nwriter.writeheader()\nfor s in students:\n    writer.writerow(___)\n\ncsv_text = output.getvalue()\nprint('=== Raw CSV ===')\nprint(csv_text)\n\n# Read back\nreader = csv.DictReader(io.StringIO(csv_text))\nscores = []\nfor row in ___:\n    scores.append(int(row['___']))\n    print(f\"  {row['name']:10} {row['course']:10} {row['score']}\")\n\nprint(f'\\nAverage: {sum(scores)/len(scores):.1f}')\nprint(f'Highest: {max(scores)}')",
    "solution": "import csv\nimport io\nstudents=[{'name':'Ada','course':'Python','score':92},{'name':'Tunde','course':'SQL','score':78},{'name':'Ngozi','course':'AI','score':95},{'name':'Kemi','course':'Python','score':88}]\noutput=io.StringIO()\nwriter=csv.DictWriter(output,fieldnames=['name','course','score'])\nwriter.writeheader()\nfor s in students:writer.writerow(s)\ncsv_text=output.getvalue()\nprint('=== Raw CSV ===')\nprint(csv_text)\nreader=csv.DictReader(io.StringIO(csv_text))\nscores=[]\nfor row in reader:\n    scores.append(int(row['score']))\n    print(f\"  {row['name']:10} {row['course']:10} {row['score']}\")\nprint(f'\\nAverage: {sum(scores)/len(scores):.1f}')\nprint(f'Highest: {max(scores)}')",
    "hint": "DictWriter with fieldnames list. writerow(dict). DictReader iterates rows. int() for score.",
    "rubric": "CSV written with DictWriter. Read back with DictReader. Stats calculated. Report formatted."
  }
],

# ─── SQL & DATABASES: BEGINNER ───
"SQL Fundamentals": [
  {
    "title": "CREATE TABLE & Data Types",
    "theory": "## CREATE TABLE\n```python\n# SQLite in Python simulates SQL perfectly\nimport sqlite3\nconn = sqlite3.connect(':memory:')\ncursor = conn.cursor()\n\ncursor.execute('''\n    CREATE TABLE students (\n        id INTEGER PRIMARY KEY,\n        name TEXT NOT NULL,\n        email TEXT UNIQUE,\n        score REAL DEFAULT 0.0,\n        enrolled BOOLEAN DEFAULT 1\n    )\n''')\n```\nCommon types: INTEGER, TEXT, REAL, BOOLEAN, BLOB",
    "instructions": "## Task: Create Academy Tables\n1. Create a `courses` table with: id, title, level, max_students\n2. Create an `enrollments` table with: id, student_name, course_id, grade\n3. Insert 3 courses and 4 enrollments\n4. Query and print all data",
    "starterCode": "import sqlite3\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\n\nc.execute('''CREATE TABLE courses (\n    id INTEGER PRIMARY KEY,\n    title TEXT NOT ___,\n    level TEXT DEFAULT 'Beginner',\n    max_students INTEGER DEFAULT ___\n)''')\n\nc.execute('''CREATE TABLE enrollments (\n    id INTEGER PRIMARY KEY,\n    student_name TEXT NOT NULL,\n    course_id INTEGER,\n    grade TEXT DEFAULT ___\n)''')\n\n# Insert courses\nc.execute(\"INSERT INTO courses (title, level) VALUES ('Python', 'Beginner')\")\nc.execute(\"INSERT INTO courses (title, level) VALUES ('SQL', 'Intermediate')\")\nc.execute(\"INSERT INTO courses (title, level) VALUES ('AI', '___')\")\n\n# Insert enrollments\nc.execute(\"INSERT INTO enrollments (student_name, course_id) VALUES ('Ada', 1)\")\nc.execute(\"INSERT INTO enrollments (student_name, course_id) VALUES ('Tunde', ___)\")\nc.execute(\"INSERT INTO enrollments (student_name, course_id, grade) VALUES ('Ngozi', 1, 'A')\")\nc.execute(\"INSERT INTO enrollments (student_name, course_id, grade) VALUES ('Kemi', 3, '___')\")\n\nconn.commit()\n\nprint('=== Courses ===')\nfor row in c.execute('SELECT * FROM courses'):\n    print(row)\nprint('\\n=== Enrollments ===')\nfor row in c.execute('SELECT * FROM enrollments'):\n    print(row)",
    "solution": "import sqlite3\nconn=sqlite3.connect(':memory:')\nc=conn.cursor()\nc.execute('''CREATE TABLE courses(id INTEGER PRIMARY KEY,title TEXT NOT NULL,level TEXT DEFAULT 'Beginner',max_students INTEGER DEFAULT 30)''')\nc.execute('''CREATE TABLE enrollments(id INTEGER PRIMARY KEY,student_name TEXT NOT NULL,course_id INTEGER,grade TEXT DEFAULT 'N/A')''')\nc.execute(\"INSERT INTO courses(title,level)VALUES('Python','Beginner')\")\nc.execute(\"INSERT INTO courses(title,level)VALUES('SQL','Intermediate')\")\nc.execute(\"INSERT INTO courses(title,level)VALUES('AI','Advanced')\")\nc.execute(\"INSERT INTO enrollments(student_name,course_id)VALUES('Ada',1)\")\nc.execute(\"INSERT INTO enrollments(student_name,course_id)VALUES('Tunde',2)\")\nc.execute(\"INSERT INTO enrollments(student_name,course_id,grade)VALUES('Ngozi',1,'A')\")\nc.execute(\"INSERT INTO enrollments(student_name,course_id,grade)VALUES('Kemi',3,'B')\")\nconn.commit()\nprint('=== Courses ===')\nfor row in c.execute('SELECT * FROM courses'):print(row)\nprint('\\n=== Enrollments ===')\nfor row in c.execute('SELECT * FROM enrollments'):print(row)",
    "hint": "NOT NULL prevents empty values. DEFAULT sets fallback. INTEGER PRIMARY KEY auto-increments.",
    "rubric": "Two tables created. NOT NULL and DEFAULT used. Data inserted. Query displays results."
  },
  {
    "title": "UPDATE & DELETE Operations",
    "theory": "## UPDATE & DELETE\n```python\n# UPDATE specific rows\ncursor.execute('''\n    UPDATE students SET score = 95\n    WHERE name = 'Ada'\n''')\n\n# UPDATE with calculation\ncursor.execute('''\n    UPDATE students SET score = score + 10\n    WHERE score < 50\n''')\n\n# DELETE specific rows\ncursor.execute('''\n    DELETE FROM students WHERE score < 30\n''')\n\n# DELETE all (careful!)\ncursor.execute('DELETE FROM students')\n```",
    "instructions": "## Task: Student Management\n1. Create a students table and insert 5 students\n2. UPDATE: Give bonus 10 points to students scoring below 80\n3. UPDATE: Change level to 'Advanced' for scores >= 90\n4. DELETE: Remove students with score below 50\n5. Print before and after",
    "starterCode": "import sqlite3\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\n\nc.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, score INTEGER, level TEXT DEFAULT \"Beginner\")')\n\nfor name, score in [('Ada',92),('Tunde',45),('Ngozi',78),('Kemi',88),('Bayo',35)]:\n    c.execute('INSERT INTO students (name,score) VALUES (?,?)', (name, score))\nconn.commit()\n\nprint('=== BEFORE ===')\nfor row in c.execute('SELECT * FROM students'): print(row)\n\n# Bonus points\nc.execute('UPDATE students SET score = score + ___ WHERE score < ___')\n\n# Promote to Advanced\nc.execute('UPDATE students SET level = ___ WHERE score >= ___')\n\n# Remove failing students\nc.execute('DELETE FROM students WHERE score < ___')\nconn.commit()\n\nprint('\\n=== AFTER ===')\nfor row in c.execute('SELECT * FROM students'): print(row)",
    "solution": "import sqlite3\nconn=sqlite3.connect(':memory:')\nc=conn.cursor()\nc.execute('CREATE TABLE students(id INTEGER PRIMARY KEY,name TEXT,score INTEGER,level TEXT DEFAULT \"Beginner\")')\nfor name,score in [('Ada',92),('Tunde',45),('Ngozi',78),('Kemi',88),('Bayo',35)]:\n    c.execute('INSERT INTO students(name,score)VALUES(?,?)',(name,score))\nconn.commit()\nprint('=== BEFORE ===')\nfor row in c.execute('SELECT * FROM students'):print(row)\nc.execute('UPDATE students SET score=score+10 WHERE score<80')\nc.execute('UPDATE students SET level=\"Advanced\" WHERE score>=90')\nc.execute('DELETE FROM students WHERE score<50')\nconn.commit()\nprint('\\n=== AFTER ===')\nfor row in c.execute('SELECT * FROM students'):print(row)",
    "hint": "UPDATE...SET...WHERE for conditional updates. DELETE FROM...WHERE for removal.",
    "rubric": "Table created with data. UPDATE with bonus. UPDATE level. DELETE low scores. Before/after shown."
  },
  {
    "title": "WHERE Clauses & Operators",
    "theory": "## WHERE Operators\n```python\n# Comparison\nSELECT * FROM students WHERE score >= 80\n\n# AND / OR\nWHERE score >= 80 AND level = 'Advanced'\nWHERE course = 'Python' OR course = 'SQL'\n\n# IN\nWHERE course IN ('Python', 'SQL', 'AI')\n\n# BETWEEN\nWHERE score BETWEEN 70 AND 90\n\n# LIKE (pattern matching)\nWHERE name LIKE 'A%'     -- starts with A\nWHERE email LIKE '%@gmail.com'\n\n# IS NULL / IS NOT NULL\nWHERE grade IS NOT NULL\n```",
    "instructions": "## Task: Advanced Queries\n1. Create students with various attributes\n2. Query: students scoring BETWEEN 70 AND 90\n3. Query: students whose name starts with 'A' or 'N'\n4. Query: students in Python OR AI courses\n5. Query: students with no grade assigned (IS NULL)",
    "starterCode": "import sqlite3\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\n\nc.execute('CREATE TABLE students (name TEXT, course TEXT, score INTEGER, grade TEXT)')\ndata = [('Ada','Python',92,'A'),('Tunde','SQL',78,None),('Ngozi','AI',85,'B'),\n        ('Kemi','Python',70,None),('Bayo','AI',95,'A'),('Amara','SQL',62,None)]\nfor d in data:\n    c.execute('INSERT INTO students VALUES (?,?,?,?)', d)\nconn.commit()\n\nprint('=== Score 70-90 ===')\nfor r in c.execute('SELECT * FROM students WHERE score ___ 70 ___ 90'): print(r)\n\nprint('\\n=== Names starting with A or N ===')\nfor r in c.execute(\"SELECT * FROM students WHERE name LIKE '___' OR name LIKE '___'\"): print(r)\n\nprint('\\n=== Python or AI students ===')\nfor r in c.execute(\"SELECT * FROM students WHERE course ___ ('Python', 'AI')\"): print(r)\n\nprint('\\n=== No grade assigned ===')\nfor r in c.execute('SELECT * FROM students WHERE grade ___ ___'): print(r)",
    "solution": "import sqlite3\nconn=sqlite3.connect(':memory:')\nc=conn.cursor()\nc.execute('CREATE TABLE students(name TEXT,course TEXT,score INTEGER,grade TEXT)')\ndata=[('Ada','Python',92,'A'),('Tunde','SQL',78,None),('Ngozi','AI',85,'B'),('Kemi','Python',70,None),('Bayo','AI',95,'A'),('Amara','SQL',62,None)]\nfor d in data:c.execute('INSERT INTO students VALUES(?,?,?,?)',d)\nconn.commit()\nprint('=== Score 70-90 ===')\nfor r in c.execute('SELECT * FROM students WHERE score BETWEEN 70 AND 90'):print(r)\nprint('\\n=== Names starting with A or N ===')\nfor r in c.execute(\"SELECT * FROM students WHERE name LIKE 'A%' OR name LIKE 'N%'\"):print(r)\nprint('\\n=== Python or AI ===')\nfor r in c.execute(\"SELECT * FROM students WHERE course IN ('Python','AI')\"):print(r)\nprint('\\n=== No grade ===')\nfor r in c.execute('SELECT * FROM students WHERE grade IS NULL'):print(r)",
    "hint": "BETWEEN x AND y. LIKE 'A%' for starts with. IN (...) for list. IS NULL for empty.",
    "rubric": "BETWEEN used. LIKE with % wildcard. IN for list matching. IS NULL for null check."
  }
],

# ─── FRONTEND: BEGINNER ───
"HTML Essentials": [
  {
    "title": "Semantic HTML & Structure",
    "theory": "## Semantic HTML\nSemantic elements describe their meaning to both browsers and developers.\n```python\n# Python string representing semantic HTML\nhtml = '''\n<header>Site title</header>\n<nav>Navigation links</nav>\n<main>\n  <article>\n    <h1>Article Title</h1>\n    <p>Content here</p>\n  </article>\n  <aside>Sidebar</aside>\n</main>\n<footer>Copyright info</footer>\n'''\n```\nKey elements: header, nav, main, article, section, aside, footer",
    "instructions": "## Task: Build a Page Structure\n1. Create an HTML string for a course page\n2. Use header, nav, main, article, and footer\n3. The article should have h1, h2, and paragraph tags\n4. Count the semantic elements used",
    "starterCode": "html = f'''\n<___>\n  <h1>Mabel Academy</h1>\n</___>\n<___>\n  <a href=\"/courses\">Courses</a>\n  <a href=\"/about\">About</a>\n</___>\n<___>\n  <___>\n    <h1>Python Fundamentals</h1>\n    <h2>Lesson 1: Variables</h2>\n    <p>Variables store data in memory.</p>\n  </___>\n</___>\n<___>\n  <p>Copyright 2024 Mabel Academy</p>\n</___>\n'''\n\n# Count semantic elements\nsemantic_tags = ['header', 'nav', 'main', 'article', 'footer']\ncount = sum(1 for tag in semantic_tags if f'<{tag}>' in html)\nprint(f'Semantic elements used: {count}/{len(semantic_tags)}')\nprint(html)",
    "solution": "html=f'''\n<header>\n  <h1>Mabel Academy</h1>\n</header>\n<nav>\n  <a href=\"/courses\">Courses</a>\n  <a href=\"/about\">About</a>\n</nav>\n<main>\n  <article>\n    <h1>Python Fundamentals</h1>\n    <h2>Lesson 1: Variables</h2>\n    <p>Variables store data in memory.</p>\n  </article>\n</main>\n<footer>\n  <p>Copyright 2024 Mabel Academy</p>\n</footer>\n'''\nsemantic_tags=['header','nav','main','article','footer']\ncount=sum(1 for tag in semantic_tags if f'<{tag}>' in html)\nprint(f'Semantic elements used: {count}/{len(semantic_tags)}')\nprint(html)",
    "hint": "header, nav, main, article, footer are the 5 semantic elements needed.",
    "rubric": "All 5 semantic tags used. Proper nesting. h1, h2, p inside article. Count shows 5/5."
  },
  {
    "title": "HTML Tables & Data Display",
    "theory": "## HTML Tables\n```python\ntable = '''\n<table>\n  <thead>\n    <tr><th>Name</th><th>Score</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Ada</td><td>92</td></tr>\n    <tr><td>Tunde</td><td>88</td></tr>\n  </tbody>\n</table>\n'''\n```\nElements: table, thead, tbody, tr (row), th (header cell), td (data cell)",
    "instructions": "## Task: Dynamic Student Table\n1. Given student data as a list of dicts\n2. Generate an HTML table string dynamically\n3. Include thead with column headers\n4. Include tbody with data rows\n5. Add a tfoot with average score",
    "starterCode": "students = [\n    {'name': 'Ada', 'course': 'Python', 'score': 92},\n    {'name': 'Tunde', 'course': 'SQL', 'score': 78},\n    {'name': 'Ngozi', 'course': 'AI', 'score': 95},\n]\n\n# Build header\nheaders = students[0].keys()\nheader_row = ''.join(f'<th>{h.title()}</th>' for h in ___)\n\n# Build body rows\nbody_rows = ''\nfor s in students:\n    cells = ''.join(f'<td>{s[h]}</td>' for h in ___)\n    body_rows += f'<tr>{___}</tr>\\n'\n\n# Calculate average\navg = sum(s['score'] for s in ___) / len(students)\n\nhtml = f'''<table>\n  <thead><tr>{header_row}</tr></thead>\n  <tbody>{body_rows}</tbody>\n  <tfoot><tr><td colspan=\"2\">Average</td><td>{avg:.1f}</td></tr></tfoot>\n</table>'''\n\nprint(html)",
    "solution": "students=[{'name':'Ada','course':'Python','score':92},{'name':'Tunde','course':'SQL','score':78},{'name':'Ngozi','course':'AI','score':95}]\nheaders=students[0].keys()\nheader_row=''.join(f'<th>{h.title()}</th>' for h in headers)\nbody_rows=''\nfor s in students:\n    cells=''.join(f'<td>{s[h]}</td>' for h in headers)\n    body_rows+=f'<tr>{cells}</tr>\\n'\navg=sum(s['score'] for s in students)/len(students)\nhtml=f'''<table>\n  <thead><tr>{header_row}</tr></thead>\n  <tbody>{body_rows}</tbody>\n  <tfoot><tr><td colspan=\"2\">Average</td><td>{avg:.1f}</td></tr></tfoot>\n</table>'''\nprint(html)",
    "hint": "dict.keys() for headers. Loop dicts for rows. f-string for each cell. sum()/len() for average.",
    "rubric": "thead with th elements. tbody with dynamic rows. tfoot with average. colspan used."
  },
  {
    "title": "HTML Forms & Input Types",
    "theory": "## HTML Forms\n```python\nform = '''\n<form action=\"/submit\" method=\"POST\">\n  <input type=\"text\" name=\"name\" placeholder=\"Name\" required>\n  <input type=\"email\" name=\"email\" placeholder=\"Email\">\n  <input type=\"number\" name=\"age\" min=\"0\" max=\"120\">\n  <select name=\"level\">\n    <option value=\"beginner\">Beginner</option>\n    <option value=\"advanced\">Advanced</option>\n  </select>\n  <textarea name=\"bio\" rows=\"4\"></textarea>\n  <button type=\"submit\">Submit</button>\n</form>\n'''\n```\nTypes: text, email, password, number, date, checkbox, radio, file, submit",
    "instructions": "## Task: Registration Form Builder\n1. Build an HTML form string for student registration\n2. Include: text (name), email, password, select (course), textarea (bio)\n3. Add required attribute to name and email\n4. Parse the form to count input elements",
    "starterCode": "form = f'''\n<form action=\"/register\" method=\"POST\">\n  <label>Name:</label>\n  <input type=\"___\" name=\"name\" placeholder=\"Full Name\" ___>\n  \n  <label>Email:</label>\n  <input type=\"___\" name=\"email\" placeholder=\"you@example.com\" ___>\n  \n  <label>Password:</label>\n  <input type=\"___\" name=\"password\" minlength=\"8\">\n  \n  <label>Course:</label>\n  <select name=\"course\">\n    <option value=\"python\">Python</option>\n    <option value=\"sql\">SQL</option>\n    <option value=\"ai\">___</option>\n  </select>\n  \n  <label>Bio:</label>\n  <textarea name=\"___\" rows=\"4\" placeholder=\"Tell us about yourself\"></textarea>\n  \n  <button type=\"submit\">Register</button>\n</form>\n'''\n\n# Count form elements\ninput_count = form.count('<input')\nselect_count = form.count('<select')\ntextarea_count = form.count('<textarea')\nprint(f'Inputs: {input_count}, Selects: {select_count}, Textareas: {textarea_count}')\nprint(form)",
    "solution": "form=f'''\n<form action=\"/register\" method=\"POST\">\n  <label>Name:</label>\n  <input type=\"text\" name=\"name\" placeholder=\"Full Name\" required>\n  <label>Email:</label>\n  <input type=\"email\" name=\"email\" placeholder=\"you@example.com\" required>\n  <label>Password:</label>\n  <input type=\"password\" name=\"password\" minlength=\"8\">\n  <label>Course:</label>\n  <select name=\"course\">\n    <option value=\"python\">Python</option>\n    <option value=\"sql\">SQL</option>\n    <option value=\"ai\">AI Engineering</option>\n  </select>\n  <label>Bio:</label>\n  <textarea name=\"bio\" rows=\"4\" placeholder=\"Tell us about yourself\"></textarea>\n  <button type=\"submit\">Register</button>\n</form>\n'''\ninput_count=form.count('<input')\nselect_count=form.count('<select')\ntextarea_count=form.count('<textarea')\nprint(f'Inputs: {input_count}, Selects: {select_count}, Textareas: {textarea_count}')\nprint(form)",
    "hint": "type='text', type='email', type='password'. required attribute. select with options.",
    "rubric": "Form with correct action/method. Input types correct. required on name/email. select and textarea present."
  }
],

# ─── DATA SCIENCE: BEGINNER ───
"Intro to Data Science": [
  {
    "title": "Statistics with Pure Python",
    "theory": "## Basic Statistics\n```python\nimport statistics\n\ndata = [85, 92, 78, 95, 88, 72, 90]\n\nmean = statistics.mean(data)      # Average\nmedian = statistics.median(data)  # Middle value\nmode = statistics.mode(data)      # Most common\nstdev = statistics.stdev(data)    # Spread\n\n# Manual mean\nmanual_mean = sum(data) / len(data)\n```",
    "instructions": "## Task: Grade Analyzer\n1. Given a list of exam scores\n2. Calculate mean, median, min, max, and range\n3. Count how many scores are above the mean\n4. Print a statistical summary",
    "starterCode": "import statistics\n\nscores = [72, 85, 90, 68, 95, 82, 77, 91, 88, 73]\n\nmean_score = statistics.___(scores)\nmedian_score = statistics.___(scores)\nmin_score = ___(scores)\nmax_score = ___(scores)\nscore_range = max_score - ___\n\nabove_avg = [s for s in scores if s > ___]\n\nprint('=== Grade Analysis ===')\nprint(f'Count:    {len(scores)}')\nprint(f'Mean:     {mean_score:.1f}')\nprint(f'Median:   {median_score}')\nprint(f'Min:      {min_score}')\nprint(f'Max:      {max_score}')\nprint(f'Range:    {score_range}')\nprint(f'Above avg: {len(above_avg)}/{len(scores)}')",
    "solution": "import statistics\nscores=[72,85,90,68,95,82,77,91,88,73]\nmean_score=statistics.mean(scores)\nmedian_score=statistics.median(scores)\nmin_score=min(scores)\nmax_score=max(scores)\nscore_range=max_score-min_score\nabove_avg=[s for s in scores if s>mean_score]\nprint('=== Grade Analysis ===')\nprint(f'Count: {len(scores)}')\nprint(f'Mean: {mean_score:.1f}')\nprint(f'Median: {median_score}')\nprint(f'Min: {min_score}')\nprint(f'Max: {max_score}')\nprint(f'Range: {score_range}')\nprint(f'Above avg: {len(above_avg)}/{len(scores)}')",
    "hint": "statistics.mean() and statistics.median(). min() and max() built-ins. List comprehension for filtering.",
    "rubric": "Mean and median calculated. Min, max, range computed. Above average filtered. Summary printed."
  },
  {
    "title": "Data Grouping & Aggregation",
    "theory": "## Grouping with defaultdict\n```python\nfrom collections import defaultdict\n\nsales = [\n    ('Electronics', 500), ('Books', 30),\n    ('Electronics', 200), ('Books', 45),\n]\n\ngrouped = defaultdict(list)\nfor category, amount in sales:\n    grouped[category].append(amount)\n\nfor cat, amounts in grouped.items():\n    print(f'{cat}: total={sum(amounts)}, avg={sum(amounts)/len(amounts):.0f}')\n```",
    "instructions": "## Task: Student Performance by Course\n1. Given student records with course and score\n2. Group scores by course using defaultdict\n3. Calculate average, min, max per course\n4. Find the course with highest average",
    "starterCode": "from collections import defaultdict\n\nrecords = [\n    ('Python', 92), ('SQL', 78), ('Python', 85),\n    ('AI', 95), ('SQL', 82), ('Python', 88),\n    ('AI', 90), ('SQL', 75), ('AI', 92),\n]\n\n# Group by course\ngrouped = defaultdict(___)\nfor course, score in records:\n    grouped[course].___(score)\n\n# Analyze each course\nresults = {}\nfor course, scores in grouped.items():\n    results[course] = {\n        'avg': sum(scores) / len(___),\n        'min': min(___),\n        'max': max(___),\n        'count': len(scores)\n    }\n    r = results[course]\n    print(f\"{course:10} avg={r['avg']:.1f}  min={r['min']}  max={r['max']}  n={r['count']}\")\n\n# Best course\nbest = max(results.items(), key=lambda x: x[1][___])\nprint(f'\\nHighest avg: {best[0]} ({best[1][\"avg\"]:.1f})')",
    "solution": "from collections import defaultdict\nrecords=[('Python',92),('SQL',78),('Python',85),('AI',95),('SQL',82),('Python',88),('AI',90),('SQL',75),('AI',92)]\ngrouped=defaultdict(list)\nfor course,score in records:grouped[course].append(score)\nresults={}\nfor course,scores in grouped.items():\n    results[course]={'avg':sum(scores)/len(scores),'min':min(scores),'max':max(scores),'count':len(scores)}\n    r=results[course]\n    print(f\"{course:10} avg={r['avg']:.1f} min={r['min']} max={r['max']} n={r['count']}\")\nbest=max(results.items(),key=lambda x:x[1]['avg'])\nprint(f'\\nHighest avg: {best[0]} ({best[1][\"avg\"]:.1f})')",
    "hint": "defaultdict(list) creates auto-lists. .append() to add. max() with key for best course.",
    "rubric": "defaultdict grouping. Append scores. Stats per course. max() finds best average."
  },
  {
    "title": "Simple Data Visualization (Text-Based)",
    "theory": "## Text Charts\nVisualize data without external libraries!\n```python\n# Bar chart\ndata = {'Python': 45, 'SQL': 30, 'AI': 55}\nmax_val = max(data.values())\n\nfor label, value in data.items():\n    bar_len = int(value / max_val * 40)\n    bar = '█' * bar_len\n    print(f'{label:10} {bar} {value}')\n\n# Sparkline\nvalues = [3, 7, 2, 8, 5]\nchars = ' ▁▂▃▄▅▆▇█'\nfor v in values:\n    idx = int(v / max(values) * 8)\n    print(chars[idx], end='')\n```",
    "instructions": "## Task: Score Distribution Chart\n1. Given student scores, create a frequency distribution\n2. Bucket scores into ranges (0-59, 60-69, 70-79, 80-89, 90-100)\n3. Display a horizontal bar chart using block characters\n4. Show the percentage for each range",
    "starterCode": "scores = [92, 78, 85, 45, 68, 95, 72, 88, 55, 90, 82, 76, 91, 63, 87]\n\n# Define buckets\nbuckets = {'90-100': 0, '80-89': 0, '70-79': 0, '60-69': 0, '0-59': 0}\n\nfor score in scores:\n    if score >= 90: buckets['90-100'] += 1\n    elif score >= 80: buckets['___'] += 1\n    elif score >= ___: buckets['70-79'] += 1\n    elif score >= ___: buckets['60-69'] += 1\n    else: buckets['0-59'] += 1\n\ntotal = len(scores)\nmax_count = max(buckets.___())\n\nprint('=== Score Distribution ===')\nfor label, count in buckets.items():\n    bar_len = int(count / max_count * 30) if max_count > 0 else 0\n    bar = '█' * bar_len\n    pct = count / ___ * 100\n    print(f'{label:8} | {bar:30} {count} ({pct:.0f}%)')",
    "solution": "scores=[92,78,85,45,68,95,72,88,55,90,82,76,91,63,87]\nbuckets={'90-100':0,'80-89':0,'70-79':0,'60-69':0,'0-59':0}\nfor score in scores:\n    if score>=90:buckets['90-100']+=1\n    elif score>=80:buckets['80-89']+=1\n    elif score>=70:buckets['70-79']+=1\n    elif score>=60:buckets['60-69']+=1\n    else:buckets['0-59']+=1\ntotal=len(scores)\nmax_count=max(buckets.values())\nprint('=== Score Distribution ===')\nfor label,count in buckets.items():\n    bar_len=int(count/max_count*30) if max_count>0 else 0\n    bar='█'*bar_len\n    pct=count/total*100\n    print(f'{label:8} | {bar:30} {count} ({pct:.0f}%)')",
    "hint": "Bucket with if/elif chain. max(buckets.values()) for scaling. count/total*100 for percentage.",
    "rubric": "5 score buckets. Correct bucketing logic. Bar chart with blocks. Percentages shown."
  }
],

}

# ══════════════════════════════════════════════════════
# INJECTION ENGINE
# ══════════════════════════════════════════════════════

def inject_lessons(filepath, new_lessons):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    injected = 0
    skipped = 0
    
    for course_name, lessons in new_lessons.items():
        # Find the course's lessons array closing bracket
        # Pattern: "Course Name": { "aiRubric": "...", "lessons": [ ... ] }
        course_pos = content.find(f'"{course_name}"')
        if course_pos == -1:
            print(f'  SKIP: "{course_name}" not found in file')
            skipped += 1
            continue
        
        # Find the "lessons" array for this course
        lessons_key = content.find('"lessons"', course_pos)
        if lessons_key == -1:
            print(f'  SKIP: No "lessons" key for "{course_name}"')
            skipped += 1
            continue
        
        # Find the opening bracket of lessons array
        bracket_start = content.find('[', lessons_key)
        if bracket_start == -1:
            skipped += 1
            continue
        
        # Find the matching closing bracket
        depth = 0
        bracket_end = -1
        for i in range(bracket_start, min(bracket_start + 100000, len(content))):
            if content[i] == '[':
                depth += 1
            elif content[i] == ']':
                depth -= 1
                if depth == 0:
                    bracket_end = i
                    break
        
        if bracket_end == -1:
            print(f'  SKIP: Could not find closing bracket for "{course_name}"')
            skipped += 1
            continue
        
        # Generate the JSON for new lessons
        new_entries = ''
        for lesson in lessons:
            lesson_json = json.dumps(lesson, ensure_ascii=False)
            new_entries += ',\n      ' + lesson_json
        
        # Insert before the closing bracket
        content = content[:bracket_end] + new_entries + '\n    ' + content[bracket_end:]
        injected += len(lessons)
        print(f'  OK: Added {len(lessons)} lessons to "{course_name}"')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'\n=== SUMMARY ===')
    print(f'Injected: {injected} new lessons')
    print(f'Skipped:  {skipped} courses')
    return injected

if __name__ == '__main__':
    filepath = 'frontend/src/data/courses.js'
    print(f'Expanding courses in: {filepath}')
    print(f'Courses to expand: {len(NEW_LESSONS)}')
    print(f'Total new lessons: {sum(len(v) for v in NEW_LESSONS.values())}')
    print()
    inject_lessons(filepath, NEW_LESSONS)
