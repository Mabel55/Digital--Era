from database import SessionLocal
import models

def seed_database():
    db = SessionLocal()
    
    # 📚 THE COMPREHENSIVE 12-TRACK CURRICULUM DATA
    seed_data = [
        {
            "title": "1. Python (Core Programming)",
            "description": "The absolute foundation. Master Python syntax, data structures, and advanced OOP.",
            "lessons": [
                {"title": "Python Syntax & Variables", "content": "Python uses indentation to define code blocks instead of brackets. Variables are created dynamically without declaring their type.", "expected_output": "Hello, World!"},
                {"title": "Data Structures", "content": "Python's core data structures include Lists (ordered, mutable), Tuples (ordered, immutable), Sets (unordered, unique), and Dictionaries (key-value pairs).", "expected_output": "[1, 2, 3]"},
                {"title": "Object-Oriented Programming (OOP)", "content": "OOP in Python involves creating Classes and Objects. It relies on four main pillars: Encapsulation, Abstraction, Inheritance, and Polymorphism.", "expected_output": "Woof!"},
                {"title": "Decorators & Generators", "content": "Decorators allow you to wrap a function to extend its behavior. Generators use the 'yield' keyword to return data one piece at a time, saving memory.", "expected_output": "1\n2\n3"}
            ]
        },
        {
            "title": "2. Git & Version Control",
            "description": "Learn how to save, branch, and collaborate on code using Git and GitHub.",
            "lessons": [
                {"title": "What is Version Control?", "content": "Version control systems like Git track changes to your codebase over time, allowing you to revert to previous states and collaborate with other developers safely."},
                {"title": "Branching and Merging", "content": "Branches allow you to work on new features without affecting the main codebase. Once a feature is complete, it is merged back into the main branch via a Pull Request."}
            ]
        },
        {
            "title": "3. HTML & CSS",
            "description": "Frontend basics for structuring and styling web pages.",
            "lessons": [
                {"title": "Semantic HTML", "content": "Semantic HTML uses tags that convey the meaning of the content, such as <header>, <article>, and <footer>, which improves SEO and accessibility."},
                {"title": "CSS Flexbox & Grid", "content": "Flexbox is designed for 1-dimensional layouts (rows or columns), while CSS Grid is designed for complex 2-dimensional layouts (rows and columns simultaneously)."}
            ]
        },
        {
            "title": "4. SQL & Relational Databases",
            "description": "Mastering PostgreSQL, table design, and complex queries.",
            "lessons": [
                {"title": "Basic CRUD Operations", "content": "CRUD stands for Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE). These are the four basic operations for interacting with a database."},
                {"title": "Table Relationships & JOINs", "content": "Relational databases connect tables using Primary Keys and Foreign Keys. An INNER JOIN combines rows from two tables based on a related column."}
            ]
        },
        {
            "title": "5. Backend Development (FastAPI & Django)",
            "description": "Building robust, scalable REST APIs using modern Python frameworks.",
            "lessons": [
                {"title": "Client-Server Architecture & REST", "content": "REST APIs operate on a stateless client-server architecture using standard HTTP methods like GET, POST, PUT, and DELETE to transfer JSON data."},
                {"title": "FastAPI & Pydantic", "content": "FastAPI is a modern web framework that uses Pydantic for strict data validation and automatically generates Swagger UI documentation for your endpoints."},
                {"title": "Authentication (JWT)", "content": "JSON Web Tokens (JWT) are used to securely transmit information between parties as a JSON object, commonly used to verify logged-in users in APIs."}
            ]
        },
        {
            "title": "6. Data Science in Python",
            "description": "Manipulating and analyzing massive datasets using Pandas and NumPy.",
            "lessons": [
                {"title": "NumPy Basics", "content": "NumPy introduces N-dimensional arrays in Python, allowing for incredibly fast mathematical and logical operations on massive datasets."},
                {"title": "Exploratory Data Analysis (EDA) with Pandas", "content": "Pandas provides DataFrames, allowing you to load CSVs, clean missing values, and extract statistical insights from raw data before machine learning begins."}
            ]
        },
        {
            "title": "7. Machine Learning",
            "description": "Training predictive models using supervised and unsupervised learning.",
            "lessons": [
                {"title": "Supervised vs Unsupervised Learning", "content": "Supervised learning uses labeled data to train models (like predicting house prices). Unsupervised learning finds hidden patterns in unlabeled data (like clustering similar users)."},
                {"title": "Model Evaluation Metrics", "content": "Accuracy, Precision, Recall, and F1-Score are critical metrics to determine if a machine learning model is actually making good predictions on unseen test data."}
            ]
        },
        {
            "title": "8. AI Prompt Engineering",
            "description": "Mastering communication with Large Language Models.",
            "lessons": [
                {"title": "Few-Shot Prompting", "content": "Few-shot prompting involves giving the LLM a few examples of the desired input and output format within the prompt itself to guide its behavior and accuracy."},
                {"title": "System Prompts & Guardrails", "content": "System prompts define the overarching persona and rules for the AI. Guardrails are strict constraints placed in the prompt to prevent the AI from generating harmful or off-topic content."}
            ]
        },
        {
            "title": "9. LangChain",
            "description": "Orchestrating AI logic and chaining multiple LLM tools together.",
            "lessons": [
                {"title": "What is LangChain?", "content": "LangChain is a framework for developing applications powered by language models. It allows you to connect an LLM to other sources of computation or knowledge."},
                {"title": "Memory & Agents", "content": "By default, APIs are stateless. LangChain Memory allows an LLM to remember past chat history. Agents allow the LLM to decide which tools (like a calculator or search engine) to use to solve a problem."}
            ]
        },
        {
            "title": "10. RAG (Retrieval-Augmented Generation)",
            "description": "Connecting custom databases to AI to eliminate hallucinations.",
            "lessons": [
                {"title": "Vector Embeddings & FAISS", "content": "Text is converted into numerical vectors. Vector databases like FAISS store these numbers and use cosine similarity to instantly find paragraphs that match the semantic meaning of a user's question."},
                {"title": "The RAG Pipeline", "content": "In RAG, a user asks a question. The backend searches the vector database for relevant documents, then sends those documents to the LLM with the instruction: 'Answer the question using only this text.'"}
            ]
        },
        {
            "title": "11. AI Automation",
            "description": "Building trigger-based workflows and event-driven autonomous data pipelines.",
            "lessons": [
                {"title": "Trigger-Based Workflows", "content": "AI Automation relies on defined triggers—like an incoming webhook, email, or database update—to execute automated steps without requiring direct human interaction."},
                {"title": "Event-Driven AI Architectures", "content": "Event-driven systems process data in real-time as events occur, allowing autonomous LangChain handlers to react instantly to changing live data streams."}
            ]
        },
        {
            "title": "12. AI Engineering",
            "description": "Deep learning architectures, Transformers, and MLOps production systems.",
            "lessons": [
                {"title": "Deep Learning & Transformers", "content": "Transformers utilize self-attention mechanisms to process sequence data in parallel, serving as the foundational core architecture for modern Large Language Models (LLMs)."},
                {"title": "MLOps & CI/CD for ML", "content": "Machine Learning Operations (MLOps) combines data engineering, machine learning, and DevOps to automate the continuous training, deployment, and monitoring of AI models in production."}
            ]
        }
    ]

    print("🌱 Starting database seeding process...")

    try:
        # Loop through our complete list and add everything to the database
        for course_data in seed_data:
            
            # 1. Create the Course
            new_course = models.Course(name=course_data["title"], description=course_data["description"])
            db.add(new_course)
            db.commit()
            db.refresh(new_course)
            print(f"✅ Created Course: {new_course.name}")

            # 2. Add all lessons attached to this exact course
            for lesson_data in course_data["lessons"]:
                new_lesson = models.Lesson(
                    title=lesson_data["title"], 
                    content=lesson_data["content"], 
                    expected_output=lesson_data.get("expected_output", "Print the expected output for this lesson."),
                    course_id=new_course.id
                )
                db.add(new_lesson)
            
            db.commit()
            print(f"   ↳ Added {len(course_data['lessons'])} lessons.")

        print("🎉 Database successfully seeded with ALL 12 courses and lessons!")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()