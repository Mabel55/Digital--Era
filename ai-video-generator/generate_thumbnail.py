import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def create_thumbnail(prompt, output_file="thumbnail.png"):
    """
    Generates a 16:9 YouTube thumbnail using Gemini's image generation capabilities.
    """
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not set in .env file.")
        return False
        
    print(f"\n[IMAGE] Generating YouTube thumbnail from prompt: '{prompt}'...")
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    try:
        # Generate image using Imagen 3
        result = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                output_mime_type="image/png"
            )
        )
        
        # Save the generated image
        if result.generated_images:
            image_bytes = result.generated_images[0].image.image_bytes
            with open(output_file, 'wb') as f:
                f.write(image_bytes)
            print(f"[OK] Thumbnail saved successfully to {output_file}")
            return True
        else:
            print("[!] No image was generated.")
            return False
            
    except Exception as e:
        print(f"Failed to generate thumbnail: {e}")
        return False

if __name__ == "__main__":
    test_prompt = "Dark background with glowing brain illustration, bold yellow text 'YOUR BRAIN IS LYING', shocked face silhouette, neon blue and red accents"
    create_thumbnail(test_prompt)
