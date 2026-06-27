"""
Batch 60: Deep Dive into Backend (System Observability & Monitoring Masterclass)
"""
import json, os

NEW_COURSES_BATCH60 = {
    "System Observability & Monitoring Masterclass": {
        "tier": "Advanced",
        "aiRubric": "Assess deep understanding of backend observability",
        "lessons": [
            {"title": "The Three Pillars of Observability", "theory": "## Seeing Inside the Black Box\\nObservability is defined by three primary pillars: Logs (record of events), Metrics (numerical measurements over time), and Traces (the end-to-end journey of a single request).", "instructions": "## Task: Identify the Pillar\\nWhich pillar of observability is best used to track the exact millisecond breakdown of a request as it hops between 5 different microservices?", "starterCode": "# Options: Logs, Metrics, Traces\\npillar = '___'", "solution": "# Options: Logs, Metrics, Traces\\npillar = 'Traces'", "hint": "Traces track journeys across services", "rubric": "Identifies Traces."},
            {"title": "Structured Logging", "theory": "## Stop Using Print()\\nUnstructured text logs like 'User 123 logged in' are hard to parse. Structured logging outputs logs in JSON format, making it trivial for log aggregators to query and filter.", "instructions": "## Task: JSON Log\\nWhat format does structured logging typically output to ensure machines can easily parse the logs?", "starterCode": "format = '___'", "solution": "format = 'JSON'", "hint": "JSON", "rubric": "Identifies JSON."},
            {"title": "Distributed Tracing", "theory": "## OpenTelemetry\\nWhen a request hits your API gateway, a 'Trace ID' is generated and passed in the headers to every downstream microservice. This allows tracing tools (like Jaeger) to stitch the entire request together.", "instructions": "## Task: Context Propagation\\nWhat is the name of the unique identifier that must be passed along to every service to link the logs/spans together?", "starterCode": "identifier = '___ ID'", "solution": "identifier = 'Trace ID'", "hint": "Trace ID", "rubric": "Identifies Trace ID."},
            {"title": "Application Metrics", "theory": "## Measuring Health\\nMetrics are aggregated numerical data. A 'Counter' only goes up (e.g., total requests). A 'Gauge' can go up and down (e.g., active websocket connections). A 'Histogram' measures distributions (e.g., response times).", "instructions": "## Task: Metric Types\\nIf you want to track the current amount of RAM your server is using, which metric type should you use?", "starterCode": "# Options: Counter, Gauge, Histogram\\nmetric_type = '___'", "solution": "# Options: Counter, Gauge, Histogram\\nmetric_type = 'Gauge'", "hint": "It can go up and down, so it's a Gauge.", "rubric": "Identifies Gauge."},
            {"title": "Health Checks", "theory": "## Liveness vs Readiness\\nIn orchestrated environments (like Kubernetes), a 'Liveness' probe checks if the app has crashed (restarts it if failing). A 'Readiness' probe checks if the app is ready to receive traffic (stops sending traffic if failing, e.g., during DB disconnects).", "instructions": "## Task: Probe Purpose\\nIf your API is running but the Database connection drops, which probe should fail so that the load balancer temporarily stops sending traffic?", "starterCode": "# Options: Liveness Probe, Readiness Probe\\nprobe = '___'", "solution": "# Options: Liveness Probe, Readiness Probe\\nprobe = 'Readiness Probe'", "hint": "Readiness Probe", "rubric": "Identifies Readiness Probe."},
            {"title": "Alerting Strategies", "theory": "## Symptom-Based Alerting\\nDon't alert when CPU hits 80%. Alert when the 99th percentile response time exceeds 2 seconds, or when the error rate exceeds 1%. Alert on *symptoms* that affect the user, not *causes*.", "instructions": "## Task: Alert Focus\\nAccording to best practices, should you page an engineer at 3 AM because 'Database CPU is at 95%' or because 'User checkout is failing'?", "starterCode": "# Options: Database CPU, User checkout is failing\\npage_for = '___'", "solution": "# Options: Database CPU, User checkout is failing\\npage_for = 'User checkout is failing'", "hint": "User checkout is failing", "rubric": "Identifies User checkout is failing."},
            {"title": "Log Aggregation", "theory": "## The ELK Stack\\nIn distributed systems, logs are scattered across many servers. Log aggregators (like Elasticsearch, Logstash, Kibana or Datadog) ingest all logs into a central searchable database.", "instructions": "## Task: ELK Acronym\\nIn the popular open-source ELK stack, 'L' stands for Logstash, and 'K' stands for Kibana. What does the 'E' stand for?", "starterCode": "e_stands_for = '___'", "solution": "e_stands_for = 'Elasticsearch'", "hint": "Elasticsearch", "rubric": "Identifies Elasticsearch."},
            {"title": "Handling Outages", "theory": "## Incident Response\\nWhen a massive outage occurs, the primary goal is *mitigation* (stopping the bleeding), not *resolution* (fixing the root cause). After the incident, a blameless post-mortem is written to prevent it from happening again.", "instructions": "## Task: The Review\\nWhat is the industry term for the document written after an outage to analyze what went wrong without pointing fingers?", "starterCode": "term = 'Blameless ___-___'", "solution": "term = 'Blameless Post-Mortem'", "hint": "Post-Mortem", "rubric": "Identifies Post-Mortem or Postmortem."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'backend.json')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        for new_course_name, course_info in NEW_COURSES_BATCH60.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH60.items():
            tier = course_info["tier"]
            if "Backend" in index_data and tier in index_data["Backend"]:
                if new_course_name not in index_data["Backend"][tier]:
                    index_data["Backend"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 60: Added {total} lessons to Backend track')
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
