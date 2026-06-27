"""
Batch 61: Deep Dive into Python Core (Data Classes & Modern Python Masterclass)
"""
import json, os

NEW_COURSES_BATCH61 = {
    "Data Classes & Modern Python Masterclass": {
        "tier": "Intermediate",
        "aiRubric": "Assess deep understanding of modern Python features (3.7 - 3.10+)",
        "lessons": [
            {"title": "Introduction to Data Classes", "theory": "## Less Boilerplate\\nIntroduced in Python 3.7, `@dataclass` automatically generates special methods like `__init__`, `__repr__`, and `__eq__` for classes that primarily store data.", "instructions": "## Task: The Decorator\\nApply the decorator from the `dataclasses` module to automatically generate an `__init__` method for the `User` class.", "starterCode": "from dataclasses import dataclass\\n\\n___\\nclass User:\\n    name: str\\n    age: int", "solution": "from dataclasses import dataclass\\n\\n@dataclass\\nclass User:\\n    name: str\\n    age: int", "hint": "Use @dataclass", "rubric": "Uses @dataclass."},
            {"title": "Default Factories", "theory": "## Mutable Defaults\\nIn Python, you should never use a mutable object (like an empty list) as a default argument. In dataclasses, you solve this by using `field(default_factory=list)` to create a fresh list for every instance.", "instructions": "## Task: Safe Defaults\\nUse `field` and `default_factory` to safely initialize `items` as an empty list.", "starterCode": "from dataclasses import dataclass, field\\n\\n@dataclass\\nclass Cart:\\n    items: list = ___(default_factory=___)", "solution": "from dataclasses import dataclass, field\\n\\n@dataclass\\nclass Cart:\\n    items: list = field(default_factory=list)", "hint": "Use field and list", "rubric": "Uses field(default_factory=list)."},
            {"title": "Post-Init Processing", "theory": "## After Initialization\\nBecause `@dataclass` generates `__init__` for you, you can't put custom validation logic in it. Instead, dataclasses provide a `__post_init__` method that runs immediately after the generated `__init__`.", "instructions": "## Task: Custom Validation\\nDefine the magic method that dataclasses call right after initialization.", "starterCode": "@dataclass\\nclass Person:\\n    age: int\\n\\n    def ___:\\n        if self.age < 0:\\n            raise ValueError('Age cannot be negative')", "solution": "@dataclass\\nclass Person:\\n    age: int\\n\\n    def __post_init__(self):\\n        if self.age < 0:\\n            raise ValueError('Age cannot be negative')", "hint": "Define def __post_init__(self):", "rubric": "Defines __post_init__."},
            {"title": "The Walrus Operator", "theory": "## Assignment Expressions\\nIntroduced in Python 3.8, the walrus operator `:=` allows you to assign a value to a variable and return that value in the same expression. This is very useful in `if` and `while` loops.", "instructions": "## Task: Assign and Check\\nUse the walrus operator to assign the result of `get_data()` to `data` and check if it is truthy in one line.", "starterCode": "if (data ___ get_data()):\\n    print(f'Received: {data}')", "solution": "if (data := get_data()):\\n    print(f'Received: {data}')", "hint": "Use :=", "rubric": "Uses :=."},
            {"title": "Structural Pattern Matching", "theory": "## Match / Case\\nIntroduced in Python 3.10, `match / case` acts like a supercharged switch statement. It doesn't just match values; it can match structures, types, and unpack data.", "instructions": "## Task: Pattern Matching\\nUse the correct keyword to match the `status` variable against cases.", "starterCode": "___ status:\\n    case 200:\\n        print('OK')\\n    case 404:\\n        print('Not Found')", "solution": "match status:\\n    case 200:\\n        print('OK')\\n    case 404:\\n        print('Not Found')", "hint": "Use match", "rubric": "Uses match."},
            {"title": "F-String Debugging", "theory": "## Self-Documenting Strings\\nIn Python 3.8, f-strings got a powerful debugging feature. Adding an equals sign `=` to the end of a variable inside an f-string will print both the variable name and its value.", "instructions": "## Task: Debug Print\\nUse the f-string debugging feature so that it prints 'user_id=42'.", "starterCode": "user_id = 42\\nprint(f'{user_id___}')", "solution": "user_id = 42\\nprint(f'{user_id=}')", "hint": "Add an = sign", "rubric": "Adds =."},
            {"title": "Dictionary Union Operators", "theory": "## Merging Dicts Cleanly\\nIn Python 3.9, you can merge dictionaries using the `|` operator, and update them using the `|=` operator, similar to how sets work. If there are duplicate keys, the right-side dictionary wins.", "instructions": "## Task: Merge Dictionaries\\nUse the pipe operator to merge `dict1` and `dict2` into a new dictionary.", "starterCode": "dict1 = {'a': 1, 'b': 2}\\ndict2 = {'b': 3, 'c': 4}\\nmerged = dict1 ___ dict2", "solution": "dict1 = {'a': 1, 'b': 2}\\ndict2 = {'b': 3, 'c': 4}\\nmerged = dict1 | dict2", "hint": "Use the | operator", "rubric": "Uses |."},
            {"title": "Positional-Only Parameters", "theory": "## Enforcing API Design\\nIn Python 3.8, the `/` syntax was introduced in function signatures to indicate that some parameters *must* be passed positionally and cannot be passed as keyword arguments.", "instructions": "## Task: Positional Only\\nPlace the correct symbol to enforce that `x` and `y` must be positional, but `z` can be a keyword argument.", "starterCode": "def power(x, y, ___, z=1):\\n    return (x ** y) * z", "solution": "def power(x, y, /, z=1):\\n    return (x ** y) * z", "hint": "Use the / symbol", "rubric": "Uses /."}
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
        
        for new_course_name, course_info in NEW_COURSES_BATCH61.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH61.items():
            tier = course_info["tier"]
            if "Python Core" in index_data and tier in index_data["Python Core"]:
                if new_course_name not in index_data["Python Core"][tier]:
                    index_data["Python Core"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 61: Added {total} lessons to Python Core track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
