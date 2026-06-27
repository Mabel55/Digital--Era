import json
import os

track_courses = {
    "Python Core": {
        "Beginner": ["Python Basics", "Control Flow", "Functions"],
        "Intermediate": ["Data Structures", "OOP in Python", "File I/O"],
        "Advanced": ["Decorators", "Generators", "Asyncio"]
    },
    "Frontend": {
        "Beginner": ["HTML5 Essentials", "CSS Styling", "JS Basics"],
        "Intermediate": ["React Fundamentals", "State Management", "CSS Grid & Flexbox"],
        "Advanced": ["Next.js", "Frontend Performance", "Web Accessibility"]
    },
    "Backend": {
        "Beginner": ["HTTP & APIs", "Node.js Basics", "Express Server"],
        "Intermediate": ["Database Integration", "Authentication", "RESTful Design"],
        "Advanced": ["GraphQL", "Microservices", "WebSockets"]
    },
    "SQL & Databases": {
        "Beginner": ["SQL SELECTs", "Filtering Data", "Basic Joins"],
        "Intermediate": ["Aggregations", "Subqueries", "Database Design"],
        "Advanced": ["Indexing", "Stored Procedures", "Query Optimization"]
    },
    "Data Science": {
        "Beginner": ["Pandas Intro", "Data Cleaning", "Matplotlib"],
        "Intermediate": ["Statistical Analysis", "Scikit-Learn", "Feature Engineering"],
        "Advanced": ["Time Series", "NLP Basics", "Advanced ML Models"]
    },
    "AI Engineering": {
        "Beginner": ["Intro to LLMs", "Prompt Engineering", "OpenAI API"],
        "Intermediate": ["RAG Architecture", "Vector Databases", "LangChain"],
        "Advanced": ["Fine-tuning Models", "AI Agents", "Evaluating AI Output"]
    },
    "AI Automation": {
        "Beginner": ["Zapier Basics", "Make.com Workflows", "API Connections"],
        "Intermediate": ["Automated Content", "Email Automation", "Custom Webhooks"],
        "Advanced": ["Enterprise AI Bots", "Voice AI Agents", "Multi-Agent Systems"]
    },
    "Version Control": {
        "Beginner": ["Git Basics", "Commits & Logs", "Branches"],
        "Intermediate": ["Merging & Conflicts", "Pull Requests", "GitHub Actions"],
        "Advanced": ["Rebasing", "Git Hooks", "Monorepo Management"]
    },
    "Mobile Development": {
        "Beginner": ["React Native Intro", "UI Components", "Navigation"],
        "Intermediate": ["Device APIs", "Local Storage", "Animations"],
        "Advanced": ["App Deployment", "Native Modules", "Performance Profiling"]
    },
    "Systems Programming": {
        "Beginner": ["Rust Basics", "Ownership & Borrowing", "Memory Safety"],
        "Intermediate": ["Concurrency", "File Systems", "Macros"],
        "Advanced": ["Unsafe Rust", "FFI", "Network Programming"]
    },
    "Cloud Native & Go": {
        "Beginner": ["Go Syntax", "Structs & Interfaces", "Goroutines"],
        "Intermediate": ["Go Web Servers", "Docker Containers", "Kubernetes Basics"],
        "Advanced": ["gRPC", "Service Meshes", "Cloud Operators"]
    },
    "Cloud & DevOps": {
        "Beginner": ["AWS Basics", "EC2 & S3", "Linux Fundamentals"],
        "Intermediate": ["Terraform", "CI/CD Pipelines", "Monitoring & Logging"],
        "Advanced": ["Serverless", "Security Groups", "Cost Optimization"]
    },
    "System Design & Architecture": {
        "Beginner": ["Client-Server Model", "DNS & Load Balancing", "Caching Strategies"],
        "Intermediate": ["Database Sharding", "Message Queues", "CAP Theorem"],
        "Advanced": ["Distributed Consensus", "Designing Uber", "Designing Netflix"]
    },
    "Agentic AI & MCP": {
        "Beginner": ["Agent Foundations", "Tool Calling", "MCP Intro"],
        "Intermediate": ["ReAct Prompting", "Memory Systems", "MCP Servers"],
        "Advanced": ["Swarm Architectures", "Autonomous Execution", "Evaluation"]
    },
    "Computer Vision & Deep Learning": {
        "Beginner": ["Image Processing", "OpenCV Basics", "Neural Networks Intro"],
        "Intermediate": ["PyTorch Tensors", "CNN Architecture", "Transfer Learning"],
        "Advanced": ["Object Detection", "GANs", "Vision Transformers"]
    },
    "Data Engineering & MLOps": {
        "Beginner": ["ETL Pipelines", "Data Warehouses", "Apache Airflow"],
        "Intermediate": ["Apache Spark", "Kafka Streaming", "ML Model Tracking"],
        "Advanced": ["Model Deployment", "Drift Detection", "Feature Stores"]
    },
    "C Programming": {
        "Beginner": ["C Syntax", "Pointers Basics", "Arrays & Strings"],
        "Intermediate": ["Dynamic Memory", "Structs & Unions", "File Handling"],
        "Advanced": ["Data Structures in C", "Bit Manipulation", "System Calls"]
    },
    "Data Structures & Algorithms": {
        "Beginner": ["Big O Notation", "Arrays & Strings", "Linked Lists"],
        "Intermediate": ["Stacks & Queues", "Trees & Graphs", "Sorting Algorithms"],
        "Advanced": ["Dynamic Programming", "Tries", "Graph Traversal"]
    }
}

def generate_curriculum():
    os.makedirs(os.path.join("curriculum", "tracks"), exist_ok=True)
    
    for track, levels in track_courses.items():
        track_data = {}
        for level, courses in levels.items():
            for course_name in courses:
                # Generate 5 placeholder lessons for each course
                lessons = []
                for i in range(1, 6):
                    lessons.append({
                        "title": f"{course_name} Lesson {i}",
                        "theory": f"This is placeholder theory for {course_name} Lesson {i}. This will be dynamically generated by the AI.",
                        "instructions": f"Placeholder instructions for {course_name}.",
                        "starterCode": "# Write code here",
                        "solution": "# Solution code",
                        "hint": "Placeholder hint",
                        "rubric": "Code runs successfully"
                    })
                # Add to track data (flat structure by course_name as expected by build_courses)
                track_data[course_name] = {
                    "aiRubric": f"Check logic for {course_name}",
                    "lessons": lessons
                }
                
        # Write to curriculum/tracks/track_name.json
        safe_filename = track.lower().replace(" ", "_").replace("&", "").replace("__", "_") + ".json"
        target_path = os.path.join("curriculum", "tracks", safe_filename)
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(track_data, f, indent=2)
            
    # Write curriculum/index.json
    index_curriculum = {}
    for track, levels in track_courses.items():
        index_curriculum[track] = {}
        for level, courses in levels.items():
            index_curriculum[track][level] = courses
            
    with open(os.path.join("curriculum", "index.json"), "w", encoding="utf-8") as f:
        json.dump(index_curriculum, f, indent=2)

    print(f"Successfully rebuilt all JSON files in curriculum/tracks/ and index.json")
    # Now run build_courses.py to compile them into courses.js
    os.system("python build_courses.py")

if __name__ == "__main__":
    generate_curriculum()
