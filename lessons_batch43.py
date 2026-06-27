"""
Batch 43: Expanding Data Engineering & MLOps Curriculum (Data Quality, dbt, Data Lakes, Model Drift, Kubeflow)
"""
import json, os

NEW_COURSES_BATCH43 = {
    "Data Quality & Validation": {
        "tier": "Beginner",
        "aiRubric": "Assess data quality checks",
        "lessons": [
            {"title": "Missing Data", "theory": "## The Bane of Data Science\\nReal-world data is messy. You must check for missing values (NaN/Null) before building pipelines.", "instructions": "## Task: Detect Nulls\\nUse pandas to count the number of missing values in each column of a DataFrame.", "starterCode": "import pandas as pd\\n\\ndf = pd.DataFrame({'A': [1, None], 'B': [3, 4]})\\nmissing_counts = df.___().sum()", "solution": "import pandas as pd\\n\\ndf = pd.DataFrame({'A': [1, None], 'B': [3, 4]})\\nmissing_counts = df.isnull().sum()", "hint": "Use isnull() or isna()", "rubric": "Correctly uses isnull() or isna()."},
            {"title": "Great Expectations", "theory": "## Assertions for Data\\nGreat Expectations is a Python library that allows you to define strict rules (expectations) for your data, much like unit tests for code.", "instructions": "## Task: Define Expectation\\nWrite the expectation that checks if the 'age' column values are between 18 and 99.", "starterCode": "import great_expectations as ge\\n\\ndf = ge.dataset.PandasDataset({'age': [25, 40, 17]})\\nresult = df.expect_column_values_to_be_between('___', min_value=___, max_value=___)", "solution": "import great_expectations as ge\\n\\ndf = ge.dataset.PandasDataset({'age': [25, 40, 17]})\\nresult = df.expect_column_values_to_be_between('age', min_value=18, max_value=99)", "hint": "Column is age, min 18, max 99", "rubric": "Correctly sets the column name and boundaries."}
        ]
    },
    "dbt (Data Build Tool)": {
        "tier": "Intermediate",
        "aiRubric": "Assess dbt knowledge",
        "lessons": [
            {"title": "Transformations in SQL", "theory": "## The 'T' in ELT\\ndbt allows data analysts and engineers to transform data in their warehouse simply by writing SELECT statements. dbt handles the boilerplate DDL.", "instructions": "## Task: dbt Model\\nWrite a simple dbt model that selects all active users.", "starterCode": "-- models/active_users.sql\\nSELECT * \\nFROM {{ ref('___') }} \\nWHERE status = '___'", "solution": "-- models/active_users.sql\\nSELECT * \\nFROM {{ ref('users') }} \\nWHERE status = 'active'", "hint": "Ref 'users' and status 'active'", "rubric": "References the users table and active status."},
            {"title": "Testing Models", "theory": "## Data Integrity\\ndbt comes with built-in tests for `unique`, `not_null`, `accepted_values`, and `relationships`.", "instructions": "## Task: YAML Config\\nConfigure a dbt YAML file to enforce that the `id` column in `users` is unique and not null.", "starterCode": "version: 2\\nmodels:\\n  - name: users\\n    columns:\\n      - name: id\\n        tests:\\n          - ___\\n          - ___", "solution": "version: 2\\nmodels:\\n  - name: users\\n    columns:\\n      - name: id\\n        tests:\\n          - unique\\n          - not_null", "hint": "Use unique and not_null", "rubric": "Correctly defines unique and not_null tests."}
        ]
    },
    "Data Lakes & Warehouses": {
        "tier": "Intermediate",
        "aiRubric": "Assess cloud data architectures",
        "lessons": [
            {"title": "Schema on Read vs Write", "theory": "## Fundamental Differences\\nA Data Warehouse expects structured data and enforces a schema before writing (Schema on Write). A Data Lake accepts unstructured data, and structure is applied when querying (Schema on Read).", "instructions": "## Task: Identify Architecture\\nWhich system is best suited for storing petabytes of raw, unstructured log files and images?", "starterCode": "best_system = 'Data ___'", "solution": "best_system = 'Data Lake'", "hint": "Data Lake", "rubric": "Identifies Data Lake."},
            {"title": "Columnar Storage", "theory": "## Parquet & ORC\\nAnalytical databases and data lakes heavily use columnar formats like Parquet, which store data by columns rather than rows. This drastically speeds up aggregations.", "instructions": "## Task: Save as Parquet\\nUse pandas to save a DataFrame to a Parquet file.", "starterCode": "import pandas as pd\\n\\ndf = pd.DataFrame({'sales': [100, 200, 300]})\\ndf.to____('sales.parquet')", "solution": "import pandas as pd\\n\\ndf = pd.DataFrame({'sales': [100, 200, 300]})\\ndf.to_parquet('sales.parquet')", "hint": "Use to_parquet", "rubric": "Correctly uses to_parquet."}
        ]
    },
    "Model Monitoring & Drift": {
        "tier": "Advanced",
        "aiRubric": "Assess MLOps monitoring",
        "lessons": [
            {"title": "Data Drift", "theory": "## Changing Worlds\\nData Drift occurs when the statistical properties of the input features change over time in production, causing your model's accuracy to degrade.", "instructions": "## Task: Identify Drift Type\\nIf a model trained to predict housing prices in 2019 is now making predictions in 2024 (where inflation has changed the baseline), what kind of drift is this?", "starterCode": "# Options: Concept Drift, Data Drift\\ndrift_type = '___'", "solution": "# Options: Concept Drift, Data Drift\\ndrift_type = 'Data Drift'", "hint": "Data Drift", "rubric": "Identifies Data Drift."},
            {"title": "Evidently AI", "theory": "## Automated Detection\\nLibraries like Evidently calculate statistical distance metrics (like Wasserstein distance) between a reference dataset and current production data.", "instructions": "## Task: Report Generation\\nGenerate a data drift report using Evidently.", "starterCode": "from evidently.report import Report\\nfrom evidently.metric_preset import DataDriftPreset\\n\\nreport = Report(metrics=[___()])\\nreport.run(reference_data=ref_df, current_data=curr_df)", "solution": "from evidently.report import Report\\nfrom evidently.metric_preset import DataDriftPreset\\n\\nreport = Report(metrics=[DataDriftPreset()])\\nreport.run(reference_data=ref_df, current_data=curr_df)", "hint": "Use DataDriftPreset", "rubric": "Instantiates DataDriftPreset."}
        ]
    },
    "Kubeflow Pipelines": {
        "tier": "Advanced",
        "aiRubric": "Assess Kubeflow pipelines",
        "lessons": [
            {"title": "Containerized ML", "theory": "## Kubernetes Native\\nKubeflow Pipelines (KFP) is a platform for building and deploying scalable machine learning workflows on Kubernetes.", "instructions": "## Task: KFP Decorator\\nUse the KFP SDK decorator to define a python function as a pipeline component.", "starterCode": "from kfp import dsl\\n\\n@dsl.___\\ndef train_model(data: str) -> str:\\n    return 'model_path'", "solution": "from kfp import dsl\\n\\n@dsl.component\\ndef train_model(data: str) -> str:\\n    return 'model_path'", "hint": "Use @dsl.component", "rubric": "Correctly uses the component decorator."},
            {"title": "Pipeline Definition", "theory": "## Stitching Components\\nA Pipeline connects the outputs of one component to the inputs of another, creating a Directed Acyclic Graph (DAG).", "instructions": "## Task: Pass Data\\nPass the output of the `preprocess` component into the `train` component.", "starterCode": "@dsl.pipeline(name='my-pipeline')\\ndef my_pipeline():\\n    data_task = preprocess()\\n    train_task = train(data=data_task.___)", "solution": "@dsl.pipeline(name='my-pipeline')\\ndef my_pipeline():\\n    data_task = preprocess()\\n    train_task = train(data=data_task.output)", "hint": "Use .output", "rubric": "Accesses the output property."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'data_engineering_mlops.json')
    
    # 1. Update data_engineering_mlops.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH43.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH43.items():
            tier = course_info["tier"]
            if "Data Engineering & MLOps" in index_data and tier in index_data["Data Engineering & MLOps"]:
                if new_course_name not in index_data["Data Engineering & MLOps"][tier]:
                    index_data["Data Engineering & MLOps"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 43: Added {total} lessons to Data Engineering & MLOps track')
    # Use fix_newlines instead to build and clean!
    os.system('python fix_newlines.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
