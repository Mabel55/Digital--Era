import os
import requests

def download_bgm(output_path="bgm.mp3"):
    """
    Generates a creepy ambient drone instead of downloading to guarantee it never fails.
    If the file already exists, skips generation.
    """
    if os.path.exists(output_path):
        print("Background music already exists.")
        return True
        
    print("Generating creepy background drone...")
    try:
        import numpy as np
        from moviepy import AudioArrayClip
        
        sr = 44100
        duration = 60 # 60 seconds is enough for a short
        t = np.linspace(0, duration, duration*sr, endpoint=False)
        
        # Very slow, low-frequency creepy drone with slight modulation
        freq1 = 55.0 + 2.0 * np.sin(2 * np.pi * 0.1 * t)
        freq2 = 54.0 + 1.5 * np.sin(2 * np.pi * 0.08 * t)
        
        drone1 = 0.2 * np.sin(2 * np.pi * freq1 * t)
        drone2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
        
        audio = drone1 + drone2
        
        # Fade in
        fade_in_len = sr * 3
        fade_in = np.linspace(0, 1, fade_in_len)
        audio[:fade_in_len] *= fade_in
        
        audio_stereo = np.column_stack((audio, audio))
        clip = AudioArrayClip(audio_stereo, fps=sr)
        clip.write_audiofile(output_path, logger=None)
        
        print("Successfully generated background music.")
        return True
    except Exception as e:
        print(f"Error generating BGM: {e}")
        return False

def generate_sfx(boom_path="boom.mp3", whoosh_path="whoosh.mp3"):
    """
    Synthesizes cinematic sound effects (Boom and Whoosh) using numpy and moviepy.
    This guarantees we always have SFX without relying on external APIs.
    """
    if os.path.exists(boom_path) and os.path.exists(whoosh_path):
        print("SFX files already exist.")
        return
        
    print("Generating cinematic sound effects...")
    try:
        import numpy as np
        from moviepy import AudioArrayClip
        
        sr = 44100
        t = np.linspace(0, 2, 2*sr, endpoint=False)
        
        # BOOM: Deep low-frequency decaying sine wave
        freq = np.linspace(80, 20, len(t))
        boom = np.sin(2 * np.pi * freq * t) * np.exp(-t * 3)
        boom_stereo = np.column_stack((boom, boom))
        boom_clip = AudioArrayClip(boom_stereo, fps=sr)
        boom_clip.write_audiofile(boom_path, logger=None)
        
        # WHOOSH: White noise with a bell-shaped volume envelope
        noise = np.random.normal(0, 1, len(t))
        whoosh = noise * np.exp(-((t - 1)**2) / 0.05) * 0.3
        whoosh_stereo = np.column_stack((whoosh, whoosh))
        whoosh_clip = AudioArrayClip(whoosh_stereo, fps=sr)
        whoosh_clip.write_audiofile(whoosh_path, logger=None)
        
        print("Successfully generated SFX.")
    except Exception as e:
        print(f"Error generating SFX: {e}")

if __name__ == "__main__":
    download_bgm()
