"""
Add absolute beginner lessons to HTML5 Essentials course.
Inserts 5 new introductory lessons BEFORE the existing lessons.
"""
import json
import re

# Read the courses.js file
with open(r'frontend\src\data\courses.js', 'r', encoding='utf-8') as f:
    content = f.read()

# New absolute beginner lessons to insert before the existing ones
new_lessons = [
    {
        "title": "What is HTML?",
        "theory": """## Your Very First Step into Web Development

Have you ever wondered how websites are made? Every website you visit — Google, Instagram, YouTube — is built using **HTML**.

**HTML** stands for **HyperText Markup Language**. Don't let the big name scare you! It's simply a way to tell the browser (Chrome, Safari, Firefox) what to show on a page.

### Think of it Like This

Imagine you're decorating a room:
- HTML is the **furniture and walls** — it decides WHAT goes where (a couch here, a table there)
- CSS (which you'll learn later) is the **paint and decorations** — it makes things look pretty
- JavaScript (also later) is the **electricity** — it makes things interactive

### Tags — The Building Blocks

HTML uses **tags** to create elements. Tags look like this:

```html
<h1>Hello World!</h1>
```

Let's break this down:
- `<h1>` is the **opening tag** — it says "start a big heading here"
- `Hello World!` is the **content** — the actual text you see
- `</h1>` is the **closing tag** — it says "end the heading here" (notice the `/`)

That's it! You just learned your first HTML tag. `<h1>` creates the biggest heading on a page.

### Important Rules
1. Most tags come in pairs: an opening `<tag>` and a closing `</tag>`
2. Tags are NOT case-sensitive, but always write them in **lowercase**
3. You can put tags inside other tags (called **nesting**)

```html
<p>This is a paragraph of text.</p>
<p>This is another paragraph.</p>
```

`<p>` stands for **paragraph** — it creates a block of text.""",
        "instructions": "## Task: Write Your First HTML\n1. Create a heading using the `<h1>` tag with the text 'My First Website'\n2. Create a paragraph using the `<p>` tag with a sentence about yourself\n3. Create another paragraph with what you want to learn",
        "starterCode": "<___>My First Website</___>\n<___>Hello! My name is ___.</___>\n<___>I want to learn ___.</___>",
        "solution": "<h1>My First Website</h1>\n<p>Hello! My name is Mabel.</p>\n<p>I want to learn web development.</p>",
        "hint": "h1 for headings, p for paragraphs. Don't forget the closing tags with /",
        "rubric": "Uses h1 for heading and p for paragraphs. All tags properly opened and closed."
    },
    {
        "title": "Headings & Paragraphs",
        "theory": """## Organizing Text on a Page

Just like a book has a title, chapter headings, and paragraphs — a web page uses **headings** and **paragraphs** to organize text.

### The 6 Heading Levels

HTML gives you 6 sizes of headings, from biggest (`<h1>`) to smallest (`<h6>`):

```html
<h1>This is Heading 1 — The Biggest (Page Title)</h1>
<h2>This is Heading 2 — Section Title</h2>
<h3>This is Heading 3 — Sub-section</h3>
<h4>This is Heading 4 — Smaller</h4>
<h5>This is Heading 5 — Even Smaller</h5>
<h6>This is Heading 6 — The Smallest</h6>
```

**Important Rule:** Only use **ONE** `<h1>` per page — it's the main title. Think of it like a book: one title, many chapter headings.

### Paragraphs

The `<p>` tag creates a paragraph. Each paragraph gets its own line with some space above and below:

```html
<p>This is the first paragraph. The browser adds spacing automatically.</p>
<p>This is the second paragraph. Notice the gap between them.</p>
```

### Line Breaks and Horizontal Rules

Sometimes you need a line break without starting a new paragraph:

```html
<p>
  Roses are red,<br>
  Violets are blue,<br>
  HTML is fun,<br>
  And so are you!
</p>
```

`<br>` is a **self-closing tag** — it doesn't need a closing `</br>`.

To add a horizontal line (divider) across the page:

```html
<h2>Chapter 1</h2>
<p>Once upon a time...</p>
<hr>
<h2>Chapter 2</h2>
<p>The adventure continues...</p>
```

`<hr>` is also self-closing — it draws a line across the page.

### Bold, Italic, and More

You can style text inside paragraphs:

```html
<p>This word is <strong>bold</strong> and important.</p>
<p>This word is <em>italic</em> for emphasis.</p>
<p>This is <u>underlined</u> text.</p>
<p>This is <del>deleted</del> text (crossed out).</p>
<p>This text has a <mark>highlighted</mark> part.</p>
```

- `<strong>` = **bold** (means this text is important)
- `<em>` = *italic* (means emphasis)""",
        "instructions": "## Task: Create a Blog Post\n1. Add an `<h1>` page title: 'My Learning Journey'\n2. Add an `<h2>` section heading: 'Week 1'\n3. Write a `<p>` paragraph about what you learned\n4. Make one word **bold** using `<strong>` and one *italic* using `<em>`",
        "starterCode": "<h1>___</h1>\n<h2>___</h2>\n<p>I started learning <strong>___</strong> this week. It was <em>___</em> exciting!</p>",
        "solution": "<h1>My Learning Journey</h1>\n<h2>Week 1</h2>\n<p>I started learning <strong>HTML</strong> this week. It was <em>really</em> exciting!</p>",
        "hint": "h1 for the main title, h2 for sections. strong for bold, em for italic.",
        "rubric": "Uses h1 and h2 correctly. Paragraph has strong and em tags with content."
    },
    {
        "title": "Lists — Ordered & Unordered",
        "theory": """## Making Lists in HTML

Lists are everywhere on the web — shopping carts, navigation menus, recipe steps, to-do lists. HTML gives you two types of lists.

### Unordered Lists (Bullet Points)

Use `<ul>` when the order doesn't matter:

```html
<h2>My Favorite Foods</h2>
<ul>
  <li>Jollof Rice</li>
  <li>Suya</li>
  <li>Pounded Yam</li>
  <li>Chin Chin</li>
</ul>
```

This shows:
- Jollof Rice
- Suya
- Pounded Yam
- Chin Chin

### Ordered Lists (Numbered)

Use `<ol>` when the order DOES matter:

```html
<h2>How to Make Tea</h2>
<ol>
  <li>Boil water</li>
  <li>Put tea bag in cup</li>
  <li>Pour hot water</li>
  <li>Add sugar and milk</li>
  <li>Stir and enjoy!</li>
</ol>
```

This shows:
1. Boil water
2. Put tea bag in cup
3. Pour hot water
4. Add sugar and milk
5. Stir and enjoy!

### The Rules

- `<ul>` = **U**nordered **L**ist (bullets)
- `<ol>` = **O**rdered **L**ist (numbers)
- `<li>` = **L**ist **I**tem (goes inside `<ul>` or `<ol>`)
- You can ONLY put `<li>` directly inside `<ul>` or `<ol>`

### Nesting Lists (Lists inside Lists)

```html
<ul>
  <li>Frontend
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>Backend
    <ul>
      <li>Python</li>
      <li>Node.js</li>
    </ul>
  </li>
</ul>
```

This creates an indented sub-list inside each item — perfect for showing categories!""",
        "instructions": "## Task: Create Two Lists\n1. Create an **unordered list** (`<ul>`) of 3 programming languages you want to learn\n2. Create an **ordered list** (`<ol>`) of 3 steps to become a developer\n3. Add a heading above each list",
        "starterCode": "<h2>Languages I Want to Learn</h2>\n<___>\n  <li>___</li>\n  <li>___</li>\n  <li>___</li>\n</___>\n\n<h2>Steps to Become a Developer</h2>\n<___>\n  <li>___</li>\n  <li>___</li>\n  <li>___</li>\n</___>",
        "solution": "<h2>Languages I Want to Learn</h2>\n<ul>\n  <li>Python</li>\n  <li>JavaScript</li>\n  <li>HTML</li>\n</ul>\n\n<h2>Steps to Become a Developer</h2>\n<ol>\n  <li>Learn the basics</li>\n  <li>Build projects</li>\n  <li>Never stop learning</li>\n</ol>",
        "hint": "ul for bullet points (unordered), ol for numbered (ordered). Each item uses li.",
        "rubric": "Has ul with 3 li items and ol with 3 li items. Headings present above each list."
    },
    {
        "title": "Links — Connecting Pages",
        "theory": """## Making Text Clickable

Links are what make the web... a WEB! They let you jump from one page to another. Without links, every page would be an island.

### The `<a>` Tag (Anchor)

The `<a>` tag creates a clickable link. The `href` attribute tells the browser WHERE to go:

```html
<a href="https://google.com">Click here to visit Google</a>
```

Let's break this down:
- `<a>` — the anchor (link) tag
- `href="https://google.com"` — the **destination** (where to go when clicked)
- `Click here to visit Google` — the **text the user sees** on the page
- `</a>` — closing tag

### Opening Links in a New Tab

By default, links open in the SAME tab (replacing the current page). To open in a new tab:

```html
<a href="https://youtube.com" target="_blank">Watch on YouTube</a>
```

`target="_blank"` means "open this in a blank (new) tab."

### Different Types of Links

```html
<!-- Link to another website -->
<a href="https://github.com">Visit GitHub</a>

<!-- Link to an email address -->
<a href="mailto:hello@example.com">Email Me</a>

<!-- Link to a phone number -->
<a href="tel:+2348012345678">Call Me</a>

<!-- Link to a section on the SAME page -->
<a href="#about">Jump to About Section</a>

<!-- ...then somewhere below on the page: -->
<h2 id="about">About Me</h2>
<p>I am a developer...</p>
```

### What is an Attribute?

You've now seen `href`, `target`, and `id`. These are called **attributes** — they give extra information to HTML tags:

```html
<tag attribute="value">Content</tag>
```

Think of attributes as settings for a tag. The `<a>` tag needs the `href` attribute to know where to link to.""",
        "instructions": "## Task: Create a Link Collection\n1. Create a link to Google that opens in a new tab\n2. Create a link to your email address\n3. Create a link that jumps to a section called 'skills' on the same page\n4. Create the skills section with an `id`",
        "starterCode": "<a href='___' target='___'>Visit Google</a>\n<a href='mailto:___'>Email Me</a>\n<a href='#___'>Jump to My Skills</a>\n\n<h2 id='___'>My Skills</h2>\n<p>I know HTML!</p>",
        "solution": "<a href='https://google.com' target='_blank'>Visit Google</a>\n<a href='mailto:hello@example.com'>Email Me</a>\n<a href='#skills'>Jump to My Skills</a>\n\n<h2 id='skills'>My Skills</h2>\n<p>I know HTML!</p>",
        "hint": "href needs the full URL with https://. target='_blank' for new tab. Use # for same-page links.",
        "rubric": "3 links with correct href values. Section has matching id. New tab link uses target."
    },
    {
        "title": "Images — Adding Pictures",
        "theory": """## Putting Images on Your Page

A website without images would be boring! The `<img>` tag lets you display pictures on your page.

### The `<img>` Tag

```html
<img src="photo.jpg" alt="A cute cat sitting on a laptop">
```

The `<img>` tag is special — it's **self-closing** (no `</img>` needed!). It has two required attributes:

- `src` — the **source** (where the image file is). This can be:
  - A file name: `"photo.jpg"`
  - A web URL: `"https://example.com/photo.jpg"`
- `alt` — **alternative text** (describes the image). This is VERY important because:
  - Screen readers read it aloud for blind users
  - It shows if the image fails to load
  - Search engines use it to understand your images

### Controlling Image Size

```html
<!-- Set width (height adjusts automatically) -->
<img src="logo.png" alt="Company logo" width="200">

<!-- Set both width and height -->
<img src="avatar.jpg" alt="Profile photo" width="150" height="150">
```

### Using Images from the Internet

You can use any image URL from the web:

```html
<img src="https://via.placeholder.com/300x200" alt="Placeholder image" width="300">
```

### Making an Image Clickable

Wrap an `<img>` inside an `<a>` tag:

```html
<a href="https://example.com">
  <img src="banner.jpg" alt="Click this banner to visit our site">
</a>
```

### The `<figure>` and `<figcaption>` Tags

For images with a caption (like in a textbook):

```html
<figure>
  <img src="chart.png" alt="Sales growth chart">
  <figcaption>Figure 1: Our sales grew by 200% this year</figcaption>
</figure>
```

### Common Image Formats
- `.jpg` / `.jpeg` — Photos (good quality, small file size)
- `.png` — Graphics with transparency (logos, icons)
- `.gif` — Animated images
- `.svg` — Scalable graphics (logos that zoom perfectly)
- `.webp` — Modern format (best quality + smallest size)""",
        "instructions": "## Task: Create an Image Gallery\n1. Add an image using a placeholder URL with alt text\n2. Set the image width to 300\n3. Make a second image that is clickable (links to a website)\n4. Add a figure with a caption",
        "starterCode": "<img src='https://via.placeholder.com/300x200' alt='___' width='___'>\n\n<a href='___'>\n  <img src='https://via.placeholder.com/200x200' alt='___'>\n</a>\n\n<figure>\n  <img src='https://via.placeholder.com/400x250' alt='___'>\n  <figcaption>___</figcaption>\n</figure>",
        "solution": "<img src='https://via.placeholder.com/300x200' alt='A beautiful landscape' width='300'>\n\n<a href='https://google.com'>\n  <img src='https://via.placeholder.com/200x200' alt='Click to visit Google'>\n</a>\n\n<figure>\n  <img src='https://via.placeholder.com/400x250' alt='My project screenshot'>\n  <figcaption>Figure 1: My first web project</figcaption>\n</figure>",
        "hint": "img is self-closing (no </img>). Always include alt text. Wrap img in <a> to make it clickable.",
        "rubric": "3 images with alt text. One has width set. One is wrapped in a link. Figure has figcaption."
    }
]

