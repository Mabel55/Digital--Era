import os
import sys
import requests
import urllib.parse

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def create_thumbnail(prompt, output_file="thumbnail.png"):
    """
    Generates a 16:9 YouTube thumbnail using Pollinations.ai (free, no API key).
    """
    print(f"\n[IMAGE] Generating YouTube thumbnail...")
    
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1280&height=720&nologo=true&seed=42"
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=60)
            if response.status_code == 200 and len(response.content) > 1000:
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                print(f"[OK] Thumbnail saved successfully to {output_file}")
                return True
            else:
                print(f"[!] Bad response (status {response.status_code}). Retrying...")
        except Exception as e:
            print(f"[!] Attempt {attempt+1} failed: {e}")
        
        if attempt < max_retries - 1:
            import time
            time.sleep(3)
    
    print("[!] Failed to generate thumbnail after all retries.")
    return False

if __name__ == "__main__":
    test_prompt = "Dark background with glowing brain illustration, bold yellow text 'YOUR BRAIN IS LYING', shocked face silhouette, neon blue and red accents"
    create_thumbnail(test_prompt)
