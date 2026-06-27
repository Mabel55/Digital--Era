"""
Batch 50: Expanding Python Core Curriculum (Dicts & Sets, Lambdas, Regex, Metaclasses, Type Hinting)
"""
import json, os

NEW_COURSES_BATCH50 = {
    "Dictionaries & Sets": {
        "tier": "Beginner",
        "aiRubric": "Assess dictionary and set operations",
        "lessons": [
            {"title": "Key-Value Pairs", "theory": "## Dictionaries\\nA dictionary (`dict`) stores data in key-value pairs. Keys must be unique and immutable (like strings or numbers).", "instructions": "## Task: Accessing Values\\nRetrieve the value associated with the key 'age' from the dictionary.", "starterCode": "person = {'name': 'Alice', 'age': 30}\\nuser_age = person['___']", "solution": "person = {'name': 'Alice', 'age': 30}\\nuser_age = person['age']", "hint": "Use 'age' as the key", "rubric": "Correctly accesses the 'age' key."},
            {"title": "Unique Elements", "theory": "## Sets\\nA set is an unordered collection of unique elements. It is highly optimized for checking if an item exists within it.", "instructions": "## Task: Remove Duplicates\\nConvert the list to a set to automatically remove duplicate values.", "starterCode": "nums = [1, 2, 2, 3, 3, 3]\\nunique_nums = ___(nums)", "solution": "nums = [1, 2, 2, 3, 3, 3]\\nunique_nums = set(nums)", "hint": "Use the set() constructor", "rubric": "Uses set(nums)."}
        ]
    },
    "Lambda Functions & Map/Filter": {
        "tier": "Intermediate",
        "aiRubric": "Assess lambda and functional programming",
        "lessons": [
            {"title": "Anonymous Functions", "theory": "## Lambdas\\nA lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.", "instructions": "## Task: Write a Lambda\\nWrite a lambda function that multiplies its argument `x` by 10.", "starterCode": "multiply_by_10 = ___ x: x ___ 10", "solution": "multiply_by_10 = lambda x: x * 10", "hint": "Use lambda and *", "rubric": "Correctly defines the lambda x: x * 10."},
            {"title": "Map and Filter", "theory": "## Functional Tools\\n`map()` applies a function to all items in an iterable. `filter()` creates a list of elements for which a function returns True.", "instructions": "## Task: Map a Function\\nUse `map` to apply the `str` function to every integer in the list.", "starterCode": "nums = [1, 2, 3]\\nstr_nums = list(map(___, nums))", "solution": "nums = [1, 2, 3]\\nstr_nums = list(map(str, nums))", "hint": "Pass the 'str' function to map", "rubric": "Uses map(str, nums)."}
        ]
    },
    "Regular Expressions in Python": {
        "tier": "Intermediate",
        "aiRubric": "Assess regex module usage",
        "lessons": [
            {"title": "The RE Module", "theory": "## Pattern Matching\\nPython's built-in `re` module allows you to search, replace, and parse strings using Regular Expressions.", "instructions": "## Task: Find All\\nUse `re.findall()` to find all occurrences of digits (`\\d+`) in the string.", "starterCode": "import re\\n\\ntext = 'I have 2 apples and 10 oranges.'\\nnumbers = re.findall(r'___', text)", "solution": "import re\\n\\ntext = 'I have 2 apples and 10 oranges.'\\nnumbers = re.findall(r'\\d+', text)", "hint": "Use \\d+", "rubric": "Correctly uses \\d+ to match digits."},
            {"title": "Regex Substitution", "theory": "## Search and Replace\\nThe `re.sub()` function replaces the matches in a string with a replacement string.", "instructions": "## Task: Redact Info\\nUse `re.sub()` to replace any sequence of digits with the string '[REDACTED]'.", "starterCode": "import re\\n\\ntext = 'My pin is 1234'\\nredacted = re.sub(r'\\d+', '___', text)", "solution": "import re\\n\\ntext = 'My pin is 1234'\\nredacted = re.sub(r'\\d+', '[REDACTED]', text)", "hint": "Use '[REDACTED]'", "rubric": "Replaces with '[REDACTED]'."}
        ]
    },
    "Metaclasses": {
        "tier": "Advanced",
        "aiRubric": "Assess metaclass concepts",
        "lessons": [
            {"title": "Classes are Objects", "theory": "## The Class Factory\\nIn Python, a class is just an object that creates instances. A Metaclass is the 'class of a class'—it is the factory that creates class objects.", "instructions": "## Task: Identify the Base\\nWhat is the built-in metaclass that all default Python classes are instances of?", "starterCode": "# Options: object, type, class\\ndefault_metaclass = '___'", "solution": "# Options: object, type, class\\ndefault_metaclass = 'type'", "hint": "The answer is 'type'", "rubric": "Identifies 'type'."},
            {"title": "Custom Metaclasses", "theory": "## Hooking into Class Creation\\nBy overriding `__new__` in a metaclass, you can automatically alter the attributes or methods of a class at the exact moment it is defined.", "instructions": "## Task: Metaclass Keyword\\nSpecify `MyMeta` as the metaclass for the `MyClass` definition.", "starterCode": "class MyClass(___ = MyMeta):\\n    pass", "solution": "class MyClass(metaclass = MyMeta):\\n    pass", "hint": "Use the 'metaclass' keyword argument", "rubric": "Uses metaclass=MyMeta."}
        ]
    },
    "Type Hinting & Pydantic": {
        "tier": "Advanced",
        "aiRubric": "Assess modern python typing",
        "lessons": [
            {"title": "Static Typing", "theory": "## Hints, not Rules\\nPython 3.5+ introduced type hints. They don't enforce types at runtime, but they allow IDEs and tools like `mypy` to catch bugs before you run the code.", "instructions": "## Task: Hint a Return Type\\nAdd a type hint indicating that the function `greet` returns a `str`.", "starterCode": "def greet(name: str) -> ___:\\n    return f'Hello {name}'", "solution": "def greet(name: str) -> str:\\n    return f'Hello {name}'", "hint": "Use -> str:", "rubric": "Correctly sets the return type to str."},
            {"title": "Pydantic Models", "theory": "## Runtime Validation\\nUnlike standard type hints, the `pydantic` library uses type hints to perform *strict runtime validation* and data parsing. It is heavily used in FastAPI.", "instructions": "## Task: Base Model\\nMake the `User` class inherit from Pydantic's `BaseModel`.", "starterCode": "from pydantic import BaseModel\\n\\nclass User(___):\\n    id: int\\n    name: str", "solution": "from pydantic import BaseModel\\n\\nclass User(BaseModel):\\n    id: int\\n    name: str", "hint": "Inherit from BaseModel", "rubric": "Inherits from BaseModel."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'python_core.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH50.items():
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
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH50.items():
            tier = course_info["tier"]
            if "Python Core" in index_data and tier in index_data["Python Core"]:
                if new_course_name not in index_data["Python Core"][tier]:
                    index_data["Python Core"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 50: Added {total} lessons to Python Core track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
