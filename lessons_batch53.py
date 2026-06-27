"""
Batch 53: Deep Dive into Python Core (Advanced OOP & Magic Methods)
"""
import json, os

NEW_COURSES_BATCH53 = {
    "Advanced OOP & Magic Methods": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of Python's data model and magic methods",
        "lessons": [
            {"title": "Instantiation vs Initialization", "theory": "## Object Creation\\nMost developers only use `__init__` (Initialization). But `__new__` is the method actually responsible for *Creating* (Instantiating) the object before `__init__` is ever called.", "instructions": "## Task: The True Constructor\\nWhat magic method is the true constructor of a class and must return an instance?", "starterCode": "true_constructor = '___'", "solution": "true_constructor = '__new__'", "hint": "It's __new__", "rubric": "Identifies __new__."},
            {"title": "Str vs Repr", "theory": "## String Representation\\n`__str__` is meant to be readable for end-users, while `__repr__` is meant to be unambiguous for developers (ideally, it should return a string that could recreate the object).", "instructions": "## Task: Implement Repr\\nImplement the `__repr__` method to return 'Point(x, y)'.", "starterCode": "class Point:\\n    def __init__(self, x, y):\\n        self.x, self.y = x, y\\n    def ___:\\n        return f'Point({self.x}, {self.y})'", "solution": "class Point:\\n    def __init__(self, x, y):\\n        self.x, self.y = x, y\\n    def __repr__(self):\\n        return f'Point({self.x}, {self.y})'", "hint": "Define def __repr__(self):", "rubric": "Defines __repr__."},
            {"title": "Equality and Hashing", "theory": "## Custom Comparisons\\nBy default, objects are compared by memory address. Overriding `__eq__` lets you compare them by value. If you override `__eq__` and want the object to be used as a dictionary key, you MUST also override `__hash__`.", "instructions": "## Task: Override Equality\\nOverride the method that is called when you do `obj1 == obj2`.", "starterCode": "class Item:\\n    def ___:\\n        return self.id == other.id", "solution": "class Item:\\n    def __eq__(self, other):\\n        return self.id == other.id", "hint": "Define def __eq__(self, other):", "rubric": "Defines __eq__(self, other)."},
            {"title": "Property Decorators", "theory": "## Managed Attributes\\nThe `@property` decorator allows you to define methods that can be accessed like attributes, giving you getter/setter control without breaking the API.", "instructions": "## Task: Make a Getter\\nTurn the `temperature` method into a read-only property.", "starterCode": "class Sensor:\\n    ___\\n    def temperature(self):\\n        return 72", "solution": "class Sensor:\\n    @property\\n    def temperature(self):\\n        return 72", "hint": "Use @property", "rubric": "Uses @property decorator."},
            {"title": "Classmethods vs Staticmethods", "theory": "## Method Binding\\nInstance methods take `self`. `@classmethod` takes `cls` and is often used for alternative constructors. `@staticmethod` takes neither and is just a regular function living in a class namespace.", "instructions": "## Task: Alternative Constructor\\nUse the correct decorator to create a factory method that takes the class `cls` as its first argument.", "starterCode": "class User:\\n    ___\\n    def from_string(cls, data):\\n        return cls(data)", "solution": "class User:\\n    @classmethod\\n    def from_string(cls, data):\\n        return cls(data)", "hint": "Use @classmethod", "rubric": "Uses @classmethod."},
            {"title": "Multiple Inheritance & MRO", "theory": "## Method Resolution Order\\nWhen inheriting from multiple classes, Python uses C3 Linearization to determine the Method Resolution Order (MRO). You can view this order by checking `ClassName.__mro__`.", "instructions": "## Task: Check the MRO\\nAccess the built-in attribute that lists the class search path for method resolution.", "starterCode": "mro_tuple = MyClass.___", "solution": "mro_tuple = MyClass.__mro__", "hint": "Access __mro__", "rubric": "Uses __mro__."},
            {"title": "Callable Instances", "theory": "## Objects as Functions\\nBy implementing the `__call__` magic method, you can execute an instance of a class exactly as if it were a function.", "instructions": "## Task: Make it Callable\\nDefine the magic method so that calling `counter()` executes it.", "starterCode": "class Counter:\\n    def ___:\\n        self.count += 1\\n\\ncounter = Counter()\\ncounter()", "solution": "class Counter:\\n    def __call__(self):\\n        self.count += 1\\n\\ncounter = Counter()\\ncounter()", "hint": "Define def __call__(self):", "rubric": "Defines __call__."},
            {"title": "Indexing and Slicing", "theory": "## Behaving like a List\\nIf you want your custom object to support indexing like `my_obj[0]` or dictionary lookups like `my_obj['key']`, you implement `__getitem__` and `__setitem__`.", "instructions": "## Task: Implement Get Item\\nDefine the magic method that is triggered by bracket notation.", "starterCode": "class CustomList:\\n    def ___:\\n        return self.data[index]", "solution": "class CustomList:\\n    def __getitem__(self, index):\\n        return self.data[index]", "hint": "Define def __getitem__(self, index):", "rubric": "Defines __getitem__."}
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
        
        for new_course_name, course_info in NEW_COURSES_BATCH53.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH53.items():
            tier = course_info["tier"]
            if "Python Core" in index_data and tier in index_data["Python Core"]:
                if new_course_name not in index_data["Python Core"][tier]:
                    index_data["Python Core"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 53: Added {total} lessons to Python Core track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
