"""
Batch 6: Massive Expansion for JS, C/C++, AI, and more.
"""
import json

NEW_LESSONS = {

"DOM Manipulation": [
  {
    "title": "Selecting Elements",
    "theory": "## The Document Object Model (DOM)\n```js\n// Select by ID\nconst header = document.getElementById('main-title');\n\n// Select by class (returns HTMLCollection)\nconst cards = document.getElementsByClassName('card');\n\n// Select using CSS selectors (Modern)\nconst firstButton = document.querySelector('.btn-primary');\nconst allButtons = document.querySelectorAll('button');\n```",
    "instructions": "## Task: Query Selectors\nUse `querySelector` to get the element with ID `header` and class `item`.",
    "starterCode": "const js_code = `\nconst header = document.querySelector('___');\nconst firstItem = document.querySelector('___');\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst header = document.querySelector('#header');\nconst firstItem = document.querySelector('.item');\n`;\nconsole.log(js_code);",
    "hint": "Use # for ID and . for class in querySelector.",
    "rubric": "Correct CSS selectors used."
  },
  {
    "title": "Changing Content & Styles",
    "theory": "## Editing Elements\n```js\nconst box = document.querySelector('.box');\n// Change text\nbox.textContent = 'Hello World';\n// Change HTML\nbox.innerHTML = '<strong>Bold Text</strong>';\n// Change Styles\nbox.style.backgroundColor = 'blue';\n```",
    "instructions": "## Task: Update the Page\nChange the `textContent` of a title, and make its text color `red`.",
    "starterCode": "const js_code = `\nconst title = document.querySelector('h1');\ntitle.___ = 'Welcome';\ntitle.___.color = '___';\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst title = document.querySelector('h1');\ntitle.textContent = 'Welcome';\ntitle.style.color = 'red';\n`;\nconsole.log(js_code);",
    "hint": "Use textContent for text. Access styles via element.style.",
    "rubric": "textContent and style properties correctly manipulated."
  },
  {
    "title": "Event Listeners",
    "theory": "## Handling Events\n```js\nconst btn = document.querySelector('button');\nbtn.addEventListener('click', function(event) {\n    alert('Button clicked!');\n});\n```",
    "instructions": "## Task: Click Event\nAttach a click event listener to a button that logs 'Clicked'.",
    "starterCode": "const js_code = `\nconst btn = document.querySelector('button');\nbtn.___('___', () => {\n  console.log('Clicked');\n});\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst btn = document.querySelector('button');\nbtn.addEventListener('click', () => {\n  console.log('Clicked');\n});\n`;\nconsole.log(js_code);",
    "hint": "Use addEventListener('click', ...)",
    "rubric": "addEventListener and click event used."
  }
],

"Fetch API & AJAX": [
  {
    "title": "Promises in JavaScript",
    "theory": "## Promises\nA Promise represents a value that may be available now, or in the future.\n```js\nconst myPromise = new Promise((resolve, reject) => {\n  setTimeout(() => resolve('Done!'), 1000);\n});\nmyPromise.then(result => console.log(result));\n```",
    "instructions": "## Task: Resolve a Promise\nWrite a Promise that resolves with the text 'Success'.",
    "starterCode": "const js_code = `\nconst p = new Promise((resolve, reject) => {\n  ___('___');\n});\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst p = new Promise((resolve, reject) => {\n  resolve('Success');\n});\n`;\nconsole.log(js_code);",
    "hint": "Call resolve() with the text.",
    "rubric": "Promise properly resolves."
  },
  {
    "title": "Making a Fetch Request",
    "theory": "## Fetch API\n```js\nfetch('https://api.github.com/users/octocat')\n  .then(response => response.json())\n  .then(data => console.log(data.name));\n```",
    "instructions": "## Task: Fetch User Data\nUse fetch to request data from `/api/user` and parse it as JSON.",
    "starterCode": "const js_code = `\nfetch('___')\n  .then(res => res.___())\n  .then(data => console.log(data));\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nfetch('/api/user')\n  .then(res => res.json())\n  .then(data => console.log(data));\n`;\nconsole.log(js_code);",
    "hint": "Use fetch('/api/user') and res.json().",
    "rubric": "Fetch and json() methods chained."
  },
  {
    "title": "Async / Await Syntax",
    "theory": "## Async/Await\nA cleaner way to write Promise-based code.\n```js\nasync function getUser() {\n  const res = await fetch('/api/user');\n  const data = await res.json();\n  console.log(data);\n}\n```",
    "instructions": "## Task: Convert to Async\nConvert a fetch call into async/await syntax.",
    "starterCode": "const js_code = `\n___ function load() {\n  const res = ___ fetch('/api/data');\n  const data = ___ res.json();\n  return data;\n}\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nasync function load() {\n  const res = await fetch('/api/data');\n  const data = await res.json();\n  return data;\n}\n`;\nconsole.log(js_code);",
    "hint": "Prefix the function with async, and use await before Promises.",
    "rubric": "async and await keywords used correctly."
  }
],

"C Fundamentals": [
  {
    "title": "Hello World in C",
    "theory": "## C Basics\n```c\n#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}\n```\nC is a compiled, statically typed language.",
    "instructions": "## Task: Write Main Function\nWrite the standard `main` function in C that prints 'Hello C'.",
    "starterCode": "const c_code = `\n#include <stdio.h>\n\nint ___(void) {\n    ___(\"Hello C\\n\");\n    return ___;\n}\n`;\nconsole.log(c_code);",
    "solution": "const c_code = `\n#include <stdio.h>\n\nint main(void) {\n    printf(\"Hello C\\n\");\n    return 0;\n}\n`;\nconsole.log(c_code);",
    "hint": "main(), printf(), return 0;",
    "rubric": "main function and printf correctly written."
  },
  {
    "title": "Data Types & Variables",
    "theory": "## Data Types\n```c\nint age = 25;\nfloat pi = 3.14;\nchar grade = 'A';\n// Print with format specifiers\nprintf(\"Age: %d, PI: %f, Grade: %c\", age, pi, grade);\n```",
    "instructions": "## Task: Format Specifiers\nUse the correct format specifiers for an integer and a character in `printf`.",
    "starterCode": "const c_code = `\nint count = 10;\nchar letter = 'Z';\nprintf(\"Count is ___ and Letter is ___\\n\", count, letter);\n`;\nconsole.log(c_code);",
    "solution": "const c_code = `\nint count = 10;\nchar letter = 'Z';\nprintf(\"Count is %d and Letter is %c\\n\", count, letter);\n`;\nconsole.log(c_code);",
    "hint": "%d for int, %c for char.",
    "rubric": "%d and %c used correctly."
  },
  {
    "title": "Control Structures (if/while)",
    "theory": "## Control Structures\n```c\nint x = 10;\nif (x > 5) {\n    printf(\"Large\");\n}\nwhile (x > 0) {\n    x--;\n}\n```",
    "instructions": "## Task: While Loop\nWrite a while loop that counts down from 5 to 1.",
    "starterCode": "const c_code = `\nint i = 5;\n___ (i > 0) {\n    printf(\"%d \", i);\n    ___; // decrement i\n}\n`;\nconsole.log(c_code);",
    "solution": "const c_code = `\nint i = 5;\nwhile (i > 0) {\n    printf(\"%d \", i);\n    i--; // decrement i\n}\n`;\nconsole.log(c_code);",
    "hint": "Use while loop and decrement operator i--.",
    "rubric": "while and decrement used."
  }
],

"Memory & Pointers": [
  {
    "title": "Address of Operator",
    "theory": "## The Address Operator (&)\nEvery variable is stored in memory. You can get its memory address using `&`.\n```c\nint num = 42;\nprintf(\"Value: %d\\n\", num);\nprintf(\"Address: %p\\n\", &num);\n```",
    "instructions": "## Task: Print an Address\nUse the `&` operator to get the address of variable `x`.",
    "starterCode": "const c_code = `\nint x = 100;\nprintf(\"Address of x is %p\", ___x);\n`;\nconsole.log(c_code);",
    "solution": "const c_code = `\nint x = 100;\nprintf(\"Address of x is %p\", &x);\n`;\nconsole.log(c_code);",
    "hint": "Use the ampersand symbol: &",
    "rubric": "Address operator & is used."
  },
  {
    "title": "Pointer Variables",
    "theory": "## Pointers (*)\nA pointer is a variable that stores a memory address.\n```c\nint num = 42;\nint *ptr = &num;  // ptr stores the address of num\n```",
    "instructions": "## Task: Declare a Pointer\nDeclare an integer pointer `p` and assign it the address of `score`.",
    "starterCode": "const c_code = `\nint score = 95;\nint ___p = ___score;\n`;\nconsole.log(c_code);",
    "solution": "const c_code = `\nint score = 95;\nint *p = &score;\n`;\nconsole.log(c_code);",
    "hint": "Use * to declare pointer, and & to get address.",
    "rubric": "Pointer declared and assigned address."
  },
  {
    "title": "Dereferencing Pointers",
    "theory": "## Dereferencing\nYou can access or modify the value at a pointer's address by dereferencing it using `*`.\n```c\nint num = 42;\nint *ptr = &num;\n*ptr = 100;  // Changes 'num' to 100!\n```",
    "instructions": "## Task: Modify via Pointer\nChange the value of `val` to 50 using its pointer `ptr`.",
    "starterCode": "const c_code = `\nint val = 10;\nint *ptr = &val;\n___ptr = 50;\n`;\nconsole.log(c_code);",
    "solution": "const c_code = `\nint val = 10;\nint *ptr = &val;\n*ptr = 50;\n`;\nconsole.log(c_code);",
    "hint": "Use *ptr to dereference.",
    "rubric": "Pointer properly dereferenced and assigned."
  }
],

"RAG Pipelines": [
  {
    "title": "What is RAG?",
    "theory": "## Retrieval-Augmented Generation\nRAG allows an LLM to access external data before answering.\n1. User asks question.\n2. System searches a database for relevant documents.\n3. System feeds documents + question to LLM.",
    "instructions": "## Task: RAG Steps\nAssign the three steps of RAG in order: 'Retrieve', 'Augment', 'Generate'.",
    "starterCode": "step1 = '___'\nstep2 = '___'\nstep3 = '___'\nprint(f'{step1} -> {step2} -> {step3}')",
    "solution": "step1 = 'Retrieve'\nstep2 = 'Augment'\nstep3 = 'Generate'\nprint(f'{step1} -> {step2} -> {step3}')",
    "hint": "Retrieve, Augment, Generate",
    "rubric": "Steps correctly ordered."
  },
  {
    "title": "Document Chunking",
    "theory": "## Chunking Text\nLarge documents cannot fit in an LLM's context window. They must be split into chunks (e.g., 500 words each) before being indexed.",
    "instructions": "## Task: Simple Chunker\nWrite a function that splits a string into chunks of exactly 5 characters.",
    "starterCode": "def chunk_text(text, size):\n    return [text[i:i+___] for i in range(0, len(text), ___)]\n\nprint(chunk_text('HelloWorld', 5))",
    "solution": "def chunk_text(text, size):\n    return [text[i:i+size] for i in range(0, len(text), size)]\n\nprint(chunk_text('HelloWorld', 5))",
    "hint": "Use the size parameter.",
    "rubric": "Chunking logic uses size parameter."
  },
  {
    "title": "Embeddings",
    "theory": "## Vector Embeddings\nEmbeddings convert text into lists of numbers (vectors) representing semantic meaning. Similar texts have similar vectors.",
    "instructions": "## Task: Dummy Embedding\nCreate a function that simulates an embedding by returning a list of the ASCII values of the characters.",
    "starterCode": "def embed(text):\n    return [___(char) for char in text]\n\nprint(embed('AI'))",
    "solution": "def embed(text):\n    return [ord(char) for char in text]\n\nprint(embed('AI'))",
    "hint": "Use the ord() function to get ASCII values.",
    "rubric": "ord() function used for simulated embedding."
  }
],

"LangChain Basics": [
  {
    "title": "Intro to LangChain",
    "theory": "## LangChain Framework\nLangChain is a Python/JS framework for developing applications powered by LLMs, providing components like PromptTemplates, LLMs, and Chains.",
    "instructions": "## Task: Identify Components\nList two core LangChain components.",
    "starterCode": "components = ['___', '___']\nprint(components)",
    "solution": "components = ['PromptTemplates', 'Chains']\nprint(components)",
    "hint": "PromptTemplates, Chains",
    "rubric": "Correctly identified components."
  },
  {
    "title": "LLM Wrappers",
    "theory": "## LLM Wrapper\n```python\nfrom langchain.llms import OpenAI\nllm = OpenAI(api_key='...')\nprint(llm(\"Tell me a joke\"))\n```",
    "instructions": "## Task: Mock LLM\nCreate a mock LLM class that returns 'Mock Answer' when called.",
    "starterCode": "class MockLLM:\n    def __call__(self, prompt):\n        return '___'\n\nllm = MockLLM()\nprint(llm('Hello'))",
    "solution": "class MockLLM:\n    def __call__(self, prompt):\n        return 'Mock Answer'\n\nllm = MockLLM()\nprint(llm('Hello'))",
    "hint": "Return the string 'Mock Answer'.",
    "rubric": "MockLLM returns correct string."
  },
  {
    "title": "Simple Chains",
    "theory": "## LLMChain\nAn `LLMChain` links a PromptTemplate and an LLM together.\n```python\nchain = LLMChain(llm=llm, prompt=prompt)\nchain.run(topic='AI')\n```",
    "instructions": "## Task: Mock Chain\nImplement a mock chain that takes a topic and formats it.",
    "starterCode": "class MockChain:\n    def run(self, topic):\n        return f'Here is info about {___}'\n\nchain = MockChain()\nprint(chain.run('Python'))",
    "solution": "class MockChain:\n    def run(self, topic):\n        return f'Here is info about {topic}'\n\nchain = MockChain()\nprint(chain.run('Python'))",
    "hint": "Inject the topic variable into the string.",
    "rubric": "Variable injected correctly."
  }
],

"ES6+ Modern JS": [
  {
    "title": "Template Literals",
    "theory": "## Template Literals\nUse backticks `` to allow string interpolation.\n```js\nconst name = 'Ada';\nconsole.log(`Hello ${name}`);\n```",
    "instructions": "## Task: Interpolation\nFix the string to use template literals.",
    "starterCode": "const js_code = `\nconst framework = 'React';\nconsole.log(___I love ___framework___);\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst framework = 'React';\nconsole.log(\\`I love ${framework}\\`);\n`;\nconsole.log(js_code);",
    "hint": "Use backticks \\` and ${...}.",
    "rubric": "Template literals used properly."
  },
  {
    "title": "Destructuring",
    "theory": "## Object Destructuring\nExtract properties from objects easily.\n```js\nconst user = { id: 1, name: 'Ada' };\nconst { id, name } = user;\n```",
    "instructions": "## Task: Destructure an Object\nExtract `score` and `level` from the `game` object.",
    "starterCode": "const js_code = `\nconst game = { score: 100, level: 2, player: 'Ada' };\nconst { ___, ___ } = game;\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst game = { score: 100, level: 2, player: 'Ada' };\nconst { score, level } = game;\n`;\nconsole.log(js_code);",
    "hint": "Extract score and level.",
    "rubric": "Destructuring assignment used."
  },
  {
    "title": "Spread Operator",
    "theory": "## Spread (...)\nSpread allows an iterable to be expanded.\n```js\nconst arr1 = [1, 2];\nconst arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]\n```",
    "instructions": "## Task: Spread an Array\nMerge `listA` and `listB` into `combined` using the spread operator.",
    "starterCode": "const js_code = `\nconst listA = [1, 2];\nconst listB = [3, 4];\nconst combined = [___listA, ___listB];\n`;\nconsole.log(js_code);",
    "solution": "const js_code = `\nconst listA = [1, 2];\nconst listB = [3, 4];\nconst combined = [...listA, ...listB];\n`;\nconsole.log(js_code);",
    "hint": "Use ... before the array names.",
    "rubric": "Spread operator (...) used correctly."
  }
],

"CSS Animations": [
  {
    "title": "Transitions",
    "theory": "## CSS Transitions\nSmoothly change CSS properties.\n```css\n.btn {\n  background: blue;\n  transition: background 0.3s ease;\n}\n.btn:hover {\n  background: red;\n}\n```",
    "instructions": "## Task: Add a Transition\nAdd a 0.5s transition to the transform property.",
    "starterCode": "const css = `\n.card {\n  ___: transform 0.5s ease;\n}\n`;\nconsole.log(css);",
    "solution": "const css = `\n.card {\n  transition: transform 0.5s ease;\n}\n`;\nconsole.log(css);",
    "hint": "Use the transition property.",
    "rubric": "transition property specified."
  },
  {
    "title": "Keyframes",
    "theory": "## @keyframes\nDefine complex animations.\n```css\n@keyframes slide {\n  0% { transform: translateX(0); }\n  100% { transform: translateX(100px); }\n}\n```",
    "instructions": "## Task: Define Keyframes\nDefine keyframes named `fade` that goes from opacity 0 to 1.",
    "starterCode": "const css = `\n___ fade {\n  0% { ___: 0; }\n  100% { ___: 1; }\n}\n`;\nconsole.log(css);",
    "solution": "const css = `\n@keyframes fade {\n  0% { opacity: 0; }\n  100% { opacity: 1; }\n}\n`;\nconsole.log(css);",
    "hint": "Use @keyframes and opacity.",
    "rubric": "keyframes and opacity used."
  },
  {
    "title": "Applying Animations",
    "theory": "## The Animation Property\n```css\n.box {\n  animation: slide 2s infinite;\n}\n```",
    "instructions": "## Task: Apply Animation\nApply the `fade` animation over 1s infinitely.",
    "starterCode": "const css = `\n.element {\n  ___: fade 1s ___;\n}\n`;\nconsole.log(css);",
    "solution": "const css = `\n.element {\n  animation: fade 1s infinite;\n}\n`;\nconsole.log(css);",
    "hint": "animation property and infinite.",
    "rubric": "animation and infinite keywords used."
  }
],

"C++ Fundamentals": [
  {
    "title": "Hello C++",
    "theory": "## C++ Standard Library\n```cpp\n#include <iostream>\nint main() {\n    std::cout << \"Hello World!\" << std::endl;\n    return 0;\n}\n```",
    "instructions": "## Task: Print in C++\nUse `std::cout` to print \"C++ Rocks\".",
    "starterCode": "const cpp_code = `\n#include <iostream>\nint main() {\n    ___ << \"C++ Rocks\" << ___;\n    return 0;\n}\n`;\nconsole.log(cpp_code);",
    "solution": "const cpp_code = `\n#include <iostream>\nint main() {\n    std::cout << \"C++ Rocks\" << std::endl;\n    return 0;\n}\n`;\nconsole.log(cpp_code);",
    "hint": "std::cout and std::endl",
    "rubric": "std::cout and std::endl used."
  },
  {
    "title": "Namespaces",
    "theory": "## using namespace std\nTo avoid typing `std::` repeatedly:\n```cpp\nusing namespace std;\ncout << \"Easier!\";\n```",
    "instructions": "## Task: Use Namespace\nInclude the `std` namespace globally.",
    "starterCode": "const cpp_code = `\n#include <iostream>\n___ ___ std;\nint main() { cout << \"Hi\"; }\n`;\nconsole.log(cpp_code);",
    "solution": "const cpp_code = `\n#include <iostream>\nusing namespace std;\nint main() { cout << \"Hi\"; }\n`;\nconsole.log(cpp_code);",
    "hint": "using namespace std;",
    "rubric": "using namespace std applied."
  },
  {
    "title": "Classes in C++",
    "theory": "## OOP in C++\n```cpp\nclass Dog {\npublic:\n    void bark() { cout << \"Woof!\"; }\n};\n```",
    "instructions": "## Task: Create a Class\nCreate a `Car` class with a public method `honk()`.",
    "starterCode": "const cpp_code = `\n___ Car {\n___:\n    void honk() { cout << \"Beep!\"; }\n};\n`;\nconsole.log(cpp_code);",
    "solution": "const cpp_code = `\nclass Car {\npublic:\n    void honk() { cout << \"Beep!\"; }\n};\n`;\nconsole.log(cpp_code);",
    "hint": "class keyword and public: access modifier.",
    "rubric": "Class and public modifiers used."
  }
],

"Deep Learning for Vision": [
  {
    "title": "Convolutional Neural Networks",
    "theory": "## CNNs\nCNNs (Convolutional Neural Networks) use 'filters' to slide across an image and extract features like edges and textures.",
    "instructions": "## Task: CNN Key Terms\nWhat mathematical operation do CNNs use to extract features from an image?",
    "starterCode": "operation = '___'\nprint(operation)",
    "solution": "operation = 'Convolution'\nprint(operation)",
    "hint": "Convolution",
    "rubric": "Convolution specified."
  },
  {
    "title": "Pooling Layers",
    "theory": "## Pooling (Downsampling)\nPooling layers reduce the spatial size of the representation, reducing parameters and computation.",
    "instructions": "## Task: Identify Pooling\nWhich pooling method takes the largest value in a patch?",
    "starterCode": "pooling_type = '___ Pooling'\nprint(pooling_type)",
    "solution": "pooling_type = 'Max Pooling'\nprint(pooling_type)",
    "hint": "Max Pooling",
    "rubric": "Max Pooling specified."
  },
  {
    "title": "Transfer Learning",
    "theory": "## Transfer Learning\nReusing a pre-trained model (like ResNet or VGG) on a new, related task.",
    "instructions": "## Task: Freeze Weights\nIn transfer learning, we often 'freeze' the early layers so they don't change during training.",
    "starterCode": "action = '___ the weights'\nprint(action)",
    "solution": "action = 'Freeze the weights'\nprint(action)",
    "hint": "Freeze",
    "rubric": "Freeze specified."
  }
]

}

