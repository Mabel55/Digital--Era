"""
Phase 7: Add 35 new lessons to AI Automation and 35 new lessons to Version Control.
"""
import json

NEW_AUTO_LESSONS = {
    "Intro to AI Automation": [
        {
            "title": "What is Automation?",
            "theory": "## Automation\nAutomation means making a system operate without human intervention. AI automation adds decision-making capabilities to these systems.",
            "instructions": "## Task: Identify Automation\n1. Return True if the task is repetitive and rule-based, and thus a good candidate for automation.",
            "starterCode": "def is_automatable(task_type):\n    if task_type == '___':\n        return True\n    return False",
            "solution": "def is_automatable(task_type):\n    if task_type == 'Repetitive':\n        return True\n    return False",
            "hint": "Task type should be 'Repetitive'.",
            "rubric": "Automation logic implemented correctly."
        },
        {
            "title": "RPA vs AI",
            "theory": "## Robotic Process Automation\nRPA mimics human clicks on a screen. AI can read unstructured text and make decisions. Modern tools combine both.",
            "instructions": "## Task: Distinguish RPA\n1. If the input is 'Screen Click', return 'RPA'. If it's 'Extract intent from email', return 'AI'.",
            "starterCode": "def classify(action):\n    if action == '___': return 'RPA'\n    if action == '___': return 'AI'",
            "solution": "def classify(action):\n    if action == 'Screen Click': return 'RPA'\n    if action == 'Extract intent from email': return 'AI'",
            "hint": "Screen Click vs Extract intent from email.",
            "rubric": "Correctly classified RPA and AI."
        },
        {
            "title": "Triggers and Actions",
            "theory": "## Workflow Components\nEvery automation workflow has a Trigger (what starts it) and one or more Actions (what it does).",
            "instructions": "## Task: Define Workflow\n1. Create a dictionary with a 'trigger' (e.g., 'New Email') and an 'action' (e.g., 'Save Attachment').",
            "starterCode": "workflow = {\n    \"___\": \"New Email\",\n    \"___\": \"Save Attachment\"\n}",
            "solution": "workflow = {\n    \"trigger\": \"New Email\",\n    \"action\": \"Save Attachment\"\n}",
            "hint": "Keys are trigger and action.",
            "rubric": "Workflow components defined."
        },
        {
            "title": "Return on Investment",
            "theory": "## ROI\nAutomation takes time to build. It's only worth it if the time saved over months outweighs the time spent building it.",
            "instructions": "## Task: Calculate Saved Time\n1. If you save 1 hour a week, how many hours do you save in a year (52 weeks)?",
            "starterCode": "hours_saved = 1 * ___",
            "solution": "hours_saved = 1 * 52",
            "hint": "Multiply by 52.",
            "rubric": "Basic ROI calculation is correct."
        }
    ],
    "Python Automation Basics": [
        {
            "title": "OS Module",
            "theory": "## File Operations\nThe `os` module allows you to interact with the operating system, like listing directories or renaming files.",
            "instructions": "## Task: List Files\n1. Import `os`.\n2. Use `os.listdir()` to list files in the current directory ('.').",
            "starterCode": "import ___\nfiles = os.___('.')",
            "solution": "import os\nfiles = os.listdir('.')",
            "hint": "Use os.listdir('.').",
            "rubric": "os.listdir utilized correctly."
        },
        {
            "title": "Shutil Module",
            "theory": "## Moving Files\nWhile `os` can rename, `shutil` is better for copying or moving files between directories.",
            "instructions": "## Task: Move a File\n1. Import `shutil`.\n2. Move 'data.txt' to the 'backup/' folder.",
            "starterCode": "import ___\nshutil.___('___', 'backup/')",
            "solution": "import shutil\nshutil.move('data.txt', 'backup/')",
            "hint": "Use shutil.move.",
            "rubric": "shutil.move executed."
        },
        {
            "title": "Subprocess",
            "theory": "## Running CLI Commands\n`subprocess.run()` lets Python run terminal commands as if a user typed them.",
            "instructions": "## Task: Run echo\n1. Import `subprocess`.\n2. Run `['echo', 'Hello']`.",
            "starterCode": "import ___\nsubprocess.___(['___', 'Hello'])",
            "solution": "import subprocess\nsubprocess.run(['echo', 'Hello'])",
            "hint": "Use subprocess.run.",
            "rubric": "Subprocess run command executed."
        },
        {
            "title": "Time and Sleep",
            "theory": "## Pausing Execution\n`time.sleep(secs)` pauses your script. Useful when waiting for a web page to load or a file to download.",
            "instructions": "## Task: Wait 2 Seconds\n1. Import `time`.\n2. Sleep for 2 seconds.",
            "starterCode": "import ___\ntime.___(___)",
            "solution": "import time\ntime.sleep(2)",
            "hint": "Use time.sleep(2).",
            "rubric": "Sleep applied correctly."
        }
    ],
    "Email & Calendar Automation": [
        {
            "title": "SMTP Protocol",
            "theory": "## Sending Emails\nPython's `smtplib` uses the Simple Mail Transfer Protocol to send emails.",
            "instructions": "## Task: Init SMTP Server\n1. Import `smtplib`.\n2. Connect to `smtp.gmail.com` on port `587`.",
            "starterCode": "import ___\nserver = smtplib.SMTP('___', ___)",
            "solution": "import smtplib\nserver = smtplib.SMTP('smtp.gmail.com', 587)",
            "hint": "Use smtplib.SMTP.",
            "rubric": "SMTP server initialized."
        },
        {
            "title": "Email Messages",
            "theory": "## email.message\nUse `EmailMessage` to cleanly format subjects, senders, and content rather than raw strings.",
            "instructions": "## Task: Create Message\n1. Set the 'Subject' to 'Hello' and the content to 'World'.",
            "starterCode": "from email.message import EmailMessage\nmsg = EmailMessage()\nmsg['___'] = 'Hello'\nmsg.___('World')",
            "solution": "from email.message import EmailMessage\nmsg = EmailMessage()\nmsg['Subject'] = 'Hello'\nmsg.set_content('World')",
            "hint": "Use Subject and set_content.",
            "rubric": "EmailMessage populated correctly."
        },
        {
            "title": "IMAP Protocol",
            "theory": "## Reading Emails\n`imaplib` allows you to connect to an email server and read or search through your inbox.",
            "instructions": "## Task: Connect IMAP\n1. Import `imaplib`.\n2. Connect to `imap.gmail.com` using SSL.",
            "starterCode": "import ___\nmail = imaplib.___('___')",
            "solution": "import imaplib\nmail = imaplib.IMAP4_SSL('imap.gmail.com')",
            "hint": "Use IMAP4_SSL.",
            "rubric": "IMAP SSL connection created."
        },
        {
            "title": "Google Calendar API",
            "theory": "## Calendar Events\nGoogle's API allows creating events. You need credentials and the `google-api-python-client`.",
            "instructions": "## Task: Event Dict\n1. Create a Python dict representing an event with 'summary' and 'start'/'end' times.",
            "starterCode": "event = {\n    '___': 'Meeting',\n    '___': {'dateTime': '2025-01-01T10:00:00-07:00'},\n    '___': {'dateTime': '2025-01-01T11:00:00-07:00'}\n}",
            "solution": "event = {\n    'summary': 'Meeting',\n    'start': {'dateTime': '2025-01-01T10:00:00-07:00'},\n    'end': {'dateTime': '2025-01-01T11:00:00-07:00'}\n}",
            "hint": "Use summary, start, end.",
            "rubric": "Calendar event dictionary formulated."
        }
    ],
    "Web Scraping & Data Extraction": [
        {
            "title": "Requests and HTML",
            "theory": "## Fetching Pages\nBefore scraping, you must download the HTML using the `requests` library.",
            "instructions": "## Task: Fetch HTML\n1. Get `http://example.com` and extract the `.text` property.",
            "starterCode": "import requests\nres = requests.___('http://example.com')\nhtml = res.___",
            "solution": "import requests\nres = requests.get('http://example.com')\nhtml = res.text",
            "hint": "Use get() and .text.",
            "rubric": "HTML text fetched successfully."
        },
        {
            "title": "BeautifulSoup",
            "theory": "## Parsing HTML\nBeautifulSoup makes it easy to find tags and extract data from messy HTML strings.",
            "instructions": "## Task: Find all Links\n1. Import `BeautifulSoup`.\n2. Parse `html` with `html.parser`.\n3. Find all `<a>` tags.",
            "starterCode": "from bs4 import ___\nsoup = ___(html, '___')\nlinks = soup.___('___')",
            "solution": "from bs4 import BeautifulSoup\nsoup = BeautifulSoup(html, 'html.parser')\nlinks = soup.find_all('a')",
            "hint": "Use BeautifulSoup, html.parser, find_all('a').",
            "rubric": "BeautifulSoup parsing utilized properly."
        },
        {
            "title": "Extracting Attributes",
            "theory": "## Tag Attributes\nOnce you have a BeautifulSoup tag, you can access attributes like `href` or `src` like a dictionary.",
            "instructions": "## Task: Get URL\n1. Get the `href` attribute from the `link` tag.",
            "starterCode": "url = link['___']",
            "solution": "url = link['href']",
            "hint": "Use ['href'].",
            "rubric": "Href attribute extracted."
        },
        {
            "title": "Selenium Basics",
            "theory": "## Browser Automation\nIf a site uses JavaScript to load data, BeautifulSoup won't see it. Selenium opens a real browser.",
            "instructions": "## Task: Open URL\n1. Assuming `driver` is a Selenium WebDriver, navigate to `http://example.com`.",
            "starterCode": "driver.___('http://example.com')",
            "solution": "driver.get('http://example.com')",
            "hint": "Use driver.get().",
            "rubric": "Selenium driver.get executed."
        }
    ],
    "API Automation with Python": [
        {
            "title": "API Keys and Headers",
            "theory": "## Authentication\nMost APIs require a key sent in the headers. Often `Authorization: Bearer <token>`.",
            "instructions": "## Task: Set Headers\n1. Create a headers dictionary with the Authorization Bearer token.",
            "starterCode": "headers = {\"___\": f\"___ {api_key}\"}",
            "solution": "headers = {\"Authorization\": f\"Bearer {api_key}\"}",
            "hint": "Authorization and Bearer.",
            "rubric": "Auth header constructed correctly."
        },
        {
            "title": "Pagination",
            "theory": "## Iterating Pages\nAPIs rarely return all data at once. They paginate. You often need to loop and pass a `page` or `offset` parameter.",
            "instructions": "## Task: Loop 3 Pages\n1. Write a loop from 1 to 3.\n2. Pass the page number in the `params` dict to `requests.get`.",
            "starterCode": "for i in range(1, ___):\n    res = requests.get(url, ___={'page': ___})",
            "solution": "for i in range(1, 4):\n    res = requests.get(url, params={'page': i})",
            "hint": "range(1, 4) and params.",
            "rubric": "Pagination loop correctly logic applied."
        },
        {
            "title": "Handling Rate Limits",
            "theory": "## HTTP 429\nIf you hit an API too fast, it returns 429 Too Many Requests. You must catch this and `time.sleep()`.",
            "instructions": "## Task: Backoff\n1. Check if `res.status_code` is 429.\n2. If so, print 'Rate limited' and sleep 5 seconds.",
            "starterCode": "if res.___ == ___:\n    print('Rate limited')\n    time.___(___)",
            "solution": "if res.status_code == 429:\n    print('Rate limited')\n    time.sleep(5)",
            "hint": "status_code == 429 and sleep(5).",
            "rubric": "Rate limit backoff logic implemented."
        },
        {
            "title": "Webhooks",
            "theory": "## Push vs Pull\nInstead of polling (pulling) an API every minute, a Webhook lets the service push data to your server via HTTP POST when an event happens.",
            "instructions": "## Task: Receive Webhook\n1. In a Flask route, read the incoming JSON data using `request.json`.",
            "starterCode": "from flask import request\n@app.route('/webhook', methods=['___'])\ndef hook():\n    data = request.___\n    return 'OK'",
            "solution": "from flask import request\n@app.route('/webhook', methods=['POST'])\ndef hook():\n    data = request.json\n    return 'OK'",
            "hint": "Use POST and request.json.",
            "rubric": "Webhook endpoint logic formulated."
        }
    ],
    "AI-Powered Bots": [
        {
            "title": "Discord Bots",
            "theory": "## discord.py\nThe `discord.py` library allows you to create bots. Use the `@bot.command()` decorator.",
            "instructions": "## Task: Ping Command\n1. Create a `ping` command that replies with 'Pong!'.",
            "starterCode": "@bot.___()\nasync def ping(ctx):\n    await ctx.___('___')",
            "solution": "@bot.command()\nasync def ping(ctx):\n    await ctx.send('Pong!')",
            "hint": "Use @bot.command() and ctx.send().",
            "rubric": "Discord bot command structured correctly."
        },
        {
            "title": "Slack Bots",
            "theory": "## Bolt for Python\nSlack provides the `bolt-python` framework to build apps listening to events.",
            "instructions": "## Task: Listen to Messages\n1. Use `@app.message` to listen for 'hello'.\n2. Reply using `say()`.",
            "starterCode": "@app.___(\"hello\")\ndef handle_hello(message, ___):\n    ___(f\"Hi <@{message['user']}>\")",
            "solution": "@app.message(\"hello\")\ndef handle_hello(message, say):\n    say(f\"Hi <@{message['user']}>\")",
            "hint": "Use @app.message and the say function.",
            "rubric": "Slack bot message listener implemented."
        },
        {
            "title": "Connecting LLMs to Bots",
            "theory": "## AI Responses\nInstead of hardcoding 'Pong', pass the user's message to OpenAI and return the AI's response.",
            "instructions": "## Task: Generate Reply\n1. Pass `user_msg` to an `ai_generate` function and await the result before sending.",
            "starterCode": "async def reply(ctx, user_msg):\n    ai_text = ___ ai_generate(___)\n    await ctx.send(___)",
            "solution": "async def reply(ctx, user_msg):\n    ai_text = await ai_generate(user_msg)\n    await ctx.send(ai_text)",
            "hint": "await the ai_generate call.",
            "rubric": "LLM integrated into bot reply sequence."
        }
    ],
    "Visual Workflow Platforms": [
        {
            "title": "Zapier Basics",
            "theory": "## No-Code Automation\nZapier connects apps using \"Zaps\". A Zap consists of a Trigger (e.g., New Typeform Entry) and Actions (e.g., Send Slack Message).",
            "instructions": "## Task: Map Zapier Terms\n1. A 'Trigger' starts the workflow. An 'Action' executes a step.",
            "starterCode": "start_event = '___'\nexecution_step = '___'",
            "solution": "start_event = 'Trigger'\nexecution_step = 'Action'",
            "hint": "Trigger and Action.",
            "rubric": "No-code workflow terms mapped."
        },
        {
            "title": "Make (Integromat)",
            "theory": "## Scenarios\nMake (formerly Integromat) uses visual 'Scenarios' with circular modules linked together, allowing complex branching.",
            "instructions": "## Task: Routing\n1. In Make, a 'Router' splits the flow into multiple paths.",
            "starterCode": "branching_module = '___'",
            "solution": "branching_module = 'Router'",
            "hint": "Router.",
            "rubric": "Make.com router concept identified."
        },
        {
            "title": "n8n",
            "theory": "## Fair-code Automation\nn8n is a node-based workflow tool you can self-host. It's heavily favored by developers because you can write JavaScript inside nodes.",
            "instructions": "## Task: Identify n8n feature\n1. n8n allows you to write custom code in nodes. What language?",
            "starterCode": "language = '___'",
            "solution": "language = 'JavaScript'",
            "hint": "JavaScript.",
            "rubric": "n8n scripting language identified."
        }
    ],
    "LLM Workflow Automation": [
        {
            "title": "Structuring Prompts in Workflows",
            "theory": "## Context Injection\nIn an automated workflow (like n8n), you pass previous node data into the prompt as variables.",
            "instructions": "## Task: Inject Variable\n1. Use an f-string to inject `email_body` into the prompt.",
            "starterCode": "prompt = f\"Summarize this email: {___}\"",
            "solution": "prompt = f\"Summarize this email: {email_body}\"",
            "hint": "Use {email_body}.",
            "rubric": "Variable injected into prompt."
        },
        {
            "title": "JSON Outputs",
            "theory": "## Structured Data\nFor the next step in the automation to work, the LLM must output clean JSON, not conversational text.",
            "instructions": "## Task: Parse JSON\n1. Import json and parse the `llm_output_string`.",
            "starterCode": "import ___\ndata = json.___(___)",
            "solution": "import json\ndata = json.loads(llm_output_string)",
            "hint": "Use json.loads().",
            "rubric": "LLM string output parsed to JSON."
        },
        {
            "title": "Error Handling LLMs",
            "theory": "## Retries\nSometimes the LLM outputs malformed JSON. You should catch the error and retry.",
            "instructions": "## Task: Try/Except\n1. Wrap the `json.loads` in a try block. If it fails with `JSONDecodeError`, print 'Failed'.",
            "starterCode": "___:\n    data = json.loads(text)\n___ json.decoder.JSONDecodeError:\n    print('___')",
            "solution": "try:\n    data = json.loads(text)\nexcept json.decoder.JSONDecodeError:\n    print('Failed')",
            "hint": "Use try, except, and print 'Failed'.",
            "rubric": "Error handling implemented for JSON decoding."
        }
    ],
    "Document Processing with AI": [
        {
            "title": "OCR Basics",
            "theory": "## Optical Character Recognition\nOCR extracts text from images/PDFs. `pytesseract` is a popular Python wrapper for Google's Tesseract engine.",
            "instructions": "## Task: Extract Text\n1. Use `pytesseract.image_to_string()` on the `image` variable.",
            "starterCode": "import pytesseract\ntext = pytesseract.___(___)",
            "solution": "import pytesseract\ntext = pytesseract.image_to_string(image)",
            "hint": "Use image_to_string(image).",
            "rubric": "OCR library invoked correctly."
        },
        {
            "title": "PDF Parsing",
            "theory": "## PyPDF2 / pdfplumber\nFor native text PDFs (not scanned images), use libraries like `pdfplumber` to extract text directly without OCR.",
            "instructions": "## Task: Read Page\n1. Assuming `pdf` is an opened pdfplumber object, extract text from the first page.",
            "starterCode": "first_page = pdf.pages[___]\ntext = first_page.___()",
            "solution": "first_page = pdf.pages[0]\ntext = first_page.extract_text()",
            "hint": "Use index 0 and .extract_text().",
            "rubric": "PDF text extracted using pdfplumber."
        },
        {
            "title": "Entity Extraction with LLMs",
            "theory": "## Unstructured to Structured\nPass the raw OCR/PDF text to an LLM to extract specific fields like 'Invoice Number' or 'Total'.",
            "instructions": "## Task: Prompt for Invoice\n1. Ask the model to extract 'Total Amount' from `raw_text`.",
            "starterCode": "prompt = f\"Extract the ___ from this invoice text: {___}\"",
            "solution": "prompt = f\"Extract the Total Amount from this invoice text: {raw_text}\"",
            "hint": "Total Amount, raw_text.",
            "rubric": "Extraction prompt tailored for invoices."
        }
    ],
    "Scheduling & Task Automation": [
        {
            "title": "Cron Expressions",
            "theory": "## Cron\nCron uses 5 fields: Minute, Hour, Day of Month, Month, Day of Week. `* * * * *` means every minute.",
            "instructions": "## Task: Daily at Midnight\n1. Write a cron expression for minute 0, hour 0, every day, month, and weekday.",
            "starterCode": "cron = \"___ ___ * * *\"",
            "solution": "cron = \"0 0 * * *\"",
            "hint": "0 0 * * *",
            "rubric": "Cron expression correctly formatted for midnight."
        },
        {
            "title": "Schedule Library",
            "theory": "## Python Schedule\nThe `schedule` library is an easier, human-readable way to run periodic tasks in Python.",
            "instructions": "## Task: Run Daily\n1. Use `schedule.every().day.at(\"10:30\").do(job)`.",
            "starterCode": "import schedule\nschedule.___().___.___(\"10:30\").___(job)",
            "solution": "import schedule\nschedule.every().day.at(\"10:30\").do(job)",
            "hint": "every().day.at().do()",
            "rubric": "Schedule library utilized for daily task."
        },
        {
            "title": "Background Tasks",
            "theory": "## Celery\nFor heavy web apps, don't block the main thread. Send long tasks (like sending 100 emails) to a background worker like Celery.",
            "instructions": "## Task: Delay Task\n1. Instead of calling `send_email()`, call `send_email.delay()` to push it to Celery.",
            "starterCode": "# Normal: send_email()\n# Celery: \nsend_email.___()",
            "solution": "# Normal: send_email()\n# Celery: \nsend_email.delay()",
            "hint": "Use .delay().",
            "rubric": "Celery delay method applied."
        }
    ]
}

