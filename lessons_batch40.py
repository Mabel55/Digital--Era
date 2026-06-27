"""
Batch 40: Expanding System Design & Architecture Curriculum (Load Balancing, API Gateways, Sharding, CAP, Rate Limiting)
"""
import json, os

NEW_COURSES_BATCH40 = {
    "Load Balancing Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess load balancing fundamentals",
        "lessons": [
            {"title": "Horizontal Scaling", "theory": "## Scaling Out\\nWhen a single server cannot handle the traffic, you scale horizontally by adding more servers. A Load Balancer sits in front of them to distribute the incoming requests.", "instructions": "## Task: Load Balancer Role\\nSelect the primary role of a load balancer from the options.", "starterCode": "# Options:\\n# A. Store database backups\\n# B. Distribute incoming network traffic across multiple servers\\n# C. Compile code faster\\n\\nanswer = '___'", "solution": "# Options:\\n# A. Store database backups\\n# B. Distribute incoming network traffic across multiple servers\\n# C. Compile code faster\\n\\nanswer = 'B'", "hint": "The answer is B", "rubric": "Correctly identifies B as the answer."},
            {"title": "Round Robin", "theory": "## Traffic Distribution Algorithms\\nRound Robin is the simplest load balancing algorithm. It forwards requests to each server in the pool sequentially.", "instructions": "## Task: Round Robin Logic\\nImplement a simple round-robin function that returns the next server from a list of servers based on the current request count.", "starterCode": "servers = ['ServerA', 'ServerB', 'ServerC']\\n\\ndef get_next_server(request_count):\\n    index = request_count ___ len(servers)\\n    return servers[index]", "solution": "servers = ['ServerA', 'ServerB', 'ServerC']\\n\\ndef get_next_server(request_count):\\n    index = request_count % len(servers)\\n    return servers[index]", "hint": "Use the modulo operator %", "rubric": "Correctly uses the modulo operator for round robin."}
        ]
    },
    "API Gateways": {
        "tier": "Intermediate",
        "aiRubric": "Assess API gateway concepts",
        "lessons": [
            {"title": "The Single Entry Point", "theory": "## Facade Pattern for Microservices\\nAn API Gateway acts as a single entry point for a group of microservices. It handles routing, authentication, and SSL termination so individual services don't have to.", "instructions": "## Task: Routing Configuration\\nWrite a mock routing configuration that sends requests from `/users` to the User Service and `/orders` to the Order Service.", "starterCode": "routes = {\\n    '/___': 'http://user-service:8080',\\n    '/___': 'http://order-service:8080'\\n}", "solution": "routes = {\\n    '/users': 'http://user-service:8080',\\n    '/orders': 'http://order-service:8080'\\n}", "hint": "Use users and orders", "rubric": "Correctly maps users and orders."},
            {"title": "Cross-Cutting Concerns", "theory": "## Centralized Logic\\nInstead of writing authentication code in 50 different microservices, you write it once in the API Gateway.", "instructions": "## Task: Gateway Middleware\\nWrite a simple middleware that checks for an 'Authorization' header before routing the request.", "starterCode": "def api_gateway_handler(request):\\n    if '___' not in request.headers:\\n        return 401 // Unauthorized\\n    return route_request(request)", "solution": "def api_gateway_handler(request):\\n    if 'Authorization' not in request.headers:\\n        return 401 // Unauthorized\\n    return route_request(request)", "hint": "Check for Authorization", "rubric": "Correctly checks for the Authorization header."}
        ]
    },
    "Database Sharding": {
        "tier": "Intermediate",
        "aiRubric": "Assess database sharding",
        "lessons": [
            {"title": "Partitioning Data", "theory": "## Sharding Basics\\nSharding is a type of database partitioning that separates very large databases into smaller, faster, more easily managed parts called data shards.", "instructions": "## Task: Shard Key Concept\\nThe piece of data used to determine which shard a row belongs to is called the Shard ___.", "starterCode": "answer = 'Shard ___'", "solution": "answer = 'Shard Key'", "hint": "It's called a Shard Key", "rubric": "Correctly identifies Shard Key."},
            {"title": "Consistent Hashing", "theory": "## Distributing Data Evenly\\nIf you shard by `user_id % num_shards`, adding a new shard requires moving almost all data. Consistent Hashing solves this by placing servers and data on a virtual ring.", "instructions": "## Task: Hash Ring\\nIf a new server is added to a Consistent Hash ring, does it require remapping all keys or only a small subset of keys?", "starterCode": "answer = '___'", "solution": "answer = 'Only a small subset of keys'", "hint": "It only requires a small subset", "rubric": "Correctly indicates that only a small subset is remapped."}
        ]
    },
    "CAP Theorem & Consensus": {
        "tier": "Advanced",
        "aiRubric": "Assess CAP theorem and distributed consensus",
        "lessons": [
            {"title": "The CAP Theorem", "theory": "## Pick Two\\nThe CAP theorem states that a distributed data store can only simultaneously provide two of three guarantees: Consistency, Availability, and Partition Tolerance.", "instructions": "## Task: Define CAP\\nAssign the three guarantees of the CAP theorem.", "starterCode": "C = '___'\\nA = '___'\\nP = '___'", "solution": "C = 'Consistency'\\nA = 'Availability'\\nP = 'Partition Tolerance'", "hint": "Consistency, Availability, Partition Tolerance", "rubric": "Correctly spells out Consistency, Availability, and Partition Tolerance."},
            {"title": "Consensus Algorithms", "theory": "## Raft and Paxos\\nIn distributed systems, servers must agree on a single state. Algorithms like Raft achieve this by electing a Leader to handle all writes, replicating them to Followers.", "instructions": "## Task: Leader Election\\nIn the Raft algorithm, if a Follower doesn't hear from the Leader within a timeout period, it becomes a ___.", "starterCode": "answer = '___'", "solution": "answer = 'Candidate'", "hint": "It becomes a Candidate", "rubric": "Correctly identifies Candidate."}
        ]
    },
    "Rate Limiting Algorithms": {
        "tier": "Advanced",
        "aiRubric": "Assess rate limiting knowledge",
        "lessons": [
            {"title": "Token Bucket", "theory": "## The Token Bucket Algorithm\\nA bucket holds tokens. Tokens are added at a constant rate. A request costs 1 token. If the bucket is empty, the request is dropped.", "instructions": "## Task: Bucket Logic\\nImplement the check to see if a request should be allowed based on token count.", "starterCode": "def allow_request(tokens):\\n    if tokens ___ 0:\\n        tokens -= 1\\n        return True\\n    return ___", "solution": "def allow_request(tokens):\\n    if tokens > 0:\\n        tokens -= 1\\n        return True\\n    return False", "hint": "Use > and False", "rubric": "Correctly checks if tokens > 0 and returns False."},
            {"title": "Leaky Bucket", "theory": "## Smoothing Traffic\\nUnlike the Token Bucket which allows bursts of traffic, the Leaky Bucket processes requests at a constant, fixed rate (like water dripping from a hole).", "instructions": "## Task: Identify Algorithm\\nWhich algorithm enforces a strict, constant output rate regardless of bursty input?", "starterCode": "answer = '___ Bucket'", "solution": "answer = 'Leaky Bucket'", "hint": "Leaky Bucket", "rubric": "Correctly identifies Leaky Bucket."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'system_design_architecture.json')
    
    # 1. Update system_design_architecture.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH40.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH40.items():
            tier = course_info["tier"]
            if "System Design & Architecture" in index_data and tier in index_data["System Design & Architecture"]:
                if new_course_name not in index_data["System Design & Architecture"][tier]:
                    index_data["System Design & Architecture"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 40: Added {total} lessons to System Design & Architecture track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
