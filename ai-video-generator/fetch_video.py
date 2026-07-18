import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def download_videos(query: str, num_videos: int = 3, orientation: str = "portrait"):
    """
    Search Pexels for a video matching the query and download multiple clips.
    Returns a list of saved file paths.
    """
    if not PEXELS_API_KEY or PEXELS_API_KEY == "your_pexels_api_key_here":
        print("Error: PEXELS_API_KEY not set in .env file. Please get a free key from pexels.com/api")
        return []
        
    url = f"https://api.pexels.com/videos/search?query={query}&per_page={num_videos * 2}&orientation={orientation}"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching from Pexels API: {response.status_code} - {response.text}")
        return []
        
    data = response.json()
    if not data.get("videos"):
        print("No videos found for this query.")
        return []
        
    saved_files = []
    for i, video in enumerate(data["videos"]):
        if len(saved_files) >= num_videos:
            break
            
        video_files = video.get("video_files", [])
        if not video_files:
            continue
            
        # Pick the best quality file
        best_file = max(video_files, key=lambda x: x.get('width', 0) * x.get('height', 0))
        video_url = best_file["link"]
        
        output_path = f"background_{i}.mp4"
        print(f"Downloading video {len(saved_files)+1} from Pexels...")
        try:
            vid_response = requests.get(video_url, stream=True, timeout=30)
            vid_response.raise_for_status()
            
            with open(output_path, "wb") as f:
                for chunk in vid_response.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
            print(f"Saved video to {output_path}")
            saved_files.append(output_path)
        except requests.exceptions.RequestException as e:
            print(f"Failed to download video file {i}: {e}")
            
    return saved_files

if __name__ == "__main__":
    download_videos("nature", 3)
