"""
Batch 30: Expanding AI Automation Content
"""
import json, os

LESSONS_BATCH30 = {
    "Zapier Basics": [
        {"title": "Triggers and Actions", "theory": "## The Anatomy of a Zap\\nA Zap consists of a Trigger (the event that starts the automation) and one or more Actions (what the automation does).", "instructions": "## Task: Define a Zap\\nIdentify the trigger and action from the scenario: 'When I get an email, save it to Google Drive.'", "starterCode": "trigger = '___'\\naction = '___'", "solution": "trigger = 'Receive email'\\naction = 'Save to Google Drive'", "hint": "trigger is receiving an email, action is saving to drive.", "rubric": "Trigger and action are correctly identified."}
    ],
    "Custom Webhooks": [
        {"title": "Catching Webhooks", "theory": "## Webhook Receivers\\nA webhook receiver is an endpoint that waits for incoming HTTP POST requests containing JSON data.", "instructions": "## Task: Webhook Parser\\nExtract the 'event_type' from a webhook payload.", "starterCode": "payload = {'event_type': 'user_signup', 'email': 'test@test.com'}\\nevent = payload[___]", "solution": "payload = {'event_type': 'user_signup', 'email': 'test@test.com'}\\nevent = payload['event_type']", "hint": "Use the key 'event_type'", "rubric": "Extracts event_type correctly."}
    ]
}

NEW_COURSES_BATCH30 = {
    "n8n Workflows": {
        "tier": "Intermediate",
        "aiRubric": "Assess n8n workflow knowledge",
        "lessons": [
            {"title": "n8n Self-Hosting", "theory": "## Hosting n8n\\nn8n is a fair-code licensed automation tool that you can self-host. It uses a node-based interface to connect different APIs.", "instructions": "## Task: Environment Setup\\nDefine the environment variable to enable webhook execution in n8n.", "starterCode": "# Enable webhook URL for n8n\\nWEBHOOK_URL=___", "solution": "# Enable webhook URL for n8n\\nWEBHOOK_URL=https://my-n8n.domain.com", "hint": "Set it to a domain URL.", "rubric": "Webhook URL is defined."},
            {"title": "Data Transformation", "theory": "## The Item Lists Node\\nIn n8n, data is processed as an array of items. The Item Lists node helps manipulate this data structure.", "instructions": "## Task: Node Configuration\\nWrite a simple JS snippet for a Code node to return the first item.", "starterCode": "for (let item of $input.all()) {\\n  return [___];\\n}", "solution": "for (let item of $input.all()) {\\n  return [item];\\n}", "hint": "Return item", "rubric": "Returns item."}
        ]
    },
    "Automated Social Media": {
        "tier": "Advanced",
        "aiRubric": "Assess social media automation",
        "lessons": [
            {"title": "Generating Posts via API", "theory": "## Content Generation\\nUse LLMs to automatically generate social media posts based on news articles or RSS feeds.", "instructions": "## Task: API Prompting\\nWrite a prompt to generate a tweet from a summary.", "starterCode": "summary = 'AI agent passes Turing test.'\\nprompt = f'Write a short tweet about: {___}'", "solution": "summary = 'AI agent passes Turing test.'\\nprompt = f'Write a short tweet about: {summary}'", "hint": "summary", "rubric": "Uses summary."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'ai_automation.json')
    
    # 1. Update ai_automation.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add new lessons to existing courses
        for course_name in track_data:
            if course_name in LESSONS_BATCH30:
                if 'lessons' not in track_data[course_name]:
                    track_data[course_name]['lessons'] = []
                existing_titles = [l['title'] for l in track_data[course_name]['lessons']]
                for new_lesson in LESSONS_BATCH30[course_name]:
                    if new_lesson['title'] not in existing_titles:
                        track_data[course_name]['lessons'].append(new_lesson)
                        updated = True
                        total += 1
                        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH30.items():
            if new_course_name not in track_data:
                track_data[new_course_name] = {
                    "aiRubric": course_info["aiRubric"],
                    "lessons": course_info["lessons"]
                }
                updated = True
                total += len(course_info["lessons"])
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH30.items():
            tier = course_info["tier"]
            if "AI Automation" in index_data and tier in index_data["AI Automation"]:
                if new_course_name not in index_data["AI Automation"][tier]:
                    index_data["AI Automation"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 30: Added/Appended {total} lessons to AI Automation')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
