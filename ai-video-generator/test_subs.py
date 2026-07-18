import asyncio
import edge_tts

async def test():
    comm = edge_tts.Communicate("Hello world, this is a test.", "en-US-AndrewNeural")
    sub = edge_tts.SubMaker()
    chunks_seen = {}
    async for chunk in comm.stream():
        t = chunk["type"]
        if t not in chunks_seen:
            chunks_seen[t] = chunk
            print(f"Type: {t}, Keys: {list(chunk.keys())}")
        if t in ("WordBoundary", "SentenceBoundary"):
            sub.feed(chunk)
    print(f"\nAll chunk types: {list(chunks_seen.keys())}")
    srt = sub.get_srt()
    print(f"SRT length: {len(srt)}")
    if srt:
        print(f"SRT preview:\n{srt[:300]}")
    else:
        print("SRT is EMPTY!")

asyncio.run(test())
