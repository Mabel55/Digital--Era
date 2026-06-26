import requests

payload = {
    "language": "python",
    "entrypoint": "main.py",
    "files": {
        "main.py": "from utils import greet\n\nprint(greet('Digital Era Student!'))\n",
        "utils.py": "def greet(name):\n    return f'Welcome to the Multi-File Workspace, {name}'\n"
    }
}

try:
    response = requests.post("http://localhost:8000/run-code/", json=payload)
    print("Status:", response.status_code)
    print("Result:", response.json())
except Exception as e:
    print("Error:", e)
