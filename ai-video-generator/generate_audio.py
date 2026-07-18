import asyncio
import edge_tts

async def create_voiceover(text: str, voice: str, output_file: str, subtitle_file: str):
    """
    Generate voiceover and subtitles from text using edge-tts.
    """
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
