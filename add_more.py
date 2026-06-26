import json
import os

FILES = [
    'agentic_ai_mcp.json',
    'c_programming.json',
    'cloud_devops.json',
    'cloud_native_go.json',
    'computer_vision_deep_learning.json',
    'data_engineering_mlops.json',
    'data_structures_algorithms.json',
    'mobile_development.json',
    'system_design_architecture.json',
    'systems_programming.json'
]

TEMPLATES = [
    {
        "title": "Advanced Debugging in {course}",
        "theory": "## Debugging at Scale\\nFinding hard-to-reproduce bugs requires structured methodology.",
        "instructions": "## Task: Debug Setup\\n1. Return True for debugging active.",
        "starterCode": "debug_active = ___",
        "solution": "debug_active = True",
        "hint": "True",
        "rubric": "Debug activated."
    },
    {
        "title": "Profiling {course} Applications",
        "theory": "## Performance Profiling\\nIdentifying bottlenecks is the first step in optimization.",
        "instructions": "## Task: Profile Scope\\n1. Set `profile_mode` to 'High'.",
        "starterCode": "profile_mode = '___'",
        "solution": "profile_mode = 'High'",
        "hint": "High",
        "rubric": "Profiling set."
    },
    {
        "title": "Memory Leaks and Management",
        "theory": "## Garbage Collection\\nUnderstanding how memory is freed is critical.",
        "instructions": "## Task: GC Status\\n1. Set `gc_enabled` to True.",
        "starterCode": "gc_enabled = ___",
        "solution": "gc_enabled = True",
        "hint": "True",
        "rubric": "GC enabled."
    },
    {
        "title": "Multi-threading Constructs",
        "theory": "## Parallelism\\nUtilizing multiple cores improves execution speed.",
        "instructions": "## Task: Thread Count\\n1. Set `threads` to 8.",
        "starterCode": "threads = ___",
        "solution": "threads = 8",
        "hint": "8",
        "rubric": "Thread count set."
    },
    {
        "title": "Final Project: {course}",
        "theory": "## Capstone\\nApply all learned concepts to build a comprehensive solution.",
        "instructions": "## Task: Project Initialization\\n1. Set `project_name` to '{course} Final'.",
        "starterCode": "project_name = '___'",
        "solution": "project_name = '{course} Final'",
        "hint": "{course} Final",
        "rubric": "Project initialized."
    }
]

def generate_lessons(course_name):
    generated = []
    for t in TEMPLATES:
        gen = {}
        for k, v in t.items():
            gen[k] = v.replace('{course}', course_name)
        generated.append(gen)
    return generated

def process_files():
    base_dir = "curriculum/tracks/"
    total_added = 0
    for filename in FILES:
        path = os.path.join(base_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        courses = list(data.keys())
        if courses:
            # Just add 5 to the first course of each of the 10 tracks
            new_lessons = generate_lessons(courses[0])
            data[courses[0]]["lessons"].extend(new_lessons)
            total_added += len(new_lessons)
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"[OK] {filename}: added {len(new_lessons)} lessons.")
        
    print(f"\\nDone! Added {total_added} lessons across 10 files.")

if __name__ == "__main__":
    process_files()
