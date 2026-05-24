import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# ==========================================
# 1. SETUP & SECURE CONFIGURATION
# ==========================================
# Load environment variables from your .env file
load_dotenv()

# Securely fetch the key (Make sure your .env file has GEMINI_API_KEY=your_key_here)
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("🚨 API Key not found! Please check your .env file.")

genai.configure(api_key=API_KEY)

# Using the requested 2.5 model, configured strictly for JSON output
model = genai.GenerativeModel(
    'gemini-2.5-flash',
    generation_config={"response_mime_type": "application/json"}
)

# ==========================================
# 2. THE CURRICULUM BATCH
# ==========================================
track_name = "Backend Engineering"
modules_to_generate = [
    "Introduction to FastAPI Routing",
    "Connecting to PostgreSQL with SQLAlchemy",
    "Building a CRUD API for a Bookstore"
]

# ==========================================
# 3. THE MASTER PROMPT
# ==========================================
def generate_module(course_title: str):
    print(f"⚙️ Generating content for: {course_title}...")
    
    prompt = f"""
    You are a Senior Curriculum Developer for 'Mabel Academy', a premium tech bootcamp.
    Write the curriculum for a module titled '{course_title}' in the '{track_name}' track.

    CRITICAL RULES:
    1. Real-World Context: Frame the exercise as a real task at a tech startup.
    2. Format: 'instructions' must be rich Markdown. 'starterCode' must be Python with `___` for blanks. 'aiRubric' must be strict instructions for an automated AI grader.
    3. Output: You MUST return a single JSON object using this exact schema:
    
    {{
      "{course_title}": {{
        "instructions": "### {course_title}\\n\\nYour markdown instructions here...",
        "starterCode": "your python code \\n___ \\n code",
        "aiRubric": "Instructions for the AI on how to pass/fail the student's code."
      }}
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        print(f"❌ Error generating {course_title}: {e}")
        return None

# ==========================================
# 4. THE GENERATION ENGINE
# ==========================================
def main():
    master_manifest = {}
    
    for module in modules_to_generate:
        module_data = generate_module(module)
        if module_data:
            master_manifest.update(module_data)
            
    # Save the output directly to a JSON file!
    output_filename = "generated_courses_output.json"
    with open(output_filename, "w") as outfile:
        json.dump(master_manifest, outfile, indent=4)
        
    print(f"✅ Success! {len(master_manifest)} modules generated and saved to {output_filename}.")

if __name__ == "__main__":
    main()