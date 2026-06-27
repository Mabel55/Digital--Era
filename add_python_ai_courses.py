import json
import os

PYTHON_CORE_COURSES = {
    "Advanced Python Concurrency": {
        "title": "Advanced Python Concurrency",
        "lessons": [
            {
                "title": "Asyncio in Depth",
                "theory": "## Asyncio\\nLearn how the event loop works and how to write efficient asynchronous code in Python.",
                "instructions": "## Task: Create a Task\\n1. Create an asyncio task for the `fetch_data` coroutine.",
                "starterCode": "import asyncio\\n\\nasync def fetch_data():\\n    await asyncio.sleep(1)\\n    return 'Data'\\n\\n# Create task here\\ntask = ___",
                "solution": "import asyncio\\n\\nasync def fetch_data():\\n    await asyncio.sleep(1)\\n    return 'Data'\\n\\ntask = asyncio.create_task(fetch_data())",
                "hint": "Use asyncio.create_task",
                "rubric": "Task created."
            },
            {
                "title": "Multiprocessing Pools",
                "theory": "## Multiprocessing\\nBypass the GIL using the `multiprocessing` module for CPU-bound tasks.",
                "instructions": "## Task: Create a Pool\\n1. Create a Multiprocessing Pool with 4 workers.",
                "starterCode": "from multiprocessing import Pool\\n\\npool = ___",
                "solution": "from multiprocessing import Pool\\n\\npool = Pool(processes=4)",
                "hint": "Pool(processes=4)",
                "rubric": "Pool created."
            }
        ]
    },
    "Python Design Patterns": {
        "title": "Python Design Patterns",
        "lessons": [
            {
                "title": "The Singleton Pattern",
                "theory": "## Singleton\\nEnsure a class has only one instance and provide a global point of access to it.",
                "instructions": "## Task: Implement Singleton\\n1. Implement the `__new__` method to return the existing instance if it exists.",
                "starterCode": "class Singleton:\\n    _instance = None\\n    def __new__(cls):\\n        ___",
                "solution": "class Singleton:\\n    _instance = None\\n    def __new__(cls):\\n        if cls._instance is None:\\n            cls._instance = super(Singleton, cls).__new__(cls)\\n        return cls._instance",
                "hint": "Check if cls._instance is None",
                "rubric": "Singleton implemented."
            },
            {
                "title": "The Factory Pattern",
                "theory": "## Factory\\nDefine an interface for creating an object, but let subclasses decide which class to instantiate.",
                "instructions": "## Task: Create a Factory\\n1. Create a `ShapeFactory` that returns a `Circle` or `Square`.",
                "starterCode": "class ShapeFactory:\\n    @staticmethod\\n    def get_shape(shape_type):\\n        ___",
                "solution": "class ShapeFactory:\\n    @staticmethod\\n    def get_shape(shape_type):\\n        if shape_type == 'CIRCLE':\\n            return Circle()\\n        elif shape_type == 'SQUARE':\\n            return Square()\\n        return None",
                "hint": "Return Circle() or Square() based on string matching",
                "rubric": "Factory implemented."
            }
        ]
    }
}

AI_ENGINEERING_COURSES = {
    "RAG Systems In Depth": {
        "title": "RAG Systems In Depth",
        "lessons": [
            {
                "title": "Vector Embeddings Pipeline",
                "theory": "## Embeddings\\nUnderstand how to encode text into dense vectors for retrieval.",
                "instructions": "## Task: Initialize Embedding Model\\n1. Initialize `SentenceTransformer` with 'all-MiniLM-L6-v2'.",
                "starterCode": "from sentence_transformers import SentenceTransformer\\n\\nmodel = ___",
                "solution": "from sentence_transformers import SentenceTransformer\\n\\nmodel = SentenceTransformer('all-MiniLM-L6-v2')",
                "hint": "SentenceTransformer('all-MiniLM-L6-v2')",
                "rubric": "Model initialized."
            },
            {
                "title": "Vector Databases Integration",
                "theory": "## Vector DBs\\nStore and query embeddings efficiently.",
                "instructions": "## Task: Connect to ChromaDB\\n1. Create a PersistentClient in ChromaDB.",
                "starterCode": "import chromadb\\n\\nclient = ___",
                "solution": "import chromadb\\n\\nclient = chromadb.PersistentClient(path='./chroma_db')",
                "hint": "chromadb.PersistentClient",
                "rubric": "Chroma connected."
            }
        ]
    },
    "LLM Fine-Tuning": {
        "title": "LLM Fine-Tuning",
        "lessons": [
            {
                "title": "LoRA and QLoRA",
                "theory": "## Parameter-Efficient Fine-Tuning\\nLearn how LoRA reduces the number of trainable parameters.",
                "instructions": "## Task: Configure LoRA\\n1. Set up a LoraConfig with r=8.",
                "starterCode": "from peft import LoraConfig\\n\\nconfig = ___",
                "solution": "from peft import LoraConfig\\n\\nconfig = LoraConfig(r=8, lora_alpha=16, target_modules=['q_proj', 'v_proj'], lora_dropout=0.05, bias='none', task_type='CAUSAL_LM')",
                "hint": "LoraConfig(r=8, ...)",
                "rubric": "LoRA configured."
            },
            {
                "title": "Supervised Fine Tuning (SFT)",
                "theory": "## SFTTrainer\\nUse the TRL library to fine-tune language models.",
                "instructions": "## Task: Initialize SFTTrainer\\n1. Set up the trainer object.",
                "starterCode": "from trl import SFTTrainer\\n\\ntrainer = ___",
                "solution": "from trl import SFTTrainer\\n\\ntrainer = SFTTrainer(model=model, train_dataset=dataset, dataset_text_field='text', max_seq_length=512)",
                "hint": "SFTTrainer(model=model, ...)",
                "rubric": "Trainer initialized."
            }
        ]
    }
}

def process():
    base_dir = "curriculum/tracks/"
    
    # Python Core
    py_path = os.path.join(base_dir, "python_core.json")
    with open(py_path, "r", encoding="utf-8") as f:
        py_data = json.load(f)
        
    for course_id, course_data in PYTHON_CORE_COURSES.items():
        if course_id not in py_data:
            py_data[course_id] = course_data
            
    with open(py_path, "w", encoding="utf-8") as f:
        json.dump(py_data, f, indent=2, ensure_ascii=False)
        
    # AI Engineering
    ai_path = os.path.join(base_dir, "ai_engineering.json")
    with open(ai_path, "r", encoding="utf-8") as f:
        ai_data = json.load(f)
        
    for course_id, course_data in AI_ENGINEERING_COURSES.items():
        if course_id not in ai_data:
            ai_data[course_id] = course_data
            
    with open(ai_path, "w", encoding="utf-8") as f:
        json.dump(ai_data, f, indent=2, ensure_ascii=False)

    print("Added courses to python_core.json and ai_engineering.json")

if __name__ == '__main__':
    process()
