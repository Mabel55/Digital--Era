"""
enrich_python_core.py
Manually patches rich, detailed theory into curriculum/tracks/python_core.json
"""
import json, os

TRACK_FILE = os.path.join("curriculum", "tracks", "python_core.json")

RICH_THEORY = {

# ════════════════════════════════════════════════
# PYTHON BASICS
# ════════════════════════════════════════════════

"Variables & Data Types": """## What is a Variable?

Think of a variable like a **labelled box** in your bedroom. The label is the variable name (e.g., `name`), and whatever you put inside the box is the value (e.g., `'Alice'`). You can always open the box, take out what's inside, change it, or replace it entirely.

In Python, you don't need to declare a type before creating a variable — Python automatically figures out what type of data is inside the box just by looking at what you assign.

### The Four Main Data Types

```python
# A string (str) holds text — always wrapped in quotes
name = 'Alice'         # Single quotes work
greeting = "Hello!"    # Double quotes also work

# An integer (int) holds whole numbers — no decimal point
age = 25
year = 2024

# A float holds decimal/fractional numbers
height = 5.6
price = 19.99

# A boolean (bool) holds one of two values: True or False
is_student = True
has_graduated = False
```

### How Python Knows the Type

Python uses the assigned value to determine the type automatically. This is called **dynamic typing**. You can check the type of any variable using the built-in `type()` function:

```python
name = 'Alice'
print(type(name))      # <class 'str'>

age = 25
print(type(age))       # <class 'int'>

height = 5.6
print(type(height))    # <class 'float'>

is_student = True
print(type(is_student)) # <class 'bool'>
```

### Naming Rules for Variables

- Must start with a letter or underscore (`_`), NOT a number
- Can contain letters, numbers, and underscores
- Case-sensitive: `Name` and `name` are two different variables
- Use **snake_case** by convention: `student_name`, `total_price`

```python
# ✅ Good variable names
student_name = 'Bob'
total_price = 49.99
is_active = True
_private = 'hidden'

# ❌ Bad variable names
2fast = 'no'       # Can't start with number
my-var = 'no'      # Hyphens not allowed
class = 'no'       # Reserved Python keyword
```

### Printing Variables with f-Strings

An **f-string** (formatted string literal) lets you embed variable values directly inside a string. Just put an `f` before the opening quote and use `{variable_name}` anywhere inside:

```python
name = 'Mabel'
age = 20
gpa = 3.8

# The f before the quote makes it an f-string
print(f'My name is {name}')                      # My name is Mabel
print(f'I am {age} years old')                   # I am 20 years old
print(f'Name: {name}, Age: {age}, GPA: {gpa}')   # Name: Mabel, Age: 20, GPA: 3.8
```

**Key Rule:** The quotes around strings and the curly braces `{}` in f-strings are two different things. Don't confuse them!""",

# ────────────────────────────────────────────────

"String Operations": """## What is a String?

A **string** is a sequence of characters — letters, numbers, spaces, punctuation — stored as text. You can think of it like a chain of beads, where each bead is one character. Python gives you a rich toolbox of built-in **methods** to manipulate strings.

### Creating Strings

```python
# Single or double quotes — both work the same
message = 'Hello, World!'
greeting = "Good morning!"

# Triple quotes for multi-line strings
essay = \"\"\"
This is line one.
This is line two.
This is line three.
\"\"\"
```

### Essential String Methods

Every string has methods built right into it. You call them with a dot: `string.method_name()`.

```python
msg = 'hello world'

# .upper() — converts every character to uppercase
print(msg.upper())          # HELLO WORLD

# .lower() — converts every character to lowercase
print(msg.lower())          # hello world

# .title() — capitalizes the first letter of each word
print(msg.title())          # Hello World

# .capitalize() — only capitalizes the very first letter
print(msg.capitalize())     # Hello world

# .strip() — removes whitespace from both ends
padded = '   hello   '
print(padded.strip())       # 'hello'

# .replace(old, new) — swaps one piece of text for another
print(msg.replace('world', 'Python'))  # hello Python

# len() — returns the number of characters (a function, not a method)
print(len(msg))             # 11
```

### Slicing: Cutting Out Pieces of a String

Strings are **indexed** — every character has a numbered position starting from 0.

```
H  e  l  l  o     W  o  r  l  d  !
0  1  2  3  4  5  6  7  8  9  10 11
```

You can extract a portion using **slice notation** `[start:stop]`. The `stop` index is **not included**.

```python
msg = 'Hello World!'

print(msg[0])       # 'H'     — single character at index 0
print(msg[0:5])     # 'Hello' — characters 0, 1, 2, 3, 4 (5 not included)
print(msg[6:])      # 'World!' — from index 6 to the end
print(msg[:5])      # 'Hello' — from the start up to index 5
print(msg[-1])      # '!'     — last character (-1 counts from the end)
print(msg[-6:])     # 'World!' — last 6 characters
```

### Checking if Text is Inside a String

```python
sentence = 'python is amazing'

# The 'in' keyword checks membership
print('python' in sentence)   # True
print('java' in sentence)     # False
print('is' in sentence)       # True
```

### Joining and Splitting

```python
# split() — breaks a string into a list of words
words = 'apple,banana,cherry'.split(',')
print(words)    # ['apple', 'banana', 'cherry']

# join() — sticks a list of strings together with a separator
fruits = ['apple', 'banana', 'cherry']
result = ', '.join(fruits)
print(result)   # 'apple, banana, cherry'
```

**Golden Rule:** Strings in Python are **immutable** — you can't change a character in place. Every string method returns a *new* string; the original stays the same.""",

# ────────────────────────────────────────────────

"Type Conversion": """## Why Do Types Matter?

Python is strict about data types — you cannot do math with text, and you cannot mix incompatible types without a crash. **Type conversion** (also called **type casting**) is the process of converting a value from one type to another.

### The Problem

```python
age_text = '25'         # This is a string — the text "25"
age_number = 25         # This is an integer — the number 25

# Trying to add them causes a TypeError:
# print(age_text + age_number)  # ❌ TypeError: can only concatenate str to str

# You must convert first:
print(age_text + str(age_number))   # '2525' — string concatenation
print(int(age_text) + age_number)   # 50   — integer addition
```

### The Four Conversion Functions

| Function | Converts To | Example |
|---|---|---|
| `int(x)` | Integer (whole number) | `int('42')` → `42` |
| `float(x)` | Float (decimal number) | `float('3.14')` → `3.14` |
| `str(x)` | String (text) | `str(100)` → `'100'` |
| `bool(x)` | Boolean (True/False) | `bool(0)` → `False` |

### Examples

```python
# String → Integer
age_str = '25'
age_int = int(age_str)
print(age_int)          # 25
print(type(age_int))    # <class 'int'>

# String → Float
price_str = '19.99'
price_float = float(price_str)
print(price_float)      # 19.99

# Integer → String
num = 42
num_str = str(num)
print(num_str)          # '42'
print(type(num_str))    # <class 'str'>

# Float → Integer (TRUNCATES — removes the decimal, does NOT round)
pi = 3.99
whole = int(pi)
print(whole)            # 3  (NOT 4! It just removes the decimal part)
```

### Boolean Conversion — What is "Truthy" and "Falsy"?

In Python, almost any value can be evaluated as True or False:

```python
# These values are FALSY (convert to False):
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(''))      # False — empty string
print(bool([]))      # False — empty list
print(bool(None))    # False

# These values are TRUTHY (convert to True):
print(bool(1))       # True
print(bool(-99))     # True — any non-zero number
print(bool('hello')) # True — any non-empty string
print(bool([1, 2]))  # True — any non-empty list
```

### Critical Gotcha: input() Always Returns a String

When a user types something, Python receives it as a string. You must convert it:

```python
age = input('Enter your age: ')  # Returns '25' — a string!
print(type(age))                 # <class 'str'>

# To use it as a number:
age = int(input('Enter your age: '))
print(age + 1)                   # Works!
```""",

# ────────────────────────────────────────────────

"Basic Operators": """## Operators: The Verbs of Programming

Operators are symbols that tell Python to perform an operation on values. There are three main families you need to master first.

### 1. Arithmetic Operators — Math

```python
a = 17
b = 5

print(a + b)    # 22  — Addition
print(a - b)    # 12  — Subtraction
print(a * b)    # 85  — Multiplication
print(a / b)    # 3.4 — Division (always gives a float!)
print(a // b)   # 3   — Floor Division (divides and rounds DOWN)
print(a % b)    # 2   — Modulus (gives the REMAINDER after division)
print(a ** b)   # 1419857 — Exponentiation (17 to the power of 5)
```

**Understanding Floor Division and Modulus:** These are extremely useful. Imagine dividing 17 cookies among 5 people:
- Each person gets **3** cookies → that's floor division `17 // 5 = 3`
- There are **2** cookies left over → that's modulus `17 % 5 = 2`

```python
# A classic use of modulus: checking if a number is even or odd
print(10 % 2)   # 0  — no remainder = EVEN
print(7 % 2)    # 1  — has remainder = ODD

# Order of operations follows PEMDAS/BODMAS
result = 2 + 3 * 4    # 14, not 20 (multiplication first)
result = (2 + 3) * 4  # 20 (parentheses first)
```

### 2. Comparison Operators — Making Decisions

Comparison operators **always return True or False**. They are the heart of all conditional logic.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | True |
| `!=` | Not equal to | `5 != 3` | True |
| `>` | Greater than | `7 > 3` | True |
| `<` | Less than | `3 < 7` | True |
| `>=` | Greater than or equal | `5 >= 5` | True |
| `<=` | Less than or equal | `4 <= 5` | True |

```python
score = 85
print(score >= 90)    # False — 85 is NOT >= 90
print(score > 80)     # True  — 85 IS > 80
print(score == 85)    # True  — 85 IS equal to 85
print(score != 100)   # True  — 85 is NOT 100
```

⚠️ **Critical Warning:** `=` assigns a value. `==` **compares** two values. They are completely different!

```python
x = 10       # Assigns the number 10 to x
x == 10      # Checks if x equals 10, returns True
```

### 3. Assignment Operators — Shorthand Math

These combine assignment with an operation:

```python
count = 0

count += 1    # Same as: count = count + 1  → count is now 1
count += 5    # count is now 6
count -= 2    # count is now 4
count *= 3    # count is now 12
count //= 5   # count is now 2
count **= 3   # count is now 8

print(count)  # 8
```

### 4. Logical Operators — Combining Conditions

```python
age = 20
has_id = True

# 'and' — BOTH conditions must be True
print(age >= 18 and has_id)    # True

# 'or' — AT LEAST ONE condition must be True
print(age < 18 or has_id)     # True

# 'not' — flips True to False, and False to True
print(not has_id)              # False
```""",

# ════════════════════════════════════════════════
# CONTROL FLOW
# ════════════════════════════════════════════════

"While Loops": """## What is a While Loop?

A **while loop** is like a bouncer at a club. It checks a condition at the door. If the condition is True, the person (code block) gets in and runs. After it's done, it comes back to the bouncer. This keeps repeating until the condition becomes False — only then does the loop stop.

This is the key difference from a `for` loop:
- **for loop** — you know exactly how many times to repeat
- **while loop** — you keep going until *something happens* to make you stop

### Basic Syntax

```python
# Format:
# while condition:
#     code block (must be indented 4 spaces)

count = 0               # 1. Start: the loop variable begins here

while count < 5:        # 2. Check: is count less than 5?
    print(count)        # 3. Run: this code executes if True
    count += 1          # 4. Update: change the condition variable!
                        #    Then go back to step 2 and check again.

# Output: 0, 1, 2, 3, 4
```

⚠️ **The #1 Mistake: Forgetting to Update the Variable**

If you forget `count += 1`, the condition `count < 5` will ALWAYS be True and the loop will run forever! This is called an **infinite loop** and will crash or freeze your program.

```python
# ❌ INFINITE LOOP — never do this!
count = 0
while count < 5:
    print(count)
    # Missing: count += 1
```

### Breaking Out of a Loop with `break`

Sometimes you want to exit a loop early based on some event — even before the condition becomes False:

```python
# Keep asking for input until the user types 'quit'
while True:                          # 'while True' runs forever by design
    user_input = input('> ')
    if user_input == 'quit':
        print('Goodbye!')
        break                        # Exit the loop immediately
    print(f'You typed: {user_input}')
```

### Skipping an Iteration with `continue`

`continue` skips the rest of the current iteration and jumps back to the condition check:

```python
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:    # If the number is even...
        continue      # ...skip printing it and go back to the check
    print(i)          # Only prints odd numbers: 1, 3, 5, 7, 9
```

### Real-World Patterns

```python
# Pattern 1: Countdown
countdown = 10
while countdown > 0:
    print(f'{countdown}...')
    countdown -= 1
print('Liftoff! 🚀')

# Pattern 2: Input validation — keep asking until valid
age = -1
while age < 0 or age > 150:
    age = int(input('Enter a valid age (0-150): '))
print(f'Your age: {age}')

# Pattern 3: Processing a list (when you need to remove items)
tasks = ['email', 'meeting', 'code review']
while tasks:              # An empty list is False, so this stops automatically
    task = tasks.pop(0)   # Remove and get the first task
    print(f'Doing: {task}')
print('All done!')
```""",

# ────────────────────────────────────────────────

"Break & Continue": """## Controlling the Flow Inside Loops

Python gives you two special keywords to change what happens during a loop iteration: `break` and `continue`. Together with loops, they give you precise control over your program's execution.

### `break` — Emergency Exit

`break` **immediately stops the loop** and jumps to the first line of code after it. Think of it like pulling an emergency stop lever on a train — it halts everything right away, regardless of what the loop condition says.

```python
# Searching for a target in a list
numbers = [4, 17, 3, 28, 9, 42, 11]
target = 28

for num in numbers:
    print(f'Checking {num}...')
    if num == target:
        print(f'Found {target}!')
        break           # Stop searching — no need to check the rest
    
print('Search complete.')
# Output:
# Checking 4...
# Checking 17...
# Checking 3...
# Checking 28...
# Found 28!
# Search complete.
```

Notice: `9`, `42`, and `11` are never checked because `break` exited the loop as soon as the target was found. This makes code much more efficient.

### `continue` — Skip and Keep Going

`continue` **skips the rest of the current iteration** and immediately goes back to the loop condition check. The loop itself continues — only the current round is cut short.

```python
# Print only even numbers
for num in range(1, 11):
    if num % 2 != 0:   # If the number is ODD...
        continue        # ...skip it and go to the next iteration
    print(num)          # Only runs for even numbers

# Output: 2, 4, 6, 8, 10
```

### Side-by-Side Comparison

```python
# Using break — stops at 5
for i in range(1, 11):
    if i == 5:
        break           # Loop ends here
    print(i)
# Output: 1, 2, 3, 4

# Using continue — skips 5
for i in range(1, 11):
    if i == 5:
        continue        # Just skips this one, loop continues
    print(i)
# Output: 1, 2, 3, 4, 6, 7, 8, 9, 10
```

### `break` in While Loops

`break` is especially useful in `while True` loops, which are designed to run until *you* decide to stop them:

```python
import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input('Guess (1-10): '))
    attempts += 1
    
    if guess < secret:
        print('Too low!')
    elif guess > secret:
        print('Too high!')
    else:
        print(f'Correct! You got it in {attempts} attempts.')
        break   # Exit the while loop
```

### Combining Both

```python
# Process a list but skip invalid entries and stop on error
data = [10, 25, -5, 30, 'ERROR', 15, 8]

total = 0
for item in data:
    if item == 'ERROR':
        print('Encountered error — stopping.')
        break                   # Stop entirely
    if item < 0:
        print(f'Skipping negative: {item}')
        continue                # Skip this item
    total += item
    print(f'Added {item}, total = {total}')

print(f'Final total: {total}')
```

**Mental Model:**
- `break` = "I'm done with the whole loop"
- `continue` = "I'm done with *this round* of the loop, start the next one" """,

# ────────────────────────────────────────────────

"Nested Loops": """## Loops Inside Loops

A **nested loop** is simply a loop placed inside another loop. The inner loop runs **completely** for each single iteration of the outer loop. Think of it like a clock: for every 1 hour the hour hand moves, the minute hand goes around all 60 minutes.

### Basic Structure

```python
for outer in range(3):          # Outer loop: runs 3 times
    for inner in range(4):      # Inner loop: runs 4 times per outer
        print(f'outer={outer}, inner={inner}')
    print('--- Inner loop finished ---')

# The inner loop runs a total of 3 × 4 = 12 times
```

### Building a Times Table

Nested loops are perfect for anything grid-like or 2D:

```python
# Print a 5x5 multiplication table
for row in range(1, 6):         # Row numbers: 1 to 5
    for col in range(1, 6):     # Column numbers: 1 to 5
        result = row * col
        # end='\t' prints a tab instead of a newline (keeps it on the same line)
        print(result, end='\t')
    print()   # This print() moves to the next line after each row

# Output:
# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25
```

### Drawing Patterns

```python
# Right triangle of stars
rows = 5
for i in range(1, rows + 1):   # i goes from 1 to 5
    for j in range(i):          # j goes from 0 to i-1 (prints i stars)
        print('*', end=' ')
    print()                     # New line after each row

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

### Nested Loops with Lists

The most common real-world use is working with **2D data** (lists of lists, like a spreadsheet):

```python
# A classroom of students with their grades
classroom = [
    ['Alice', 90, 85, 92],   # Each row: name, then grades
    ['Bob',   78, 82, 88],
    ['Carol', 95, 91, 87],
]

for student in classroom:           # Outer: each student (row)
    name = student[0]               # First element is the name
    grades = student[1:]            # Remaining elements are grades
    
    total = 0
    for grade in grades:            # Inner: each grade for this student
        total += grade
    
    average = total / len(grades)
    print(f'{name}: average = {average:.1f}')

# Output:
# Alice: average = 89.0
# Bob: average = 82.7
# Carol: average = 91.0
```

### Performance Warning

Be careful with deep nesting. Each extra level **multiplies** the total work:
- 1 loop with 1000 items → 1,000 operations
- 2 nested loops of 1000 each → 1,000,000 operations  
- 3 nested loops of 1000 each → 1,000,000,000 operations (too slow!)

**Rule of Thumb:** If you find yourself nesting more than 2-3 loops deep, consider whether there's a cleaner solution.""",

# ════════════════════════════════════════════════
# FUNCTIONS
# ════════════════════════════════════════════════

"Return Values": """## Functions Are Two-Way Conversations

When you call a function, you're starting a conversation: you send in data (arguments), and the function sends data back to you (a return value). The `return` keyword is what sends data back.

Without `return`, a function does its work but doesn't give you anything back — it returns `None` by default.

### The Difference Between print() and return

This is the #1 point of confusion for beginners:

```python
# This function only PRINTS — it doesn't give anything back
def greet_print(name):
    print(f'Hello, {name}!')   # Output goes to the screen

# This function RETURNS — it gives a value back to the caller
def greet_return(name):
    return f'Hello, {name}!'   # Value goes back to the caller

# Using the functions:
greet_print('Alice')           # Works — prints to screen
message = greet_print('Alice') # Works, but message = None!

result = greet_return('Alice') # Works — result = 'Hello, Alice!'
print(result)                  # We can print it, pass it elsewhere, etc.
```

Use `return` when you need to **use the result elsewhere** in your program.

### Returning a Single Value

```python
def square(num):
    return num ** 2            # Returns the computed value

result = square(7)             # result = 49
print(square(4) + square(3))  # 16 + 9 = 25 — can use directly in expressions
```

### Returning Multiple Values

Python allows returning multiple values at once — they come back as a **tuple**:

```python
def get_dimensions():
    width = 1920
    height = 1080
    return width, height       # Returns a tuple: (1920, 1080)

# Unpack the tuple into separate variables:
w, h = get_dimensions()
print(f'Width: {w}, Height: {h}')   # Width: 1920, Height: 1080

# You can also receive it as a single tuple:
dimensions = get_dimensions()
print(dimensions)               # (1920, 1080)
print(dimensions[0])            # 1920
```

### A Practical Example: analyze() Function

```python
def analyze(numbers):
    \"\"\"
    Takes a list of numbers and returns key statistics.
    Returns: (minimum, maximum, average)
    \"\"\"
    if not numbers:             # Guard against empty list
        return None, None, None
    
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    
    return minimum, maximum, average   # Return all three

# Using the function
data = [10, 20, 30, 40, 50]
lo, hi, avg = analyze(data)
print(f'Min: {lo}, Max: {hi}, Avg: {avg}')
# Min: 10, Max: 50, Avg: 30.0
```

### Early Return (Guard Clauses)

You can `return` from anywhere inside a function. This is useful for handling edge cases early:

```python
def divide(a, b):
    # Guard clause — exit early if invalid input
    if b == 0:
        return None   # Can't divide by zero

    return a / b       # Only reaches here if b is not 0

result = divide(10, 2)
print(result)    # 5.0

result = divide(10, 0)
print(result)    # None
```

**Golden Rule:** Once Python hits a `return` statement, it immediately exits the function. Any code after `return` is never executed.""",

# ────────────────────────────────────────────────

"Lambda Functions": """## What is a Lambda?

A **lambda function** is a small, anonymous (unnamed) function defined in a single line. "Anonymous" means it doesn't have a `def` name — it's a throwaway function for simple, one-off operations.

### Syntax Comparison

```python
# Standard function (has a name, multiple lines possible)
def square(x):
    return x ** 2

# Lambda (anonymous, single expression only)
square = lambda x: x ** 2

# Both do exactly the same thing:
print(square(5))   # 25
```

The lambda syntax: `lambda parameters: expression`
- `lambda` — the keyword
- `parameters` — comma-separated inputs (like function arguments)
- `:` — separates parameters from the expression
- `expression` — a single expression that is automatically returned

### When NOT to Use Lambda

If you need more than one line, use a regular `def`:

```python
# ❌ Don't try to squeeze multi-line logic into a lambda
# ✅ Use a regular function for anything complex

def process(x):
    if x > 0:
        return x * 2
    return 0
```

### The Real Power: Using Lambdas with Built-ins

Lambdas shine when passed as arguments to functions like `sorted()`, `map()`, and `filter()`.

#### `sorted()` with a Custom Key

```python
students = [
    {'name': 'Alice', 'gpa': 3.5},
    {'name': 'Bob',   'gpa': 3.9},
    {'name': 'Carol', 'gpa': 3.1},
]

# Sort by GPA (ascending)
by_gpa = sorted(students, key=lambda s: s['gpa'])
for s in by_gpa:
    print(s['name'], s['gpa'])
# Carol 3.1, Alice 3.5, Bob 3.9

# Sort by GPA (descending)
by_gpa_desc = sorted(students, key=lambda s: s['gpa'], reverse=True)
```

#### `map()` — Apply a Function to Every Item

```python
numbers = [1, 2, 3, 4, 5]

# map() applies the lambda to every element and returns a map object
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8, 10]

# Equivalent using a list comprehension (often preferred):
doubled = [x * 2 for x in numbers]
```

#### `filter()` — Keep Items That Match a Condition

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() keeps only items where the lambda returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]

odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)    # [1, 3, 5, 7, 9]
```

### Multiple Parameters

```python
add = lambda x, y: x + y
print(add(3, 7))   # 10

clamp = lambda val, lo, hi: max(lo, min(val, hi))
print(clamp(150, 0, 100))   # 100 — clamps 150 to the range [0, 100]
```

**Summary:** Use lambdas for short, simple operations that would be overkill to write a whole `def` for — especially as arguments to sorting and filtering functions.""",

# ────────────────────────────────────────────────

"Scope & Global Variables": """## What is Scope?

**Scope** is the concept of *where in your code a variable is accessible*. Think of it like rooms in a house — if you put something in your bedroom, it's only accessible there. You can't grab it from the kitchen.

Python has two main scopes:
- **Local scope** — inside a function (the bedroom)
- **Global scope** — at the top level of the file (the whole house)

### Local Scope — Variables Created Inside Functions

```python
def my_function():
    message = 'Hello!'    # LOCAL variable — only exists inside my_function
    print(message)

my_function()             # Hello!
# print(message)          # ❌ NameError! 'message' doesn't exist out here
```

### Global Scope — Variables at the Top Level

```python
name = 'Alice'            # GLOBAL variable — accessible everywhere

def greet():
    print(f'Hello, {name}!')   # Functions can READ global variables

greet()                   # Hello, Alice!
print(name)               # Hello, Alice!
```

### The Shadowing Problem

If you create a variable with the same name inside a function as one outside, Python creates a **new local variable** — it does NOT modify the global one:

```python
count = 100               # Global count

def reset():
    count = 0             # This creates a NEW local variable called count
    print(f'Inside: {count}')   # 0 — the local one

reset()
print(f'Outside: {count}')     # 100 — the global one is untouched!
```

### The `global` Keyword — When You Need to Modify a Global

If you genuinely need to modify a global variable from inside a function, declare it with the `global` keyword:

```python
total_score = 0            # Global variable

def add_points(points):
    global total_score     # "I want to use the GLOBAL total_score, not create a new one"
    total_score += points  # Now this modifies the global variable

add_points(10)
add_points(25)
add_points(5)
print(total_score)         # 40
```

⚠️ **Design Advice:** Using `global` is generally considered bad practice for large programs because it creates hidden dependencies. The better design is to **return** the new value from the function and reassign it:

```python
# ✅ Better approach — no global needed
def add_points(score, points):
    return score + points  # Return the new value

total_score = 0
total_score = add_points(total_score, 10)
total_score = add_points(total_score, 25)
print(total_score)   # 35
```

### The LEGB Rule

Python searches for variables in this order:
1. **L**ocal — the current function
2. **E**nclosing — any outer functions (for nested functions)
3. **G**lobal — the top level of the module
4. **B**uilt-ins — Python's built-in names like `print`, `len`, `range`

```python
x = 'global'

def outer():
    x = 'enclosing'
    
    def inner():
        # x = 'local'  # If this existed, it would take priority
        print(x)       # Finds 'enclosing' before reaching 'global'
    
    inner()

outer()   # enclosing
```""",

# ────────────────────────────────────────────────

"Recursion": """## What is Recursion?

**Recursion** is when a function solves a problem by calling itself with a smaller version of the same problem. It's a different way of thinking about repetition — instead of using a loop, you break the problem into smaller and smaller pieces until you reach a piece so simple it answers itself.

### The Two Required Parts

Every recursive function MUST have:
1. **A base case** — the simplest scenario that can be solved directly (no further recursion needed). This stops the recursion.
2. **A recursive case** — where the function calls itself with a *smaller/simpler* version of the problem.

Without a base case, the function calls itself forever → stack overflow crash!

### The Classic Example: Factorial

`factorial(5)` = 5 × 4 × 3 × 2 × 1 = 120

```python
def factorial(n):
    # Base case: factorial(0) = 1 and factorial(1) = 1
    if n <= 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(1))   # 1
```

**How it works step by step:**
```
factorial(5)
  = 5 * factorial(4)
  = 5 * 4 * factorial(3)
  = 5 * 4 * 3 * factorial(2)
  = 5 * 4 * 3 * 2 * factorial(1)
  = 5 * 4 * 3 * 2 * 1        ← base case hit!
  = 120
```

### Fibonacci Sequence

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...
Each number is the sum of the two before it.

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(11):
    print(f'fib({i}) = {fibonacci(i)}')
# fib(0) = 0, fib(1) = 1, fib(2) = 1, ..., fib(10) = 55
```

### Visualizing the Call Stack

When you call `fibonacci(4)`, Python keeps a stack of all active function calls:

```
fibonacci(4)
├── fibonacci(3)
│   ├── fibonacci(2)
│   │   ├── fibonacci(1) → 1  (base case)
│   │   └── fibonacci(0) → 0  (base case)
│   │   returns 1
│   └── fibonacci(1) → 1  (base case)
│   returns 2
└── fibonacci(2)
    ├── fibonacci(1) → 1
    └── fibonacci(0) → 0
    returns 1
= 3
```

### When to Use Recursion

Recursion is natural for problems that have a **self-similar structure**:
- Tree traversal (file systems, HTML parsing)
- Maze solving
- Mathematical sequences (factorial, Fibonacci)
- Divide and conquer algorithms (merge sort, quicksort)

**Important:** Python has a default recursion limit of ~1000 calls. For very deep recursion, use an iterative (loop-based) approach instead. For most beginner use cases, recursion is perfectly fine.""",

# ════════════════════════════════════════════════
# DATA STRUCTURES
# ════════════════════════════════════════════════

"List Comprehensions": """## The Pythonic Way to Create Lists

A **list comprehension** is a compact, readable way to create a new list by applying an expression to each item in an existing sequence — all in a single line. It's one of the most loved features of Python.

### The Basic Pattern

```python
# Standard loop (verbose):
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension (compact):
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Format:** `[expression for item in iterable]`
- `expression` — what to compute/transform for each item
- `for item in iterable` — the loop that provides each item

### Adding a Condition (Filtering)

Add an `if` at the end to only include items that match:

```python
# Format: [expression for item in iterable if condition]

# Only even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Only strings longer than 4 characters
words = ['hi', 'hello', 'hey', 'howdy', 'ok']
long_words = [w for w in words if len(w) > 4]
# ['hello', 'howdy']

# Grades above 70
grades = [55, 80, 72, 45, 91, 68]
passing = [g for g in grades if g >= 70]
# [80, 72, 91]
```

### Transforming Items

The expression can be any valid Python expression:

```python
# Convert to uppercase
names = ['alice', 'bob', 'carol']
upper = [name.upper() for name in names]
# ['ALICE', 'BOB', 'CAROL']

# Get word lengths
lengths = [len(name) for name in names]
# [5, 3, 5]

# Apply a function
import math
roots = [round(math.sqrt(n), 2) for n in [4, 9, 16, 25]]
# [2.0, 3.0, 4.0, 5.0]
```

### Both Together: Transform AND Filter

```python
# Get doubled values of even numbers only
numbers = range(1, 11)
result = [x * 2 for x in numbers if x % 2 == 0]
# [4, 8, 12, 16, 20]

# Get names in uppercase only if they start with 'A'
names = ['Alice', 'Bob', 'Anna', 'Charlie', 'Amy']
a_names = [n.upper() for n in names if n.startswith('A')]
# ['ALICE', 'ANNA', 'AMY']
```

### Nested List Comprehensions (2D)

```python
# Flatten a 2D list into a 1D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table as a 2D list
table = [[row * col for col in range(1, 6)] for row in range(1, 6)]
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10], ...]
```

### When to Use vs. When to Use a Regular Loop

✅ **Use a list comprehension when:**
- The logic is simple (one line of expression)
- You are creating a list from another sequence

❌ **Use a regular loop when:**
- The logic is complex (multiple statements)
- You have side effects (e.g., printing, modifying external state)
- Readability suffers""",

# ────────────────────────────────────────────────

"Tuples & Sets": """## Tuples — Immutable Ordered Sequences

A **tuple** is like a list, but frozen — once you create it, you cannot change its contents. It's perfect for data that should never be modified: coordinates, RGB colours, database records.

### Creating Tuples

```python
# Created with parentheses (or just commas)
coordinates = (10, 20)
rgb_red = (255, 0, 0)
person = ('Alice', 25, 'Lagos')

# A tuple with one element MUST have a trailing comma:
single = (42,)          # This is a tuple
not_tuple = (42)        # This is just the number 42
```

### Accessing Tuple Items

Just like lists — indexed from 0:

```python
point = (3, 7, -2)
print(point[0])     # 3
print(point[-1])    # -2
print(point[1:])    # (7, -2)
```

### Tuple Unpacking — A Python Superpower

You can assign each element of a tuple to a separate variable in one line:

```python
point = (10, 20)
x, y = point          # Unpacking — x=10, y=20
print(f'x={x}, y={y}')

# Swap variables without a temp variable:
a = 5
b = 10
a, b = b, a           # Python creates a tuple (10, 5) then unpacks it
print(a, b)           # 10 5

# Unpack from function return values:
def get_minmax(numbers):
    return min(numbers), max(numbers)   # Returns a tuple

low, high = get_minmax([3, 1, 7, 2, 9])
print(f'Min: {low}, Max: {high}')   # Min: 1, Max: 9
```

### Why Use Tuples Instead of Lists?

1. **Safety** — immutability prevents accidental modification
2. **Performance** — tuples are slightly faster to create and access
3. **Dictionary keys** — tuples can be used as dict keys, lists cannot
4. **Semantic meaning** — signals "this data should not change"

---

## Sets — Unordered Collections of Unique Items

A **set** is a collection that automatically eliminates duplicates. It's like a bag where you can only have one of each item. Sets are **unordered** — there is no first, second, or third element.

### Creating Sets

```python
# Created with curly braces
fruits = {'apple', 'banana', 'cherry'}

# Duplicates are automatically removed:
numbers = {1, 2, 3, 2, 1, 3}
print(numbers)   # {1, 2, 3}  — only unique values kept

# Creating a set from a list (to remove duplicates):
data = [1, 5, 3, 1, 2, 5, 3]
unique = set(data)
print(unique)    # {1, 2, 3, 5}

# Empty set — MUST use set(), NOT {} (that creates an empty dict!)
empty = set()
```

### Set Operations — Like a Venn Diagram

```python
python_devs = {'Alice', 'Bob', 'Carol', 'Dave'}
js_devs = {'Bob', 'Carol', 'Eve', 'Frank'}

# Union — everyone in either set
all_devs = python_devs | js_devs
# {'Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'}

# Intersection — only those in BOTH sets
both = python_devs & js_devs
# {'Bob', 'Carol'}

# Difference — in Python but NOT in JS
py_only = python_devs - js_devs
# {'Alice', 'Dave'}

# Symmetric difference — in one but NOT both
unique_to_one = python_devs ^ js_devs
# {'Alice', 'Dave', 'Eve', 'Frank'}
```

### Adding and Removing from Sets

```python
tags = {'python', 'coding'}

tags.add('beginner')         # Add one item
tags.discard('missing_tag')  # Remove if exists (no error if missing)
tags.remove('coding')        # Remove (raises KeyError if missing)

print('python' in tags)      # True — fast membership check!
print(len(tags))             # 2
```""",

# ────────────────────────────────────────────────

"Nested Data Structures": """## Combining Data Structures

Real-world data is almost never simple. A student has a name, age, multiple grades, and maybe a list of courses. A store has departments, each with products, each with a price and stock count. Python lets you **nest** data structures inside each other to model this complexity naturally.

### Lists of Lists — 2D Tables

```python
# A simple table: each row is a list
gradebook = [
    ['Alice', 90, 85, 92],
    ['Bob',   78, 82, 88],
    ['Carol', 95, 91, 87],
]

# Access: gradebook[row][column]
print(gradebook[0])         # ['Alice', 90, 85, 92]
print(gradebook[0][0])      # 'Alice'   — row 0, col 0
print(gradebook[1][2])      # 82        — row 1, col 2

# Loop through all students
for row in gradebook:
    name = row[0]
    scores = row[1:]         # Everything except the name
    avg = sum(scores) / len(scores)
    print(f'{name}: {avg:.1f}')
```

### Lists of Dictionaries — Records

This is the most common pattern. Each dictionary is one "record" with named fields:

```python
students = [
    {'name': 'Alice', 'age': 20, 'gpa': 3.8, 'courses': ['Python', 'Math']},
    {'name': 'Bob',   'age': 22, 'gpa': 3.2, 'courses': ['SQL', 'Python']},
    {'name': 'Carol', 'age': 21, 'gpa': 3.9, 'courses': ['AI', 'Math', 'Python']},
]

# Access a field:
print(students[0]['name'])              # Alice
print(students[1]['courses'])           # ['SQL', 'Python']
print(students[2]['courses'][0])        # AI

# Loop through all students:
for student in students:
    print(f"{student['name']} (GPA: {student['gpa']}) — {len(student['courses'])} courses")

# Find the top student:
top = max(students, key=lambda s: s['gpa'])
print(f"Top student: {top['name']}")    # Carol
```

### Dictionaries of Dictionaries — Hierarchical Data

```python
school = {
    'Class A': {
        'teacher': 'Ms. Johnson',
        'students': ['Alice', 'Bob', 'Carol'],
        'room': 101
    },
    'Class B': {
        'teacher': 'Mr. Smith',
        'students': ['Dave', 'Eve'],
        'room': 102
    }
}

# Accessing deeply nested data:
print(school['Class A']['teacher'])            # Ms. Johnson
print(school['Class B']['students'][1])        # Eve

# Iterating:
for class_name, info in school.items():
    print(f"{class_name}: {len(info['students'])} students, Room {info['room']}")
```

### The .get() Method — Safe Access

When accessing nested dictionaries, always use `.get()` to avoid `KeyError` if a key might not exist:

```python
data = {'user': {'name': 'Alice', 'email': 'alice@email.com'}}

# ❌ Risky — crashes if 'phone' doesn't exist
# phone = data['user']['phone']

# ✅ Safe — returns None (or your default) if not found
phone = data.get('user', {}).get('phone', 'Not provided')
print(phone)   # Not provided
```

### JSON — Nested Data in the Real World

This exact pattern (lists of dicts, dicts of dicts) is how **JSON** data works — the format used by virtually every web API in the world. Mastering nested data structures means you can work with any API response.""",

# ════════════════════════════════════════════════
# OOP IN PYTHON
# ════════════════════════════════════════════════

"Inheritance": """## Building On What Already Exists

**Inheritance** is one of the core pillars of Object-Oriented Programming. It lets you create a new class (the **child** or **subclass**) that automatically gets all the attributes and methods from an existing class (the **parent** or **superclass**). The child inherits everything and can then add new things or override old ones.

Think of it like genetics: a child inherits traits from their parents but also has their own unique characteristics.

### Basic Inheritance

```python
# Parent class (the blueprint)
class Animal:
    def __init__(self, name):
        self.name = name      # All animals have a name
    
    def breathe(self):        # All animals breathe
        return f'{self.name} breathes'
    
    def speak(self):
        return 'Some generic sound'

# Child class — inherits from Animal
class Dog(Animal):            # The (Animal) part means "inherit from Animal"
    def speak(self):          # OVERRIDE the parent's speak method
        return f'{self.name} says Woof!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says Meow!'

# Usage:
dog = Dog('Rex')
cat = Cat('Whiskers')

print(dog.breathe())     # Rex breathes  — inherited from Animal!
print(dog.speak())       # Rex says Woof! — overridden in Dog
print(cat.speak())       # Whiskers says Meow! — overridden in Cat
```

### `super()` — Calling the Parent's Methods

Use `super()` to call a method from the parent class, usually in `__init__` when you want to add to it rather than completely replace it:

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        return f'{self.make} {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)   # Call parent's __init__ first!
        self.doors = doors              # Then add Car-specific stuff
    
    def describe(self):
        # Call parent's describe() and add to it
        base = super().describe()
        return f'{base} ({self.doors}-door)'

class Truck(Vehicle):
    def __init__(self, make, model, payload_tons):
        super().__init__(make, model)
        self.payload_tons = payload_tons
    
    def describe(self):
        base = super().describe()
        return f'{base} (payload: {self.payload_tons}t)'

car = Car('Toyota', 'Camry', 4)
truck = Truck('Ford', 'F-150', 1.5)

print(car.describe())     # Toyota Camry (4-door)
print(truck.describe())   # Ford F-150 (payload: 1.5t)

# Both still have Vehicle attributes:
print(car.make)           # Toyota
print(truck.model)        # F-150
```

### `isinstance()` — Checking the Type Hierarchy

```python
print(isinstance(car, Car))       # True
print(isinstance(car, Vehicle))   # True!  — because Car IS a Vehicle
print(isinstance(truck, Car))     # False  — Truck is not a Car
```

### Why Use Inheritance?

1. **Code reuse** — Write the common code once in the parent
2. **Polymorphism** — Different classes can be treated the same way via the parent type
3. **Extensibility** — Easy to add new child classes without changing existing code

```python
# Polymorphism in action:
animals = [Dog('Rex'), Cat('Whiskers'), Dog('Max')]

for animal in animals:
    print(animal.speak())  # Each speaks in their own way — same method call!
# Rex says Woof!
# Whiskers says Meow!
# Max says Woof!
```""",

# ────────────────────────────────────────────────

"Encapsulation": """## Protecting Your Data

**Encapsulation** means keeping the internal data of an object hidden and protected, and providing controlled access through methods. Think of it like a bank: you can't just walk into the vault and grab money. You go through a teller (a method) who validates your request first.

### The Problem Without Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # Public — anyone can change it directly!

account = BankAccount(1000)
account.balance = -999999       # This should NEVER be allowed!
print(account.balance)           # -999999 — disaster!
```

### The Solution: Private Attributes

Python uses naming conventions to signal that an attribute is private:
- `_name` (single underscore) — "by convention, don't touch this"
- `__name` (double underscore) — name mangling, harder to access externally

```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner               # Public — fine to access
        self.__balance = initial_balance  # Private — hidden from outside

    def deposit(self, amount):
        \"\"\"Controlled way to add money.\"\"\"
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        self.__balance += amount
        print(f'Deposited ${amount}. New balance: ${self.__balance}')

    def withdraw(self, amount):
        \"\"\"Controlled way to remove money.\"\"\"
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        self.__balance -= amount
        print(f'Withdrew ${amount}. New balance: ${self.__balance}')

    def get_balance(self):
        \"\"\"Read-only access to balance.\"\"\"
        return self.__balance

# Usage:
account = BankAccount('Alice', 1000)
account.deposit(500)         # Deposited $500. New balance: $1500
account.withdraw(200)        # Withdrew $200. New balance: $1300
print(account.get_balance()) # 1300

# Try to access directly — fails!
# print(account.__balance)   # AttributeError — the name is mangled
```

### Using @property for Elegant Access

Python's `@property` decorator lets you create methods that *look like* attributes — clean access with validation built in:

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self._gpa = gpa         # Private by convention

    @property
    def gpa(self):
        \"\"\"Getter — called when you read student.gpa\"\"\"
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        \"\"\"Setter — called when you write student.gpa = value\"\"\"
        if not 0.0 <= value <= 4.0:
            raise ValueError(f'GPA must be between 0.0 and 4.0, got {value}')
        self._gpa = value

    @property
    def grade_letter(self):
        \"\"\"Computed property — no setter needed\"\"\"
        if self._gpa >= 3.7: return 'A'
        if self._gpa >= 3.0: return 'B'
        if self._gpa >= 2.0: return 'C'
        return 'F'

# Usage — looks like plain attribute access, but validation runs!
s = Student('Alice', 3.5)
print(s.gpa)             # 3.5
print(s.grade_letter)    # B

s.gpa = 3.9              # Calls the setter — validates it
print(s.grade_letter)    # A

# s.gpa = 5.0            # Raises ValueError!
```

### Why Encapsulation Matters

1. **Data integrity** — prevents invalid states (negative balance, GPA > 4.0)
2. **Abstraction** — users of your class don't need to know how it works internally
3. **Flexibility** — you can change the internal implementation without breaking code that uses the class""",

# ────────────────────────────────────────────────

"Magic Methods": """## Making Your Objects Feel Native

**Magic methods** (also called **dunder methods** — double underscore) are special methods that Python calls automatically when you use certain operations on your objects. By defining them, you make your custom class work seamlessly with Python's built-in operators and functions.

### Why They Matter

Without magic methods:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1 = Vector(3, 4)
v2 = Vector(1, 2)
# print(v1 + v2)    # ❌ TypeError: unsupported operand type(s) for +
# print(v1)         # ❌ <__main__.Vector object at 0x...> — useless!
```

With magic methods, your object feels like a built-in type:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        \"\"\"Called by print() and str() — human-readable display\"\"\"
        return f'Vector({self.x}, {self.y})'

    def __repr__(self):
        \"\"\"Called in the REPL — developer-facing representation\"\"\"
        return f'Vector(x={self.x}, y={self.y})'

    def __add__(self, other):
        \"\"\"Called when you use the + operator\"\"\"
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        \"\"\"Called when you use the - operator\"\"\"
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        \"\"\"Called when you use the * operator (scalar multiplication)\"\"\"
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        \"\"\"Called when you use == operator\"\"\"
        return self.x == other.x and self.y == other.y

    def __len__(self):
        \"\"\"Called by len() — returns the magnitude as an integer\"\"\"
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __abs__(self):
        \"\"\"Called by abs() — returns the magnitude as a float\"\"\"
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)            # Vector(3, 4)         — calls __str__
print(v1 + v2)       # Vector(4, 6)         — calls __add__
print(v1 - v2)       # Vector(2, 2)         — calls __sub__
print(v1 * 3)        # Vector(9, 12)        — calls __mul__
print(v1 == v2)      # False                — calls __eq__
print(len(v1))       # 5                   — calls __len__ (3-4-5 triangle)
print(abs(v1))       # 5.0                 — calls __abs__
```

### The Most Important Magic Methods

| Method | Triggered By | Purpose |
|---|---|---|
| `__init__` | `ClassName(args)` | Initialize a new object |
| `__str__` | `print(obj)`, `str(obj)` | Human-friendly string |
| `__repr__` | `repr(obj)`, REPL display | Dev-friendly string |
| `__len__` | `len(obj)` | Length |
| `__eq__` | `obj == other` | Equality check |
| `__lt__` | `obj < other` | Less than |
| `__add__` | `obj + other` | Addition |
| `__getitem__` | `obj[key]` | Indexing |
| `__contains__` | `item in obj` | Membership test |
| `__iter__` | `for x in obj` | Make iterable |

### Making an Object Sortable

```python
from functools import total_ordering

@total_ordering   # Automatically generates the other comparison methods
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f'{self.name} ({self.gpa})'

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):      # Only need this one + @total_ordering
        return self.gpa < other.gpa

students = [Student('Bob', 3.2), Student('Alice', 3.8), Student('Carol', 3.5)]
students.sort()                   # Works! Uses __lt__
for s in students:
    print(s)
# Bob (3.2), Carol (3.5), Alice (3.8)
```""",

# ────────────────────────────────────────────────

"Class Methods & Static Methods": """## Three Types of Methods

A class can have three kinds of methods, each with a different relationship to the class and its instances:

| Type | Decorator | First Parameter | Access To |
|---|---|---|---|
| Instance method | (none) | `self` | Instance data AND class data |
| Class method | `@classmethod` | `cls` | Class data only (not instance) |
| Static method | `@staticmethod` | (none) | Neither — it's just a helper function |

### Instance Methods — The Default

Regular methods you've already seen. They receive `self` (the specific instance) as their first argument:

```python
class Pizza:
    def __init__(self, size, topping):
        self.size = size
        self.topping = topping
    
    def describe(self):    # Instance method
        return f'{self.size} pizza with {self.topping}'

p = Pizza('Large', 'pepperoni')
print(p.describe())   # Large pizza with pepperoni
```

### Class Methods — Working With the Class Itself

`@classmethod` methods receive `cls` (the class itself) instead of an instance. They're useful for:
- **Factory methods** — alternative ways to create instances
- **Class-level counters and tracking**

```python
class Pizza:
    total_made = 0          # Class variable — shared by ALL instances
    menu = {'Small': 8.99, 'Medium': 12.99, 'Large': 16.99}

    def __init__(self, size, topping):
        self.size = size
        self.topping = topping
        Pizza.total_made += 1    # Increment the class variable
    
    @classmethod
    def from_string(cls, pizza_str):
        \"\"\"Factory method — create a Pizza from a string like 'Large:pepperoni'\"\"\"
        size, topping = pizza_str.split(':')
        return cls(size, topping)    # cls() creates a new instance
    
    @classmethod
    def get_total_made(cls):
        return cls.total_made    # Access class variable via cls

# Creating instances:
p1 = Pizza('Large', 'pepperoni')
p2 = Pizza.from_string('Medium:mushroom')    # Using the factory method

print(Pizza.get_total_made())   # 2
print(p2.size)                   # Medium
print(p2.topping)                # mushroom
```

### Static Methods — Helper Functions That Belong to a Class

`@staticmethod` methods don't receive `self` or `cls`. They're just regular functions that logically belong to the class (for organization), but don't need access to instance or class data:

```python
class Pizza:
    @staticmethod
    def is_valid_size(size):
        \"\"\"Validation helper — doesn't need self or cls\"\"\"
        return size in ['Small', 'Medium', 'Large', 'XL']
    
    @staticmethod
    def calculate_tip(price, percent=18):
        return round(price * percent / 100, 2)

# Call on the class directly — no instance needed:
print(Pizza.is_valid_size('Large'))    # True
print(Pizza.is_valid_size('Tiny'))     # False
print(Pizza.calculate_tip(16.99))      # 3.06

# Can also call on an instance (not common, but works):
p = Pizza('Large', 'pepperoni')
print(p.is_valid_size('Medium'))       # True
```

### When to Use Each

- **Instance method** — when the method needs to read or write `self.anything`
- **Class method** — when the method works at the class level (factories, class state)
- **Static method** — when the logic is related to the class conceptually but doesn't actually need the class or instance""",

# ════════════════════════════════════════════════
# FILE I/O
# ════════════════════════════════════════════════

"CSV Files": """## What is a CSV File?

**CSV** stands for **Comma-Separated Values**. It's the most widely used format for storing tabular data (like a spreadsheet) as plain text. Every spreadsheet application, database tool, and data analysis library can read and write CSV files.

A CSV file looks like this:
```
Name,Age,City,Score
Alice,25,Lagos,92
Bob,30,Abuja,78
Carol,22,Ibadan,88
```

The first row is typically the **header** (column names). Each row after that is a record, with values separated by commas.

### Reading CSV Files — The `csv` Module

Python's built-in `csv` module handles the quirks of CSV parsing (like values with commas inside them):

```python
import csv

# Basic reading — returns each row as a list
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    
    header = next(reader)          # Read and skip the header row
    print(f'Columns: {header}')   # ['Name', 'Age', 'City', 'Score']
    
    for row in reader:
        name, age, city, score = row
        print(f'{name} from {city}: {score}')

# Reading into dictionaries — much more readable!
with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)    # DictReader uses the header as keys
    
    for row in reader:
        # Now access by column name, not by index
        print(f"{row['Name']}: score = {row['Score']}")
```

### Writing CSV Files

```python
import csv

students = [
    ['Alice', 25, 'Lagos', 92],
    ['Bob', 30, 'Abuja', 78],
    ['Carol', 22, 'Ibadan', 88],
]

# Basic writing
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City', 'Score'])   # Header
    writer.writerows(students)                           # All data rows

# Writing dictionaries (easier to read and maintain)
students_dicts = [
    {'Name': 'Alice', 'Age': 25, 'City': 'Lagos', 'Score': 92},
    {'Name': 'Bob',   'Age': 30, 'City': 'Abuja', 'Score': 78},
]

with open('output2.csv', 'w', newline='') as f:
    fieldnames = ['Name', 'Age', 'City', 'Score']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()          # Writes the column names
    writer.writerows(students_dicts)
```

⚠️ **Important:** Always use `newline=''` when opening CSV files for writing on Windows. Without it, you'll get blank lines between every row.

### A Complete Example: Grade Analysis

```python
import csv

# Read grades and calculate statistics
def analyze_grades(filename):
    students = []
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                'name': row['Name'],
                'score': int(row['Score'])
            })
    
    scores = [s['score'] for s in students]
    print(f'Students: {len(students)}')
    print(f'Average: {sum(scores)/len(scores):.1f}')
    print(f'Highest: {max(scores)} — {max(students, key=lambda s: s["score"])["name"]}')
    print(f'Lowest: {min(scores)} — {min(students, key=lambda s: s["score"])["name"]}')
```""",

# ────────────────────────────────────────────────

"JSON Files": """## What is JSON?

**JSON** (JavaScript Object Notation) is the universal language of data exchange on the internet. When your phone app loads your social media feed, when a website fetches weather data, when any two programs communicate over the internet — they're almost certainly using JSON.

JSON looks exactly like Python dictionaries and lists:
```json
{
  "name": "Alice",
  "age": 25,
  "courses": ["Python", "SQL"],
  "is_active": true,
  "gpa": 3.8
}
```

The main differences from Python syntax:
- JSON uses `true`/`false` (lowercase), Python uses `True`/`False`
- JSON uses `null`, Python uses `None`
- JSON keys must be strings in double quotes

### Python's `json` Module

```python
import json

# Python dict → JSON string
data = {
    'name': 'Alice',
    'age': 25,
    'courses': ['Python', 'SQL'],
    'is_active': True,
    'gpa': 3.8
}

json_string = json.dumps(data)           # Compact string
json_pretty = json.dumps(data, indent=2) # Pretty-printed with indentation

print(json_string)
# {"name": "Alice", "age": 25, "courses": ["Python", "SQL"], ...}

print(json_pretty)
# {
#   "name": "Alice",
#   "age": 25,
#   ...
# }
```

### Writing JSON to a File

```python
import json

config = {
    'app_name': 'Digital Era',
    'version': '2.0',
    'debug': False,
    'database_url': 'sqlite:///app.db',
    'allowed_hosts': ['localhost', 'digital-era.live']
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)     # dump() writes to a file

print('Config saved!')
```

### Reading JSON from a File

```python
import json

with open('config.json', 'r') as f:
    loaded_config = json.load(f)       # load() reads from a file

print(loaded_config['app_name'])       # Digital Era
print(loaded_config['allowed_hosts'])  # ['localhost', 'digital-era.live']
print(type(loaded_config))             # <class 'dict'>
```

### JSON ↔ Python Type Mapping

| JSON | Python |
|---|---|
| object `{}` | `dict` |
| array `[]` | `list` |
| string `"hello"` | `str` |
| number `42` | `int` |
| number `3.14` | `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### Working with API Responses

JSON is how web APIs send you data. Here's a typical pattern:

```python
import json

# Simulate an API response string
api_response = '''
{
  "status": "success",
  "data": {
    "students": [
      {"id": 1, "name": "Alice", "score": 92},
      {"id": 2, "name": "Bob",   "score": 78}
    ],
    "total": 2
  }
}
'''

# Parse the JSON string into a Python dict
parsed = json.loads(api_response)    # loads() parses a string (not a file)

print(parsed['status'])              # success
students = parsed['data']['students']
for s in students:
    print(f"  {s['name']}: {s['score']}")
```

**Key distinction:**
- `json.dumps()` / `json.loads()` — work with **strings** (s = string)
- `json.dump()` / `json.load()` — work with **files**""",

# ────────────────────────────────────────────────

"Error Handling with Files": """## Files Can Fail — Handle It Gracefully

Any file operation can fail for many reasons: the file doesn't exist, you don't have permission, the disk is full, the file is corrupted. Good code anticipates these failures and handles them gracefully instead of crashing.

### The Problem

```python
# This will crash if the file doesn't exist:
with open('data.txt', 'r') as f:
    content = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

### The Solution: try / except

```python
try:
    with open('data.txt', 'r') as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print('Error: The file does not exist.')
except PermissionError:
    print('Error: You do not have permission to read this file.')
except Exception as e:
    print(f'Unexpected error: {e}')
```

### Common File-Related Exceptions

| Exception | When It Occurs |
|---|---|
| `FileNotFoundError` | File or directory does not exist |
| `PermissionError` | No read/write permission |
| `IsADirectoryError` | Tried to open a directory as a file |
| `FileExistsError` | Tried to create a file that already exists |
| `UnicodeDecodeError` | File has unexpected encoding |
| `OSError` | General OS-level I/O error |

### Using `finally` — Code That Always Runs

The `finally` block runs whether or not an exception occurred. Perfect for cleanup:

```python
file = None
try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('File not found!')
finally:
    if file:
        file.close()      # ALWAYS closes the file, even if there was an error
    print('Done (ran no matter what).')
```

Note: The `with` statement is even better because it automatically closes the file in all cases — you don't need `finally` for cleanup with `with`.

### Practical Pattern: Read or Create

A very common pattern: try to read a file, and if it doesn't exist, create it with defaults:

```python
import json

def load_settings(filename='settings.json'):
    default_settings = {
        'theme': 'dark',
        'language': 'en',
        'notifications': True
    }
    
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'Settings file not found. Creating defaults...')
        with open(filename, 'w') as f:
            json.dump(default_settings, f, indent=2)
        return default_settings
    except json.JSONDecodeError:
        print('Settings file is corrupted. Using defaults.')
        return default_settings

settings = load_settings()
print(settings['theme'])   # dark
```

### Checking Before Opening

Sometimes it's cleaner to check if a file exists before attempting to open it:

```python
import os

filename = 'report.csv'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = f.read()
else:
    print(f'{filename} does not exist yet.')
```""",

# ────────────────────────────────────────────────

"Working with Paths": """## Cross-Platform File Paths

File paths are written differently on different operating systems:
- **Windows:** `C:\\Users\\Alice\\Documents\\report.txt`
- **macOS/Linux:** `/Users/Alice/Documents/report.txt`

If you hardcode paths with backslashes, your code breaks on Mac and Linux. Python's `os.path` module and the modern `pathlib` library solve this by handling the differences automatically.

### The `os` Module — The Classic Approach

```python
import os

# Get current working directory (where the script is running from)
cwd = os.getcwd()
print(cwd)

# Build a path that works on any OS
path = os.path.join('data', 'students', 'results.csv')
# Windows: data\\students\\results.csv
# Mac/Linux: data/students/results.csv

# Check if a path exists
print(os.path.exists('config.json'))    # True or False
print(os.path.isfile('config.json'))    # True if it's a file
print(os.path.isdir('curriculum'))      # True if it's a directory

# Get just the filename from a full path
full = '/home/alice/documents/report.csv'
print(os.path.basename(full))   # report.csv
print(os.path.dirname(full))    # /home/alice/documents

# Split filename and extension
name, ext = os.path.splitext('report.csv')
print(name)   # report
print(ext)    # .csv
```

### Creating and Listing Directories

```python
import os

# Create a directory (and parent directories if needed)
os.makedirs('output/reports/2024', exist_ok=True)   
# exist_ok=True means no error if it already exists

# List files in a directory
files = os.listdir('curriculum/tracks')
for f in files:
    print(f)

# Get full absolute path of a relative path
abs_path = os.path.abspath('curriculum/tracks')
print(abs_path)
```

### `pathlib` — The Modern, Pythonic Way

Python 3.4+ introduced `pathlib`, which treats paths as objects instead of strings. It's cleaner and more powerful:

```python
from pathlib import Path

# Create a path object
base = Path('curriculum') / 'tracks'    # The / operator builds paths!
file = base / 'python_core.json'

print(file)              # curriculum/tracks/python_core.json
print(file.exists())     # True or False
print(file.name)         # python_core.json
print(file.stem)         # python_core (no extension)
print(file.suffix)       # .json
print(file.parent)       # curriculum/tracks

# Read and write text files directly:
content = file.read_text(encoding='utf-8')

new_file = Path('output.txt')
new_file.write_text('Hello, World!', encoding='utf-8')

# Find all JSON files in a directory:
tracks_dir = Path('curriculum/tracks')
for json_file in tracks_dir.glob('*.json'):
    print(json_file.name)

# Create directory structure:
output = Path('output') / 'reports' / '2024'
output.mkdir(parents=True, exist_ok=True)
```

### Finding the Script's Own Location

A crucial pattern — finding files relative to the current script, no matter where it's run from:

```python
from pathlib import Path

# __file__ is the path of the current script
script_dir = Path(__file__).parent
config_file = script_dir / 'config.json'

print(f'Script is in: {script_dir}')
print(f'Config would be at: {config_file}')
```

**Recommendation:** Use `pathlib` for all new code — it's more readable and powerful than `os.path`.""",

# ════════════════════════════════════════════════
# DECORATORS
# ════════════════════════════════════════════════

"Decorators with Arguments": """## Decorators That Accept Parameters

Basic decorators wrap a function with no configuration. But what if you want to configure the decorator itself — like specifying a rate limit, a retry count, or a log level?

The trick is to add **one more layer** of nesting: a factory function that receives the arguments and returns a decorator.

### The Pattern: Decorator Factory

```python
# A decorator factory — it returns a decorator
def repeat(times):                      # 1. Outer function: takes configuration
    def decorator(func):                 # 2. Middle function: takes the function
        def wrapper(*args, **kwargs):    # 3. Inner function: does the work
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator                     # Returns the decorator

# Usage — you call the factory with arguments:
@repeat(3)
def say_hello(name):
    print(f'Hello, {name}!')

say_hello('Alice')
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

Compare with a no-argument decorator: `@decorator` vs `@decorator(arg)` — the parentheses are the key difference.

### Practical Example: Retry on Failure

```python
import time

def retry(max_attempts=3, delay=1.0):
    \"\"\"Decorator factory: retries a function on exception.\"\"\"
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)   # If it works, return result
                except Exception as e:
                    last_error = e
                    print(f'Attempt {attempt}/{max_attempts} failed: {e}')
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_error   # If all attempts failed, raise the last error
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url):
    import random
    if random.random() < 0.7:    # 70% chance of failure (for demo)
        raise ConnectionError(f'Could not connect to {url}')
    return f'Data from {url}'

try:
    result = fetch_data('https://api.example.com')
    print(result)
except ConnectionError as e:
    print(f'Permanently failed: {e}')
```

### Practical Example: Log Level

```python
import logging

def log(level='INFO'):
    \"\"\"Logs function calls at a specified level.\"\"\"
    def decorator(func):
        def wrapper(*args, **kwargs):
            getattr(logging, level.lower())(
                f'Calling {func.__name__}({args}, {kwargs})'
            )
            result = func(*args, **kwargs)
            getattr(logging, level.lower())(
                f'{func.__name__} returned {result}'
            )
            return result
        return wrapper
    return decorator

@log(level='DEBUG')
def add(a, b):
    return a + b

@log(level='INFO')
def divide(a, b):
    return a / b
```

### Stacking Multiple Decorated Arguments

```python
@retry(max_attempts=3)
@log(level='INFO')
def process_record(record_id):
    ...
    # Decorators apply from bottom to top:
    # 1. First log (closest to function)
    # 2. Then retry wraps the logged version
```""",

# ────────────────────────────────────────────────

"Built-in Decorators": """## Python's Built-In Decorators

Python ships with several powerful decorators that you'll encounter constantly in real-world code.

### `@staticmethod` — Method Without Self

You've seen this in OOP. A static method belongs to the class namespace but doesn't receive `self` or `cls`. It's a plain function that happens to live inside a class:

```python
class MathUtils:
    @staticmethod
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

# Call on the class — no instance needed
print(MathUtils.is_prime(17))              # True
print(MathUtils.celsius_to_fahrenheit(100)) # 212.0
```

### `@classmethod` — Method That Receives the Class

Receives `cls` (the class) instead of `self` (an instance). Used for factory methods and class-level operations:

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_str):
        \"\"\"Alternative constructor: Date.from_string('2024-01-15')\"\"\"
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)    # Creates a new Date instance
    
    @classmethod
    def today(cls):
        from datetime import date
        d = date.today()
        return cls(d.year, d.month, d.day)
    
    def __str__(self):
        return f'{self.year}-{self.month:02d}-{self.day:02d}'

d1 = Date(2024, 1, 15)
d2 = Date.from_string('2024-06-20')   # Using the factory
d3 = Date.today()

print(d2)   # 2024-06-20
```

### `@property` — Methods That Look Like Attributes

Makes a method behave like a read-only attribute. Use `@name.setter` to add write access:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius    # Store in Celsius internally
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Temperature below absolute zero!')
        self._celsius = value
    
    @property
    def fahrenheit(self):          # Computed property — no setter
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

temp = Temperature(25)
print(temp.celsius)      # 25      — looks like attribute, calls getter
print(temp.fahrenheit)   # 77.0    — computed automatically
print(temp.kelvin)       # 298.15

temp.celsius = 100       # Calls the setter with validation
print(temp.fahrenheit)   # 212.0

# temp.fahrenheit = 200  # ❌ AttributeError — no setter defined for fahrenheit
```

### `@dataclass` (Python 3.7+) — Auto-Generate Boilerplate

```python
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    gpa: float = 0.0
    courses: list = field(default_factory=list)   # Mutable default
    
    # @dataclass automatically creates:
    # - __init__(self, name, gpa=0.0, courses=[])
    # - __repr__(self) — nice string representation
    # - __eq__(self, other) — value equality

s = Student('Alice', 3.8)
s.courses.append('Python')
print(s)   # Student(name='Alice', gpa=3.8, courses=['Python'])
print(s == Student('Alice', 3.8))   # False — different courses list
```""",

# ────────────────────────────────────────────────

"functools.wraps": """## The Problem with Decorators and Function Identity

When you wrap a function in a decorator, the resulting `wrapper` function has a different name and docstring — it completely loses its original identity. This breaks introspection tools, documentation generators, and debugging:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    \"\"\"Says hello to name.\"\"\"
    return f'Hello, {name}!'

# The function has LOST its identity:
print(greet.__name__)   # 'wrapper'  — wrong! Should be 'greet'
print(greet.__doc__)    # None       — docstring is gone!
```

### The Fix: `@functools.wraps`

Apply `@functools.wraps(func)` to your `wrapper` function. It copies the original function's metadata (`__name__`, `__doc__`, `__module__`, `__qualname__`, `__annotations__`, `__dict__`) onto the wrapper:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)    # ← Add this line!
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    \"\"\"Says hello to name.\"\"\"
    return f'Hello, {name}!'

# Identity preserved:
print(greet.__name__)   # 'greet'
print(greet.__doc__)    # 'Says hello to name.'
```

### Always Use `functools.wraps`

Here's the rule: **any time you write a decorator, always use `@functools.wraps`**. Here it is in a complete, production-quality decorator:

```python
import functools
import time

def timer(func):
    \"\"\"Measures and prints the execution time of a function.\"\"\"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start:.4f}s')
        return result
    return wrapper

def logger(func):
    \"\"\"Logs function calls with arguments and return values.\"\"\"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={repr(v)}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {repr(result)}')
        return result
    return wrapper

@timer
@logger
def compute(n):
    \"\"\"Computes the sum of squares up to n.\"\"\"
    return sum(i ** 2 for i in range(n))

result = compute(100)
# Calling compute(100)
# compute returned 328350
# compute took 0.0001s
print(compute.__name__)    # compute  ✅ — identity preserved through both decorators
print(compute.__doc__)     # Computes the sum of squares up to n.
```

### `functools.lru_cache` — Memoization Made Easy

Another gem from `functools` — automatic caching of function results:

```python
import functools

@functools.lru_cache(maxsize=128)   # Cache up to 128 different argument combinations
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Without caching, fibonacci(35) would make millions of recursive calls.
# With lru_cache, results are stored and reused:
print(fibonacci(35))   # Instant even for large n
print(fibonacci.cache_info())   # Shows hits/misses: CacheInfo(hits=33, misses=36, ...)
```""",

# ────────────────────────────────────────────────

"Chaining Decorators": """## Applying Multiple Decorators to One Function

You can stack multiple decorators on a single function. Python applies them **from bottom to top** — the decorator closest to the `def` runs first, wrapping the function, then the next one wraps that result, and so on.

### Basic Stacking

```python
import functools

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<b>{result}</b>'
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<i>{result}</i>'
    return wrapper

def underline(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<u>{result}</u>'
    return wrapper

@bold
@italic
@underline
def greet(name):
    return f'Hello, {name}!'

print(greet('Alice'))
# <b><i><u>Hello, Alice!</u></i></b>

# The application order (bottom to top):
# 1. underline wraps greet → greet_underlined
# 2. italic wraps greet_underlined → greet_italic_underlined
# 3. bold wraps that → final_greet
```

### A Real-World Stack: Auth + Logging + Timing

```python
import functools
import time

def require_auth(func):
    \"\"\"Checks that the user is authenticated before running.\"\"\"
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get('authenticated'):
            raise PermissionError(f'{user[\"name\"]} is not authenticated!')
        return func(user, *args, **kwargs)
    return wrapper

def log_call(func):
    \"\"\"Logs every call with arguments.\"\"\"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG] {func.__name__} called')
        result = func(*args, **kwargs)
        print(f'[LOG] {func.__name__} completed')
        return result
    return wrapper

def timing(func):
    \"\"\"Measures execution time.\"\"\"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'[TIMING] {func.__name__}: {elapsed:.4f}s')
        return result
    return wrapper

@timing      # 3. Applied last (outermost)
@log_call    # 2. Applied second
@require_auth # 1. Applied first (closest to function, innermost)
def get_dashboard(user):
    return f\"Welcome to the dashboard, {user['name']}!\"

alice = {'name': 'Alice', 'authenticated': True}
bob   = {'name': 'Bob',   'authenticated': False}

print(get_dashboard(alice))
# [LOG] get_dashboard called
# [LOG] get_dashboard completed
# [TIMING] get_dashboard: 0.0001s
# Welcome to the dashboard, Alice!

get_dashboard(bob)
# PermissionError: Bob is not authenticated!
```

### When Order Matters

The order of stacked decorators CAN affect behavior:

```python
# If authentication is outermost:
@require_auth
@timing
def my_func(user): ...
# → auth runs first, then timing wraps an already-authenticated call

# If timing is outermost:
@timing
@require_auth
def my_func(user): ...
# → timing starts the clock, THEN auth runs (so timing includes auth time)
```

Always think about which layer should be the "first gate" a call passes through.""",

# ────────────────────────────────────────────────

"Timing Decorator": """## Building a Timing Decorator

A **timing decorator** measures how long a function takes to execute. It's one of the most practical decorators you can write — invaluable for profiling and optimizing code.

### The Complete Implementation

```python
import functools
import time

def timeit(func):
    \"\"\"
    Decorator that measures and prints the execution time of a function.
    Works with any function, regardless of arguments.
    \"\"\"
    @functools.wraps(func)    # Preserve the original function's identity
    def wrapper(*args, **kwargs):
        # Record start time (perf_counter is more precise than time.time())
        start = time.perf_counter()
        
        # Call the original function with all its arguments
        result = func(*args, **kwargs)
        
        # Calculate elapsed time
        elapsed = time.perf_counter() - start
        
        # Print the timing information
        print(f'⏱  {func.__name__} took {elapsed:.4f} seconds')
        
        # IMPORTANT: Return the result so the decorator doesn't swallow it
        return result
    
    return wrapper

# Apply to any function:
@timeit
def sum_of_squares(n):
    \"\"\"Calculates the sum of squares from 1 to n.\"\"\"
    return sum(i ** 2 for i in range(1, n + 1))

@timeit
def slow_task():
    \"\"\"Simulates a slow operation.\"\"\"
    time.sleep(1.5)
    return 'Done!'

print(sum_of_squares(1_000_000))
# ⏱  sum_of_squares took 0.1234 seconds
# 333333833333500000

print(slow_task())
# ⏱  slow_task took 1.5012 seconds
# Done!
```

### Enhanced Version with Statistics

```python
import functools, time, statistics

def timeit_stats(runs=5):
    \"\"\"Times a function over multiple runs and reports statistics.\"\"\"
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            times = []
            result = None
            for i in range(runs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                times.append(time.perf_counter() - start)
            
            print(f'\\n📊 {func.__name__} over {runs} runs:')
            print(f'   Min:  {min(times)*1000:.2f} ms')
            print(f'   Max:  {max(times)*1000:.2f} ms')
            print(f'   Mean: {statistics.mean(times)*1000:.2f} ms')
            print(f'   Stdev:{statistics.stdev(times)*1000:.2f} ms')
            
            return result
        return wrapper
    return decorator

@timeit_stats(runs=10)
def bubble_sort(lst):
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

import random
data = random.sample(range(1000), 100)
bubble_sort(data)
```""",

# ════════════════════════════════════════════════
# GENERATORS
# ════════════════════════════════════════════════

"Generator Functions": """## What is a Generator?

A **generator** is a special type of function that produces values **one at a time**, on demand, without creating the entire sequence in memory at once. Instead of using `return` to send back a value and exit, generators use `yield` — which pauses the function, sends a value out, and then resumes from exactly where it left off.

### The Memory Problem Generators Solve

```python
# ❌ Regular function: creates a list of 10 MILLION numbers in memory all at once
def get_all_squares(n):
    return [x**2 for x in range(n)]

squares = get_all_squares(10_000_000)   # Uses ~400MB of RAM!

# ✅ Generator: produces one number at a time, uses almost no memory
def generate_squares(n):
    for x in range(n):
        yield x**2    # Pause here, send out x**2, resume when asked for next

squares = generate_squares(10_000_000)  # Uses <1KB of RAM!
```

### The `yield` Keyword

`yield` turns a regular function into a generator function. When Python sees `yield`:
1. The current value is sent out to the caller
2. The function **pauses** — all local variables are preserved
3. Next time the generator is asked for a value, it **resumes** from right after the `yield`

```python
def countdown(n):
    print(f'Starting countdown from {n}')
    while n > 0:
        yield n    # ← PAUSE here, send n out
        n -= 1     # ← Next call resumes here
    print('Liftoff!')

# Create the generator (the function body doesn't run yet!)
gen = countdown(3)
print(type(gen))   # <class 'generator'>

# Manually get values with next():
print(next(gen))   # Starting countdown from 3 → 3
print(next(gen))   # 2
print(next(gen))   # 1
# next(gen)        # Would raise StopIteration + print 'Liftoff!'
```

### The Natural Way: Using Generators in Loops

```python
# Much more natural — the for loop calls next() for you:
for num in countdown(5):
    print(num)
# Starting countdown from 5
# 5, 4, 3, 2, 1
# Liftoff!

# You can also convert to a list (this loads everything into memory):
values = list(countdown(5))   # [5, 4, 3, 2, 1]
```

### A Practical Generator: Reading Large Files

The #1 real-world use of generators is processing large files without loading them all into memory:

```python
def read_chunks(filename, chunk_size=1024):
    \"\"\"Read a large file in chunks instead of all at once.\"\"\"
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def count_lines(filename):
    \"\"\"Count lines in a huge file without loading it all.\"\"\"
    total = 0
    for line in open(filename):   # open() returns a generator-like object
        total += 1
    return total
```

### When to Use Generators

✅ **Use generators when:**
- Working with large datasets that don't fit in memory
- Processing a potentially infinite sequence (e.g., reading sensor data)
- Building pipelines where data is processed step-by-step
- You want to delay computation until it's actually needed (lazy evaluation)

❌ **Use a list when:**
- You need random access (e.g., `data[5]`)
- You need to iterate the sequence multiple times
- The data is small and fits easily in memory""",

# ────────────────────────────────────────────────

"Generator Expressions": """## The Lazy List Comprehension

A **generator expression** looks almost identical to a list comprehension, but uses **parentheses** instead of square brackets. The key difference: a list comprehension computes all values immediately and stores them in memory, while a generator expression computes values lazily — one at a time, only when needed.

### Syntax Comparison

```python
numbers = range(1, 1_000_001)   # 1 to 1,000,000

# List comprehension — creates 1 million integers in memory RIGHT NOW
squares_list = [x**2 for x in numbers]      # Uses ~32MB RAM

# Generator expression — creates a generator object (near-zero RAM)
squares_gen = (x**2 for x in numbers)       # Uses <100 bytes RAM
```

### Using Generator Expressions

```python
# They work with any function that accepts an iterable:
gen = (x**2 for x in range(10))

# With sum() — doesn't need the whole list at once
total = sum(x**2 for x in range(1_000_001))     # Efficient!
print(total)   # 333333833333500000

# With max()
biggest = max(len(word) for word in ['Python', 'is', 'amazing', 'really'])
print(biggest)   # 7

# With any() and all() — short-circuits (stops as soon as possible)
scores = [85, 92, 78, 95, 88]
print(all(s >= 70 for s in scores))    # True — all scores passing
print(any(s >= 90 for s in scores))    # True — at least one is A-grade
```

### With Conditions

Just like list comprehensions, generator expressions support filtering:

```python
words = ['hello', 'world', 'python', 'is', 'great']

# Filter and transform in one expression
long_upper = (word.upper() for word in words if len(word) > 4)
for word in long_upper:
    print(word)
# HELLO, WORLD, PYTHON, GREAT
```

### Generator Expressions vs. Generator Functions

Use a **generator expression** for simple, one-liners:
```python
evens = (x for x in range(100) if x % 2 == 0)
```

Use a **generator function** when the logic is more complex:
```python
def generate_primes():
    \"\"\"Generates prime numbers infinitely.\"\"\"
    def is_prime(n):
        if n < 2: return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# Get first 10 primes:
from itertools import islice
first_10 = list(islice(generate_primes(), 10))
print(first_10)   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Important: Generators Are Exhausted

Once you iterate through a generator, it's **done**:
```python
gen = (x**2 for x in range(5))
print(list(gen))    # [0, 1, 4, 9, 16]
print(list(gen))    # []  — empty! The generator is exhausted.

# To iterate again, create a new one:
gen = (x**2 for x in range(5))   # Fresh generator
```""",

# ────────────────────────────────────────────────

"yield from": """## Delegating to Another Generator

The `yield from` expression, introduced in Python 3.3, allows a generator to delegate part of its work to another iterable (a list, tuple, range, or another generator). It's a powerful shorthand that also enables efficient **generator chaining**.

### The Problem It Solves

Without `yield from`, to forward values from an inner iterable, you'd need a loop:

```python
# ❌ Verbose way: manually yielding from each sub-list
def chain_manual(*iterables):
    for it in iterables:
        for item in it:    # Extra loop just to forward values
            yield item

# ✅ With yield from: cleaner and more efficient
def chain(*iterables):
    for it in iterables:
        yield from it      # Delegates: "yield everything from 'it'"

result = list(chain([1, 2, 3], [4, 5], [6, 7, 8]))
print(result)   # [1, 2, 3, 4, 5, 6, 7, 8]
```

### Flattening Nested Structures

`yield from` is perfect for recursively flattening nested lists:

```python
def flatten(nested):
    \"\"\"Recursively flattens arbitrarily nested lists.\"\"\"
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)    # Recurse into sub-lists
        else:
            yield item                  # Yield non-list items directly

data = [1, [2, 3], [4, [5, [6, 7]]], 8]
print(list(flatten(data)))    # [1, 2, 3, 4, 5, 6, 7, 8]
```

### Delegating Between Generators

```python
def inner_gen():
    \"\"\"A generator that yields some values.\"\"\"
    print('Inner starting...')
    yield 10
    yield 20
    yield 30
    print('Inner done.')
    return 'inner result'    # Return value from a generator (special!)

def outer_gen():
    print('Outer starting...')
    yield 1
    yield 2
    # Delegate to inner_gen — outer pauses until inner is exhausted
    inner_result = yield from inner_gen()
    print(f'Inner returned: {inner_result}')
    yield 100

for val in outer_gen():
    print(f'Got: {val}')

# Outer starting...
# Got: 1
# Got: 2
# Inner starting...
# Got: 10
# Got: 20
# Got: 30
# Inner done.
# Inner returned: inner result
# Got: 100
```

### Practical: Building Composite Data Pipelines

```python
def read_file(filename):
    with open(filename) as f:
        yield from f   # yield from a file (which is iterable line by line)

def filter_comments(lines):
    yield from (line for line in lines if not line.startswith('#'))

def strip_whitespace(lines):
    yield from (line.strip() for line in lines if line.strip())

# Composing the pipeline:
def process_config(filename):
    lines = read_file(filename)
    lines = filter_comments(lines)
    lines = strip_whitespace(lines)
    yield from lines
```""",

# ────────────────────────────────────────────────

"Infinite Generators": """## Generating Values Without End

Some generators are designed to run **forever** — producing an endless stream of values. This sounds scary, but it's completely safe because generators are lazy: they only produce a value when you ask for one. You control how many values you consume.

### Why Infinite Generators?

- Infinite sequences: natural numbers, primes, Fibonacci, random numbers
- Polling loops: check a sensor every second, indefinitely
- Event processing: handle events as they arrive, without a fixed end

### A Simple Infinite Counter

```python
def counter(start=0, step=1):
    \"\"\"Counts up from start, forever.\"\"\"
    current = start
    while True:          # ← runs forever
        yield current
        current += step

# Getting values one at a time:
gen = counter(1, 2)     # Odd numbers: 1, 3, 5, 7, ...
print(next(gen))   # 1
print(next(gen))   # 3
print(next(gen))   # 5

# Getting the first N values:
from itertools import islice
first_10_odds = list(islice(counter(1, 2), 10))
print(first_10_odds)   # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

### Infinite Fibonacci

```python
def fibonacci():
    \"\"\"Generates Fibonacci numbers indefinitely.\"\"\"
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_15 = [next(fib) for _ in range(15)]
print(first_15)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

### Controlling Infinite Generators with `itertools`

The `itertools` module is the perfect companion for generators:

```python
from itertools import islice, takewhile, dropwhile, cycle

# islice — take the first N values
gen = fibonacci()
print(list(islice(gen, 10)))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# takewhile — keep taking values while condition is True
gen = fibonacci()
under_100 = list(takewhile(lambda x: x < 100, gen))
print(under_100)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# cycle — cycle through a finite sequence indefinitely
colours = cycle(['red', 'green', 'blue'])
for _ in range(7):
    print(next(colours), end=' ')
# red green blue red green blue red
```

### Infinite Polling Pattern

```python
import time

def poll_sensor(interval_seconds=1.0):
    \"\"\"Polls a sensor forever, yielding readings at each interval.\"\"\"
    import random
    while True:
        reading = random.uniform(20.0, 25.0)   # Simulate sensor
        yield reading
        time.sleep(interval_seconds)

sensor = poll_sensor(interval_seconds=0.1)

# Process readings until we get one above 24 degrees:
for reading in sensor:
    print(f'Temperature: {reading:.2f}°C')
    if reading > 24.0:
        print('Alert! High temperature detected.')
        break
```

**Safety Rule:** Never iterate an infinite generator with `list()` or a for loop without a stopping condition — that will run until your program crashes or is killed.""",

# ────────────────────────────────────────────────

"Generator Pipeline": """## Chaining Generators for Efficient Data Processing

A **generator pipeline** is a series of generators connected together, where the output of one generator flows directly into the input of the next. Data flows through the pipeline one item at a time — at no point is the entire dataset held in memory.

This is the same concept as Unix pipes: `cat file.txt | grep error | sort | uniq`.

### Building a Pipeline

```python
# Step 1: A source generator that produces raw data
def read_numbers(filename):
    \"\"\"Lazily reads numbers from a file, one per line.\"\"\"
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                yield int(line)

# Step 2: Transform stage
def square(numbers):
    \"\"\"Squares each number.\"\"\"
    for n in numbers:
        yield n ** 2

# Step 3: Filter stage
def only_large(numbers, threshold=100):
    \"\"\"Keeps only numbers above a threshold.\"\"\"
    for n in numbers:
        if n > threshold:
            yield n

# Step 4: Accumulate stage
def running_total(numbers):
    \"\"\"Yields running total after each number.\"\"\"
    total = 0
    for n in numbers:
        total += n
        yield total

# Building the pipeline — connecting generators:
def build_pipeline(filename):
    source   = read_numbers(filename)       # Raw data
    squared  = square(source)               # Transform
    filtered = only_large(squared, 100)     # Filter
    totals   = running_total(filtered)      # Accumulate
    return totals

# Consuming the pipeline:
for running_sum in build_pipeline('numbers.txt'):
    print(running_sum)

# At any given moment, only ONE number exists in memory at a time!
```

### Pipeline with a Generator Expression

For simpler pipelines, generator expressions chain naturally:

```python
import csv

# Imagine processing a 10GB log file:
def process_logs(filename):
    # Chain of generator expressions — each is lazy
    lines     = (line.strip() for line in open(filename))
    non_empty = (line for line in lines if line)
    errors    = (line for line in non_empty if 'ERROR' in line)
    parsed    = (line.split(' | ') for line in errors)
    
    for parts in parsed:
        if len(parts) >= 3:
            yield {'timestamp': parts[0], 'level': parts[1], 'message': parts[2]}

# At no point is the entire file in memory!
for error in process_logs('app.log'):
    print(error['message'])
```

### Performance: Generator Pipeline vs. List Pipeline

```python
import time, random

data = list(range(1_000_000))

# List-based: creates 3 complete lists in memory
start = time.perf_counter()
result = list(filter(lambda x: x > 100, map(lambda x: x**2, data)))
print(f'List: {time.perf_counter() - start:.3f}s, {len(result)} items')

# Generator-based: only the consumed item exists in memory
start = time.perf_counter()
result_gen = (x**2 for x in data if x**2 > 100)
count = sum(1 for _ in result_gen)
print(f'Generator: {time.perf_counter() - start:.3f}s, {count} items')
# The generator version typically uses <1MB vs dozens of MB
```""",

# ════════════════════════════════════════════════
# ASYNCIO
# ════════════════════════════════════════════════

"Async/Await Basics": """## What is Asynchronous Programming?

Imagine you're a chef in a restaurant. If you work **synchronously**, you: start boiling water → wait until it boils → add pasta → wait until pasta cooks → serve. During all that waiting, you do nothing else.

If you work **asynchronously**, while the water is boiling, you chop vegetables. While pasta cooks, you prepare the sauce. You're always doing something useful — not just waiting.

**Asyncio** brings this pattern to Python: instead of blocking and waiting during I/O operations (network requests, file reads, database queries), your program switches to doing other useful work.

### The Keywords: `async` and `await`

```python
import asyncio

# A regular function — blocks execution while running
def sync_greet(name):
    return f'Hello, {name}!'

# An async function (coroutine) — can pause and resume
async def async_greet(name):
    await asyncio.sleep(1)    # Pause here (simulate waiting for network)
    return f'Hello, {name}!'  # Resume here after 1 second

# Running an async function:
result = asyncio.run(async_greet('Alice'))
print(result)   # Hello, Alice!
```

### Key Terms

| Term | Meaning |
|---|---|
| **Coroutine** | A function defined with `async def`. It can be paused. |
| **`await`** | Pauses the current coroutine until the awaited thing finishes. Can only be used inside an `async` function. |
| **Event Loop** | The engine that manages all coroutines, deciding which one to run next. |
| **`asyncio.run()`** | Starts the event loop and runs a coroutine until it's done. |

### The Difference: Synchronous vs. Asynchronous

```python
import asyncio, time

# Synchronous (slow)
def sync_version():
    start = time.time()
    time.sleep(1)    # Task 1 — blocks for 1 second
    time.sleep(1)    # Task 2 — blocks for 1 second (sequential!)
    time.sleep(1)    # Task 3 — blocks for 1 second
    print(f'Sync done in {time.time() - start:.1f}s')  # ~3.0 seconds

# Asynchronous (fast)
async def task(name, duration):
    print(f'Task {name}: starting')
    await asyncio.sleep(duration)   # Yields control — doesn't block!
    print(f'Task {name}: done')
    return name

async def async_version():
    start = time.time()
    # Run all 3 tasks CONCURRENTLY
    results = await asyncio.gather(
        task('A', 1),
        task('B', 1),
        task('C', 1),
    )
    print(f'Async done in {time.time() - start:.1f}s')  # ~1.0 seconds!
    print(f'Results: {results}')

asyncio.run(async_version())
# Task A: starting
# Task B: starting
# Task C: starting
# Task A: done
# Task B: done
# Task C: done
# Async done in 1.0s   ← 3x faster than sequential!
```

### When to Use Asyncio

✅ **Asyncio is perfect for:**
- Making many HTTP requests (fetching URLs, calling APIs)
- Database queries
- File I/O in a web server
- Any task that involves a lot of waiting

❌ **Asyncio will NOT help with:**
- CPU-heavy computation (use `multiprocessing` instead)
- Code that doesn't involve I/O""",

# ────────────────────────────────────────────────

"Running Tasks Concurrently": """## asyncio.gather and asyncio.create_task

The real power of asyncio comes when you run multiple coroutines at the same time. Python's event loop coordinates them — while one is waiting for I/O, another runs.

### `asyncio.gather()` — Run Multiple Coroutines Together

`gather()` is the simplest way to run several coroutines concurrently and collect all their results:

```python
import asyncio
import time

async def fetch_user(user_id):
    \"\"\"Simulates fetching user data from a database.\"\"\"
    print(f'Fetching user {user_id}...')
    await asyncio.sleep(1)    # Simulates network/DB delay
    print(f'Got user {user_id}!')
    return {'id': user_id, 'name': f'User {user_id}'}

async def main():
    start = time.time()
    
    # Run all three concurrently — waits for ALL to finish
    users = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3),
    )
    
    elapsed = time.time() - start
    print(f'Fetched {len(users)} users in {elapsed:.1f}s')
    # All fetched in ~1s instead of ~3s!

asyncio.run(main())
```

### `asyncio.create_task()` — Fire and Continue

While `gather()` waits for everything together, `create_task()` starts a coroutine running in the background and returns a `Task` object immediately:

```python
import asyncio

async def background_job(name, seconds):
    print(f'{name}: starting')
    await asyncio.sleep(seconds)
    print(f'{name}: finished after {seconds}s')
    return f'{name} result'

async def main():
    # Start tasks in the background — they run concurrently
    task1 = asyncio.create_task(background_job('DataSync', 2))
    task2 = asyncio.create_task(background_job('EmailSend', 1))
    task3 = asyncio.create_task(background_job('Cleanup',  3))
    
    print('All tasks started! Doing other work...')
    await asyncio.sleep(0.1)   # Give tasks a chance to start
    print('Waiting for tasks to complete...')
    
    # Wait for specific tasks and get their results:
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(f'Results: {result1}, {result2}, {result3}')

asyncio.run(main())
```

### Handling Exceptions in Gathered Tasks

```python
import asyncio

async def risky_task(name, should_fail=False):
    await asyncio.sleep(0.5)
    if should_fail:
        raise ValueError(f'{name} encountered an error!')
    return f'{name} succeeded'

async def main():
    # By default, if one task fails, gather() raises immediately
    # Use return_exceptions=True to get results AND exceptions:
    results = await asyncio.gather(
        risky_task('Task A'),
        risky_task('Task B', should_fail=True),
        risky_task('Task C'),
        return_exceptions=True   # Don't raise — return exception as a value
    )
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f'Task {i+1} failed: {result}')
        else:
            print(f'Task {i+1}: {result}')

asyncio.run(main())
# Task 1: Task A succeeded
# Task 2 failed: Task B encountered an error!
# Task 3: Task C succeeded
```

### `asyncio.wait()` — More Control

```python
import asyncio

async def main():
    tasks = [
        asyncio.create_task(fetch_user(1)),
        asyncio.create_task(fetch_user(2)),
        asyncio.create_task(fetch_user(3)),
    ]
    
    # Wait until the FIRST task completes:
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for task in done:
        print(f'First result: {task.result()}')
    
    # Cancel the remaining pending tasks
    for task in pending:
        task.cancel()
```""",

# ────────────────────────────────────────────────

"Async Context Managers": """## Using Resources Safely in Async Code

A **context manager** (the `with` statement) ensures resources are properly cleaned up after use — even if an error occurs. The async equivalent, `async with`, works the same way but supports `await` inside the enter and exit phases.

### Why Async Context Managers?

When acquiring a resource (database connection, HTTP session, file lock) is itself an asynchronous operation, you need `async with`:

```python
import asyncio

class AsyncDBConnection:
    \"\"\"Simulates an asynchronous database connection.\"\"\"
    
    async def __aenter__(self):
        print('Connecting to database...')
        await asyncio.sleep(0.1)   # Simulate connection time
        print('Connected!')
        return self                 # Returns the connection object
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('Closing connection...')
        await asyncio.sleep(0.05)  # Simulate cleanup
        print('Connection closed.')
        return False               # Don't suppress exceptions

    async def query(self, sql):
        await asyncio.sleep(0.1)   # Simulate query time
        return f'Results of: {sql}'

async def main():
    async with AsyncDBConnection() as db:
        result = await db.query('SELECT * FROM students')
        print(result)
    # Connection is automatically closed here!

asyncio.run(main())
# Connecting to database...
# Connected!
# Results of: SELECT * FROM students
# Closing connection...
# Connection closed.
```

### `contextlib.asynccontextmanager` — The Easy Way

Instead of writing a class with `__aenter__` and `__aexit__`, use the decorator:

```python
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def managed_connection(host):
    print(f'Connecting to {host}...')
    await asyncio.sleep(0.1)
    connection = {'host': host, 'connected': True}   # Simulate a connection
    
    try:
        yield connection    # ← The 'as' variable gets this value
    finally:
        print(f'Disconnecting from {host}...')
        connection['connected'] = False

async def main():
    async with managed_connection('db.example.com') as conn:
        print(f'Using connection: {conn}')
        # Do work with conn...

asyncio.run(main())
```

### Semaphores — Limiting Concurrent Operations

An `asyncio.Semaphore` is an async context manager that limits how many coroutines can do something at the same time. Crucial for rate-limiting API calls:

```python
import asyncio, aiohttp

sem = asyncio.Semaphore(5)   # Allow at most 5 concurrent requests

async def fetch(session, url):
    async with sem:           # Only 5 can be in here at once
        async with session.get(url) as response:
            return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```""",

# ────────────────────────────────────────────────

"Async Queues": """## Coordinating Work with asyncio.Queue

An `asyncio.Queue` is a thread-safe (actually, coroutine-safe) queue that enables the classic **producer-consumer pattern** in async code. Producers put items in, consumers take items out. The queue handles coordination — consumers wait when the queue is empty, and producers wait when the queue is full.

### Basic Usage

```python
import asyncio

async def producer(queue, items):
    \"\"\"Puts items into the queue.\"\"\"
    for item in items:
        print(f'Producing: {item}')
        await queue.put(item)           # Adds an item (waits if queue is full)
        await asyncio.sleep(0.1)        # Simulate time to produce each item
    
    # Signal that production is done:
    await queue.put(None)               # Sentinel value

async def consumer(queue, consumer_id):
    \"\"\"Takes items from the queue and processes them.\"\"\"
    while True:
        item = await queue.get()        # Waits for an item to be available
        
        if item is None:               # Sentinel — production is done
            queue.task_done()
            break
        
        print(f'Consumer {consumer_id} processing: {item}')
        await asyncio.sleep(0.2)        # Simulate processing time
        queue.task_done()               # Signal that we're done with this item

async def main():
    queue = asyncio.Queue(maxsize=3)   # Max 3 items in the queue at once
    
    items = ['A', 'B', 'C', 'D', 'E', 'F']
    
    # Run producer and two consumers concurrently:
    await asyncio.gather(
        producer(queue, items),
        consumer(queue, 1),
    )

asyncio.run(main())
```

### Multiple Consumers (Worker Pool Pattern)

```python
import asyncio, random

async def worker(name, queue):
    \"\"\"A worker that processes jobs from the queue.\"\"\"
    while True:
        job = await queue.get()
        
        if job is None:           # Shutdown signal
            queue.task_done()
            break
        
        duration = random.uniform(0.1, 0.5)
        print(f'{name} processing job {job} (takes {duration:.2f}s)')
        await asyncio.sleep(duration)
        print(f'{name} finished job {job}')
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    
    # Start 3 worker coroutines:
    workers = [asyncio.create_task(worker(f'Worker-{i}', queue)) for i in range(3)]
    
    # Add 10 jobs:
    for job_id in range(10):
        await queue.put(job_id)
    
    # Wait for all jobs to be processed:
    await queue.join()    # Blocks until all items have been processed
    
    # Shut down workers:
    for _ in workers:
        await queue.put(None)
    
    await asyncio.gather(*workers)
    print('All jobs done!')

asyncio.run(main())
```

### Queue Types

| Type | Behavior |
|---|---|
| `asyncio.Queue()` | FIFO — first in, first out |
| `asyncio.LifoQueue()` | LIFO — last in, first out (like a stack) |
| `asyncio.PriorityQueue()` | Lower number = higher priority |

```python
# Priority Queue:
pq = asyncio.PriorityQueue()
await pq.put((1, 'High priority task'))
await pq.put((3, 'Low priority task'))
await pq.put((2, 'Medium priority task'))

priority, task = await pq.get()   # Gets (1, 'High priority task') first
```""",

# ────────────────────────────────────────────────

"Async Error Handling": """## Handling Errors in Async Code

Error handling in async Python works the same way as in synchronous code — you use `try/except`. The key differences are that exceptions propagate through `await` expressions, and you need to be careful when multiple tasks run concurrently.

### Basic try/except in Async Functions

```python
import asyncio

async def risky_operation(value):
    await asyncio.sleep(0.1)
    if value < 0:
        raise ValueError(f'Value must be positive, got {value}')
    return value * 2

async def safe_operation(value):
    try:
        result = await risky_operation(value)
        print(f'Success: {result}')
        return result
    except ValueError as e:
        print(f'Caught error: {e}')
        return None

async def main():
    await safe_operation(5)    # Success: 10
    await safe_operation(-3)   # Caught error: Value must be positive, got -3

asyncio.run(main())
```

### Handling Exceptions with `asyncio.gather()`

By default, `gather()` raises the first exception and cancels remaining tasks. Use `return_exceptions=True` to collect all exceptions:

```python
import asyncio

async def task(n):
    await asyncio.sleep(n * 0.1)
    if n == 2:
        raise RuntimeError('Task 2 failed!')
    return f'Task {n} completed'

async def main():
    # With return_exceptions=True — collects results and exceptions
    results = await asyncio.gather(
        task(1), task(2), task(3), task(4),
        return_exceptions=True
    )
    
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f'Task {i} error: {type(result).__name__}: {result}')
        else:
            print(f'Task {i}: {result}')

asyncio.run(main())
# Task 1: Task 1 completed
# Task 2 error: RuntimeError: Task 2 failed!
# Task 3: Task 3 completed
# Task 4: Task 4 completed
```

### Task Cancellation

Tasks can be cancelled — this raises `asyncio.CancelledError` inside the coroutine:

```python
import asyncio

async def long_running_task():
    try:
        print('Task started...')
        for i in range(10):
            await asyncio.sleep(1)
            print(f'Still running... ({i+1}/10)')
    except asyncio.CancelledError:
        print('Task was cancelled! Cleaning up...')
        # Do cleanup here (close files, connections, etc.)
        raise   # Re-raise so the cancellation propagates

async def main():
    task = asyncio.create_task(long_running_task())
    
    await asyncio.sleep(2.5)   # Let it run for 2.5 seconds
    
    task.cancel()              # Cancel it
    
    try:
        await task             # Wait for the cancellation to complete
    except asyncio.CancelledError:
        print('Main: confirmed task was cancelled')

asyncio.run(main())
```

### Timeout Handling

```python
import asyncio

async def slow_api_call():
    await asyncio.sleep(10)    # Simulates a slow API
    return 'data'

async def main():
    try:
        # Raise TimeoutError if not done in 2 seconds:
        result = await asyncio.wait_for(slow_api_call(), timeout=2.0)
        print(f'Got: {result}')
    except asyncio.TimeoutError:
        print('Request timed out after 2 seconds!')

asyncio.run(main())   # Request timed out after 2 seconds!
```""",

}

# ════════════════════════════════════════════════
# Now load, patch, and save the JSON file
# ════════════════════════════════════════════════

def patch_theory():
    print(f"Loading {TRACK_FILE}...")
    with open(TRACK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    patched = 0
    skipped = 0
    not_found = list(RICH_THEORY.keys())

    for topic, topic_data in data.items():
        for lesson in topic_data.get("lessons", []):
            title = lesson.get("title", "")
            if title in RICH_THEORY:
                old_len = len(lesson.get("theory", ""))
                lesson["theory"] = RICH_THEORY[title]
                new_len = len(lesson["theory"])
                print(f"  [OK] Patched: {title!r} ({old_len} -> {new_len} chars)")
                patched += 1
                if title in not_found:
                    not_found.remove(title)
            else:
                if lesson.get("type") != "quiz" and len(lesson.get("theory", "")) <= 800:
                    skipped += 1

    print(f"\n{'='*60}")
    print(f"Patched: {patched} lessons")
    print(f"Still needs work: {skipped} lessons")
    if not_found:
        print(f"Theory written but NOT found in JSON: {not_found}")

    with open(TRACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {TRACK_FILE}")

if __name__ == "__main__":
    patch_theory()