# Find the HTML5 Essentials course and its lessons array
# We need to insert the new lessons at the beginning of the lessons array

# Find the start of HTML5 Essentials lessons array
marker = '"HTML5 Essentials": {'
marker_pos = content.find(marker)
if marker_pos == -1:
    print("ERROR: Could not find 'HTML5 Essentials' in courses.js")
    exit(1)

print(f"Found HTML5 Essentials at position {marker_pos}")

# Find the lessons array opening bracket
lessons_start_marker = '"lessons": ['
lessons_pos = content.find(lessons_start_marker, marker_pos)
if lessons_pos == -1:
    print("ERROR: Could not find lessons array")
    exit(1)

# Position right after the opening bracket
insert_pos = lessons_pos + len(lessons_start_marker)

print(f"Found lessons array at position {lessons_pos}")

# Build the JSON for new lessons
new_lessons_json = ""
for lesson in new_lessons:
    lesson_json = json.dumps(lesson, ensure_ascii=False)
    new_lessons_json += "\n      " + lesson_json + ","

# Insert the new lessons
new_content = content[:insert_pos] + new_lessons_json + content[insert_pos:]

# Write back
with open(r'frontend\src\data\courses.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nSuccessfully added {len(new_lessons)} beginner lessons to HTML5 Essentials!")
print("New lesson order:")
for i, lesson in enumerate(new_lessons):
    print(f"  {i+1}. {lesson['title']} (NEW)")
print(f"  {len(new_lessons)+1}. HTML Document Structure (existing)")
print(f"  {len(new_lessons)+2}. Links & Images (existing)")
print(f"  {len(new_lessons)+3}. Forms & Inputs (existing)")