NEW_VC_LESSONS = {
    "Git Fundamentals": [
        {
            "title": "What is Version Control?",
            "theory": "## Tracking Changes\nVersion control systems (VCS) record changes to a file or set of files over time so you can recall specific versions later.",
            "instructions": "## Task: Identify VCS\n1. Return True if Git is a distributed VCS.",
            "starterCode": "is_git_distributed = ___",
            "solution": "is_git_distributed = True",
            "hint": "Set to True.",
            "rubric": "Git architecture concept identified."
        },
        {
            "title": "Initializing a Repository",
            "theory": "## git init\nTo track a project with Git, you must initialize it. This creates a hidden `.git` folder.",
            "instructions": "## Task: Run Init\n1. Provide the command to initialize an empty Git repository.",
            "starterCode": "git ___",
            "solution": "git init",
            "hint": "init",
            "rubric": "git init command specified."
        },
        {
            "title": "The Staging Area",
            "theory": "## git add\nGit has three states: Modified, Staged, and Committed. You use `git add` to move files to the staging area.",
            "instructions": "## Task: Stage a File\n1. Provide the command to stage `main.py`.",
            "starterCode": "git ___ ___",
            "solution": "git add main.py",
            "hint": "add main.py",
            "rubric": "git add command specified."
        }
    ],
    "Commits & History": [
        {
            "title": "Making a Commit",
            "theory": "## git commit\nA commit permanently stores the staged changes in the Git directory. Always include a descriptive message using `-m`.",
            "instructions": "## Task: Commit Changes\n1. Provide the command to commit with the message \"Fix typo\".",
            "starterCode": "git ___ ___ \"___\"",
            "solution": "git commit -m \"Fix typo\"",
            "hint": "commit -m \"Fix typo\"",
            "rubric": "git commit command properly formatted."
        },
        {
            "title": "Viewing History",
            "theory": "## git log\nTo see the history of commits, use `git log`.",
            "instructions": "## Task: View Log\n1. Provide the command to view the commit history.",
            "starterCode": "git ___",
            "solution": "git log",
            "hint": "log",
            "rubric": "git log command specified."
        },
        {
            "title": "Checking Status",
            "theory": "## git status\n`git status` shows which files are modified and which are staged.",
            "instructions": "## Task: Check Status\n1. Provide the command to check the current state of the working tree.",
            "starterCode": "git ___",
            "solution": "git status",
            "hint": "status",
            "rubric": "git status command specified."
        }
    ],
    "Branching Basics": [
        {
            "title": "Creating Branches",
            "theory": "## git branch\nBranches allow you to diverge from the main line of development to work on features safely.",
            "instructions": "## Task: Create Branch\n1. Provide the command to create a new branch named `feature-x`.",
            "starterCode": "git ___ ___",
            "solution": "git branch feature-x",
            "hint": "branch feature-x",
            "rubric": "git branch command specified."
        },
        {
            "title": "Switching Branches",
            "theory": "## git checkout / switch\nTo start working on a different branch, you switch to it. `git checkout` or `git switch`.",
            "instructions": "## Task: Switch Branch\n1. Provide the command to switch to `feature-x`.",
            "starterCode": "git ___ ___",
            "solution": "git switch feature-x",
            "hint": "switch feature-x",
            "rubric": "git switch command specified."
        },
        {
            "title": "Create and Switch",
            "theory": "## git checkout -b\nYou can create and switch to a branch in one step.",
            "instructions": "## Task: Create & Switch\n1. Provide the command to create and switch to `bugfix`.",
            "starterCode": "git checkout ___ ___",
            "solution": "git checkout -b bugfix",
            "hint": "checkout -b bugfix",
            "rubric": "git checkout -b command utilized."
        }
    ],
    "GitHub Essentials": [
        {
            "title": "Adding Remotes",
            "theory": "## git remote add\nTo push code to GitHub, you add a remote URL (usually named 'origin').",
            "instructions": "## Task: Add Remote\n1. Add a remote named `origin` pointing to `https://github.com/user/repo.git`.",
            "starterCode": "git ___ ___ ___ https://github.com/user/repo.git",
            "solution": "git remote add origin https://github.com/user/repo.git",
            "hint": "remote add origin",
            "rubric": "git remote add command specified."
        },
        {
            "title": "Pushing Code",
            "theory": "## git push\nPushing sends your local commits to the remote repository.",
            "instructions": "## Task: Push Main\n1. Push the `main` branch to the `origin` remote.",
            "starterCode": "git ___ ___ ___",
            "solution": "git push origin main",
            "hint": "push origin main",
            "rubric": "git push command specified."
        },
        {
            "title": "Cloning Repos",
            "theory": "## git clone\nCloning downloads a full copy of a remote repository to your local machine.",
            "instructions": "## Task: Clone Repo\n1. Clone the repo at `https://github.com/user/repo.git`.",
            "starterCode": "git ___ https://github.com/user/repo.git",
            "solution": "git clone https://github.com/user/repo.git",
            "hint": "clone",
            "rubric": "git clone command specified."
        }
    ],
    "Collaborative Workflows": [
        {
            "title": "Fetching Updates",
            "theory": "## git fetch\nFetching downloads updates from the remote, but does not merge them into your working files.",
            "instructions": "## Task: Fetch Origin\n1. Fetch updates from the `origin` remote.",
            "starterCode": "git ___ ___",
            "solution": "git fetch origin",
            "hint": "fetch origin",
            "rubric": "git fetch command specified."
        },
        {
            "title": "Pulling Updates",
            "theory": "## git pull\nPulling is effectively `git fetch` followed immediately by `git merge`. It updates your current branch.",
            "instructions": "## Task: Pull Code\n1. Pull updates from `origin` into your current branch.",
            "starterCode": "git ___ ___",
            "solution": "git pull origin",
            "hint": "pull origin",
            "rubric": "git pull command specified."
        },
        {
            "title": "Merge Conflicts",
            "theory": "## Conflicts\nIf two people edit the same lines, Git pauses the merge and asks you to manually resolve the conflict.",
            "instructions": "## Task: Resolve Status\n1. After fixing a conflict in a file, what command do you run to mark it resolved before committing?",
            "starterCode": "git ___ <filename>",
            "solution": "git add <filename>",
            "hint": "add",
            "rubric": "git add used for conflict resolution."
        }
    ],
    "Merging & Rebasing": [
        {
            "title": "git merge",
            "theory": "## Merging\nMerging takes the contents of a source branch and integrates them into a target branch, creating a new merge commit.",
            "instructions": "## Task: Merge Feature\n1. While on `main`, merge the `feature-x` branch into it.",
            "starterCode": "git ___ ___",
            "solution": "git merge feature-x",
            "hint": "merge feature-x",
            "rubric": "git merge command specified."
        },
        {
            "title": "git rebase",
            "theory": "## Rebasing\nRebasing rewrites history by moving your branch's starting point to the tip of the target branch, resulting in a linear history.",
            "instructions": "## Task: Rebase onto Main\n1. While on your feature branch, rebase it onto `main`.",
            "starterCode": "git ___ ___",
            "solution": "git rebase main",
            "hint": "rebase main",
            "rubric": "git rebase command specified."
        },
        {
            "title": "Force Pushing",
            "theory": "## git push --force\nBecause rebasing rewrites history, pushing that branch to a remote usually requires a force push. Be careful!",
            "instructions": "## Task: Force Push\n1. Force push your current branch to origin.",
            "starterCode": "git push ___ ___",
            "solution": "git push origin --force",
            "hint": "origin --force",
            "rubric": "git push --force command utilized."
        }
    ],
    "Pull Requests & Code Review": [
        {
            "title": "What is a PR?",
            "theory": "## Pull Requests\nA PR is a request to merge your pushed branch into another branch (usually main), providing a space for code review on platforms like GitHub.",
            "instructions": "## Task: PR Purpose\n1. True or False: PRs are a native Git feature, not just a GitHub/GitLab feature.",
            "starterCode": "is_native_git = ___",
            "solution": "is_native_git = False",
            "hint": "False. Git only has branches. GitHub adds PRs.",
            "rubric": "PR concept identified correctly."
        },
        {
            "title": "Code Reviews",
            "theory": "## Approvals\nBefore merging, peers review the code for bugs or style issues. If changes are needed, you add commits to the PR branch.",
            "instructions": "## Task: Update PR\n1. If a reviewer asks for a change, do you close the PR and open a new one? (True/False)",
            "starterCode": "open_new_pr = ___",
            "solution": "open_new_pr = False",
            "hint": "False. Just push new commits to the same branch.",
            "rubric": "PR workflow understood."
        },
        {
            "title": "Squash and Merge",
            "theory": "## Squashing\nSquash and Merge takes all commits in a PR and squashes them into a single commit on the main branch, keeping history clean.",
            "instructions": "## Task: Squashing effect\n1. If a PR has 5 commits, how many commits are added to `main` when using Squash and Merge?",
            "starterCode": "commits_added = ___",
            "solution": "commits_added = 1",
            "hint": "1",
            "rubric": "Squash concept understood."
        }
    ],
    "Tags & Releases": [
        {
            "title": "Creating Tags",
            "theory": "## git tag\nTags are used to mark specific points in history as important. Typically used for release versions (e.g., v1.0.0).",
            "instructions": "## Task: Tag Version\n1. Create a lightweight tag named `v1.0.0`.",
            "starterCode": "git ___ ___",
            "solution": "git tag v1.0.0",
            "hint": "tag v1.0.0",
            "rubric": "git tag command specified."
        },
        {
            "title": "Pushing Tags",
            "theory": "## git push --tags\nBy default, `git push` does not transfer tags to remote servers. You must push them explicitly.",
            "instructions": "## Task: Push All Tags\n1. Provide the command to push all tags to origin.",
            "starterCode": "git push ___ ___",
            "solution": "git push origin --tags",
            "hint": "origin --tags",
            "rubric": "git push --tags command specified."
        }
    ],
    "Undoing Changes": [
        {
            "title": "Reverting Commits",
            "theory": "## git revert\n`git revert` creates a *new* commit that undoes the changes of a previous commit. This is safe for public history.",
            "instructions": "## Task: Revert HEAD\n1. Revert the last commit (HEAD).",
            "starterCode": "git ___ ___",
            "solution": "git revert HEAD",
            "hint": "revert HEAD",
            "rubric": "git revert command specified."
        },
        {
            "title": "Resetting Commits",
            "theory": "## git reset\n`git reset` moves the branch pointer backward. `--hard` wipes the changes. Never do this on pushed public commits.",
            "instructions": "## Task: Hard Reset\n1. Hard reset to the previous commit (HEAD~1).",
            "starterCode": "git reset ___ ___",
            "solution": "git reset --hard HEAD~1",
            "hint": "--hard HEAD~1",
            "rubric": "git reset --hard command specified."
        }
    ],
    "Git Internals": [
        {
            "title": "The .git Directory",
            "theory": "## Under the Hood\nGit stores all its objects (commits, trees, blobs) inside the hidden `.git` folder.",
            "instructions": "## Task: Object Types\n1. Which object type stores file contents: 'blob' or 'tree'?",
            "starterCode": "file_contents_object = '___'",
            "solution": "file_contents_object = 'blob'",
            "hint": "blob",
            "rubric": "Git blob internal object identified."
        },
        {
            "title": "SHA-1 Hashes",
            "theory": "## Checksums\nEvery object in Git is checksummed with a 40-character SHA-1 hash. This ensures data integrity.",
            "instructions": "## Task: Hash Length\n1. Set the integer length of a Git SHA-1 hash.",
            "starterCode": "hash_length = ___",
            "solution": "hash_length = 40",
            "hint": "40",
            "rubric": "SHA-1 hash length identified."
        }
    ],
    "CI/CD with GitHub Actions": [
        {
            "title": "Workflows",
            "theory": "## GitHub Actions\nWorkflows are defined in YAML files placed in the `.github/workflows` directory of your repository.",
            "instructions": "## Task: Workflow Directory\n1. Provide the directory path where GitHub Actions looks for workflows.",
            "starterCode": "path = \"___\"",
            "solution": "path = \".github/workflows\"",
            "hint": ".github/workflows",
            "rubric": "GitHub actions directory identified."
        },
        {
            "title": "Triggers",
            "theory": "## on:\nWorkflows run based on triggers, such as pushing code or opening a pull request.",
            "instructions": "## Task: Push Trigger\n1. In YAML syntax, trigger the workflow `on: push`.",
            "starterCode": "___: ___",
            "solution": "on: push",
            "hint": "on: push",
            "rubric": "Workflow trigger defined."
        }
    ],
    "Monorepo Strategies": [
        {
            "title": "What is a Monorepo?",
            "theory": "## Multiple Projects, One Repo\nA monorepo stores code for multiple projects (like frontend and backend) in a single repository.",
            "instructions": "## Task: Monorepo truth\n1. True or False: In a monorepo, everything must be deployed together.",
            "starterCode": "must_deploy_together = ___",
            "solution": "must_deploy_together = False",
            "hint": "False. You can deploy services independently.",
            "rubric": "Monorepo concept understood."
        },
        {
            "title": "Sparse Checkout",
            "theory": "## git sparse-checkout\nIf a monorepo is huge, you can use sparse-checkout to only download the directories you need to work on.",
            "instructions": "## Task: Sparse Concept\n1. Does sparse-checkout reduce the disk space used locally? (True/False)",
            "starterCode": "reduces_disk_space = ___",
            "solution": "reduces_disk_space = True",
            "hint": "True.",
            "rubric": "Sparse checkout benefit understood."
        }
    ],
    "Advanced Git Workflows": [
        {
            "title": "Git Flow",
            "theory": "## Branching Models\nGit Flow uses strict branches: `main` (production), `develop` (next release), and ephemeral `feature` branches.",
            "instructions": "## Task: Develop Branch\n1. In Git Flow, which branch serves as the integration branch for features?",
            "starterCode": "integration_branch = '___'",
            "solution": "integration_branch = 'develop'",
            "hint": "develop",
            "rubric": "Git Flow develop branch identified."
        },
        {
            "title": "Trunk-Based Development",
            "theory": "## TBD\nDevelopers merge small, frequent updates directly to `main` (the trunk) rather than maintaining long-lived feature branches.",
            "instructions": "## Task: TBD Target\n1. In TBD, what is the target branch for daily merges?",
            "starterCode": "target_branch = '___'",
            "solution": "target_branch = 'main'",
            "hint": "main",
            "rubric": "Trunk-Based Development concept identified."
        }
    ],
    "Git for Teams": [
        {
            "title": "Branch Protection",
            "theory": "## GitHub Rules\nBranch protection rules prevent direct pushes to `main` and require approved pull requests and passing CI checks.",
            "instructions": "## Task: Direct Pushes\n1. Can you force push to a protected branch? (True/False)",
            "starterCode": "can_force_push = ___",
            "solution": "can_force_push = False",
            "hint": "False.",
            "rubric": "Branch protection rule understood."
        },
        {
            "title": "CODEOWNERS",
            "theory": "## Auto-Reviewers\nA `CODEOWNERS` file automatically assigns PR reviewers based on which files were modified.",
            "instructions": "## Task: Backend Owner\n1. In a CODEOWNERS file, assign `/backend/` to `@alice`.",
            "starterCode": "/___/ @___",
            "solution": "/backend/ @alice",
            "hint": "/backend/ @alice",
            "rubric": "CODEOWNERS syntax applied."
        }
    ]
}

def add_lessons(track_file, new_lessons_dict):
    with open(track_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    added = 0
    for course_name, new_lessons in new_lessons_dict.items():
        if course_name in data:
            data[course_name]["lessons"].extend(new_lessons)
            added += len(new_lessons)
            print(f"[OK] {course_name}: +{len(new_lessons)} lessons")
        else:
            print(f"[WARN] Course not found: {course_name}")
    
    with open(track_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\\nDone! Added {added} new lessons to {track_file}")

if __name__ == "__main__":
    print("--- Updating AI Automation ---")
    add_lessons("curriculum/tracks/ai_automation.json", NEW_AUTO_LESSONS)
    print("\\n--- Updating Version Control ---")
    add_lessons("curriculum/tracks/version_control.json", NEW_VC_LESSONS)
