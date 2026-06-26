"""
Phase 3: Add 49 new unique lessons to Frontend track.
"""
import json

TRACK_FILE = "curriculum/tracks/frontend.json"

NEW_LESSONS = {
    "HTML Essentials": [
        {
            "title": "Semantic HTML Tags",
            "theory": "## Semantic HTML\nSemantic HTML introduces meaning to the web page rather than just presentation.\nTags like `<header>`, `<footer>`, `<article>`, and `<section>` replace generic `<div>`s to help search engines and screen readers understand content structure.",
            "instructions": "## Task: Build a Semantic Article\n1. Use an `<article>` tag to wrap the main content.\n2. Inside, use a `<header>` with an `<h1>` for the title.\n3. Add a `<section>` with two `<p>` tags for content.\n4. Use a `<footer>` with author information.",
            "starterCode": "___>\n  ___>\n    <h1>Semantic Web</h1>\n  </___>\n  ___>\n    <p>Semantic tags are great.</p>\n    <p>They improve accessibility.</p>\n  </___>\n  ___>\n    <p>By Jane Doe</p>\n  </___>\n</___>",
            "solution": "<article>\n  <header>\n    <h1>Semantic Web</h1>\n  </header>\n  <section>\n    <p>Semantic tags are great.</p>\n    <p>They improve accessibility.</p>\n  </section>\n  <footer>\n    <p>By Jane Doe</p>\n  </footer>\n</article>",
            "hint": "Use <article>, <header>, <section>, and <footer> instead of <div>.",
            "rubric": "Code correctly uses article, header, section, and footer tags."
        },
        {
            "title": "HTML Lists & Tables",
            "theory": "## Lists and Tables\nHTML provides unordered `<ul>` and ordered `<ol>` lists, containing list items `<li>`.\nTables use `<table>`, with rows `<tr>`, headers `<th>`, and data cells `<td>`.",
            "instructions": "## Task: Create a Menu Table\n1. Create a table with two columns: 'Item' and 'Price'.\n2. Add two rows of data: 'Coffee' ($3) and 'Tea' ($2).\n3. Below the table, add an unordered list of 'Add-ons': 'Sugar', 'Milk'.",
            "starterCode": "___>\n  <tr>\n    ___>Item</___>\n    ___>Price</___>\n  </tr>\n  <tr>\n    ___>Coffee</___>\n    ___>$3</___>\n  </tr>\n  <tr>\n    ___>Tea</___>\n    ___>$2</___>\n  </tr>\n</___>\n\n___>\n  ___>Sugar</___>\n  ___>Milk</___>\n</___>",
            "solution": "<table>\n  <tr>\n    <th>Item</th>\n    <th>Price</th>\n  </tr>\n  <tr>\n    <td>Coffee</td>\n    <td>$3</td>\n  </tr>\n  <tr>\n    <td>Tea</td>\n    <td>$2</td>\n  </tr>\n</table>\n\n<ul>\n  <li>Sugar</li>\n  <li>Milk</li>\n</ul>",
            "hint": "Use <table>, <tr>, <th>, <td> for the table. Use <ul> and <li> for the unordered list.",
            "rubric": "Table and unordered list structure is complete and correct."
        },
        {
            "title": "HTML Forms and Inputs",
            "theory": "## Forms\nForms collect user input using `<form>`, `<input>`, `<label>`, and `<button>`.\nAlways link `<label>` to `<input>` using `for` and `id` attributes for accessibility.",
            "instructions": "## Task: Simple Contact Form\n1. Create a form.\n2. Add a text input with a corresponding label for 'Name'.\n3. Add an email input with a label for 'Email'.\n4. Add a submit button.",
            "starterCode": "___>\n  <___ ___=\"name\">Name:</___>\n  <input type=\"___\" id=\"name\" name=\"name\">\n  \n  <___ ___=\"email\">Email:</___>\n  <input type=\"___\" id=\"email\" name=\"email\">\n  \n  <___ type=\"submit\">Send</___>\n</___>",
            "solution": "<form>\n  <label for=\"name\">Name:</label>\n  <input type=\"text\" id=\"name\" name=\"name\">\n  \n  <label for=\"email\">Email:</label>\n  <input type=\"email\" id=\"email\" name=\"email\">\n  \n  <button type=\"submit\">Send</button>\n</form>",
            "hint": "Use <form>, <label for='id'>, <input type='text'/'email'>, and <button type='submit'>.",
            "rubric": "Form contains inputs with associated labels and a submit button."
        }
    ],
    "CSS Styling & Layout": [
        {
            "title": "CSS Box Model",
            "theory": "## Box Model\nEvery element is a box with content, padding, border, and margin.\n`box-sizing: border-box;` includes padding and border in the element's total width and height.",
            "instructions": "## Task: Style a Card\n1. Set the class `.card` to have `20px` padding, `2px solid black` border, and `15px` margin.\n2. Apply `border-box` sizing.",
            "starterCode": ".card {\n  box-sizing: ___;\n  padding: ___;\n  border: ___;\n  margin: ___;\n}",
            "solution": ".card {\n  box-sizing: border-box;\n  padding: 20px;\n  border: 2px solid black;\n  margin: 15px;\n}",
            "hint": "Use border-box for box-sizing. Provide correct values for padding, border, and margin.",
            "rubric": "Box model properties correctly applied."
        },
        {
            "title": "Flexbox Layout",
            "theory": "## Flexbox\nFlexbox is a one-dimensional layout method.\nSet `display: flex;` on a container. Use `justify-content` to align horizontally and `align-items` to align vertically.",
            "instructions": "## Task: Center Elements\n1. Use flexbox on `.container`.\n2. Center its children horizontally and vertically.",
            "starterCode": ".container {\n  display: ___;\n  justify-content: ___;\n  align-items: ___;\n  height: 100vh;\n}",
            "solution": ".container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100vh;\n}",
            "hint": "Use display: flex; justify-content: center; align-items: center;",
            "rubric": "Elements are perfectly centered using flexbox."
        },
        {
            "title": "CSS Grid Layout",
            "theory": "## CSS Grid\nGrid is a two-dimensional layout system.\nDefine rows and columns on a container using `grid-template-rows` and `grid-template-columns`.",
            "instructions": "## Task: Create a 3-Column Grid\n1. Apply `display: grid;` to `.grid`.\n2. Create 3 equal columns using `1fr`.\n3. Set a gap of `10px`.",
            "starterCode": ".grid {\n  display: ___;\n  grid-template-columns: ___ ___ ___;\n  gap: ___;\n}",
            "solution": ".grid {\n  display: grid;\n  grid-template-columns: 1fr 1fr 1fr;\n  gap: 10px;\n}",
            "hint": "Use display: grid, grid-template-columns with 1fr repeated 3 times, and gap: 10px.",
            "rubric": "Grid layout correctly implemented with 3 equal columns and a gap."
        }
    ],
    "JavaScript Basics": [
        {
            "title": "Variables and Data Types",
            "theory": "## JS Variables\nUse `let` for variables that change, and `const` for constants.\nPrimitives: string, number, boolean, null, undefined.",
            "instructions": "## Task: Declare Variables\n1. Declare a constant `name` with your name.\n2. Declare a variable `age` using `let`.\n3. Create a boolean `isStudent`.",
            "starterCode": "___ name = \"Alex\";\n___ age = 25;\n___ isStudent = ___;",
            "solution": "const name = \"Alex\";\nlet age = 25;\nlet isStudent = true;",
            "hint": "Use const for name, let for age and isStudent.",
            "rubric": "Variables correctly declared using let and const with appropriate types."
        },
        {
            "title": "Functions and Arrow Functions",
            "theory": "## Functions\nFunctions can be declared or written as arrow functions.\nArrow functions provide a concise syntax: `const add = (a, b) => a + b;`",
            "instructions": "## Task: Write Arrow Functions\n1. Write an arrow function `multiply` that takes two numbers and returns their product.\n2. Write an arrow function `greet` that takes a name and returns \"Hello, [name]\".",
            "starterCode": "const multiply = (a, b) => ___;\n\nconst greet = (name) => `___, ${___}`;\n\nconsole.log(multiply(3, 4));\nconsole.log(greet(\"Alice\"));",
            "solution": "const multiply = (a, b) => a * b;\n\nconst greet = (name) => `Hello, ${name}`;\n\nconsole.log(multiply(3, 4));\nconsole.log(greet(\"Alice\"));",
            "hint": "Use a * b for multiplication. Use template literals for greeting.",
            "rubric": "Arrow functions correctly implemented and return correct values."
        },
        {
            "title": "Arrays and Methods",
            "theory": "## Array Methods\nJS provides built-in methods to manipulate arrays: `push()`, `pop()`, `map()`, `filter()`.",
            "instructions": "## Task: Manipulate Arrays\n1. Create an array `nums` with numbers 1 to 5.\n2. Use `.map()` to create a new array `doubled` where each number is multiplied by 2.\n3. Use `.filter()` to create an array `evens` from `nums`.",
            "starterCode": "const nums = [1, 2, 3, 4, 5];\nconst doubled = nums.___((n) => n * ___);\nconst evens = nums.___((n) => n % ___ === 0);",
            "solution": "const nums = [1, 2, 3, 4, 5];\nconst doubled = nums.map((n) => n * 2);\nconst evens = nums.filter((n) => n % 2 === 0);",
            "hint": "Use .map(n => n * 2) and .filter(n => n % 2 === 0).",
            "rubric": "Array methods map and filter used correctly to generate new arrays."
        }
    ],
    "Forms & Validation": [
        {
            "title": "HTML5 Form Validation",
            "theory": "## HTML5 Validation\nUse attributes like `required`, `minlength`, `maxlength`, `min`, `max`, and `pattern` directly in HTML to validate input before JS.",
            "instructions": "## Task: Native Validation\n1. Make the username field required with a minimum length of 3.\n2. Make the age field accept numbers between 18 and 99.",
            "starterCode": "<input type=\"text\" name=\"username\" ___ ___=\"3\">\n<input type=\"number\" name=\"age\" ___=\"18\" ___=\"99\">",
            "solution": "<input type=\"text\" name=\"username\" required minlength=\"3\">\n<input type=\"number\" name=\"age\" min=\"18\" max=\"99\">",
            "hint": "Use required, minlength, min, and max attributes.",
            "rubric": "HTML inputs have correct validation attributes applied."
        },
        {
            "title": "Custom JS Validation",
            "theory": "## JS Validation\nSometimes HTML5 validation isn't enough. You can use JavaScript to listen to `submit` events, prevent default behavior, and run custom checks.",
            "instructions": "## Task: Password Match\n1. Write JS to check if `password` and `confirmPassword` inputs match.\n2. If they don't match, set an error message using `setCustomValidity()`.",
            "starterCode": "function validatePass(pwd, confirmPwd) {\n  if (pwd.value !== confirmPwd.___) {\n    confirmPwd.___(\"Passwords do not match\");\n  } else {\n    confirmPwd.___(\"\");\n  }\n}",
            "solution": "function validatePass(pwd, confirmPwd) {\n  if (pwd.value !== confirmPwd.value) {\n    confirmPwd.setCustomValidity(\"Passwords do not match\");\n  } else {\n    confirmPwd.setCustomValidity(\"\");\n  }\n}",
            "hint": "Compare .value properties. Use setCustomValidity to set or clear errors.",
            "rubric": "JavaScript logic correctly compares values and uses setCustomValidity."
        },
        {
            "title": "Handling Submit Events",
            "theory": "## Form Submission\nUse `e.preventDefault()` inside a `submit` event listener to stop the page from reloading, allowing you to process the form data using `FormData`.",
            "instructions": "## Task: Prevent Default and Get Data\n1. Add a submit event listener to `form`.\n2. Prevent the default form submission.\n3. Create a new `FormData` object from the form.",
            "starterCode": "form.addEventListener(\"___\", (e) => {\n  e.___();\n  const data = new ___(form);\n  console.log(data.get(\"username\"));\n});",
            "solution": "form.addEventListener(\"submit\", (e) => {\n  e.preventDefault();\n  const data = new FormData(form);\n  console.log(data.get(\"username\"));\n});",
            "hint": "Listen for 'submit'. Use e.preventDefault() and new FormData().",
            "rubric": "Event listener correctly prevents default behavior and extracts FormData."
        }
    ],
    "Responsive Design Basics": [
        {
            "title": "Media Queries",
            "theory": "## Media Queries\nUse `@media` rules to apply CSS based on viewport width. Mobile-first design starts with default styles and uses `min-width` to adapt for larger screens.",
            "instructions": "## Task: Mobile-First Styles\n1. Default `.container` background is `red`.\n2. Use a media query to change it to `blue` for screens wider than `600px`.",
            "starterCode": ".container {\n  background-color: red;\n}\n\n___ (___: 600px) {\n  .container {\n    background-color: ___;\n  }\n}",
            "solution": ".container {\n  background-color: red;\n}\n\n@media (min-width: 600px) {\n  .container {\n    background-color: blue;\n  }\n}",
            "hint": "Use @media and min-width.",
            "rubric": "Media query is correctly formatted with min-width."
        },
        {
            "title": "Relative Units",
            "theory": "## Relative Units\nUse `rem`, `em`, `vw`, and `vh` instead of fixed `px` to make layouts responsive.\n`rem` is relative to the root font size, while `vw` is relative to viewport width.",
            "instructions": "## Task: Fluid Typography and Layout\n1. Set root `html` font-size to `16px`.\n2. Set `.title` font-size to `2rem`.\n3. Set `.box` width to `50vw`.",
            "starterCode": "html {\n  font-size: ___px;\n}\n\n.title {\n  font-size: ___;\n}\n\n.box {\n  width: ___;\n}",
            "solution": "html {\n  font-size: 16px;\n}\n\n.title {\n  font-size: 2rem;\n}\n\n.box {\n  width: 50vw;\n}",
            "hint": "Use 16px, 2rem, and 50vw.",
            "rubric": "Correct relative units applied for responsive sizing."
        },
        {
            "title": "Responsive Images",
            "theory": "## Responsive Images\nMake images scale with their containers to prevent overflow. Set `max-width: 100%` and `height: auto`.",
            "instructions": "## Task: Fluid Image\n1. Apply CSS to `img` tags to ensure they never overflow their container.\n2. Maintain their aspect ratio.",
            "starterCode": "img {\n  max-width: ___;\n  height: ___;\n}",
            "solution": "img {\n  max-width: 100%;\n  height: auto;\n}",
            "hint": "Set max-width to 100% and height to auto.",
            "rubric": "Images are styled with max-width 100% and height auto."
        }
    ],
    "TypeScript: Beginner": [
        {
            "title": "Basic Types",
            "theory": "## Basic Types\nTypeScript adds static typing to JavaScript. Common types include `string`, `number`, `boolean`, `any`.",
            "instructions": "## Task: Annotate Variables\n1. Define `username` as a string.\n2. Define `userAge` as a number.\n3. Define `isActive` as a boolean.",
            "starterCode": "let username: ___ = \"Alice\";\nlet userAge: ___ = 30;\nlet isActive: ___ = true;",
            "solution": "let username: string = \"Alice\";\nlet userAge: number = 30;\nlet isActive: boolean = true;",
            "hint": "Use string, number, boolean.",
            "rubric": "Variables correctly typed with TS basic types."
        },
        {
            "title": "Function Typing",
            "theory": "## Function Types\nIn TS, you can define types for function parameters and return values.",
            "instructions": "## Task: Type a Function\n1. Write a function `add` taking two `number`s and returning a `number`.\n2. Write a void function `log` taking a `string`.",
            "starterCode": "function add(a: ___, b: ___): ___ {\n  return a + b;\n}\n\nfunction log(msg: ___): ___ {\n  console.log(msg);\n}",
            "solution": "function add(a: number, b: number): number {\n  return a + b;\n}\n\nfunction log(msg: string): void {\n  console.log(msg);\n}",
            "hint": "Parameters need :number, return type :number. For log, return type is :void.",
            "rubric": "Functions are fully typed including parameters and return types."
        },
        {
            "title": "Interfaces and Objects",
            "theory": "## Interfaces\nInterfaces define the shape of objects in TypeScript.",
            "instructions": "## Task: Create a User Interface\n1. Create an interface `User` with `id` (number), `name` (string), and optional `email` (string).\n2. Create an object `user1` implementing `User`.",
            "starterCode": "___ User {\n  id: ___;\n  name: ___;\n  email___: ___;\n}\n\nconst user1: ___ = {\n  id: 1,\n  name: \"Bob\"\n};",
            "solution": "interface User {\n  id: number;\n  name: string;\n  email?: string;\n}\n\nconst user1: User = {\n  id: 1,\n  name: \"Bob\"\n};",
            "hint": "Use `interface` keyword. Use `?` for optional properties.",
            "rubric": "Interface defined correctly with optional parameter and object assigned the interface type."
        }
    ],
    "DOM Manipulation": [
        {
            "title": "Querying Elements",
            "theory": "## DOM Selection\nUse `document.querySelector()` to find the first matching element, or `document.querySelectorAll()` to find all matching elements.",
            "instructions": "## Task: Select Elements\n1. Select the element with ID `header`.\n2. Select all elements with class `item`.",
            "starterCode": "const header = document.___(\"#___\");\nconst items = document.___(\".___\");",
            "solution": "const header = document.querySelector(\"#header\");\nconst items = document.querySelectorAll(\".item\");",
            "hint": "Use querySelector and querySelectorAll with CSS selectors.",
            "rubric": "Elements successfully selected using correct DOM methods."
        },
        {
            "title": "Creating and Appending Elements",
            "theory": "## Modifying DOM\nYou can create new HTML elements dynamically using `document.createElement()` and add them to the page using `appendChild()`.",
            "instructions": "## Task: Add a New List Item\n1. Create a new `<li>` element.\n2. Set its `textContent` to \"New Item\".\n3. Append it to an existing `<ul>` with ID `list`.",
            "starterCode": "const li = document.___(\"___\");\nli.___ = \"New Item\";\nconst list = document.querySelector(\"#list\");\nlist.___(li);",
            "solution": "const li = document.createElement(\"li\");\nli.textContent = \"New Item\";\nconst list = document.querySelector(\"#list\");\nlist.appendChild(li);",
            "hint": "Use createElement, textContent, and appendChild.",
            "rubric": "New element successfully created, populated, and appended."
        },
        {
            "title": "Event Delegation",
            "theory": "## Event Delegation\nInstead of adding an event listener to every child, add one listener to the parent and check `e.target` to see which child was clicked.",
            "instructions": "## Task: Delegate Clicks\n1. Add a click listener to the `#list` ul.\n2. If the clicked element is an `<li>`, log its text.",
            "starterCode": "const list = document.querySelector(\"#list\");\nlist.addEventListener(\"___\", (e) => {\n  if (e.___.tagName === \"___\") {\n    console.log(e.target.textContent);\n  }\n});",
            "solution": "const list = document.querySelector(\"#list\");\nlist.addEventListener(\"click\", (e) => {\n  if (e.target.tagName === \"LI\") {\n    console.log(e.target.textContent);\n  }\n});",
            "hint": "Listen for 'click', check e.target.tagName === 'LI'.",
            "rubric": "Event delegation logic uses e.target to identify the clicked child."
        }
    ],
    "Fetch API & AJAX": [
        {
            "title": "Basic Fetch",
            "theory": "## Fetch API\n`fetch()` makes HTTP requests and returns a Promise. Use `.json()` on the response to parse JSON data.",
            "instructions": "## Task: Fetch User Data\n1. Fetch data from `/api/user`.\n2. Parse the response as JSON.\n3. Log the data.",
            "starterCode": "fetch(\"___\")\n  .then(response => response.___())\n  .then(data => console.___(___));",
            "solution": "fetch(\"/api/user\")\n  .then(response => response.json())\n  .then(data => console.log(data));",
            "hint": "Use fetch('/api/user'), response.json(), and console.log(data).",
            "rubric": "Basic fetch chain with .then() parsing JSON correctly implemented."
        },
        {
            "title": "Async / Await with Fetch",
            "theory": "## Async/Await\n`async`/`await` makes asynchronous code look synchronous. Always wrap await calls in `try/catch` to handle errors.",
            "instructions": "## Task: Async Fetch\n1. Write an `async` function `getUser`.\n2. `await` the fetch call.\n3. `await` the JSON parsing.",
            "starterCode": "___ function getUser() {\n  try {\n    const response = ___ fetch(\"/api/user\");\n    const data = ___ response.___();\n    console.log(data);\n  } catch (err) {\n    console.error(err);\n  }\n}",
            "solution": "async function getUser() {\n  try {\n    const response = await fetch(\"/api/user\");\n    const data = await response.json();\n    console.log(data);\n  } catch (err) {\n    console.error(err);\n  }\n}",
            "hint": "Declare function as async, use await before fetch and response.json().",
            "rubric": "Async function defined correctly using await and try/catch."
        },
        {
            "title": "POST Requests",
            "theory": "## Sending Data\nTo send data via fetch, configure the second argument with `method: 'POST'`, set `headers`, and convert the body to a JSON string.",
            "instructions": "## Task: Send JSON Data\n1. Send a POST request to `/api/data`.\n2. Set `Content-Type` header to `application/json`.\n3. Send the object `{ name: 'Alice' }` as the body.",
            "starterCode": "fetch(\"/api/data\", {\n  ___: \"POST\",\n  headers: {\n    \"___\": \"application/json\"\n  },\n  body: JSON.___({ name: \"Alice\" })\n});",
            "solution": "fetch(\"/api/data\", {\n  method: \"POST\",\n  headers: {\n    \"Content-Type\": \"application/json\"\n  },\n  body: JSON.stringify({ name: \"Alice\" })\n});",
            "hint": "method is POST, header is Content-Type, and use JSON.stringify().",
            "rubric": "Fetch is configured for POST with correct headers and stringified body."
        }
    ],
    "ES6+ Modern JS": [
        {
            "title": "Destructuring",
            "theory": "## Destructuring\nExtract properties from objects and elements from arrays into distinct variables easily.",
            "instructions": "## Task: Object and Array Destructuring\n1. Destructure `name` and `age` from the `person` object.\n2. Destructure the first two elements from the `colors` array.",
            "starterCode": "const person = { name: \"Bob\", age: 30, job: \"Dev\" };\nconst { ___, ___ } = person;\n\nconst colors = [\"red\", \"green\", \"blue\"];\nconst [___, ___] = colors;",
            "solution": "const person = { name: \"Bob\", age: 30, job: \"Dev\" };\nconst { name, age } = person;\n\nconst colors = [\"red\", \"green\", \"blue\"];\nconst [color1, color2] = colors;",
            "hint": "Use {} for object destructuring and [] for arrays.",
            "rubric": "Properties successfully destructured from both object and array."
        },
        {
            "title": "Spread and Rest Operators",
            "theory": "## Spread and Rest (...)\nThe `...` operator spreads array/object elements, or collects remaining parameters into an array.",
            "instructions": "## Task: Use Spread and Rest\n1. Merge `arr1` and `arr2` into `merged` using spread.\n2. Create a function `sum` that takes an indefinite number of arguments using rest and sums them.",
            "starterCode": "const arr1 = [1, 2];\nconst arr2 = [3, 4];\nconst merged = [___, ___];\n\nfunction sum(___args) {\n  return args.reduce((acc, curr) => acc + curr, 0);\n}",
            "solution": "const arr1 = [1, 2];\nconst arr2 = [3, 4];\nconst merged = [...arr1, ...arr2];\n\nfunction sum(...args) {\n  return args.reduce((acc, curr) => acc + curr, 0);\n}",
            "hint": "Use ...arr1, ...arr2. For parameters use ...args.",
            "rubric": "Spread used to merge arrays, rest used to gather function arguments."
        },
        {
            "title": "Template Literals",
            "theory": "## Template Literals\nUse backticks `` to allow multi-line strings and string interpolation with `${expression}`.",
            "instructions": "## Task: Multi-line and Interpolation\n1. Use backticks to create a multi-line string containing a greeting for a variable `user`.",
            "starterCode": "const user = \"Charlie\";\nconst greeting = ___\n  Hello ${___},\n  Welcome to our site!\n___;",
            "solution": "const user = \"Charlie\";\nconst greeting = `\n  Hello ${user},\n  Welcome to our site!\n`;",
            "hint": "Wrap the string in backticks ` and use ${user}.",
            "rubric": "Template literals utilized correctly for multi-line and interpolation."
        }
    ],
    "CSS Animations": [
        {
            "title": "CSS Transitions",
            "theory": "## Transitions\nTransitions provide a way to control animation speed when changing CSS properties. Syntax: `transition: property duration timing-function;`",
            "instructions": "## Task: Button Hover Transition\n1. Add a transition to `.btn` for `background-color` lasting `0.3s` with `ease` timing.\n2. Change the background color on hover.",
            "starterCode": ".btn {\n  background-color: blue;\n  ___: background-color ___ ___;\n}\n\n.btn:___ {\n  background-color: red;\n}",
            "solution": ".btn {\n  background-color: blue;\n  transition: background-color 0.3s ease;\n}\n\n.btn:hover {\n  background-color: red;\n}",
            "hint": "Use 'transition' property and ':hover' pseudo-class.",
            "rubric": "Transition applied correctly to smoothly animate background-color."
        },
        {
            "title": "Keyframe Animations",
            "theory": "## @keyframes\n`@keyframes` define the steps in an animation. Apply it using the `animation` property.",
            "instructions": "## Task: Simple Fade In\n1. Define a `@keyframes` named `fadeIn` from opacity 0 to opacity 1.\n2. Apply the animation to `.box`, taking `2s` to complete.",
            "starterCode": "___ fadeIn {\n  from { opacity: ___; }\n  to { opacity: ___; }\n}\n\n.box {\n  ___: fadeIn ___ ease-in;\n}",
            "solution": "@keyframes fadeIn {\n  from { opacity: 0; }\n  to { opacity: 1; }\n}\n\n.box {\n  animation: fadeIn 2s ease-in;\n}",
            "hint": "Use @keyframes, 0, 1, and animation: fadeIn 2s.",
            "rubric": "Keyframes defined and animation property applied correctly."
        },
        {
            "title": "Transform Property",
            "theory": "## Transform\nThe `transform` property allows rotating, scaling, skewing, or translating elements.",
            "instructions": "## Task: Scale and Rotate\n1. Rotate the `.icon` element by `45deg`.\n2. Scale it to `1.5` times its size on hover.",
            "starterCode": ".icon {\n  transform: ___(___deg);\n  transition: transform 0.2s;\n}\n\n.icon:hover {\n  transform: ___(___);\n}",
            "solution": ".icon {\n  transform: rotate(45deg);\n  transition: transform 0.2s;\n}\n\n.icon:hover {\n  transform: scale(1.5);\n}",
            "hint": "Use rotate(45deg) and scale(1.5).",
            "rubric": "Transform properties rotate and scale are used successfully."
        }
    ],
    "LocalStorage & State": [
        {
            "title": "Storing and Retrieving Data",
            "theory": "## LocalStorage\n`localStorage` allows saving key/value string pairs in the browser that persist after page reload.",
            "instructions": "## Task: Save and Read\n1. Save the string \"dark\" under the key \"theme\".\n2. Retrieve the value and store it in `currentTheme`.",
            "starterCode": "localStorage.___(\"___\", \"dark\");\nconst currentTheme = localStorage.___(\"___\");",
            "solution": "localStorage.setItem(\"theme\", \"dark\");\nconst currentTheme = localStorage.getItem(\"theme\");",
            "hint": "Use setItem and getItem methods.",
            "rubric": "localStorage methods setItem and getItem are used properly."
        },
        {
            "title": "Storing JSON in LocalStorage",
            "theory": "## Storing Objects\nSince localStorage only stores strings, use `JSON.stringify()` before saving and `JSON.parse()` after retrieving objects/arrays.",
            "instructions": "## Task: Save an Array\n1. Stringify the `users` array and save it to `localStorage`.\n2. Retrieve it and parse it back into a JavaScript array.",
            "starterCode": "const users = [{id: 1, name: 'Alice'}];\nlocalStorage.setItem(\"users\", JSON.___(___));\n\nconst storedUsers = JSON.___(localStorage.getItem(\"users\"));",
            "solution": "const users = [{id: 1, name: 'Alice'}];\nlocalStorage.setItem(\"users\", JSON.stringify(users));\n\nconst storedUsers = JSON.parse(localStorage.getItem(\"users\"));",
            "hint": "Use JSON.stringify to save and JSON.parse to load.",
            "rubric": "JSON serialization techniques applied perfectly with localStorage."
        },
        {
            "title": "Removing Data",
            "theory": "## Clearing Storage\nUse `removeItem(key)` to delete a specific item, or `clear()` to wipe all data for the domain.",
            "instructions": "## Task: Logout User\n1. Remove the `token` key from localStorage.\n2. Then clear all localStorage completely.",
            "starterCode": "localStorage.___(\"token\");\nlocalStorage.___();",
            "solution": "localStorage.removeItem(\"token\");\nlocalStorage.clear();",
            "hint": "Use removeItem('token') and clear().",
            "rubric": "Data successfully deleted using removeItem and clear."
        }
    ],
    "TypeScript: Intermediate": [
        {
            "title": "Union and Intersection Types",
            "theory": "## Advanced Types\nUnion types (`|`) allow a value to be one of several types. Intersection types (`&`) combine multiple types into one.",
            "instructions": "## Task: Type Combinations\n1. Define `Status` as a union of \"success\", \"error\", or \"loading\".\n2. Combine `HasName` and `HasAge` interfaces into a new type `Person` using an intersection.",
            "starterCode": "type Status = ___ | ___ | ___;\n\ninterface HasName { name: string; }\ninterface HasAge { age: number; }\ntype Person = ___ ___ ___;",
            "solution": "type Status = \"success\" | \"error\" | \"loading\";\n\ninterface HasName { name: string; }\ninterface HasAge { age: number; }\ntype Person = HasName & HasAge;",
            "hint": "Use | for union and & for intersection.",
            "rubric": "Union and Intersection types properly formulated."
        },
        {
            "title": "Generics Basics",
            "theory": "## Generics\nGenerics `<T>` allow you to write reusable, type-safe functions and classes that work with any data type.",
            "instructions": "## Task: Generic Identity Function\n1. Create a function `identity` that takes an argument of type `T` and returns it.\n2. Call it explicitly with `string` type.",
            "starterCode": "function identity<___>(arg: ___): ___ {\n  return arg;\n}\n\nlet result = identity<___>(\"Hello\");",
            "solution": "function identity<T>(arg: T): T {\n  return arg;\n}\n\nlet result = identity<string>(\"Hello\");",
            "hint": "Use <T> for the generic parameter. Pass <string> when calling.",
            "rubric": "Generic function correctly defined and invoked with a type parameter."
        },
        {
            "title": "Enums",
            "theory": "## Enums\nEnums allow you to define a set of named constants, making intent clearer.",
            "instructions": "## Task: Define an Enum\n1. Define a string enum `Direction` with UP, DOWN, LEFT, RIGHT mapped to their string equivalents.\n2. Assign `Direction.UP` to a variable `move`.",
            "starterCode": "___ Direction {\n  UP = \"UP\",\n  DOWN = \"___\",\n  ___ = \"LEFT\",\n  ___ = \"RIGHT\"\n}\n\nlet move: Direction = Direction.___;",
            "solution": "enum Direction {\n  UP = \"UP\",\n  DOWN = \"DOWN\",\n  LEFT = \"LEFT\",\n  RIGHT = \"RIGHT\"\n}\n\nlet move: Direction = Direction.UP;",
            "hint": "Use enum keyword and ensure all members are defined as strings.",
            "rubric": "Enum correctly configured and utilized."
        }
    ],
    "React Fundamentals": [
        {
            "title": "Creating Components",
            "theory": "## React Components\nComponents are reusable pieces of UI. They are just JavaScript functions that return JSX.",
            "instructions": "## Task: Build a Greeting Component\n1. Create a functional component `Greeting`.\n2. Return an `<h1>` saying \"Hello, React!\".",
            "starterCode": "function ___() {\n  return (\n    ___>Hello, React!</___>\n  );\n}\n\nexport default Greeting;",
            "solution": "function Greeting() {\n  return (\n    <h1>Hello, React!</h1>\n  );\n}\n\nexport default Greeting;",
            "hint": "Define function Greeting() and return <h1>.",
            "rubric": "Functional component correctly defined and returns JSX."
        },
        {
            "title": "Props",
            "theory": "## Passing Data\nProps (properties) are used to pass data from a parent component down to a child component.",
            "instructions": "## Task: Using Props\n1. Modify `Greeting` to accept `props`.\n2. Render the `props.name` inside the `<h1>` instead of hardcoded text.",
            "starterCode": "function Greeting(___) {\n  return (\n    <h1>Hello, {___.___}!</h1>\n  );\n}",
            "solution": "function Greeting(props) {\n  return (\n    <h1>Hello, {props.name}!</h1>\n  );\n}",
            "hint": "Pass 'props' as parameter, use {props.name} inside JSX.",
            "rubric": "Props are passed to the component and rendered correctly."
        },
        {
            "title": "JSX Syntax and Rules",
            "theory": "## JSX\nJSX looks like HTML but is JavaScript. You must return a single parent element, use `className` instead of `class`, and close all tags.",
            "instructions": "## Task: Fix the JSX\n1. Wrap the adjacent `<h1>` and `<p>` in a single `<div>` or Fragment `<>`.\n2. Use `className` instead of HTML's `class` attribute.",
            "starterCode": "function App() {\n  return (\n    <___>\n      <h1 ___=\"title\">Title</h1>\n      <p>Content</p>\n    </___>\n  );\n}",
            "solution": "function App() {\n  return (\n    <>\n      <h1 className=\"title\">Title</h1>\n      <p>Content</p>\n    </>\n  );\n}",
            "hint": "Use fragments <> </> to wrap elements, and className for CSS classes.",
            "rubric": "JSX follows rules: single parent element and className attribute used."
        }
    ],
    "React Hooks & Context": [
        {
            "title": "useState Hook",
            "theory": "## useState\nThe `useState` hook allows functional components to have local state.",
            "instructions": "## Task: Counter State\n1. Import `useState`.\n2. Initialize state variable `count` to 0, and function `setCount`.\n3. Update the count on button click.",
            "starterCode": "import { ___ } from 'react';\n\nfunction Counter() {\n  const [___, ___] = useState(___);\n  \n  return (\n    <button onClick={() => ___(count + 1)}>\n      Count is {___}\n    </button>\n  );\n}",
            "solution": "import { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  \n  return (\n    <button onClick={() => setCount(count + 1)}>\n      Count is {count}\n    </button>\n  );\n}",
            "hint": "const [count, setCount] = useState(0).",
            "rubric": "useState is correctly imported, initialized, and state is updated."
        },
        {
            "title": "useEffect Hook",
            "theory": "## useEffect\n`useEffect` performs side effects (like data fetching) in function components. Provide a dependency array to control when it runs.",
            "instructions": "## Task: Run Effect Once\n1. Import `useEffect`.\n2. Add an effect that logs \"Mounted\" to the console.\n3. Ensure it only runs once by passing an empty dependency array.",
            "starterCode": "import { ___ } from 'react';\n\nfunction App() {\n  ___(() => {\n    console.log(\"Mounted\");\n  }, [___]);\n  return <div>App</div>;\n}",
            "solution": "import { useEffect } from 'react';\n\nfunction App() {\n  useEffect(() => {\n    console.log(\"Mounted\");\n  }, []);\n  return <div>App</div>;\n}",
            "hint": "Use useEffect and pass [] as the second argument.",
            "rubric": "useEffect implemented properly to fire only on component mount."
        },
        {
            "title": "useContext Hook",
            "theory": "## Context API\nContext provides a way to pass data through the component tree without passing props down manually.",
            "instructions": "## Task: Consume Context\n1. Import `useContext`.\n2. Consume the `ThemeContext`.\n3. Apply the theme as a CSS class to the div.",
            "starterCode": "import { ___ } from 'react';\nimport { ThemeContext } from './ThemeContext';\n\nfunction ThemedBox() {\n  const theme = ___(ThemeContext);\n  return <div className={___}>Box</div>;\n}",
            "solution": "import { useContext } from 'react';\nimport { ThemeContext } from './ThemeContext';\n\nfunction ThemedBox() {\n  const theme = useContext(ThemeContext);\n  return <div className={theme}>Box</div>;\n}",
            "hint": "Use useContext(ThemeContext) and inject theme into className.",
            "rubric": "Context is consumed and data is applied to the UI."
        }
    ],
    "Performance Optimization": [
        {
            "title": "React.memo",
            "theory": "## Component Memoization\n`React.memo` is a higher order component. It prevents functional components from re-rendering if their props haven't changed.",
            "instructions": "## Task: Memoize a Component\n1. Wrap the `ListItem` component export with `memo` to prevent unnecessary re-renders.",
            "starterCode": "import { ___ } from 'react';\n\nfunction ListItem({ item }) {\n  return <li>{item.name}</li>;\n}\n\nexport default ___(ListItem);",
            "solution": "import { memo } from 'react';\n\nfunction ListItem({ item }) {\n  return <li>{item.name}</li>;\n}\n\nexport default memo(ListItem);",
            "hint": "Import memo from React and wrap the component export.",
            "rubric": "Component is successfully wrapped with React.memo."
        },
        {
            "title": "useMemo and useCallback",
            "theory": "## Memoizing Values and Functions\n`useMemo` caches a calculated value, while `useCallback` caches a function definition, preventing them from being recreated on every render.",
            "instructions": "## Task: Cache a Calculation\n1. Use `useMemo` to cache the result of an expensive calculation.\n2. It should only recalculate when `inputData` changes.",
            "starterCode": "import { ___ } from 'react';\n\nfunction DataView({ inputData }) {\n  const processed = ___(() => {\n    return inputData.map(d => d * 2); // Expensive op\n  }, [___]);\n  \n  return <div>{processed.length} items</div>;\n}",
            "solution": "import { useMemo } from 'react';\n\nfunction DataView({ inputData }) {\n  const processed = useMemo(() => {\n    return inputData.map(d => d * 2); // Expensive op\n  }, [inputData]);\n  \n  return <div>{processed.length} items</div>;\n}",
            "hint": "Use useMemo and pass [inputData] in the dependency array.",
            "rubric": "useMemo applied perfectly with correct dependency array."
        }
    ],
    "Testing Frontend Code": [
        {
            "title": "Unit Testing with Jest",
            "theory": "## Unit Tests\nJest is a popular testing framework. Write tests to assert that a function behaves as expected.",
            "instructions": "## Task: Write a Simple Test\n1. Write a test for a function `add(a, b)`.\n2. Expect `add(2, 3)` to equal `5`.",
            "starterCode": "___('adds 2 + 3 to equal 5', () => {\n  ___(add(2, 3)).___(5);\n});",
            "solution": "test('adds 2 + 3 to equal 5', () => {\n  expect(add(2, 3)).toBe(5);\n});",
            "hint": "Use test(), expect(), and toBe().",
            "rubric": "Jest test correctly structured using expect and toBe assertions."
        },
        {
            "title": "React Testing Library",
            "theory": "## RTL Basics\nReact Testing Library tests components from the user's perspective, querying DOM nodes by text, role, or label.",
            "instructions": "## Task: Test Component Render\n1. Render the `<Button />` component.\n2. Query the button by its text \"Submit\".\n3. Assert that it is in the document.",
            "starterCode": "import { ___, screen } from '@testing-library/react';\nimport Button from './Button';\n\ntest('renders button', () => {\n  ___(<Button>Submit</Button>);\n  const btnElement = screen.___(/Submit/i);\n  expect(btnElement).toBeInTheDocument();\n});",
            "solution": "import { render, screen } from '@testing-library/react';\nimport Button from './Button';\n\ntest('renders button', () => {\n  render(<Button>Submit</Button>);\n  const btnElement = screen.getByText(/Submit/i);\n  expect(btnElement).toBeInTheDocument();\n});",
            "hint": "Use render() from RTL, and screen.getByText() to query elements.",
            "rubric": "Component rendered and queried correctly using RTL methods."
        }
    ],
    "Build Tools & Webpack": [
        {
            "title": "NPM Scripts",
            "theory": "## package.json Scripts\nNPM scripts automate tasks like starting a dev server, building for production, or running tests.",
            "instructions": "## Task: Add NPM Scripts\n1. In a `package.json` file snippet, add a `start` script to run `webpack serve`.\n2. Add a `build` script to run `webpack --mode production`.",
            "starterCode": "\"scripts\": {\n  \"start\": \"___\",\n  \"build\": \"___\"\n}",
            "solution": "\"scripts\": {\n  \"start\": \"webpack serve\",\n  \"build\": \"webpack --mode production\"\n}",
            "hint": "Provide 'webpack serve' and 'webpack --mode production'.",
            "rubric": "Standard NPM scripts for a Webpack project defined correctly."
        },
        {
            "title": "Webpack Configuration",
            "theory": "## Webpack Basics\nWebpack bundles JS modules. You need an `entry` point (where it starts) and an `output` (where the bundle goes).",
            "instructions": "## Task: Basic Webpack Setup\n1. Set the Webpack `entry` to `./src/index.js`.\n2. Set the `output` filename to `bundle.js`.",
            "starterCode": "module.exports = {\n  ___: './src/index.js',\n  ___: {\n    filename: '___',\n    path: __dirname + '/dist'\n  }\n};",
            "solution": "module.exports = {\n  entry: './src/index.js',\n  output: {\n    filename: 'bundle.js',\n    path: __dirname + '/dist'\n  }\n};",
            "hint": "Define 'entry' and 'output' with 'bundle.js'.",
            "rubric": "Basic webpack configuration for entry and output is valid."
        }
    ],
    "TypeScript: Advanced": [
        {
            "title": "Utility Types",
            "theory": "## TS Utility Types\nTypeScript provides utilities like `Partial<T>`, `Readonly<T>`, `Pick<T, K>`, and `Omit<T, K>` to transform existing types.",
            "instructions": "## Task: Use Partial and Omit\n1. Create a `User` interface with `id`, `name`, `email`.\n2. Use `Partial` to create an `UpdateUser` type where all fields are optional.\n3. Use `Omit` to create a `NewUser` type omitting the `id`.",
            "starterCode": "interface User { id: number; name: string; email: string; }\n\ntype UpdateUser = ___<User>;\ntype NewUser = ___<User, \"___\">;",
            "solution": "interface User { id: number; name: string; email: string; }\n\ntype UpdateUser = Partial<User>;\ntype NewUser = Omit<User, \"id\">;",
            "hint": "Use Partial<User> and Omit<User, 'id'>.",
            "rubric": "Advanced utility types Partial and Omit are utilized accurately."
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
    
    print(f"\nDone! Added {added} new lessons to frontend.json")

if __name__ == "__main__":
    add_new_lessons()
