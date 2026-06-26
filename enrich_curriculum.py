import json
import time
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Key manually
api_key = None
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'GEMINI_API_KEY=' in line:
                api_key = line.strip().split('=', 1)[1].strip()
                break

if not api_key:
    raise ValueError("API key not found in .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.3
)

def enrich_lesson_theory(topic_title, lesson_title, old_theory):
    prompt = (
        f"You are Mabel, an expert coding instructor. The current theory for the lesson '{lesson_title}' in the topic '{topic_title}' is too brief:\n\n"
        f"CURRENT THEORY:\n{old_theory}\n\n"
        "Your task is to rewrite this theory to be highly beginner-friendly. Explain what the concepts mean in plain English using real-world analogies before showing the code. "
        "Make it 2 to 3 paragraphs long. Keep the markdown formatting and include the original code examples, just vastly enrich the text explanation. Do not add any conversational fluff like 'Sure, here is the rewritten theory'. Just output the markdown theory."
    )
    
    try:
        response = llm.invoke([("human", prompt)])
        return response.content.strip()
    except Exception as e:
        print(f"Error enriching {lesson_title}: {e}")
        return old_theory

def enrich_track(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for topic, topic_data in data.items():
        print(f"Processing Topic: {topic}")
        for lesson in topic_data.get("lessons", []):
            if "theory" in lesson and lesson["theory"]:
                if lesson.get("type") == "quiz":
                    continue
                print(f"  Enriching lesson: {lesson['title']}")
                new_theory = enrich_lesson_theory(topic, lesson['title'], lesson['theory'])
                if new_theory:
                    lesson['theory'] = new_theory
                time.sleep(3) # Safe rate limiting
                
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("All lessons enriched and saved!")

if __name__ == "__main__":
    enrich_track("curriculum/tracks/python_core.json")
