"""
Batch 32: Massive AI Automation Expansion (Scraping, Sales, Data, Support, No-Code)
"""
import json, os

NEW_COURSES_BATCH32 = {
    "Web Scraping & RPA": {
        "tier": "Intermediate",
        "aiRubric": "Assess web scraping and RPA knowledge",
        "lessons": [
            {"title": "Headless Browser Automation", "theory": "## Playwright & Puppeteer\\nWhen a website lacks an API, you can automate a headless browser to click buttons, fill forms, and extract data programmatically.", "instructions": "## Task: Browser Script\\nWrite a simple Playwright snippet to navigate to a URL and print its title.", "starterCode": "import asyncio\\nfrom playwright.async_api import async_playwright\\n\\nasync def main():\\n    async with async_playwright() as p:\\n        browser = await p.chromium.launch()\\n        page = await browser.new_page()\\n        await page.___(url)\\n        print(await page.___) \\n        await browser.close()", "solution": "import asyncio\\nfrom playwright.async_api import async_playwright\\n\\nasync def main():\\n    async with async_playwright() as p:\\n        browser = await p.chromium.launch()\\n        page = await browser.new_page()\\n        await page.goto(url)\\n        print(await page.title()) \\n        await browser.close()", "hint": "Use goto and title()", "rubric": "Correctly navigates and prints title."},
            {"title": "Vision AI Scraping", "theory": "## Reading Screenshots\\nModern web apps use dynamic CSS classes that break traditional scrapers. Multimodal LLMs can simply 'look' at a screenshot and extract the data you need.", "instructions": "## Task: Image Prompting\\nWrite a prompt to extract a pricing table from an image.", "starterCode": "image_url = 'https://example.com/pricing.png'\\nprompt = 'Extract the pricing tiers and features from this image into ___ format.'", "solution": "image_url = 'https://example.com/pricing.png'\\nprompt = 'Extract the pricing tiers and features from this image into JSON format.'", "hint": "Use JSON", "rubric": "Requests JSON format."}
        ]
    },
    "AI Lead Generation": {
        "tier": "Advanced",
        "aiRubric": "Assess AI sales automation",
        "lessons": [
            {"title": "Hyper-Personalized Outreach", "theory": "## Doing the Research\\nNobody replies to generic cold emails. AI agents can scrape a company's website, read their recent news, and craft an email that sounds 100% human.", "instructions": "## Task: Prompting for Personalization\\nWrite a prompt that uses a company summary to generate a personalized opening line.", "starterCode": "company_summary = 'Recent series B funding to build AI chips.'\\nprompt = f'Write a casual opening sentence for a cold email mentioning: {___}'", "solution": "company_summary = 'Recent series B funding to build AI chips.'\\nprompt = f'Write a casual opening sentence for a cold email mentioning: {company_summary}'", "hint": "company_summary", "rubric": "Uses company_summary in the prompt."},
            {"title": "Sentiment Routing in CRM", "theory": "## Automated Inbox Management\\nInstead of manually reading replies, an LLM can analyze the sentiment of incoming emails and tag them in your CRM as 'Interested', 'Unsubscribe', or 'Questions'.", "instructions": "## Task: Sentiment Classification\\nWrite an API call configuration that classifies email sentiment.", "starterCode": "email = 'Stop emailing me.'\\nmessages = [{'role': 'system', 'content': 'Classify as Interested or Unsubscribe. Reply with only one word.'}, {'role': 'user', 'content': ___}]", "solution": "email = 'Stop emailing me.'\\nmessages = [{'role': 'system', 'content': 'Classify as Interested or Unsubscribe. Reply with only one word.'}, {'role': 'user', 'content': email}]", "hint": "Pass the email content.", "rubric": "Passes the email variable."}
        ]
    },
    "Document & Audio Pipelines": {
        "tier": "Intermediate",
        "aiRubric": "Assess unstructured data extraction",
        "lessons": [
            {"title": "Invoice Parsing", "theory": "## Extracting Unstructured Data\\nPDF invoices come in thousands of formats. Instead of writing Regex for each one, LLMs can extract fields like 'Total Amount' reliably.", "instructions": "## Task: Data Schema Setup\\nDefine a Pydantic schema for an invoice so the LLM knows what to extract.", "starterCode": "from pydantic import BaseModel\\n\\nclass Invoice(BaseModel):\\n    vendor_name: str\\n    total_amount: ___\\n    date_issued: ___", "solution": "from pydantic import BaseModel\\n\\nclass Invoice(BaseModel):\\n    vendor_name: str\\n    total_amount: float\\n    date_issued: str", "hint": "float and str", "rubric": "Defines float for amount and str for date."},
            {"title": "Meeting Transcripts", "theory": "## Whisper to Action Items\\nThe classic AI pipeline: Audio -> Whisper API (Transcription) -> GPT-4 (Summarization & Action Items).", "instructions": "## Task: The Whisper API Call\\nWrite the basic structure to send an audio file to OpenAI's transcription endpoint.", "starterCode": "with open('meeting.mp3', 'rb') as audio_file:\\n    transcript = client.audio.___.create(\\n        model='whisper-1',\\n        file=___\\n    )", "solution": "with open('meeting.mp3', 'rb') as audio_file:\\n    transcript = client.audio.transcriptions.create(\\n        model='whisper-1',\\n        file=audio_file\\n    )", "hint": "Use transcriptions and audio_file", "rubric": "Correctly calls transcriptions.create."}
        ]
    },
    "AI Support Helpdesks": {
        "tier": "Intermediate",
        "aiRubric": "Assess customer support automation",
        "lessons": [
            {"title": "Intelligent Ticket Routing", "theory": "## Triage with AI\\nWhen a ticket arrives, AI can determine its urgency (e.g., 'Server down' = P1) and the correct department (e.g., 'Billing').", "instructions": "## Task: Routing Logic\\nWrite a script that routes the ticket based on an LLM's JSON response.", "starterCode": "ai_response = {'department': 'billing', 'urgency': 'high'}\\n\\nif ai_response['___'] == 'high':\\n    notify_on_call()\\nif ai_response['___'] == 'billing':\\n    assign_to_team('Finance')", "solution": "ai_response = {'department': 'billing', 'urgency': 'high'}\\n\\nif ai_response['urgency'] == 'high':\\n    notify_on_call()\\nif ai_response['department'] == 'billing':\\n    assign_to_team('Finance')", "hint": "urgency and department", "rubric": "Correctly accesses dictionary keys."},
            {"title": "Auto-Drafting Replies", "theory": "## Human in the Loop\\nInstead of auto-replying (which is dangerous), use AI to draft a response inside Zendesk/Intercom. The human agent simply reviews, tweaks, and sends.", "instructions": "## Task: Draft Mode\\nEnsure your automation sets the message as an internal note/draft, not a public reply.", "starterCode": "ticket_update = {\\n    'body': llm_draft,\\n    'public': ___ # Set to false to keep it internal\\n}", "solution": "ticket_update = {\\n    'body': llm_draft,\\n    'public': False # Set to false to keep it internal\\n}", "hint": "False", "rubric": "Sets public to False."}
        ]
    },
    "No-Code AI Apps": {
        "tier": "Beginner",
        "aiRubric": "Assess no-code AI integrations",
        "lessons": [
            {"title": "Notion AI Automations", "theory": "## Smarter Workspaces\\nNotion's API allows you to automatically tag incoming tasks, summarize meeting notes, or generate project timelines.", "instructions": "## Task: Notion Property Update\\nWrite the JSON payload to update a Notion page's 'Status' property to 'Done'.", "starterCode": "properties = {\\n    'Status': {\\n        'select': {\\n            'name': '___'\\n        }\\n    }\\n}", "solution": "properties = {\\n    'Status': {\\n        'select': {\\n            'name': 'Done'\\n        }\\n    }\\n}", "hint": "Done", "rubric": "Sets name to Done."},
            {"title": "Bubble & OpenAI", "theory": "## Building AI Interfaces\\nTools like Bubble let you build visual frontends for your AI tools without writing code. You use the 'API Connector' to talk to OpenAI.", "instructions": "## Task: Dynamic Data\\nIn Bubble, parameters enclosed in <> are dynamic. Define a dynamic prompt parameter.", "starterCode": "json_body = {\\n    \"prompt\": \"<___>\"\\n}", "solution": "json_body = {\\n    \"prompt\": \"<user_input>\"\\n}", "hint": "user_input (or any variable name)", "rubric": "Uses dynamic parameter syntax."}
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
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH32.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH32.items():
            tier = course_info["tier"]
            if "AI Automation" in index_data and tier in index_data["AI Automation"]:
                if new_course_name not in index_data["AI Automation"][tier]:
                    index_data["AI Automation"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 32: Added/Appended {total} lessons to AI Automation')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
