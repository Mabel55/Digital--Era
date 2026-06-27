"""
Batch 15: AI Eng, Distributed Systems, FFI
"""
import json, os

LESSONS_BATCH15 = {
    # ─── SYSTEM DESIGN & ARCHITECTURE ───
    "Distributed Consensus": [
        {"title": "Who is the Leader?", "theory": "## The Split-Brain Problem\nIn a distributed database (like MongoDB or Kafka), multiple servers work together. If the leader server crashes, the other servers must elect a new leader.\n\nBut what if the network splits, and two groups of servers both think the other group died? You could get TWO leaders (Split-Brain), leading to corrupted data.\n\n**Consensus Algorithms** (like Raft or Paxos) solve this. A leader can only be elected if a **majority** (quorum) of servers vote for it. If you have 5 servers, you need 3 votes. You can never have two majorities!", "instructions": "## Task: Quorum Calculator\n1. Write a function that calculates the required quorum (majority) for a given number of nodes.\n2. Formula: `(N / 2) + 1` (integer division).\n3. Calculate quorum for 3, 4, 5, and 100 nodes.", "starterCode": "def get_quorum(total_nodes):\n    # Calculate majority using integer division\n    return (total_nodes ___ 2) + ___\n\nnodes_list = [3, 4, 5, 100]\nfor n in nodes_list:\n    q = get_quorum(n)\n    print(f\"Total Nodes: {n} -> Quorum Needed: {q}\")", "solution": "def get_quorum(total_nodes):\n    # Calculate majority using integer division\n    return (total_nodes // 2) + 1\n\nnodes_list = [3, 4, 5, 100]\nfor n in nodes_list:\n    q = get_quorum(n)\n    print(f\"Total Nodes: {n} -> Quorum Needed: {q}\")", "hint": "Use // for integer division. Add 1.", "rubric": "Returns 2 for 3 nodes, 3 for 4 nodes, 3 for 5 nodes, 51 for 100 nodes."}
    ],
    # ─── SYSTEMS PROGRAMMING (RUST) ───
    "FFI": [
        {"title": "Foreign Function Interface", "theory": "## Calling C from Rust\nRust can talk to other languages (mostly C). This is called FFI.\n\nYou have to use `extern \"C\"` to define the C functions you want to call, and you MUST call them inside an `unsafe` block because Rust can't guarantee that the C code is safe.\n\n```rust\nextern \"C\" {\n    fn abs(input: i32) -> i32;\n}\n\nfn main() {\n    unsafe {\n        println!(\"Absolute value of -3 according to C: {}\", abs(-3));\n    }\n}\n```", "instructions": "## Task: Call a C Function\n1. Declare an external C function `sqrt(input: f64) -> f64`.\n2. Call it from `main` to find the square root of 64.0.\n3. Remember the `unsafe` block!", "starterCode": "extern \"C\" {\n    fn ___(input: f64) -> f64;\n}\n\nfn main() {\n    let number = 64.0;\n    \n    // Calling C code is unsafe!\n    ___ {\n        let result = ___(number);\n        println!(\"Square root of {} is {}\", number, result);\n    }\n}", "solution": "extern \"C\" {\n    fn sqrt(input: f64) -> f64;\n}\n\nfn main() {\n    let number = 64.0;\n    \n    // Calling C code is unsafe!\n    unsafe {\n        let result = sqrt(number);\n        println!(\"Square root of {} is {}\", number, result);\n    }\n}", "hint": "fn sqrt. unsafe { }. sqrt(number).", "rubric": "Properly declares sqrt and calls it inside an unsafe block."}
    ],
    # ─── AI ENGINEERING ───
    "CNN Architecture": [
        {"title": "Convolutional Neural Networks", "theory": "## How AI Sees Images\nStandard Neural Networks (Dense layers) are terrible for images because they flatten the image, losing spatial context (what pixels are next to what).\n\n**CNNs** slide a small filter (like a 3x3 window) across the image. \n- Early layers find simple edges and corners.\n- Later layers combine edges to find shapes (wheels, eyes).\n- Final layers recognize objects (cars, faces).", "instructions": "## Task: Layer Matcher\n1. Match the CNN component to its function.\n2. Components: 'Convolutional Layer', 'Pooling Layer', 'Fully Connected Layer'\n3. Functions: 'Extracts features (edges/shapes)', 'Reduces image size/resolution', 'Makes the final classification guess'", "starterCode": "cnn_layers = {\n    'Extracts features (edges/shapes) by sliding filters': '___',\n    'Reduces image size (downsampling) to save memory': '___',\n    'Flattens the data to make the final classification guess': '___'\n}\n\nfor desc, layer in cnn_layers.items():\n    print(f\"{layer:25} -> {desc}\")", "solution": "cnn_layers = {\n    'Extracts features (edges/shapes) by sliding filters': 'Convolutional Layer',\n    'Reduces image size (downsampling) to save memory': 'Pooling Layer',\n    'Flattens the data to make the final classification guess': 'Fully Connected Layer'\n}\n\nfor desc, layer in cnn_layers.items():\n    print(f\"{layer:25} -> {desc}\")", "hint": "Conv layer extracts. Pooling reduces size. Fully Connected classifies.", "rubric": "Layers correctly matched to their functions."}
    ],
    # ─── AI AUTOMATION & AGENTS ───
    "Automated Content": [
        {"title": "Content Generation", "theory": "## AI Writers at Scale\nAutomated content pipelines take raw data and turn it into polished content automatically.\n\nPipeline flow:\n1. **Ingest**: Read a raw JSON feed (e.g., weather data).\n2. **Prompt Construction**: Inject the data into a prompt template.\n3. **LLM Generation**: Ask the AI to write a natural language summary.\n4. **Publish**: Send the summary to a CMS or Twitter.", "instructions": "## Task: Weather Bot Simulator\n1. You have raw weather data in a dictionary.\n2. Create a function that formats a prompt for the AI.\n3. The prompt should say: \"Write a friendly weather report for [City]. The temp is [Temp] and it's [Condition].\"", "starterCode": "def create_prompt(weather_data):\n    city = weather_data['___']\n    temp = weather_data['___']\n    condition = weather_data['___']\n    \n    return f\"Write a friendly weather report for {___}. The temp is {___} and it's {___}.\"\n\nraw_data = {\n    'city': 'Seattle',\n    'temp': '65F',\n    'condition': 'raining as usual'\n}\n\nprompt = create_prompt(raw_data)\nprint(\"Generated Prompt to send to LLM:\\n\", prompt)", "solution": "def create_prompt(weather_data):\n    city = weather_data['city']\n    temp = weather_data['temp']\n    condition = weather_data['condition']\n    \n    return f\"Write a friendly weather report for {city}. The temp is {temp} and it's {condition}.\"\n\nraw_data = {\n    'city': 'Seattle',\n    'temp': '65F',\n    'condition': 'raining as usual'\n}\n\nprompt = create_prompt(raw_data)\nprint(\"Generated Prompt to send to LLM:\\n\", prompt)", "hint": "Extract keys: 'city', 'temp', 'condition'. Inject them into the f-string.", "rubric": "Prompt correctly incorporates the data from the dictionary."}
    ]
}

def apply_lessons(tracks_dir):
    from rebuild_curriculum import track_courses
    total = 0
    for track_name, levels in track_courses.items():
        safe_name = track_name.lower().replace(" ", "_").replace("&", "").replace("__", "_") + ".json"
        filepath = os.path.join(tracks_dir, safe_name)
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
        updated = False
        for course_name in track_data:
            if course_name in LESSONS_BATCH15:
                track_data[course_name]['lessons'] = LESSONS_BATCH15[course_name]
                updated = True
                total += len(LESSONS_BATCH15[course_name])
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(track_data, f, indent=2, ensure_ascii=False)
    print(f'Batch 15: Applied {total} lessons')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
