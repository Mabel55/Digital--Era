import os
import requests
from dotenv import load_dotenv

load_dotenv()

FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")

def test_fb_init():
    url = f"https://graph.facebook.com/v25.0/{FB_PAGE_ID}/video_reels"
    init_payload = {
        "upload_phase": "start",
        "access_token": FB_ACCESS_TOKEN
    }
    print("Initializing Facebook upload session...")
    init_res = requests.post(url, data=init_payload)
    init_data = init_res.json()
    print("Response from Facebook:", init_data)

if __name__ == "__main__":
    test_fb_init()
