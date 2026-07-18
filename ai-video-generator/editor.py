import os
import shutil
import subprocess
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip
from moviepy import vfx, afx
import imageio_ffmpeg
import tempfile

def make_video(video_paths, audio_path, vtt_path, output_path):
    print("Loading videos and audio...")
    from moviepy import concatenate_videoclips
    
    audio = AudioFileClip(audio_path)
    
    # Process all video clips
    clips = []
    target_ratio = 9 / 16
    
    for vp in video_paths:
        if not os.path.exists(vp):
            continue
        v = VideoFileClip(vp)
        current_ratio = v.w / v.h
        
        if current_ratio > target_ratio:
            new_w = int(v.h * target_ratio)
            v = v.cropped(x_center=v.w/2, y_center=v.h/2, width=new_w, height=v.h)
        else:
            new_h = int(v.w / target_ratio)
            v = v.cropped(x_center=v.w/2, y_center=v.h/2, width=v.w, height=new_h)
            
        v = v.resized((1080, 1920))
        clips.append(v)
        
    if not clips:
        print("No valid video clips found.")
        return
        
    # We want to cycle through clips, changing every 2.0 seconds for faster pacing
    clip_duration = 2.0
    num_clips_needed = int(audio.duration / clip_duration) + 1
    
    final_clips = []
    for i in range(num_clips_needed):
        source_clip = clips[i % len(clips)]
        # We need a 4-second subclip. If the source is shorter, we loop it.
        if source_clip.duration < clip_duration:
            segment = source_clip.with_effects([vfx.Loop(duration=clip_duration)])
        else:
            # We take a random or sequential 4s chunk. Let's just take the first 4s.
            segment = source_clip.subclipped(0, clip_duration)
        final_clips.append(segment)
        
    video = concatenate_videoclips(final_clips, method="compose")
    video = video.subclipped(0, audio.duration)
    
    # Handle SFX
    boom_path = "boom.mp3"
    whoosh_path = "whoosh.mp3"
    
    sfx_clips = []
    if os.path.exists(boom_path):
        boom = AudioFileClip(boom_path).with_volume_scaled(0.5)
        # Boom at the very beginning
        sfx_clips.append(boom)
        
    if os.path.exists(whoosh_path):
        whoosh = AudioFileClip(whoosh_path).with_volume_scaled(0.3)
        # Whoosh at every 4-second transition
        for i in range(1, num_clips_needed):
            transition_time = i * clip_duration
            if transition_time < audio.duration:
                sfx_clips.append(whoosh.with_start(transition_time))
                
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
            
        # Dramatic Silence: cut the BGM 5 seconds before the end
        if audio.duration > 10:
            silence_start = audio.duration - 5.0
            bgm = bgm.subclipped(0, silence_start)
            
        bgm = bgm.with_volume_scaled(0.1)
        sfx_clips.append(bgm)
        
    # Mix voiceover, SFX, and BGM
    final_audio = CompositeAudioClip([audio] + sfx_clips)
    video = video.with_audio(final_audio)
    
    temp_output = "temp_no_subs.mp4"
    print("Writing temp video...")
    video.write_videofile(temp_output, fps=30, codec="libx264", audio_codec="aac")
    
    # Close clips to free memory
    for c in clips:
        c.close()
    video.close()
    audio.close()
    
    # Check if subtitle file exists and has content
    srt_abs = os.path.abspath(vtt_path)
    if not os.path.exists(srt_abs) or os.path.getsize(srt_abs) == 0:
        print("No subtitles found or subtitle file is empty. Skipping subtitle burn.")
        os.replace(temp_output, output_path)
        return
    
    # Burn subtitles using the ffmpeg binary included with moviepy
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    print("Burning subtitles with FFmpeg...")
    # Copy subtitle file to a simple temp path to avoid FFmpeg issues with spaces in paths
    temp_srt = os.path.join(tempfile.gettempdir(), "temp_subs.srt")
    shutil.copy2(srt_abs, temp_srt)
    
    # Escape the temp path for FFmpeg subtitle filter
    vtt_escaped = temp_srt.replace('\\', '/').replace(':', '\\:')
    
    # Viral TikTok/Shorts style: large, bold, centered, high-contrast yellow with thick black outline
    style = "FontName=Arial,FontSize=44,Bold=1,PrimaryColour=&H0000FFFF,OutlineColour=&H00000000,BackColour=&H00000000,BorderStyle=1,Outline=4,Shadow=1,Alignment=10,MarginV=0"
    
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
        
    # Clean up temp files
    if os.path.exists(temp_output):
        os.remove(temp_output)
    if os.path.exists(temp_srt):
        os.remove(temp_srt)

if __name__ == "__main__":
    pass
