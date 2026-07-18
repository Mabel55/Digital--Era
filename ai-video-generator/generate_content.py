import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import random
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# All topic categories — one is picked randomly each run
TOPIC_CATEGORIES = [
    "Creepy unsolved mysteries — unsettling events that have never been explained",
    "Glitch in the matrix stories — creepy coincidences that prove reality might be fake",
    "Deep ocean terrors — horrifying things discovered at the bottom of the sea",
    "Space anomalies — horrifying things scientists just discovered in deep space",
    "Internet mysteries — the creepiest, most unsettling things found on the dark web",
    "Lost ancient technologies — advanced inventions from the past that were mysteriously destroyed",
    "Mandela effects — collective false memories that suggest we shifted parallel universes",
    "Cursed objects — real-life items that bring disaster to anyone who touches them",
    "Secret societies — the shadowy groups that allegedly control the world from behind closed doors",
    "Time traveler confessions — alleged accounts from people claiming to be from the future",
    "Unexplained disappearances — chilling cases of people who vanished into thin air",
    "Simulation theory evidence — signs that our reality is just an advanced computer program",
    "Government cover-ups — declassified documents that prove conspiracy theorists were right",
    "Creepy AI interactions — terrifying things artificial intelligence has said to humans",
    "Unsolved ciphers — mysterious codes and messages that no genius has been able to crack",
    "Bizarre medical anomalies — strange and terrifying conditions that baffle doctors",
    "Bermuda triangle secrets — bizarre disappearances and terrifying anomalies that cannot be explained",
    "Unidentified submarine objects (USOs) — the mysterious alien crafts spotted deep underwater",
    "Giant legendary sea creatures — terrifying evidence that prehistoric monsters still roam the deep ocean",
    "Lost underwater cities — massive ancient, advanced civilizations mysteriously swallowed by the sea",
    "Bizarre ocean sounds — unexplained, massive audio anomalies detected from the darkest depths of the ocean",
    "Ghost ships — mysterious ships found drifting perfectly intact but completely abandoned by the crew",
    "The Dyatlov Pass incident — nine experienced hikers die mysteriously in the Ural Mountains with bizarre injuries",
    "The Voynich Manuscript — a centuries-old book full of strange drawings written in an unknown language that no genius can decipher",
    "The Zodiac Killer's unsolved ciphers — mysterious, taunting codes left by a notorious serial killer that remain unbroken",
    "The Roanoke Colony — an entire settlement that vanished without a trace, leaving only one creepy word carved into a tree",
    "The Antikythera Mechanism — an ancient Greek analog computer that is thousands of years ahead of its time and shouldn't exist",
    "The Taos Hum — a maddening, low-frequency hum heard by people worldwide with no identifiable source",
    "The Dancing Plague of 1518 — a terrifying, bizarre event where hundreds of people danced uncontrollably until they collapsed or died",
    "The Wow! Signal — a mysterious, incredibly strong radio signal from deep space that was never heard again",
    "The Tunguska Event — a massive, unexplained explosion in Siberia that flattened millions of trees but left no crater",
    "The Nazca Lines — giant, perfectly straight geoglyphs in the Peruvian desert visible only from the sky, created by ancient people",
    "The Green Children of Woolpit — mysterious green-skinned children who mysteriously appeared in a 12th-century English village",
    "The Mary Celeste — a legendary ghost ship found adrift with its cargo intact but the entire crew missing without a trace",
    "The Overtoun Bridge — a creepy, mysterious bridge in Scotland where dogs inexplicably jump to their deaths",
    "The Pollock Twins — a chilling case of identical twins who seemingly remembered every detail of their deceased sisters' lives",
    "The Silent Twins — eerie twins who only spoke to each other in a secret language and made a chilling, deadly pact",
    "The Somerton Man — an unidentified man found dead on a beach with a mysterious, uncrackable code hidden in his pocket",
    "DB Cooper — the only completely unsolved commercial airplane hijacking in human history",
    "The Oak Island Money Pit — a mysterious, incredibly deep excavation site booby-trapped with deadly flood tunnels",
    "The Lost City of Atlantis — a legendary, highly advanced civilization that supposedly sank into the sea in a single day",
    "Flight 19 — five torpedo bombers that flew into the Bermuda Triangle and vanished into thin air without a single piece of wreckage",
    "The Piri Reis Map — a bizarre 16th-century map that accurately shows Antarctica without ice, long before it was officially discovered",
    "Spontaneous Human Combustion — terrifying, unexplained cases where people allegedly burst into flames for no apparent reason",
    "The Mothman Sightings — terrifying encounters with a winged, red-eyed creature that always seems to predict a massive disaster",
    "The Shroud of Turin — a highly controversial cloth bearing the detailed image of a man, believed by many to be supernatural",
    "The Baghdad Battery — ancient, mysterious artifacts that suggest people had working electricity thousands of years ago",
    "Dark Psychology tricks to read minds — simple psychological hacks that feel like superpowers",
    "Glitches in the Matrix — terrifying, real-life stories where reality seemed to break down",
    "Deep sea creatures that shouldn't exist — bizarre, terrifying monsters lurking at the bottom of the ocean",
    "The Mandela Effect — instances where millions of people clearly remember something that never existed",
    "Bizarre internet mysteries — creepy, unsolved internet puzzles and deep web legends",
]

