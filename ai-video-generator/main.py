import os
import sys
import asyncio

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from generate_audio import create_voiceover
from fetch_video import download_videos
from fetch_music import download_bgm, generate_sfx
from editor import make_video
from generate_content import generate_script_and_topic
from publish_youtube import upload_to_youtube
from publish_facebook import upload_to_facebook
from generate_thumbnail import create_thumbnail

async def main():
    print("=== AI Viral Video Generator ===")
    
    # 1. Generate script, topic, and YouTube metadata with AI
    script, topic, yt_title, yt_description, yt_tags, yt_category_id, thumb_prompt = generate_script_and_topic()
    if not script or not topic:
        print("Failed to generate content via AI. Falling back to default.")
        topic = "nature"
        script = "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over three thousand years old and still perfectly edible!"
        yt_title = "This Fact Will Blow Your Mind 🤯"
        yt_description = "You won't believe this... #shorts #facts #mindblown"
        yt_tags = ["shorts", "facts", "ai", "viral", "mind blown"]
        yt_category_id = "22"
        thumb_prompt = "A glowing pot of honey inside an ancient Egyptian tomb, dramatic lighting, bold text 'NEVER SPOILS'"
    else:
        print(f"\n[AI] Topic chosen: {topic}")
        print(f"[AI] Script generated:\n{script}\n")
        print(f"[AI] YouTube Title: {yt_title}")
        print(f"[AI] YouTube Tags: {yt_tags}")
        print(f"[AI] YouTube Category ID: {yt_category_id}")
        print(f"[AI] Thumbnail Prompt: {thumb_prompt}")
        
    # File paths
    audio_file = "voiceover.mp3"
    subtitle_file = "subtitles.srt"
    final_output = "final_output.mp4"
    thumbnail_file = "thumbnail.png"
    
    # Clean up previous files if they exist
    for f in [audio_file, subtitle_file, final_output, thumbnail_file]:
        if os.path.exists(f):
            os.remove(f)
            
    # Clean old background files
    for f in os.listdir("."):
        if f.startswith("background_") and f.endswith(".mp4"):
            os.remove(f)
            
    # 2. Generate Audio and Subtitles
    print("\n[1/4] Generating AI voiceover and subtitles...")
    # Using AndrewNeural — warm, authoritative voice that performs well for viral content
    await create_voiceover(script, "en-US-AndrewNeural", audio_file, subtitle_file)
    
    # 3. Download Background Videos
    print(f"\n[2/4] Fetching dynamic background videos for topic: {topic}...")
    video_files = download_videos(topic, num_videos=8, orientation="portrait")
    
    if not video_files:
        print("Failed to get background videos. Please check your PEXELS_API_KEY in .env")
        return
        
    # 4. Fetch background music & SFX
    print("\n[3/4] Fetching background music & SFX...")
    download_bgm()
    generate_sfx()
    
    # 5. Stitch everything together
    print("\n[4/5] Editing video...")
    make_video(video_files, audio_file, subtitle_file, final_output)
    
    # 6. Generate Thumbnail
    print("\n[5/5] Generating thumbnail...")
    if thumb_prompt:
        create_thumbnail(thumb_prompt, thumbnail_file)
    else:
        print("Skipping thumbnail generation (no prompt).")
    
    print("\n=== Done! ===")
    print(f"Your video is ready at: {os.path.abspath(final_output)}")
    
    # 7. Publish
    print("\n[Publishing]...")
    upload_to_youtube(
        final_output,
        yt_title,
        yt_description,
        category_id=yt_category_id,
        keywords=yt_tags,
        privacy="public",
        thumbnail_file=thumbnail_file
    )
    
    # 8. Upload to Facebook Reels
    print(f"\n[7/8] Preparing Facebook upload...")
    upload_to_facebook(final_output, f"{yt_title}\n\n{yt_description}")
    
    
    print("\n=== All tasks completed successfully! ===")
    
    # Optional clean up of temp files
    # os.remove(audio_file)
    # os.remove(subtitle_file)
    # os.remove(video_file)

if __name__ == "__main__":
    asyncio.run(main())
