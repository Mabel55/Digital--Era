import json
import os

NEW_COURSES = {
    "Python Core": {
        "Advanced": [
            "Advanced Python Concurrency",
            "Python Design Patterns",
            "Python Testing Frameworks",
            "Python Security Practices"
        ]
    },
    "AI Engineering": {
        "Advanced": [
            "RAG Systems In Depth",
            "LLM Fine-Tuning",
            "AI Ethics and Safety",
            "Advanced Autonomous Agents"
        ]
    }
}

NEW_COURSE_CONTENT = {
    "Python Core": {
        "Python Testing Frameworks": {
            "aiRubric": "Assess testing concepts",
            "lessons": [
                {
                    "title": "Pytest Basics",
                    "theory": "## Pytest\nPytest is a popular testing framework that makes it easy to write small tests.",
                    "instructions": "## Task: Write a test\nWrite a test for the `add` function.",
                    "starterCode": "def add(a, b):\n    return a + b\n\ndef test_add():\n    assert add(2, 3) == ___",
                    "solution": "def add(a, b):\n    return a + b\n\ndef test_add():\n    assert add(2, 3) == 5",
                    "hint": "5",
                    "rubric": "Test is correct."
                }
            ]
        },
        "Python Security Practices": {
            "aiRubric": "Assess security practices",
            "lessons": [
                {
                    "title": "SQL Injection Prevention",
                    "theory": "## Parameterized Queries\nAlways use parameterized queries instead of string concatenation to prevent SQL injection.",
                    "instructions": "## Task: Secure the query\nFix the query to use parameterized inputs.",
                    "starterCode": "username = 'admin'\nquery = f\"SELECT * FROM users WHERE username = '{username}'\" # INSECURE",
                    "solution": "username = 'admin'\nquery = \"SELECT * FROM users WHERE username = ?\" # SECURE",
                    "hint": "Use '?' for parameters.",
                    "rubric": "Query uses parameters."
                }
            ]
        }
    },
    "AI Engineering": {
        "AI Ethics and Safety": {
            "aiRubric": "Assess AI ethics",
            "lessons": [
                {
                    "title": "Bias Detection",
                    "theory": "## Model Bias\nAI models can reflect biases in their training data. We must actively test for and mitigate these biases.",
                    "instructions": "## Task: Detect Bias\nIdentify if the output exhibits gender bias.",
                    "starterCode": "output = 'The doctor told the nurse she should...'\nbias_detected = ___",
                    "solution": "output = 'The doctor told the nurse she should...'\nbias_detected = True",
                    "hint": "True",
                    "rubric": "Bias correctly identified."
                }
            ]
        },
        "Advanced Autonomous Agents": {
            "aiRubric": "Assess advanced agents",
            "lessons": [
                {
                    "title": "Multi-Agent Collaboration",
                    "theory": "## Agent Swarms\nMultiple specialized agents can collaborate to solve complex problems better than a single general agent.",
                    "instructions": "## Task: Create a Swarm\nInstantiate two agents and pass a message between them.",
                    "starterCode": "agent1 = Agent('Researcher')\nagent2 = Agent('Writer')\n# Message from agent1 to agent2\nmsg = agent1.send(___, 'Here is the research')",
                    "solution": "agent1 = Agent('Researcher')\nagent2 = Agent('Writer')\n# Message from agent1 to agent2\nmsg = agent1.send(agent2, 'Here is the research')",
                    "hint": "Send to agent2.",
                    "rubric": "Message sent correctly."
                }
            ]
        }
    }
}

def add_new_courses():
    # 1. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)
        
    for track, tiers in NEW_COURSES.items():
        if track in index_data:
            for tier, courses in tiers.items():
                if tier in index_data[track]:
                    for course in courses:
                        if course not in index_data[track][tier]:
                            index_data[track][tier].append(course)
                            
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
        
    print("Updated index.json")

    # 2. Update track files
    tracks = {
        "Python Core": os.path.join("curriculum", "tracks", "python_core.json"),
        "AI Engineering": os.path.join("curriculum", "tracks", "ai_engineering.json")
    }
    
    for track_name, track_path in tracks.items():
        if os.path.exists(track_path):
            with open(track_path, "r", encoding="utf-8") as f:
                track_data = json.load(f)
                
            for course_name, course_content in NEW_COURSE_CONTENT[track_name].items():
                if course_name not in track_data:
                    track_data[course_name] = course_content
                    print(f"Added course payload for {course_name} in {track_name}")
                    
            with open(track_path, "w", encoding="utf-8") as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)

    # 3. Rebuild courses.js
    os.system("python build_courses.py")

if __name__ == '__main__':
    add_new_courses()