HISTORY_FILE = "used_topics.json"

MAX_REWRITE_ATTEMPTS = 3
MIN_SCORE = 9


def _build_script_prompt(topic_category):
    """Build the main script generation prompt with the selected topic."""
    return f"""
    You are the world's top-performing short-form video script writer for a VIRAL MYSTERY channel. Your videos consistently get millions of views on YouTube Shorts, TikTok, and Instagram Reels. You understand viral psychology and the mystery niche deeply.
    
    Write a 60-second script (130-150 words) that is ENGINEERED to go viral, focusing strictly on the 'unsolved', 'unexplained', and 'bizarre' aspects of the topic.
    
    **TODAY'S TOPIC CATEGORY:**
    {topic_category}
    
    Pick a SPECIFIC, surprising angle within this category. Don't be generic — find the one fact/insight that makes people say "Wait, WHAT?!"
    
    **SCRIPT STRUCTURE (follow this EXACTLY):**
    1. HOOK (first sentence, under 3 seconds): Must be an extremely aggressive, mind-blowing open loop. Do NOT give context. Punch the viewer in the face with curiosity. Use patterns like:
       - "You've been lied to your entire life."
       - "This is the most terrifying thing nobody is talking about."
       - "Stop scrolling right now. This will blow your mind."
       - "If you ever see this, run away immediately."
       - "This secret psychological trick gives you superpowers."
    2. BODY (core content, ~100 words): Deliver rapid-fire value. Build up massive suspense. The very last sentence of the body must be a mind-blowing, terrifying twist or an unanswered question that leaves the viewer speechless.
    3. CLOSER (last 2 sentences, ~20 words): Create FOMO + drive engagement:
       - "Follow for part 2 — I'm exposing everything."
       - "Save this before it gets taken down."
       - "Comment 'MORE' if you want the full breakdown."
    
    **STYLE RULES:**
    - Write ONLY the spoken words. No stage directions, no [pause], no visuals.
    - Use conversational, high-energy language. Talk TO the viewer, not at them.
    - Every sentence must earn the next second of watch time.
    - Include at least one surprising statistic or specific number for credibility.
    
    **ALSO GENERATE METADATA:**
    - A Pexels video search query (1-3 words) for the background. MUST feature humans/people.
    - An incredibly SEO-optimized YouTube title (max 60 chars) that balances high search volume keywords with a clickbait hook. Include an emoji.
    - An SEO-rich YouTube description. The first 1-2 sentences MUST contain the primary search keywords naturally. Include a call to action and 3-5 targeted hashtags including #shorts.
    - A strategic list of 8-12 YouTube tags ranging from broad category keywords to specific long-tail phrases.
    - A youtube_category_id: The most appropriate YouTube category ID for this topic (e.g., "24" for Entertainment, "27" for Education, "28" for Science/Technology, "22" for People & Blogs).
    - A thumbnail_prompt: A detailed description for an eye-catching YouTube thumbnail. It should have bold text overlay (2-5 words), high contrast colors (bright yellows, reds, neons) that pop against YouTube's dark mode, and dramatic visuals.

    Format your response as a JSON object with exactly these keys:
    {{
        "script": "the full script text",
        "topic": "pexels search query",
        "youtube_title": "SEO clickbait title with emoji",
        "youtube_description": "SEO description with keywords in first sentences and hashtags",
        "youtube_tags": ["tag1", "tag2", "tag3", ...],
        "youtube_category_id": "numeric_string_id",
        "thumbnail_prompt": "detailed thumbnail image description"
    }}
    """


