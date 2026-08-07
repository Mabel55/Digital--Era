"""
enrich_python_core_part2.py
Patches rich theory into the remaining 46 python_core.json lessons.
"""
import json, os

TRACK_FILE = os.path.join("curriculum", "tracks", "python_core.json")

RICH_THEORY = {

# ════════════════════════════════════════════════
# CONTROL FLOW — already-good lessons needing top-up
# ════════════════════════════════════════════════

"If/Elif/Else Statements": """## Making Decisions in Code

Every useful program needs to make decisions. "If the user is logged in, show the dashboard. Otherwise, show the login page." Python uses `if`, `elif`, and `else` statements to make your program choose different paths based on conditions.

### Basic Syntax

```python
# Format:
# if condition:
#     code block (indented 4 spaces)

score = 75

if score >= 90:
    grade = 'A'          # Only runs if score >= 90
elif score >= 80:
    grade = 'B'          # Only runs if previous conditions were False AND this is True
elif score >= 70:
    grade = 'C'          # Only runs if all above were False AND this is True
else:
    grade = 'F'          # Runs if ALL conditions above were False

print(f'Grade: {grade}')   # Grade: C
```

**Indentation is mandatory!** Python uses 4 spaces of indentation to define what belongs inside each block. A colon (`:`) always ends the condition line.

### How Python Evaluates the Chain

Python checks each condition **from top to bottom**. The moment it finds one that is `True`, it runs that block and **skips all the rest** — even if later conditions would also be True:

```python
age = 25

if age >= 18:             # True — runs this block
    print('Adult')
elif age >= 13:           # Skipped! Even though 25 >= 13 is also True
    print('Teenager')
else:                     # Skipped
    print('Child')

# Output: Adult
```

### Conditions Can Be Any Expression That Returns True/False

```python
name = 'Alice'
courses = ['Python', 'SQL']
score = 85
logged_in = True

if name == 'Alice':          # String equality
    print('Hello, Alice!')

if len(courses) > 0:         # Checking list is not empty
    print('Enrolled in courses')

if score >= 70 and score < 90:   # Multiple conditions with 'and'
    print('B or C grade')

if not logged_in:                # Using 'not' to flip True/False
    print('Please log in')
```

### Nested If Statements

You can place `if` statements inside other `if` statements:

```python
user_type = 'admin'
is_active = True

if user_type == 'admin':
    if is_active:
        print('Active admin — full access granted')
    else:
        print('Inactive admin — access denied')
else:
    print('Regular user')
```

### One-Line Ternary Expression

For simple conditions, Python supports a compact inline syntax:

```python
age = 20
status = 'adult' if age >= 18 else 'minor'
print(status)   # adult

# Equivalent to:
if age >= 18:
    status = 'adult'
else:
    status = 'minor'
```

### Truthiness — What Counts as True?

You don't always need `== True`. Python evaluates these as False:
- `0`, `0.0`  
- `''` (empty string)  
- `[]`, `{}`, `()`, `set()` (empty collections)  
- `None`

Everything else is True:
```python
name = ''
if name:                    # False — empty string is falsy
    print('Hello,', name)
else:
    print('No name provided!')   # This runs

items = [1, 2, 3]
if items:                   # True — non-empty list is truthy
    print(f'Found {len(items)} items')
```""",

# ────────────────────────────────────────────────

"For Loops": """## Repeating Actions — For Loops

A `for` loop is how you tell Python: "Do this action for every item in this collection." It's the most common type of loop because most repetitive tasks involve processing a list, string, or range of numbers.

### Iterating Over a List

```python
fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:         # 'fruit' is a temporary variable
    print(fruit)             # Runs once per item

# apple
# banana
# cherry
# date
```

Each time through the loop, the variable `fruit` is assigned the next item from the list. The loop runs exactly as many times as there are items.

### Iterating With `range()`

`range()` generates a sequence of numbers without creating a list in memory:

```python
# range(stop) — from 0 up to (not including) stop
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# range(start, stop) — from start up to stop
for i in range(1, 6):
    print(i)
# 1, 2, 3, 4, 5

# range(start, stop, step) — with a step size
for i in range(0, 20, 5):
    print(i)
# 0, 5, 10, 15

# Counting backwards
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Iterating Over a String

Strings are sequences too — you can loop over each character:

```python
for char in 'Python':
    print(char)
# P, y, t, h, o, n
```

### `enumerate()` — Getting Index AND Value

Very commonly, you need both the position (index) and the value:

```python
fruits = ['apple', 'banana', 'cherry']

# Without enumerate — ugly:
for i in range(len(fruits)):
    print(f'{i}: {fruits[i]}')

# With enumerate — Pythonic:
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1:
for num, fruit in enumerate(fruits, start=1):
    print(f'{num}. {fruit}')
# 1. apple
# 2. banana
# 3. cherry
```

### `zip()` — Iterating Two Lists Together

```python
names = ['Alice', 'Bob', 'Carol']
scores = [92, 78, 88]

for name, score in zip(names, scores):
    grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
    print(f'{name}: {score} ({grade})')
# Alice: 92 (A)
# Bob: 78 (C)
# Carol: 88 (B)
```

### Iterating Over a Dictionary

```python
student = {'name': 'Alice', 'age': 20, 'gpa': 3.8}

# Keys only (default):
for key in student:
    print(key)

# Values only:
for value in student.values():
    print(value)

# Both keys and values:
for key, value in student.items():
    print(f'{key}: {value}')
```

### The `for/else` Pattern

Python has a unique `else` clause for loops — it runs if the loop completed without hitting a `break`:

```python
target = 42
numbers = [10, 25, 7, 99, 3]

for num in numbers:
    if num == target:
        print(f'Found {target}!')
        break
else:
    print(f'{target} not found in the list.')  # Runs only if no break

# 42 not found in the list.
```""",

# ════════════════════════════════════════════════
# FUNCTIONS
# ════════════════════════════════════════════════

"Defining Functions": """## What is a Function and Why Use One?

A **function** is a named, reusable block of code. Instead of writing the same logic 10 times in different places, you write it once as a function and call it 10 times. Functions make your code:
- **DRY** (Don't Repeat Yourself)
- **Readable** — good function names explain *what* the code does
- **Testable** — you can test one function independently
- **Maintainable** — fix it once, fixed everywhere

### Defining and Calling a Function

```python
# DEFINE a function (create the blueprint):
def greet(name):
    \"\"\"Says hello to the given name.\"\"\"    # This is a docstring
    message = f'Hello, {name}!'
    return message

# CALL a function (use the blueprint):
result = greet('Alice')
print(result)       # Hello, Alice!
print(greet('Bob')) # Hello, Bob!
```

### Anatomy of a Function

```python
def calculate_area(length, width):
#   ^^^             ^^^^^^  ^^^^^
#   keyword         name    parameters (inputs)
    area = length * width   # Function body — indented
    return area             # The output
```

- `def` — keyword that tells Python "I'm defining a function"
- Function name — follows the same rules as variable names (snake_case)
- Parameters — local variable names that receive the arguments when called
- `return` — sends a value back to the caller

### Parameters and Arguments

**Parameters** are the variables listed in the function definition.  
**Arguments** are the actual values passed when you call the function.

```python
def power(base, exponent):    # 'base' and 'exponent' are parameters
    return base ** exponent

result = power(2, 8)          # 2 and 8 are arguments
print(result)   # 256
```

### Default Parameter Values

You can give parameters a default value — making them optional when calling:

```python
def greet(name, greeting='Hello', punctuation='!'):
    return f'{greeting}, {name}{punctuation}'

print(greet('Alice'))                     # Hello, Alice!
print(greet('Bob', 'Hi'))                 # Hi, Bob!
print(greet('Carol', punctuation='.'))    # Hello, Carol.
```

### `*args` — Variable Number of Positional Arguments

```python
def sum_all(*numbers):    # *numbers collects all positional args into a tuple
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
```

### `**kwargs` — Variable Keyword Arguments

```python
def print_info(**details):    # **details collects all keyword args into a dict
    for key, value in details.items():
        print(f'  {key}: {value}')

print_info(name='Alice', age=25, city='Lagos')
# name: Alice
# age: 25
# city: Lagos
```

### The Docstring — Documenting Your Function

Always write a brief docstring explaining what the function does:

```python
def calculate_bmi(weight_kg, height_m):
    \"\"\"
    Calculate Body Mass Index (BMI).
    
    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in metres.
    
    Returns:
        float: The BMI value.
    \"\"\"
    return weight_kg / (height_m ** 2)

# Access the docstring:
print(calculate_bmi.__doc__)
help(calculate_bmi)   # Also displays it
```""",

# ════════════════════════════════════════════════
# DECORATORS
# ════════════════════════════════════════════════

"Understanding Decorators": """## What is a Decorator?

A **decorator** is a function that wraps another function to add extra behaviour — without modifying the original function's source code. Think of it like putting a gift in a box: the gift (original function) is unchanged, but the box (decorator) adds presentation, a ribbon, maybe a card.

### The Core Concept: Functions Are Objects

In Python, functions are **first-class objects** — you can pass them as arguments and return them from other functions, just like any other value:

```python
def shout(name):
    return name.upper()

def whisper(name):
    return name.lower()

def greet(name, style_function):
    return style_function(name)

print(greet('Alice', shout))     # ALICE
print(greet('Alice', whisper))   # alice
```

### Building a Decorator from Scratch

A decorator is a function that:
1. Takes a function as its argument
2. Defines a `wrapper` function inside itself
3. Adds behaviour before/after calling the original
4. Returns the wrapper

```python
import functools

def my_decorator(func):           # 1. Takes a function
    @functools.wraps(func)        # Preserves original function's name/docs
    def wrapper(*args, **kwargs): # 2. The wrapper can take any arguments
        print('Before the function')
        result = func(*args, **kwargs)  # 3. Calls the original
        print('After the function')
        return result             # 4. Returns the result
    return wrapper                # Returns the wrapper, not calling it!

def say_hello(name):
    print(f'Hello, {name}!')

# Manual decoration (what @ does behind the scenes):
say_hello = my_decorator(say_hello)
say_hello('Alice')
# Before the function
# Hello, Alice!
# After the function
```

### The `@` Syntax — Syntactic Sugar

The `@` symbol is just a cleaner way to write `func = decorator(func)`:

```python
@my_decorator        # Same as: say_hello = my_decorator(say_hello)
def say_hello(name):
    print(f'Hello, {name}!')

say_hello('Bob')
```

### Practical Decorators

#### 1. Logging Decorator

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'[LOG] {func.__name__} returned {result}')
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(3, 5)
# [LOG] Calling add with args=(3, 5), kwargs={}
# [LOG] add returned 8
```

#### 2. Validation Decorator

```python
def require_positive(func):
    @functools.wraps(func)
    def wrapper(n, *args, **kwargs):
        if n <= 0:
            raise ValueError(f'Argument must be positive, got {n}')
        return func(n, *args, **kwargs)
    return wrapper

@require_positive
def square_root(n):
    return n ** 0.5

print(square_root(16))   # 4.0
# square_root(-4)        # Raises ValueError
```

### Summary: The Three Key Takeaways

1. Decorators are functions that accept a function and return a (wrapped) function
2. Use `@functools.wraps` to preserve the wrapped function's identity
3. They're perfect for cross-cutting concerns: logging, authentication, caching, validation""",

# ════════════════════════════════════════════════
# ADVANCED PYTHON CONCURRENCY
# ════════════════════════════════════════════════

"Asyncio in Depth": """## Deep Dive: How asyncio Works Under the Hood

You've seen the basics of `async`/`await`. Now let's understand *how* asyncio actually manages concurrency, and learn the more advanced tools it provides.

### The Event Loop — The Heart of asyncio

The **event loop** is a single-threaded scheduler that manages all coroutines. It works like a traffic controller:

1. It maintains a queue of coroutines ready to run
2. It runs a coroutine until it hits an `await`
3. The coroutine yields control back to the loop ("I'm waiting for I/O")
4. The loop picks another ready coroutine and runs that
5. When the I/O completes, the original coroutine goes back in the ready queue

```python
import asyncio

async def main():
    # Getting the running loop:
    loop = asyncio.get_event_loop()
    print(f'Event loop: {loop}')
    print(f'Running: {loop.is_running()}')   # True (we're inside it)

asyncio.run(main())
```

### `asyncio.wait_for()` — Timeouts

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(10)   # Would take 10 seconds
    return 'result'

async def main():
    try:
        # Cancel if not done in 2 seconds
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
    except asyncio.TimeoutError:
        print('Operation timed out!')

asyncio.run(main())
```

### `asyncio.shield()` — Protect a Coroutine from Cancellation

```python
import asyncio

async def critical_task():
    \"\"\"This must complete — don't cancel it!\"\"\"
    print('Critical task starting...')
    await asyncio.sleep(2)
    print('Critical task done!')
    return 'critical result'

async def main():
    task = asyncio.create_task(critical_task())
    
    try:
        # Shield the task — if THIS await gets cancelled,
        # the underlying task keeps running
        result = await asyncio.shield(task)
    except asyncio.CancelledError:
        print('Shield got cancelled, but task continues...')
        result = await task   # Wait for it to finish anyway
    
    print(f'Result: {result}')

asyncio.run(main())
```

### `asyncio.Lock()` — Preventing Race Conditions

When multiple coroutines might try to modify the same data:

```python
import asyncio

lock = asyncio.Lock()
balance = 1000

async def withdraw(amount, who):
    global balance
    async with lock:    # Only one coroutine can be in here at a time
        if balance >= amount:
            print(f'{who}: withdrawing {amount}')
            await asyncio.sleep(0.1)   # Simulate processing
            balance -= amount
            print(f'{who}: done, balance = {balance}')
        else:
            print(f'{who}: insufficient funds')

async def main():
    await asyncio.gather(
        withdraw(600, 'Alice'),
        withdraw(600, 'Bob'),   # Will fail — balance won't be enough
    )

asyncio.run(main())
```

### `asyncio.Semaphore()` — Limiting Concurrent Operations

```python
import asyncio

sem = asyncio.Semaphore(3)   # Allow at most 3 concurrent operations

async def limited_task(n):
    async with sem:           # At most 3 can be here at once
        print(f'Task {n} running')
        await asyncio.sleep(1)
        print(f'Task {n} done')

async def main():
    # Launch 10 tasks, but only 3 run at a time
    await asyncio.gather(*[limited_task(i) for i in range(10)])

asyncio.run(main())
```""",

# ────────────────────────────────────────────────

"Multiprocessing Pools": """## CPU-Bound Parallelism with multiprocessing

The **Global Interpreter Lock (GIL)** prevents Python threads from running Python code in parallel. This means `threading` is fine for I/O-bound tasks (where threads wait for network/disk) but useless for CPU-bound tasks (pure computation).

**`multiprocessing`** bypasses the GIL completely by spawning **separate OS processes** — each with its own Python interpreter and memory space. True parallelism on multiple CPU cores.

### Process vs Thread vs Coroutine

| Type | Module | Good For | Parallel? |
|---|---|---|---|
| Coroutine | asyncio | I/O-bound, lots of waiting | Concurrent (not parallel) |
| Thread | threading | I/O-bound, simpler code | No (GIL) |
| Process | multiprocessing | CPU-bound computation | Yes (real parallel) |

### Basic multiprocessing.Pool

```python
import multiprocessing
import time

def cpu_intensive(n):
    \"\"\"Simulates heavy CPU work.\"\"\"
    total = 0
    for i in range(n * 1_000_000):
        total += i * i
    return total

def sequential():
    start = time.time()
    results = [cpu_intensive(n) for n in [5, 5, 5, 5]]
    print(f'Sequential: {time.time() - start:.1f}s')
    return results

def parallel():
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_intensive, [5, 5, 5, 5])
    print(f'Parallel (4 cores): {time.time() - start:.1f}s')
    return results

if __name__ == '__main__':   # REQUIRED on Windows!
    sequential()    # ~4x slower
    parallel()      # ~1x (all 4 run at same time)
```

### Pool Methods

```python
import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        
        # map() — like built-in map(), blocks until all done
        results = pool.map(square, range(10))
        print(results)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        
        # map_async() — non-blocking version
        async_result = pool.map_async(square, range(10))
        # Do other things while it runs...
        results = async_result.get(timeout=10)
        
        # starmap() — for functions with multiple arguments
        def add(a, b): return a + b
        pairs = [(1, 2), (3, 4), (5, 6)]
        results = pool.starmap(add, pairs)   # [3, 7, 11]
        
        # imap() — returns an iterator (memory efficient for large inputs)
        for result in pool.imap(square, range(1000)):
            process(result)   # Process results as they come in
```

### Sharing Data Between Processes

Processes don't share memory — you need explicit mechanisms:

```python
import multiprocessing

def worker(shared_value, lock):
    with lock:                    # Acquire lock to prevent race conditions
        shared_value.value += 1

if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)   # Shared integer
    lock = multiprocessing.Lock()
    
    processes = [
        multiprocessing.Process(target=worker, args=(counter, lock))
        for _ in range(100)
    ]
    
    for p in processes: p.start()
    for p in processes: p.join()
    
    print(f'Counter: {counter.value}')   # 100
```""",

# ════════════════════════════════════════════════
# PYTHON DESIGN PATTERNS
# ════════════════════════════════════════════════

"The Singleton Pattern": """## Ensuring Only One Instance Exists

The **Singleton** pattern ensures a class can only ever have **one instance**. No matter how many times you call the constructor, you always get back the same object. This is useful for:

- **Configuration objects** — one source of truth for app settings
- **Database connection pools** — share one pool across the whole app
- **Loggers** — one central logging system

### Problem Without Singleton

```python
class DatabasePool:
    def __init__(self):
        print('Creating new connection pool...')
        self.connections = []

# Without Singleton, every 'new' creates a separate pool:
pool1 = DatabasePool()   # Creating new connection pool...
pool2 = DatabasePool()   # Creating new connection pool...
print(pool1 is pool2)    # False — two separate objects!
```

### Implementation 1: Using `__new__`

```python
class Singleton:
    _instance = None    # Class variable — shared by all instances
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # First call — actually create an instance
            cls._instance = super().__new__(cls)
        # All subsequent calls — return the existing instance
        return cls._instance
    
    def __init__(self, value=None):
        # Only set on first init
        if not hasattr(self, '_initialized'):
            self.value = value
            self._initialized = True

s1 = Singleton('first')
s2 = Singleton('second')

print(s1 is s2)      # True — same object!
print(s1.value)      # 'first' — not overwritten by second call
print(s2.value)      # 'first' — same object
```

### Implementation 2: Using a Decorator (Cleaner)

```python
def singleton(cls):
    \"\"\"Decorator that makes any class a Singleton.\"\"\"
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Config:
    def __init__(self):
        self.debug = False
        self.db_url = 'sqlite:///app.db'
        self.secret_key = 'abc123'

c1 = Config()
c2 = Config()
print(c1 is c2)    # True
c1.debug = True
print(c2.debug)    # True — same object!
```

### Implementation 3: Module-Level Variable (Python Idiom)

The simplest Singleton in Python — just use a module-level variable. Python modules are singletons by design (only loaded once):

```python
# config.py
class _Config:
    def __init__(self):
        self.debug = False
        self.db_url = 'sqlite:///app.db'

config = _Config()   # Create exactly once at module level

# In any other file:
from config import config
config.debug = True
```

### When NOT to Use Singleton

Singletons introduce **global state**, which makes testing harder (one test can affect another through the shared instance). Consider using **dependency injection** instead for easier testing.""",

# ────────────────────────────────────────────────

"The Factory Pattern": """## Creating Objects Without Specifying Their Class

The **Factory** pattern is a design pattern that provides a method to create objects without exposing the creation logic. Instead of calling `Dog()` or `Cat()` directly, you call `AnimalFactory.create('dog')` — the factory decides what to instantiate.

### The Problem

```python
# Without a factory — tight coupling:
def create_shape(shape_type, *args):
    if shape_type == 'circle':
        return Circle(*args)
    elif shape_type == 'square':
        return Square(*args)
    elif shape_type == 'triangle':
        return Triangle(*args)
    # ❌ Every time you add a new shape, you must modify this function
```

### Simple Factory

```python
class Animal:
    def speak(self): raise NotImplementedError
    def __str__(self): return self.__class__.__name__

class Dog(Animal):
    def speak(self): return 'Woof!'

class Cat(Animal):
    def speak(self): return 'Meow!'

class Bird(Animal):
    def speak(self): return 'Tweet!'

# Factory function:
def create_animal(animal_type):
    animals = {
        'dog': Dog,
        'cat': Cat,
        'bird': Bird,
    }
    
    animal_class = animals.get(animal_type.lower())
    if animal_class is None:
        raise ValueError(f'Unknown animal type: {animal_type}')
    
    return animal_class()   # Create and return an instance

# Usage — caller doesn't know or care which class is created:
for animal_type in ['dog', 'cat', 'bird']:
    animal = create_animal(animal_type)
    print(f'{animal}: {animal.speak()}')

# Dog: Woof!
# Cat: Meow!
# Bird: Tweet!
```

### Factory Method Pattern (OOP Version)

```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotification(Notification):
    def __init__(self, email): self.email = email
    def send(self, message): print(f'Email to {self.email}: {message}')

class SMSNotification(Notification):
    def __init__(self, phone): self.phone = phone
    def send(self, message): print(f'SMS to {self.phone}: {message}')

class PushNotification(Notification):
    def __init__(self, device_id): self.device_id = device_id
    def send(self, message): print(f'Push to {self.device_id}: {message}')

class NotificationFactory:
    @staticmethod
    def create(notification_type, **kwargs):
        types = {
            'email': EmailNotification,
            'sms':   SMSNotification,
            'push':  PushNotification,
        }
        cls = types.get(notification_type)
        if not cls:
            raise ValueError(f'Unknown type: {notification_type}')
        return cls(**kwargs)

# Registering new notification types without changing the factory:
notifier = NotificationFactory.create('email', email='alice@example.com')
notifier.send('Welcome!')
# Email to alice@example.com: Welcome!

sms = NotificationFactory.create('sms', phone='+234-800-000-0000')
sms.send('Your OTP is 123456')
```

### When to Use Factory Pattern

✅ Use it when:
- You have multiple similar classes and want a single point of creation
- You want to add new types without changing calling code
- You want to hide complex creation logic""",

# ════════════════════════════════════════════════
# PYTHON TESTING FRAMEWORKS
# ════════════════════════════════════════════════

"Pytest Basics": """## Testing Your Code with pytest

**pytest** is Python's most popular testing framework. A **test** is a small piece of code that runs your function with a known input and checks that it produces the expected output. Tests are your safety net — they catch bugs early and make refactoring safe.

### Installing pytest

```bash
pip install pytest
```

### Your First Test

Create a file named `test_calculator.py` (pytest finds files starting with `test_`):

```python
# calculator.py — the code we're testing
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

# test_calculator.py — the tests
from calculator import add, divide

def test_add_two_positives():
    assert add(2, 3) == 5          # assert raises AssertionError if False

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)  # For floating point!

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        divide(10, 0)              # Expect this to raise ValueError
```

### Running pytest

```bash
# Run all tests in the current directory:
pytest

# Run tests in a specific file:
pytest test_calculator.py

# Verbose output (shows test names):
pytest -v

# Stop at the first failure:
pytest -x

# Run only tests matching a keyword:
pytest -k "add"
```

### pytest Fixtures — Reusable Setup

Fixtures provide reusable setup code that tests can share:

```python
import pytest

@pytest.fixture
def sample_students():
    \"\"\"Returns a sample list of students for testing.\"\"\"
    return [
        {'name': 'Alice', 'gpa': 3.8},
        {'name': 'Bob',   'gpa': 3.2},
        {'name': 'Carol', 'gpa': 3.9},
    ]

def test_top_student(sample_students):
    top = max(sample_students, key=lambda s: s['gpa'])
    assert top['name'] == 'Carol'
    assert top['gpa'] == 3.9

def test_passing_students(sample_students):
    passing = [s for s in sample_students if s['gpa'] >= 3.5]
    assert len(passing) == 2
```

### Parametrize — Test Many Inputs at Once

```python
import pytest

@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
# Runs 4 separate tests automatically!
```

### Best Practices

1. **Name tests clearly:** `test_add_returns_correct_sum` beats `test_1`
2. **One assertion per test** (ideally) — makes failures obvious
3. **Test edge cases:** empty lists, zero, None, very large/small numbers
4. **Test failures:** make sure your code rejects invalid input properly""",

# ════════════════════════════════════════════════
# PYTHON SECURITY PRACTICES
# ════════════════════════════════════════════════

"SQL Injection Prevention": """## The Most Critical Security Vulnerability

**SQL Injection** is consistently ranked as one of the top web security vulnerabilities. It occurs when untrusted user input is directly inserted into a SQL query, allowing attackers to manipulate the query and potentially read, modify, or delete your entire database.

### How SQL Injection Works

```python
import sqlite3

# DANGEROUS — never do this!
def get_user_UNSAFE(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Directly inserting user input into the query string:
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# Normal usage:
user = get_user_UNSAFE('alice')
# Executes: SELECT * FROM users WHERE username = 'alice'  ✅

# Malicious usage:
user = get_user_UNSAFE("' OR '1'='1")
# Executes: SELECT * FROM users WHERE username = '' OR '1'='1'
# '1'='1' is always True, so this returns ALL users!

# Even more dangerous:
user = get_user_UNSAFE("'; DROP TABLE users; --")
# Executes: SELECT * FROM users WHERE username = ''; DROP TABLE users; --
# DROPS YOUR ENTIRE TABLE!
```

### The Fix: Parameterized Queries (ALWAYS Use These)

```python
import sqlite3

def get_user_SAFE(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Use ? as a placeholder, pass values separately:
    query = 'SELECT * FROM users WHERE username = ?'
    cursor.execute(query, (username,))   # Database handles escaping safely!
    return cursor.fetchone()

# The malicious input is now just treated as literal text — not SQL:
user = get_user_SAFE("' OR '1'='1")
# Database looks for a user literally named "' OR '1'='1" — finds none
```

### With SQLAlchemy (ORM — Even Better)

SQLAlchemy's ORM handles parameterization automatically. This is the recommended approach in FastAPI and Flask projects:

```python
from sqlalchemy.orm import Session
from models import User

def get_user_by_username(db: Session, username: str):
    # ORM automatically parameterizes this — completely safe
    return db.query(User).filter(User.username == username).first()

def get_users_by_score(db: Session, min_score: int):
    return db.query(User).filter(User.score >= min_score).all()
```

### If You Must Write Raw SQL in SQLAlchemy

Use `text()` with named parameters:

```python
from sqlalchemy import text

def search_users(db: Session, keyword: str):
    # WRONG — vulnerable:
    # result = db.execute(f"SELECT * FROM users WHERE name LIKE '%{keyword}%'")
    
    # CORRECT — safe:
    result = db.execute(
        text('SELECT * FROM users WHERE name LIKE :keyword'),
        {'keyword': f'%{keyword}%'}   # Parameterized!
    )
    return result.fetchall()
```

### Other Security Best Practices

```python
# 1. Password Hashing — NEVER store plaintext passwords
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# 2. Input Validation — reject bad data before it reaches the database
def validate_username(username: str) -> bool:
    import re
    # Only allow letters, numbers, underscores, 3-20 chars
    return bool(re.match(r'^[a-zA-Z0-9_]{3,20}$', username))

# 3. Least Privilege — database user should only have needed permissions
# Create a DB user that can only SELECT/INSERT, not DROP or ALTER
```""",

# ════════════════════════════════════════════════
# STRING MANIPULATION
# ════════════════════════════════════════════════

"F-Strings": """## The Modern Way to Format Strings

**f-strings** (formatted string literals), introduced in Python 3.6, are the most readable and efficient way to embed values inside strings. You prefix the string with `f` and use `{expression}` anywhere inside.

### Basic Syntax

```python
name = 'Alice'
age = 25
score = 87.5

# The 'f' prefix makes it a formatted string literal
print(f'Hello, {name}!')                   # Hello, Alice!
print(f'{name} is {age} years old.')        # Alice is 25 years old.
print(f'Score: {score}')                   # Score: 87.5
```

### Expressions Inside Braces

You can put **any valid Python expression** inside the `{}`:

```python
x = 10
print(f'Double: {x * 2}')                 # Double: 20
print(f'Square: {x ** 2}')                # Square: 100
print(f'Is large: {x > 5}')               # Is large: True
print(f'Upper: {"hello".upper()}')         # Upper: HELLO
print(f'Length: {len("Python")}')          # Length: 6
```

### Format Specifications — Controlling Appearance

Inside the braces, use `:` to specify a format:

```python
pi = 3.14159265358979

# Number of decimal places:
print(f'{pi:.2f}')     # 3.14    — 2 decimal places, float
print(f'{pi:.4f}')     # 3.1416  — 4 decimal places
print(f'{pi:.0f}')     # 3       — 0 decimal places (rounds)

# Integer formatting:
n = 1234567
print(f'{n:,}')        # 1,234,567  — thousands separator
print(f'{n:10}')       # '   1234567' — right-align in 10-wide field
print(f'{n:<10}')      # '1234567   ' — left-align in 10-wide field
print(f'{n:010}')      # 0001234567  — zero-padded

# Percentages:
rate = 0.8523
print(f'{rate:.1%}')   # 85.2%

# Scientific notation:
big = 123456789
print(f'{big:.2e}')    # 1.23e+08
```

### Padding and Alignment

```python
# Creating a formatted table:
students = [('Alice', 95), ('Bob', 78), ('Carol', 88)]

print(f'{"Name":<10} {"Score":>6}')
print('-' * 18)
for name, score in students:
    print(f'{name:<10} {score:>6}')

# Name       Score
# ------------------
# Alice          95
# Bob            78
# Carol          88
```

### Debug Format (Python 3.8+)

Use `=` inside the brace to print the variable name AND value:

```python
x = 42
name = 'Alice'
items = [1, 2, 3]

print(f'{x=}')        # x=42
print(f'{name=}')     # name='Alice'
print(f'{items=}')    # items=[1, 2, 3]
print(f'{len(items)=}')  # len(items)=3

# Incredibly useful for debugging without print('x =', x)!
```

### Multiline f-Strings

```python
name = 'Alice'
gpa = 3.8
courses = ['Python', 'SQL', 'ML']

report = f\"\"\"
Student Report
==============
Name:    {name}
GPA:     {gpa:.2f}
Courses: {', '.join(courses)}
Status:  {'Excellent' if gpa >= 3.5 else 'Good'}
\"\"\"
print(report)
```""",

# ────────────────────────────────────────────────

"Splitting and Joining": """## Splitting Strings Apart and Joining Them Back Together

Two of the most frequently used string operations in real-world Python are `split()` (breaking a string into a list) and `join()` (combining a list into a string). They're perfect inverses of each other.

### `str.split()` — String to List

`split()` divides a string into parts based on a separator:

```python
# Split on whitespace (default — any whitespace, any amount)
sentence = 'Python is an amazing language'
words = sentence.split()
print(words)   # ['Python', 'is', 'an', 'amazing', 'language']

# Split on a specific separator:
csv_line = 'Alice,25,Lagos,3.8'
parts = csv_line.split(',')
print(parts)   # ['Alice', '25', 'Lagos', '3.8']

name, age, city, gpa = csv_line.split(',')   # Unpack directly!
print(f'{name} from {city}, GPA: {gpa}')

# Split on multi-char separator:
path = 'home/user/documents/report.pdf'
components = path.split('/')
print(components)   # ['home', 'user', 'documents', 'report.pdf']

# Limit the number of splits:
text = 'one:two:three:four'
print(text.split(':', 1))    # ['one', 'two:three:four'] — only first split
print(text.split(':', 2))    # ['one', 'two', 'three:four']
```

### `str.splitlines()` — Split on Line Boundaries

```python
multiline = \"\"\"Line one
Line two
Line three\"\"\"

lines = multiline.splitlines()
print(lines)   # ['Line one', 'Line two', 'Line three']
# splitlines() handles \\n, \\r\\n, \\r, etc. automatically
```

### `str.join()` — List to String

`join()` is called on the **separator** string, with the list as the argument:

```python
words = ['Python', 'is', 'amazing']

# Join with space:
sentence = ' '.join(words)
print(sentence)   # Python is amazing

# Join with comma and space:
csv = ', '.join(words)
print(csv)   # Python, is, amazing

# Join with no separator:
letters = ['P', 'y', 't', 'h', 'o', 'n']
word = ''.join(letters)
print(word)   # Python

# Join with newline (great for writing files):
lines = ['First line', 'Second line', 'Third line']
content = '\n'.join(lines)
print(content)
# First line
# Second line
# Third line
```

### The Split → Process → Join Pattern

This is one of the most common patterns in text processing:

```python
# Capitalize each word in a sentence:
sentence = 'python is amazing'
words = sentence.split()                   # 1. Split
words = [w.capitalize() for w in words]   # 2. Process
result = ' '.join(words)                  # 3. Join
print(result)   # Python Is Amazing

# Or more concisely:
result = ' '.join(w.capitalize() for w in sentence.split())

# Remove duplicate spaces:
messy = 'Python   is    amazing'
clean = ' '.join(messy.split())   # split() on whitespace discards extras
print(clean)   # Python is amazing

# Reverse the words in a sentence:
reversed_sentence = ' '.join(sentence.split()[::-1])
print(reversed_sentence)   # amazing is python
```

### Building Strings Efficiently

When building a string by concatenating many pieces, `join()` is dramatically faster than `+=` in a loop:

```python
# ❌ Slow — creates a new string object every iteration
parts = []
result = ''
for i in range(10000):
    result += str(i)   # Creates 10,000 intermediate strings!

# ✅ Fast — collect first, join once
parts = [str(i) for i in range(10000)]
result = ''.join(parts)   # One string creation
```""",

# ════════════════════════════════════════════════
# ERROR HANDLING
# ════════════════════════════════════════════════

"Try Except Blocks": """## Handling Errors Gracefully

In real programs, things go wrong all the time: a file doesn't exist, the network is down, the user types invalid input, a division by zero occurs. A well-written program **anticipates** these failures and handles them gracefully instead of crashing.

### The try/except Structure

```python
# Without error handling — crashes on invalid input:
age = int('not a number')   # ValueError: invalid literal for int()

# With error handling:
try:
    age = int('not a number')
    print(f'Age: {age}')
except ValueError:
    print('That was not a valid number!')

print('Program continues...')   # This runs even after the exception
```

How it works:
1. Python **tries** to run the code in the `try` block
2. If an exception occurs, it **immediately** jumps to the matching `except` block
3. After the `except` block, program continues normally

### Catching Specific Exceptions

Always catch the **most specific** exception you expect:

```python
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Cannot divide by zero! → None
```

### Catching Multiple Exception Types

```python
def convert_and_divide(a_str, b_str):
    try:
        a = int(a_str)
        b = int(b_str)
        result = a / b
        return result
    except ValueError:
        print('Both inputs must be numbers')
        return None
    except ZeroDivisionError:
        print('Second number cannot be zero')
        return None

# Catch multiple in one line:
try:
    risky_code()
except (TypeError, ValueError, AttributeError) as e:
    print(f'One of those errors: {e}')
```

### The `as e` — Getting Error Details

```python
try:
    with open('missing.txt') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f'Error: {e}')
    # Error: [Errno 2] No such file or directory: 'missing.txt'
    print(f'Error type: {type(e).__name__}')   # FileNotFoundError
    print(f'Error code: {e.errno}')             # 2
```

### The `else` Clause — Code That Runs When No Error Occurred

```python
try:
    result = int(input('Enter a number: '))
except ValueError:
    print('Not a valid number!')
else:
    # Only runs if the try block succeeded (no exception)
    print(f'You entered: {result}')
    print(f'Doubled: {result * 2}')
```

### Common Exception Types

| Exception | Cause |
|---|---|
| `ValueError` | Wrong value type (e.g., `int('abc')`) |
| `TypeError` | Wrong type entirely (e.g., `'5' + 5`) |
| `KeyError` | Dictionary key doesn't exist |
| `IndexError` | List index out of range |
| `AttributeError` | Object doesn't have that attribute |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `ImportError` | Module not found |
| `PermissionError` | No permission to access file |
| `TimeoutError` | Operation timed out |""",

# ────────────────────────────────────────────────

"Finally Clause": """## Code That Always Runs

The `finally` block runs **no matter what** — whether the try block succeeded, an exception was raised and caught, or even if the exception was NOT caught. It's the guaranteed cleanup zone.

### Basic Structure

```python
try:
    # Risky code
    result = 10 / 2
except ZeroDivisionError:
    print('Division error!')
finally:
    print('This ALWAYS runs!')   # Runs whether or not there was an error

# Output:
# This ALWAYS runs!   (no error occurred, but finally still ran)
```

```python
try:
    result = 10 / 0    # This raises ZeroDivisionError
except ZeroDivisionError:
    print('Division error!')
finally:
    print('This ALWAYS runs!')

# Output:
# Division error!
# This ALWAYS runs!   (ran after the except block)
```

### When finally Is Essential: Resource Cleanup

The most important use of `finally` is ensuring resources (file handles, database connections, network sockets) are properly released:

```python
# Without finally — if an error occurs, the file stays open (resource leak!)
file = open('data.txt', 'r')
try:
    content = file.read()
    process(content)
except IOError:
    print('Failed to read')
finally:
    file.close()   # ALWAYS closes the file, even if process() crashes

# But the 'with' statement does this automatically (preferred approach):
with open('data.txt', 'r') as file:
    content = file.read()
    process(content)
# File is automatically closed here, error or not
```

### Complete try/except/else/finally

```python
def load_and_process(filename):
    file = None
    
    try:
        print(f'Opening {filename}...')
        file = open(filename, 'r')
        data = file.read()
        result = process_data(data)   # Might raise ValueError
    
    except FileNotFoundError:
        print(f'File not found: {filename}')
        result = None
    
    except ValueError as e:
        print(f'Data processing error: {e}')
        result = None
    
    else:
        # Only runs if NO exception occurred
        print(f'Successfully processed {len(data)} characters')
    
    finally:
        # ALWAYS runs — perfect for cleanup
        if file and not file.closed:
            file.close()
            print('File closed.')
    
    return result
```

### finally Runs Even After return!

This surprises many developers:

```python
def example():
    try:
        print('In try')
        return 'from try'    # Return is attempted here
    finally:
        print('In finally')  # Runs BEFORE the function actually returns!

result = example()
# In try
# In finally
print(result)   # from try
```

### The Pattern: Setup → Work → Teardown

```python
class DatabaseConnection:
    def __init__(self):
        print('Connecting...')
        self.connected = True
    
    def query(self, sql):
        if not self.connected:
            raise RuntimeError('Not connected')
        return f'Results of: {sql}'
    
    def close(self):
        self.connected = False
        print('Disconnected.')

conn = None
try:
    conn = DatabaseConnection()
    result = conn.query('SELECT * FROM users')
    print(result)
except RuntimeError as e:
    print(f'Query failed: {e}')
finally:
    if conn and conn.connected:
        conn.close()   # Always disconnect
```""",

# ════════════════════════════════════════════════
# LIST COMPREHENSIONS (intermediate topics)
# ════════════════════════════════════════════════

"Compact Loops": """## List Comprehensions — The Pythonic Loop

A **list comprehension** creates a new list by applying an expression to each item in an existing sequence, all in a single clean line. It's faster than an equivalent for loop and is considered the "Pythonic" way to create lists.

### From Loop to Comprehension

```python
# Standard for loop:
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent list comprehension:
squares = [x ** 2 for x in range(10)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Read it as:** "Give me `x squared` for each `x` in `range(10)`"

### The Format

```
[  expression  for  item  in  iterable  ]
```

- `expression` — what to compute for each item
- `for item in iterable` — the loop

### More Examples

```python
# Double every number:
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)   # [2, 4, 6, 8, 10]

# Get word lengths:
words = ['hello', 'world', 'python']
lengths = [len(w) for w in words]
print(lengths)   # [5, 5, 6]

# Convert to uppercase:
names = ['alice', 'bob', 'carol']
upper = [name.upper() for name in names]
print(upper)   # ['ALICE', 'BOB', 'CAROL']

# Convert all items in a CSV row to integers:
csv_row = ['10', '25', '38', '42']
numbers = [int(n) for n in csv_row]
print(numbers)   # [10, 25, 38, 42]
print(sum(numbers))   # 115
```

### Using Functions in Comprehensions

```python
import math

data = [1, 4, 9, 16, 25, 36]
roots = [math.sqrt(n) for n in data]
print(roots)   # [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

# Your own function:
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

temps_celsius = [0, 20, 37, 100]
temps_fahrenheit = [celsius_to_fahrenheit(c) for c in temps_celsius]
print(temps_fahrenheit)   # [32.0, 68.0, 98.6, 212.0]
```

### When Comprehensions Are Better Than Loops

Comprehensions are preferred when:
1. You're creating a list from another sequence
2. The transformation is simple (one expression)
3. The result fits on one readable line

```python
# Loop (fine for complex logic):
result = []
for item in data:
    processed = complex_multi_step_process(item)
    if processed.is_valid():
        result.append(processed.value)

# Comprehension (better for simple transformations):
result = [x ** 2 for x in range(100)]
```""",

# ────────────────────────────────────────────────

"Adding Conditions": """## Filtering with List Comprehensions

You can add an `if` condition to a list comprehension to filter out items that don't meet a criterion. Only items where the condition is `True` will be included in the result.

### Basic Filtering

```python
# Format: [expression for item in iterable if condition]

numbers = range(1, 21)

# Only even numbers:
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Only odd numbers:
odds = [n for n in numbers if n % 2 != 0]
print(odds)   # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Only numbers divisible by 3:
threes = [n for n in range(1, 31) if n % 3 == 0]
print(threes)   # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

### Filtering Strings

```python
words = ['python', 'java', 'go', 'rust', 'javascript', 'c', 'kotlin']

# Only long words (more than 4 characters):
long_words = [w for w in words if len(w) > 4]
print(long_words)   # ['python', 'javascript', 'kotlin']

# Words starting with specific letters:
j_words = [w for w in words if w.startswith('j')]
print(j_words)   # ['java', 'javascript']

# Words that contain 'o':
with_o = [w for w in words if 'o' in w]
print(with_o)   # ['python', 'go', 'kotlin']
```

### Filtering Lists of Dictionaries

This is very common when processing API data or database results:

```python
students = [
    {'name': 'Alice', 'score': 92, 'level': 'Advanced'},
    {'name': 'Bob',   'score': 55, 'level': 'Beginner'},
    {'name': 'Carol', 'score': 78, 'level': 'Intermediate'},
    {'name': 'Dave',  'score': 45, 'level': 'Beginner'},
    {'name': 'Eve',   'score': 88, 'level': 'Advanced'},
]

# Passing students only:
passing = [s for s in students if s['score'] >= 70]
print([s['name'] for s in passing])   # ['Alice', 'Carol', 'Eve']

# Advanced students:
advanced = [s['name'] for s in students if s['level'] == 'Advanced']
print(advanced)   # ['Alice', 'Eve']

# Both transform AND filter:
names_of_passing = [s['name'].upper() for s in students if s['score'] >= 70]
print(names_of_passing)   # ['ALICE', 'CAROL', 'EVE']
```

### Multiple Conditions

```python
numbers = range(1, 101)

# Numbers divisible by both 3 and 5 (FizzBuzz!):
fizzbuzz = [n for n in numbers if n % 3 == 0 and n % 5 == 0]
print(fizzbuzz)   # [15, 30, 45, 60, 75, 90]

# Scores between 70 and 90 (inclusive):
scores = [55, 70, 85, 92, 78, 45, 88, 91]
b_grade = [s for s in scores if 80 <= s <= 89]
print(b_grade)   # [85, 88]
```

### Conditional Expression (if/else in the Expression Part)

Note: `if/else` in the **expression** is different from `if` in the **filter**:

```python
scores = [55, 70, 85, 92, 78, 45, 88]

# Filter (if at the end) — only includes passing scores:
passing = [s for s in scores if s >= 70]
# [70, 85, 92, 78, 88]

# Transform (if/else in the expression) — all items kept, but transformed:
graded = ['Pass' if s >= 70 else 'Fail' for s in scores]
# ['Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass']
```""",

# ════════════════════════════════════════════════
# CONTEXT MANAGERS
# ════════════════════════════════════════════════

"The With Statement": """## Automatic Resource Management

The `with` statement is Python's elegant solution for managing resources that need to be properly acquired and then released — no matter what happens in between. Files, database connections, network sockets, locks, and more.

### The Problem with Manual Resource Management

```python
# Without 'with' — easy to forget to close:
file = open('data.txt', 'r')
# What if an exception happens here? The file stays open!
content = file.read()
file.close()   # May never be reached if exception occurred above

# Even with try/finally — verbose:
file = open('data.txt', 'r')
try:
    content = file.read()
finally:
    file.close()   # Guaranteed, but lots of boilerplate
```

### The Solution: The `with` Statement

```python
# Clean, safe, automatic:
with open('data.txt', 'r') as file:
    content = file.read()
# File is automatically closed here — guaranteed, even if read() raises!
```

The `with` statement guarantees that the resource is properly released when the block exits, whether normally or due to an exception.

### How It Works: Context Manager Protocol

Any object with `__enter__` and `__exit__` methods can be used with `with`:

- `__enter__` — called when entering the `with` block. Return value becomes the `as` variable.
- `__exit__` — called when leaving the block (normally or via exception). Used for cleanup.

```python
# Behind the scenes, 'with open(...) as f' is equivalent to:
file = open('data.txt', 'r')
file.__enter__()    # Sets up the file
try:
    content = file.read()
finally:
    file.__exit__(...)   # Closes the file
```

### Common Built-in Context Managers

```python
# 1. Files
with open('output.txt', 'w') as f:
    f.write('Hello!')

# 2. Multiple files at once
with open('input.txt') as src, open('output.txt', 'w') as dst:
    dst.write(src.read())

# 3. Threading locks
import threading
lock = threading.Lock()
with lock:
    # Only one thread can be in here at a time
    shared_data += 1

# 4. Decimal precision
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec = 50   # 50 decimal places of precision
    result = Decimal('1') / Decimal('3')
    print(result)   # 0.33333333333333333333333333333333333333333333333333

# 5. Temporary directory
import tempfile, os
with tempfile.TemporaryDirectory() as tmpdir:
    path = os.path.join(tmpdir, 'test.txt')
    with open(path, 'w') as f:
        f.write('temporary data')
# Directory and its contents are automatically deleted here
```

### Suppressing Exceptions with contextlib.suppress

```python
from contextlib import suppress

# Without suppress:
try:
    os.remove('maybe_exists.txt')
except FileNotFoundError:
    pass   # We don't care if it doesn't exist

# With suppress — cleaner:
with suppress(FileNotFoundError):
    os.remove('maybe_exists.txt')
```""",

# ────────────────────────────────────────────────

"Custom Context Managers": """## Building Your Own Context Managers

You can create custom context managers to make any resource management code cleaner. There are two ways: using a class with `__enter__`/`__exit__`, or using the `@contextmanager` decorator.

### Method 1: Class-Based Context Manager

```python
import time

class Timer:
    \"\"\"Context manager that measures elapsed time.\"\"\"
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self    # This becomes the 'as' variable
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f'Elapsed: {self.elapsed:.4f}s')
        # exc_type, exc_val, exc_tb: exception info (None if no exception)
        # Return False (or None) to NOT suppress exceptions
        return False

# Usage:
with Timer() as t:
    sum(range(1_000_000))

print(f'Stored elapsed: {t.elapsed:.4f}s')

# With an exception — __exit__ still runs:
with Timer():
    time.sleep(0.5)
    # Even if an exception occurred, elapsed time would print
```

### Understanding `__exit__` Parameters

```python
class ErrorHandler:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type: the exception class (e.g., ValueError)
        # exc_val: the exception instance
        # exc_tb: the traceback object
        
        if exc_type is None:
            print('No exception occurred')
            return False
        
        if exc_type is ValueError:
            print(f'Caught a ValueError: {exc_val}')
            return True   # True = suppress the exception (don't re-raise)
        
        print(f'Unhandled exception: {exc_type.__name__}: {exc_val}')
        return False   # False = let the exception propagate

with ErrorHandler():
    raise ValueError('test error')   # Suppressed by __exit__!

print('Program continues...')
```

### Method 2: `@contextmanager` Decorator (Simpler)

The `contextlib.contextmanager` decorator lets you write context managers as generator functions. Everything before `yield` is `__enter__`, everything after is `__exit__`:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name=''):
    start = time.perf_counter()
    try:
        yield    # ← Execution pauses here; 'with' block runs
    finally:
        elapsed = time.perf_counter() - start
        label = f'[{name}] ' if name else ''
        print(f'{label}Elapsed: {elapsed:.4f}s')

@contextmanager
def temp_directory():
    import tempfile, shutil
    tmpdir = tempfile.mkdtemp()
    try:
        yield tmpdir   # ← The yielded value becomes the 'as' variable
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

# Usage:
with timer('sorting'):
    sorted(range(1_000_000), reverse=True)
# [sorting] Elapsed: 0.0634s

with temp_directory() as tmpdir:
    print(f'Working in: {tmpdir}')
    # Create temp files here
# Directory automatically deleted
```

### A Database Transaction Context Manager

```python
from contextlib import contextmanager

@contextmanager
def transaction(db_connection):
    \"\"\"Automatically commits on success, rolls back on error.\"\"\"
    try:
        yield db_connection.cursor()
        db_connection.commit()      # Success — commit the changes
        print('Transaction committed.')
    except Exception as e:
        db_connection.rollback()    # Error — undo all changes
        print(f'Transaction rolled back: {e}')
        raise

# Usage:
with transaction(conn) as cursor:
    cursor.execute('INSERT INTO users VALUES (?, ?)', ('Alice', 25))
    cursor.execute('INSERT INTO users VALUES (?, ?)', ('Bob', 30))
# Either BOTH inserts succeed, or NEITHER does
```""",

# ════════════════════════════════════════════════
# CONCURRENCY & ASYNCIO
# ════════════════════════════════════════════════

"Async/Await": """## Concurrency Without Threads

**Asynchronous programming** lets your program do multiple things at once — not by running them truly in parallel (that's multiprocessing), but by *interleaving* tasks during their waiting time.

### The Key Insight

Most I/O operations (network requests, file reads, database queries) spend most of their time **waiting**. Asyncio lets your program switch to other work during that waiting time.

```python
import asyncio

# Mark a function as async — it becomes a coroutine
async def fetch_data(url):
    print(f'Starting fetch: {url}')
    await asyncio.sleep(2)    # 'await' says "pause here, do other things"
    print(f'Done: {url}')
    return f'Data from {url}'

# Must run async functions with asyncio.run():
result = asyncio.run(fetch_data('https://api.example.com'))
print(result)
```

### `async def` vs Regular `def`

```python
# Regular function — blocks everything while running
def sync_func():
    time.sleep(1)    # The entire program freezes for 1 second
    return 'done'

# Async function — pauses and yields control while waiting
async def async_func():
    await asyncio.sleep(1)   # Pauses this function; event loop can run others
    return 'done'
```

### Running Multiple Coroutines Concurrently

```python
import asyncio

async def task(name, seconds):
    print(f'{name}: started')
    await asyncio.sleep(seconds)
    print(f'{name}: finished')
    return f'{name} result'

async def main():
    # gather() runs all coroutines CONCURRENTLY
    results = await asyncio.gather(
        task('Alpha', 1),
        task('Beta', 2),
        task('Gamma', 1.5),
    )
    print(f'All done: {results}')

asyncio.run(main())
# Alpha: started
# Beta: started
# Gamma: started
# Alpha: finished  (after 1s)
# Gamma: finished  (after 1.5s)
# Beta: finished   (after 2s)
# All done: ['Alpha result', 'Beta result', 'Gamma result']
# Total time: ~2s instead of 4.5s!
```

### When to Use asyncio

| Scenario | Use asyncio? |
|---|---|
| Making many HTTP requests | ✅ Yes |
| Reading/writing many files | ✅ Yes |
| Database queries in a web server | ✅ Yes |
| Heavy math/computation | ❌ No — use multiprocessing |
| Simple sequential script | ❌ No — overkill |""",

# ────────────────────────────────────────────────

"Awaiting Coroutines": """## How `await` Works

The `await` keyword is the mechanism that makes async Python tick. It can only be used inside `async def` functions, and it tells the event loop "I'm pausing — you can run other coroutines while I wait."

### What Can You `await`?

You can `await` any **awaitable** object:
1. **Coroutines** — other `async def` functions
2. **Tasks** — coroutines wrapped with `asyncio.create_task()`
3. **Futures** — low-level async primitives
4. **Objects with `__await__`** — asyncio-compatible classes

```python
import asyncio

async def step_one():
    await asyncio.sleep(0.5)   # Awaiting a coroutine (asyncio.sleep)
    return 'Step 1 done'

async def step_two():
    result = await step_one()  # Awaiting our own coroutine
    print(result)
    return 'Step 2 done'

async def main():
    # Awaiting a task:
    task = asyncio.create_task(step_one())   # Start running in background
    # Do other work here...
    await asyncio.sleep(0.1)                  # Some other work
    result = await task                       # Now wait for the task
    print(result)

asyncio.run(main())
```

### Sequential vs Concurrent Awaiting

This is the #1 source of asyncio confusion:

```python
import asyncio

async def slow(name, seconds):
    await asyncio.sleep(seconds)
    return name

async def sequential():
    \"\"\"Awaiting one at a time — NOT concurrent, runs sequentially!\"\"\"
    r1 = await slow('A', 1)   # Wait 1 second...
    r2 = await slow('B', 1)   # ...THEN wait another second
    r3 = await slow('C', 1)   # ...THEN another
    # Total time: ~3 seconds
    return [r1, r2, r3]

async def concurrent():
    \"\"\"Using gather — truly concurrent!\"\"\"
    results = await asyncio.gather(
        slow('A', 1),   # All three start at the same time
        slow('B', 1),
        slow('C', 1),
    )
    # Total time: ~1 second
    return results

import time

start = time.time()
asyncio.run(sequential())
print(f'Sequential: {time.time() - start:.1f}s')   # 3.0s

start = time.time()
asyncio.run(concurrent())
print(f'Concurrent: {time.time() - start:.1f}s')   # 1.0s
```

### Real-World Example: Fetching Multiple URLs

```python
import asyncio
import aiohttp   # pip install aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)   # All fetched concurrently!
    return pages

urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
]

# Fetches all 3 in ~1 second instead of ~3 seconds:
results = asyncio.run(fetch_all(urls))
```""",

# ════════════════════════════════════════════════
# DICTIONARIES & SETS
# ════════════════════════════════════════════════

"Key-Value Pairs": """## Dictionaries — Fast Lookup by Name

A **dictionary** is Python's most powerful and versatile data structure. It stores data as **key-value pairs** — like a real-world dictionary where each word (key) has a definition (value). You can instantly look up any value by its key in O(1) time, regardless of how many items there are.

### Creating Dictionaries

```python
# Literal syntax (most common):
student = {
    'name': 'Alice',
    'age': 25,
    'gpa': 3.8,
    'courses': ['Python', 'SQL', 'ML'],
    'graduated': False
}

# From keyword arguments:
point = dict(x=10, y=20)

# From a list of key-value pairs:
config = dict([('host', 'localhost'), ('port', 5432)])

# Empty dictionary:
empty = {}
empty2 = dict()
```

### Accessing Values

```python
student = {'name': 'Alice', 'age': 25, 'gpa': 3.8}

# By key — raises KeyError if key doesn't exist:
print(student['name'])    # Alice
print(student['age'])     # 25
# print(student['city'])  # ❌ KeyError

# With .get() — safe, returns None (or your default) if key doesn't exist:
print(student.get('name'))         # Alice
print(student.get('city'))         # None  (no error!)
print(student.get('city', 'N/A'))  # N/A   (custom default)
```

### Adding, Updating, and Removing

```python
student = {'name': 'Alice', 'age': 25}

# Add or update:
student['gpa'] = 3.8         # Add new key
student['age'] = 26          # Update existing key
student.update({'city': 'Lagos', 'level': 'Advanced'})   # Add/update multiple

# Remove:
del student['age']           # Removes 'age' — KeyError if missing
removed = student.pop('gpa', None)   # Removes and returns value (safe)

print(student)
```

### Iterating Over a Dictionary

```python
data = {'name': 'Alice', 'score': 92, 'grade': 'A'}

# Iterate over keys (default):
for key in data:
    print(key)

# Iterate over values:
for value in data.values():
    print(value)

# Iterate over key-value pairs (most common):
for key, value in data.items():
    print(f'{key}: {value}')
```

### Dictionary Comprehensions

```python
names = ['alice', 'bob', 'carol']
scores = [92, 78, 88]

# Build a dict from two lists:
gradebook = {name: score for name, score in zip(names, scores)}
print(gradebook)   # {'alice': 92, 'bob': 78, 'carol': 88}

# Build a dict with a condition:
passing = {name: score for name, score in gradebook.items() if score >= 80}
print(passing)   # {'alice': 92, 'carol': 88}

# Invert a dictionary (swap keys and values):
inverted = {v: k for k, v in gradebook.items()}
print(inverted)   # {92: 'alice', 78: 'bob', 88: 'carol'}
```

### Common Dictionary Methods

```python
d = {'a': 1, 'b': 2, 'c': 3}

print(d.keys())       # dict_keys(['a', 'b', 'c'])
print(d.values())     # dict_values([1, 2, 3])
print(d.items())      # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(len(d))         # 3
print('a' in d)       # True (checks keys)
d.setdefault('d', 0) # Add 'd' with value 0 if 'd' not present
d2 = d.copy()         # Shallow copy
d.clear()             # Remove all items
```""",

# ────────────────────────────────────────────────

"Unique Elements": """## Sets — Collections Without Duplicates

A **set** is an unordered collection of **unique** elements. If you add a duplicate, it's silently ignored. Sets are blazing fast at membership testing (checking if something is in the set) and are perfect for deduplication and mathematical set operations.

### Creating Sets

```python
# Literal syntax — curly braces (like dict, but no key-value pairs):
fruits = {'apple', 'banana', 'cherry'}
print(fruits)   # {'apple', 'banana', 'cherry'} (order may vary — sets are unordered)

# Duplicates are automatically removed:
numbers = {1, 2, 3, 2, 1, 3, 4}
print(numbers)   # {1, 2, 3, 4}

# From a list — the easiest way to remove duplicates:
data = [1, 5, 3, 1, 2, 5, 3, 7, 2]
unique = set(data)
print(unique)   # {1, 2, 3, 5, 7}

# IMPORTANT: Empty set must use set() — {} creates an empty DICT!
empty = set()
print(type(empty))   # <class 'set'>
```

### Membership Testing — The Main Advantage

Sets check membership in O(1) time — instantly, regardless of size. Lists take O(n) — they scan every element.

```python
# Slow for large collections:
allowed_users_list = ['alice', 'bob', 'carol', ...]   # 10,000 users
'alice' in allowed_users_list    # Scans from the beginning — slow!

# Fast — always instant:
allowed_users_set = {'alice', 'bob', 'carol', ...}
'alice' in allowed_users_set    # Hash lookup — O(1) time!
```

### Adding and Removing Elements

```python
tags = {'python', 'coding'}

tags.add('beginner')          # Add one item
tags.update({'web', 'api'})   # Add multiple items

tags.remove('coding')         # Remove — raises KeyError if not found
tags.discard('missing')       # Remove — no error if not found
popped = tags.pop()           # Remove and return an arbitrary item

print(len(tags))   # Number of items
```

### Set Operations — Like Venn Diagrams

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — everything in A OR B:
print(a | b)         # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))    # Same

# Intersection — only in BOTH A and B:
print(a & b)              # {4, 5}
print(a.intersection(b))  # Same

# Difference — in A but NOT in B:
print(a - b)            # {1, 2, 3}
print(a.difference(b))  # Same

# Symmetric Difference — in one but NOT both:
print(a ^ b)                      # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))  # Same

# Subset / Superset:
small = {1, 2, 3}
large = {1, 2, 3, 4, 5}
print(small.issubset(large))      # True — all of small is in large
print(large.issuperset(small))    # True — large contains all of small
print(small.isdisjoint({9, 10}))  # True — no common elements
```

### Practical: Deduplicating and Finding Common Items

```python
# Remove duplicates from a list (preserving order in Python 3.7+):
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = list(dict.fromkeys(data))   # Preserves order
print(unique)   # [3, 1, 4, 5, 9, 2, 6]

# Find common elements across multiple lists:
list1 = ['python', 'java', 'go']
list2 = ['python', 'rust', 'go']
list3 = ['python', 'c', 'go']
common = set(list1) & set(list2) & set(list3)
print(common)   # {'python', 'go'}
```""",

# ════════════════════════════════════════════════
# LAMBDA FUNCTIONS & MAP/FILTER
# ════════════════════════════════════════════════

"Anonymous Functions": """## Lambda Functions — Throwaway Functions

A **lambda function** is a small, anonymous (unnamed) function created in a single expression. It's called anonymous because you don't need to give it a name with `def`. Lambdas are throwaway functions for simple, one-off operations.

### Syntax

```python
# Regular function:
def square(x):
    return x ** 2

# Equivalent lambda:
square = lambda x: x ** 2

# Format: lambda parameters: expression
# The expression is automatically returned — no 'return' keyword needed
```

### Lambda vs def

| Feature | `def` | `lambda` |
|---|---|---|
| Name | Has a name | Anonymous |
| Lines | Multiple allowed | Single expression only |
| `return` | Explicit | Automatic |
| Docstring | Can have one | Cannot |
| Complexity | Unlimited | One expression |

### Basic Lambdas

```python
# Single parameter:
double = lambda x: x * 2
print(double(7))          # 14

# Two parameters:
add = lambda x, y: x + y
print(add(3, 5))          # 8

# Three parameters:
describe = lambda name, age, city: f'{name} ({age}) from {city}'
print(describe('Alice', 25, 'Lagos'))   # Alice (25) from Lagos

# With a conditional expression:
grade = lambda score: 'Pass' if score >= 70 else 'Fail'
print(grade(85))   # Pass
print(grade(55))   # Fail
```

### The Real Use: As Arguments to Other Functions

Lambdas are most powerful when passed directly as arguments:

```python
# sorted() with a custom key:
students = [
    {'name': 'Alice', 'gpa': 3.5},
    {'name': 'Bob',   'gpa': 3.9},
    {'name': 'Carol', 'gpa': 3.1},
]

# Sort by GPA ascending:
by_gpa = sorted(students, key=lambda s: s['gpa'])
for s in by_gpa: print(s['name'], s['gpa'])
# Carol 3.1, Alice 3.5, Bob 3.9

# Sort by GPA descending:
by_gpa_desc = sorted(students, key=lambda s: s['gpa'], reverse=True)

# Sort strings by length:
words = ['banana', 'apple', 'kiwi', 'watermelon']
by_length = sorted(words, key=lambda w: len(w))
print(by_length)   # ['kiwi', 'apple', 'banana', 'watermelon']

# Sort by multiple criteria (tuple — Python sorts tuples element by element):
people = [('Alice', 30), ('Bob', 25), ('Alice', 25)]
sorted_people = sorted(people, key=lambda p: (p[0], p[1]))
# [('Alice', 25), ('Alice', 30), ('Bob', 25)]
```

### When to Prefer List Comprehensions Over lambda

In Python, list comprehensions are often cleaner than `map()`/`filter()` with lambdas:

```python
numbers = [1, 2, 3, 4, 5]

# Lambda + map (okay):
doubled = list(map(lambda x: x * 2, numbers))

# List comprehension (often more readable):
doubled = [x * 2 for x in numbers]

# Both are valid — choose whichever reads better
```""",

# ────────────────────────────────────────────────

"Map and Filter": """## map() and filter() — Functional Programming Tools

`map()` and `filter()` are built-in functions that apply operations to sequences in a functional style. They return lazy **iterator** objects (not lists), so they're memory-efficient.

### `map()` — Transform Every Item

`map(function, iterable)` applies a function to every item and returns an iterator of results:

```python
numbers = [1, 2, 3, 4, 5]

# Using a named function:
def square(x):
    return x ** 2

result = map(square, numbers)   # Returns a map object (lazy)
print(list(result))             # [1, 4, 9, 16, 25]

# Using a lambda:
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)   # [2, 4, 6, 8, 10]

# Converting types:
strings = ['1', '2', '3', '4', '5']
ints = list(map(int, strings))   # int is a function!
print(ints)   # [1, 2, 3, 4, 5]

# With multiple iterables:
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)   # [11, 22, 33]
```

### `filter()` — Keep Only Matching Items

`filter(function, iterable)` keeps only items where the function returns `True`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers:
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]

# Keep only positive numbers:
mixed = [-3, 1, -7, 5, 0, 2, -1]
positives = list(filter(lambda x: x > 0, mixed))
print(positives)   # [1, 5, 2]

# Filter strings by length:
words = ['hi', 'hello', 'hey', 'howdy', 'ok']
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)   # ['hello', 'howdy']

# Filter using a named function:
def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primes = list(filter(is_prime, range(2, 50)))
print(primes)   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### Chaining map() and filter()

```python
students = [
    {'name': 'Alice', 'score': 92},
    {'name': 'Bob',   'score': 55},
    {'name': 'Carol', 'score': 78},
    {'name': 'Dave',  'score': 45},
]

# Filter to passing students, then map to get just their names:
passing_names = list(map(
    lambda s: s['name'],
    filter(lambda s: s['score'] >= 70, students)
))
print(passing_names)   # ['Alice', 'Carol']

# The list comprehension equivalent (often more readable):
passing_names = [s['name'] for s in students if s['score'] >= 70]
```

### `map()` vs List Comprehension — Which to Choose?

Both are valid Pythonic styles. Choose based on readability:

```python
data = [1, 2, 3, 4, 5]

# When the transform is a simple, already-named function, map() is clean:
result = list(map(str, data))           # ['1', '2', '3', '4', '5']

# When the transform is more complex, comprehension reads better:
result = [f'Item {x}: {x**2}' for x in data]
```""",

# ════════════════════════════════════════════════
# REGULAR EXPRESSIONS
# ════════════════════════════════════════════════

"The RE Module": """## Pattern Matching with Regular Expressions

A **regular expression** (regex) is a sequence of characters that defines a search pattern. Instead of searching for exact text, you describe a pattern — like "any 10-digit phone number" or "any valid email address". Python's `re` module provides powerful regex tools.

### Basic regex Patterns

| Pattern | Matches |
|---|---|
| `.` | Any character (except newline) |
| `\\d` | Any digit (0-9) |
| `\\D` | Any non-digit |
| `\\w` | Any word character (letter, digit, underscore) |
| `\\W` | Any non-word character |
| `\\s` | Any whitespace (space, tab, newline) |
| `\\S` | Any non-whitespace |
| `^` | Start of string |
| `$` | End of string |

### Quantifiers (How Many)

| Quantifier | Meaning |
|---|---|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` | Exactly n |
| `{n,m}` | Between n and m |

### Key re Functions

```python
import re

text = 'Contact us at support@digitalera.com or sales@example.co.uk'

# re.findall() — returns all matches as a list
emails = re.findall(r'[\\w.-]+@[\\w.-]+\\.\\w+', text)
print(emails)   # ['support@digitalera.com', 'sales@example.co.uk']

# re.search() — finds FIRST match, returns match object (or None)
match = re.search(r'\\d+', 'I am 25 years old and earn 5000 a month')
if match:
    print(match.group())   # '25' — the first number found
    print(match.start())   # 5   — position in string
    print(match.end())     # 7

# re.match() — matches at the START of string only
result = re.match(r'\\d+', '123abc')    # Matches!
result2 = re.match(r'\\d+', 'abc123')   # None — doesn't start with digits

# re.fullmatch() — pattern must match ENTIRE string
is_valid = re.fullmatch(r'\\d{10}', '0801234567')   # Exactly 10 digits
```

### Working with Match Objects

```python
import re

# Groups — parentheses capture portions of the match
pattern = r'(\\w+)@(\\w+)\\.(\\w+)'
match = re.search(pattern, 'user@example.com')

if match:
    print(match.group(0))   # 'user@example.com' — whole match
    print(match.group(1))   # 'user'            — first group
    print(match.group(2))   # 'example'         — second group
    print(match.group(3))   # 'com'             — third group
    print(match.groups())   # ('user', 'example', 'com')

# Named groups:
pattern = r'(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})'
match = re.search(pattern, 'Date: 2024-01-15')
if match:
    print(match.group('year'))    # 2024
    print(match.group('month'))   # 01
    print(match.group('day'))     # 15
```

### Compiling Patterns (for Performance)

If you use the same pattern many times, compile it first:

```python
import re

phone_pattern = re.compile(r'\\d{3}[-.]\\d{3}[-.]\\d{4}')

texts = ['Call 555-123-4567 today', 'Or 555.987.6543', 'No phone here']
for text in texts:
    if phone_pattern.search(text):
        print(f'Found phone in: {text}')
```""",

# ────────────────────────────────────────────────

"Regex Substitution": """## Finding and Replacing with Regex

`re.sub()` is the regex equivalent of `str.replace()`, but with the full power of pattern matching. It finds all occurrences of a pattern and replaces them.

### `re.sub()` Basics

```python
import re

# Format: re.sub(pattern, replacement, string, count=0, flags=0)

text = 'Hello     World!   Multiple   spaces.'

# Replace multiple spaces with a single space:
cleaned = re.sub(r'\\s+', ' ', text)
print(cleaned)   # Hello World! Multiple spaces.

# Remove all digits:
no_digits = re.sub(r'\\d', '', 'abc123def456')
print(no_digits)   # abcdef

# Replace phone numbers:
text2 = 'Call 555-123-4567 or 800-555-0100'
masked = re.sub(r'\\d{3}-\\d{3}-\\d{4}', '[REDACTED]', text2)
print(masked)   # Call [REDACTED] or [REDACTED]
```

### Using Groups in Replacements

In the replacement string, use `\\1`, `\\2` etc. to reference captured groups:

```python
import re

# Reformat dates from MM/DD/YYYY to YYYY-MM-DD:
dates = 'Born: 01/15/1990, Joined: 06/20/2024'
reformatted = re.sub(
    r'(\\d{2})/(\\d{2})/(\\d{4})',    # Match MM/DD/YYYY
    r'\\3-\\1-\\2',                    # Rearrange to YYYY-MM-DD
    dates
)
print(reformatted)   # Born: 1990-01-15, Joined: 2024-06-20

# Add quotes around words:
words = 'apple banana cherry'
quoted = re.sub(r'(\\w+)', r'"\\1"', words)
print(quoted)   # "apple" "banana" "cherry"
```

### Using a Function as the Replacement

Instead of a string, you can pass a function:

```python
import re

# Replacement function receives the match object:
def double_number(match):
    num = int(match.group())
    return str(num * 2)

text = 'I have 5 cats and 3 dogs'
result = re.sub(r'\\d+', double_number, text)
print(result)   # I have 10 cats and 6 dogs

# Censoring profanity (mask middle characters):
def censor(match):
    word = match.group()
    if len(word) <= 2:
        return word
    return word[0] + '*' * (len(word) - 2) + word[-1]

text = 'hello world python'
censored = re.sub(r'\\b\\w{5,}\\b', censor, text)
# Words of 5+ characters get censored
```

### Common Practical Uses

```python
import re

# 1. Slugify a string (for URLs):
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\\w\\s-]', '', text)    # Remove non-word chars
    text = re.sub(r'\\s+', '-', text)           # Spaces to hyphens
    text = re.sub(r'-+', '-', text)             # Multiple hyphens to one
    return text.strip('-')

print(slugify('Hello, World! Python 3.12'))   # hello-world-python-312

# 2. Remove HTML tags:
html = '<p>Hello <b>World</b>!</p>'
plain = re.sub(r'<[^>]+>', '', html)
print(plain)   # Hello World!

# 3. Normalize whitespace in a name:
name = '  Alice   Smith  '
normalized = re.sub(r'\\s+', ' ', name).strip()
print(normalized)   # Alice Smith
```""",

# ════════════════════════════════════════════════
# METACLASSES
# ════════════════════════════════════════════════

"Classes are Objects": """## Everything in Python is an Object — Including Classes

One of Python's most mind-bending features: **classes themselves are objects**. A class is not just a template; it's a living object in memory that belongs to a type. That type is called a **metaclass**.

### Demonstrating That Classes Are Objects

```python
class Dog:
    def bark(self):
        return 'Woof!'

# Dog is an object — you can do object-things with it:
print(type(Dog))           # <class 'type'> — Dog's type is 'type'
print(isinstance(Dog, type))   # True
print(Dog.__name__)         # 'Dog'
print(Dog.__bases__)        # (<class 'object'>,) — its parent classes
print(Dog.__dict__)         # {'bark': <function Dog.bark at ...>, ...}

# Store a class in a variable:
MyDog = Dog               # Now MyDog and Dog are the same class
d = MyDog()               # Create an instance using the stored reference
print(d.bark())           # Woof!

# Pass a class as an argument:
def create_instance(cls, *args):
    return cls(*args)

d = create_instance(Dog)  # Works!
```

### `type()` — The Metaclass of All Classes

You've used `type(x)` to check a variable's type. But `type` can also **create classes dynamically**:

```python
# The three-argument form: type(name, bases, dict)
# creates a new class at runtime!

# This:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point({self.x}, {self.y})'

# Is equivalent to:
def point_init(self, x, y):
    self.x = x
    self.y = y

def point_str(self):
    return f'Point({self.x}, {self.y})'

Point = type('Point', (object,), {
    '__init__': point_init,
    '__str__': point_str,
})

p = Point(3, 4)
print(p)   # Point(3, 4)
```

### The Class Creation Process

When Python sees a `class` statement, it:
1. Executes the class body to collect attributes into a dict
2. Determines the metaclass (usually `type`)
3. Calls `metaclass(name, bases, namespace)` to create the class object

```python
print(type(int))     # <class 'type'>
print(type(str))     # <class 'type'>
print(type(list))    # <class 'type'>
print(type(type))    # <class 'type'>  — type is its own metaclass!

# All built-in and custom classes are instances of 'type'
class MyClass:
    pass

print(isinstance(MyClass, type))   # True
print(isinstance(int, type))       # True
print(isinstance(str, type))       # True
```

### Introspecting Classes

Since classes are objects, you can inspect and modify them dynamically:

```python
class Student:
    school = 'Digital Era'
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def greet(self):
        return f'Hi, I am {self.name}'

# Introspection:
print(dir(Student))              # All attributes and methods
print(Student.__dict__.keys())   # 'school', '__init__', 'greet', ...

# Dynamic attribute access:
s = Student('Alice', 3.8)
attr_name = 'name'
print(getattr(s, attr_name))     # Alice
setattr(s, 'gpa', 4.0)          # Dynamically set an attribute
print(s.gpa)                     # 4.0

# Check if attribute exists:
print(hasattr(s, 'name'))    # True
print(hasattr(s, 'phone'))   # False
```""",

# ────────────────────────────────────────────────

"Custom Metaclasses": """## Writing Your Own Metaclass

A **metaclass** is the class of a class. Just as a class controls how its instances are created, a metaclass controls how *classes* are created. By writing a custom metaclass, you can intercept class creation and modify or validate the resulting class.

### Creating a Custom Metaclass

```python
class SingletonMeta(type):
    \"\"\"A metaclass that makes any class using it a Singleton.\"\"\"
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        # __call__ runs when you do ClassName(...)
        if cls not in cls._instances:
            # First time: create the instance normally
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabasePool(metaclass=SingletonMeta):
    def __init__(self):
        print('Creating pool')
        self.connections = []

p1 = DatabasePool()   # Creating pool
p2 = DatabasePool()   # No output — returns existing instance
print(p1 is p2)       # True — same object!
```

### Metaclass `__new__` — Intercepting Class Creation

```python
class ValidateAttrs(type):
    \"\"\"Metaclass that validates class attributes at definition time.\"\"\"
    
    def __new__(mcs, name, bases, namespace):
        # mcs = the metaclass itself
        # name = name of the class being created
        # bases = tuple of parent classes
        # namespace = dict of class attributes/methods
        
        # Enforce that all methods have docstrings:
        for attr_name, attr_value in namespace.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                if not attr_value.__doc__:
                    raise TypeError(
                        f'Method {attr_name} in {name} must have a docstring!'
                    )
        
        return super().__new__(mcs, name, bases, namespace)

class MyAPI(metaclass=ValidateAttrs):
    def get_users(self):
        \"\"\"Returns all users.\"\"\"    # ✅ Has docstring
        pass
    
    # def delete_all(self):   # ❌ Would raise TypeError at class creation!
    #     pass

print('MyAPI created successfully!')
```

### Metaclass vs Decorator vs `__init_subclass__`

For many common use cases, Python 3.6+ offers `__init_subclass__` as a simpler alternative:

```python
class Base:
    def __init_subclass__(cls, required_attrs=None, **kwargs):
        super().__init_subclass__(**kwargs)
        
        if required_attrs:
            for attr in required_attrs:
                if not hasattr(cls, attr):
                    raise TypeError(f'{cls.__name__} must have {attr!r} attribute')

class Animal(Base, required_attrs=['sound', 'legs']):
    sound = 'generic'
    legs = 4

# class Fish(Base, required_attrs=['sound', 'legs']):   # ❌ TypeError
#     sound = 'blub'
#     # Missing 'legs'!

print('Animal class created successfully!')
```

### When to Use Metaclasses

Metaclasses are an **advanced tool** for library/framework authors. In everyday application code, they're almost never needed. Prefer:
- `@classmethod` for class-level behavior
- `@decorator` for function modification
- `__init_subclass__` for subclass validation
- `__class_getitem__` for generic types

> "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't." — Tim Peters""",

# ════════════════════════════════════════════════
# TYPE HINTING & PYDANTIC
# ════════════════════════════════════════════════

"Static Typing": """## Type Hints — Documenting Your Code's Contracts

Python is dynamically typed (you don't declare types), but since Python 3.5, you can add **type hints** that document what types a function expects and returns. These hints are not enforced at runtime — they're for developers and tools like type checkers (mypy, pyright) and IDEs.

### Basic Type Hints

```python
# Without hints — ambiguous:
def greet(name):
    return f'Hello, {name}!'

# With hints — clear contract:
def greet(name: str) -> str:
    return f'Hello, {name}!'

def add(a: int, b: int) -> int:
    return a + b

def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

def is_adult(age: int) -> bool:
    return age >= 18
```

### Importing Types from `typing`

```python
from typing import List, Dict, Tuple, Optional, Union, Any

# Lists, Dicts, Tuples:
def get_names() -> List[str]:
    return ['Alice', 'Bob', 'Carol']

def get_scores() -> Dict[str, int]:
    return {'Alice': 92, 'Bob': 78}

def get_point() -> Tuple[int, int]:
    return (10, 20)

# Optional — the value can be that type OR None:
def find_user(user_id: int) -> Optional[Dict]:
    # Returns a dict if found, None if not found
    ...

# Union — the value can be one of several types:
def process(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data
```

### Python 3.10+ — Modern Syntax

Python 3.10 simplified type hints:

```python
# Instead of Optional[str], use str | None:
def find_user(user_id: int) -> dict | None:
    ...

# Instead of Union[str, int]:
def process(value: str | int) -> str:
    return str(value)

# Instead of List, Dict (lowercase in 3.9+):
def get_names() -> list[str]:
    return ['Alice', 'Bob']

def get_scores() -> dict[str, int]:
    return {'Alice': 92}
```

### Type Aliases

```python
from typing import TypeAlias

# Create readable names for complex types:
UserId: TypeAlias = int
UserData: TypeAlias = dict[str, str | int | list]
StudentRecord: TypeAlias = tuple[str, float, list[str]]

def get_student(user_id: UserId) -> UserData:
    ...
```

### Running Type Checking with mypy

```bash
pip install mypy
mypy your_script.py
```

```python
def add(a: int, b: int) -> int:
    return a + b

result = add('hello', 'world')   # mypy catches this!
# error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

### Variable Annotations

```python
# You can annotate variables too:
name: str = 'Alice'
age: int = 25
scores: list[int] = [90, 85, 92]
user: dict[str, str | int] = {'name': 'Alice', 'age': 25}

# Annotate without assigning (useful in class bodies):
class Student:
    name: str
    gpa: float
    courses: list[str]
    
    def __init__(self, name: str, gpa: float) -> None:
        self.name = name
        self.gpa = gpa
        self.courses = []
```""",

# ────────────────────────────────────────────────

"Pydantic Models": """## Data Validation with Pydantic

**Pydantic** is Python's most popular data validation library. It uses type hints to automatically validate data, parse it into the correct types, and provide clear error messages when validation fails. It's the backbone of FastAPI.

### Installation

```bash
pip install pydantic
```

### Basic Model

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    gpa: float
    email: str
    is_active: bool = True        # Default value
    courses: list[str] = []       # Default empty list

# Creating an instance — Pydantic validates automatically:
s = Student(
    name='Alice',
    age=25,
    gpa=3.8,
    email='alice@example.com'
)
print(s)
# name='Alice' age=25 gpa=3.8 email='alice@example.com' is_active=True courses=[]

print(s.name)    # Alice
print(s.gpa)     # 3.8

# Pydantic converts types automatically:
s2 = Student(name='Bob', age='22', gpa='3.5', email='bob@x.com')
#                          ^str       ^str   — Pydantic converts these to int/float!
print(type(s2.age))   # <class 'int'>
```

### Validation Errors

```python
from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    age: int
    gpa: float

try:
    bad = Student(name='Alice', age='not_a_number', gpa=3.8)
except ValidationError as e:
    print(e)
    # 1 validation error for Student
    # age
    #   Input should be a valid integer, unable to parse string as an integer [...]
```

### Field — Advanced Validation

```python
from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=0, le=150)              # >= 0 and <= 150
    gpa: float = Field(ge=0.0, le=4.0)
    email: str = Field(pattern=r'^\\S+@\\S+\\.\\S+$')  # Email regex

# Fails validation:
try:
    Student(name='A', age=200, gpa=5.0, email='notanemail')
except Exception as e:
    print('Validation failed!')
```

### Validators — Custom Validation Logic

```python
from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    username: str
    password: str
    confirm_password: str
    
    @field_validator('username')
    @classmethod
    def username_must_be_lowercase(cls, v):
        if not v.islower():
            raise ValueError('Username must be all lowercase')
        return v
    
    @field_validator('confirm_password')
    @classmethod
    def passwords_must_match(cls, v, info):
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v

user = UserCreate(username='alice', password='secret123', confirm_password='secret123')
```

### Converting to/from Dict and JSON

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

p = Product(name='Laptop', price=999.99, in_stock=True)

# To dict:
d = p.model_dump()
print(d)   # {'name': 'Laptop', 'price': 999.99, 'in_stock': True}

# To JSON string:
json_str = p.model_dump_json()
print(json_str)   # {"name":"Laptop","price":999.99,"in_stock":true}

# From dict:
data = {'name': 'Mouse', 'price': 29.99, 'in_stock': False}
p2 = Product.model_validate(data)

# From JSON string:
p3 = Product.model_validate_json('{"name":"Keyboard","price":49.99,"in_stock":true}')
```""",

# ════════════════════════════════════════════════
# ADVANCED OOP & MAGIC METHODS
# ════════════════════════════════════════════════

"Instantiation vs Initialization": """## `__new__` vs `__init__` — Two Stages of Object Creation

Creating an object in Python is actually a two-step process that's hidden from you in everyday code. Understanding both steps unlocks advanced patterns like the Singleton and custom memory allocation.

### The Two Steps

1. **`__new__`** — Allocates memory and creates the raw object. Called first. Returns the new (empty) object.
2. **`__init__`** — Initializes the object. Called second. Receives the object and sets up its attributes.

```python
class MyClass:
    def __new__(cls, value):
        print(f'1. __new__ called with cls={cls.__name__}, value={value}')
        # Must call super().__new__(cls) to actually create the object:
        instance = super().__new__(cls)
        print(f'   Created object: {instance}')
        return instance   # This object is then passed to __init__
    
    def __init__(self, value):
        print(f'2. __init__ called with value={value}')
        self.value = value

obj = MyClass(42)
# 1. __new__ called with cls=MyClass, value=42
#    Created object: <MyClass object at 0x...>
# 2. __init__ called with value=42
```

### When `__new__` is Useful: Singleton Pattern

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance   # Always return the same instance

a = Singleton()
b = Singleton()
print(a is b)   # True — same object!
```

### When `__new__` is Useful: Immutable Subclasses

You can't modify an int's value after creation (it's immutable). `__new__` is called instead of `__init__` for immutable types:

```python
class PositiveInt(int):
    \"\"\"An integer that must always be positive.\"\"\"
    
    def __new__(cls, value):
        if value <= 0:
            raise ValueError(f'PositiveInt must be positive, got {value}')
        # Call int's __new__ to create the immutable int value:
        return super().__new__(cls, value)

n = PositiveInt(5)
print(n)         # 5
print(n + 3)     # 8 — inherits all int behavior
# PositiveInt(-1)  # Raises ValueError!
```

### The Normal Case: Stick with `__init__`

For 99% of use cases, only `__init__` is needed. Use `__new__` only when:
- You need control over the creation of immutable objects
- You're implementing the Singleton pattern
- You're doing metaprogramming

```python
# The everyday pattern — just __init__:
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        self.courses = []
```""",

# ────────────────────────────────────────────────

"Str vs Repr": """## `__str__` vs `__repr__` — Two Kinds of String Representation

Every Python object has two string representations. Understanding when each is used is essential for writing professional classes.

### The Difference

- **`__repr__`** — The **developer** representation. Should be unambiguous and ideally allow recreating the object. Shown in the REPL and in error messages.
- **`__str__`** — The **user-facing** representation. Should be readable and friendly. Used by `print()` and `str()`.

```python
import datetime

d = datetime.date(2024, 1, 15)

print(repr(d))   # datetime.date(2024, 1, 15)  — could recreate the object!
print(str(d))    # 2024-01-15                  — human-friendly
```

### Implementing Both

```python
class Money:
    def __init__(self, amount, currency='NGN'):
        self.amount = amount
        self.currency = currency
    
    def __repr__(self):
        # Developer representation — precise, recreatable
        return f'Money({self.amount!r}, {self.currency!r})'
    
    def __str__(self):
        # User-friendly representation
        return f'{self.currency} {self.amount:,.2f}'

m = Money(5000, 'NGN')

print(repr(m))   # Money(5000, 'NGN')   — useful in debugging
print(str(m))    # NGN 5,000.00         — shown to users
print(m)         # NGN 5,000.00         — print() uses __str__

# In lists, repr() is used:
wallet = [Money(5000, 'NGN'), Money(20, 'USD')]
print(wallet)   # [Money(5000, 'NGN'), Money(20, 'USD')]
```

### Rules of Thumb

1. **Always implement `__repr__`** — it's the most important one
2. Implement `__str__` only if you want a different user-facing format
3. `__repr__` should ideally look like `ClassName(arg1, arg2, ...)` so you could paste it into Python to recreate the object
4. If only `__repr__` is defined, Python uses it for `str()` too

```python
class Vector:
    def __init__(self, x, y, z=0):
        self.x, self.y, self.z = x, y, z
    
    def __repr__(self):
        if self.z == 0:
            return f'Vector({self.x}, {self.y})'
        return f'Vector({self.x}, {self.y}, {self.z})'
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

v = Vector(3, 4)
print(repr(v))   # Vector(3, 4)     — developer can eval() this to get it back
print(str(v))    # (3, 4, 0)        — user-friendly
```

### The `!r` Format Spec

In f-strings, `!r` calls `repr()` on the value:

```python
name = 'Alice'
print(f'User: {name}')     # User: Alice    — calls str()
print(f'User: {name!r}')   # User: 'Alice'  — calls repr() (shows quotes)
```""",

# ────────────────────────────────────────────────

"Equality and Hashing": """## Customizing == and Dictionaries

Python's `==` operator calls `__eq__`. By default, it checks **identity** (same object in memory), not value equality. For your custom classes, you usually want `==` to compare values.

### The Default Problem

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(3, 4)
p2 = Point(3, 4)    # Same values, different objects

print(p1 == p2)    # False — they're different objects! (checks identity)
print(p1 is p2)    # False — definitely different objects
```

### Implementing `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented   # Can't compare with non-Points
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(p1 == p2)    # True  — same values!
print(p1 == p3)    # False
print(p1 != p2)    # False — __ne__ is automatically the opposite of __eq__
```

### The Hash Problem

If you define `__eq__`, Python **automatically makes your class unhashable** (removes `__hash__`). This means you can't use your objects as dict keys or in sets:

```python
p = Point(3, 4)
# {p: 'value'}    # ❌ TypeError: unhashable type: 'Point'
# {p, Point(1,2)} # ❌ TypeError: unhashable type: 'Point'
```

### Implementing `__hash__`

If your objects are meant to be **immutable** (values never change), implement `__hash__` consistently with `__eq__`:

**Rule:** Objects that compare equal (`a == b`) MUST have the same hash (`hash(a) == hash(b)`).

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        # hash() of a tuple is consistent and well-distributed:
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p1 = Point(3, 4)
p2 = Point(3, 4)

# Now usable in sets and dicts:
point_set = {p1, p2}
print(len(point_set))   # 1 — they're equal, so only one!

point_data = {p1: 'origin point'}
print(point_data[p2])   # 'origin point' — p2 == p1, same hash!
```

### Using `@dataclass` (eq and hash auto-generated)

```python
from dataclasses import dataclass

@dataclass(frozen=True)   # frozen=True makes it immutable AND hashable
class Point:
    x: int
    y: int
    # __eq__ and __hash__ are automatically generated!

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)          # True
print({p1, p2})          # {Point(x=3, y=4)} — deduplicated!
print(hash(p1) == hash(p2))   # True
```""",

# ────────────────────────────────────────────────

"Property Decorators": """## Computed Attributes and Validation

The `@property` decorator turns a method into an attribute-style property. This lets you add **validation, computation, and access control** without changing how the attribute is accessed externally.

### Basic Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius   # Store as private (by convention)
    
    @property
    def radius(self):
        \"\"\"Read-only access to radius.\"\"\"
        return self._radius
    
    @property
    def area(self):
        \"\"\"Computed property — calculated from radius.\"\"\"
        import math
        return math.pi * self._radius ** 2
    
    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)
print(c.radius)     # 5     — looks like attribute access, calls the method
print(c.area)       # 78.54 — computed each time it's accessed
print(c.diameter)   # 10

# c.radius = 10     # ❌ AttributeError — no setter defined!
```

### Adding a Setter with Validation

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius   # Uses the setter for validation!
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Radius must be a number')
        if value < 0:
            raise ValueError(f'Radius cannot be negative, got {value}')
        self._radius = value

c = Circle(5)
print(c.radius)   # 5

c.radius = 10     # Calls the setter — validates first
print(c.radius)   # 10

# c.radius = -1   # ❌ ValueError: Radius cannot be negative
```

### Adding a Deleter

```python
class CachedProperty:
    def __init__(self, value):
        self._value = value
        self._cache = {}
    
    @property
    def result(self):
        if 'result' not in self._cache:
            self._cache['result'] = expensive_computation(self._value)
        return self._cache['result']
    
    @result.deleter
    def result(self):
        \"\"\"Clear the cache.\"\"\"
        self._cache.pop('result', None)
        print('Cache cleared!')

obj = CachedProperty(42)
del obj.result   # Clears the cache — calls the deleter
```

### `functools.cached_property` — Compute Once and Cache

For expensive properties that shouldn't recompute every access:

```python
from functools import cached_property
import statistics

class Dataset:
    def __init__(self, values):
        self.values = values
    
    @cached_property
    def mean(self):
        \"\"\"Computed once, then cached.\"\"\"
        print('Computing mean...')
        return statistics.mean(self.values)
    
    @cached_property
    def stdev(self):
        return statistics.stdev(self.values)

data = Dataset([2, 4, 6, 8, 10, 12])
print(data.mean)   # Computing mean... → 7
print(data.mean)   # 7 (no recomputation — cached!)
print(data.stdev)  # 3.74...
```""",

# ────────────────────────────────────────────────

"Classmethods vs Staticmethods": """## Three Ways to Define Class Methods

You've met `@classmethod` and `@staticmethod` before. Here's a deep-dive into when to use each, with practical examples.

### Summary Table

| | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | (none) | `@classmethod` | `@staticmethod` |
| First arg | `self` (instance) | `cls` (class) | (nothing) |
| Accesses instance | ✅ Yes | ❌ No | ❌ No |
| Accesses class vars | ✅ Via self.__class__ | ✅ Via cls | ❌ No |
| Can be overridden by subclasses | ✅ Yes | ✅ Yes (cls changes) | ❌ No (no cls) |

### Instance Methods — The Default

```python
class BankAccount:
    interest_rate = 0.05   # Class variable
    
    def __init__(self, owner, balance=0):
        self.owner = owner     # Instance variable
        self.balance = balance
    
    def deposit(self, amount):   # Instance method — uses self
        self.balance += amount
        return self.balance
    
    def get_summary(self):
        return f'{self.owner}: ${self.balance:.2f}'
```

### Class Methods — Factory Pattern and Tracking

```python
class BankAccount:
    interest_rate = 0.05
    _total_accounts = 0     # Tracks how many accounts exist
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount._total_accounts += 1
    
    # Factory method — alternative constructor
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['owner'], data.get('balance', 0))
    
    # Works with subclasses correctly — cls refers to the actual class
    @classmethod
    def create_savings(cls, owner):
        return cls(owner, balance=100)   # $100 bonus for savings accounts
    
    @classmethod
    def get_total_accounts(cls):
        return cls._total_accounts
    
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate         # Changes it for ALL accounts

# Creating from a dict:
data = {'owner': 'Alice', 'balance': 5000}
account = BankAccount.from_dict(data)

# Class-level info:
print(BankAccount.get_total_accounts())   # 1
BankAccount.set_interest_rate(0.06)       # Changes for all
```

### Static Methods — Pure Utility Functions

```python
class DateUtils:
    \"\"\"Utility class — no instances needed, just helper functions.\"\"\"
    
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and DateUtils.is_leap_year(year):
            return 29
        return days[month - 1]

print(DateUtils.is_leap_year(2024))     # True
print(DateUtils.days_in_month(2024, 2)) # 29
```""",

# ────────────────────────────────────────────────

"Multiple Inheritance & MRO": """## Inheriting from Multiple Classes

Python supports **multiple inheritance** — a class can have more than one parent class. This is powerful but requires understanding the **Method Resolution Order (MRO)** to avoid confusion about which method gets called.

### Basic Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return f'{self.__class__.__name__} is flying!'
    
    def move(self):
        return 'Moving by flying'

class Swimmable:
    def swim(self):
        return f'{self.__class__.__name__} is swimming!'
    
    def move(self):
        return 'Moving by swimming'

class Duck(Flyable, Swimmable):   # Inherits from both!
    def quack(self):
        return 'Quack!'

d = Duck()
print(d.fly())    # Duck is flying!    — from Flyable
print(d.swim())   # Duck is swimming!  — from Swimmable
print(d.quack())  # Quack!             — from Duck itself

# Which move() is called?
print(d.move())   # Moving by flying   — Flyable comes first in MRO!
```

### The MRO — Method Resolution Order

Python uses the **C3 linearization algorithm** to determine the order in which classes are checked for methods. Use `ClassName.__mro__` to see it:

```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```

Python checks in this order:
1. `Duck` itself
2. `Flyable` (listed first in `Duck(Flyable, Swimmable)`)
3. `Swimmable`
4. `object` (base of all classes)

### Cooperative Multiple Inheritance with `super()`

The power of multiple inheritance comes from `super()` working cooperatively through the MRO chain:

```python
class LogMixin:
    def save(self):
        print(f'[LOG] Saving {self.__class__.__name__}')
        super().save()   # Calls the next in MRO!

class ValidationMixin:
    def save(self):
        print('[VALIDATE] Validation passed')
        super().save()   # Calls the next in MRO!

class Model:
    def save(self):
        print('[DB] Saved to database')

# Composing behavior with mixins:
class UserModel(LogMixin, ValidationMixin, Model):
    pass

user = UserModel()
user.save()
# [LOG] Saving UserModel
# [VALIDATE] Validation passed
# [DB] Saved to database
```

The MRO ensures each method in the chain is called exactly once, in the right order.

### The Diamond Problem — MRO Solves It

```python
class A:
    def method(self): return 'A'

class B(A):
    def method(self): return f'B -> {super().method()}'

class C(A):
    def method(self): return f'C -> {super().method()}'

class D(B, C):  # Both B and C inherit from A — diamond!
    pass

d = D()
print(d.method())   # B -> C -> A
print(D.__mro__)    # D -> B -> C -> A -> object
# A's method is called only ONCE — the MRO prevents double execution!
```""",

# ────────────────────────────────────────────────

"Callable Instances": """## Objects That Behave Like Functions

By implementing `__call__`, you can make an instance of your class callable — you can call it just like a function with `()`. This is useful for objects that maintain state between calls.

### Why Make an Object Callable?

Sometimes you want a function that:
- Maintains state between calls (without using global variables)
- Can be configured at creation time
- Needs to be stored and passed around like a function

### Basic Example

```python
class Multiplier:
    \"\"\"A callable that multiplies by a fixed factor.\"\"\"
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(7))    # 14
print(triple(7))    # 21
print(double(100))  # 200

# It IS callable:
print(callable(double))   # True
```

### Stateful Function — Counting Calls

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'Called {self.count} time(s)')

counter = Counter()
counter()   # Called 1 time(s)
counter()   # Called 2 time(s)
counter()   # Called 3 time(s)
print(f'Total calls: {counter.count}')   # 3
```

### Memoization Using `__call__`

```python
class Memoize:
    \"\"\"Caches the results of function calls.\"\"\"
    
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))   # Fast! Results are cached
print(fibonacci.cache)  # Shows all cached values
```

### Callable Check

```python
def regular_function(): pass

class WithCall:
    def __call__(self): pass

class WithoutCall:
    pass

print(callable(regular_function))  # True
print(callable(WithCall()))        # True — has __call__
print(callable(WithoutCall()))     # False — no __call__
print(callable(42))                # False — integers aren't callable
```""",

# ────────────────────────────────────────────────

"Indexing and Slicing": """## Making Your Objects Support [] Notation

Implement `__getitem__`, `__setitem__`, and `__delitem__` to make your objects support indexing (`obj[key]`) and slicing (`obj[start:stop]`).

### `__getitem__` — Reading with []

```python
class NumberList:
    def __init__(self, numbers):
        self._data = list(numbers)
    
    def __getitem__(self, index):
        # index can be an int or a slice object
        if isinstance(index, slice):
            return NumberList(self._data[index])
        return self._data[index]
    
    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f'NumberList({self._data})'

nl = NumberList([10, 20, 30, 40, 50])
print(nl[0])       # 10
print(nl[-1])      # 50
print(nl[1:4])     # NumberList([20, 30, 40])
print(nl[::2])     # NumberList([10, 30, 50])
```

### `__setitem__` and `__delitem__`

```python
class Matrix:
    def __init__(self, rows, cols, default=0):
        self._data = [[default] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols
    
    def __getitem__(self, key):
        row, col = key   # Expect a tuple: matrix[row, col]
        return self._data[row][col]
    
    def __setitem__(self, key, value):
        row, col = key
        self._data[row][col] = value
    
    def __repr__(self):
        return '\n'.join(str(row) for row in self._data)

m = Matrix(3, 3)
m[0, 0] = 1
m[1, 1] = 5
m[2, 2] = 9
print(m)
# [1, 0, 0]
# [0, 5, 0]
# [0, 0, 9]
print(m[1, 1])   # 5
```

### Implementing Slicing for Custom Sequences

```python
import math

class InfiniteRange:
    \"\"\"An infinite sequence of integers starting from 'start'.\"\"\"
    
    def __init__(self, start=0):
        self.start = start
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(10_000_000)   # Bound the slice
            return [self.start + i for i in range(start, stop, step or 1)]
        if index < 0:
            raise IndexError('Infinite sequence does not support negative indexing')
        return self.start + index

inf = InfiniteRange(10)
print(inf[0])         # 10
print(inf[5])         # 15
print(inf[100])       # 110
print(inf[0:10])      # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(inf[0:20:3])    # [10, 13, 16, 19, 22, 25, 28]
```""",

# ════════════════════════════════════════════════
# DATA CLASSES & MODERN PYTHON MASTERCLASS
# ════════════════════════════════════════════════

"Introduction to Data Classes": """## `@dataclass` — Eliminating Boilerplate

A **dataclass** automatically generates `__init__`, `__repr__`, and `__eq__` methods based on class variable annotations. It's perfect for classes that mainly hold data.

### The Boilerplate Problem

```python
# Without dataclass — lots of repetitive code:
class Point:
    def __init__(self, x: float, y: float, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z
```

### With `@dataclass`

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0   # Default value

# __init__, __repr__, and __eq__ are automatically generated!

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0, 3.0)
p3 = Point(1.0, 2.0)

print(p1)            # Point(x=1.0, y=2.0, z=0.0)
print(p1 == p3)      # True — auto-generated __eq__!
print(p1 == p2)      # False
```

### Options

```python
@dataclass(
    order=True,     # Generate __lt__, __le__, __gt__, __ge__ for sorting
    frozen=True,    # Make immutable (like a named tuple) — also adds __hash__
    slots=True,     # Use __slots__ for memory efficiency (Python 3.10+)
)
class ImmutablePoint:
    x: float
    y: float

p = ImmutablePoint(3.0, 4.0)
# p.x = 10   # ❌ FrozenInstanceError — can't modify frozen dataclass

points = [ImmutablePoint(3, 1), ImmutablePoint(1, 5), ImmutablePoint(2, 3)]
sorted_points = sorted(points)   # Works because order=True
print(sorted_points)
```

### Practical Dataclass Example

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Student:
    name: str
    email: str
    gpa: float = 0.0
    courses: list[str] = field(default_factory=list)   # Mutable default!
    enrolled_at: datetime = field(default_factory=datetime.now)
    
    def add_course(self, course: str):
        self.courses.append(course)
    
    @property
    def grade_letter(self) -> str:
        if self.gpa >= 3.7: return 'A'
        if self.gpa >= 3.0: return 'B'
        return 'C'

alice = Student(name='Alice', email='alice@example.com', gpa=3.8)
alice.add_course('Python')
alice.add_course('ML')
print(alice)   # Student(name='Alice', email='alice@example.com', gpa=3.8, ...)
print(alice.grade_letter)   # A
```""",

# ────────────────────────────────────────────────

"Default Factories": """## Mutable Defaults in Dataclasses

Mutable default values (lists, dicts, sets) in dataclasses require special handling. Using a bare mutable default would share the same object across all instances — a classic Python gotcha.

### The Problem (Without dataclass)

```python
class Student:
    # ❌ WRONG — ALL instances share the SAME list!
    def __init__(self, name, courses=[]):
        self.name = name
        self.courses = courses   # This is the SAME list for all students!

alice = Student('Alice')
bob   = Student('Bob')

alice.courses.append('Python')
print(bob.courses)    # ['Python'] — Bob's courses changed too!?
```

### The Solution in Dataclasses: `field(default_factory=...)`

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Student:
    name: str
    
    # ✅ CORRECT — each instance gets its OWN fresh list:
    courses: list[str] = field(default_factory=list)
    
    # ✅ CORRECT — each instance gets its OWN fresh dict:
    grades: dict[str, float] = field(default_factory=dict)
    
    # ✅ CORRECT — a factory function that creates the default:
    tags: set[str] = field(default_factory=set)
    
    # Lambda as a factory:
    metadata: dict = field(default_factory=lambda: {'active': True, 'score': 0})

alice = Student('Alice')
bob   = Student('Bob')

alice.courses.append('Python')
print(alice.courses)   # ['Python']
print(bob.courses)     # []  — completely separate list!
```

### Advanced `field()` Options

```python
from dataclasses import dataclass, field

@dataclass
class Config:
    # repr=False — exclude from __repr__:
    api_key: str = field(default='', repr=False)
    
    # compare=False — exclude from __eq__:
    timestamp: float = field(default=0.0, compare=False)
    
    # init=False — not a parameter in __init__:
    cache: dict = field(default_factory=dict, init=False)
    
    # hash=False — exclude from __hash__:
    description: str = field(default='', hash=False)

c = Config(api_key='abc123', timestamp=1234567890.0)
print(c)   # Config(timestamp=1234567890.0, description='') — api_key not shown!
```

### Using Custom Factory Functions

```python
from dataclasses import dataclass, field
import uuid

@dataclass
class Task:
    title: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    subtasks: list['Task'] = field(default_factory=list)
    tags: set[str] = field(default_factory=set)

t1 = Task('Build API')
t2 = Task('Write tests')

print(t1.id)   # Something like: a1b2c3d4-...
print(t2.id)   # Different UUID each time!

t1.tags.add('backend')
t2.tags.add('testing')
print(t1.tags)   # {'backend'} — not shared with t2
```""",

# ────────────────────────────────────────────────

"Post-Init Processing": """## `__post_init__` — Running Code After Auto-Init

In a dataclass, `__init__` is automatically generated. But sometimes you need to run additional code after the initial values are set — validation, derived values, or side effects. That's what `__post_init__` is for.

### Basic Usage

```python
from dataclasses import dataclass, field

@dataclass
class Temperature:
    celsius: float
    fahrenheit: float = field(init=False)   # Not in __init__, computed in __post_init__
    
    def __post_init__(self):
        # Runs automatically after __init__
        self.fahrenheit = self.celsius * 9/5 + 32

t = Temperature(100)
print(t.celsius)     # 100
print(t.fahrenheit)  # 212.0
print(t)             # Temperature(celsius=100, fahrenheit=212.0)
```

### Validation in `__post_init__`

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    gpa: float
    
    def __post_init__(self):
        # Validate name
        if not self.name.strip():
            raise ValueError('Name cannot be empty')
        self.name = self.name.strip().title()   # Normalize name
        
        # Validate age
        if not 0 <= self.age <= 150:
            raise ValueError(f'Age {self.age} is out of valid range')
        
        # Validate GPA
        if not 0.0 <= self.gpa <= 4.0:
            raise ValueError(f'GPA {self.gpa} must be between 0.0 and 4.0')

s = Student('  alice  ', 25, 3.8)
print(s.name)   # Alice — normalized!

try:
    bad = Student('', 200, 5.0)
except ValueError as e:
    print(f'Validation failed: {e}')
```

### `InitVar` — Parameters Only for `__post_init__`

```python
from dataclasses import dataclass, field, InitVar

@dataclass
class HashedPassword:
    username: str
    password_hash: str = field(init=False)
    
    # InitVar — passed to __post_init__ but NOT stored as an attribute
    raw_password: InitVar[str] = None
    
    def __post_init__(self, raw_password: str):
        import hashlib
        self.password_hash = hashlib.sha256(
            raw_password.encode()
        ).hexdigest()

user = HashedPassword('alice', raw_password='secret123')
print(user.username)       # alice
print(user.password_hash)  # sha256 hash
# print(user.raw_password) # AttributeError — it's not stored!
```""",

# ────────────────────────────────────────────────

"The Walrus Operator": """## `:=` — Assign and Use in One Expression

The **walrus operator** (`:=`), introduced in Python 3.8, allows you to assign a value to a variable as part of an expression. It's called the walrus operator because `:=` looks like a walrus's eyes and tusks.

### The Problem It Solves

Sometimes you need to compute a value and immediately use it in a condition — without computing it twice or creating an extra variable before the loop:

```python
# Old way — compute and store, then check:
data = get_data()   # Compute once
if data:            # Check result
    process(data)   # Use it

# Or awkwardly in loops:
while True:
    line = file.readline()
    if not line:
        break
    process(line)
```

### Basic Walrus Operator

```python
# Assign and check in one step:
if data := get_data():      # Assign to 'data' AND check if truthy
    process(data)

# Equivalent to:
data = get_data()
if data:
    process(data)
```

### In While Loops — The Most Common Use

```python
import re

text = 'Error: line 42, column 5: unexpected token'

# Cleaner than: match = re.search(...); while match:
while match := re.search(r'\\d+', text):
    print(f'Found number: {match.group()}')
    text = text[match.end():]   # Move past the match

# Reading from a file efficiently:
with open('data.txt') as f:
    while chunk := f.read(1024):   # Read 1024 bytes at a time
        process(chunk)

# Without walrus (more verbose):
with open('data.txt') as f:
    chunk = f.read(1024)
    while chunk:
        process(chunk)
        chunk = f.read(1024)   # Repeated code!
```

### In Comprehensions — Avoiding Repeated Computation

```python
# Without walrus — compute len() twice:
words = ['hi', 'hello', 'hey', 'howdy', 'python']
long_lengths = [len(w) for w in words if len(w) > 4]   # len(w) called twice!

# With walrus — compute once, use in both test and expression:
long_lengths = [n for w in words if (n := len(w)) > 4]
print(long_lengths)   # [5, 5, 6]  (lengths of 'hello', 'howdy', 'python')
```

### Avoiding Walrus Overuse

The walrus operator is a tool, not a mandate. Use it when it genuinely improves readability:

```python
# ✅ Good use — avoids repetition:
if (avg := sum(values) / len(values)) > 90:
    print(f'Excellent! Average is {avg:.1f}')

# ❌ Bad use — harder to read, no benefit:
if (x := 5) > 3:
    print(x)   # Just use: x = 5; if x > 3:
```""",

# ────────────────────────────────────────────────

"Structural Pattern Matching": """## `match/case` — Python's Switch Statement (But Smarter)

Python 3.10 introduced `match/case` (also called **structural pattern matching**). It goes far beyond a simple switch statement — it can match against data structures, extract values, and check types in one clean operation.

### Basic Syntax

```python
command = 'quit'

match command:
    case 'quit':
        print('Goodbye!')
    case 'hello':
        print('Hello!')
    case _:              # Default case — the wildcard
        print(f'Unknown command: {command}')
```

### Matching Types

```python
def describe(value):
    match value:
        case int():
            return f'An integer: {value}'
        case str():
            return f'A string: {value!r}'
        case list():
            return f'A list with {len(value)} items'
        case dict():
            return f'A dict with {len(value)} keys'
        case None:
            return 'Nothing'
        case _:
            return f'Something else: {type(value).__name__}'

print(describe(42))          # An integer: 42
print(describe('hello'))     # A string: 'hello'
print(describe([1, 2, 3]))   # A list with 3 items
```

### Matching Structures (Destructuring)

This is where pattern matching really shines:

```python
point = (3, 4)

match point:
    case (0, 0):
        print('Origin')
    case (x, 0):           # Matches any point on x-axis; x is captured
        print(f'On x-axis at x={x}')
    case (0, y):
        print(f'On y-axis at y={y}')
    case (x, y):           # Matches any 2-tuple; x and y are captured
        print(f'Point at ({x}, {y})')
```

### Matching Dictionaries

```python
command = {'action': 'buy', 'item': 'laptop', 'quantity': 2}

match command:
    case {'action': 'quit'}:
        print('Quitting...')
    case {'action': 'buy', 'item': item, 'quantity': qty}:
        print(f'Buying {qty}x {item}')
    case {'action': action}:
        print(f'Unknown action: {action}')
```

### Guards — Adding Conditions to Cases

```python
number = 42

match number:
    case n if n < 0:
        print(f'{n} is negative')
    case n if n == 0:
        print('Zero')
    case n if n % 2 == 0:
        print(f'{n} is positive and even')
    case n:
        print(f'{n} is positive and odd')
```

### Real Use Case: Command Parsing

```python
def process_command(cmd: dict):
    match cmd:
        case {'type': 'create_user', 'name': name, 'email': email}:
            return f'Creating user {name} ({email})'
        case {'type': 'delete_user', 'id': int(user_id)} if user_id > 0:
            return f'Deleting user {user_id}'
        case {'type': 'list_users', 'page': int(page)}:
            return f'Listing users, page {page}'
        case {'type': unknown}:
            return f'Unknown command type: {unknown}'
        case _:
            return 'Invalid command format'

print(process_command({'type': 'create_user', 'name': 'Alice', 'email': 'a@b.com'}))
```""",

# ────────────────────────────────────────────────

"F-String Debugging": """## f-String = for Instant Debugging

Python 3.8 introduced the `=` specifier inside f-strings that automatically prints both the variable name and its value. It's one of the most underrated debugging tools in Python.

### The Problem with Normal Debugging

```python
x = 42
items = [1, 2, 3, 4, 5]
name = 'Alice'

# Old way — lots of typing:
print('x =', x)
print('items =', items)
print('name =', name)
print('len(items) =', len(items))
print('x + 100 =', x + 100)
```

### The `=` Specifier

```python
x = 42
items = [1, 2, 3, 4, 5]
name = 'Alice'

# New way — f-string with = automatically prints name AND value:
print(f'{x=}')              # x=42
print(f'{items=}')          # items=[1, 2, 3, 4, 5]
print(f'{name=}')           # name='Alice'
print(f'{len(items)=}')     # len(items)=5
print(f'{x + 100=}')        # x + 100=142
```

### Combining `=` with Format Specifiers

```python
pi = 3.14159265358979
score = 87.5678

print(f'{pi=}')          # pi=3.14159265358979
print(f'{pi=:.2f}')      # pi=3.14   — 2 decimal places, showing the name
print(f'{score=:.1f}')   # score=87.6
```

### Multiple Variables at Once

```python
def calculate_stats(data):
    n = len(data)
    mean = sum(data) / n
    minimum = min(data)
    maximum = max(data)
    
    # Compact debugging output:
    print(f'{n=}, {mean=:.2f}, {minimum=}, {maximum=}')
    # n=5, mean=30.00, minimum=10, maximum=50

calculate_stats([10, 20, 30, 40, 50])
```

### In Practice: Debugging Functions

```python
def process_order(user_id, items, discount=0):
    subtotal = sum(item['price'] for item in items)
    discount_amount = subtotal * discount
    total = subtotal - discount_amount
    
    # Quick debug dump:
    print(f'{user_id=}, {subtotal=:.2f}, {discount=}, {discount_amount=:.2f}, {total=:.2f}')
    
    return total

order = process_order(
    user_id=42,
    items=[{'price': 50.0}, {'price': 30.0}],
    discount=0.1
)
# user_id=42, subtotal=80.00, discount=0.1, discount_amount=8.00, total=72.00
```""",

# ────────────────────────────────────────────────

"Dictionary Union Operators": """## Merging Dictionaries with `|` and `|=`

Python 3.9 introduced the `|` (union) and `|=` (update) operators for dictionaries, making it much cleaner to merge dictionaries.

### Before Python 3.9 (Old Ways)

```python
defaults = {'theme': 'dark', 'lang': 'en', 'debug': False}
overrides = {'debug': True, 'lang': 'fr'}

# Method 1: {**dict1, **dict2} — unpacking (works in 3.5+):
merged = {**defaults, **overrides}
# {'theme': 'dark', 'lang': 'fr', 'debug': True}

# Method 2: dict.update() — modifies in place:
config = defaults.copy()
config.update(overrides)
```

### Python 3.9+: The `|` Operator

```python
defaults = {'theme': 'dark', 'lang': 'en', 'debug': False}
overrides = {'debug': True, 'lang': 'fr'}

# New way — clean and readable:
merged = defaults | overrides
# {'theme': 'dark', 'lang': 'fr', 'debug': True}

# Right-hand side values win on conflicts — just like update()
print(merged['lang'])    # 'fr' — overrides wins
print(merged['theme'])   # 'dark' — only in defaults
```

### The `|=` Operator — In-Place Merge

```python
config = {'theme': 'dark', 'lang': 'en'}
user_prefs = {'lang': 'fr', 'font_size': 16}

config |= user_prefs    # Merges user_prefs INTO config (modifies config)
print(config)
# {'theme': 'dark', 'lang': 'fr', 'font_size': 16}
```

### Chaining Multiple Merges

```python
base = {'a': 1, 'b': 2}
layer1 = {'b': 10, 'c': 3}
layer2 = {'c': 30, 'd': 4}

# Chaining — later dicts override earlier ones:
result = base | layer1 | layer2
# {'a': 1, 'b': 10, 'c': 30, 'd': 4}
```

### Practical Use Case: Config Management

```python
# Building a layered configuration:
DEFAULT_CONFIG = {
    'debug': False,
    'db_url': 'sqlite:///app.db',
    'max_connections': 10,
    'log_level': 'INFO',
}

PRODUCTION_CONFIG = {
    'debug': False,
    'db_url': 'postgresql://...',
    'max_connections': 100,
}

DEV_CONFIG = {
    'debug': True,
    'log_level': 'DEBUG',
}

def get_config(environment='production'):
    if environment == 'production':
        return DEFAULT_CONFIG | PRODUCTION_CONFIG
    elif environment == 'development':
        return DEFAULT_CONFIG | DEV_CONFIG
    return DEFAULT_CONFIG

config = get_config('production')
print(config['db_url'])       # postgresql://...
print(config['max_connections'])  # 100
```""",

# ────────────────────────────────────────────────

"Positional-Only Parameters": """## `/` and `*` — Controlling How Arguments Are Passed

Python 3.8 introduced the `/` parameter separator, completing the set of markers that control whether arguments must be passed positionally or as keywords.

### The Three Zones

```python
def func(pos_only, /, normal, *, kw_only):
    #        ^^^       ^^^^^      ^^^^^^^
    #  positional    can be    keyword
    #    only        either     only
    pass
```

- Before `/`: **Positional-only** — must be passed by position, not by name
- Between `/` and `*`: **Regular** — can be passed either way
- After `*`: **Keyword-only** — must be passed by name

### Positional-Only (Before `/`)

```python
def power(base, exponent, /):
    return base ** exponent

# ✅ These work:
power(2, 8)        # 256 — positional
power(2, 10)       # 1024

# ❌ These fail — can't use keywords for positional-only params:
# power(base=2, exponent=8)   # TypeError!
```

### Keyword-Only (After `*`)

```python
def send_email(to, subject, *, cc=None, bcc=None, priority='normal'):
    #                        ^
    #                  bare * means no *args, just marks keyword-only
    pass

# ✅ These work:
send_email('alice@x.com', 'Hello', cc='bob@x.com')
send_email('alice@x.com', 'Hello', priority='high')

# ❌ These fail:
# send_email('alice@x.com', 'Hello', 'bob@x.com')   # TypeError — cc must be keyword!
```

### Combining All Three

```python
def database_query(host, port, /, query, *, timeout=30, retries=3):
    # host, port: positional-only (internal details, shouldn't be named)
    # query: can be either positional or keyword
    # timeout, retries: keyword-only (for clarity)
    pass

# All valid:
database_query('localhost', 5432, 'SELECT * FROM users', timeout=10)
database_query('localhost', 5432, query='SELECT * FROM users')
database_query('localhost', 5432, 'SELECT * FROM users', retries=5, timeout=15)

# Invalid:
# database_query(host='localhost', port=5432, ...)  # host/port are positional-only!
```

### Why Use Positional-Only?

1. **API stability** — If you rename the parameter, existing callers (who use positional args) aren't broken
2. **Performance** — Slightly faster than keyword arguments
3. **Clarity** — Some parameters are clearly positional by nature (like `x, y` in `distance(x, y)`)

```python
# Good candidates for /:
def len(obj, /): ...      # len(items) — no one writes len(obj=items)
def abs(x, /): ...        # abs(-5) — no one writes abs(x=-5)

# Good candidates for *:
def create_user(name, *, role='user', active=True): ...
# Forces: create_user('Alice', role='admin') — role must be explicit
```""",

}  # End of RICH_THEORY


def patch_theory():
    print(f"Loading {TRACK_FILE}...")
    with open(TRACK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    patched = 0
    skipped = 0

    for topic, topic_data in data.items():
        for lesson in topic_data.get("lessons", []):
            title = lesson.get("title", "")
            if title in RICH_THEORY:
                old_len = len(lesson.get("theory", ""))
                lesson["theory"] = RICH_THEORY[title]
                new_len = len(lesson["theory"])
                print(f"  [OK] Patched: {title!r} ({old_len} -> {new_len} chars)")
                patched += 1
            elif lesson.get("type") != "quiz" and len(lesson.get("theory", "")) <= 800:
                skipped += 1
                print(f"  [??] Still short: {title!r} (topic: {topic})")

    print(f"\n{'='*60}")
    print(f"Patched: {patched} lessons")
    print(f"Still needs work: {skipped} lessons")

    with open(TRACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {TRACK_FILE}")

if __name__ == "__main__":
    patch_theory()
