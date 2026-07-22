import os
import sys
import json
import random
from dotenv import load_dotenv
from google import genai
from google.genai import types
import state_manager

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MAX_REWRITE_ATTEMPTS = 3
MIN_SCORE = 9

def _build_script_prompt(state):
    """Build the main script generation prompt for the series."""
    previous_context = "\n".join(state['previous_events']) if state['previous_events'] else "This is the very first episode."
    
    return f"""
    You are the showrunner and lead writer for a viral, episodic "movie-like" series on YouTube Shorts/Reels/TikTok.
    The videos are published in horizontal (16:9) format and are 3 MINUTES LONG.
    Your writing must be gripping, atmospheric, and terrifying. Every sentence must build suspense.
    
    **SERIES INFO:**
    Title: {state['series_title']}
    Genre: {state['genre']}
    Current Episode: {state['current_episode']}
    Main Character: {state['main_character']['name']}
    
    **STORY CONTEXT:**
    Previous Events:
    {previous_context}
    
    Current Plot Hook (Start here):
    {state['plot_summary']}
    
    **YOUR TASK:**
    Write a 3-minute script (approx. 400-450 words) for Episode {state['current_episode']}.
    It MUST be spoken narration. No stage directions in the script part.
    End the episode on a massive cliffhanger.
    
    **STRUCTURE:**
    1. Hook: Start immediately with action, discovery, or fear based on the current plot hook.
    2. Body: Build massive tension. Escalate the mystery.
    3. Cliffhanger: End the episode leaving the viewer desperate for Episode {state['current_episode'] + 1}.
    
    **METADATA TO GENERATE:**
    - "image_prompts": A list of exactly 18 highly detailed image generation prompts that EXACTLY match the events in the script (approx. one image every 10 seconds).
      - VERY IMPORTANT: Create a MIX of shots! Some should show environments, some should show specific objects, clues, or monsters, and some should show the character. DO NOT just show the character in every single shot.
      - When the character IS in the shot, DO NOT use their name. Instead, inject this EXACT description: "{state['main_character']['description']}"
      - Prompts must be cinematic, photorealistic, 8k resolution, dramatic lighting.
    - "youtube_title": SEO clickbait title for this episode (e.g., "The Hollow Protocol: Ep {state['current_episode']} - The Shadow in the Woods 😱"). Max 60 chars. DO NOT use the word "shorts" or "#shorts".
    - "youtube_description": Description for the video with keywords and hashtags. DO NOT include #shorts.
    - "youtube_tags": List of 8-12 SEO tags. DO NOT include "shorts".
    - "thumbnail_prompt": Dramatic 16:9 thumbnail description for this episode.
    - "next_plot_summary": A 1-2 sentence summary of what happens next (the cliffhanger state) so the next episode can pick up from there.
    
    Format your response as a JSON object:
    {{
        "script": "the full script text",
        "image_prompts": ["prompt 1", "prompt 2", ...],
        "youtube_title": "...",
        "youtube_description": "...",
        "youtube_tags": ["tag1", "tag2"],
        "thumbnail_prompt": "...",
        "next_plot_summary": "..."
    }}
    """

def _build_scoring_prompt(content, state):
    """Build the quality scoring prompt."""
    return f"""
    You are a ruthless viral content quality analyst. Rate this 3-minute script on 5 dimensions.
    
    **SCRIPT TO EVALUATE:**
    "{content['script']}"
    
    **SCORING CRITERIA (1-10):**
    1. hook_strength: Does the start immediately grab attention?
    2. pacing: Is it engaging for a full 3 minutes (400+ words)?
    3. atmosphere: Does it feel like a cinematic {state['genre']} movie?
    4. cliffhanger: Is the ending an irresistible cliffhanger?
    5. prompt_quality: Are there 18 detailed image prompts that include the exact physical description of the character?
    
    Format your response as a JSON object:
    {{
        "hook_strength": <number>,
        "pacing": <number>,
        "atmosphere": <number>,
        "cliffhanger": <number>,
        "prompt_quality": <number>,
        "total_score": <sum of all five>,
        "feedback": "specific actionable feedback"
    }}
    """