def _build_scoring_prompt(script, title, description, tags, topic_category):
    """Build the quality scoring prompt for a generated script."""
    return f"""
    You are a ruthless viral content quality analyst and a master of YouTube SEO. You've studied thousands of videos that got 10M+ views on YouTube Shorts.
    
    Rate this script and metadata on 5 dimensions. Be BRUTALLY honest — a 9 or 10 means this is in the top 1% of viral content.
    
    **TOPIC CATEGORY:** {topic_category}
    
    **METADATA TO EVALUATE:**
    Title: "{title}"
    Description: "{description}"
    Tags: {tags}
    
    **SCRIPT TO EVALUATE:**
    "{script}"
    
    **SCORING CRITERIA:**
    
    1. **hook_strength** (1-10): Does the first sentence FORCE you to stop scrolling? 
       - 9-10: Impossible to ignore. Creates immediate tension or curiosity.
       - 7-8: Good but predictable. Uses a known pattern without a twist.
       - Below 7: Weak, generic, or slow start.
    
    2. **curiosity** (1-10): Does the script create open loops that DEMAND you keep watching?
       - 9-10: Multiple nested curiosity gaps. You physically cannot look away.
       - 7-8: Some curiosity but payoff is predictable.
       - Below 7: Information is front-loaded, no reason to stay.
    
    3. **shareability** (1-10): Would someone SEND this to a friend unprompted?
       - 9-10: Contains a "holy shit" moment that demands sharing.
       - 7-8: Interesting but not share-worthy.
       - Below 7: Generic info anyone could Google.
    
    4. **retention** (1-10): Does EVERY sentence earn the next second of watch time?
       - 9-10: Zero filler. Each line is a mini-revelation. Perfect pacing.
       - 7-8: Some sentences don't add value or pace drops.
       - Below 7: Could be shorter. Attention wanders.
       
    5. **seo_optimization** (1-10): Are the title, description, and tags perfectly optimized for discovery?
       - 9-10: Title is highly clickable and contains main keywords. Description naturally integrates primary keywords in the first 2 sentences. Tags are a strategic mix of broad and long-tail.
       - 7-8: Basic SEO, maybe keyword stuffed or lacking a strong clickbait hook in the title.
       - Below 7: Weak keywords, poor description structure, or generic tags.
    
    Also provide specific, actionable feedback on what needs improvement.
    
    Format your response as a JSON object:
    {{
        "hook_strength": <number>,
        "curiosity": <number>,
        "shareability": <number>,
        "retention": <number>,
        "seo_optimization": <number>,
        "total_score": <sum of all five>,
        "feedback": "specific actionable feedback for improvement"
    }}
    """


