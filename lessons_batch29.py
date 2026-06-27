"""
Batch 29: Expanding Python Core and AI Engineering Content
"""
import json, os

LESSONS_BATCH29 = {
    # ─── PYTHON CORE ───
    "Functions": [
        {"title": "Lambda Functions", "theory": "## Anonymous Functions\\nSometimes you need a small, throwaway function. Lambda functions allow you to define a function in a single line without a name.\\n\\nSyntax: `lambda arguments: expression`", "instructions": "## Task: Lambda Sorting\\n1. Use a lambda function as the key to sort a list of tuples based on the second element.", "starterCode": "pairs = [(1, 'one'), (3, 'three'), (2, 'two')]\\n\\n# Sort by the second element (the string)\\nsorted_pairs = sorted(pairs, key=___)\\nprint(sorted_pairs)", "solution": "pairs = [(1, 'one'), (3, 'three'), (2, 'two')]\\n\\n# Sort by the second element (the string)\\nsorted_pairs = sorted(pairs, key=lambda x: x[1])\\nprint(sorted_pairs)", "hint": "lambda x: x[1]", "rubric": "Correctly uses a lambda function to sort by the second element."}
    ],
    "Decorators": [
        {"title": "Timing Decorator", "theory": "## Measuring Execution Time\\nDecorators are functions that modify the behavior of other functions. A common use case is measuring how long a function takes to execute.", "instructions": "## Task: Create a Timer\\n1. Implement a decorator `timer` that prints the time taken by the decorated function.", "starterCode": "import time\\n\\ndef timer(func):\\n    def wrapper(*args, **kwargs):\\n        start = time.time()\\n        result = func(*args, **kwargs)\\n        end = time.time()\\n        print(f'{func.__name__} took {end - start:.4f}s')\\n        return result\\n    return ___\\n\\n@timer\\ndef slow_function():\\n    time.sleep(0.5)\\n    return 'Done'\\n\\nprint(slow_function())", "solution": "import time\\n\\ndef timer(func):\\n    def wrapper(*args, **kwargs):\\n        start = time.time()\\n        result = func(*args, **kwargs)\\n        end = time.time()\\n        print(f'{func.__name__} took {end - start:.4f}s')\\n        return result\\n    return wrapper\\n\\n@timer\\ndef slow_function():\\n    time.sleep(0.5)\\n    return 'Done'\\n\\nprint(slow_function())", "hint": "Return the wrapper function.", "rubric": "Decorator correctly returns wrapper and measures time."}
    ],

    # ─── AI ENGINEERING ───
    "Vector Databases": [
        {"title": "Cosine Similarity", "theory": "## Measuring Distance\\nVector Databases find related concepts by calculating the distance between vectors. The most common metric is Cosine Similarity, which measures the angle between two vectors rather than their magnitude.", "instructions": "## Task: Calculate Similarity\\n1. Implement a simple cosine similarity calculation between two 1D lists (vectors) using pure Python.", "starterCode": "import math\\n\\ndef cosine_similarity(v1, v2):\\n    dot_product = sum(a*b for a, b in zip(v1, v2))\\n    mag1 = math.sqrt(sum(a*a for a in v1))\\n    mag2 = math.sqrt(sum(b*b for b in v2))\\n    \\n    return dot_product / (___ * ___)\\n\\nvector_a = [1, 0, 1]\\nvector_b = [0, 1, 1]\\n\\nprint('Similarity:', cosine_similarity(vector_a, vector_b))", "solution": "import math\\n\\ndef cosine_similarity(v1, v2):\\n    dot_product = sum(a*b for a, b in zip(v1, v2))\\n    mag1 = math.sqrt(sum(a*a for a in v1))\\n    mag2 = math.sqrt(sum(b*b for b in v2))\\n    \\n    return dot_product / (mag1 * mag2)\\n\\nvector_a = [1, 0, 1]\\nvector_b = [0, 1, 1]\\n\\nprint('Similarity:', cosine_similarity(vector_a, vector_b))", "hint": "Multiply the magnitudes in the denominator.", "rubric": "Calculates the correct cosine similarity."}
    ],
    "Fine-tuning Models": [
        {"title": "Dataset Preparation", "theory": "## Instruction Tuning Format\\nTo fine-tune an LLM to follow instructions, your dataset must be formatted in a specific way, often called ChatML or an Alpaca-style JSONL format.\\nEach example needs a 'system' prompt, a 'user' query, and an 'assistant' response.", "instructions": "## Task: Format Converter\\n1. Convert a simple Q&A dictionary into the standard messages list format required by OpenAI/Anthropic APIs.", "starterCode": "def format_for_finetuning(system_prompt, question, answer):\\n    return {\\n        'messages': [\\n            {'role': 'system', 'content': ___},\\n            {'role': 'user', 'content': ___},\\n            {'role': 'assistant', 'content': ___}\\n        ]\\n    }\\n\\nprint(format_for_finetuning('You are a helpful bot.', 'What is 2+2?', 'It is 4.'))", "solution": "def format_for_finetuning(system_prompt, question, answer):\\n    return {\\n        'messages': [\\n            {'role': 'system', 'content': system_prompt},\\n            {'role': 'user', 'content': question},\\n            {'role': 'assistant', 'content': answer}\\n        ]\\n    }\\n\\nprint(format_for_finetuning('You are a helpful bot.', 'What is 2+2?', 'It is 4.'))", "hint": "Map the arguments to the content fields.", "rubric": "Successfully constructs the messages list."}
    ]
}

def apply_lessons(tracks_dir):
    total_python = 0
    total_ai = 0
    
    # Python Core
    py_filepath = os.path.join(tracks_dir, 'python_core.json')
    if os.path.exists(py_filepath):
        with open(py_filepath, 'r', encoding='utf-8') as f:
            py_track_data = json.load(f)
            
        py_updated = False
        for course_name in py_track_data:
            if course_name in LESSONS_BATCH29:
                if 'lessons' not in py_track_data[course_name]:
                    py_track_data[course_name]['lessons'] = []
                existing_titles = [l['title'] for l in py_track_data[course_name]['lessons']]
                for new_lesson in LESSONS_BATCH29[course_name]:
                    if new_lesson['title'] not in existing_titles:
                        py_track_data[course_name]['lessons'].append(new_lesson)
                        py_updated = True
                        total_python += 1
                        
        if py_updated:
            with open(py_filepath, 'w', encoding='utf-8') as f:
                json.dump(py_track_data, f, indent=2, ensure_ascii=False)
                
    # AI Engineering
    ai_filepath = os.path.join(tracks_dir, 'ai_engineering.json')
    if os.path.exists(ai_filepath):
        with open(ai_filepath, 'r', encoding='utf-8') as f:
            ai_track_data = json.load(f)
            
        ai_updated = False
        for course_name in ai_track_data:
            if course_name in LESSONS_BATCH29:
                if 'lessons' not in ai_track_data[course_name]:
                    ai_track_data[course_name]['lessons'] = []
                existing_titles = [l['title'] for l in ai_track_data[course_name]['lessons']]
                for new_lesson in LESSONS_BATCH29[course_name]:
                    if new_lesson['title'] not in existing_titles:
                        ai_track_data[course_name]['lessons'].append(new_lesson)
                        ai_updated = True
                        total_ai += 1
                        
        if ai_updated:
            with open(ai_filepath, 'w', encoding='utf-8') as f:
                json.dump(ai_track_data, f, indent=2, ensure_ascii=False)

    print(f'Batch 29: Appended {total_python} new lessons to Python Core')
    print(f'Batch 29: Appended {total_ai} new lessons to AI Engineering')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
