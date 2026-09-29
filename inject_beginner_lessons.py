import json
import os

new_lessons = {
    "python_core.json": {
        "course": "Python Basics",
        "lesson": {
            "title": "What is Python?",
            "theory": "## Writing Recipes for Computers\n\nComputers are incredibly fast but completely mindless. Programming is simply the act of writing a highly specific recipe (an algorithm) that tells the computer exactly what to do.\n\n### Why Python?\n\nPython was designed to be easily readable by humans. Unlike older languages that look like dense mathematical formulas, Python looks almost like plain English.\n\n```python\n# This is a comment. The computer ignores it.\n# In Python, we use the 'print' command to make the computer speak.\n\nprint(\"Hello, World!\")\n```\n\n### Doing Math\n\nPython is a powerful calculator out of the box:\n\n```python\nprint(10 + 5)    # Addition (15)\nprint(10 - 2)    # Subtraction (8)\nprint(10 * 3)    # Multiplication (30)\nprint(10 / 2)    # Division (5.0)\n```\n\n### The Rules of Python\n\n1. **Case matters**: `Print` is not the same as `print`.\n2. **Punctuation matters**: Missing a parenthesis `)` will break your code.\n3. **Spacing matters**: Python uses indentation (spaces at the start of a line) to organize code blocks (which you'll learn later). For now, make sure all your code starts at the very left edge of the line.",
            "instructions": "## Task: Your First Code\n1. Use the `print` command to output the exact phrase `\"Hello, Python!\"` (don't forget the quotes).\n2. On the next line, use `print` to calculate `100 * 5` (without quotes!).",
            "starterCode": "print(___)\nprint(___)",
            "solution": "print(\"Hello, Python!\")\nprint(100 * 5)",
            "hint": "Text goes inside quotes \" \". Math goes directly inside the parentheses.",
            "rubric": "Prints Hello Python and 500."
        }
    },
    "sql_databases.json": {
        "course": "SQL SELECTs",
        "lesson": {
            "title": "What is a Database?",
            "theory": "## Beyond the Spreadsheet\n\nIf you've used Excel or Google Sheets, you already understand the basics of a database. A **Relational Database** stores data in **Tables**.\n\n- Each Table represents a specific concept (e.g., `Users`, `Products`, `Orders`).\n- A **Row** (or Record) is one individual item (e.g., one specific User).\n- A **Column** (or Field) is an attribute of that item (e.g., the User's Email or Age).\n\n### Why not just use Excel?\n\n1. **Scale**: A spreadsheet crashes with 1 million rows. A database handles billions of rows easily.\n2. **Rules**: A database enforces strict rules. You can tell a database \"The Age column can NEVER be negative, and the Email column MUST be unique.\" Excel lets users type whatever they want.\n3. **Relationships**: Databases excel at connecting data. An Order record can link directly to a User record.\n\n### What is SQL?\n\nSQL (Structured Query Language) is the language we use to talk to the database. It allows you to ask the database questions (Queries).\n\nInstead of opening a file and using your mouse to filter a column, you write a command:\n\n```sql\n-- Get all users who are 18 or older\nSELECT * FROM Users WHERE Age >= 18;\n```\n\nEvery major tech company in the world uses SQL.",
            "instructions": "## Task: Terminology Check\nWe'll write real SQL in the next lesson. For now, match the database terms to their spreadsheet equivalents.",
            "starterCode": "q1 = \"A single entry for 'Alice' (Spreadsheet Row) is called a ___ in a Database.\"\nq2 = \"The 'Email' header (Spreadsheet Column) is called a ___ in a Database.\"\n\nprint(q1)\nprint(q2)",
            "solution": "q1 = \"A single entry for 'Alice' (Spreadsheet Row) is called a Row (or Record) in a Database.\"\nq2 = \"The 'Email' header (Spreadsheet Column) is called a Column (or Field) in a Database.\"\n\nprint(\"Row/Record\")\nprint(\"Column/Field\")",
            "hint": "Row/Record and Column/Field.",
            "rubric": "Matches terms correctly."
        }
    },
    "data_science.json": {
        "course": "Pandas Intro",
        "lesson": {
            "title": "Data Science & Pandas",
            "theory": "## Making Sense of Data\n\n**Data Science** is the practice of extracting useful insights from raw data. Before we can use AI to predict the future, we have to clean and analyze the data of the past.\n\n### What is Pandas?\n\nIn standard Python, dealing with thousands of rows of data is incredibly tedious. **Pandas** is a powerful Python library built specifically for data analysis. It essentially gives Python a highly-optimized, programmable Excel spreadsheet.\n\n### The DataFrame\n\nThe core of Pandas is the **DataFrame**. A DataFrame is a 2-dimensional table of data with rows and columns.\n\n```python\nimport pandas as pd\n\n# Creating a DataFrame from raw data\ndata = {\n    \"Name\": [\"Alice\", \"Bob\", \"Charlie\"],\n    \"Age\": [25, 30, 22],\n    \"City\": [\"Lagos\", \"Nairobi\", \"Accra\"]\n}\n\ndf = pd.DataFrame(data)\n\n# Looking at the data\nprint(df)\n```\n\n### Why use Pandas over Excel?\n\nIf you have a CSV file with 5 million rows, opening it in Excel will crash your computer. Pandas can load it in seconds, filter it instantly, and perform complex math operations across entire columns simultaneously (called vectorization).",
            "instructions": "## Task: Your First DataFrame\n1. Import pandas as `pd`.\n2. Create a DataFrame `df` using the provided `data` dictionary.\n3. Print the DataFrame to see how it formats the output.",
            "starterCode": "import ___ as pd\n\ndata = {\n    \"Product\": [\"Laptop\", \"Mouse\", \"Keyboard\"],\n    \"Price\": [1200, 25, 75]\n}\n\n# Create the DataFrame\ndf = pd.___(data)\n\n# Print it\nprint(___)",
            "solution": "import pandas as pd\n\ndata = {\n    \"Product\": [\"Laptop\", \"Mouse\", \"Keyboard\"],\n    \"Price\": [1200, 25, 75]\n}\n\n# Create the DataFrame\ndf = pd.DataFrame(data)\n\n# Print it\nprint(df)",
            "hint": "pd.DataFrame(data)",
            "rubric": "Successfully imports pandas, creates DataFrame, and prints it."
        }
    },
    "c_programming.json": {
        "course": "C Syntax",
        "lesson": {
            "title": "How Computers Think",
            "theory": "## The Language of Hardware\n\nC is one of the oldest and most important programming languages in the world. While languages like Python are \"high-level\" (abstracted away from the hardware), C is \"low-level\".\n\nWhen you write C, you are talking almost directly to the computer's CPU and RAM.\n\n### Compilers vs Interpreters\n\n- **Interpreted Languages (Python/JavaScript)**: Another program reads your code line-by-line as it runs and translates it for the computer on the fly. This is slow.\n- **Compiled Languages (C/C++/Rust)**: You run a special tool called a **Compiler** before you run the code. The compiler reads your entire C file and translates it entirely into raw machine code (1s and 0s) creating an `.exe` or executable file. This is blazingly fast.\n\n### Memory Management\n\nIn Python, if you create a variable, the language finds RAM for it, and when you're done, it cleans up the RAM automatically (Garbage Collection).\n\nIn C, **you are the garbage collector**. You must manually ask the operating system for RAM, and manually give it back when you're done. If you forget to give it back, your program causes a \"Memory Leak\" and eventually crashes the computer.\n\nWhy use C? Because it gives you absolute control and maximum performance. It's used to build operating systems, game engines, and embedded systems (like the computer in your microwave).",
            "instructions": "## Task: Conceptual Check\nSet the variable `is_compiled` to True or False depending on whether C is compiled or interpreted.",
            "starterCode": "is_compiled = ___\n\nprint(f\"Is C a compiled language? {is_compiled}\")",
            "solution": "is_compiled = True\n\nprint(f\"Is C a compiled language? {is_compiled}\")",
            "hint": "C uses a compiler to create machine code.",
            "rubric": "Sets is_compiled to True."
        }
    },
    "cloud_native_go.json": {
        "course": "Go Syntax",
        "lesson": {
            "title": "Why Go?",
            "theory": "## The Cloud Native Language\n\n**Go** (or Golang) was created by Google in 2009 to solve the problems of modern cloud infrastructure.\n\nThey wanted a language that was:\n1. Fast like C++ (Compiled).\n2. Easy to read like Python.\n3. Built for the modern web (Concurrency).\n\n### Concurrency (Doing things at the same time)\n\nImagine a web server that receives 10,000 requests per second. Most older languages struggle to handle thousands of simultaneous connections. Go was designed from the ground up to do many things at once using \"Goroutines\" — ultra-lightweight threads that allow a Go server to handle millions of connections easily.\n\n### Statically Typed\n\nPython is **Dynamically Typed**. A variable can be a number, and then later become text.\n```python\n# Python\nx = 10\nx = \"Hello\"\n```\n\nGo is **Statically Typed**. You must declare what type of data a variable holds, and it can *never* change. This catches thousands of bugs before the code ever runs.\n```go\n// Go\nvar x int = 10\n// x = \"Hello\" // This will cause the compiler to crash!\n```",
            "instructions": "## Task: Static vs Dynamic\nSet the variable `go_is_static` to True or False.",
            "starterCode": "go_is_static = ___\nprint(f\"Is Go statically typed? {go_is_static}\")",
            "solution": "go_is_static = True\nprint(f\"Is Go statically typed? {go_is_static}\")",
            "hint": "Go requires types to be declared and fixed.",
            "rubric": "Sets go_is_static to True."
        }
    },
    "systems_programming.json": {
        "course": "Rust Basics",
        "lesson": {
            "title": "Safety First",
            "theory": "## The Holy Grail of Programming\n\nFor 40 years, software engineering has had a fundamental trade-off:\n\n1. Use C/C++: Blazingly fast, but developers constantly make manual memory mistakes that cause crashes and 70% of the world's security vulnerabilities (hackers exploit memory bugs).\n2. Use Java/Python: Safe (has a Garbage Collector to manage memory), but slow and uses a lot of RAM.\n\n**Rust** broke the trade-off. It is just as fast as C++, but it is mathematically impossible to write an unsafe memory bug.\n\n### The Borrow Checker\n\nRust achieves this using a concept called **Ownership and the Borrow Checker**. \n\nInstead of a garbage collector running in the background, the Rust Compiler analyzes your code *before it runs*. It tracks exactly who \"owns\" every piece of memory. If your code tries to access memory that has been deleted, or tries to change memory while someone else is reading it, the Compiler simply refuses to compile your code.\n\nIt forces you to write safe code.\n\n### The Impact\n\nRust is so revolutionary that it is the first language in history (other than C) to be officially added to the Linux Operating System kernel. It is beloved by developers for its incredible speed, safety, and modern tooling.",
            "instructions": "## Task: The Borrow Checker\nWhat is the name of the Rust feature that guarantees memory safety at compile time?",
            "starterCode": "feature_name = \"___\"\nprint(f\"Rust guarantees safety using the {feature_name}\")",
            "solution": "feature_name = \"Borrow Checker\"\nprint(f\"Rust guarantees safety using the {feature_name}\")",
            "hint": "It checks how variables borrow memory.",
            "rubric": "Mentions Borrow Checker."
        }
    }
}

for filename, update_data in new_lessons.items():
    filepath = os.path.join('curriculum', 'tracks', filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: File not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    course_name = update_data['course']
    new_lesson = update_data['lesson']
    
    if course_name in data:
        # Check if we already inserted it
        if data[course_name]['lessons'][0]['title'] != new_lesson['title']:
            data[course_name]['lessons'].insert(0, new_lesson)
            print(f"Added '{new_lesson['title']}' to {course_name} in {filename}")
        else:
            print(f"Lesson already exists in {course_name}")
    else:
        print(f"Course {course_name} not found in {filename}")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
