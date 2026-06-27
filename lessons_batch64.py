"""
Batch 64: Deep Dive into Data Engineering & MLOps (Distributed Computing & Spark Masterclass)
"""
import json, os

NEW_COURSES_BATCH64 = {
    "Distributed Computing & Spark Masterclass": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of Apache Spark and distributed computing concepts",
        "lessons": [
            {"title": "Hadoop vs Apache Spark", "theory": "## In-Memory Speed\\nHadoop MapReduce writes intermediate results to disk, which is very slow. Apache Spark revolutionized distributed computing by keeping intermediate data in-memory (RAM), making it up to 100x faster for iterative workloads like Machine Learning.", "instructions": "## Task: The Secret Sauce\\nWhat is the primary architectural difference that makes Apache Spark so much faster than Hadoop MapReduce?", "starterCode": "# Options: Disk-based storage, In-memory computation, Using Python instead of Java\\nadvantage = '___'", "solution": "# Options: Disk-based storage, In-memory computation, Using Python instead of Java\\nadvantage = 'In-memory computation'", "hint": "In-memory computation", "rubric": "Identifies In-memory computation."},
            {"title": "Resilient Distributed Datasets (RDDs)", "theory": "## The Core Abstraction\\nAn RDD is Spark's fundamental data structure. They are distributed across the cluster, immutable (cannot be changed once created), and fault-tolerant because they remember their 'lineage' (the steps used to create them).", "instructions": "## Task: Fault Tolerance\\nIf a node in a Spark cluster crashes and loses an RDD partition, how does Spark recover the lost data?", "starterCode": "# Options: Recomputes it using the lineage graph, Asks the user to restart, Reads it from a backup database\\nrecovery_method = '___'", "solution": "# Options: Recomputes it using the lineage graph, Asks the user to restart, Reads it from a backup database\\nrecovery_method = 'Recomputes it using the lineage graph'", "hint": "Recomputes it using the lineage graph", "rubric": "Identifies Recomputes it using the lineage graph."},
            {"title": "Spark DataFrames and Catalyst", "theory": "## The Optimizer\\nWhile RDDs give you low-level control, Spark DataFrames provide a higher-level API. Behind the scenes, the Catalyst Optimizer analyzes your DataFrame code and generates an optimized physical execution plan.", "instructions": "## Task: The Engine\\nWhat is the name of the engine that optimizes DataFrame and Spark SQL queries before execution?", "starterCode": "engine = 'The ___ Optimizer'", "solution": "engine = 'The Catalyst Optimizer'", "hint": "Catalyst Optimizer", "rubric": "Identifies Catalyst."},
            {"title": "Lazy Evaluation", "theory": "## Waiting to Execute\\nIn Spark, 'Transformations' (like `map` or `filter`) do not execute immediately; they just build the lineage graph. Spark only actually runs the computation when an 'Action' (like `count` or `collect`) is called. This is called Lazy Evaluation.", "instructions": "## Task: Action vs Transformation\\nWhich of the following Spark operations will actually trigger computation across the cluster?", "starterCode": "# Options: .filter(), .select(), .count()\\ntrigger = '___'", "solution": "# Options: .filter(), .select(), .count()\\ntrigger = '.count()'", "hint": ".count() is an action", "rubric": "Identifies .count()."},
            {"title": "Partitioning and Shuffling", "theory": "## Network Bottlenecks\\nSpark splits data into 'partitions' across different nodes. Operations like `groupByKey` or `join` require data to be moved between different nodes. This massive movement of data across the network is called a 'Shuffle' and is the biggest performance bottleneck.", "instructions": "## Task: The Bottleneck\\nWhat is the term for the expensive operation where Spark redistributes data across the cluster's network?", "starterCode": "term = '___'", "solution": "term = 'Shuffle'", "hint": "Shuffle", "rubric": "Identifies Shuffle."},
            {"title": "Broadcast Variables", "theory": "## Distributing Lookups\\nIf you have a small lookup table (like a list of zip codes) that every node needs for a Join, a standard join will cause a massive Shuffle. Instead, you can 'Broadcast' the small table, sending a read-only copy to every node's memory.", "instructions": "## Task: Avoid the Shuffle\\nTo optimize a join between a 1TB table and a 10MB lookup table, what type of variable should you use for the 10MB table?", "starterCode": "variable_type = '___ Variable'", "solution": "variable_type = 'Broadcast Variable'", "hint": "Broadcast Variable", "rubric": "Identifies Broadcast Variable."},
            {"title": "PySpark SQL", "theory": "## SQL on Clusters\\nYou don't have to learn the DataFrame API to use Spark. You can register a DataFrame as a temporary view and run standard ANSI SQL queries against terabytes of data using `spark.sql()`.", "instructions": "## Task: Query Execution\\nWrite the method call to execute a raw SQL query string against registered views in PySpark.", "starterCode": "df = ___.sql('SELECT * FROM users WHERE age > 21')", "solution": "df = spark.sql('SELECT * FROM users WHERE age > 21')", "hint": "Use spark", "rubric": "Uses spark.sql()."},
            {"title": "Structured Streaming", "theory": "## Real-Time Pipelines\\nSpark isn't just for batch processing. Structured Streaming allows you to process real-time data (e.g., from Kafka) using the exact same DataFrame API you use for batch processing, treating the stream as an infinitely growing table.", "instructions": "## Task: The Abstraction\\nIn Structured Streaming, a real-time data stream is conceptually treated as an unbounded what?", "starterCode": "# Options: Unbounded Array, Unbounded Table, Unbounded Dictionary\\nconcept = '___'", "solution": "# Options: Unbounded Array, Unbounded Table, Unbounded Dictionary\\nconcept = 'Unbounded Table'", "hint": "Unbounded Table", "rubric": "Identifies Unbounded Table."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'data_engineering_mlops.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH64.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH64.items():
            tier = course_info["tier"]
            if "Data Engineering & MLOps" in index_data and tier in index_data["Data Engineering & MLOps"]:
                if new_course_name not in index_data["Data Engineering & MLOps"][tier]:
                    index_data["Data Engineering & MLOps"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 64: Added {total} lessons to Data Engineering & MLOps track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
