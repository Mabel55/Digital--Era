"""
Batch 31: Adding LLM and RAG to AI Automation
"""
import json, os

NEW_COURSES_BATCH31 = {
    "LLM Automation APIs": {
        "tier": "Advanced",
        "aiRubric": "Assess LLM API integration",
        "lessons": [
            {"title": "OpenAI in Workflows", "theory": "## Automating with LLMs\\nIntegrating LLMs into automation tools allows you to process unstructured data, generate text, and make dynamic decisions within a workflow.", "instructions": "## Task: API Request Setup\\nWrite the JSON body required to send a prompt to the OpenAI Chat Completions API.", "starterCode": "payload = {\\n    'model': '___',\\n    'messages': [\\n        {'role': '___', 'content': 'You are a helpful assistant.'},\\n        {'role': 'user', 'content': 'Summarize this email.'}\\n    ]\\n}", "solution": "payload = {\\n    'model': 'gpt-4o',\\n    'messages': [\\n        {'role': 'system', 'content': 'You are a helpful assistant.'},\\n        {'role': 'user', 'content': 'Summarize this email.'}\\n    ]\\n}", "hint": "Use gpt-4o and system role.", "rubric": "Correctly constructs the JSON payload for OpenAI API."},
            {"title": "Handling Hallucinations in Flows", "theory": "## Workflow Fallbacks\\nWhen an LLM hallucinates or returns invalid JSON in an automated workflow, the workflow breaks. You must use fallback routes and structured outputs to prevent this.", "instructions": "## Task: Fallback Logic\\nCheck if the LLM output is valid JSON. If not, return a default dictionary.", "starterCode": "import json\\n\\ndef parse_llm_response(response_text):\\n    try:\\n        return json.___(response_text)\\n    except ValueError:\\n        return {'status': '___', 'message': 'Invalid output'}", "solution": "import json\\n\\ndef parse_llm_response(response_text):\\n    try:\\n        return json.loads(response_text)\\n    except ValueError:\\n        return {'status': 'error', 'message': 'Invalid output'}", "hint": "Use json.loads and an error status.", "rubric": "Properly catches exceptions and parses JSON."}
        ]
    },
    "RAG Automation Workflows": {
        "tier": "Advanced",
        "aiRubric": "Assess automated RAG knowledge",
        "lessons": [
            {"title": "Automated Document Ingestion", "theory": "## Ingestion Pipelines\\nA robust RAG system requires an automated pipeline that detects new documents (e.g., in Google Drive), chunks them, and upserts them to a Vector DB automatically.", "instructions": "## Task: Upsert Trigger\\nWrite a mock function that triggers when a new file is added and upserts it to Pinecone.", "starterCode": "def on_file_added(file_content):\\n    chunks = chunk_text(file_content)\\n    embeddings = get_embeddings(chunks)\\n    # Upsert to vector db\\n    vector_db.___(___)", "solution": "def on_file_added(file_content):\\n    chunks = chunk_text(file_content)\\n    embeddings = get_embeddings(chunks)\\n    # Upsert to vector db\\n    vector_db.upsert(embeddings)", "hint": "Use the upsert method with embeddings.", "rubric": "Uses upsert function on the embeddings."},
            {"title": "Dynamic Context Retrieval", "theory": "## Context Injection in Automation\\nWhen a user triggers an automation (like a customer support email), the workflow should automatically query the Vector DB for relevant context before sending it to the LLM.", "instructions": "## Task: Context Query\\nRetrieve the top 3 similar documents from a query embedding.", "starterCode": "def handle_support_ticket(ticket_text):\\n    query_embedding = get_embedding(ticket_text)\\n    # Retrieve top 3 results\\n    results = vector_db.___(query_embedding, top_k=___)\\n    return results", "solution": "def handle_support_ticket(ticket_text):\\n    query_embedding = get_embedding(ticket_text)\\n    # Retrieve top 3 results\\n    results = vector_db.query(query_embedding, top_k=3)\\n    return results", "hint": "Use query and top_k=3.", "rubric": "Correctly queries the DB with top_k."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'ai_automation.json')
    
    # 1. Update ai_automation.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH31.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH31.items():
            tier = course_info["tier"]
            if "AI Automation" in index_data and tier in index_data["AI Automation"]:
                if new_course_name not in index_data["AI Automation"][tier]:
                    index_data["AI Automation"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 31: Added/Appended {total} lessons to AI Automation')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
