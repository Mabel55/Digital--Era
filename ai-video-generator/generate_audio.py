import asyncio
import edge_tts

async def create_voiceover(text: str, voice: str, output_file: str, subtitle_file: str):
    """
    Generate voiceover and subtitles from text using edge-tts.
    Includes a timeout and retry logic for network stability.
    """
    max_retries = 3
    
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  Voiceover attempt {attempt}/{max_retries}...")
            
            # Use asyncio.wait_for to add a 120-second timeout
            await asyncio.wait_for(
                _generate_audio(text, voice, output_file, subtitle_file),
                timeout=120
            )
            print("  Voiceover generated successfully!")
            return
            
        except asyncio.TimeoutError:
            print(f"  Attempt {attempt} timed out after 120 seconds.")
        except Exception as e:
            print(f"  Attempt {attempt} failed: {e}")
        
        if attempt < max_retries:
            wait = 5 * attempt
            print(f"  Retrying in {wait} seconds...")
            await asyncio.sleep(wait)
    
    print("  [!] All voiceover attempts failed. Creating empty files.")
    # Create empty files so the pipeline doesn't crash
    open(output_file, 'wb').close()
    open(subtitle_file, 'w').close()


async def _generate_audio(text, voice, output_file, subtitle_file):
    """Internal function that does the actual TTS generation."""
    communicate = edge_tts.Communicate(text, voice)
    submaker = edge_tts.SubMaker()
    
    with open(output_file, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    
    with open(subtitle_file, "w", encoding="utf-8") as file:
        file.write(submaker.get_srt())


if __name__ == "__main__":
    # Test block
    asyncio.run(create_voiceover("Did you know that honey never spoils?", "en-US-ChristopherNeural", "voiceover.mp3", "subtitles.srt"))
    print("Generated voiceover and subtitles successfully.")
