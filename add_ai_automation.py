import json
import os

NEW_COURSES = {
    "AI Automation": {
        "Intermediate": [
            "n8n Workflows"
        ],
        "Advanced": [
            "Automated Social Media"
        ]
    }
}

NEW_COURSE_CONTENT = {
    "AI Automation": {
        # --- NEW COURSES ---
        "n8n Workflows": {
            "aiRubric": "Assess n8n workflow knowledge",
            "lessons": [
                {
                    "title": "n8n Self-Hosting",
                    "theory": "## Hosting n8n\nn8n is a fair-code licensed automation tool that you can self-host. It uses a node-based interface to connect different APIs.",
                    "instructions": "## Task: Environment Setup\nDefine the environment variable to enable webhook execution in n8n.",
                    "starterCode": "# Enable webhook URL for n8n\nWEBHOOK_URL=___",
                    "solution": "# Enable webhook URL for n8n\nWEBHOOK_URL=https://my-n8n.domain.com",
                    "hint": "Set it to a domain URL.",
                    "rubric": "Webhook URL is defined."
                },
                {
                    "title": "Data Transformation",
                    "theory": "## The Item Lists Node\nIn n8n, data is processed as an array of items. The Item Lists node helps manipulate this data structure.",
                    "instructions": "## Task: Node Configuration\nWrite a simple JS snippet for a Code node to return the first item.",
                    "starterCode": "for (let item of $input.all()) {\n  return [___];\n}",
                    "solution": "for (let item of $input.all()) {\n  return [item];\n}",
                    "hint": "Return item",
                    "rubric": "Returns item."
                }
            ]
        },
        "Automated Social Media": {
            "aiRubric": "Assess social media automation",
            "lessons": [
                {
                    "title": "Generating Posts via API",
                    "theory": "## Content Generation\nUse LLMs to automatically generate social media posts based on news articles or RSS feeds.",
                    "instructions": "## Task: API Prompting\nWrite a prompt to generate a tweet from a summary.",
                    "starterCode": "summary = 'AI agent passes Turing test.'\nprompt = f'Write a short tweet about: {___}'",
                    "solution": "summary = 'AI agent passes Turing test.'\nprompt = f'Write a short tweet about: {summary}'",
                    "hint": "summary",
                    "rubric": "Uses summary."
                }
            ]
        }
    }
}

ADDITIONAL_LESSONS = {
    # --- EXISTING COURSES ---
    "Zapier Basics": [
        {
            "title": "Triggers and Actions",
            "theory": "## The Anatomy of a Zap\nA Zap consists of a Trigger (the event that starts the automation) and one or more Actions (what the automation does).",
            "instructions": "## Task: Define a Zap\nIdentify the trigger and action from the scenario: 'When I get an email, save it to Google Drive.'",
            "starterCode": "trigger = '___'\naction = '___'",
            "solution": "trigger = 'Receive email'\naction = 'Save to Google Drive'",
            "hint": "trigger is receiving an email, action is saving to drive.",
            "rubric": "Trigger and action are correctly identified."
        }
    ],
    "Custom Webhooks": [
        {
            "title": "Catching Webhooks",
            "theory": "## Webhook Receivers\nA webhook receiver is an endpoint that waits for incoming HTTP POST requests containing JSON data.",
            "instructions": "## Task: Webhook Parser\nExtract the 'event_type' from a webhook payload.",
            "starterCode": "payload = {'event_type': 'user_signup', 'email': 'test@test.com'}\nevent = payload[___]",
            "solution": "payload = {'event_type': 'user_signup', 'email': 'test@test.com'}\nevent = payload['event_type']",
            "hint": "Use the key 'event_type'",
            "rubric": "Extracts event_type correctly."
        }
    ]
}

def add_new_courses_and_lessons():
    # 1. Update index.json with new courses
    index_path = os.path.join("curriculum", "index.json")
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)
        
    for track, tiers in NEW_COURSES.items():
        if track in index_data:
            for tier, courses in tiers.items():
                if tier in index_data[track]:
                    for course in courses:
                        if course not in index_data[track][tier]:
                            index_data[track][tier].append(course)
                            
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
        
    print("Updated index.json")

    # 2. Update track file
    track_path = os.path.join("curriculum", "tracks", "ai_automation.json")
    
    if os.path.exists(track_path):
        with open(track_path, "r", encoding="utf-8") as f:
            track_data = json.load(f)
            
        # Add new courses
        for course_name, course_content in NEW_COURSE_CONTENT["AI Automation"].items():
            if course_name not in track_data:
                track_data[course_name] = course_content
                print(f"Added course payload for {course_name}")
                
        # Add additional lessons to existing courses
        for course_name, lessons in ADDITIONAL_LESSONS.items():
            if course_name in track_data:
                if 'lessons' not in track_data[course_name]:
                    track_data[course_name]['lessons'] = []
                existing_titles = [l['title'] for l in track_data[course_name]['lessons']]
                for new_lesson in lessons:
                    if new_lesson['title'] not in existing_titles:
                        track_data[course_name]['lessons'].append(new_lesson)
                        print(f"Appended lesson '{new_lesson['title']}' to {course_name}")
                        
        with open(track_path, "w", encoding="utf-8") as f:
            json.dump(track_data, f, indent=2, ensure_ascii=False)

    # 3. Rebuild courses.js
    os.system("python build_courses.py")

if __name__ == '__main__':
    add_new_courses_and_lessons()
