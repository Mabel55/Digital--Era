"""
Batch 34: Expanding Backend Curriculum (FastAPI, Redis, Serverless, Kafka, gRPC)
"""
import json, os

NEW_COURSES_BATCH34 = {
    "Python FastAPI Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess FastAPI basics",
        "lessons": [
            {"title": "FastAPI Setup", "theory": "## Modern Python APIs\\nFastAPI is a modern, fast web framework for building APIs with Python based on standard Python type hints.", "instructions": "## Task: Create an Endpoint\\nCreate a GET endpoint at `/hello` that returns a JSON message.", "starterCode": "from fastapi import FastAPI\\n\\napp = FastAPI()\\n\\n@app.___('/hello')\\ndef read_hello():\\n    return {'message': '___'}", "solution": "from fastapi import FastAPI\\n\\napp = FastAPI()\\n\\n@app.get('/hello')\\ndef read_hello():\\n    return {'message': 'Hello World'}", "hint": "Use @app.get and return 'Hello World'", "rubric": "Correctly defines a GET route."},
            {"title": "Path Parameters", "theory": "## Dynamic URLs\\nYou can declare path parameters or variables with the same syntax used by Python format strings.", "instructions": "## Task: Item ID\\nCreate an endpoint that takes an `item_id` in the URL and returns it.", "starterCode": "from fastapi import FastAPI\\n\\napp = FastAPI()\\n\\n@app.get('/items/{___}')\\ndef read_item(item_id: ___):\\n    return {'item_id': item_id}", "solution": "from fastapi import FastAPI\\n\\napp = FastAPI()\\n\\n@app.get('/items/{item_id}')\\ndef read_item(item_id: int):\\n    return {'item_id': item_id}", "hint": "item_id and int", "rubric": "Correctly captures the item_id parameter with type int."}
        ]
    },
    "Caching with Redis": {
        "tier": "Intermediate",
        "aiRubric": "Assess Redis caching",
        "lessons": [
            {"title": "Redis Basics", "theory": "## In-Memory Datastore\\nRedis stores data in RAM, making read and write operations incredibly fast compared to traditional databases. It's often used as a cache.", "instructions": "## Task: Set and Get\\nUse the Redis Python client to set a key 'user:1' to 'Alice' and then retrieve it.", "starterCode": "import redis\\n\\nr = redis.Redis(host='localhost', port=6379, db=0)\\n\\n# Set the key\\nr.___('user:1', 'Alice')\\n\\n# Get the key\\nname = r.___('user:1')\\nprint(name.decode('utf-8'))", "solution": "import redis\\n\\nr = redis.Redis(host='localhost', port=6379, db=0)\\n\\n# Set the key\\nr.set('user:1', 'Alice')\\n\\n# Get the key\\nname = r.get('user:1')\\nprint(name.decode('utf-8'))", "hint": "Use set() and get()", "rubric": "Correctly uses set and get commands."},
            {"title": "Cache Expiration", "theory": "## Time-To-Live (TTL)\\nCaches should not hold stale data forever. You can set a TTL (Time-To-Live) on keys so they automatically delete themselves after a duration.", "instructions": "## Task: Set with TTL\\nSet a key 'session_token' that expires in 60 seconds.", "starterCode": "import redis\\n\\nr = redis.Redis()\\n\\n# Set with expiration\\nr.setex('session_token', ___, 'abc123xyz')", "solution": "import redis\\n\\nr = redis.Redis()\\n\\n# Set with expiration\\nr.setex('session_token', 60, 'abc123xyz')", "hint": "Pass 60 for the time", "rubric": "Correctly uses setex with 60 seconds."}
        ]
    },
    "Serverless Functions": {
        "tier": "Intermediate",
        "aiRubric": "Assess serverless concepts",
        "lessons": [
            {"title": "AWS Lambda Basics", "theory": "## Event-Driven Compute\\nServerless functions (like AWS Lambda) run your code in response to events (HTTP requests, file uploads) without provisioning servers.", "instructions": "## Task: Lambda Handler\\nWrite the basic structure of an AWS Lambda function handler in Python.", "starterCode": "def ___(event, context):\\n    body = event.get('body', {})\\n    return {\\n        'statusCode': ___,\\n        'body': 'Success'\\n    }", "solution": "def lambda_handler(event, context):\\n    body = event.get('body', {})\\n    return {\\n        'statusCode': 200,\\n        'body': 'Success'\\n    }", "hint": "lambda_handler and 200", "rubric": "Correctly names lambda_handler and returns a 200 status code."},
            {"title": "Cold Starts", "theory": "## The Serverless Tradeoff\\nBecause servers scale to zero when unused, the first request after a period of inactivity experiences a 'cold start' delay while the container boots up.", "instructions": "## Task: Global State Initialization\\nInitialize heavy resources (like DB connections) *outside* the handler to mitigate cold starts for subsequent warm invocations.", "starterCode": "import database\\n\\n# Initialize outside handler\\ndb_conn = database.___()\\n\\ndef lambda_handler(event, context):\\n    data = db_conn.query('SELECT *')\\n    return {'statusCode': 200}", "solution": "import database\\n\\n# Initialize outside handler\\ndb_conn = database.connect()\\n\\ndef lambda_handler(event, context):\\n    data = db_conn.query('SELECT *')\\n    return {'statusCode': 200}", "hint": "Use connect()", "rubric": "Initializes the DB connection globally."}
        ]
    },
    "Message Queues & Kafka": {
        "tier": "Advanced",
        "aiRubric": "Assess messaging queues",
        "lessons": [
            {"title": "Producers and Consumers", "theory": "## Asynchronous Messaging\\nMessage queues decouple services. A Producer sends a message to a topic, and a Consumer reads from that topic at its own pace.", "instructions": "## Task: Kafka Producer\\nWrite a snippet to send a JSON message to a Kafka topic named 'orders'.", "starterCode": "from kafka import KafkaProducer\\nimport json\\n\\nproducer = KafkaProducer(\\n    value_serializer=lambda v: json.dumps(v).___('utf-8')\\n)\\n\\nproducer.___('___', {'order_id': 101, 'amount': 25.50})", "solution": "from kafka import KafkaProducer\\nimport json\\n\\nproducer = KafkaProducer(\\n    value_serializer=lambda v: json.dumps(v).encode('utf-8')\\n)\\n\\nproducer.send('orders', {'order_id': 101, 'amount': 25.50})", "hint": "encode and send to 'orders'", "rubric": "Correctly serializes and sends the message."},
            {"title": "Consumer Groups", "theory": "## Scalable Processing\\nMultiple consumers can read from the same topic by joining a 'Consumer Group'. Kafka automatically splits the topic's partitions among the group members.", "instructions": "## Task: Kafka Consumer\\nCreate a consumer that listens to the 'orders' topic under the group 'order-processors'.", "starterCode": "from kafka import KafkaConsumer\\n\\nconsumer = KafkaConsumer(\\n    '___',\\n    group_id='___'\\n)\\n\\nfor message in consumer:\\n    print(message.value)", "solution": "from kafka import KafkaConsumer\\n\\nconsumer = KafkaConsumer(\\n    'orders',\\n    group_id='order-processors'\\n)\\n\\nfor message in consumer:\\n    print(message.value)", "hint": "orders and order-processors", "rubric": "Correctly configures the topic and group_id."}
        ]
    },
    "gRPC & Protocol Buffers": {
        "tier": "Advanced",
        "aiRubric": "Assess gRPC knowledge",
        "lessons": [
            {"title": "Protobuf Definitions", "theory": "## Strictly Typed Contracts\\nInstead of JSON, gRPC uses Protocol Buffers (.proto files) to define strict, binary-serialized contracts between microservices.", "instructions": "## Task: Define a Message\\nWrite a simple Protobuf message for a User containing a string name and an int32 id.", "starterCode": "syntax = \"proto3\";\\n\\nmessage User {\\n  ___ name = 1;\\n  ___ id = 2;\\n}", "solution": "syntax = \"proto3\";\\n\\nmessage User {\\n  string name = 1;\\n  int32 id = 2;\\n}", "hint": "string and int32", "rubric": "Correctly assigns protobuf types."},
            {"title": "Defining Services", "theory": "## RPC Endpoints\\nInside a .proto file, you define the Service and the RPC (Remote Procedure Call) methods it exposes.", "instructions": "## Task: User Service\\nDefine an RPC method `GetUser` that takes a `UserRequest` and returns a `UserResponse`.", "starterCode": "service UserService {\\n  rpc ___(UserRequest) ___ (UserResponse);\\n}", "solution": "service UserService {\\n  rpc GetUser(UserRequest) returns (UserResponse);\\n}", "hint": "GetUser and returns", "rubric": "Correctly defines the rpc method and returns keyword."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'backend.json')
    
    # 1. Update backend.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH34.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH34.items():
            tier = course_info["tier"]
            if "Backend" in index_data and tier in index_data["Backend"]:
                if new_course_name not in index_data["Backend"][tier]:
                    index_data["Backend"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 34: Added {total} lessons to Backend track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