def _build_rewrite_prompt(script, state, scores, feedback):
    """Build a rewrite prompt."""
    return f"""
    You are the showrunner for {state['series_title']}. A previous version of Episode {state['current_episode']} scored poorly and needs a COMPLETE rewrite.
    
    **SCORES:**
    - Hook: {scores.get('hook_strength')}/10
    - Pacing: {scores.get('pacing')}/10
    - Atmosphere: {scores.get('atmosphere')}/10
    - Cliffhanger: {scores.get('cliffhanger')}/10
    - Prompt Quality: {scores.get('prompt_quality')}/10
    
    **FEEDBACK:**
    {feedback}
    
    Write a COMPLETELY NEW 3-minute script (400-450 words) and 18 image prompts that fixes ALL issues. 
    Remember to create a MIX of environment, object, and character shots. 
    When the character is in the shot, use: "{state['main_character']['description']}"
    
    Format your response as a JSON object:
    {{
        "script": "the full script text",
        "image_prompts": ["prompt 1", "prompt 2", ...],
        "youtube_title": "...",
        "youtube_description": "...",
        "youtube_tags": ["tag1", "tag2"],
        "thumbnail_prompt": "...",
        "next_plot_summary": "..."
    }}
    """

def _parse_content_response(response_text):
    result = json.loads(response_text)
    return {
        "script": result.get("script", "").strip(),
        "image_prompts": result.get("image_prompts", []),
        "youtube_title": result.get("youtube_title", "").strip(),
        "youtube_description": result.get("youtube_description", "").strip(),
        "youtube_tags": result.get("youtube_tags", []),
        "thumbnail_prompt": result.get("thumbnail_prompt", "").strip(),
        "next_plot_summary": result.get("next_plot_summary", "").strip()
    }

def _score_script(client, content, state):
    prompt = _build_scoring_prompt(content, state)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json")
    )
    return json.loads(response.text)

def generate_script_and_topic():
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not set in .env file.")
        return None
        
    client = genai.Client(api_key=GEMINI_API_KEY)
    state = state_manager.load_state()
    
    print(f"\n--- Generating {state['series_title']} - Episode {state['current_episode']} ---")
    
    attempts = []
    print("Generating initial script and prompts...")
    prompt = _build_script_prompt(state)
    
    content = None
    for retry in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(response_mime_type="application/json")
            )
            content = _parse_content_response(response.text)
            break
        except Exception as e:
            print(f"Attempt {retry+1}/3 failed: {e}")
            if retry < 2:
                import time
                wait = 5 * (retry + 1)
                print(f"Retrying in {wait} seconds...")
                time.sleep(wait)
            else:
                print("All retries failed.")
                return None
    
    if content is None:
        return None
    
    for attempt in range(1, MAX_REWRITE_ATTEMPTS + 1):
        print(f"Scoring (attempt {attempt}/{MAX_REWRITE_ATTEMPTS})...")
        try:
            scores = _score_script(client, content, state)
        except Exception as e:
            print(f"Scoring failed: {e}. Using as-is.")
            break
            
        print(f"Total Score: {scores.get('total_score')}/50. Feedback: {scores.get('feedback')[:100]}...")
        attempts.append({"content": content, "scores": scores})
        
        passed = all(scores.get(m, 0) >= MIN_SCORE for m in ["hook_strength", "pacing", "atmosphere", "cliffhanger", "prompt_quality"])
        if passed:
            print("[OK] All scores >= 9!")
            break
            
        if attempt < MAX_REWRITE_ATTEMPTS:
            print("Rewriting to improve score...")
            try:
                rewrite_prompt = _build_rewrite_prompt(content["script"], state, scores, scores.get("feedback", ""))
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=rewrite_prompt,
                    config=types.GenerateContentConfig(response_mime_type="application/json")
                )
                content = _parse_content_response(response.text)
            except Exception as e:
                print(f"Rewrite failed: {e}. Using best available.")
                break
    
    best = max(attempts, key=lambda a: a["scores"].get("total_score", 0)) if attempts else {"content": content}
    final_content = best["content"]
    
    # NOTE: State is NOT updated here. main.py handles it after the video is fully generated.
    
    return final_content

if __name__ == "__main__":
    content = generate_script_and_topic()
    if content:
        print(f"\nScript ({len(content['script'].split())} words):\n{content['script'][:200]}...")
        print(f"\nImage Prompts ({len(content['image_prompts'])}):")
        for i, p in enumerate(content['image_prompts'][:3]):
            print(f" {i+1}. {p}")
        print(" ...")
