import json
import os

new_lessons = [
    {
        "title": "Servers & Clients",
        "theory": "## How Devices Talk to Each Other\n\nIn our restaurant analogy, you learned that the browser is the customer (Client) and the backend is the kitchen (Server). Let's explore how they actually communicate.\n\n### The Client\n\nA **Client** is any device or software that *requests* information. \n- When you open the Netflix app on your TV, your TV is the Client.\n- When you check your email on your phone, your phone is the Client.\n- When you type `google.com` into Chrome, Chrome is the Client.\n\n### The Server\n\nA **Server** is just a computer that is turned on 24/7, waiting to *serve* information when requested.\n- Netflix's servers hold all the movies.\n- Google's servers hold the search results.\n\nServers don't usually have screens or keyboards. They sit in massive, climate-controlled warehouses called Data Centers. When your Client asks for a movie, the Server finds it and sends it across the internet cables back to your house.\n\n### The Conversation\n\nThis entire interaction is a strict two-step process:\n1. The Client sends a **Request** (\"I want to see my emails\").\n2. The Server sends a **Response** (\"Here is a list of your emails\").\n\nThe server *never* talks unless it is spoken to first. It just waits for requests.",
        "instructions": "## Task: The Conversation\nMatch the action to whether it is a `Request` or a `Response`.",
        "starterCode": "clicking_a_link = '___'\nreceiving_a_webpage = '___'\n\nprint(f\"Clicking a link sends a {clicking_a_link}\")\nprint(f\"The server sends back a {receiving_a_webpage}\")",
        "solution": "clicking_a_link = 'Request'\nreceiving_a_webpage = 'Response'\n\nprint(f\"Clicking a link sends a {clicking_a_link}\")\nprint(f\"The server sends back a {receiving_a_webpage}\")",
        "hint": "Clients Request, Servers Respond.",
        "rubric": "Correctly assigns Request and Response."
    },
    {
        "title": "IP Addresses",
        "theory": "## Addressing the Internet\n\nIf you want to send a physical letter to a friend, you need their street address. Without an address, the post office has no idea where to deliver the letter.\n\nThe internet works the exact same way.\n\n### What is an IP Address?\n\nEvery single device connected to the internet (your phone, your laptop, your smart fridge, and every server in the world) is assigned a unique number called an **IP Address** (Internet Protocol Address).\n\nWhen your phone (Client) wants to talk to a Server, it essentially writes a digital letter, puts the Server's IP Address on the envelope, and sends it into the internet.\n\n### IPv4 (The Classic Address)\n\nThe most common format is called IPv4. It looks like four numbers separated by dots, where each number is between 0 and 255.\n\nExamples:\n- `192.168.1.1` (Your home Wi-Fi router)\n- `142.250.190.46` (One of Google's servers)\n- `8.8.8.8` (A famous Google DNS server)\n\n### Public vs Private IPs\n\nYour laptop has a **Private IP Address** that only devices inside your house can see. Your internet router has a **Public IP Address** that the whole world can see. Servers always have Public IP Addresses so that anyone on the internet can find them.",
        "instructions": "## Task: Identify the IP\nLook at the list of strings below. Only one of them is a valid IPv4 address. Assign it to the variable `valid_ip`.",
        "starterCode": "options = [\n    '300.1.2.3',     # Numbers can't be over 255\n    '192.168.0',     # Needs 4 numbers\n    '172.16.254.1',  # ???\n    '192-168-1-1'    # Uses dashes instead of dots\n]\n\nvalid_ip = '___'\nprint(f\"The valid IP address is {valid_ip}\")",
        "solution": "valid_ip = '172.16.254.1'\nprint(f\"The valid IP address is {valid_ip}\")",
        "hint": "It needs 4 numbers separated by dots, and no number can be greater than 255.",
        "rubric": "Correctly assigns the valid IP."
    },
    {
        "title": "DNS (The Phonebook)",
        "theory": "## Translating Names to Numbers\n\nIn the previous lesson, we learned that computers talk to each other using IP Addresses like `142.250.190.46`.\n\nBut as a human, when you want to search for something, you don't type `142.250.190.46` into your browser. You type `google.com`. How does that work?\n\n### The Domain Name System (DNS)\n\nHumans are bad at remembering numbers, but good at remembering words. Computers are the exact opposite.\n\nTo solve this, we invented **DNS** (Domain Name System). DNS is literally just a massive phonebook for the internet.\n\n### How it works:\n\n1. You type `facebook.com` into your browser.\n2. Before doing anything else, your browser contacts a DNS Server and asks: *\"Excuse me, what is the IP Address for facebook.com?\"*\n3. The DNS Server looks up the name in its phonebook and replies: *\"It is 157.240.22.35\"*\n4. Now your browser sends the actual Request directly to `157.240.22.35`.\n\nAll of this happens in milliseconds, completely invisibly to you.\n\n### Buying a Domain\n\nWhen a Backend Developer builds a website and puts it on a Server, it only has an IP Address. They have to go to a company like GoDaddy or Namecheap, pay $10 to buy a \"Domain Name\" (like `mycoolwebsite.com`), and tell the global DNS phonebook to point that name to their Server's IP Address.",
        "instructions": "## Task: The Phonebook Check\nMatch the concept to the correct term. Is it a `Domain Name` or an `IP Address`?",
        "starterCode": "google_com = '___'\nnumber_string = '___'\n\nprint(f\"google.com is a {google_com}\")\nprint(f\"142.250.190.46 is an {number_string}\")",
        "solution": "google_com = 'Domain Name'\nnumber_string = 'IP Address'\n\nprint(f\"google.com is a {google_com}\")\nprint(f\"142.250.190.46 is an {number_string}\")",
        "hint": "Words are Domain Names. Numbers are IP Addresses.",
        "rubric": "Correctly assigns Domain Name and IP Address."
    },
    {
        "title": "Ports (Doors to the Server)",
        "theory": "## Finding the Right Room\n\nSo far, we know that an IP Address gets your Request to the correct Server building. But a Server is a powerful computer that can run many different programs at the same time.\n\nHow does the Server know which program your Request is for?\n\n### What is a Port?\n\nIf an IP Address is the street address of a massive apartment building, a **Port** is the specific apartment number.\n\nWhen a Request arrives at the Server, it goes to a specific Port number (from 0 to 65,535). Different programs \"listen\" on different doors.\n\n### The Standard Ports\n\nOver the decades, the internet agreed on some standard apartment numbers so everyone knows where to go:\n\n- **Port 80 (HTTP)**: This is the standard door for unencrypted web traffic.\n- **Port 443 (HTTPS)**: This is the standard door for secure, encrypted web traffic. Almost all modern websites use this.\n- **Port 25 (SMTP)**: This door handles sending Emails.\n- **Port 22 (SSH)**: This door allows developers to remotely log into the server to fix things.\n\n### URLs hide the Port\n\nWhen you type `https://github.com`, your browser is secretly adding `:443` to the end because you used `https`. The full request is actually going to `140.82.113.3:443`. \n\nWhen you build your own backend servers locally on your laptop, you will often use \"development ports\" like `3000` or `8000` (e.g., `http://localhost:3000`).",
        "instructions": "## Task: Which Door?\nMatch the port number to its common usage: `HTTP`, `HTTPS`, or `Email`.",
        "starterCode": "port_80 = '___'\nport_443 = '___'\nport_25 = '___'\n\nprint(f\"Port 80 is for {port_80}\")\nprint(f\"Port 443 is for {port_443}\")\nprint(f\"Port 25 is for {port_25}\")",
        "solution": "port_80 = 'HTTP'\nport_443 = 'HTTPS'\nport_25 = 'Email'\n\nprint(f\"Port 80 is for {port_80}\")\nprint(f\"Port 443 is for {port_443}\")\nprint(f\"Port 25 is for {port_25}\")",
        "hint": "80 is HTTP, 443 is the secure version (HTTPS), 25 is for SMTP (Email).",
        "rubric": "Matches the 3 ports correctly."
    },
    {
        "title": "Databases vs Files",
        "theory": "## Where does the data go?\n\nNow we know how the Client talks to the Server (The Backend). But what happens when you create an account on a website? Where does the Backend save your username and password?\n\n### The Simple Way: A Text File\n\nTechnically, a Backend developer could just write code that saves your information into a simple `users.txt` file on the Server's hard drive.\n\n```text\nAlice, password123, 25\nBob, securepass, 30\nCharlie, mypassword, 22\n```\n\n### Why Text Files Fail\n\nWhile this works for 3 users, what happens when you have 10 million users?\n\n1. **Speed (Searchability)**: If Bob tries to log in, the Server has to read all 10 million lines of the text file one by one to find him. It would take ages.\n2. **Concurrency**: What if Alice and Charlie both create an account at the exact same millisecond? If the server tries to write to the exact same text file at the same time, the file gets corrupted and the data is destroyed.\n3. **Relationships**: How do we link Alice to the 50 photos she uploaded without making a massive mess?\n\n### The Solution: Databases\n\nA **Database** is a highly specialized piece of software designed solely to store, search, and manage data at lightning speed.\n\n- It uses complex math (Indexing) to find Bob instantly, even among 10 million users.\n- It handles thousands of people saving data at the exact same millisecond without breaking (Transactions/Concurrency).\n- It is the absolute backbone of the Backend. A Backend is usually just a middleman sitting between the Client and the Database.",
        "instructions": "## Task: Why Databases?\nRead the scenarios and match them to the database superpower they require: `Searchability` or `Concurrency`.",
        "starterCode": "scenario_1 = \"Finding one specific user out of 5 million in milliseconds\"\nsuperpower_1 = '___'\n\nscenario_2 = \"10,000 people buying Taylor Swift tickets at the exact same second without crashing\"\nsuperpower_2 = '___'\n\nprint(f\"{scenario_1} requires {superpower_1}\")\nprint(f\"{scenario_2} requires {superpower_2}\")",
        "solution": "scenario_1 = \"Finding one specific user out of 5 million in milliseconds\"\nsuperpower_1 = 'Searchability'\n\nscenario_2 = \"10,000 people buying Taylor Swift tickets at the exact same second without crashing\"\nsuperpower_2 = 'Concurrency'\n\nprint(f\"{scenario_1} requires {superpower_1}\")\nprint(f\"{scenario_2} requires {superpower_2}\")",
        "hint": "Speed = Searchability. Simultaneous actions = Concurrency.",
        "rubric": "Correctly matches Searchability and Concurrency."
    }
]

filepath = os.path.join('curriculum', 'tracks', 'backend.json')

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

course_name = "HTTP & APIs"

if course_name in data:
    lessons = data[course_name]['lessons']
    # The first lesson should be "What is a Backend?" which we already added.
    # We want to insert these 5 lessons immediately after it (index 1 to 5).
    # Let's check if they are already there to avoid duplicates.
    
    existing_titles = [l['title'] for l in lessons]
    
    insert_idx = 1
    for lesson in new_lessons:
        if lesson['title'] not in existing_titles:
            lessons.insert(insert_idx, lesson)
            print(f"Inserted '{lesson['title']}' at index {insert_idx}")
            insert_idx += 1
        else:
            print(f"Skipped '{lesson['title']}' - already exists.")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print("backend.json saved successfully.")
else:
    print(f"Error: {course_name} not found in backend.json")
