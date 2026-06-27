"""
Batch 54: Deep Dive into Frontend (React Hooks Masterclass)
"""
import json, os

NEW_COURSES_BATCH54 = {
    "React Hooks Masterclass": {
        "tier": "Intermediate",
        "aiRubric": "Assess deep understanding of React Hooks",
        "lessons": [
            {"title": "useState Basics", "theory": "## Managing Local State\\n`useState` allows functional components to hold and update their own local state, triggering a re-render whenever the state setter function is called.", "instructions": "## Task: Initialize State\\nUse the `useState` hook to initialize a `count` variable to 0.", "starterCode": "import { useState } from 'react';\\n\\nfunction Counter() {\\n  const [count, ___] = ___(0);\\n  return <div>{count}</div>;\\n}", "solution": "import { useState } from 'react';\\n\\nfunction Counter() {\\n  const [count, setCount] = useState(0);\\n  return <div>{count}</div>;\\n}", "hint": "Use setCount and useState", "rubric": "Correctly sets setCount and useState(0)."},
            {"title": "useEffect and Cleanup", "theory": "## Side Effects\\n`useEffect` lets you perform side effects (like data fetching or subscriptions) after a render. Returning a function from inside the effect acts as the 'cleanup' step when the component unmounts.", "instructions": "## Task: Cleanup Function\\nReturn the function that clears the interval when the component is unmounted.", "starterCode": "useEffect(() => {\\n  const timer = setInterval(() => console.log('Tick'), 1000);\\n  ___ () => clearInterval(___);\\n}, []);", "solution": "useEffect(() => {\\n  const timer = setInterval(() => console.log('Tick'), 1000);\\n  return () => clearInterval(timer);\\n}, []);", "hint": "Use 'return' and 'timer'", "rubric": "Correctly returns the clearInterval function."},
            {"title": "useContext", "theory": "## Avoiding Prop Drilling\\n`useContext` lets you subscribe to React context without introducing nesting, allowing deeply nested components to access global data (like a User Theme) directly.", "instructions": "## Task: Consume Context\\nUse the `useContext` hook to consume the `ThemeContext`.", "starterCode": "import { useContext } from 'react';\\nimport { ThemeContext } from './Theme';\\n\\nfunction Button() {\\n  const theme = ___(ThemeContext);\\n}", "solution": "import { useContext } from 'react';\\nimport { ThemeContext } from './Theme';\\n\\nfunction Button() {\\n  const theme = useContext(ThemeContext);\\n}", "hint": "Use useContext", "rubric": "Uses useContext(ThemeContext)."},
            {"title": "useReducer", "theory": "## Complex State Logic\\nWhen state logic is complex or when the next state depends on the previous one, `useReducer` is often preferable to `useState`. It is heavily inspired by Redux.", "instructions": "## Task: Dispatch an Action\\nCall the dispatch function with an action object of type 'INCREMENT'.", "starterCode": "function Counter() {\\n  const [state, dispatch] = useReducer(reducer, { count: 0 });\\n  return <button onClick={() => ___({ type: '___' })}>Add</button>;\\n}", "solution": "function Counter() {\\n  const [state, dispatch] = useReducer(reducer, { count: 0 });\\n  return <button onClick={() => dispatch({ type: 'INCREMENT' })}>Add</button>;\\n}", "hint": "Use dispatch and 'INCREMENT'", "rubric": "Calls dispatch with type INCREMENT."},
            {"title": "useRef for the DOM", "theory": "## Mutable References\\n`useRef` returns a mutable ref object whose `.current` property is initialized to the passed argument. It is most commonly used to directly access a DOM element.", "instructions": "## Task: Focus an Input\\nAttach the `inputRef` to the input element so the button can focus it.", "starterCode": "function TextInput() {\\n  const inputRef = useRef(null);\\n  return (\\n    <>\\n      <input ___={inputRef} />\\n      <button onClick={() => inputRef.___.focus()}>Focus</button>\\n    </>\\n  );\\n}", "solution": "function TextInput() {\\n  const inputRef = useRef(null);\\n  return (\\n    <>\\n      <input ref={inputRef} />\\n      <button onClick={() => inputRef.current.focus()}>Focus</button>\\n    </>\\n  );\\n}", "hint": "Use 'ref' and 'current'", "rubric": "Uses ref attribute and current property."},
            {"title": "useMemo", "theory": "## Performance Optimization\\n`useMemo` returns a memoized *value*. It only recomputes the memoized value when one of its dependencies has changed, preventing expensive calculations on every render.", "instructions": "## Task: Memoize a Calculation\\nWrap the expensive calculation in `useMemo` so it only runs when `a` or `b` changes.", "starterCode": "const expensiveResult = ___( () => computeExpensiveValue(a, b), [___, ___] );", "solution": "const expensiveResult = useMemo( () => computeExpensiveValue(a, b), [a, b] );", "hint": "Use useMemo and pass a, b into the dependency array.", "rubric": "Uses useMemo and [a, b]."},
            {"title": "useCallback", "theory": "## Memoizing Functions\\nWhile `useMemo` memoizes a value, `useCallback` returns a memoized *callback function*. This is crucial when passing callbacks to optimized child components that rely on reference equality to prevent unnecessary renders.", "instructions": "## Task: Memoize a Callback\\nWrap the click handler in `useCallback` so it isn't recreated on every render.", "starterCode": "const handleClick = ___( () => {\\n  console.log('Clicked!', id);\\n}, [___] );", "solution": "const handleClick = useCallback( () => {\\n  console.log('Clicked!', id);\\n}, [id] );", "hint": "Use useCallback and [id]", "rubric": "Uses useCallback and [id]."},
            {"title": "Custom Hooks", "theory": "## Extracting Logic\\nIf you find yourself copying hook logic across components (like tracking window size or fetching data), you can extract it into a Custom Hook (a function starting with 'use').", "instructions": "## Task: Create a Custom Hook\\nDefine a custom hook named `useWindowWidth`.", "starterCode": "function ___( ) {\\n  const [width, setWidth] = useState(window.innerWidth);\\n  // ...\\n  return width;\\n}", "solution": "function useWindowWidth( ) {\\n  const [width, setWidth] = useState(window.innerWidth);\\n  // ...\\n  return width;\\n}", "hint": "Name it useWindowWidth", "rubric": "Names the function useWindowWidth."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'frontend.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH54.items():
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
                
    index_path = os.path.join("curriculum", "index.json")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            
        index_updated = False
        for new_course_name, course_info in NEW_COURSES_BATCH54.items():
            tier = course_info["tier"]
            if "Frontend" in index_data and tier in index_data["Frontend"]:
                if new_course_name not in index_data["Frontend"][tier]:
                    index_data["Frontend"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 54: Added {total} lessons to Frontend track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
