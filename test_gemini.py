import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the core Google API
genai.configure(api_key=api_key)

print("🔌 Asking Google for available embedding models...")
print("-" * 40)

try:
    # Loop through every model Google offers
    found = False
    for m in genai.list_models():
        if 'embedContent' in m.supported_generation_methods:
            print(f"✅ EXACT MODEL NAME TO USE: {m.name}")
            found = True
            
    if not found:
        print("⚠️ Google says your API key doesn't have access to ANY embedding models!")

except Exception as e:
    print("❌ GOOGLE API ERROR:")
    print(e)