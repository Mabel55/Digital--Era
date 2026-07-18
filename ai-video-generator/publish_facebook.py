import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Facebook Page ID and Access Token
FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")

def upload_to_facebook(video_file, description):
    """
    Uploads a video to a Facebook Page as a Reel.
    Requires FB_PAGE_ID and FB_ACCESS_TOKEN in the .env file.
    """
    print("Preparing to upload to Facebook...")
    
    if not FB_PAGE_ID or not FB_ACCESS_TOKEN:
        print("Error: FB_PAGE_ID or FB_ACCESS_TOKEN not set in .env file.")
        print("To upload to Facebook, you must create a Meta App, get Page access,")
        print("and generate a long-lived Page Access Token.")
        return False
        
    # The Facebook Graph API endpoint for publishing a video Reel
    url = f"https://graph.facebook.com/v25.0/{FB_PAGE_ID}/video_reels"
    
    try:
        # Step 1: Initialize the upload session
        init_payload = {
            "upload_phase": "start",
            "access_token": FB_ACCESS_TOKEN
        }
        print("Initializing Facebook upload session...")
        init_res = requests.post(url, data=init_payload)
        init_data = init_res.json()
        
        if "video_id" not in init_data:
            print(f"Failed to initialize Facebook upload: {init_data}")
            return False
            
        video_id = init_data["video_id"]
        
        # Step 2: Upload the video file
        upload_url = init_data.get("upload_url", f"https://rupload.facebook.com/video-upload/v25.0/{video_id}")
        headers = {
            "Authorization": f"OAuth {FB_ACCESS_TOKEN}",
            "offset": "0",
            "file_size": str(os.path.getsize(video_file)),
            "Content-Type": "application/octet-stream"
        }
        
        print("Uploading file to Facebook...")
        with open(video_file, "rb") as f:
            upload_res = requests.post(upload_url, headers=headers, data=f)
            
        if upload_res.status_code != 200:
            print(f"Failed to upload video to Facebook: {upload_res.text}")
            return False
            
        # Step 3: Publish the Reel
        publish_payload = {
            "upload_phase": "finish",
            "access_token": FB_ACCESS_TOKEN,
            "video_id": video_id,
            "description": description + "\n#reels #facts #ai",
            "video_state": "PUBLISHED"
        }
        
        print("Publishing Reel...")
        publish_res = requests.post(url, data=publish_payload)
        publish_data = publish_res.json()
        
        if "success" in publish_data and publish_data["success"]:
            print("Video successfully published to Facebook Reels!")
            return True
        else:
            print(f"Failed to publish Reel: {publish_data}")
            return False
            
    except Exception as e:
        print(f"An error occurred during Facebook upload: {e}")
        return False

if __name__ == "__main__":
    upload_to_facebook("final_output.mp4", "Test AI Video for Facebook")
