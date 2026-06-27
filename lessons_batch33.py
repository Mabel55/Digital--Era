"""
Batch 33: Expanding Frontend Curriculum (Tailwind, Vue, TypeScript, Animations, Testing)
"""
import json, os

NEW_COURSES_BATCH33 = {
    "Tailwind CSS Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess Tailwind styling knowledge",
        "lessons": [
            {"title": "Utility-First CSS", "theory": "## The Utility Approach\\nInstead of writing custom CSS, Tailwind provides low-level utility classes like `flex`, `pt-4`, and `text-center` that let you build designs directly in your markup.", "instructions": "## Task: Apply Tailwind Classes\\nStyle a button to have a blue background, white text, padding, and rounded corners.", "starterCode": "<button class=\"___ ___ px-4 py-2 ___\">Click Me</button>", "solution": "<button class=\"bg-blue-500 text-white px-4 py-2 rounded\">Click Me</button>", "hint": "Use bg-blue-500, text-white, and rounded", "rubric": "Correctly applies standard Tailwind classes."},
            {"title": "Responsive Design", "theory": "## Breakpoint Prefixes\\nTailwind makes responsive design easy by prefixing classes with screen sizes, e.g., `md:flex` applies flexbox only on medium screens and larger.", "instructions": "## Task: Responsive Grid\\nCreate a grid that is 1 column on mobile, and 3 columns on medium screens.", "starterCode": "<div class=\"grid grid-cols-1 md:___\">\\n  <div>Item 1</div>\\n  <div>Item 2</div>\\n  <div>Item 3</div>\\n</div>", "solution": "<div class=\"grid grid-cols-1 md:grid-cols-3\">\\n  <div>Item 1</div>\\n  <div>Item 2</div>\\n  <div>Item 3</div>\\n</div>", "hint": "Use md:grid-cols-3", "rubric": "Applies md:grid-cols-3 correctly."}
        ]
    },
    "Vue.js Fundamentals": {
        "tier": "Intermediate",
        "aiRubric": "Assess Vue.js concepts",
        "lessons": [
            {"title": "Declarative Rendering", "theory": "## The Template Syntax\\nVue uses an HTML-based template syntax that allows you to declaratively bind the rendered DOM to the underlying component instance's data.", "instructions": "## Task: Interpolation\\nUse Vue's mustache syntax to render the `message` variable.", "starterCode": "<template>\\n  <div>\\n    <p>___</p>\\n  </div>\\n</template>\\n\\n<script setup>\\nimport { ref } from 'vue'\\nconst message = ref('Hello Vue!')\\n</script>", "solution": "<template>\\n  <div>\\n    <p>{{ message }}</p>\\n  </div>\\n</template>\\n\\n<script setup>\\nimport { ref } from 'vue'\\nconst message = ref('Hello Vue!')\\n</script>", "hint": "Use {{ message }}", "rubric": "Correctly renders the ref using double curly braces."},
            {"title": "Directives", "theory": "## v-if and v-for\\nDirectives are special attributes with the `v-` prefix. `v-if` conditionally renders an element, while `v-for` renders a list of items.", "instructions": "## Task: Rendering a List\\nUse `v-for` to render a list of items from an array.", "starterCode": "<template>\\n  <ul>\\n    <li ___=\"item in items\" :key=\"item.id\">\\n      {{ item.name }}\\n    </li>\\n  </ul>\\n</template>\\n\\n<script setup>\\nimport { ref } from 'vue'\\nconst items = ref([{id: 1, name: 'Apple'}, {id: 2, name: 'Banana'}])\\n</script>", "solution": "<template>\\n  <ul>\\n    <li v-for=\"item in items\" :key=\"item.id\">\\n      {{ item.name }}\\n    </li>\\n  </ul>\\n</template>\\n\\n<script setup>\\nimport { ref } from 'vue'\\nconst items = ref([{id: 1, name: 'Apple'}, {id: 2, name: 'Banana'}])\\n</script>", "hint": "Use v-for", "rubric": "Correctly applies the v-for directive."}
        ]
    },
    "TypeScript for Frontend": {
        "tier": "Intermediate",
        "aiRubric": "Assess TypeScript knowledge in UI",
        "lessons": [
            {"title": "Typing Props", "theory": "## Interface Definitions\\nWhen building components (e.g. in React), defining the shape of your props using TypeScript Interfaces catches errors during development instead of runtime.", "instructions": "## Task: Define Button Props\\nCreate an interface for a Button component that requires a string `label` and an optional boolean `disabled`.", "starterCode": "interface ButtonProps {\\n    ___: ___;\\n    disabled___: ___;\\n}\\n\\nfunction Button({ label, disabled }: ButtonProps) {\\n    return <button disabled={disabled}>{label}</button>\\n}", "solution": "interface ButtonProps {\\n    label: string;\\n    disabled?: boolean;\\n}\\n\\nfunction Button({ label, disabled }: ButtonProps) {\\n    return <button disabled={disabled}>{label}</button>\\n}", "hint": "Use label: string and disabled?: boolean", "rubric": "Correctly types the required string and optional boolean."},
            {"title": "Generics in State", "theory": "## Type Inference and Generics\\nSometimes you need to explicitly type state hooks when the initial value is null or empty, using Generics.", "instructions": "## Task: Type useState\\nUse a generic to specify that the state can be a User object or null.", "starterCode": "import { useState } from 'react';\\n\\ntype User = { name: string, age: number };\\n\\n// Specify that user can be User or null\\nconst [user, setUser] = useState<___>(null);", "solution": "import { useState } from 'react';\\n\\ntype User = { name: string, age: number };\\n\\n// Specify that user can be User or null\\nconst [user, setUser] = useState<User | null>(null);", "hint": "Use User | null", "rubric": "Applies the correct union type generic."}
        ]
    },
    "Web Animations": {
        "tier": "Advanced",
        "aiRubric": "Assess web animation techniques",
        "lessons": [
            {"title": "CSS Keyframes", "theory": "## @keyframes\\nKeyframes allow you to control the intermediate steps in a CSS animation sequence.", "instructions": "## Task: Define a Fade-In\\nWrite a keyframe animation that fades opacity from 0 to 1.", "starterCode": "@keyframes fadeIn {\\n  from {\\n    opacity: ___;\\n  }\\n  to {\\n    opacity: ___;\\n  }\\n}\\n\\n.animated-box {\\n  animation: fadeIn 2s ease-in;\\n}", "solution": "@keyframes fadeIn {\\n  from {\\n    opacity: 0;\\n  }\\n  to {\\n    opacity: 1;\\n  }\\n}\\n\\n.animated-box {\\n  animation: fadeIn 2s ease-in;\\n}", "hint": "Use 0 and 1 for opacity.", "rubric": "Correctly defines the start and end opacity."},
            {"title": "Framer Motion", "theory": "## React Animations\\nFramer Motion is a production-ready motion library for React that simplifies complex animations.", "instructions": "## Task: Animate a Div\\nUse the `motion.div` component to animate a box moving 100px to the right.", "starterCode": "import { motion } from 'framer-motion';\\n\\nexport default function App() {\\n  return (\\n    <motion.div\\n      animate={{ x: ___ }}\\n      transition={{ duration: 0.5 }}\\n    >\\n      Sliding Box\\n    </motion.div>\\n  );\\n}", "solution": "import { motion } from 'framer-motion';\\n\\nexport default function App() {\\n  return (\\n    <motion.div\\n      animate={{ x: 100 }}\\n      transition={{ duration: 0.5 }}\\n    >\\n      Sliding Box\\n    </motion.div>\\n  );\\n}", "hint": "Set x to 100", "rubric": "Uses the correct translation value in the animate prop."}
        ]
    },
    "Frontend Testing": {
        "tier": "Advanced",
        "aiRubric": "Assess frontend testing strategies",
        "lessons": [
            {"title": "React Testing Library", "theory": "## Testing Behavior\\nReact Testing Library encourages testing applications in the way they are used by users, focusing on querying the DOM.", "instructions": "## Task: Assert Element Presence\\nWrite an assertion that checks if an element with the text 'Submit' is in the document.", "starterCode": "import { render, screen } from '@testing-library/react';\\nimport '@testing-library/jest-dom';\\nimport Button from './Button';\\n\\ntest('renders submit button', () => {\\n  render(<Button label=\"Submit\" />);\\n  const buttonElement = screen.getByText(/Submit/i);\\n  expect(buttonElement).___.toBeInTheDocument();\\n});", "solution": "import { render, screen } from '@testing-library/react';\\nimport '@testing-library/jest-dom';\\nimport Button from './Button';\\n\\ntest('renders submit button', () => {\\n  render(<Button label=\"Submit\" />);\\n  const buttonElement = screen.getByText(/Submit/i);\\n  expect(buttonElement).toBeInTheDocument();\\n});", "hint": "Remove the blank space, it just calls toBeInTheDocument()", "rubric": "Correctly invokes toBeInTheDocument assertion."},
            {"title": "E2E with Cypress", "theory": "## End-to-End Tests\\nCypress runs in the browser and tests the entire application flow, interacting with it exactly like a real user would.", "instructions": "## Task: Visit and Type\\nWrite a Cypress test that visits a page, targets an input field, and types a value.", "starterCode": "describe('Login Flow', () => {\\n  it('can type into email input', () => {\\n    cy.___('/login');\\n    cy.get('input[name=\"email\"]').___('test@example.com');\\n  });\\n});", "solution": "describe('Login Flow', () => {\\n  it('can type into email input', () => {\\n    cy.visit('/login');\\n    cy.get('input[name=\"email\"]').type('test@example.com');\\n  });\\n});", "hint": "Use visit and type.", "rubric": "Correctly uses visit and type commands."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'frontend.json')
    
    # 1. Update frontend.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH33.items():
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
                
    # 2. Update index.json
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH33.items():
            tier = course_info["tier"]
            if "Frontend" in index_data and tier in index_data["Frontend"]:
                if new_course_name not in index_data["Frontend"][tier]:
                    index_data["Frontend"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 33: Added {total} lessons to Frontend track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