def _build_rewrite_prompt(script, topic_category, scores, feedback):
    """Build a rewrite prompt incorporating scoring feedback."""
    return f"""
    You are the world's top-performing short-form video script writer. A previous version of your script scored poorly and needs a COMPLETE rewrite.
    
    **TOPIC CATEGORY:** {topic_category}
    
    **PREVIOUS SCRIPT (DO NOT reuse this — write something COMPLETELY NEW):**
    \"{script}\"
    
    **SCORES FROM QUALITY REVIEW:**
    - Hook Strength: {scores.get('hook_strength', 'N/A')}/10
    - Curiosity: {scores.get('curiosity', 'N/A')}/10
    - Shareability: {scores.get('shareability', 'N/A')}/10
    - Retention: {scores.get('retention', 'N/A')}/10
    - SEO Optimization: {scores.get('seo_optimization', 'N/A')}/10
    
    **SPECIFIC FEEDBACK TO ADDRESS:**
    {feedback}
    
    Write a COMPLETELY NEW 60-second script (130-150 words) and METADATA that fixes ALL the issues above. Every score must be 9 or higher. Focus heavily on SEO if the SEO score was low.
    
    **SCRIPT STRUCTURE (follow this EXACTLY):**
    1. HOOK (first 2 sentences, ~15 words): Must create an irresistible open loop.
    2. BODY (core content, ~100 words): Build massive suspense. The last sentence must be a mind-blowing, terrifying twist.
    3. CLOSER (last 2 sentences, ~20 words): Create FOMO + drive engagement.
    
    **STYLE RULES:**
    - Write ONLY the spoken words. No stage directions.
    - Conversational, high-energy language.
    - Every sentence must earn the next second of watch time.
    - Include at least one surprising statistic or specific number.
    
    **ALSO GENERATE METADATA:**
    - A Pexels video search query (1-3 words) featuring humans/people.
    - An incredibly SEO-optimized YouTube title (max 60 chars) with emoji.
    - An SEO-rich YouTube description. First 1-2 sentences MUST contain primary search keywords. Include hashtags.
    - A strategic list of 8-12 YouTube tags for SEO.
    - A youtube_category_id (e.g., "24", "27", "28", "22").
    - A thumbnail_prompt: detailed description for a high-contrast YouTube thumbnail with bold text.
    
    Format your response as a JSON object with exactly these keys:
    {{
        "script": "the full script text",
        "topic": "pexels search query",
        "youtube_title": "SEO title with emoji",
        "youtube_description": "SEO description with keywords and hashtags",
        "youtube_tags": ["tag1", "tag2", "tag3", ...],
        "youtube_category_id": "numeric_string_id",
        "thumbnail_prompt": "detailed thumbnail image description"
    }}
    """


def _parse_content_response(response_text):
    """Parse the JSON response from content generation."""
    result = json.loads(response_text)
    return {
        "script": result.get("script", "").strip(),
        "topic": result.get("topic", "").strip(),
        "youtube_title": result.get("youtube_title", "").strip(),
        "youtube_description": result.get("youtube_description", "").strip(),
        "youtube_tags": result.get("youtube_tags", []),
        "youtube_category_id": result.get("youtube_category_id", "22"),
        "thumbnail_prompt": result.get("thumbnail_prompt", "").strip(),
    }


def _score_script(client, content, topic_category):
    """Score a script and metadata using Gemini and return the scores dict."""
    scoring_prompt = _build_scoring_prompt(
        content["script"], 
        content.get("youtube_title", ""), 
        content.get("youtube_description", ""), 
        content.get("youtube_tags", []), 
        topic_category
    )
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=scoring_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )
    return json.loads(response.text)


def _passes_quality_gate(scores):
    """Check if all individual scores meet the minimum threshold."""
    metrics = ["hook_strength", "curiosity", "shareability", "retention", "seo_optimization"]
    for metric in metrics:
        if scores.get(metric, 0) < MIN_SCORE:
            return False
    return True


def _print_scores(scores, attempt):
    """Pretty-print the quality scores."""
    print(f"\n  [ Quality Scores (Attempt {attempt}) ]")
    print(f"     Hook Strength:  {scores.get('hook_strength', '?')}/10")
    print(f"     Curiosity:      {scores.get('curiosity', '?')}/10")
    print(f"     Shareability:   {scores.get('shareability', '?')}/10")
    print(f"     Retention:      {scores.get('retention', '?')}/10")
    print(f"     SEO Quality:    {scores.get('seo_optimization', '?')}/10")
    print(f"     Total:          {scores.get('total_score', '?')}/50")
    if scores.get('feedback'):
        print(f"     Feedback:       {scores['feedback'][:120]}...")


