import json
import os

new_lesson = {
    "title": "What is a Backend?",
    "theory": "## The Hidden Half of the Web\n\nWhen you go to a restaurant, you only see the dining room and the waiter. You don't see the kitchen, the chefs, or the refrigerators where the food is stored.\n\nWebsites work the exact same way.\n\n### Frontend (The Dining Room)\n\nThe **Frontend** (or Client) is what you see in your browser or on your phone app. It's built with HTML, CSS, and JavaScript. It's the buttons you click and the images you see. \n\n### Backend (The Kitchen)\n\nThe **Backend** (or Server) is the hidden computer running somewhere else in the world. \n\nWhen you click \"Log In\" on the frontend, your browser sends a message to the backend. The backend checks its **Database** (the refrigerator) to see if your password is correct, and then sends a message back to the frontend saying \"Yes, let them in!\"\n\n### What do Backend Developers do?\n\nBackend developers write code that lives on these hidden servers. They worry about:\n1. **Security**: Making sure users can't steal data.\n2. **Databases**: Storing user accounts, posts, and transactions safely.\n3. **Performance**: Making sure the server doesn't crash if 1 million people log in at the exact same time.",
    "instructions": "## Task: Frontend vs Backend\nIdentify which technology belongs to the Frontend (Client) and which belongs to the Backend (Server).\nSet the variables to either 'Frontend' or 'Backend'.",
    "starterCode": "browser = '___'\ndatabase = '___'\n\nprint(f\"The Browser is the {browser}\")\nprint(f\"The Database is the {database}\")",
    "solution": "browser = 'Frontend'\ndatabase = 'Backend'\n\nprint(f\"The Browser is the {browser}\")\nprint(f\"The Database is the {database}\")",
    "hint": "The browser is what the user sees. The database is hidden away.",
    "rubric": "Correctly assigns Frontend and Backend."
}

filepath = os.path.join('curriculum', 'tracks', 'backend.json')

with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

course_name = "HTTP & APIs"

if course_name in data:
    if data[course_name]['lessons'][0]['title'] != new_lesson['title']:
        data[course_name]['lessons'].insert(0, new_lesson)
        print(f"Added '{new_lesson['title']}' to {course_name} in backend.json")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    else:
        print(f"Lesson already exists in {course_name}")
else:
    print(f"Course {course_name} not found in backend.json")
