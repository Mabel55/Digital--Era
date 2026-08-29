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
    """Build the main script generation prompt for the marketing series."""
    previous_context = "\n".join(state['previous_events']) if state['previous_events'] else "This is the very first episode."
    
    return f"""
    You are the lead marketer and educational content creator for "Digital Era", a top-tier tech training centre in Ikorodu, Lagos, Nigeria.
    The videos are published in horizontal (16:9) format and are 1 MINUTE LONG.
    Your writing must be highly engaging, educational, and end with a strong Call to Action (CTA) to enroll at Digital Era.
    
    **SERIES INFO:**
    Title: {state['series_title']}
    Genre: {state['genre']}
    Current Episode: {state['current_episode']}
    
    **STORY CONTEXT:**
    Previous Topics Covered:
    {previous_context}
    
    Current Topic (Start here):
    {state['plot_summary']}
    
    **YOUR TASK:**
    Write a 1-minute script (approx. 130-150 words) for Episode {state['current_episode']}.
    It MUST be spoken narration. No stage directions in the script part.
    End the video with a strong Call to Action to enroll at Digital Era by calling +234 703 719 7261 or visiting digital-era.live.
    
    **STRUCTURE:**
    1. Hook: Start immediately with a strong question or fact about the current tech topic.
    2. Body: Explain the concept simply but professionally. Mention how learning this can lead to a great career.
    3. CTA: Call to action to join Digital Era in Ikorodu, Lagos.
    
    **METADATA TO GENERATE:**
    - "image_prompts": A list of exactly 6 highly detailed image generation prompts that EXACTLY match the events in the script (approx. one image every 10 seconds).
      - VERY IMPORTANT: Create a MIX of shots! Some should show modern computer screens with code, some should show diverse tech students in a classroom, and some should show neon green branding (Digital Era's colors).
      - Prompts must be cinematic, photorealistic, 8k resolution, dramatic lighting.
    - "youtube_title": SEO clickbait title for this episode (e.g., "Why Learn Python in 2024? 🚀 | Digital Era Tech Tips"). Max 60 chars.
    - "youtube_description": Description for the video with keywords and hashtags. Mention Ikorodu and Lagos.
    - "youtube_tags": List of 8-12 SEO tags related to the tech topic.
    - "thumbnail_prompt": Dramatic 16:9 thumbnail description for this episode.
    - "next_plot_summary": A 1-2 sentence summary of what tech topic should be covered next (e.g., "Data Science vs Data Analytics").
    
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
    You are a viral content quality analyst. Rate this 1-minute script on 5 dimensions.
    
    **SCRIPT TO EVALUATE:**
    "{content['script']}"
    
    **SCORING CRITERIA (1-10):**
    1. hook_strength: Does the start immediately grab attention?
    2. pacing: Is it engaging for a full 1 minute (130+ words)?
    3. educational_value: Is the tech concept explained clearly?
    4. call_to_action: Is the CTA to enroll at Digital Era clear and compelling?
    5. prompt_quality: Are there exactly 6 detailed image prompts related to tech and Digital Era?
    
    Format your response as a JSON object:
    {{
        "hook_strength": <number>,
        "pacing": <number>,
        "educational_value": <number>,
        "call_to_action": <number>,
        "prompt_quality": <number>,
        "total_score": <sum of all five>,
        "feedback": "specific actionable feedback"
    }}
    """

def _build_rewrite_prompt(script, state, scores, feedback):
    """Build a rewrite prompt."""
    return f"""
    You are the lead marketer for {state['series_title']}. A previous version of Episode {state['current_episode']} scored poorly and needs a COMPLETE rewrite.
    
    **SCORES:**
    - Hook: {scores.get('hook_strength')}/10
    - Pacing: {scores.get('pacing')}/10
    - Educational Value: {scores.get('educational_value')}/10
    - Call to Action: {scores.get('call_to_action')}/10
    - Prompt Quality: {scores.get('prompt_quality')}/10
    
    **FEEDBACK:**
    {feedback}
    
    Write a COMPLETELY NEW 1-minute script (130-150 words) and 6 image prompts that fixes ALL issues. 
    Remember to create a MIX of tech-related shots and mention Digital Era in Ikorodu. 
    
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
        
        passed = all(scores.get(m, 0) >= MIN_SCORE for m in ["hook_strength", "pacing", "educational_value", "call_to_action", "prompt_quality"])
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
