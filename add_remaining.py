"""
Phase 8: Add 25 lessons to the 10 remaining tracks (250 new lessons total).
Each track has 3 courses. We add 8, 8, and 9 lessons to them respectively.
"""
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
        "title": "Core Concepts of {course}",
        "theory": "## Understanding {course}\\nBefore diving into complex implementations, it's essential to understand the foundational principles of {course}.",
        "instructions": "## Task: Define Core Concept\\n1. Create a function `get_concept()` that returns the string '{course} Foundation'.",
        "starterCode": "def get_concept():\\n    return '___'",
        "solution": "def get_concept():\\n    return '{course} Foundation'",
        "hint": "Return the exact string '{course} Foundation'.",
        "rubric": "Function returns the correct concept string."
    },
    {
        "title": "Setting up the Environment for {course}",
        "theory": "## Tooling\\nProperly configuring your development environment is the first step in mastering {course}.",
        "instructions": "## Task: Environment Status\\n1. Create a function `is_ready()` that returns True.",
        "starterCode": "def is_ready():\\n    return ___",
        "solution": "def is_ready():\\n    return True",
        "hint": "Return True.",
        "rubric": "Function returns True."
    },
    {
        "title": "Basic Syntax and Operations",
        "theory": "## Syntax Rules\\nEvery discipline has its syntax. Here we apply standard operations relevant to {course}.",
        "instructions": "## Task: Basic Math\\n1. Return the sum of a and b.",
        "starterCode": "def add(a, b):\\n    return a ___ b",
        "solution": "def add(a, b):\\n    return a + b",
        "hint": "Use the + operator.",
        "rubric": "Function adds two numbers."
    },
    {
        "title": "Control Structures in {course}",
        "theory": "## Branching\\nConditional logic dictates how applications respond to different states.",
        "instructions": "## Task: Check State\\n1. Return 'Active' if state is 1, else 'Inactive'.",
        "starterCode": "def check_state(state):\\n    if state == 1:\\n        return '___'\\n    return '___'",
        "solution": "def check_state(state):\\n    if state == 1:\\n        return 'Active'\\n    return 'Inactive'",
        "hint": "Return Active or Inactive.",
        "rubric": "Logic branches correctly."
    },
    {
        "title": "Advanced Memory Management",
        "theory": "## Resource Allocation\\nEfficient memory use is critical, especially when applying {course} at scale.",
        "instructions": "## Task: Clear Memory\\n1. Set the variable `cache` to an empty dictionary.",
        "starterCode": "cache = {'data': 123}\\ncache = ___",
        "solution": "cache = {'data': 123}\\ncache = {}",
        "hint": "Use {}.",
        "rubric": "Cache is cleared."
    },
    {
        "title": "Object-Oriented Approaches",
        "theory": "## OOP\\nEncapsulating state and behavior within objects helps structure {course} projects.",
        "instructions": "## Task: Create Class\\n1. Create a class `Module` with a property `name` initialized to '{course}'.",
        "starterCode": "class Module:\\n    def __init__(self):\\n        self.name = '___'",
        "solution": "class Module:\\n    def __init__(self):\\n        self.name = '{course}'",
        "hint": "Use '{course}'.",
        "rubric": "Class encapsulates state."
    },
    {
        "title": "Functional Programming Paradigms",
        "theory": "## Pure Functions\\nFunctional programming avoids side effects. This is increasingly popular in {course}.",
        "instructions": "## Task: Pure Function\\n1. Write a function `square(x)` that returns x squared.",
        "starterCode": "def square(x):\\n    return x ___ ___",
        "solution": "def square(x):\\n    return x ** 2",
        "hint": "Use ** 2.",
        "rubric": "Pure function implemented."
    },
    {
        "title": "Error Handling and Debugging",
        "theory": "## Resilience\\nHandling exceptions gracefully ensures robustness in {course}.",
        "instructions": "## Task: Try/Except\\n1. Wrap the division in a try block, catch ZeroDivisionError, and return None.",
        "starterCode": "def safe_div(a, b):\\n    try:\\n        return a / b\\n    ___ ZeroDivisionError:\\n        return ___",
        "solution": "def safe_div(a, b):\\n    try:\\n        return a / b\\n    except ZeroDivisionError:\\n        return None",
        "hint": "Use except and return None.",
        "rubric": "Exceptions caught properly."
    },
    {
        "title": "Concurrency and Async Operations",
        "theory": "## Asynchronous Work\\nBlocking operations freeze applications. Async allows overlapping tasks in {course}.",
        "instructions": "## Task: Async Function\\n1. Define an async function `fetch_data()`.",
        "starterCode": "___ def fetch_data():\\n    return 'Data'",
        "solution": "async def fetch_data():\\n    return 'Data'",
        "hint": "Use async def.",
        "rubric": "Async function defined."
    },
    {
        "title": "Working with Data Structures",
        "theory": "## Data Organization\\nChoosing the right data structure dictates performance.",
        "instructions": "## Task: Use a Set\\n1. Return a set containing the elements 1, 2, 3.",
        "starterCode": "def get_set():\\n    return ___[1, 2, 3]___",
        "solution": "def get_set():\\n    return {1, 2, 3}",
        "hint": "Use {} for sets.",
        "rubric": "Set structure utilized."
    },
    {
        "title": "Network Communication Protocols",
        "theory": "## Connectivity\\nUnderstanding HTTP/TCP is essential for networked components in {course}.",
        "instructions": "## Task: HTTP Status\\n1. Return 200 for OK.",
        "starterCode": "status_code = ___",
        "solution": "status_code = 200",
        "hint": "200",
        "rubric": "Status code set."
    },
    {
        "title": "File I/O and Storage",
        "theory": "## Persistence\\nSaving data to disk allows state to survive reboots.",
        "instructions": "## Task: Open File\\n1. Write code to open 'data.txt' in read mode.",
        "starterCode": "f = open('data.txt', '___')",
        "solution": "f = open('data.txt', 'r')",
        "hint": "Use 'r'.",
        "rubric": "File opened in correct mode."
    },
    {
        "title": "Security Best Practices",
        "theory": "## Defense\\nProtecting applications from vulnerabilities is non-negotiable.",
        "instructions": "## Task: Hash Length\\n1. Return 64, the length of a SHA-256 hash in hex.",
        "starterCode": "sha256_length = ___",
        "solution": "sha256_length = 64",
        "hint": "64",
        "rubric": "Security constant identified."
    },
    {
        "title": "Performance Optimization Strategies",
        "theory": "## Efficiency\\nOptimizing critical paths improves throughput in {course}.",
        "instructions": "## Task: Time Complexity\\n1. Return 'O(1)' for constant time complexity.",
        "starterCode": "constant_time = '___'",
        "solution": "constant_time = 'O(1)'",
        "hint": "O(1)",
        "rubric": "Complexity identified."
    },
    {
        "title": "Unit Testing Fundamentals",
        "theory": "## Validation\\nUnit tests verify that individual components work as expected.",
        "instructions": "## Task: Assert True\\n1. Write an assert statement that 1 equals 1.",
        "starterCode": "___ 1 == 1",
        "solution": "assert 1 == 1",
        "hint": "assert",
        "rubric": "Assertion written."
    },
    {
        "title": "Integration Testing",
        "theory": "## System Harmony\\nIntegration tests ensure that components function together.",
        "instructions": "## Task: Integration Status\\n1. Set `integrated` to True.",
        "starterCode": "integrated = ___",
        "solution": "integrated = True",
        "hint": "True",
        "rubric": "Status set."
    },
    {
        "title": "Continuous Integration Setup",
        "theory": "## CI Pipelines\\nCI automatically runs tests when code is pushed.",
        "instructions": "## Task: Pipeline Step\\n1. Create a list with 'build', 'test', 'deploy'.",
        "starterCode": "pipeline = ['___', '___', '___']",
        "solution": "pipeline = ['build', 'test', 'deploy']",
        "hint": "build, test, deploy",
        "rubric": "Pipeline steps defined."
    },
    {
        "title": "Deployment Pipelines",
        "theory": "## Shipping Code\\nDeploying reliably requires automated release pipelines.",
        "instructions": "## Task: Environment\\n1. Set `env` to 'production'.",
        "starterCode": "env = '___'",
        "solution": "env = 'production'",
        "hint": "production",
        "rubric": "Environment set."
    },
    {
        "title": "Logging and Monitoring",
        "theory": "## Observability\\nLogs help diagnose issues in production.",
        "instructions": "## Task: Log Level\\n1. Set `level` to 'ERROR'.",
        "starterCode": "level = '___'",
        "solution": "level = 'ERROR'",
        "hint": "ERROR",
        "rubric": "Log level defined."
    },
    {
        "title": "Design Patterns in {course}",
        "theory": "## Reusable Solutions\\nDesign patterns solve common architectural problems.",
        "instructions": "## Task: Singleton\\n1. Set `pattern` to 'Singleton'.",
        "starterCode": "pattern = '___'",
        "solution": "pattern = 'Singleton'",
        "hint": "Singleton",
        "rubric": "Pattern named."
    },
    {
        "title": "API Integration Strategies",
        "theory": "## Connecting Services\\nAPIs allow different systems to communicate.",
        "instructions": "## Task: JSON Data\\n1. Set `format` to 'JSON'.",
        "starterCode": "format = '___'",
        "solution": "format = 'JSON'",
        "hint": "JSON",
        "rubric": "Format specified."
    },
    {
        "title": "Database Connectivity",
        "theory": "## Data Access\\nConnecting to a DB safely is essential.",
        "instructions": "## Task: Connection String\\n1. Set `conn_str` to 'postgres://localhost'.",
        "starterCode": "conn_str = '___'",
        "solution": "conn_str = 'postgres://localhost'",
        "hint": "postgres://localhost",
        "rubric": "Connection string created."
    },
    {
        "title": "Scaling Applications",
        "theory": "## Horizontal Scaling\\nAdding more instances handles increased load.",
        "instructions": "## Task: Instance Count\\n1. Set `instances` to 3.",
        "starterCode": "instances = ___",
        "solution": "instances = 3",
        "hint": "3",
        "rubric": "Instances scaled."
    },
    {
        "title": "Microservices Architecture",
        "theory": "## Decoupling\\nMicroservices break large apps into independent services.",
        "instructions": "## Task: Service Name\\n1. Set `service` to 'Auth'.",
        "starterCode": "service = '___'",
        "solution": "service = 'Auth'",
        "hint": "Auth",
        "rubric": "Service named."
    },
    {
        "title": "Best Practices and Anti-patterns",
        "theory": "## Writing Clean Code\\nMaintainability ensures the long-term success of {course} projects.",
        "instructions": "## Task: Clean Code\\n1. Set `is_clean` to True.",
        "starterCode": "is_clean = ___",
        "solution": "is_clean = True",
        "hint": "True",
        "rubric": "Clean code enabled."
    }
]

def generate_lessons(course_name, template_subset):
    generated = []
    for t in template_subset:
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
        # We need 25 lessons total. Distribution: 8, 8, 9
        if len(courses) >= 3:
            dist = [8, 8, 9]
        elif len(courses) == 2:
            dist = [12, 13]
        elif len(courses) == 1:
            dist = [25]
        else:
            dist = []

        template_index = 0
        added_to_track = 0
        for i, course_name in enumerate(courses):
            if i < len(dist):
                count = dist[i]
                subset = TEMPLATES[template_index : template_index + count]
                template_index += count
                
                new_lessons = generate_lessons(course_name, subset)
                data[course_name]["lessons"].extend(new_lessons)
                added_to_track += len(new_lessons)
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"[OK] {filename}: added {added_to_track} lessons.")
        total_added += added_to_track
        
    print(f"\\nDone! Added {total_added} lessons across 10 files.")

if __name__ == "__main__":
    process_files()
