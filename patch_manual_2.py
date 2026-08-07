import json
import os

TRACKS_THEORY = {
    "ui_ux.json": {
        "Data-Driven Design": "## Making Decisions with Data\nGood design is not just about making things look pretty or following your gut instinct; it is about solving problems for users. **Data-Driven Design** is the practice of using quantitative and qualitative data to inform your design decisions.\n\nImagine you are debating with your team whether the 'Checkout' button should be green or blue, or if it should be at the top or bottom of the screen. Instead of arguing based on personal preference, you run an A/B test. You show 50% of users the green button and 50% the blue button. If the data shows that the green button results in 15% more sales, the decision is made for you.\n\nBy leveraging tools like Google Analytics, Heatmaps (like Hotjar), and A/B testing platforms, designers can identify where users are getting stuck, what features they actually use, and whether a redesign objectively improved the user experience."
    },
    "data_structures_algorithms.json": {
        "Time Complexity Basics": "## Big O Notation\nWhen writing software, there are often dozens of different ways to solve the exact same problem. How do we know which algorithm is 'better'? We use **Time Complexity**, typically expressed in **Big O Notation**.\n\nBig O Notation doesn't measure the exact time an algorithm takes in seconds (because a supercomputer will run the exact same code faster than an old laptop). Instead, it measures how the runtime *grows* as the amount of input data (N) grows. \n\nFor example, if you have to look at every single item in a list of N items, the time complexity is **O(N)** (Linear Time). If the list doubles in size, the time it takes doubles. If an algorithm takes the exact same amount of time regardless of how big the list is (like fetching the first item), it is **O(1)** (Constant Time). Understanding this is critical for writing code that scales from 10 users to 10 million users."
    },
    "agent_theory.json": {
        "What is a Cognitive Architecture?": "## The Brain of an Agent\nWhen building an AI Agent, simply throwing a prompt at a Large Language Model isn't enough. A **Cognitive Architecture** is the blueprint for how an AI system thinks, remembers, and acts. It is the structural framework that gives the LLM its 'brain'.\n\nThink of the LLM as the raw reasoning engine (the prefrontal cortex). But a human needs more than just reasoning—we need memory to recall past events, tools (hands) to interact with the world, and a loop to observe our environment and plan our next move. \n\nA Cognitive Architecture ties all these pieces together. It dictates how the agent retrieves context from a vector database (memory), how it decides which API to call (tool use), and how it breaks a massive goal down into a step-by-step plan (reasoning). Frameworks like LangChain and LlamaIndex provide the building blocks to construct these architectures.",
        "The ReAct Architecture In-Depth": "## Reason + Act\nThe **ReAct** (Reasoning and Acting) framework is a foundational cognitive architecture that interleaves thinking with doing. It forces the LLM to 'think out loud' before taking an action.\n\nImagine you are asked to 'Find the current CEO of Apple and email them.' A naive LLM might just hallucinate a name and try to write an email immediately. The ReAct framework forces the agent into a loop: \n1. **Thought:** 'I need to find out who the CEO of Apple is. I should search Wikipedia.'\n2. **Action:** `SearchWikipedia('Apple CEO')`\n3. **Observation:** 'Tim Cook is the CEO.'\n4. **Thought:** 'Now I know the CEO is Tim Cook. I need his email address...'\n\nBy explicitly generating a 'Thought' before every 'Action', the agent is much less likely to hallucinate and can dynamically adjust its plan based on the 'Observation' it receives from its environment.",
        "Agent Communication Languages": "## How Agents Talk\nAs we move from single-agent systems to multi-agent swarms, the agents need a standardized way to talk to each other. This is where **Agent Communication Languages (ACLs)** come in.\n\nThink of it like human languages. If an English-speaking manager tries to give instructions to a French-speaking worker, they will fail without a common language or translator. Similarly, if an 'Analysis Agent' needs to send a complex data structure to a 'Coding Agent', they need an agreed-upon format.\n\nWhile traditional ACLs like FIPA-ACL exist, modern LLM agents typically use structured JSON formats (like OpenAI's Function Calling schema) to communicate. The message usually contains an `intent` (e.g., 'REQUEST', 'INFORM'), the `sender`, the `receiver`, and the structured `payload`. This allows specialized agents to collaborate seamlessly to solve complex tasks.",
        "The Reflection Pattern": "## Self-Correction\nThe **Reflection Pattern** is a powerful technique where an agent is explicitly instructed to review, critique, and correct its own past outputs or actions before finalizing a result.\n\nHumans rarely write a perfect essay on the first draft. We write, we review, we find our own mistakes, and we edit. The Reflection pattern applies this exact loop to AI. \n\nFor example, a Coding Agent might write a Python script. Instead of returning it to the user immediately, the script is passed to a 'Critic' prompt (or a separate Critic Agent). The Critic reviews the code for bugs, security flaws, or inefficiencies and provides feedback. The Coding Agent then uses that feedback to rewrite the code. This iterative loop of generation and critique drastically improves the quality and reliability of the final output."
    }
}

if __name__ == "__main__":
    total_patched = 0
    for filename, theory_dict in TRACKS_THEORY.items():
        filepath = os.path.join("curriculum", "tracks", filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            patched = 0
            for topic, topic_data in data.items():
                for lesson in topic_data.get("lessons", []):
                    if lesson.get("title") in theory_dict:
                        lesson["theory"] = theory_dict[lesson.get("title")]
                        patched += 1
                        
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            print(f"Patched {patched} lessons in {filename}")
            total_patched += patched
            
    print(f"Total patched: {total_patched}")
