"""
Batch 49: Expanding AI Automation Curriculum (Concepts & Strategies, not tools)
"""
import json, os

NEW_COURSES_BATCH49 = {
    "Automation Architecture": {
        "tier": "Beginner",
        "aiRubric": "Assess understanding of event-driven automation",
        "lessons": [
            {"title": "Triggers vs Actions", "theory": "## Event-Driven Design\\nEvery automation relies on an event-driven architecture. A `Trigger` is the event that starts the workflow (e.g., 'New Email Received'), while an `Action` is the task the workflow performs (e.g., 'Draft a Reply').", "instructions": "## Task: Identify the Trigger\\nIn a workflow that says: 'When a new row is added to Google Sheets, send a Slack message', what is the trigger?", "starterCode": "# Options: Send Slack message, New row added, Google Sheets API\\ntrigger = '___'", "solution": "# Options: Send Slack message, New row added, Google Sheets API\\ntrigger = 'New row added'", "hint": "The trigger is what starts it: New row added", "rubric": "Identifies 'New row added'."},
            {"title": "Stateful vs Stateless", "theory": "## Remembering Context\\nA stateless automation forgets everything once it finishes running. A stateful automation updates a central database (like a CRM) so the next time it runs, it knows what happened previously.", "instructions": "## Task: Concept Check\\nIf your automation needs to check if a customer was already emailed last week, does it need to be stateful or stateless?", "starterCode": "architecture = '___'", "solution": "architecture = 'stateful'", "hint": "It needs to remember, so it's stateful.", "rubric": "Identifies stateful."}
        ]
    },
    "Process Mapping": {
        "tier": "Intermediate",
        "aiRubric": "Assess business process analysis",
        "lessons": [
            {"title": "Identifying Bottlenecks", "theory": "## Don't Automate Broken Processes\\nBefore building an AI automation, you must map the manual process step-by-step. If a process is chaotic and poorly defined, automating it will just execute a bad process faster.", "instructions": "## Task: Rule of Thumb\\nAccording to Bill Gates: 'Automation applied to an efficient operation will magnify the efficiency. Automation applied to an inefficient operation will magnify the ___.'", "starterCode": "word = '___'", "solution": "word = 'inefficiency'", "hint": "inefficiency", "rubric": "Identifies inefficiency."},
            {"title": "Standard Operating Procedures", "theory": "## SOPs as Prompts\\nA well-written Standard Operating Procedure (SOP) is essentially an algorithmic instruction manual for humans. In AI automation, human SOPs map perfectly into System Prompts for LLMs.", "instructions": "## Task: Translation\\nWhat human document serves as the best starting template for an AI Agent's system prompt?", "starterCode": "answer = '___'", "solution": "answer = 'SOP'", "hint": "SOP (Standard Operating Procedure)", "rubric": "Identifies SOP or Standard Operating Procedure."}
        ]
    },
    "Human-in-the-Loop Strategy": {
        "tier": "Intermediate",
        "aiRubric": "Assess human-AI augmentation",
        "lessons": [
            {"title": "Augmentation vs Replacement", "theory": "## The Centaur Approach\\nTotal replacement is risky. Augmentation means the AI prepares 90% of the work (e.g., drafts a response), but a human must click 'Approve' or edit it before it goes out. This balances speed with quality control.", "instructions": "## Task: Strategy Definition\\nWhat is the term for a workflow where an AI pauses execution and waits for human approval?", "starterCode": "term = 'Human-in-the-___'", "solution": "term = 'Human-in-the-Loop'", "hint": "Loop", "rubric": "Identifies Human-in-the-Loop."},
            {"title": "Confidence Thresholds", "theory": "## Conditional Routing\\nYou can design an automation to check the AI's confidence score. If confidence > 95%, send automatically. If < 95%, route to a human.", "instructions": "## Task: Dynamic Routing\\nWrite a simple check that routes to a human if confidence is below 0.95.", "starterCode": "confidence = 0.82\\nif confidence ___ 0.95:\\n    route_to = '___'", "solution": "confidence = 0.82\\nif confidence < 0.95:\\n    route_to = 'Human'", "hint": "Use < and 'Human'", "rubric": "Correctly sets < and routes to Human."}
        ]
    },
    "Cost Analysis of Automation": {
        "tier": "Advanced",
        "aiRubric": "Assess token economics and ROI",
        "lessons": [
            {"title": "Token Economics", "theory": "## Calculating Costs\\nLLM API pricing is based on Tokens (roughly 0.75 words). You must calculate the cost of both the Input Prompt (which includes the system instructions and context) and the Output Tokens.", "instructions": "## Task: Calculate Cost\\nIf input tokens cost $10 per 1M and output tokens cost $30 per 1M, what is the cost of 100k input and 10k output tokens?", "starterCode": "input_cost = (100000 / 1000000) * 10\\noutput_cost = (10000 / 1000000) * 30\\ntotal = ___", "solution": "input_cost = (100000 / 1000000) * 10\\noutput_cost = (10000 / 1000000) * 30\\ntotal = 1.30", "hint": "1.00 + 0.30 = 1.30", "rubric": "Calculates 1.30."},
            {"title": "Return on Investment (ROI)", "theory": "## Business Value\\nAn automation might cost $500/month in API calls, but if it saves 100 hours of human labor billed at $30/hour, the net savings is massive.", "instructions": "## Task: Calculate ROI\\nA bot costs $200 but saves 50 hours of work at $20/hour. What is the net savings?", "starterCode": "human_cost = 50 * 20\\nnet_savings = human_cost - ___\\nanswer = ___", "solution": "human_cost = 50 * 20\\nnet_savings = human_cost - 200\\nanswer = 800", "hint": "1000 - 200 = 800", "rubric": "Calculates 800."}
        ]
    },
    "Failure States & Fallbacks": {
        "tier": "Advanced",
        "aiRubric": "Assess robust workflow design",
        "lessons": [
            {"title": "Graceful Degradation", "theory": "## Expecting Errors\\nAPIs fail. LLMs hallucinate. A robust automation uses 'Try/Catch' logic to gracefully degrade. If the AI API is down, the workflow should alert an admin rather than failing silently.", "instructions": "## Task: Error Path\\nIf an API call returns a 500 error, what is the safest automation step to trigger next?", "starterCode": "# Options: Retry infinitely, Send alert to admin, Ignore and proceed\\nnext_step = '___'", "solution": "# Options: Retry infinitely, Send alert to admin, Ignore and proceed\\nnext_step = 'Send alert to admin'", "hint": "Send alert to admin", "rubric": "Identifies Send alert to admin."},
            {"title": "Exponential Backoff", "theory": "## Rate Limits\\nIf you hit an API rate limit (e.g., 429 Too Many Requests), retrying immediately will just fail again. Exponential backoff means waiting 1s, then 2s, then 4s, etc., before retrying.", "instructions": "## Task: Backoff Multiplier\\nIf your first wait is 1s, and you multiply the wait time by 2 after each failure, what is the wait time after the 3rd failure?", "starterCode": "wait_1 = 1\\nwait_2 = 2\\nwait_3 = ___", "solution": "wait_1 = 1\\nwait_2 = 2\\nwait_3 = 4", "hint": "Multiply 2 by 2 = 4", "rubric": "Calculates 4."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'ai_automation.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH49.items():
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
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH49.items():
            tier = course_info["tier"]
            if "AI Automation" in index_data and tier in index_data["AI Automation"]:
                if new_course_name not in index_data["AI Automation"][tier]:
                    index_data["AI Automation"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 49: Added {total} lessons to AI Automation track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
