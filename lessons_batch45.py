"""
Batch 45: Expanding Python Core Curriculum (Strings, Error Handling, Comprehensions, Context Managers, Asyncio)
"""
import json, os

NEW_COURSES_BATCH45 = {
    "String Manipulation": {
        "tier": "Beginner",
        "aiRubric": "Assess basic Python string methods",
        "lessons": [
            {"title": "F-Strings", "theory": "## String Formatting\\nIntroduced in Python 3.6, f-strings offer a concise and readable way to embed expressions inside string literals.", "instructions": "## Task: Use an F-String\\nFormat the string to say 'My name is Alice and I am 30 years old.' using the variables.", "starterCode": "name = 'Alice'\\nage = 30\\ngreeting = ___'My name is {___} and I am {___} years old.'", "solution": "name = 'Alice'\\nage = 30\\ngreeting = f'My name is {name} and I am {age} years old.'", "hint": "Use the f prefix and the variable names", "rubric": "Correctly uses f-strings with {name} and {age}."},
            {"title": "Splitting and Joining", "theory": "## String to List and Back\\nThe `.split()` method breaks a string into a list based on a delimiter, and `.join()` merges a list of strings into one.", "instructions": "## Task: Join Words\\nJoin the list of words into a single string separated by spaces.", "starterCode": "words = ['Hello', 'world']\\nsentence = '___'.___(words)", "solution": "words = ['Hello', 'world']\\nsentence = ' '.join(words)", "hint": "Use ' '.join()", "rubric": "Uses ' '.join(words)."}
        ]
    },
    "Error Handling": {
        "tier": "Intermediate",
        "aiRubric": "Assess Python exception handling",
        "lessons": [
            {"title": "Try Except Blocks", "theory": "## Catching Exceptions\\nTo prevent your program from crashing when an error occurs, you can wrap risky code in a `try` block and handle the error in an `except` block.", "instructions": "## Task: Catch Division by Zero\\nCatch the specific error that occurs when dividing by zero.", "starterCode": "try:\\n    result = 10 / 0\\nexcept ___:\\n    print(\"Cannot divide by zero!\")", "solution": "try:\\n    result = 10 / 0\\nexcept ZeroDivisionError:\\n    print(\"Cannot divide by zero!\")", "hint": "The error is ZeroDivisionError", "rubric": "Uses ZeroDivisionError."},
            {"title": "Finally Clause", "theory": "## Guaranteed Execution\\nThe `finally` block executes regardless of whether an exception was thrown or caught. It's often used for cleanup, like closing files.", "instructions": "## Task: Add Finally\\nAdd the block that ensures 'Cleanup done.' is always printed.", "starterCode": "try:\\n    pass\\nexcept Exception:\\n    pass\\n___:\\n    print(\"Cleanup done.\")", "solution": "try:\\n    pass\\nexcept Exception:\\n    pass\\nfinally:\\n    print(\"Cleanup done.\")", "hint": "Use the finally keyword", "rubric": "Uses the finally block."}
        ]
    },
    "List Comprehensions": {
        "tier": "Intermediate",
        "aiRubric": "Assess list comprehension syntax",
        "lessons": [
            {"title": "Compact Loops", "theory": "## Pythonic Lists\\nA list comprehension provides a shorter syntax to create a new list based on the values of an existing list.", "instructions": "## Task: Square the Numbers\\nUse a list comprehension to create a list of squares for `x` in `nums`.", "starterCode": "nums = [1, 2, 3]\\nsquares = [___ for ___ in ___]", "solution": "nums = [1, 2, 3]\\nsquares = [x**2 for x in nums]", "hint": "Use x**2 for x in nums", "rubric": "Correctly writes x**2 for x in nums."},
            {"title": "Adding Conditions", "theory": "## Filtering Lists\\nYou can add an `if` statement to the end of a list comprehension to filter items.", "instructions": "## Task: Filter Evens\\nCreate a list of only the even numbers from `nums`.", "starterCode": "nums = [1, 2, 3, 4]\\nevens = [x for x in nums if x ___ 2 == ___]", "solution": "nums = [1, 2, 3, 4]\\nevens = [x for x in nums if x % 2 == 0]", "hint": "Use x % 2 == 0", "rubric": "Correctly uses x % 2 == 0."}
        ]
    },
    "Context Managers": {
        "tier": "Advanced",
        "aiRubric": "Assess context managers",
        "lessons": [
            {"title": "The With Statement", "theory": "## Automatic Resource Management\\nThe `with` statement in Python is used with context managers to automatically acquire and release resources, ensuring files are closed even if errors occur.", "instructions": "## Task: Open a File\\nUse the `with` statement to open 'data.txt' in read mode.", "starterCode": "___ open('data.txt', 'r') ___ f:\\n    content = f.read()", "solution": "with open('data.txt', 'r') as f:\\n    content = f.read()", "hint": "Use with ... as f:", "rubric": "Correctly uses with and as."},
            {"title": "Custom Context Managers", "theory": "## __enter__ and __exit__\\nTo create a custom class that works with the `with` statement, you must implement the `__enter__` and `__exit__` dunder methods.", "instructions": "## Task: Define Enter Method\\nDefine the magic method that is called when entering the `with` block.", "starterCode": "class Timer:\\n    def ___(self):\\n        self.start = time.time()\\n        return self", "solution": "class Timer:\\n    def __enter__(self):\\n        self.start = time.time()\\n        return self", "hint": "The method is __enter__", "rubric": "Defines __enter__ method."}
        ]
    },
    "Concurrency & Asyncio": {
        "tier": "Advanced",
        "aiRubric": "Assess asyncio and concurrency",
        "lessons": [
            {"title": "Async/Await", "theory": "## Asynchronous I/O\\n`asyncio` allows you to write concurrent code using the `async` and `await` syntax. It is perfect for IO-bound tasks like network requests.", "instructions": "## Task: Define Async Function\\nDefine a coroutine function named `fetch_data`.", "starterCode": "___ def fetch_data():\\n    pass", "solution": "async def fetch_data():\\n    pass", "hint": "Use the async keyword", "rubric": "Correctly uses the async keyword."},
            {"title": "Awaiting Coroutines", "theory": "## Yielding Control\\nWhen you use `await`, the function yields control back to the event loop until the awaited task is complete, allowing other tasks to run.", "instructions": "## Task: Await Sleep\\nPause the coroutine for 1 second without blocking the entire thread.", "starterCode": "import asyncio\\n\\nasync def main():\\n    ___ asyncio.sleep(1)", "solution": "import asyncio\\n\\nasync def main():\\n    await asyncio.sleep(1)", "hint": "Use the await keyword", "rubric": "Correctly uses the await keyword."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'python_core.json')
    
    # 1. Update python_core.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH45.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH45.items():
            tier = course_info["tier"]
            if "Python Core" in index_data and tier in index_data["Python Core"]:
                if new_course_name not in index_data["Python Core"][tier]:
                    index_data["Python Core"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 45: Added {total} lessons to Python Core track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
