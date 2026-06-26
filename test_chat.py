import requests

token = "replace_me"  # I don't have the user's token but I can login
login_data = {"username": "nasaadanna@gmail.com", "password": "password123"} # using reset password
res = requests.post("http://127.0.0.1:8000/login", data=login_data)
token = res.json()["access_token"]

chat_data = {
    "message": "Hello",
    "course": "Python Fundamentals"
}
headers = {"Authorization": f"Bearer {token}"}
res = requests.post("http://127.0.0.1:8000/chat", json=chat_data, headers=headers)
print(res.status_code)
print(res.json())
