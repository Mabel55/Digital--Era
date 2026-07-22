import requests
import urllib.parse

prompt = "A foggy, deserted town square at night, cinematic moody lighting, 8k, photorealistic"
encoded = urllib.parse.quote(prompt)
url = f"https://image.pollinations.ai/prompt/{encoded}?width=1920&height=1080&nologo=true&seed=1"

print("Testing Pollinations.ai...")
response = requests.get(url, timeout=60)
print(f"Status: {response.status_code}, Size: {len(response.content)} bytes")
if response.status_code == 200 and len(response.content) > 1000:
    with open("test_image.png", "wb") as f:
        f.write(response.content)
    print("SUCCESS! Image saved to test_image.png")
else:
    print("FAILED")
