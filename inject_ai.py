import json
import os

new_lessons = {
    "ai_engineering.json": {
        "course": "Intro to LLMs",
        "lesson": {
            "title": "What is Artificial Intelligence?",
            "theory": "## From Rules to Patterns\n\nFor the last 50 years, computers have operated on a very simple premise: **Rules**. \n\nIf you wanted a computer to sort emails into a spam folder, a programmer had to write strict rules:\n- `IF email contains \"buy now\" THEN move to spam`\n- `IF email is from an unknown sender THEN move to spam`\n\nThis is traditional software engineering. It works perfectly for banking apps or video games, but it fails completely for complex human tasks. You cannot write a \"rule\" for how to recognize a picture of a cat, or how to translate a poem from English to Japanese.\n\n### The Shift to AI\n\n**Artificial Intelligence (AI)** flips the traditional model upside down.\n\nInstead of giving the computer the *rules*, we give the computer the *data*, and force it to figure out the rules itself.\n\nInstead of writing a rule to detect spam, we feed an AI 10,000 emails labeled \"spam\" and 10,000 emails labeled \"not spam\". The AI uses complex math (usually Neural Networks) to find invisible mathematical patterns in the text.\n\nOnce it finds the pattern, it can look at a brand new email it has never seen before, and predict with 99% accuracy if it matches the \"spam\" pattern.\n\nAI is not magic. It is just extremely advanced pattern recognition.",
            "instructions": "## Task: Rules vs Patterns\nIdentify which approach belongs to Traditional Programming and which belongs to AI. Set the variables to either 'Traditional' or 'AI'.",
            "starterCode": "writing_if_statements = '___'\nlearning_from_data = '___'\n\nprint(f\"Writing rules is {writing_if_statements}\")\nprint(f\"Finding patterns is {learning_from_data}\")",
            "solution": "writing_if_statements = 'Traditional'\nlearning_from_data = 'AI'\n\nprint(f\"Writing rules is {writing_if_statements}\")\nprint(f\"Finding patterns is {learning_from_data}\")",
            "hint": "Traditional programming uses if/else rules. AI learns from data.",
            "rubric": "Correctly assigns Traditional and AI."
        }
    },
    "generative_theory.json": {
        "course": "Foundations of Generative AI",
        "lesson": {
            "title": "What is Machine Learning?",
            "theory": "## Teaching Computers to Learn\n\n**Artificial Intelligence (AI)** is the broad concept of machines acting smartly. **Machine Learning (ML)** is the specific technique we use to achieve it.\n\nMachine learning is the process of training a computer to perform a task without explicitly programming it to do so.\n\n### The Three Types of Machine Learning\n\n1. **Supervised Learning**: \n   You act as the teacher. You give the computer 1,000 pictures of cats (labeled \"cat\") and 1,000 pictures of dogs (labeled \"dog\"). The computer learns the difference. If you show it a new picture, it can predict which one it is.\n   \n2. **Unsupervised Learning**: \n   You give the computer a massive pile of raw data with no labels. You tell it: \"Sort this into groups.\" It might look at a millions of grocery receipts and discover that people who buy diapers also tend to buy beer on Friday nights. It finds hidden structures.\n\n3. **Reinforcement Learning**: \n   You don't give the computer any data. You drop it into a video game (or a robot body) and give it a goal (e.g., \"Maximize your score\"). When it does something right, you give it a digital \"reward\". When it fails, you punish it. It learns by trial and error over millions of attempts.\n\nMost modern AI (like ChatGPT) is built using a combination of these techniques.",
            "instructions": "## Task: The Three Types\nMatch the scenario to the ML type: `Supervised`, `Unsupervised`, or `Reinforcement`.",
            "starterCode": "learning_by_trial_and_error = '___'\nlearning_from_labeled_examples = '___'\n\nprint(f\"Trial and error is {learning_by_trial_and_error}\")\nprint(f\"Using labels is {learning_from_labeled_examples}\")",
            "solution": "learning_by_trial_and_error = 'Reinforcement'\nlearning_from_labeled_examples = 'Supervised'\n\nprint(f\"Trial and error is {learning_by_trial_and_error}\")\nprint(f\"Using labels is {learning_from_labeled_examples}\")",
            "hint": "Reinforcement is trial/error. Supervised uses teacher labels.",
            "rubric": "Correctly assigns Reinforcement and Supervised."
        }
    },
    "agentic_ai_mcp.json": {
        "course": "Agent Foundations",
        "lesson": {
            "title": "What is Agency?",
            "theory": "## From Assistants to Agents\n\nTo understand \"Agentic AI\", we first have to understand the human concept of **Agency**.\n\nIn sociology and business, Agency is the capacity of an actor to act independently and make their own free choices. \n\n### The Intern vs The Manager\n\nImagine you run a company and you need to research competitors.\n\n**The Non-Agentic approach (The Assistant):**\n- You ask an intern: \"Give me a list of competitors.\"\n- The intern returns with a list.\n- You say: \"Okay, now go find their pricing pages.\"\n- The intern finds the pricing pages.\n- You say: \"Now put this in a spreadsheet.\"\n\nIn this scenario, *you* are doing all the thinking, planning, and managing. The intern is just executing micro-tasks.\n\n**The Agentic approach (The Manager):**\n- You tell a senior manager: \"I need a competitive analysis report on my desk by Friday.\"\n- You walk away.\n- The manager breaks the goal into sub-tasks, delegates the research, creates the spreadsheet, and emails you the final result.\n\nThe manager has **Agency**. They can plan, use tools, recover from errors, and work autonomously toward a high-level goal.\n\nFor the last two years, AI (like ChatGPT) has been the Intern. You have to guide it step-by-step. The entire field of Agentic AI is focused on turning the AI into the Manager.",
            "instructions": "## Task: Who has Agency?\nIdentify which scenario describes an Agent and which describes a standard Assistant.",
            "starterCode": "waits_for_step_by_step_instructions = '___'\nworks_autonomously_toward_a_goal = '___'\n\nprint(f\"Waiting for instructions is an {waits_for_step_by_step_instructions}\")\nprint(f\"Working autonomously is an {works_autonomously_toward_a_goal}\")",
            "solution": "waits_for_step_by_step_instructions = 'Assistant'\nworks_autonomously_toward_a_goal = 'Agent'\n\nprint(f\"Waiting for instructions is an {waits_for_step_by_step_instructions}\")\nprint(f\"Working autonomously is an {works_autonomously_toward_a_goal}\")",
            "hint": "Assistants need steps. Agents act autonomously.",
            "rubric": "Correctly assigns Assistant and Agent."
        }
    },
    "ai_automation.json": {
        "course": "Zapier Basics",
        "lesson": {
            "title": "What is AI Automation?",
            "theory": "## Working Smarter, Not Harder\n\nIn the business world, 80% of office work is incredibly repetitive: copying data from an email into a spreadsheet, moving a file from Slack to Google Drive, or messaging a team when a customer pays an invoice.\n\n**Automation** is the practice of using software to do these repetitive tasks instantly, 24/7, without human intervention.\n\n### Traditional Automation (If This, Then That)\n\nFor years, automation was strictly rules-based. Tools like Zapier allowed non-programmers to set up simple pipelines:\n- **Trigger**: IF a new email arrives with an attachment...\n- **Action**: THEN save the attachment to Google Drive.\n\nThis is powerful, but very fragile. If a customer sends an email *without* an attachment but pastes a Dropbox link instead, the automation breaks because it doesn't understand context.\n\n### The AI Revolution\n\n**AI Automation** injects intelligence into these pipelines. By putting an LLM (like Claude or GPT) in the middle of the pipeline, the automation gains reasoning abilities.\n\nInstead of a rigid rule, the pipeline looks like this:\n- **Trigger**: IF a new email arrives...\n- **AI Step**: Read the email. Determine if the customer is angry, happy, or confused. Extract any action items.\n- **Action**: THEN send a summary to Slack, and tag the appropriate department.\n\nAI turns rigid, fragile pipelines into flexible, intelligent workflows that can handle messy human data.",
            "instructions": "## Task: Rigid vs Intelligent\nSet the variables to identify which approach is 'Traditional' automation and which is 'AI' automation.",
            "starterCode": "breaks_if_format_changes = '___'\ncan_understand_messy_emails = '___'\n\nprint(f\"Breaking easily is {breaks_if_format_changes}\")\nprint(f\"Understanding context is {can_understand_messy_emails}\")",
            "solution": "breaks_if_format_changes = 'Traditional'\ncan_understand_messy_emails = 'AI'\n\nprint(f\"Breaking easily is {breaks_if_format_changes}\")\nprint(f\"Understanding context is {can_understand_messy_emails}\")",
            "hint": "Traditional automation is rigid. AI is flexible.",
            "rubric": "Correctly assigns Traditional and AI."
        }
    }
}

for filename, update_data in new_lessons.items():
    filepath = os.path.join('curriculum', 'tracks', filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: File not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    course_name = update_data['course']
    new_lesson = update_data['lesson']
    
    if course_name in data:
        # Check if we already inserted it
        if data[course_name]['lessons'][0]['title'] != new_lesson['title']:
            data[course_name]['lessons'].insert(0, new_lesson)
            print(f"Added '{new_lesson['title']}' to {course_name} in {filename}")
        else:
            print(f"Lesson already exists in {course_name}")
    else:
        print(f"Course {course_name} not found in {filename}")
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
