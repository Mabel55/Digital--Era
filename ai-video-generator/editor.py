import os
import shutil
import subprocess
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip, ImageClip, CompositeVideoClip
from moviepy import vfx, afx
import imageio_ffmpeg
import tempfile

def make_video(image_paths, audio_path, vtt_path, output_path):
    print("Loading images and audio...")
    from moviepy import concatenate_videoclips
    
    audio = AudioFileClip(audio_path)
    
    if not image_paths:
        print("No image clips provided.")
        return
        
    duration_per_image = audio.duration / len(image_paths)
    
    clips = []
    for img_path in image_paths:
        if not os.path.exists(img_path):
            continue
            
        # Create image clip with duration
        img_clip = ImageClip(img_path, duration=duration_per_image)
        
        # Resize slightly larger for zoom headroom, then crop to 1920x1080
        img_clip = img_clip.resized((2112, 1188))  # ~10% larger than 1920x1080
        
        # Apply Ken Burns Zoom Effect by cropping into the oversized image over time
        def make_zoom(clip, dur):
            def zoom_effect(get_frame, t):
                frame = get_frame(t)
                h, w = frame.shape[:2]
                # Zoom from full frame to center crop over time
                progress = t / dur
                crop_w = int(1920 + (w - 1920) * (1 - progress))
                crop_h = int(1080 + (h - 1080) * (1 - progress))
                x1 = (w - crop_w) // 2
                y1 = (h - crop_h) // 2
                cropped = frame[y1:y1+crop_h, x1:x1+crop_w]
                # Resize back to 1920x1080
                from PIL import Image
                import numpy as np
                img = Image.fromarray(cropped)
                img = img.resize((1920, 1080), Image.LANCZOS)
                return np.array(img)
            return clip.transform(zoom_effect)
        
        comp = make_zoom(img_clip, duration_per_image)
        clips.append(comp)
        
    if not clips:
        print("No valid image clips found.")
        return
        
    video = concatenate_videoclips(clips, method="compose")
    video = video.subclipped(0, audio.duration)
    
    # Handle SFX
    # Boom and whoosh sounds removed per user request for a cleaner narration feel
    sfx_clips = []
                
    # Handle Background Music
    bgm_path = "bgm.ogg"
    if not os.path.exists(bgm_path):
        bgm_path = "bgm.mp3"
        
    if os.path.exists(bgm_path):
        bgm = AudioFileClip(bgm_path)
        if bgm.duration < audio.duration:
            bgm = bgm.with_effects([afx.AudioLoop(duration=audio.duration)])
        else:
            bgm = bgm.subclipped(0, audio.duration)
            
        if audio.duration > 10:
            silence_start = audio.duration - 5.0
            bgm = bgm.subclipped(0, silence_start)
            
        bgm = bgm.with_volume_scaled(0.1)
        sfx_clips.append(bgm)
        
    final_audio = CompositeAudioClip([audio] + sfx_clips)
    video = video.with_audio(final_audio)
    
    temp_output = "temp_no_subs.mp4"
    print("Writing temp video...")
    # Lower fps for image slideshows is fine (24 fps is cinematic)
    video.write_videofile(temp_output, fps=24, codec="libx264", audio_codec="aac")
    
    for c in clips:
        c.close()
    video.close()
    audio.close()
    
    srt_abs = os.path.abspath(vtt_path)
    if not os.path.exists(srt_abs) or os.path.getsize(srt_abs) == 0:
        print("No subtitles found. Skipping subtitle burn.")
        os.replace(temp_output, output_path)
        return
    
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    print("Burning subtitles with FFmpeg...")
    
    temp_srt = os.path.join(tempfile.gettempdir(), "temp_subs.srt")
    shutil.copy2(srt_abs, temp_srt)
    vtt_escaped = temp_srt.replace('\\', '/').replace(':', '\\:')
    
    # Cinematic Style Subtitles: Smaller, bottom-center, less intrusive than Shorts
    style = "FontName=Arial,FontSize=24,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H80000000,BorderStyle=1,Outline=2,Shadow=1,Alignment=2,MarginV=20"
    
    cmd = [
        ffmpeg_exe,
        "-y",
        "-i", temp_output,
        "-vf", f"subtitles='{vtt_escaped}':force_style='{style}'",
        "-c:a", "copy",
        output_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\nFinal video saved successfully to {output_path}")
    except Exception as e:
        print(f"Failed to burn subtitles, using video without subs. Error: {e}")
        os.replace(temp_output, output_path)
        
    if os.path.exists(temp_output):
        os.remove(temp_output)
    if os.path.exists(temp_srt):
        os.remove(temp_srt)

if __name__ == "__main__":
    pass