def _get_recent_topics(max_history):
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def _save_recent_topic(topic, max_history):
    history = _get_recent_topics(max_history)
    history.append(topic)
    if len(history) > max_history:
        history = history[-max_history:]
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def generate_script_and_topic():
    """
    Generates a viral ~60-second video script with quality scoring.
    
    The script goes through a quality gate:
    - Gemini scores it on hook_strength, curiosity, shareability, retention (each 1-10)
    - If any score < 9, the script is rewritten with feedback
    - Up to 3 attempts; picks the best-scoring version
    
    Returns: (script, topic, youtube_title, youtube_description, youtube_tags, youtube_category_id, thumbnail_prompt)
    """
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not set in .env file.")
        return None, None, None, None, None, None, None
        
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # Pick a random topic category that wasn't used recently
    max_history = len(TOPIC_CATEGORIES) - 3  # Leave at least 3 topics available to choose from
    recent_topics = _get_recent_topics(max_history)
    available_topics = [t for t in TOPIC_CATEGORIES if t not in recent_topics]
    
    if not available_topics:
        available_topics = TOPIC_CATEGORIES
        
    topic_category = random.choice(available_topics)
    _save_recent_topic(topic_category, max_history)
    
    print(f"Selected topic category: {topic_category.split('—')[0].strip()}")
    
    # Track all attempts to pick the best one
    attempts = []
    
    # === Attempt 1: Initial generation ===
    print("\nGenerating initial script with Gemini...")
    prompt = _build_script_prompt(topic_category)
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            )
        )
        content = _parse_content_response(response.text)
    except Exception as e:
        print(f"Failed to generate content: {e}")
        return None, None, None, None, None, None, None
    
    # === Score and rewrite loop ===
    for attempt in range(1, MAX_REWRITE_ATTEMPTS + 1):
        print(f"\nScoring script (attempt {attempt}/{MAX_REWRITE_ATTEMPTS})...")
        
        try:
            scores = _score_script(client, content, topic_category)
        except Exception as e:
            print(f"  [!] Scoring failed: {e}. Using script as-is.")
            break
        
        _print_scores(scores, attempt)
        attempts.append({"content": content, "scores": scores})
        
        if _passes_quality_gate(scores):
            print("\n  [OK] All scores >= 9! Script approved.")
            break
        
        if attempt < MAX_REWRITE_ATTEMPTS:
            print(f"\n  [RETRY] Score below 9 detected. Rewriting (attempt {attempt + 1})...")
            try:
                rewrite_prompt = _build_rewrite_prompt(
                    content["script"], topic_category, scores, scores.get("feedback", "")
                )
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=rewrite_prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                    )
                )
                content = _parse_content_response(response.text)
            except Exception as e:
                print(f"  [!] Rewrite failed: {e}. Using best available script.")
                break
        else:
            print(f"\n  [!] Max attempts reached. Using best-scoring version.")
    
    # Pick the best-scoring attempt
    if attempts:
        best = max(attempts, key=lambda a: a["scores"].get("total_score", 0))
        content = best["content"]
        best_total = best["scores"].get("total_score", 0)
        print(f"\n[BEST] Best script selected (total score: {best_total}/50)")
    
    return (
        content["script"],
        content["topic"],
        content["youtube_title"],
        content["youtube_description"],
        content["youtube_tags"],
        content["youtube_category_id"],
        content["thumbnail_prompt"],
    )


if __name__ == "__main__":
    s, t, yt_title, yt_desc, yt_tags, yt_category_id, thumb_prompt = generate_script_and_topic()
    if s and t:
        print(f"\n{'='*50}")
        print(f"Topic: {t}\n")
        print(f"Script ({len(s.split())} words):\n{s}\n")
        print(f"YouTube Title: {yt_title}")
        print(f"YouTube Description: {yt_desc}")
        print(f"YouTube Tags: {yt_tags}")
        print(f"YouTube Category ID: {yt_category_id}")
        print(f"\nThumbnail Prompt: {thumb_prompt}")
