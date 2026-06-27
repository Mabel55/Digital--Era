"""
Batch 52: Expanding AI Engineering Curriculum (Tokens, Caching, Structured Outputs, LoRA, Multi-Modal)
"""
import json, os

NEW_COURSES_BATCH52 = {
    "Tokenization Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess tokenization concepts",
        "lessons": [
            {"title": "Words vs Tokens", "theory": "## How LLMs Read\\nLLMs don't read words; they read 'tokens'. A token is a chunk of text. In English, 1 token is roughly 4 characters or 0.75 words. A long word like 'unbelievable' might be split into multiple tokens.", "instructions": "## Task: Token Mapping\\nIf an LLM uses Byte Pair Encoding (BPE), what is the most likely way it tokenizes the word 'hamburger'?", "starterCode": "# Options: [hamburger], [ham, burger], [h,a,m,b,u,r,g,e,r]\\ntokens = '___'", "solution": "# Options: [hamburger], [ham, burger], [h,a,m,b,u,r,g,e,r]\\ntokens = '[ham, burger]'", "hint": "It splits into common subwords: [ham, burger]", "rubric": "Identifies [ham, burger]."},
            {"title": "Context Windows", "theory": "## Short-Term Memory\\nEvery LLM has a maximum context window limit (e.g., 128k tokens). This limit includes BOTH the input prompt you send and the output response it generates.", "instructions": "## Task: Context Limit Calculation\\nIf a model has a 4096 token limit and your input prompt is 3000 tokens, what is the maximum number of tokens it can generate in its response?", "starterCode": "max_output = 4096 - ___", "solution": "max_output = 4096 - 3000", "hint": "Subtract 3000", "rubric": "Subtracts 3000."}
        ]
    },
    "Caching LLM Responses": {
        "tier": "Intermediate",
        "aiRubric": "Assess LLM caching strategies",
        "lessons": [
            {"title": "Exact Match Caching", "theory": "## Saving Money & Time\\nIf thousands of users ask 'What is the capital of France?', you shouldn't call the OpenAI API every time. You can cache the exact string in Redis and return it instantly.", "instructions": "## Task: Cache Check\\nWrite an if-statement that checks if the `user_prompt` exists in the `cache` dictionary.", "starterCode": "cache = {'Hello': 'Hi there!'}\\nuser_prompt = 'Hello'\\nif user_prompt ___ ___:\\n    return cache[user_prompt]", "solution": "cache = {'Hello': 'Hi there!'}\\nuser_prompt = 'Hello'\\nif user_prompt in cache:\\n    return cache[user_prompt]", "hint": "Use 'in cache'", "rubric": "Correctly checks if user_prompt in cache."},
            {"title": "Semantic Caching", "theory": "## Similar Intent\\nExact match caching fails if someone asks 'What's the capital of France?' instead of 'What is the capital of France?'. Semantic caching solves this by comparing the *embedding* of the new query to cached embeddings. If they are 99% similar, it returns the cached response.", "instructions": "## Task: Similarity Metric\\nWhat metric does a Semantic Cache use to compare the new query against cached queries?", "starterCode": "metric = '___ Similarity'", "solution": "metric = 'Cosine Similarity'", "hint": "Cosine Similarity", "rubric": "Identifies Cosine Similarity."}
        ]
    },
    "Structured Outputs": {
        "tier": "Intermediate",
        "aiRubric": "Assess constrained LLM generation",
        "lessons": [
            {"title": "JSON Mode", "theory": "## Predictable Parsing\\nIf you want an LLM to extract data from a resume, you need it returned in a strict JSON format so your code can parse it. Many APIs offer a 'JSON Mode' to guarantee this.", "instructions": "## Task: Enable JSON Mode\\nIn the OpenAI API, how do you specify the response format to ensure valid JSON?", "starterCode": "response_format = { 'type': '___' }", "solution": "response_format = { 'type': 'json_object' }", "hint": "The type is json_object", "rubric": "Sets type to json_object."},
            {"title": "Constrained Generation", "theory": "## Guiding the Grammar\\nAdvanced tools like `guidance` or `outlines` force the LLM to only output tokens that adhere to a specific Pydantic model or Regex pattern, completely eliminating parsing errors.", "instructions": "## Task: Regex Constraint\\nIf you constrain the LLM to only output matching `^\\d{4}$`, what is it generating?", "starterCode": "# Options: A 4-letter word, A 4-digit number, A JSON object\\noutput_type = '___'", "solution": "# Options: A 4-letter word, A 4-digit number, A JSON object\\noutput_type = 'A 4-digit number'", "hint": "It generates A 4-digit number", "rubric": "Identifies A 4-digit number."}
        ]
    },
    "LoRA & QLoRA": {
        "tier": "Advanced",
        "aiRubric": "Assess parameter-efficient fine-tuning",
        "lessons": [
            {"title": "Low-Rank Adaptation", "theory": "## Freezing the Base Model\\nFine-tuning a 70B model normally requires massive GPU clusters. LoRA freezes the original weights and injects tiny, trainable 'rank decomposition matrices' into the layers, reducing trainable parameters by 99%.", "instructions": "## Task: LoRA Memory Benefit\\nWhy does LoRA allow you to fine-tune large models on a single consumer GPU?", "starterCode": "# Options: It compresses the dataset, It drastically reduces trainable parameters\\nreason = '___'", "solution": "# Options: It compresses the dataset, It drastically reduces trainable parameters\\nreason = 'It drastically reduces trainable parameters'", "hint": "It drastically reduces trainable parameters", "rubric": "Identifies that it reduces trainable parameters."},
            {"title": "QLoRA", "theory": "## Quantized LoRA\\nQLoRA takes it a step further: it loads the base model in 4-bit precision (Quantized), and trains the tiny LoRA adapters in 16-bit precision. This maximizes memory efficiency.", "instructions": "## Task: QLoRA Base Model\\nIn QLoRA, what bit precision is the massive *base model* typically loaded into?", "starterCode": "precision = '___-bit'", "solution": "precision = '4-bit'", "hint": "4-bit", "rubric": "Identifies 4-bit."}
        ]
    },
    "Multi-Modal Models": {
        "tier": "Advanced",
        "aiRubric": "Assess multi-modal architectures",
        "lessons": [
            {"title": "Vision-Language Models", "theory": "## Seeing the World\\nVLMs (like GPT-4V or LLaVA) use an Image Encoder (like CLIP) to convert images into embeddings, which are then passed alongside text embeddings into the LLM.", "instructions": "## Task: The Image Encoder\\nWhat architecture is most commonly used to encode images into embeddings for a Vision-Language Model?", "starterCode": "# Options: RNN, Vision Transformer (ViT), LSTM\\nencoder = '___'", "solution": "# Options: RNN, Vision Transformer (ViT), LSTM\\nencoder = 'Vision Transformer (ViT)'", "hint": "Vision Transformer (ViT)", "rubric": "Identifies Vision Transformer (ViT)."},
            {"title": "Joint Embedding Spaces", "theory": "## Cross-Modal Search\\nModels like CLIP map text and images into the *exact same* embedding space. This means the embedding for the word 'Dog' and the embedding for a picture of a dog will have a high cosine similarity.", "instructions": "## Task: Search Application\\nIf text and images are in the same embedding space, what powerful feature does this enable?", "starterCode": "# Options: Image Generation, Text-to-Image Search\\nfeature = '___'", "solution": "# Options: Image Generation, Text-to-Image Search\\nfeature = 'Text-to-Image Search'", "hint": "Text-to-Image Search", "rubric": "Identifies Text-to-Image Search."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'ai_engineering.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH52.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH52.items():
            tier = course_info["tier"]
            if "AI Engineering" in index_data and tier in index_data["AI Engineering"]:
                if new_course_name not in index_data["AI Engineering"][tier]:
                    index_data["AI Engineering"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 52: Added {total} lessons to AI Engineering track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
