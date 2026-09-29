import json
import re

with open(r'frontend\src\data\courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

# ----------------- CSS STYLING NEW LESSONS -----------------
new_css_lessons = [
    {
        "title": "What is CSS?",
        "theory": """## Painting the Web

If HTML is the walls and furniture of a house, **CSS** (Cascading Style Sheets) is the paint, the wallpaper, and the lighting. Without CSS, every website would look like a plain, boring text document from 1995.

### How to use CSS

You can add CSS to an HTML file in three ways, but the best way is an **External CSS File**.

You create a file called `styles.css` and link it in your HTML `<head>`:
```html
<link rel="stylesheet" href="styles.css">
```

### The Basic Syntax

A CSS "Rule" has a **Selector** (what you want to style) and **Declarations** (how you want it to look).

```css
/* This targets all <h1> headings */
h1 {
  color: blue;
  text-align: center;
  font-size: 24px;
}
```
- `h1` is the **selector**.
- `color: blue;` is a declaration.
- Notice the curly braces `{ }` and the semicolons `;`. The semicolon is CRITICAL!

### Colors and Backgrounds

You can change text color and background color easily:

```css
body {
  background-color: lightgray;
  color: #333333; /* Dark gray text */
}

p {
  color: red;
  background-color: yellow; /* Highlighting a paragraph! */
}
```

Colors can be written as names (`red`), Hex codes (`#FF0000`), or RGB values (`rgb(255, 0, 0)`).""",
        "instructions": "## Task: Paint the Text\n1. Write a CSS rule targeting the `h1` element.\n2. Set its text color to 'red'.\n3. Set its background-color to 'black'.",
        "starterCode": "___ {\n  color: ___;\n  background-color: ___;\n}",
        "solution": "h1 {\n  color: red;\n  background-color: black;\n}",
        "hint": "Use h1 as the selector. Don't forget semicolons!",
        "rubric": "Targets h1. Uses color and background-color correctly."
    },
    {
        "title": "The Box Model",
        "theory": """## Everything is a Box

This is the most important concept in CSS: **Every single HTML element is a rectangular box.**

Even if an image is a circle, the browser treats it as a rectangular box. The **CSS Box Model** defines how these boxes are spaced out.

### The 4 Layers of the Box

From the inside out, every element has:
1. **Content**: The actual text or image.
2. **Padding**: The clear space *inside* the border, around the content.
3. **Border**: The line that goes around the padding and content.
4. **Margin**: The clear space *outside* the border. It pushes other elements away.

```text
+-----------------------------------+
|             Margin                |
|  +-----------------------------+  |
|  |          Border             |  |
|  |  +-----------------------+  |  |
|  |  |       Padding         |  |  |
|  |  |  +-----------------+  |  |  |
|  |  |  |    CONTENT      |  |  |  |
|  |  |  +-----------------+  |  |  |
|  |  +-----------------------+  |  |
|  +-----------------------------+  |
+-----------------------------------+
```

### Writing Box Model CSS

```css
.my-box {
  /* 1. Content Size */
  width: 200px;
  height: 100px;
  
  /* 2. Padding (Inside space) */
  padding: 20px;
  
  /* 3. Border (The visible edge) */
  border: 2px solid black;
  
  /* 4. Margin (Outside space pushing others away) */
  margin: 30px;
}
```

### The Shorthand Trick

You can specify different sides: Top, Right, Bottom, Left (Clockwise!).
```css
/* top right bottom left */
margin: 10px 20px 30px 40px;

/* top/bottom right/left */
padding: 10px 20px; 
```""",
        "instructions": "## Task: Style a Box\n1. Create a `.box` class.\n2. Give it a width of 100px.\n3. Add 10px of padding.\n4. Add a 1px solid black border.\n5. Add a 20px margin.",
        "starterCode": ".box {\n  width: ___px;\n  padding: ___px;\n  border: ___px solid ___;\n  margin: ___px;\n}",
        "solution": ".box {\n  width: 100px;\n  padding: 10px;\n  border: 1px solid black;\n  margin: 20px;\n}",
        "hint": "Just fill in the numbers and the color black.",
        "rubric": "Box model properties correctly filled in."
    }
]

# ----------------- JS BASICS NEW LESSONS -----------------
new_js_lessons = [
    {
        "title": "What is JavaScript?",
        "theory": """## Adding Life to the Web

- **HTML** provides the structure (nouns).
- **CSS** provides the styling (adjectives).
- **JavaScript** provides the interactivity (verbs).

Without JavaScript, clicking a button on a website wouldn't do anything. JavaScript allows you to change the page *after* it has loaded.

### Connecting JS to HTML

Just like CSS, you usually put your JavaScript in a separate file (e.g., `app.js`) and link it at the very bottom of your HTML `<body>`:

```html
<body>
  <h1>Welcome!</h1>
  <script src="app.js"></script>
</body>
```

### Your First Commands

JavaScript runs commands line by line. Here are two basic ones:

```javascript
// This pops up a small alert box on the user's screen
alert("Welcome to my website!");

// This prints a message invisibly to the Developer Console
console.log("The page has loaded successfully.");
```

### Variables (Storing Data)

A variable is like a labeled box where you can store data to use later. 

```javascript
// 'let' allows the value to change later
let playerName = "Mabel";
let score = 0;

// You can update the variable:
score = score + 10;
console.log("Your score is now: " + score);

// 'const' is for values that NEVER change
const gravity = 9.8;
```""",
        "instructions": "## Task: Basic Variables\n1. Create a variable called `playerName` using `let` and set it to your name.\n2. Create a variable called `health` using `let` and set it to 100.\n3. Subtract 20 from health.",
        "starterCode": "___ playerName = \"___\";\n___ health = 100;\n\nhealth = health - ___;\nconsole.log(playerName + \" has \" + health + \" health left.\");",
        "solution": "let playerName = \"Mabel\";\nlet health = 100;\n\nhealth = health - 20;\nconsole.log(playerName + \" has \" + health + \" health left.\");",
        "hint": "Use 'let' to declare the variables so they can change.",
        "rubric": "Variables declared with let and math correctly applied."
    },
    {
        "title": "If/Else Statements",
        "theory": """## Making Decisions in Code

Programs need to make decisions. If a user enters the right password, log them in. If they enter the wrong one, show an error. We do this using **If Statements**.

### The Syntax

```javascript
let age = 18;

if (age >= 18) {
  // This code runs IF the condition is true
  console.log("You can vote!");
} else {
  // This code runs IF the condition is false
  console.log("You are too young to vote.");
}
```

### Comparison Operators

To make decisions, you need to compare things:
- `===` : Is exactly equal to (always use 3 equals signs in JS!)
- `!==` : Is NOT equal to
- `>`   : Greater than
- `<`   : Less than
- `>=`  : Greater than or equal to
- `<=`  : Less than or equal to

### Else If (Multiple Conditions)

You can chain multiple checks together using `else if`:

```javascript
let score = 85;

if (score >= 90) {
  console.log("Grade: A");
} else if (score >= 80) {
  console.log("Grade: B");
} else if (score >= 70) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}
```
The computer checks them top to bottom. As soon as it finds one that is `true`, it runs that block and skips the rest!""",
        "instructions": "## Task: Password Checker\n1. Write an if statement that checks if the `password` variable is exactly equal to `\"secret123\"`.\n2. If true, log `\"Access Granted\"`.\n3. Else, log `\"Access Denied\"`.",
        "starterCode": "let password = \"wrongpass\";\n\nif (password ___ \"secret123\") {\n  console.log(\"___\");\n} else {\n  console.log(\"___\");\n}",
        "solution": "let password = \"wrongpass\";\n\nif (password === \"secret123\") {\n  console.log(\"Access Granted\");\n} else {\n  console.log(\"Access Denied\");\n}",
        "hint": "Use === for exact equality. Watch your spelling on the console logs.",
        "rubric": "Uses === correctly and logs the appropriate strings."
    }
]


# Insert CSS Styling lessons
css_marker = '"CSS Styling": {'
css_pos = content.find(css_marker)
css_lessons_pos = content.find('"lessons": [', css_pos) + len('"lessons": [')

css_json = ""
for lesson in new_css_lessons:
    css_json += "\n      " + json.dumps(lesson, ensure_ascii=False) + ","

content = content[:css_lessons_pos] + css_json + content[css_lessons_pos:]


# Insert JS Basics lessons
js_marker = '"JS Basics": {'
js_pos = content.find(js_marker)
js_lessons_pos = content.find('"lessons": [', js_pos) + len('"lessons": [')

js_json = ""
for lesson in new_js_lessons:
    js_json += "\n      " + json.dumps(lesson, ensure_ascii=False) + ","

content = content[:js_lessons_pos] + js_json + content[js_lessons_pos:]

# Write back
with open(r'frontend\src\data\courses.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added beginner lessons to CSS Styling and JS Basics!")
