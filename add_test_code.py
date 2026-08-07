import json
import os

path = "curriculum/tracks/python_core.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Add testCode to the first lesson "Variables & Data Types"
if "Python Basics" in data:
    for lesson in data["Python Basics"]["lessons"]:
        if lesson["title"] == "Variables & Data Types":
            lesson["testCode"] = """
assert 'name' in locals() and type(name) == str, "Error: 'name' variable must be a string"
assert 'age' in locals() and type(age) == int, "Error: 'age' variable must be an integer"
assert 'gpa' in locals() and type(gpa) == float, "Error: 'gpa' variable must be a float"
print('\\n✅ Automatic Tests Passed! You can move to the next lesson.')
"""
        elif lesson["title"] == "String Operations":
            lesson["testCode"] = """
assert 'sentence' in locals(), "Error: 'sentence' variable missing"
assert sentence == 'python is amazing', "Error: sentence must be 'python is amazing'"
print('\\n✅ Automatic Tests Passed! You can move to the next lesson.')
"""
        elif lesson["title"] == "Type Conversion":
            lesson["testCode"] = """
assert 'num' in locals() and type(num) == int, "Error: 'num' must be an int"
assert 'num_float' in locals() and type(num_float) == float, "Error: 'num_float' must be a float"
assert 'num_str' in locals() and type(num_str) == str, "Error: 'num_str' must be a str"
print('\\n✅ Automatic Tests Passed! You can move to the next lesson.')
"""

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("testCode added to Python Basics successfully!")
