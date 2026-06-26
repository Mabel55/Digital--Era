"""
Phase 4: Add 44 new unique lessons to Backend track.
"""
import json

TRACK_FILE = "curriculum/tracks/backend.json"

NEW_LESSONS = {
    "Intro to Backend": [
        {
            "title": "Client-Server Model",
            "theory": "## Client-Server Architecture\nIn web applications, the client (browser/mobile app) requests resources or actions from the server. The server processes the request, interacts with databases, and returns a response.",
            "instructions": "## Task: Conceptualize a Request\n1. Write a conceptual function `handleRequest(clientData)`.\n2. Return a simulated server response object with status 200 and a welcome message.",
            "starterCode": "function handleRequest(clientData) {\n  // simulated server processing\n  return {\n    ___: 200,\n    ___: \"Welcome to the backend!\"\n  };\n}",
            "solution": "function handleRequest(clientData) {\n  // simulated server processing\n  return {\n    status: 200,\n    message: \"Welcome to the backend!\"\n  };\n}",
            "hint": "Set status to 200 and message to the string.",
            "rubric": "Function returns a correct object structure representing a response."
        },
        {
            "title": "Backend Languages",
            "theory": "## Popular Backend Languages\nBackend can be written in many languages: Python (Django/FastAPI), JavaScript/TypeScript (Node.js), Java (Spring), Go, Ruby, etc.",
            "instructions": "## Task: Simple Node.js Server\n1. Use Node's `http` module to create a server.\n2. Make it listen on port 3000 and log \"Server running\".",
            "starterCode": "const http = require('___');\n\nconst server = http.___((req, res) => {\n  res.end('Hello World');\n});\n\nserver.___(___, () => {\n  console.log('Server running');\n});",
            "solution": "const http = require('http');\n\nconst server = http.createServer((req, res) => {\n  res.end('Hello World');\n});\n\nserver.listen(3000, () => {\n  console.log('Server running');\n});",
            "hint": "require 'http', use createServer, and listen on 3000.",
            "rubric": "Basic Node.js HTTP server configured correctly."
        },
        {
            "title": "Statelessness",
            "theory": "## Stateless Servers\nA server is stateless if it doesn't store client state between requests. Every request must contain all info needed to process it.",
            "instructions": "## Task: Stateless vs Stateful\n1. Write a function `statelessAdd` that takes previous state and new value and returns the sum.\n2. Ensure it does not modify external variables.",
            "starterCode": "let state = 0; // Don't use this!\n\nfunction statelessAdd(currentState, newValue) {\n  return ___ + ___;\n}",
            "solution": "let state = 0; // Don't use this!\n\nfunction statelessAdd(currentState, newValue) {\n  return currentState + newValue;\n}",
            "hint": "Just return the sum of the parameters without using global state.",
            "rubric": "Function correctly implements pure stateless addition."
        }
    ],
    "HTTP & REST Concepts": [
        {
            "title": "HTTP Methods",
            "theory": "## HTTP Methods (Verbs)\n`GET` fetches data. `POST` creates data. `PUT`/`PATCH` update data. `DELETE` removes data.",
            "instructions": "## Task: Map Methods to Actions\n1. Write a function `routeMethod` that returns the correct action string based on the HTTP method passed ('GET', 'POST', 'DELETE').",
            "starterCode": "function routeMethod(method) {\n  if (method === '___') return 'Fetch Data';\n  if (method === '___') return 'Create Data';\n  if (method === '___') return 'Delete Data';\n  return 'Unknown';\n}",
            "solution": "function routeMethod(method) {\n  if (method === 'GET') return 'Fetch Data';\n  if (method === 'POST') return 'Create Data';\n  if (method === 'DELETE') return 'Delete Data';\n  return 'Unknown';\n}",
            "hint": "Map GET, POST, and DELETE to their corresponding actions.",
            "rubric": "Function correctly maps HTTP verbs to their standard CRUD operations."
        },
        {
            "title": "HTTP Status Codes",
            "theory": "## Status Codes\n2xx (Success): 200 OK, 201 Created.\n4xx (Client Error): 400 Bad Request, 401 Unauthorized, 404 Not Found.\n5xx (Server Error): 500 Internal Server Error.",
            "instructions": "## Task: Handle Status Codes\n1. Write a function `checkStatus` that takes a status code.\n2. Return 'Success' for 200, 'Not Found' for 404, and 'Server Error' for 500.",
            "starterCode": "function checkStatus(code) {\n  switch(code) {\n    case ___: return 'Success';\n    case ___: return 'Not Found';\n    case ___: return 'Server Error';\n    default: return 'Other';\n  }\n}",
            "solution": "function checkStatus(code) {\n  switch(code) {\n    case 200: return 'Success';\n    case 404: return 'Not Found';\n    case 500: return 'Server Error';\n    default: return 'Other';\n  }\n}",
            "hint": "Use 200, 404, and 500 for the switch cases.",
            "rubric": "Status codes are accurately mapped to their meanings."
        },
        {
            "title": "REST Principles",
            "theory": "## Representational State Transfer (REST)\nREST APIs organize resources around URLs (e.g., `/users`), use standard HTTP methods, and return JSON. They should be stateless.",
            "instructions": "## Task: Design a REST Endpoint\n1. You manage a 'books' resource.\n2. Define the URL path for getting all books.\n3. Define the URL path for getting a specific book by ID (e.g., 42).",
            "starterCode": "const getAllBooksUrl = \"/___\";\nconst getSingleBookUrl = \"/___/42\";",
            "solution": "const getAllBooksUrl = \"/books\";\nconst getSingleBookUrl = \"/books/42\";",
            "hint": "Use plural nouns like /books and /books/id.",
            "rubric": "RESTful URL patterns correctly designed."
        }
    ],
    "Python for Web": [
        {
            "title": "Python web servers",
            "theory": "## WSGI and ASGI\nPython uses WSGI (synchronous) and ASGI (asynchronous) interfaces to communicate between web servers (like Gunicorn or Uvicorn) and web frameworks (like Django or FastAPI).",
            "instructions": "## Task: Simple WSGI App\n1. Define an `application` function accepting `environ` and `start_response`.\n2. Call `start_response` with a 200 status.\n3. Return an iterable of bytes.",
            "starterCode": "def application(___, ___):\n    status = '___ OK'\n    headers = [('Content-type', 'text/plain')]\n    ___(status, headers)\n    return [___'Hello World!']",
            "solution": "def application(environ, start_response):\n    status = '200 OK'\n    headers = [('Content-type', 'text/plain')]\n    start_response(status, headers)\n    return [b'Hello World!']",
            "hint": "Arguments are environ and start_response. Status is '200 OK', return b'string'.",
            "rubric": "Valid minimal Python WSGI application created."
        },
        {
            "title": "Python Requests Library",
            "theory": "## Requests\nThe `requests` library is the standard for making HTTP calls in Python. E.g., `requests.get('url')`.",
            "instructions": "## Task: Make a GET request\n1. Import `requests`.\n2. Make a GET call to `https://api.example.com/data`.\n3. Extract the JSON response.",
            "starterCode": "import ___\n\nresponse = ___.get('https://api.example.com/data')\ndata = response.___()",
            "solution": "import requests\n\nresponse = requests.get('https://api.example.com/data')\ndata = response.json()",
            "hint": "Import requests, use requests.get, and response.json().",
            "rubric": "Requests library used correctly to fetch and parse JSON."
        },
        {
            "title": "Basic Routing in Python",
            "theory": "## Routing\nRouting maps URLs to Python functions. Most frameworks use decorators like `@app.route('/path')`.",
            "instructions": "## Task: Simulated Router\n1. Create a `routes` dictionary mapping `/home` to a function returning 'Home' and `/about` to 'About'.\n2. Call the dictionary to simulate routing.",
            "starterCode": "routes = {\n    '___': lambda: 'Home',\n    '___': lambda: 'About'\n}\n\ndef route_request(path):\n    handler = routes.get(path, lambda: '404')\n    return ___()",
            "solution": "routes = {\n    '/home': lambda: 'Home',\n    '/about': lambda: 'About'\n}\n\ndef route_request(path):\n    handler = routes.get(path, lambda: '404')\n    return handler()",
            "hint": "Map '/home' and '/about'. Call the returned handler function.",
            "rubric": "Dictionary-based routing logic works appropriately."
        }
    ],
    "JSON & APIs": [
        {
            "title": "Parsing JSON",
            "theory": "## JSON (JavaScript Object Notation)\nJSON is the standard format for API communication. It resembles a stringified JS object. Use `json.loads()` in Python to parse it.",
            "instructions": "## Task: Parse JSON in Python\n1. Import the `json` module.\n2. Parse the string `json_string` into a Python dictionary.\n3. Access the `name` key.",
            "starterCode": "import ___\n\njson_string = '{\"name\": \"Alice\", \"age\": 30}'\ndata = json.___(___)\nprint(data['___'])",
            "solution": "import json\n\njson_string = '{\"name\": \"Alice\", \"age\": 30}'\ndata = json.loads(json_string)\nprint(data['name'])",
            "hint": "Use json.loads() and access 'name'.",
            "rubric": "JSON string successfully parsed into a dictionary."
        },
        {
            "title": "Serializing JSON",
            "theory": "## Serializing\nConverting a Python dictionary to a JSON string is called serializing or encoding. Use `json.dumps()`.",
            "instructions": "## Task: Serialize a Dictionary\n1. Create a dict with `status` (success) and `code` (200).\n2. Convert it to a JSON string using `json.dumps()`.",
            "starterCode": "import json\n\nmy_dict = { \"status\": \"___\", \"code\": ___ }\njson_result = json.___(___)",
            "solution": "import json\n\nmy_dict = { \"status\": \"success\", \"code\": 200 }\njson_result = json.dumps(my_dict)",
            "hint": "Populate the dict and use json.dumps().",
            "rubric": "Dictionary successfully converted to JSON string."
        },
        {
            "title": "API Design Best Practices",
            "theory": "## Consistency\nAPIs should have consistent structures. Responses should wrap data predictably, e.g., `{ \"data\": [...], \"error\": null }`.",
            "instructions": "## Task: Standardize API Response\n1. Write a function `apiResponse(data, error)`.\n2. Return a dictionary containing both keys, handling `None` defaults.",
            "starterCode": "def apiResponse(data=___, error=___):\n    return {\n        \"___\": data,\n        \"___\": error\n    }",
            "solution": "def apiResponse(data=None, error=None):\n    return {\n        \"data\": data,\n        \"error\": error\n    }",
            "hint": "Set defaults to None and map to 'data' and 'error' keys.",
            "rubric": "API response formatter correctly constructs standard response dictionary."
        }
    ],
    "Environment & Setup": [
        {
            "title": "Virtual Environments",
            "theory": "## venv\nVirtual environments keep dependencies required by different projects separate. In Python: `python -m venv myenv`.",
            "instructions": "## Task: Create a bash script snippet\n1. Write the bash commands to create a virtual environment named `venv`.\n2. Write the command to activate it on Linux/Mac.",
            "starterCode": "python -m ___ ___\n___ venv/bin/___",
            "solution": "python -m venv venv\nsource venv/bin/activate",
            "hint": "Use `venv` module and `source` command.",
            "rubric": "Correct bash commands for creating and activating a venv."
        },
        {
            "title": "Environment Variables",
            "theory": "## .env Files\nStore secrets (API keys, DB URLs) in `.env` files. Don't commit these to version control. Use `python-dotenv` to load them.",
            "instructions": "## Task: Load .env in Python\n1. Import `load_dotenv` and `os`.\n2. Call `load_dotenv()`.\n3. Retrieve the `SECRET_KEY` from the environment.",
            "starterCode": "import ___\nfrom dotenv import ___\n\n___()\nsecret = os.___.get('___')",
            "solution": "import os\nfrom dotenv import load_dotenv\n\nload_dotenv()\nsecret = os.environ.get('SECRET_KEY')",
            "hint": "Use os and load_dotenv. Get from os.environ.get().",
            "rubric": "Environment variables correctly loaded and accessed."
        },
        {
            "title": "requirements.txt",
            "theory": "## Managing Dependencies\nUse `pip freeze > requirements.txt` to save dependencies. Use `pip install -r requirements.txt` to install them.",
            "instructions": "## Task: Read Requirements\n1. In Python, write a script to open `requirements.txt`.\n2. Read all lines into a list, stripping whitespace.",
            "starterCode": "with open('___', 'r') as f:\n    deps = [line.___() for line in f.___()]",
            "solution": "with open('requirements.txt', 'r') as f:\n    deps = [line.strip() for line in f.readlines()]",
            "hint": "Open 'requirements.txt', readlines(), and strip().",
            "rubric": "File operations to read dependency lists are correct."
        }
    ],
    "Java: Beginner": [
        {
            "title": "Basic Syntax",
            "theory": "## Java Basics\nJava is strictly typed and object-oriented. Every application begins with a `public static void main(String[] args)` method.",
            "instructions": "## Task: Hello World\n1. Create a `Main` class.\n2. Add the `main` method.\n3. Print \"Hello Java\" using `System.out.println`.",
            "starterCode": "public class ___ {\n    public static void ___(String[] args) {\n        ___.___.___(\"Hello Java\");\n    }\n}",
            "solution": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello Java\");\n    }\n}",
            "hint": "Class Main, method main, System.out.println.",
            "rubric": "Java Hello World program is syntactically perfect."
        },
        {
            "title": "Java Data Types",
            "theory": "## Primitives vs Objects\nJava has primitives like `int`, `double`, `boolean`. Object wrappers include `Integer`, `Double`, `String`.",
            "instructions": "## Task: Declare Variables\n1. Declare an integer `age` set to 25.\n2. Declare a double `price` set to 19.99.\n3. Declare a String `name` set to \"Alice\".",
            "starterCode": "___ age = 25;\n___ price = 19.99;\n___ name = \"Alice\";",
            "solution": "int age = 25;\ndouble price = 19.99;\nString name = \"Alice\";",
            "hint": "Use int, double, and String.",
            "rubric": "Variables are correctly declared with their respective types."
        },
        {
            "title": "Control Flow in Java",
            "theory": "## Loops and Conditionals\nJava uses standard C-style loops (`for`, `while`) and `if/else` conditionals.",
            "instructions": "## Task: Write a Loop\n1. Write a `for` loop that runs from `i = 0` up to `4`.\n2. Inside the loop, print the value of `i`.",
            "starterCode": "for (___ i = 0; i ___ 5; i___) {\n    System.out.println(___);\n}",
            "solution": "for (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}",
            "hint": "Declare int i, condition i < 5, increment i++.",
            "rubric": "Java for loop correctly constructed and prints iterator."
        }
    ],
    "REST APIs with FastAPI": [
        {
            "title": "FastAPI Setup",
            "theory": "## FastAPI\nFastAPI is a modern, fast framework for building APIs with Python based on standard Python type hints.",
            "instructions": "## Task: Basic App\n1. Import `FastAPI`.\n2. Initialize an `app` instance.\n3. Create a GET route at `/` returning `{\"message\": \"Hello\"}`.",
            "starterCode": "from fastapi import ___\n\napp = ___()\n\n@app.___(\"___\")\ndef read_root():\n    return {\"message\": \"Hello\"}",
            "solution": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/\")\ndef read_root():\n    return {\"message\": \"Hello\"}",
            "hint": "Import FastAPI, instantiate app = FastAPI(), use @app.get('/').",
            "rubric": "FastAPI application is correctly initialized and routed."
        },
        {
            "title": "Path and Query Parameters",
            "theory": "## Parameters\nPath parameters are declared in the URL path (e.g., `/items/{item_id}`). Query parameters are passed in the URL string (e.g., `?q=search`).",
            "instructions": "## Task: Define Parameters\n1. Create a route `/items/{item_id}`.\n2. Accept `item_id` as an `int`.\n3. Accept a query parameter `q` as a `str` with default `None`.",
            "starterCode": "@app.get(\"/items/___}\")\ndef read_item(item_id: ___, q: ___ = None):\n    return {\"item_id\": item_id, \"q\": q}",
            "solution": "@app.get(\"/items/{item_id}\")\ndef read_item(item_id: int, q: str = None):\n    return {\"item_id\": item_id, \"q\": q}",
            "hint": "Use {item_id} in path, type hint int and str.",
            "rubric": "Path and query parameters are correctly typed and utilized."
        }
    ],
    "Authentication & JWT": [
        {
            "title": "Hashing Passwords",
            "theory": "## Security\nNever store plain-text passwords. Use hashing algorithms like `bcrypt`.",
            "instructions": "## Task: Use passlib\n1. Given a `pwd_context` using bcrypt, hash a password.\n2. Verify the plain password against the hash.",
            "starterCode": "hashed_pwd = pwd_context.___(\"mysecret\")\nis_valid = pwd_context.___(\"mysecret\", ___)",
            "solution": "hashed_pwd = pwd_context.hash(\"mysecret\")\nis_valid = pwd_context.verify(\"mysecret\", hashed_pwd)",
            "hint": "Use .hash() and .verify(plain, hashed).",
            "rubric": "Password hashing and verification methods are correctly applied."
        },
        {
            "title": "Creating JWTs",
            "theory": "## JSON Web Tokens\nJWTs encode user claims (like user_id) securely. They consist of a header, payload, and signature.",
            "instructions": "## Task: Encode a Token\n1. Import `jwt` from `jose`.\n2. Encode the payload `{\"sub\": \"123\"}` using `SECRET_KEY` and algorithm `HS256`.",
            "starterCode": "from jose import ___\n\ntoken = jwt.___(\n    {\"sub\": \"123\"}, \n    ___, \n    algorithm=\"___\"\n)",
            "solution": "from jose import jwt\n\ntoken = jwt.encode(\n    {\"sub\": \"123\"}, \n    SECRET_KEY, \n    algorithm=\"HS256\"\n)",
            "hint": "Use jwt.encode, pass the SECRET_KEY and 'HS256'.",
            "rubric": "JWT encoding successfully utilizes python-jose."
        }
    ],
    "Django Web Framework": [
        {
            "title": "Django Models",
            "theory": "## ORM Models\nDjango maps Python classes to database tables using its ORM. Subclass `models.Model`.",
            "instructions": "## Task: Create a Book Model\n1. Create a `Book` model.\n2. Add a `title` as a `CharField` (max length 200).\n3. Add an `author` as a `CharField` (max length 100).",
            "starterCode": "from django.db import models\n\nclass Book(models.___):\n    title = models.___(max_length=___)\n    author = models.___(max_length=___)",
            "solution": "from django.db import models\n\nclass Book(models.Model):\n    title = models.CharField(max_length=200)\n    author = models.CharField(max_length=100)",
            "hint": "Inherit from models.Model, use models.CharField.",
            "rubric": "Django model defined properly with CharFields."
        },
        {
            "title": "Django Views",
            "theory": "## Views\nViews process requests and return responses. They can be function-based (FBV) or class-based (CBV).",
            "instructions": "## Task: Simple FBV\n1. Create a view `hello_world` taking a `request`.\n2. Return an `HttpResponse` containing \"Hello\".",
            "starterCode": "from django.http import ___\n\ndef hello_world(___):\n    return ___(\"Hello\")",
            "solution": "from django.http import HttpResponse\n\ndef hello_world(request):\n    return HttpResponse(\"Hello\")",
            "hint": "Import HttpResponse, view takes request, returns HttpResponse.",
            "rubric": "Function-based view successfully returns HttpResponse."
        }
    ],
    "Flask Microframework": [
        {
            "title": "Flask Routing",
            "theory": "## Flask Basics\nFlask uses `@app.route` decorators to define endpoints. It's lightweight and explicitly configured.",
            "instructions": "## Task: Create a Route\n1. Import `Flask` and instantiate `app`.\n2. Create a route `/greet/<name>`.\n3. Return a greeting string.",
            "starterCode": "from flask import ___\n\napp = ___(__name__)\n\n@app.___('/greet/<___>')\ndef greet(name):\n    return f\"Hello {___}\"",
            "solution": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/greet/<name>')\ndef greet(name):\n    return f\"Hello {name}\"",
            "hint": "Use @app.route and matching parameter <name>.",
            "rubric": "Flask route with path parameter implemented correctly."
        },
        {
            "title": "Returning JSON in Flask",
            "theory": "## jsonify\nFlask provides `jsonify` to properly format dictionaries into JSON responses with correct headers.",
            "instructions": "## Task: JSON Response\n1. Import `jsonify`.\n2. Return a JSON response `{\"status\": \"ok\"}` from the `/health` endpoint.",
            "starterCode": "from flask import Flask, ___\n\napp = Flask(__name__)\n\n@app.route('/health')\ndef health_check():\n    return ___({'status': '___'})",
            "solution": "from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route('/health')\ndef health_check():\n    return jsonify({'status': 'ok'})",
            "hint": "Use jsonify() on the dictionary.",
            "rubric": "JSON response correctly formatted using Flask jsonify."
        }
    ],
    "Database Integration": [
        {
            "title": "SQLAlchemy Basics",
            "theory": "## ORMs\nSQLAlchemy is a popular Python ORM. You query tables like Python objects.",
            "instructions": "## Task: Query Users\n1. Given a SQLAlchemy `session` and a `User` model, query all users.\n2. Query a user by ID 1.",
            "starterCode": "all_users = session.___(___).___()\nuser_one = session.query(User).___(___).___()",
            "solution": "all_users = session.query(User).all()\nuser_one = session.query(User).filter_by(id=1).first()",
            "hint": "Use query(User).all() and filter_by(id=1).first().",
            "rubric": "SQLAlchemy queries correctly formulated for all and single records."
        },
        {
            "title": "Raw SQL in Python",
            "theory": "## Database Drivers\nLibraries like `psycopg2` or `sqlite3` execute raw SQL.",
            "instructions": "## Task: Execute SQLite Query\n1. Execute `SELECT * FROM users` using a cursor.\n2. Fetch all results.",
            "starterCode": "import sqlite3\nconn = sqlite3.connect('test.db')\ncursor = conn.___()\n\ncursor.___(\"___ FROM users\")\nresults = cursor.___()",
            "solution": "import sqlite3\nconn = sqlite3.connect('test.db')\ncursor = conn.cursor()\n\ncursor.execute(\"SELECT * FROM users\")\nresults = cursor.fetchall()",
            "hint": "Use conn.cursor(), cursor.execute(), and cursor.fetchall().",
            "rubric": "Raw SQL execution using SQLite3 cursor works perfectly."
        }
    ],
    "Java: Intermediate": [
        {
            "title": "Classes and Objects",
            "theory": "## OOP in Java\nClasses define blueprints. Objects are instances. Constructors initialize state.",
            "instructions": "## Task: Create a Constructor\n1. Define class `Car` with private field `model`.\n2. Write a constructor to initialize `model`.",
            "starterCode": "public class Car {\n    private String ___;\n    \n    public ___(String model) {\n        this.___ = model;\n    }\n}",
            "solution": "public class Car {\n    private String model;\n    \n    public Car(String model) {\n        this.model = model;\n    }\n}",
            "hint": "Constructor name must match class name exactly.",
            "rubric": "Java class features a correctly implemented constructor."
        },
        {
            "title": "Java Collections",
            "theory": "## ArrayList\n`ArrayList` is a resizable array implementation of the `List` interface.",
            "instructions": "## Task: Use ArrayList\n1. Create an `ArrayList` of Strings named `list`.\n2. Add \"Apple\" to it.\n3. Retrieve the first element.",
            "starterCode": "import java.util.ArrayList;\n\nArrayList<___> list = new ___<>();\nlist.___(\"Apple\");\nString item = list.___(0);",
            "solution": "import java.util.ArrayList;\n\nArrayList<String> list = new ArrayList<>();\nlist.add(\"Apple\");\nString item = list.get(0);",
            "hint": "Use generic <String>, new ArrayList<>(), .add(), and .get().",
            "rubric": "ArrayList initialization and methods applied properly."
        }
    ],
    "Node.js & Express": [
        {
            "title": "Express Setup",
            "theory": "## Express.js\nExpress is a minimalist web framework for Node.js.",
            "instructions": "## Task: Basic Express App\n1. Import `express` and create an `app`.\n2. Define a GET route at `/ping` returning \"pong\".",
            "starterCode": "const express = require('___');\nconst app = ___();\n\napp.___('/ping', (req, res) => {\n  res.___('pong');\n});",
            "solution": "const express = require('express');\nconst app = express();\n\napp.get('/ping', (req, res) => {\n  res.send('pong');\n});",
            "hint": "Require 'express', call express(), use app.get and res.send.",
            "rubric": "Express application instantiated and route defined successfully."
        },
        {
            "title": "Express Middleware",
            "theory": "## Middleware\nMiddleware functions run between the request and the response. They can modify requests or end the cycle early.",
            "instructions": "## Task: Logger Middleware\n1. Write a middleware function that logs the request method.\n2. Call `next()` to pass control to the next handler.",
            "starterCode": "function logger(req, res, ___) {\n  console.log(req.___);\n  ___();\n}\n\napp.___(___);",
            "solution": "function logger(req, res, next) {\n  console.log(req.method);\n  next();\n}\n\napp.use(logger);",
            "hint": "Include 'next' parameter and call it. Use app.use() to register it.",
            "rubric": "Middleware function correctly logs method and calls next()."
        }
    ],
    "Django REST Framework": [
        {
            "title": "DRF Serializers",
            "theory": "## Serializers\nDRF serializers convert complex data like QuerySets into native Python datatypes that can be rendered to JSON.",
            "instructions": "## Task: ModelSerializer\n1. Create a serializer for the `User` model.\n2. Inherit from `serializers.ModelSerializer`.\n3. Include `id` and `username` fields.",
            "starterCode": "from rest_framework import ___\nfrom .models import User\n\nclass UserSerializer(serializers.___):\n    class ___:\n        model = ___\n        fields = ['___', '___']",
            "solution": "from rest_framework import serializers\nfrom .models import User\n\nclass UserSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = User\n        fields = ['id', 'username']",
            "hint": "Use ModelSerializer, Meta class, set model=User.",
            "rubric": "DRF ModelSerializer structure is perfectly formed."
        },
        {
            "title": "API Views",
            "theory": "## DRF Views\nUse the `@api_view` decorator to write function-based views in DRF, restricting allowed HTTP methods.",
            "instructions": "## Task: @api_view\n1. Decorate the view to only allow GET requests.\n2. Return a DRF `Response` with `{\"hello\": \"world\"}`.",
            "starterCode": "from rest_framework.decorators import ___\nfrom rest_framework.response import ___\n\n@___(['___'])\ndef hello_world(request):\n    return ___({\"hello\": \"world\"})",
            "solution": "from rest_framework.decorators import api_view\nfrom rest_framework.response import Response\n\n@api_view(['GET'])\ndef hello_world(request):\n    return Response({\"hello\": \"world\"})",
            "hint": "Use @api_view(['GET']) and Response().",
            "rubric": "Function correctly utilizes DRF decorators and Response objects."
        }
    ],
    "Flask Advanced Patterns": [
        {
            "title": "Flask Blueprints",
            "theory": "## Blueprints\nBlueprints allow you to organize Flask apps into smaller, modular components (e.g., auth, blog).",
            "instructions": "## Task: Create a Blueprint\n1. Import `Blueprint`.\n2. Create an `auth_bp` blueprint named 'auth'.\n3. Register a route `/login` on the blueprint.",
            "starterCode": "from flask import ___\n\nauth_bp = ___('auth', __name__)\n\n@auth_bp.___('/login')\ndef login():\n    return \"Login page\"",
            "solution": "from flask import Blueprint\n\nauth_bp = Blueprint('auth', __name__)\n\n@auth_bp.route('/login')\ndef login():\n    return \"Login page\"",
            "hint": "Use Blueprint and @auth_bp.route.",
            "rubric": "Flask Blueprint instantiated and routed correctly."
        },
        {
            "title": "Application Context",
            "theory": "## App Context\nFlask uses context locals to keep track of the current request and app. Sometimes you need `app.app_context()` when working outside a request.",
            "instructions": "## Task: Use App Context\n1. Create an app context block.\n2. Print the app name inside the block using `current_app`.",
            "starterCode": "from flask import current_app\n\nwith app.___():\n    print(___.name)",
            "solution": "from flask import current_app\n\nwith app.app_context():\n    print(current_app.name)",
            "hint": "Use app.app_context() and current_app.",
            "rubric": "Application context manager used appropriately."
        }
    ],
    "Async Python": [
        {
            "title": "Asyncio Loops",
            "theory": "## Event Loop\nThe event loop is the core of asyncio applications. `asyncio.run(main())` creates the loop, runs the coroutine, and closes it.",
            "instructions": "## Task: Run a Coroutine\n1. Import `asyncio`.\n2. Define an async function `main()`.\n3. Run it using `asyncio.run()`.",
            "starterCode": "___ ___\n\n___ def main():\n    print(\"Hello async\")\n\n___.___(main())",
            "solution": "import asyncio\n\nasync def main():\n    print(\"Hello async\")\n\nasyncio.run(main())",
            "hint": "Use async def and asyncio.run.",
            "rubric": "Asyncio runtime correctly initialized and executed."
        },
        {
            "title": "Gathering Tasks",
            "theory": "## Concurrency\n`asyncio.gather` runs awaitables concurrently and waits for all of them to finish.",
            "instructions": "## Task: Concurrent Sleeps\n1. Create two sleep tasks of 1 second using `asyncio.sleep()`.\n2. Run them concurrently using `asyncio.gather`.",
            "starterCode": "async def run_tasks():\n    await asyncio.___(\n        asyncio.___(___),\n        asyncio.___(___)\n    )",
            "solution": "async def run_tasks():\n    await asyncio.gather(\n        asyncio.sleep(1),\n        asyncio.sleep(1)\n    )",
            "hint": "Use gather and pass asyncio.sleep(1) twice.",
            "rubric": "Concurrent tasks properly orchestrated using gather."
        }
    ],
    "API Security & Rate Limiting": [
        {
            "title": "CORS Headers",
            "theory": "## Cross-Origin Resource Sharing (CORS)\nCORS allows frontend apps on one domain to request data from an API on another domain.",
            "instructions": "## Task: Allow CORS in Response\n1. Write a function modifying a response dictionary.\n2. Add the `Access-Control-Allow-Origin` header allowing `*`.",
            "starterCode": "def addCors(response_headers) {\n    response_headers[\"___\"] = \"___\";\n    return response_headers;\n}",
            "solution": "def addCors(response_headers) {\n    response_headers[\"Access-Control-Allow-Origin\"] = \"*\";\n    return response_headers;\n}",
            "hint": "Set 'Access-Control-Allow-Origin' to '*'.",
            "rubric": "CORS header securely configured."
        },
        {
            "title": "Basic Rate Limiting Logic",
            "theory": "## Rate Limiting\nRate limiting prevents abuse by restricting how many requests an IP can make in a time window.",
            "instructions": "## Task: Simple Token Bucket\n1. You have a `tokens` integer representing allowed requests.\n2. If `tokens > 0`, decrement and return `True` (allow).\n3. Else return `False` (block).",
            "starterCode": "let tokens = 5;\n\nfunction checkRateLimit() {\n    if (tokens > ___) {\n        tokens___;\n        return ___;\n    }\n    return ___;\n}",
            "solution": "let tokens = 5;\n\nfunction checkRateLimit() {\n    if (tokens > 0) {\n        tokens--;\n        return true;\n    }\n    return false;\n}",
            "hint": "Check > 0, decrement with --.",
            "rubric": "Basic rate limiting algorithm implements correctly."
        }
    ],
    "Deployment & Docker": [
        {
            "title": "Writing a Dockerfile",
            "theory": "## Dockerfile\nA Dockerfile is a recipe for building an image. You specify a base image, copy files, and set a run command.",
            "instructions": "## Task: Simple Python Dockerfile\n1. Use `python:3.9-slim` as base.\n2. Copy the current directory to `/app`.\n3. Set command to `python main.py`.",
            "starterCode": "___ python:3.9-slim\n___ . /app\nWORKDIR /app\n___ [\"python\", \"main.py\"]",
            "solution": "FROM python:3.9-slim\nCOPY . /app\nWORKDIR /app\nCMD [\"python\", \"main.py\"]",
            "hint": "Use FROM, COPY, and CMD.",
            "rubric": "Dockerfile directives are syntactically valid."
        },
        {
            "title": "Docker Compose",
            "theory": "## docker-compose.yml\nCompose defines multi-container applications (e.g., an API and a Database).",
            "instructions": "## Task: Add a Redis Service\n1. Define a service named `cache`.\n2. Use the `redis:alpine` image.\n3. Expose port `6379:6379`.",
            "starterCode": "version: '3'\nservices:\n  ___:\n    image: ___\n    ports:\n      - \"___\"",
            "solution": "version: '3'\nservices:\n  cache:\n    image: redis:alpine\n    ports:\n      - \"6379:6379\"",
            "hint": "Name it cache, image redis:alpine, ports '6379:6379'.",
            "rubric": "Docker Compose service accurately defined."
        }
    ],
    "Java: Advanced": [
        {
            "title": "Java Streams",
            "theory": "## Streams API\nJava 8 Streams allow declarative manipulation of collections (filter, map, reduce).",
            "instructions": "## Task: Filter and Count\n1. Given a list of names, use `.stream()`.\n2. Filter names starting with 'A'.\n3. Count them.",
            "starterCode": "long count = names.___()\n    .___((name) -> name.startsWith(\"A\"))\n    .___();",
            "solution": "long count = names.stream()\n    .filter((name) -> name.startsWith(\"A\"))\n    .count();",
            "hint": "Use .stream(), .filter(), and .count().",
            "rubric": "Java Stream methods properly chained to produce count."
        },
        {
            "title": "Concurrency in Java",
            "theory": "## Threads and Runnables\nJava can execute code concurrently by implementing the `Runnable` interface or extending `Thread`.",
            "instructions": "## Task: Implement Runnable\n1. Create a class `Task` implementing `Runnable`.\n2. Override the `run` method to print \"Running\".",
            "starterCode": "class Task ___ ___ {\n    @Override\n    public void ___() {\n        System.out.println(\"Running\");\n    }\n}",
            "solution": "class Task implements Runnable {\n    @Override\n    public void run() {\n        System.out.println(\"Running\");\n    }\n}",
            "hint": "implements Runnable, public void run().",
            "rubric": "Runnable interface successfully implemented with run method."
        }
    ]
}

def add_new_lessons():
    with open(TRACK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    added = 0
    for course_name, new_lessons in NEW_LESSONS.items():
        if course_name in data:
            data[course_name]["lessons"].extend(new_lessons)
            added += len(new_lessons)
            print(f"[OK] {course_name}: +{len(new_lessons)} lessons")
        else:
            print(f"[WARN] Course not found: {course_name}")
    
    with open(TRACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\nDone! Added {added} new lessons to backend.json")

if __name__ == "__main__":
    add_new_lessons()
