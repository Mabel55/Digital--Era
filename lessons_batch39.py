"""
Batch 39: Expanding Cloud & DevOps Curriculum (Bash, Terraform, GitHub Actions, Prometheus, SRE)
"""
import json, os

NEW_COURSES_BATCH39 = {
    "Bash Scripting Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess Bash scripting fundamentals",
        "lessons": [
            {"title": "The Shebang", "theory": "## Defining the Interpreter\\nThe first line of a bash script is called a shebang (`#!`). It tells the operating system which interpreter to use to parse the rest of the file.", "instructions": "## Task: Add a Shebang\\nWrite the correct shebang for a bash script.", "starterCode": "___/bin/___\\n\\necho \"Hello World\"", "solution": "#!/bin/bash\\n\\necho \"Hello World\"", "hint": "Use #! and bash", "rubric": "Correctly defines the #!/bin/bash shebang."},
            {"title": "Variables and Arguments", "theory": "## Passing Data\\nIn a bash script, you can define variables without spaces around the equals sign, and access command-line arguments using `$1`, `$2`, etc.", "instructions": "## Task: Greeting Script\\nAssign the first command line argument to a variable named `USER_NAME` and print it.", "starterCode": "#!/bin/bash\\n\\n___=$1\\necho \"Welcome, $___!\"", "solution": "#!/bin/bash\\n\\nUSER_NAME=$1\\necho \"Welcome, $USER_NAME!\"", "hint": "USER_NAME", "rubric": "Correctly assigns and references the variable."}
        ]
    },
    "Terraform Fundamentals": {
        "tier": "Intermediate",
        "aiRubric": "Assess Infrastructure as Code concepts",
        "lessons": [
            {"title": "Providers and Resources", "theory": "## Declarative Infrastructure\\nTerraform uses blocks to define infrastructure. The `provider` block configures the API connection, and the `resource` block defines the actual infrastructure object (like an EC2 instance).", "instructions": "## Task: Define an AWS Instance\\nComplete the resource block to create an AWS EC2 instance named 'web'.", "starterCode": "___ \"aws_instance\" \"___\" {\\n  ami           = \"ami-0ff8a91507f77f867\"\\n  instance_type = \"t2.micro\"\\n}", "solution": "resource \"aws_instance\" \"web\" {\\n  ami           = \"ami-0ff8a91507f77f867\"\\n  instance_type = \"t2.micro\"\\n}", "hint": "Use resource and web", "rubric": "Correctly uses the resource block and names it web."},
            {"title": "State Files", "theory": "## The Source of Truth\\nTerraform creates a `.tfstate` file to map your configuration to the real-world resources. You should *never* modify this file manually or commit it to a public repo if it contains secrets.", "instructions": "## Task: Terraform Apply\\nWrite the command that reads the configuration, compares it against the state, and creates the infrastructure.", "starterCode": "terraform ___", "solution": "terraform apply", "hint": "Use apply", "rubric": "Correctly writes the terraform apply command."}
        ]
    },
    "GitHub Actions": {
        "tier": "Intermediate",
        "aiRubric": "Assess CI/CD pipelines",
        "lessons": [
            {"title": "Workflow Triggers", "theory": "## YAML Pipelines\\nGitHub Actions workflows are defined in YAML. The `on` key determines what events trigger the pipeline to run (e.g., a push to the main branch).", "instructions": "## Task: Push Trigger\\nConfigure the workflow to trigger on a `push` to the `main` branch.", "starterCode": "name: CI\\n___:\\n  push:\\n    branches:\\n      - ___", "solution": "name: CI\\non:\\n  push:\\n    branches:\\n      - main", "hint": "Use on and main", "rubric": "Correctly configures the trigger using 'on' and 'main'."},
            {"title": "Jobs and Steps", "theory": "## Executing Tasks\\nA workflow consists of one or more `jobs` that run in parallel by default. Each job contains a sequence of `steps` (running scripts or pre-built actions).", "instructions": "## Task: Checkout Code\\nUse the standard GitHub action `actions/checkout@v3` to checkout your repository code.", "starterCode": "jobs:\\n  build:\\n    runs-on: ubuntu-latest\\n    steps:\\n      - name: Checkout Repo\\n        ___: ___", "solution": "jobs:\\n  build:\\n    runs-on: ubuntu-latest\\n    steps:\\n      - name: Checkout Repo\\n        uses: actions/checkout@v3", "hint": "Use 'uses' and 'actions/checkout@v3'", "rubric": "Correctly references the checkout action."}
        ]
    },
    "Prometheus & Grafana": {
        "tier": "Advanced",
        "aiRubric": "Assess observability stacks",
        "lessons": [
            {"title": "Metrics Exporters", "theory": "## Scraping Targets\\nPrometheus operates on a pull model. Applications expose a `/metrics` HTTP endpoint, and Prometheus periodically scrapes it.", "instructions": "## Task: Node Exporter Config\\nConfigure a Prometheus scrape job to pull metrics from a Node Exporter running on port 9100.", "starterCode": "scrape_configs:\\n  - job_name: 'node'\\n    static_configs:\\n      - targets: ['localhost:___']", "solution": "scrape_configs:\\n  - job_name: 'node'\\n    static_configs:\\n      - targets: ['localhost:9100']", "hint": "Port 9100", "rubric": "Correctly sets the port to 9100."},
            {"title": "PromQL Basics", "theory": "## Querying Metrics\\nPrometheus Query Language (PromQL) allows you to aggregate and filter time-series data. This is what you write in Grafana to create dashboards.", "instructions": "## Task: Calculate Error Rate\\nWrite a PromQL query to get the per-second rate of HTTP 500 errors over the last 5 minutes.", "starterCode": "___(http_requests_total{status=\"___\"}[___])", "solution": "rate(http_requests_total{status=\"500\"}[5m])", "hint": "Use rate, 500, and 5m", "rubric": "Correctly writes the PromQL rate query."}
        ]
    },
    "Site Reliability Engineering (SRE)": {
        "tier": "Advanced",
        "aiRubric": "Assess SRE practices",
        "lessons": [
            {"title": "SLAs, SLOs, and SLIs", "theory": "## Measuring Reliability\\nAn **SLI** (Indicator) is the actual measurement (e.g. 99.9% uptime). An **SLO** (Objective) is the internal goal (e.g. 99.99%). An **SLA** (Agreement) is the legal contract with customers if you miss the SLO.", "instructions": "## Task: Define SLI\\nWrite a basic formula to calculate the SLI for system availability.", "starterCode": "SLI = (___ / Total Requests) * 100", "solution": "SLI = (Successful Requests / Total Requests) * 100", "hint": "Successful Requests", "rubric": "Defines SLI using Successful Requests."},
            {"title": "Error Budgets", "theory": "## Balancing Speed and Stability\\nAn Error Budget is 100% minus your SLO. If your SLO is 99.9%, your Error Budget is 0.1%. While you have budget remaining, you can push new features rapidly. If it's depleted, you must halt features and focus on reliability.", "instructions": "## Task: Calculate Budget\\nIf the Monthly SLO for availability is 99%, how much downtime (in hours) is allowed in a 720-hour month?", "starterCode": "Allowed Downtime = 720 * ___", "solution": "Allowed Downtime = 720 * 0.01", "hint": "Multiply by 0.01 (which is 1%)", "rubric": "Correctly calculates the error budget multiplier."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'cloud_devops.json')
    
    # 1. Update cloud_devops.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH39.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH39.items():
            tier = course_info["tier"]
            if "Cloud & DevOps" in index_data and tier in index_data["Cloud & DevOps"]:
                if new_course_name not in index_data["Cloud & DevOps"][tier]:
                    index_data["Cloud & DevOps"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 39: Added {total} lessons to Cloud & DevOps track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
