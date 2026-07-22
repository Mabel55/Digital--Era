import os
import sys
import requests
import urllib.parse
import time

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def generate_scene_images(prompts, output_dir="scenes"):
    """
    Generates 16:9 cinematic images using Pollinations.ai (100% free, no API key needed).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    saved_files = []
    
    print(f"\n[IMAGE] Generating {len(prompts)} cinematic scene images (free via Pollinations.ai)...")
    
    for i, prompt in enumerate(prompts):
        output_file = os.path.join(output_dir, f"scene_{i:02d}.png")
        print(f" Generating image {i+1}/{len(prompts)}...")
        
        # Pollinations.ai free image generation API
        # Width x Height for 16:9 aspect ratio
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1920&height=1080&nologo=true&seed={i}"
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=60)
                if response.status_code == 200 and len(response.content) > 1000:
                    with open(output_file, 'wb') as f:
                        f.write(response.content)
                    saved_files.append(output_file)
                    break
                else:
                    print(f"  [!] Bad response for image {i+1} (status {response.status_code}). Retrying...")
            except Exception as e:
                print(f"  [!] Attempt {attempt+1} failed for image {i+1}: {e}")
            
            if attempt < max_retries - 1:
                time.sleep(3)
        
        # Small delay between requests to be polite to the API
        time.sleep(2)
                
    return saved_files

if __name__ == "__main__":
    test_prompts = [
        "A weary, 40-year-old male detective with dark circles under his eyes, a scruffy beard, wearing a rumpled grey trench coat and a loose tie, standing in a foggy, deserted town square. Cinematic moody lighting, 8k, photorealistic.",
        "A close-up of a rusted sign reading 'Oakhaven'. Heavy mist, eerie green glow from a broken street lamp. Cinematic moody lighting, 8k, photorealistic."
    ]
    files = generate_scene_images(test_prompts)
    print(f"\nGenerated {len(files)} images: {files}")
