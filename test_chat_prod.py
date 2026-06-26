import requests

try:
    # 1. Register a new test user
    signup_data = {
        "email": "testchat@test.com",
        "password": "password",
        "full_name": "Test User",
        "role": "student"
    }
    requests.post("https://digital-era.live/signup", json=signup_data)
    
    # 2. Login
    login_data = {"username": "testchat@test.com", "password": "password"}
    res = requests.post("https://digital-era.live/login", data=login_data)
    print("Login:", res.status_code, res.text)
    
    if res.ok:
        token = res.json()["access_token"]
        chat_data = {
            "message": "Please give me a detailed technical explanation of this lesson",
            "course": "Python Fundamentals"
        }
        headers = {"Authorization": f"Bearer {token}"}
        chat_res = requests.post("https://digital-era.live/chat", json=chat_data, headers=headers)
        print("Chat:", chat_res.status_code, chat_res.text)
except Exception as e:
    print("Error:", e)