def inject_lessons_safe(filepath, new_lessons):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    manifest_start = content.find('courseManifest')
    if manifest_start == -1: return

    injected = 0
    for course_name, lessons in new_lessons.items():
        course_pos = content.find(f'"{course_name}":', manifest_start)
        if course_pos == -1: continue
        lessons_key = content.find('"lessons"', course_pos)
        if lessons_key == -1: continue
        bracket_start = content.find('[', lessons_key)
        if bracket_start == -1: continue
            
        depth = 0; bracket_end = -1
        for i in range(bracket_start, min(bracket_start + 100000, len(content))):
            if content[i] == '[': depth += 1
            elif content[i] == ']':
                depth -= 1
                if depth == 0: bracket_end = i; break
        if bracket_end == -1: continue

        first_title = f'"title": "{lessons[0]["title"]}"'
        if content[bracket_start:bracket_end].find(first_title) != -1: continue

        new_entries = ''
        for lesson in lessons:
            new_entries += ',\\n      ' + json.dumps(lesson, ensure_ascii=False)
            
        content = content[:bracket_end] + new_entries + '\\n    ' + content[bracket_end:]
        injected += len(lessons)
        print(f'OK: Added {len(lessons)} lessons to "{course_name}"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\\nTOTAL: {injected}')

if __name__ == '__main__':
    inject_lessons_safe('frontend/src/data/courses.js', NEW_LESSONS)
