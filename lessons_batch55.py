"""
Batch 55: Deep Dive into Backend (Advanced Authentication & Security)
"""
import json, os

NEW_COURSES_BATCH55 = {
    "Advanced Authentication & Security": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of backend security and authentication",
        "lessons": [
            {"title": "JWT vs Session Cookies", "theory": "## State vs Stateless\\nSessions are 'stateful' (the server stores the session ID in a database). JWTs (JSON Web Tokens) are 'stateless' (the token itself contains all the user data). JWTs are great for microservices but are harder to revoke.", "instructions": "## Task: Token Format\\nA JWT consists of three parts separated by dots. Which of these is NOT one of the parts?", "starterCode": "# Options: Header, Payload, Signature, DatabaseID\\nnot_a_part = '___'", "solution": "# Options: Header, Payload, Signature, DatabaseID\\nnot_a_part = 'DatabaseID'", "hint": "A JWT does not contain a DatabaseID", "rubric": "Identifies DatabaseID."},
            {"title": "OAuth 2.0 Flow", "theory": "## Delegated Access\\nOAuth 2.0 allows a user to grant a third-party application access to their data without giving away their password (e.g., 'Log in with Google').", "instructions": "## Task: The Exchange\\nIn the Authorization Code flow, the client receives an 'Authorization Code' first. What does it exchange this code for?", "starterCode": "# Options: An Access Token, A Password, A Session Cookie\\nexchanges_for = '___'", "solution": "# Options: An Access Token, A Password, A Session Cookie\\nexchanges_for = 'An Access Token'", "hint": "It exchanges it for An Access Token", "rubric": "Identifies An Access Token."},
            {"title": "Role-Based Access Control (RBAC)", "theory": "## Permissions\\nAuthentication verifies *who* you are. Authorization verifies *what you can do*. RBAC assigns permissions to Roles (e.g., 'Admin', 'Editor') and then assigns users to those roles.", "instructions": "## Task: Authorization Middleware\\nWrite the logic to block the request if the user's role is not 'admin'.", "starterCode": "function requireAdmin(req, res, next) {\\n  if (req.user.role !== '___') {\\n    return res.status(403).send('Forbidden');\\n  }\\n  next();\\n}", "solution": "function requireAdmin(req, res, next) {\\n  if (req.user.role !== 'admin') {\\n    return res.status(403).send('Forbidden');\\n  }\\n  next();\\n}", "hint": "Check if role is not equal to 'admin'", "rubric": "Checks against 'admin'."},
            {"title": "CSRF Protection", "theory": "## Cross-Site Request Forgery\\nCSRF happens when a malicious site tricks a user's browser into making an unwanted request to your site. Since the browser automatically includes cookies, the request looks legit.", "instructions": "## Task: Anti-Forgery Token\\nThe most common defense is requiring a unique, hidden token in every state-changing request (like POST). What is this token called?", "starterCode": "token_name = '___ Token'", "solution": "token_name = 'CSRF Token'", "hint": "It is called a CSRF Token", "rubric": "Identifies CSRF Token."},
            {"title": "XSS Prevention", "theory": "## Cross-Site Scripting\\nXSS occurs when an attacker injects malicious JavaScript into your database, which is then rendered and executed by other users' browsers.", "instructions": "## Task: Defense Mechanism\\nWhat is the primary defense against XSS when outputting user data in a template engine?", "starterCode": "# Options: Database indexing, HTML Escaping (Sanitization), CSRF Tokens\\ndefense = '___'", "solution": "# Options: Database indexing, HTML Escaping (Sanitization), CSRF Tokens\\ndefense = 'HTML Escaping (Sanitization)'", "hint": "You must sanitize or escape HTML", "rubric": "Identifies HTML Escaping (Sanitization)."},
            {"title": "Password Hashing", "theory": "## Never Store Plaintext\\nYou must never store user passwords in plaintext. You should hash them using a slow algorithm like Bcrypt or Argon2, and always include a unique 'salt' to defeat rainbow table attacks.", "instructions": "## Task: Bcrypt Rounds\\nIn bcrypt, you can increase the 'cost factor' (rounds) to make hashing slower, which defends against brute force. Set the salt rounds to 12.", "starterCode": "const bcrypt = require('bcrypt');\\nconst saltRounds = ___;\\nconst hash = await bcrypt.hash(myPlaintextPassword, saltRounds);", "solution": "const bcrypt = require('bcrypt');\\nconst saltRounds = 12;\\nconst hash = await bcrypt.hash(myPlaintextPassword, saltRounds);", "hint": "Set saltRounds to 12", "rubric": "Sets saltRounds to 12."},
            {"title": "Rate Limiting", "theory": "## Preventing Abuse\\nRate limiting restricts how many requests a user or IP can make in a given timeframe. It prevents brute-force login attempts and DDoS attacks.", "instructions": "## Task: HTTP Status Code\\nWhen a user exceeds their rate limit, what standard HTTP status code should your API return?", "starterCode": "# Options: 400, 403, 429\\nstatus_code = ___", "solution": "# Options: 400, 403, 429\\nstatus_code = 429", "hint": "429 means Too Many Requests", "rubric": "Identifies 429."},
            {"title": "Multi-Factor Authentication (MFA)", "theory": "## Layered Security\\nMFA requires users to provide two or more verification factors to gain access. A common implementation uses TOTP (Time-based One-Time Password) generated by an authenticator app.", "instructions": "## Task: TOTP Secret\\nTo set up TOTP, the backend generates a secret key and usually shares it with the user's authenticator app via what method?", "starterCode": "# Options: A phone call, A QR Code, A text message\\nsetup_method = '___'", "solution": "# Options: A phone call, A QR Code, A text message\\nsetup_method = 'A QR Code'", "hint": "It is shared via A QR Code", "rubric": "Identifies A QR Code."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'backend.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH55.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH55.items():
            tier = course_info["tier"]
            if "Backend" in index_data and tier in index_data["Backend"]:
                if new_course_name not in index_data["Backend"][tier]:
                    index_data["Backend"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 55: Added {total} lessons to Backend track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
