"""
Batch 57: Deep Dive into Agentic AI & MCP (Building MCP Servers Masterclass)
"""
import json, os

NEW_COURSES_BATCH57 = {
    "Building MCP Servers Masterclass": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of Model Context Protocol server development",
        "lessons": [
            {"title": "The Model Context Protocol", "theory": "## Standardizing AI Tools\\nThe Model Context Protocol (MCP) is an open standard that allows AI models to securely connect to local and remote resources. Instead of writing custom integrations for every AI agent, you write one MCP server that any compliant agent can talk to.", "instructions": "## Task: The Core Philosophy\\nMCP separates the AI Agent (the Client) from the Data Source (the Server). What is the primary benefit of this architecture?", "starterCode": "# Options: Faster training, Write once connect anywhere, Reduced hallucinations\\nbenefit = '___'", "solution": "# Options: Faster training, Write once connect anywhere, Reduced hallucinations\\nbenefit = 'Write once connect anywhere'", "hint": "Write once connect anywhere", "rubric": "Identifies Write once connect anywhere."},
            {"title": "Server Architecture & Transports", "theory": "## Stdio vs SSE\\nMCP servers can communicate locally via standard input/output (stdio) or remotely via HTTP Server-Sent Events (SSE). Stdio is preferred for local, high-security operations.", "instructions": "## Task: Local Transport\\nWhich transport mechanism is generally used when an AI Agent spins up a local MCP server as a subprocess on the same machine?", "starterCode": "# Options: WebSockets, Stdio, REST API\\ntransport = '___'", "solution": "# Options: WebSockets, Stdio, REST API\\ntransport = 'Stdio'", "hint": "Stdio", "rubric": "Identifies Stdio."},
            {"title": "Exposing Tools", "theory": "## tools/list\\nWhen an AI Agent connects to your MCP Server, it first asks 'What can you do?'. Your server responds to the `tools/list` request with a JSON schema describing every available function.", "instructions": "## Task: Tool Definition\\nWhen exposing a 'calculator' tool, you must provide its name, description, and the JSON schema for its ___.", "starterCode": "# Options: inputSchema, outputSchema, errorLogs\\nproperty = '___'", "solution": "# Options: inputSchema, outputSchema, errorLogs\\nproperty = 'inputSchema'", "hint": "inputSchema", "rubric": "Identifies inputSchema."},
            {"title": "Handling Tool Calls", "theory": "## tools/call\\nWhen the AI Agent decides to use a tool, it sends a `tools/call` request with the tool name and arguments. Your server executes the actual code (e.g., querying a database) and returns the result as text or images.", "instructions": "## Task: Response Format\\nWhen returning text from an MCP tool call, the `content` array must contain an object with a type of what?", "starterCode": "response = {\\n  content: [ { type: '___', text: 'Result is 42' } ]\\n}", "solution": "response = {\\n  content: [ { type: 'text', text: 'Result is 42' } ]\\n}", "hint": "The type is text", "rubric": "Identifies text."},
            {"title": "Exposing Resources", "theory": "## resources/list\\nUnlike Tools (which perform actions), Resources provide static or dynamic data context to the AI (like 'API Documentation' or 'Current System Logs'). They are accessed via custom URI templates.", "instructions": "## Task: Resource URI\\nWhat URI scheme is typically used to expose a custom resource in an MCP server (e.g., `___://logs/system`)?", "starterCode": "uri = '___://logs/system'", "solution": "uri = 'file://logs/system'", "hint": "file (or a custom scheme, but usually file or specific protocol). Let's accept 'custom' or whatever is specific.", "rubric": "Any URI scheme is acceptable."},
            {"title": "Exposing Prompts", "theory": "## prompts/list\\nMCP Servers can also expose predefined Prompts. This allows the server to dictate exactly how the AI should format its queries when interacting with the server's specific domain.", "instructions": "## Task: Prompt Arguments\\nPrompts can accept dynamic arguments. If your prompt is 'Summarize a file', what argument should it require?", "starterCode": "argument_name = '___'", "solution": "argument_name = 'filepath'", "hint": "filepath", "rubric": "Identifies filepath or filename."},
            {"title": "Security & Sandboxing", "theory": "## Never Trust the Agent\\nMCP Servers execute code on behalf of the AI. You must heavily validate all inputs, restrict file system access to specific directories, and never allow raw bash execution without user consent.", "instructions": "## Task: Best Practice\\nIf an agent sends `tools/call` to 'delete_file' with `path=\"/etc/passwd\"`, what should the MCP server do?", "starterCode": "# Options: Execute it, Reject due to sandbox violation, Ask the user\\naction = '___'", "solution": "# Options: Execute it, Reject due to sandbox violation, Ask the user\\naction = 'Reject due to sandbox violation'", "hint": "Reject due to sandbox violation", "rubric": "Identifies Reject due to sandbox violation."},
            {"title": "Deploying an MCP Server", "theory": "## Dockerization\\nBecause MCP Servers often require specific environments (Python, Node, system dependencies), the best way to distribute them is via Docker containers. The Agent can then run `docker run -i` to communicate via Stdio.", "instructions": "## Task: Interactive Flag\\nWhich Docker flag is required to keep Stdin open so the AI agent can communicate with the containerized MCP server?", "starterCode": "flag = '-___'", "solution": "flag = '-i'", "hint": "-i", "rubric": "Identifies -i."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'agentic_ai_mcp.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # We'll patch the 'Exposing Resources' solution to be 'custom' to fit typical generic MCP URI instructions
        NEW_COURSES_BATCH57["Building MCP Servers Masterclass"]["lessons"][4]["solution"] = "uri = 'custom://logs/system'"
        
        for new_course_name, course_info in NEW_COURSES_BATCH57.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH57.items():
            tier = course_info["tier"]
            if "Agentic AI & MCP" in index_data and tier in index_data["Agentic AI & MCP"]:
                if new_course_name not in index_data["Agentic AI & MCP"][tier]:
                    index_data["Agentic AI & MCP"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 57: Added {total} lessons to Agentic AI & MCP track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
