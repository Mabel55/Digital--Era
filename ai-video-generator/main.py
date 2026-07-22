import os
import sys
import asyncio
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from generate_audio import create_voiceover
from generate_visuals import generate_scene_images
from fetch_music import download_bgm, generate_sfx
from editor import make_video
from generate_content import generate_script_and_topic
from publish_youtube import upload_to_youtube
from publish_facebook import upload_to_facebook
from generate_thumbnail import create_thumbnail
import state_manager

async def main():
    state = state_manager.load_state()
    print(f"=== AI Movie-Like Series Generator: {state['series_title']} ===")
    print(f"Generating Episode {state['current_episode']}...")
    
    # 1. Generate episodic script, image prompts, and metadata
    content = generate_script_and_topic()
    if not content:
        print("Failed to generate content via AI.")
        return
        
    script = content["script"]
    image_prompts = content["image_prompts"]
    yt_title = content["youtube_title"]
    yt_description = content["youtube_description"]
    yt_tags = content["youtube_tags"]
    thumb_prompt = content["thumbnail_prompt"]
    
    print(f"\n[AI] YouTube Title: {yt_title}")
    
    # File paths
    audio_file = "voiceover.mp3"
    subtitle_file = "subtitles.srt"
    final_output = "final_output.mp4"
    thumbnail_file = "thumbnail.png"
    scenes_dir = "scenes"
    
    # Clean up previous files if they exist
    for f in [audio_file, subtitle_file, final_output, thumbnail_file]:
        if os.path.exists(f):
            os.remove(f)
            
    if os.path.exists(scenes_dir):
        shutil.rmtree(scenes_dir)
            
    # 2. Generate Audio and Subtitles
    print("\n[1/4] Generating AI voiceover and subtitles...")
    await create_voiceover(script, "en-US-AndrewNeural", audio_file, subtitle_file)
    
    # 3. Generate Cinematic Visuals
    print(f"\n[2/4] Generating cinematic scene images using Gemini Imagen 3...")
    image_files = generate_scene_images(image_prompts, output_dir=scenes_dir)
    
    if not image_files:
        print("Failed to get cinematic images. Please check your GEMINI_API_KEY")
        return
        
    # 4. Fetch background music & SFX
    print("\n[3/4] Fetching background music & SFX...")
    download_bgm()
    generate_sfx()
    
    # 5. Stitch everything together with Ken Burns effect
    print("\n[4/5] Editing cinematic video...")
    make_video(image_files, audio_file, subtitle_file, final_output)
    
    # 6. Generate Thumbnail
    print("\n[5/5] Generating thumbnail...")
    if thumb_prompt:
        create_thumbnail(thumb_prompt, thumbnail_file)
    else:
        print("Skipping thumbnail generation (no prompt).")
    
    print("\n=== Done! ===")
    print(f"Your cinematic episode is ready at: {os.path.abspath(final_output)}")
    
    # 7. Publish
    print("\n[Publishing]...")
    try:
        # Assuming category_id 24 is Entertainment for the series
        upload_to_youtube(
            final_output,
            yt_title,
            yt_description,
            category_id="24",
            keywords=yt_tags,
            privacy="public",
            thumbnail_file=thumbnail_file
        )
    except Exception as e:
        print(f"Failed to publish to YouTube: {e}")
    
    print(f"\n[7/8] Preparing Facebook upload...")
    try:
        upload_to_facebook(final_output, f"{yt_title}\n\n{yt_description}")
    except Exception as e:
        print(f"Failed to publish to Facebook: {e}")
    
    # Only update state AFTER video is fully generated and published
    state_manager.update_state_after_episode(state, content["next_plot_summary"])
    print(f"\n[STATE] Series state updated. Next run will generate Episode {state['current_episode']}.")
    
    print("\n=== Episode generation complete! ===")

if __name__ == "__main__":
    asyncio.run(main())
