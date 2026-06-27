"""
Batch 47: Expanding AI Engineering Curriculum (Open Source LLMs, Semantic Routing, Function Calling, Quantization, Graph RAG)
"""
import json, os

NEW_COURSES_BATCH47 = {
    "Open Source LLMs": {
        "tier": "Beginner",
        "aiRubric": "Assess usage of local and open source models",
        "lessons": [
            {"title": "Hugging Face Hub", "theory": "## The GitHub of AI\\nHugging Face is the central hub for open-source AI models. You can use the `transformers` library to easily download and run these models locally.", "instructions": "## Task: Load a Pipeline\\nUse the pipeline function from the transformers library to load a sentiment-analysis model.", "starterCode": "from transformers import ___\\n\\nclassifier = ___('sentiment-analysis')", "solution": "from transformers import pipeline\\n\\nclassifier = pipeline('sentiment-analysis')", "hint": "Use pipeline", "rubric": "Correctly imports and uses the pipeline function."},
            {"title": "Ollama for Local Inference", "theory": "## Running Models Locally\\nOllama allows you to run large language models (like Llama 3) locally on your own machine without relying on external APIs.", "instructions": "## Task: Ollama CLI\\nWrite the terminal command used to download and run the `llama3` model using Ollama.", "starterCode": "___ run ___", "solution": "ollama run llama3", "hint": "ollama run llama3", "rubric": "Writes 'ollama run llama3'."}
        ]
    },
    "Semantic Routing": {
        "tier": "Intermediate",
        "aiRubric": "Assess semantic routing concepts",
        "lessons": [
            {"title": "Intent Detection", "theory": "## Steering the Conversation\\nInstead of using a single giant prompt for everything, semantic routing uses embeddings to classify the user's intent (e.g., 'small talk' vs 'database query') and routes the request to a specialized prompt or tool.", "instructions": "## Task: Routing Logic\\nIf a user asks 'What's the weather?', the router should direct it to the `weather_agent`. Assign the correct route.", "starterCode": "user_input = \"What's the weather?\"\\nroute = classify_intent(user_input)\\nif route == '___':\\n    call_weather_agent()", "solution": "user_input = \"What's the weather?\"\\nroute = classify_intent(user_input)\\nif route == 'weather':\\n    call_weather_agent()", "hint": "weather", "rubric": "Checks for the 'weather' route."},
            {"title": "Fast Embedding Search", "theory": "## Router Speed\\nSemantic routers must be extremely fast. Instead of using a slow LLM to classify intent, they often embed the user's query and do a fast Cosine Similarity check against predefined intent examples.", "instructions": "## Task: Similarity Metric\\nWhich mathematical metric is commonly used to compare two text embeddings in a semantic router?", "starterCode": "metric = '___ Similarity'", "solution": "metric = 'Cosine Similarity'", "hint": "Cosine Similarity", "rubric": "Identifies Cosine Similarity."}
        ]
    },
    "Function Calling & Tools": {
        "tier": "Intermediate",
        "aiRubric": "Assess LLM tool calling",
        "lessons": [
            {"title": "Defining a Tool Schema", "theory": "## Teaching the LLM\\nTo allow an LLM to call a function, you must pass a JSON schema that describes the function's name, description, and required parameters.", "instructions": "## Task: JSON Schema\\nComplete the schema definition for a `get_current_weather` function by specifying the parameter type as 'string'.", "starterCode": "tools = [{\\n    \"type\": \"function\",\\n    \"function\": {\\n        \"name\": \"get_current_weather\",\\n        \"parameters\": {\\n            \"type\": \"object\",\\n            \"properties\": {\\n                \"location\": {\"type\": \"___\"}\\n            }\\n        }\\n    }\\n}]", "solution": "tools = [{\\n    \"type\": \"function\",\\n    \"function\": {\\n        \"name\": \"get_current_weather\",\\n        \"parameters\": {\\n            \"type\": \"object\",\\n            \"properties\": {\\n                \"location\": {\"type\": \"string\"}\\n            }\\n        }\\n    }\\n}]", "hint": "The type is string", "rubric": "Sets the type to 'string'."},
            {"title": "Handling the Response", "theory": "## Executing the Function\\nThe LLM does not execute the function itself; it returns a JSON object telling *your code* to execute the function with specific arguments.", "instructions": "## Task: Parse Arguments\\nParse the JSON string returned by the LLM into a Python dictionary using the `json` module.", "starterCode": "import json\\n\\nllm_args_string = '{\"location\": \"Paris\"}'\\nargs_dict = json.___(llm_args_string)", "solution": "import json\\n\\nllm_args_string = '{\"location\": \"Paris\"}'\\nargs_dict = json.loads(llm_args_string)", "hint": "Use json.loads()", "rubric": "Correctly uses json.loads()."}
        ]
    },
    "Model Quantization": {
        "tier": "Advanced",
        "aiRubric": "Assess LLM quantization",
        "lessons": [
            {"title": "Reducing Precision", "theory": "## Shrinking Models\\nQuantization reduces the memory footprint of an LLM by converting its weights from high-precision floats (e.g., 16-bit) to lower precision (e.g., 8-bit or 4-bit integer), allowing massive models to fit on consumer GPUs.", "instructions": "## Task: Bit Precision\\nIf you apply INT4 quantization, how many bits are used to store each weight?", "starterCode": "bits = ___", "solution": "bits = 4", "hint": "INT4 means 4 bits", "rubric": "Identifies 4 bits."},
            {"title": "GGUF Format", "theory": "## Local Formats\\nGGUF (GPT-Generated Unified Format) is a popular file format designed specifically for fast loading and saving of quantized LLMs, commonly used by `llama.cpp`.", "instructions": "## Task: Identify Format\\nWhat is the acronym of the file format optimized for loading quantized models on CPUs and Apple Silicon?", "starterCode": "format = '___'", "solution": "format = 'GGUF'", "hint": "GGUF", "rubric": "Identifies GGUF."}
        ]
    },
    "Graph RAG": {
        "tier": "Advanced",
        "aiRubric": "Assess Graph RAG architectures",
        "lessons": [
            {"title": "Knowledge Graphs", "theory": "## Entities and Relationships\\nUnlike standard RAG (which chunks text into vector embeddings), Graph RAG extracts entities (Nodes) and their relationships (Edges) to form a structured Knowledge Graph.", "instructions": "## Task: Graph Components\\nIn a Knowledge Graph representing 'Alice knows Bob', what is 'knows' considered?", "starterCode": "# Options: Node, Edge, Vector\\ncomponent = '___'", "solution": "# Options: Node, Edge, Vector\\ncomponent = 'Edge'", "hint": "It is a relationship, so it's an Edge.", "rubric": "Identifies Edge."},
            {"title": "Combining Vectors and Graphs", "theory": "## The Best of Both Worlds\\nAdvanced systems combine Semantic Search (Vector DB) with Structural Search (Graph DB). The vector search finds relevant nodes, and the graph search retrieves the connected neighborhood to provide deep context to the LLM.", "instructions": "## Task: Multi-Hop Retrieval\\nWhen answering complex questions like 'Who is the CEO of the company that acquired WhatsApp?', which RAG approach is generally better at tracing this 'multi-hop' connection?", "starterCode": "# Options: Standard RAG, Graph RAG\\nbest_approach = '___'", "solution": "# Options: Standard RAG, Graph RAG\\nbest_approach = 'Graph RAG'", "hint": "Graph RAG", "rubric": "Identifies Graph RAG."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'ai_engineering.json')
    
    # 1. Update ai_engineering.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH47.items():
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
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH47.items():
            tier = course_info["tier"]
            if "AI Engineering" in index_data and tier in index_data["AI Engineering"]:
                if new_course_name not in index_data["AI Engineering"][tier]:
                    index_data["AI Engineering"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 47: Added {total} lessons to AI Engineering track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
