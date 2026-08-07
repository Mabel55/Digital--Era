import json

with open("curriculum/tracks/data_engineering_mlops.json", "r", encoding="utf-8") as f:
    data = json.load(f)

theories = {
    "What is ETL?": """## Extract, Transform, Load — The Backbone of Data Engineering

**ETL** stands for **Extract, Transform, Load** — the three-step process that moves data from its raw source into a clean, usable format inside a data warehouse. It's the most fundamental concept in data engineering and powers every analytics dashboard, machine learning pipeline, and business intelligence report you've ever seen.

### The Three Steps

Think of ETL like cooking a meal from raw ingredients:

```
1. EXTRACT  (Go shopping)
   - Pull raw data from its source
   - Sources: APIs, databases, CSV files, log files, web scraping
   - The data is messy, duplicated, and in different formats

2. TRANSFORM  (Prep and cook)
   - Clean the data: remove nulls, fix formats, deduplicate
   - Enrich: add calculated fields, join with other datasets
   - Aggregate: sum by category, average by month
   - Standardize: dates to ISO format, currencies to USD

3. LOAD  (Serve the dish)
   - Write the clean, transformed data into a data warehouse
   - Destinations: Snowflake, BigQuery, Redshift, PostgreSQL
   - Data is now ready for analysts and dashboards
```

### A Real-World ETL Example

```python
# EXTRACT: Pull data from multiple sources
def extract():
    api_data = requests.get("https://api.store.com/orders").json()
    csv_data = pd.read_csv("customers.csv")
    db_data = pd.read_sql("SELECT * FROM products", connection)
    return api_data, csv_data, db_data

# TRANSFORM: Clean and merge the data
def transform(orders, customers, products):
    # Remove rows with missing values
    orders = orders.dropna(subset=["customer_id", "amount"])
    
    # Convert dates to standard format
    orders["date"] = pd.to_datetime(orders["date"])
    
    # Join orders with customer names
    merged = orders.merge(customers, on="customer_id")
    
    # Calculate total spending per customer
    summary = merged.groupby("customer_name")["amount"].sum().reset_index()
    
    return summary

# LOAD: Save to the data warehouse
def load(clean_data):
    clean_data.to_sql("customer_spending", warehouse_engine, if_exists="replace")
    print(f"Loaded {len(clean_data)} rows to warehouse.")

# Run the pipeline
raw_orders, raw_customers, raw_products = extract()
clean_data = transform(raw_orders, raw_customers, raw_products)
load(clean_data)
```

### ETL vs ELT

Modern cloud warehouses have led to a shift:

| Approach | Process | When to Use |
|---|---|---|
| **ETL** | Extract → Transform → Load | When compute is expensive; transform before loading |
| **ELT** | Extract → Load → Transform | When your warehouse is powerful (BigQuery, Snowflake); load raw data first, transform inside the warehouse using SQL |

ELT is becoming dominant because cloud warehouses can handle massive transformations cheaply. Tools like **dbt** make the "T" step easy by letting you write transformations as SQL SELECT statements.

### Common ETL Tools

| Tool | Type | Description |
|---|---|---|
| **Apache Airflow** | Orchestrator | Schedules and monitors ETL jobs |
| **dbt** | Transform only | SQL-based transformations inside the warehouse |
| **Fivetran/Airbyte** | Extract + Load | Connectors that sync data from 300+ sources |
| **Apache Spark** | Transform (big data) | Distributed processing for massive datasets |""",

    "OLTP vs OLAP": """## Two Worlds of Databases — Transactions vs Analytics

In data engineering, you'll encounter two fundamentally different types of database systems: **OLTP** (Online Transaction Processing) and **OLAP** (Online Analytical Processing). Understanding the difference is critical because they serve completely different purposes, are optimized for different workloads, and you should never try to use one for the other's job.

### OLTP — The Transaction Engine

**OLTP databases** are designed for fast, small, individual transactions. Every time someone signs up, places an order, or updates their profile, that's a transaction hitting an OLTP database.

```
OLTP Examples:
  INSERT INTO orders (user_id, product, amount) VALUES (42, 'Laptop', 999)
  UPDATE users SET email = 'new@email.com' WHERE id = 42
  SELECT * FROM users WHERE id = 42
  
  Each query touches 1-10 rows. Needs to complete in < 50ms.
  Thousands of these per second.
```

**Examples:** PostgreSQL, MySQL, MongoDB, DynamoDB

### OLAP — The Analytics Engine

**OLAP databases** (Data Warehouses) are designed for complex analytical queries that scan millions or billions of rows to produce aggregate results. Analysts and dashboards query OLAP systems.

```
OLAP Examples:
  SELECT region, SUM(revenue) FROM sales 
  WHERE date BETWEEN '2023-01-01' AND '2024-01-01'
  GROUP BY region
  
  This query scans 50 million rows. Takes 5-30 seconds. That's fine!
  Only a few of these queries per minute.
```

**Examples:** Snowflake, Google BigQuery, Amazon Redshift, ClickHouse

### Key Differences

| Feature | OLTP | OLAP |
|---|---|---|
| **Purpose** | Run the business | Analyze the business |
| **Query type** | Simple CRUD (insert, update, delete) | Complex aggregations (SUM, AVG, GROUP BY) |
| **Rows per query** | 1-100 | Millions to billions |
| **Response time** | Milliseconds | Seconds to minutes |
| **Users** | App users, APIs | Analysts, dashboards |
| **Data format** | Row-oriented (fast writes) | Column-oriented (fast reads) |
| **Schema** | Normalized (3NF) | Denormalized (star/snowflake schema) |
| **Data freshness** | Real-time | Near real-time to daily |
| **Examples** | PostgreSQL, MySQL | Snowflake, BigQuery |

### The Data Pipeline: OLTP → ETL → OLAP

```
┌──────────────┐     ETL Pipeline      ┌──────────────┐
│   OLTP       │ ───────────────────→  │   OLAP       │
│  (PostgreSQL)│  Extract, Transform,  │  (Snowflake) │
│              │  Load nightly or      │              │
│ Users table  │  every 15 minutes     │ Fact tables  │
│ Orders table │                       │ Dim tables   │
│ Products     │                       │ Aggregates   │
└──────────────┘                       └──────────────┘
       ↑                                      ↑
  App writes here                    Analysts query here
  (fast transactions)               (complex analytics)
```

### Why You Can't Use One For Both

Running heavy analytics on your OLTP database will **slow down your application** — your users will experience lag while an analyst's 50-million-row query is running. Running transactional workloads on your OLAP warehouse is wasteful and slow because column-oriented storage isn't optimized for single-row lookups. Keep them separate!""",

    "Big Data Processing": """## Apache Spark — Distributed Computing at Scale

When your data grows beyond what a single machine can handle — think billions of rows, terabytes of data — you need **Apache Spark**. Spark is a distributed computing engine that splits your data across a cluster of machines and processes it **in parallel**, making it possible to analyze datasets that would take hours on a single machine in just minutes.

### Why Not Just Use Pandas?

```
Pandas (single machine):
  - Loads ALL data into RAM on ONE computer
  - Your laptop has 16GB RAM
  - Your dataset is 500GB
  - Result: MemoryError! 💥

Apache Spark (distributed cluster):
  - Splits 500GB across 50 machines (10GB each)
  - Each machine processes its chunk in parallel
  - Results are combined automatically
  - Runs in minutes, not hours
```

### How Spark Distributes Work

```
┌─────────────────────────────────────────────────┐
│                DRIVER (your code)                │
│   spark.read.csv("500GB_file.csv")              │
│        .filter(col("age") > 25)                 │
│        .groupBy("city").count()                  │
└───────────┬──────────┬──────────┬───────────────┘
            │          │          │
     ┌──────▼──┐ ┌─────▼──┐ ┌────▼───┐
     │ Worker 1│ │Worker 2│ │Worker 3│
     │ 170GB   │ │ 170GB  │ │ 170GB  │
     │ Process │ │Process │ │Process │
     │ locally │ │locally │ │locally │
     └────┬────┘ └───┬────┘ └───┬────┘
          │          │          │
          └──────────┼──────────┘
                     │
              Combined Result
```

### The MapReduce Paradigm

Spark's processing model is based on **MapReduce** — a two-phase approach:

```python
# The MAP phase: Apply a function to every element independently
# (Can run in parallel — each machine handles its own chunk)
data = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x ** 2, data))
# [1, 4, 9, 16, 25]

# The REDUCE phase: Combine all results into a single value
# (Aggregates across machines)
from functools import reduce
result = reduce(lambda a, b: a + b, mapped)
# 55
```

### Spark vs Hadoop MapReduce

The predecessor to Spark was **Hadoop MapReduce**, which was revolutionary but painfully slow:

```
Hadoop MapReduce:
  Step 1: Read data from disk (HDFS)
  Step 2: Map (process) in memory
  Step 3: Write intermediate results to DISK  ← SLOW!
  Step 4: Read intermediate results from DISK  ← SLOW!
  Step 5: Reduce (aggregate)
  Step 6: Write final results to disk
  
  Every step involves disk I/O. For iterative ML algorithms
  that run 100+ iterations, this is catastrophically slow.

Apache Spark:
  Step 1: Read data from disk (or S3, HDFS, etc.)
  Step 2: Keep intermediate results IN MEMORY (RAM)  ← FAST!
  Step 3: Process everything in memory
  Step 4: Write only the final result to disk
  
  Up to 100x faster for iterative workloads!
```

### Spark APIs

| API | Level | Use Case |
|---|---|---|
| **RDDs** | Low-level | Fine-grained control, custom transformations |
| **DataFrames** | High-level | Structured data, SQL-like operations |
| **Spark SQL** | Highest | Write actual SQL queries on big data |
| **Spark MLlib** | ML-specific | Distributed machine learning algorithms |
| **Structured Streaming** | Real-time | Process streaming data with DataFrame API |

### PySpark Quick Start

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Read a massive CSV (distributed automatically)
df = spark.read.csv("s3://my-bucket/500GB_file.csv", header=True)

# Transformations (lazy — not executed yet!)
filtered = df.filter(df.age > 25)
grouped = filtered.groupBy("city").count()

# Action (triggers execution across the cluster!)
grouped.show()
```""",

    "Real-time Data Pipelines": """## Apache Kafka — Event Streaming at Scale

**Apache Kafka** is a distributed event streaming platform that enables real-time data pipelines. Instead of processing data in nightly batches ("Here's yesterday's orders"), Kafka processes events **as they happen** ("User just clicked checkout" — immediately sent to analytics, fraud detection, and inventory systems simultaneously).

### Batch Processing vs Stream Processing

```
Batch Processing (traditional):
  Orders from the day are collected
  → At midnight, an ETL job runs
  → Processes all orders at once
  → Dashboard updates the next morning
  
  Latency: 12-24 hours. You're always looking at yesterday's data.

Stream Processing (Kafka):
  Each order is published to Kafka THE INSTANT it happens
  → Multiple consumers read it in real-time
  → Dashboard updates within seconds
  → Fraud detection checks it immediately
  
  Latency: Milliseconds to seconds. Real-time visibility.
```

### Kafka Architecture

Kafka uses a **Publish/Subscribe** (Pub/Sub) model with three core concepts:

```
┌──────────────┐     publish      ┌──────────────────┐
│  Producers   │ ─────────────→  │   KAFKA TOPIC    │
│  (data       │                  │  "order-events"  │
│   sources)   │                  │                  │
│              │                  │  [event1]        │
│ - Web app    │                  │  [event2]        │
│ - Mobile app │                  │  [event3]        │
│ - IoT sensor │                  │  [event4]        │
└──────────────┘                  └────────┬─────────┘
                                           │
                              subscribe    │    subscribe
                          ┌────────────────┼────────────────┐
                          │                │                │
                   ┌──────▼──────┐  ┌──────▼──────┐  ┌─────▼───────┐
                   │ Consumer 1  │  │ Consumer 2  │  │ Consumer 3  │
                   │ Analytics   │  │ Fraud Det.  │  │ Inventory   │
                   │ Dashboard   │  │ Service     │  │ Service     │
                   └─────────────┘  └─────────────┘  └─────────────┘
```

### Key Concepts

| Concept | Description |
|---|---|
| **Producer** | Application that publishes events to a topic |
| **Consumer** | Application that reads events from a topic |
| **Topic** | A named channel/category for events (like "orders", "clicks") |
| **Partition** | Topics are split into partitions for parallelism |
| **Consumer Group** | Multiple consumers sharing the work of reading a topic |
| **Offset** | The position of a consumer in the topic (like a bookmark) |

### Why Kafka, Not Just a Database?

```python
# The naive approach: Write to database, then read from it
# Problem: Only ONE system reads. If you add fraud detection,
# you need to query the same database again. Doesn't scale.

db.insert(order)
analytics.query(db)        # Reads from DB
fraud.query(db)            # Also reads from DB (competing!)
inventory.query(db)        # Also reads from DB (slow!)

# The Kafka approach: Publish once, multiple consumers read independently
kafka.publish("orders", order)

# Each consumer reads at its own pace, independently:
# Analytics consumer → reads and aggregates
# Fraud consumer → reads and checks patterns  
# Inventory consumer → reads and updates stock
# They DON'T compete with each other!
```

### Real-World Kafka Use Cases

| Company | Use Case |
|---|---|
| **Netflix** | Real-time viewing analytics, recommendations |
| **Uber** | Live trip tracking, surge pricing calculations |
| **LinkedIn** | Activity feed, real-time notifications |
| **Spotify** | Song play tracking, real-time charts |

Kafka processes **trillions of events per day** at companies like LinkedIn and Netflix. It's the backbone of any modern real-time data architecture.""",

    "Experiment Tracking": """## Never Lose a Good Model — ML Experiment Tracking

When training machine learning models, you'll run **hundreds of experiments** — tweaking hyperparameters, trying different features, testing various algorithms. Without tracking, you'll inevitably forget which combination of settings produced your best result. **Experiment tracking** solves this by automatically logging every detail of every run.

### The Problem Without Tracking

```
Monday:   Trained model with lr=0.01, depth=5     → accuracy 0.82
Tuesday:  Trained model with lr=0.001, depth=10   → accuracy 0.91 ← Best!
Wednesday: Trained model with lr=0.005, depth=8   → accuracy 0.87
Thursday: "Wait, what settings did I use on Tuesday? 
           Which preprocessing did I apply? 
           Which dataset version did I use??"
           
           → Lost. You can't reproduce your best model. 😱
```

### What Gets Tracked

Experiment trackers like **MLflow**, **Weights & Biases (W&B)**, and **Neptune** log three categories:

```
1. PARAMETERS (inputs — what you configured)
   - learning_rate: 0.001
   - max_depth: 10
   - batch_size: 32
   - model_type: "random_forest"
   - preprocessing: "standard_scaler"

2. METRICS (outputs — how the model performed)
   - accuracy: 0.91
   - precision: 0.89
   - recall: 0.93
   - f1_score: 0.91
   - training_time: 45.2 seconds

3. ARTIFACTS (files — the actual model and data)
   - model.pkl (the trained model file)
   - confusion_matrix.png
   - feature_importance.csv
   - requirements.txt
```

### MLflow — The Most Popular Tracker

```python
import mlflow

# Start tracking an experiment
mlflow.set_experiment("customer_churn_prediction")

with mlflow.start_run(run_name="random_forest_v3"):
    # Log parameters (the settings you chose)
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("n_estimators", 100)
    
    # Train the model
    model = RandomForestClassifier(
        max_depth=10, n_estimators=100
    )
    model.fit(X_train, y_train)
    
    # Log metrics (the results)
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1_score(y_test, predictions))
    
    # Log the model artifact (save the actual model)
    mlflow.sklearn.log_model(model, "model")
    
    # Log any file as an artifact
    mlflow.log_artifact("confusion_matrix.png")
```

### Comparing Runs

The real power is comparing experiments side by side:

```
┌──────────────┬──────────┬──────────┬──────────┐
│  Run Name    │ LR       │ Depth    │ Accuracy │
├──────────────┼──────────┼──────────┼──────────┤
│  Run_1       │ 0.1      │ 5        │ 0.82     │
│  Run_2 ★     │ 0.001    │ 10       │ 0.91     │ ← Best!
│  Run_3       │ 0.01     │ 8        │ 0.87     │
│  Run_4       │ 0.0001   │ 15       │ 0.85     │
│  Run_5       │ 0.001    │ 12       │ 0.90     │
└──────────────┴──────────┴──────────┴──────────┘

Now you can instantly see: lr=0.001 + depth=10 was the winner.
You can reproduce it exactly.
```

### Experiment Tracking Tools

| Tool | Strengths | Hosting |
|---|---|---|
| **MLflow** | Open-source, broad ML framework support | Self-hosted or Databricks |
| **Weights & Biases** | Beautiful UI, team collaboration, sweeps | Cloud-hosted |
| **Neptune** | Enterprise-ready, great for large teams | Cloud-hosted |
| **TensorBoard** | Deep learning visualizations, free | Local |
| **Comet ML** | Code diffing, reproducibility | Cloud-hosted |""",

    "Serving ML Models": """## From Jupyter Notebook to Production — Deploying ML Models

Training a model in a Jupyter Notebook is the easy part. **Deploying** it so that real users can get predictions — reliably, at scale, with low latency — is where data engineering meets software engineering. This is the bridge between data science and production systems.

### The Deployment Gap

```
Data Scientist's world:
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)
  print(f"Accuracy: {accuracy_score(y_test, predictions)}")
  # "My model is 95% accurate! Ship it!"

Production reality:
  - How do 10,000 users call this model simultaneously?
  - What happens if the model crashes?
  - How do you update the model without downtime?
  - How do you monitor if the model is still accurate?
  - What if the input data format changes?
```

### Three Ways to Deploy

**1. Batch Inference — Run on a Schedule**

```python
# Every night at midnight:
# 1. Load new data from the database
new_data = pd.read_sql("SELECT * FROM users WHERE needs_prediction", db)

# 2. Run predictions
predictions = model.predict(new_data)

# 3. Save results back to the database
new_data["prediction"] = predictions
new_data.to_sql("predictions_table", db, if_exists="replace")

# Users see predictions when they open the app in the morning.
# Latency: hours (but cheap and simple)
```

**Best for:** Recommendation engines, risk scores, email campaigns

**2. Real-time API — Respond Instantly**

```python
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
async def predict(data: dict):
    # Validate input
    if "feature_x" not in data:
        return {"error": "Missing feature_x"}, 400
    
    # Run prediction
    features = [[data["feature_x"], data.get("feature_y", 0)]]
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max()
    
    return {
        "prediction": int(prediction),
        "confidence": float(probability),
        "model_version": "v2.3.1"
    }
```

```
Client sends: POST /predict {"feature_x": 42, "feature_y": 7}
Server returns: {"prediction": 1, "confidence": 0.94, "model_version": "v2.3.1"}
Latency: 20-100ms
```

**Best for:** Fraud detection, pricing, search ranking

**3. Edge Deployment — On the User's Device**

```
Convert model to a lightweight format:
  PyTorch → ONNX → CoreML (iOS) or TFLite (Android)

The model runs entirely on the user's phone.
No internet needed. Zero latency. Maximum privacy.
```

**Best for:** Photo filters, voice assistants, keyboard predictions

### Production Deployment Checklist

| Concern | Solution |
|---|---|
| **Scaling** | Container orchestration (Docker + Kubernetes) |
| **Reliability** | Health checks, auto-restart, load balancing |
| **Versioning** | Model registry (MLflow), A/B testing |
| **Monitoring** | Track prediction latency, error rates, accuracy |
| **Security** | Input validation, rate limiting, authentication |
| **Rollback** | Keep previous model versions, instant rollback |

### The Model Serving Stack

```
Client Request → API Gateway → Load Balancer
    → Container 1 (model v2.3)
    → Container 2 (model v2.3)
    → Container 3 (model v2.3)
    → Response back to client

If v2.3 has a bug → instant rollback to v2.2
If traffic spikes → auto-scale to 10 containers
```""",

    "Missing Data": """## The Bane of Data Science — Detecting and Handling Missing Values

Real-world data is almost never complete. Sensors fail, users skip form fields, APIs return partial responses, and databases have gaps. **Missing data** (represented as `NaN`, `None`, or `NULL`) is the most common data quality issue you'll face, and how you handle it can make or break your analysis and models.

### Why Data Goes Missing

```
Reasons for missing data:
  - User skipped a field:     email = NaN
  - Sensor malfunction:       temperature = NaN for 3 hours
  - API returned partial:     {"name": "Alice", "age": null}
  - Database migration bug:   1000 rows lost the 'city' column
  - Feature didn't exist yet: new column added last month, old rows are NaN
```

### Detecting Missing Data in Pandas

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'Diana'],
    'Age': [25, np.nan, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', None],
    'Score': [95, 82, np.nan, np.nan]
})

# Check for missing values (returns True/False for every cell)
print(df.isnull())
#     Name    Age   City  Score
# 0  False  False  False  False
# 1  False   True  False  False
# 2   True  False  False   True
# 3  False  False   True   True

# Count missing values per column
print(df.isnull().sum())
# Name     1
# Age      1
# City     1
# Score    2

# Percentage missing per column
print((df.isnull().sum() / len(df) * 100).round(1))
# Name     25.0%
# Age      25.0%
# City     25.0%
# Score    50.0%

# Total missing values in the entire DataFrame
print(df.isnull().sum().sum())  # 5
```

### Strategies for Handling Missing Data

| Strategy | When to Use | Risk |
|---|---|---|
| **Drop rows** | Few missing values, large dataset | Lose data |
| **Drop columns** | Column is >50% missing | Lose a feature entirely |
| **Fill with mean/median** | Numerical columns, random missingness | Reduces variance |
| **Fill with mode** | Categorical columns | Over-represents one category |
| **Forward/backward fill** | Time series data | Assumes continuity |
| **Interpolation** | Smooth time series data | Assumes linear change |
| **Flag + fill** | Missingness itself is informative | Adds a column |

```python
# Drop rows with ANY missing value
df_clean = df.dropna()

# Drop rows only if a specific column is missing
df_clean = df.dropna(subset=['Name', 'Age'])

# Fill numeric columns with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill categorical columns with the most common value
df['City'] = df['City'].fillna(df['City'].mode()[0])

# Forward fill (for time series: use previous value)
df['Score'] = df['Score'].fillna(method='ffill')

# Create a flag column (missingness might be meaningful!)
df['Score_was_missing'] = df['Score'].isnull().astype(int)
df['Score'] = df['Score'].fillna(0)
```

### The Golden Rule

Before handling missing data, always ask **why** it's missing. Data that's missing at random (sensor glitch) should be handled differently from data that's missing systematically (users deliberately skipping income fields). The strategy you choose directly impacts your model's accuracy and fairness.""",

    "Great Expectations": """## Unit Tests for Data — Validating Data Quality with Great Expectations

**Great Expectations** is a Python library that lets you define strict rules (called **expectations**) for your data — exactly like unit tests for code, but for data. Just as you write `assert result == 42` for code, you can write `expect_column_values_to_be_between('age', 0, 120)` for data. When data violates an expectation, the pipeline alerts you before bad data contaminates your analytics.

### Why You Need Data Validation

```
Without data validation:
  1. A vendor sends a CSV with negative ages (-5, -10)
  2. Your ETL pipeline loads it into the warehouse
  3. Your ML model trains on this corrupted data
  4. Your model now predicts nonsense
  5. You notice the problem... 3 weeks later 😱

With Great Expectations:
  1. A vendor sends a CSV with negative ages
  2. Great Expectations catches it IMMEDIATELY:
     "FAILED: expect_column_values_to_be_between('age', 0, 120)"
  3. Pipeline halts. Alert sent. Bad data never enters the warehouse.
```

### Core Concepts

| Concept | Description |
|---|---|
| **Expectation** | A single assertion about your data ("age must be between 0-120") |
| **Expectation Suite** | A collection of expectations for one dataset |
| **Validation Result** | Pass/fail results of running expectations against data |
| **Data Docs** | Auto-generated HTML reports showing validation results |
| **Checkpoint** | An executable validation job you can schedule |

### Using Great Expectations

```python
import great_expectations as ge

# Wrap a pandas DataFrame
df = ge.dataset.PandasDataset({
    'name': ['Alice', 'Bob', 'Charlie', ''],
    'age': [25, 40, 17, 150],
    'email': ['a@test.com', 'b@test.com', None, 'd@test.com']
})

# Define expectations (each one is an assertion)
# Check that age is between 18 and 99
result = df.expect_column_values_to_be_between(
    'age', min_value=18, max_value=99
)
print(result["success"])  # False! (17 and 150 are out of range)

# Check that no names are empty strings
result = df.expect_column_values_to_not_be_null('name')
# Passes — None values are null, empty strings are NOT null

# Check that emails match a pattern
result = df.expect_column_values_to_match_regex(
    'email', r'^[\\w]+@[\\w]+\\.com$'
)

# Check that age column exists
result = df.expect_column_to_exist('age')

# Check uniqueness
result = df.expect_column_values_to_be_unique('email')
```

### Built-in Expectations

Great Expectations comes with 300+ built-in expectations:

```python
# Column-level expectations
df.expect_column_to_exist('column_name')
df.expect_column_values_to_not_be_null('column_name')
df.expect_column_values_to_be_unique('column_name')
df.expect_column_values_to_be_between('age', 0, 120)
df.expect_column_values_to_be_in_set('status', ['active', 'inactive'])
df.expect_column_values_to_match_regex('email', r'.+@.+')

# Table-level expectations
df.expect_table_row_count_to_be_between(min_value=100, max_value=10000)
df.expect_table_columns_to_match_ordered_list(['id', 'name', 'age'])
```

### Integrating into ETL Pipelines

```python
# In your Airflow DAG:
def validate_data(df):
    ge_df = ge.dataset.PandasDataset(df)
    
    ge_df.expect_column_values_to_not_be_null('user_id')
    ge_df.expect_column_values_to_be_between('amount', 0, 100000)
    ge_df.expect_column_values_to_be_in_set('currency', ['USD', 'EUR', 'GBP'])
    
    results = ge_df.validate()
    
    if not results["success"]:
        raise ValueError("Data validation FAILED! Check Data Docs.")
    
    return df  # Only passes if ALL expectations pass

# extract → validate → transform → load
raw_data = extract()
validated_data = validate_data(raw_data)  # Stops here if bad!
clean_data = transform(validated_data)
load(clean_data)
```

Data validation is the **immune system** of your data pipeline — it catches infections (bad data) before they spread to the rest of your system.""",

    "Transformations in SQL": """## dbt — The 'T' in ELT, Powered by SQL

**dbt (Data Build Tool)** revolutionized data engineering by letting analysts and engineers define data transformations using nothing but SQL SELECT statements. Instead of writing complex Python ETL scripts, you write a SQL query that describes the output you want, and dbt handles creating the table, managing dependencies, and running tests. It's the standard tool for the "Transform" step in modern ELT architectures.

### Why dbt Changed Everything

```
Before dbt (traditional ETL):
  - Write Python scripts to extract, transform, and load
  - Manage table creation DDL manually (CREATE TABLE, ALTER TABLE)
  - Handle dependencies between transformations yourself
  - No version control, no testing, no documentation
  
After dbt (modern ELT):
  - Load raw data into the warehouse first (Fivetran, Airbyte)
  - Write a SQL SELECT statement describing your transformation
  - dbt creates the table for you
  - Dependencies are automatic ({{ ref('other_model') }})
  - Built-in testing, documentation, version control with Git
```

### dbt Models — Just SQL Files

A dbt "model" is simply a `.sql` file containing a SELECT statement:

```sql
-- models/active_users.sql
-- This creates a table/view called "active_users" in your warehouse

SELECT
    id,
    name,
    email,
    signup_date,
    last_login
FROM {{ ref('users') }}
WHERE status = 'active'
  AND last_login > CURRENT_DATE - INTERVAL '30 days'
```

When you run `dbt run`, dbt executes this SELECT and materializes the result as a table or view in your warehouse. The `{{ ref('users') }}` syntax tells dbt that this model depends on the `users` model — dbt will run `users` first, automatically.

### The ref() Function — Automatic Dependencies

```sql
-- models/staging/stg_orders.sql
SELECT * FROM {{ source('raw', 'orders') }}
WHERE order_date > '2023-01-01'

-- models/marts/monthly_revenue.sql
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_revenue
FROM {{ ref('stg_orders') }}   -- dbt knows to run stg_orders first!
GROUP BY 1

-- models/marts/revenue_growth.sql
SELECT
    month,
    total_revenue,
    LAG(total_revenue) OVER (ORDER BY month) AS prev_month,
    total_revenue - LAG(total_revenue) OVER (ORDER BY month) AS growth
FROM {{ ref('monthly_revenue') }}  -- runs monthly_revenue first!
```

dbt builds a **DAG (Directed Acyclic Graph)** from all the `ref()` calls, ensuring models run in the correct order.

### Materializations

dbt can materialize your model in different ways:

```yaml
# dbt_project.yml
models:
  my_project:
    staging:
      materialized: view      # Fast to build, always fresh
    marts:
      materialized: table     # Pre-computed, fast to query
    snapshots:
      materialized: incremental  # Only process new/changed rows
```

| Type | Description | When to Use |
|---|---|---|
| **View** | A saved SQL query (no data stored) | Staging models, small datasets |
| **Table** | A full copy of the data | Final analytics models, dashboards |
| **Incremental** | Only processes new rows since last run | Large tables, daily appends |
| **Ephemeral** | Inlined as a CTE, not materialized | Shared logic, intermediate calculations |

### dbt Commands

```bash
dbt run          # Run all models
dbt test         # Run all tests
dbt docs generate  # Generate documentation
dbt docs serve   # Serve docs website locally
dbt run --select monthly_revenue  # Run one model + dependencies
```""",

    "Testing Models": """## Data Quality Gates — Testing dbt Models

dbt comes with a powerful **testing framework** that lets you define assertions about your data — ensuring data integrity at every stage of your transformation pipeline. Just as software engineers write unit tests for code, data engineers write dbt tests for data. If a test fails, the pipeline stops, and you're alerted before bad data reaches your dashboards.

### Why Test Data?

```
Without tests:
  An ETL bug introduces duplicate user IDs into your users table.
  → Your revenue report counts some users twice.
  → The CEO sees $2M instead of $1M in revenue.
  → Bad business decisions follow.
  → You get a very uncomfortable phone call. 😬

With dbt tests:
  dbt test catches: "FAIL: Column 'id' in 'users' has duplicate values!"
  → Pipeline halts. Alert sent. Dashboard is safe.
```

### Built-in Generic Tests

dbt ships with four essential tests you can apply to any column using YAML:

```yaml
# models/schema.yml
version: 2

models:
  - name: users
    description: "All registered platform users"
    columns:
      - name: id
        description: "Unique user identifier"
        tests:
          - unique          # No duplicate IDs
          - not_null        # Every row must have an ID
      
      - name: email
        tests:
          - unique          # No duplicate emails
          - not_null
      
      - name: status
        tests:
          - accepted_values:
              values: ['active', 'inactive', 'banned']
              # Only these three values are allowed
      
      - name: company_id
        tests:
          - relationships:
              to: ref('companies')
              field: id
              # Every company_id must exist in the companies table
```

### The Four Built-in Tests

| Test | What It Checks | SQL Equivalent |
|---|---|---|
| **unique** | No duplicate values | `SELECT col, COUNT(*) HAVING COUNT(*) > 1` |
| **not_null** | No NULL values | `SELECT * WHERE col IS NULL` |
| **accepted_values** | Values in an allowed set | `SELECT * WHERE col NOT IN (...)` |
| **relationships** | Foreign key integrity | `SELECT * WHERE id NOT IN (SELECT id FROM other)` |

### Custom Tests (Singular Tests)

For complex validations, write a SQL query in the `tests/` directory. If the query returns **any rows**, the test fails:

```sql
-- tests/assert_no_negative_revenue.sql
-- This test FAILS if any row is returned

SELECT
    order_id,
    revenue
FROM {{ ref('orders') }}
WHERE revenue < 0
-- If any order has negative revenue, this returns rows → TEST FAILS
```

### Custom Generic Tests (Reusable)

```sql
-- macros/test_is_positive.sql
{% test is_positive(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} < 0
{% endtest %}
```

```yaml
# Now use it anywhere:
columns:
  - name: price
    tests:
      - is_positive   # Reusable across all models!
```

### Running Tests

```bash
# Run all tests
dbt test

# Run tests for a specific model
dbt test --select users

# Run tests and see details
dbt test --store-failures  # Failed rows saved to a table for debugging

# Output:
# Running 8 tests...
# PASS: unique_users_id
# PASS: not_null_users_id
# PASS: unique_users_email
# FAIL: accepted_values_users_status  ← FOUND invalid values!
# 7 of 8 tests passed. 1 FAILED.
```

The philosophy is simple: **test your data the way you test your code**. Every model should have at minimum `unique` and `not_null` tests on its primary key.""",

    "Schema on Read vs Write": """## Data Lakes vs Data Warehouses — Two Philosophies of Schema

When storing data at scale, there are two fundamentally different philosophies about **when to impose structure** (a schema) on your data. This choice affects storage costs, query speed, flexibility, and the types of data you can handle. Understanding this distinction is the key to choosing between a Data Lake and a Data Warehouse.

### Schema on Write (Data Warehouse)

A **Data Warehouse** requires you to define the schema **before** you write data. Every row must conform to the predefined columns, types, and constraints. If your data doesn't fit the schema, it's rejected.

```sql
-- Define the schema FIRST (before any data enters):
CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    amount      DECIMAL(10,2) NOT NULL,
    order_date  DATE NOT NULL,
    status      VARCHAR(20) CHECK (status IN ('pending','shipped','delivered'))
);

-- Only conforming data can be inserted:
INSERT INTO orders VALUES (1, 42, 99.99, '2024-01-15', 'shipped');  -- ✅

-- This FAILS because status 'cancelled' isn't in the allowed values:
INSERT INTO orders VALUES (2, 43, 50.00, '2024-01-16', 'cancelled'); -- ❌ REJECTED!
```

**Pros:** Fast queries, clean data, strong consistency
**Cons:** Rigid, can't store unstructured data, schema changes are painful

### Schema on Read (Data Lake)

A **Data Lake** accepts data in **any format** — CSV, JSON, Parquet, images, video, logs. There's no predefined schema. Structure is applied only when you query (read) the data.

```python
# Dump ANYTHING into the data lake:
s3.upload("raw/orders/2024-01-15.json")        # Semi-structured JSON
s3.upload("raw/logs/server.log")                # Unstructured text
s3.upload("raw/images/product_photos.zip")      # Binary files
s3.upload("raw/sensor_data/readings.parquet")   # Columnar data

# No schema enforced at write time. Everything goes in.

# Apply structure ONLY when reading:
df = spark.read.json("s3://datalake/raw/orders/2024-01-15.json")
# Now you define which fields to extract:
df.select("order_id", "amount", "status").show()
```

**Pros:** Flexible, stores anything, cheap storage (S3/GCS)
**Cons:** Queries are slower, data quality issues, "data swamp" risk

### Comparison

| Feature | Data Warehouse (Schema on Write) | Data Lake (Schema on Read) |
|---|---|---|
| **Schema defined** | Before writing | When reading/querying |
| **Data types** | Structured only | Structured + Semi-structured + Unstructured |
| **Storage format** | Rows/columns (proprietary) | Files (Parquet, JSON, CSV, images) |
| **Query speed** | Very fast (pre-optimized) | Slower (must parse at read time) |
| **Flexibility** | Rigid schema changes | Accept anything |
| **Cost** | Expensive (compute + storage) | Cheap storage (S3: $0.023/GB/month) |
| **Risk** | Over-engineering | Data swamp (messy, unusable data) |
| **Examples** | Snowflake, BigQuery, Redshift | S3 + Spark, Azure Data Lake, GCS |

### The Modern Hybrid: Data Lakehouse

The industry is converging on a **Lakehouse** architecture that combines the best of both:

```
Data Lakehouse = Data Lake storage + Data Warehouse performance

Tools: Delta Lake (Databricks), Apache Iceberg, Apache Hudi

- Store raw data as files (cheap, flexible)
- Add ACID transactions and schema enforcement on top
- Query with SQL at warehouse speed
- Best of both worlds!
```""",

    "Columnar Storage": """## Column-Oriented Storage — Why Parquet is King

Traditional databases store data **row by row** — each row's fields are stored together on disk. But analytical queries almost never need entire rows. They need a few columns from millions of rows (e.g., "sum of all revenue" scans only the revenue column). **Columnar storage formats** like Parquet and ORC store data **column by column**, making analytical queries dramatically faster.

### Row Storage vs Column Storage

```
Row-oriented storage (PostgreSQL, MySQL, CSV):
  Row 1: [Alice, 25, NYC, 95000]
  Row 2: [Bob,   30, LA,  85000]
  Row 3: [Carol, 28, NYC, 92000]
  
  To calculate SUM(salary), the database must read:
  [Alice, 25, NYC, 95000] ← reads 4 fields, needs only 1
  [Bob,   30, LA,  85000] ← reads 4 fields, needs only 1
  [Carol, 28, NYC, 92000] ← reads 4 fields, needs only 1
  → Reads 12 values, but only needs 3. 75% waste!

Column-oriented storage (Parquet, BigQuery):
  Name column:   [Alice, Bob, Carol]
  Age column:    [25, 30, 28]
  City column:   [NYC, LA, NYC]
  Salary column: [95000, 85000, 92000]
  
  To calculate SUM(salary), the database reads ONLY:
  [95000, 85000, 92000] ← reads exactly what it needs
  → Reads 3 values, needs 3. 0% waste!
```

### Why Columnar is Faster for Analytics

| Operation | Row Storage | Column Storage |
|---|---|---|
| `SELECT * FROM users WHERE id = 5` | Fast (reads one row) | Slow (must reconstruct row from columns) |
| `SELECT AVG(salary) FROM users` | Slow (reads all columns for every row) | Fast (reads only salary column) |
| `SELECT city, SUM(salary) GROUP BY city` | Slow | Very fast (reads only 2 columns) |
| `INSERT INTO users VALUES (...)` | Fast (append one row) | Slower (must update multiple column files) |

**Rule of thumb:** Row storage for transactions (OLTP). Column storage for analytics (OLAP).

### Apache Parquet — The Industry Standard

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'user_id': range(1, 1000001),
    'name': ['User_' + str(i) for i in range(1, 1000001)],
    'age': [20 + (i % 50) for i in range(1, 1000001)],
    'salary': [50000 + (i * 10) for i in range(1, 1000001)]
})

# Save as CSV (row-oriented)
df.to_csv('users.csv', index=False)
# File size: ~30 MB

# Save as Parquet (column-oriented, compressed)
df.to_parquet('users.parquet', index=False)
# File size: ~8 MB  (73% smaller due to compression!)

# Read back — Parquet can read specific columns without loading the whole file
df_salary = pd.read_parquet('users.parquet', columns=['salary'])
# Only reads the salary column from disk. Lightning fast!
```

### Why Parquet Files are Smaller

Columnar formats achieve incredible compression because values in the same column tend to be similar:

```
Name column:  [Alice, Alice, Alice, Bob, Bob, Bob, Carol, Carol]
→ Run-length encoding: [(Alice, 3), (Bob, 3), (Carol, 2)]
→ 8 values compressed to 3 entries!

Age column:   [25, 25, 25, 25, 30, 30, 30, 30]
→ Dictionary encoding + RLE: [25→0, 30→1] + [(0,4), (1,4)]
→ Massive compression!

Salary column: [95000, 95100, 95200, 95300, ...]
→ Delta encoding: [95000, +100, +100, +100, ...]
→ Store deltas instead of full values!
```

### Parquet vs Other Formats

| Format | Type | Compression | Speed | Ecosystem |
|---|---|---|---|---|
| **CSV** | Row-based text | None | Slow | Universal |
| **JSON** | Row-based text | None | Slow | Web/APIs |
| **Parquet** | Columnar binary | Snappy/Gzip | Fast | Spark, AWS, BigQuery |
| **ORC** | Columnar binary | Zlib/Snappy | Fast | Hive, Hadoop |
| **Avro** | Row-based binary | Deflate | Medium | Kafka, streaming |

Parquet is the de facto standard for analytical data in the modern data stack. If you're storing data for analysis, always use Parquet over CSV.""",

    "Data Drift": """## When the World Changes — Understanding Data Drift

**Data Drift** occurs when the statistical properties of the data your model receives in production **diverge** from the data it was trained on. Even if your model was 99% accurate at launch, it can slowly (or suddenly) become unreliable as the real world changes around it. Detecting drift is critical for maintaining model reliability.

### What Causes Data Drift?

```
Training data (2023):
  Average house price: $350,000
  Most common age group: 30-40
  Most popular feature: "3 bedrooms"

Production data (2024):
  Average house price: $420,000      ← Inflation shifted prices up
  Most common age group: 25-35       ← Demographic shift
  Most popular feature: "2 bedrooms" ← Market preference changed

Your model learned the patterns of 2023.
It's now making predictions in a 2024 world.
The inputs have drifted — predictions will degrade.
```

### Types of Drift

| Type | What Changes | Example |
|---|---|---|
| **Data Drift** | Input feature distributions | Average income of users increased by 20% |
| **Concept Drift** | The relationship between input and output | $500K used to mean "luxury home" but now means "starter home" |
| **Label Drift** | The distribution of target labels | Fraud rate increased from 1% to 5% |
| **Prediction Drift** | The distribution of model predictions | Model starts predicting "high risk" more often |

### Detecting Data Drift

```python
import numpy as np
from scipy import stats

# Training data distribution
train_ages = [25, 30, 35, 28, 32, 29, 31, 34, 27, 33]

# Production data (collected this week)
prod_ages = [22, 24, 21, 23, 25, 20, 22, 24, 21, 23]

# Statistical test: Kolmogorov-Smirnov test
# Tests if two samples come from the same distribution
ks_stat, p_value = stats.ks_2samp(train_ages, prod_ages)

print(f"KS Statistic: {ks_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("DRIFT DETECTED! Distributions are significantly different.")
else:
    print("No significant drift detected.")
```

### Monitoring Dashboard

```
Feature: user_age
  Training mean:    31.2
  Production mean:  22.8
  Drift score:      0.87 (HIGH)    🔴
  Status: ALERT — Retrain recommended

Feature: purchase_amount
  Training mean:    $85.50
  Production mean:  $82.30
  Drift score:      0.12 (LOW)     🟢
  Status: Stable

Feature: session_duration
  Training mean:    12.3 min
  Production mean:  8.7 min
  Drift score:      0.64 (MEDIUM)  🟡
  Status: Monitor closely
```

### Common Drift Detection Methods

| Method | Description | Best For |
|---|---|---|
| **KS Test** | Compares cumulative distributions | Continuous features |
| **Chi-Square Test** | Compares categorical distributions | Categorical features |
| **PSI (Population Stability Index)** | Measures distribution shift | Credit scoring, finance |
| **Wasserstein Distance** | "Earth mover's distance" between distributions | Continuous features |
| **Jensen-Shannon Divergence** | Symmetric measure of distribution similarity | Any distribution |

### What to Do When Drift is Detected

```
1. ALERT    → Notify the ML team automatically
2. ANALYZE  → Which features drifted? By how much?
3. VALIDATE → Is the model's accuracy actually degrading?
4. RETRAIN  → Train a new model on recent data
5. DEPLOY   → Replace the old model with the updated one
6. MONITOR  → Continue watching for the next drift
```

Data drift is inevitable — the world never stops changing. The goal isn't to prevent drift, but to **detect it quickly** and respond before your users notice degraded predictions.""",

    "Evidently AI": """## Automated Drift Detection with Evidently AI

**Evidently AI** is an open-source Python library that automates the detection and visualization of data drift, prediction drift, and data quality issues in machine learning systems. Instead of manually computing statistical tests, Evidently generates comprehensive reports and dashboards that show exactly how your production data differs from your training data.

### Why Evidently?

```
Manual drift detection:
  1. Pull training data distribution
  2. Pull production data distribution  
  3. Choose statistical test (KS? PSI? Chi-Square?)
  4. Run test on each feature (you have 50 features)
  5. Interpret results
  6. Create visualizations
  7. Write alerts
  → Takes hours of custom code per model

Evidently:
  report = Report(metrics=[DataDriftPreset()])
  report.run(reference_data=train_df, current_data=prod_df)
  report.save_html("drift_report.html")
  → Done in 3 lines. Beautiful HTML report generated.
```

### Core Concepts

| Concept | Description |
|---|---|
| **Reference Data** | Your training/baseline dataset (what the model expects) |
| **Current Data** | Live production data (what the model is actually seeing) |
| **Report** | A collection of metrics computed on reference vs current data |
| **Metric Preset** | Pre-configured bundles of related metrics |
| **Test Suite** | Pass/fail checks with configurable thresholds |

### Generating a Data Drift Report

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset
import pandas as pd

# Your reference (training) data
reference_df = pd.DataFrame({
    'age': [25, 30, 35, 28, 32, 29, 31, 34, 27, 33],
    'income': [50000, 65000, 72000, 58000, 70000, 62000, 68000, 75000, 55000, 71000],
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'C', 'A', 'B']
})

# Your current (production) data
current_df = pd.DataFrame({
    'age': [22, 24, 21, 23, 25, 20, 22, 24, 21, 23],
    'income': [45000, 48000, 42000, 47000, 50000, 41000, 46000, 49000, 43000, 48000],
    'category': ['A', 'A', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'B']
})

# Create a report with the Data Drift preset
report = Report(metrics=[
    DataDriftPreset(),        # Checks for distribution shifts
    DataQualityPreset()       # Checks for missing values, new categories
])

# Run the comparison
report.run(reference_data=reference_df, current_data=current_df)

# Save as interactive HTML
report.save_html("drift_report.html")

# Or get results as a dictionary
results = report.as_dict()
print(f"Dataset drift detected: {results['metrics'][0]['result']['dataset_drift']}")
```

### Available Presets

```python
from evidently.metric_preset import (
    DataDriftPreset,          # Feature distribution changes
    DataQualityPreset,        # Missing values, duplicates, new categories
    TargetDriftPreset,        # Target/prediction distribution changes
    RegressionPreset,         # Regression model performance metrics
    ClassificationPreset,     # Classification model performance metrics
)

# Combine multiple presets in one report:
report = Report(metrics=[
    DataDriftPreset(),
    DataQualityPreset(),
    ClassificationPreset()
])
```

### Test Suites — Automated Pass/Fail

For production monitoring, use **Test Suites** with explicit thresholds:

```python
from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset

# Create a test suite (like unit tests for data)
suite = TestSuite(tests=[
    DataDriftTestPreset()  # Fails if significant drift detected
])

suite.run(reference_data=reference_df, current_data=current_df)

# Check if all tests passed
if suite.as_dict()["summary"]["all_passed"]:
    print("All drift tests passed. Model is safe to use.")
else:
    print("ALERT: Drift detected! Review the report.")
    suite.save_html("drift_alert.html")
```

### Integration with MLOps

Evidently integrates into your ML monitoring pipeline:

```
Training Data (reference)     Production Data (current)
        ↓                              ↓
    ┌───────────────────────────────────────┐
    │          Evidently Report             │
    │                                       │
    │  Feature Drift:  2 of 10 drifted 🔴  │
    │  Data Quality:   No missing values 🟢 │
    │  Model Perf:     Accuracy dropped 🟡  │
    └───────────┬───────────────────────────┘
                │
         Alert if drift detected
                │
    ┌───────────▼───────────┐
    │  Retrain Pipeline     │
    │  (triggered by drift)  │
    └───────────────────────┘
```""",

    "Containerized ML": """## Kubeflow Pipelines — Running ML on Kubernetes

**Kubeflow Pipelines (KFP)** is a platform for building, deploying, and managing **end-to-end machine learning workflows** on Kubernetes. Each step of your ML pipeline (data preprocessing, training, evaluation, deployment) runs inside its own isolated **container**, making it reproducible, scalable, and portable across any cloud provider.

### Why Containerize ML?

```
The "works on my machine" problem:
  Data Scientist: "My model trains perfectly on my laptop!"
  
  On the production server:
  - Different Python version (3.8 vs 3.11)
  - Different scikit-learn version (1.0 vs 1.3)
  - Different OS (Mac vs Linux)
  - Missing system libraries (libgomp, libblas)
  → Model crashes or produces different results! 💥

With containers:
  Every step runs inside a Docker container with:
  - Exact Python version
  - Exact library versions
  - Exact system dependencies
  - Same environment everywhere: laptop, CI/CD, production
  → Perfectly reproducible. Always.
```

### KFP Architecture

```
┌──────────────────────────────────────────────────┐
│              Kubeflow Pipeline                    │
│                                                   │
│  ┌──────────┐   ┌──────────┐   ┌──────────────┐ │
│  │Preprocess│ → │  Train   │ → │  Evaluate    │ │
│  │Container │   │Container │   │  Container   │ │
│  │          │   │          │   │              │ │
│  │Python3.11│   │PyTorch   │   │scikit-learn  │ │
│  │pandas    │   │GPU       │   │matplotlib    │ │
│  │numpy     │   │wandb     │   │              │ │
│  └──────────┘   └──────────┘   └──────┬───────┘ │
│                                        │         │
│                              ┌─────────▼───────┐ │
│                              │    Deploy       │ │
│                              │    Container    │ │
│                              │    FastAPI      │ │
│                              │    model.pkl    │ │
│                              └─────────────────┘ │
└──────────────────────────────────────────────────┘
     Running on Kubernetes cluster (auto-scaling)
```

### Defining Components with KFP

Each pipeline step is a **component** — a Python function decorated with `@dsl.component`:

```python
from kfp import dsl

@dsl.component(
    base_image="python:3.11",
    packages_to_install=["pandas", "scikit-learn"]
)
def preprocess_data(input_path: str) -> str:
    import pandas as pd
    df = pd.read_csv(input_path)
    df = df.dropna()
    output_path = "/tmp/clean_data.csv"
    df.to_csv(output_path, index=False)
    return output_path

@dsl.component(
    base_image="pytorch/pytorch:2.0.0-cuda11.7",
    packages_to_install=["scikit-learn"]
)
def train_model(data_path: str, learning_rate: float) -> str:
    import joblib
    from sklearn.ensemble import RandomForestClassifier
    import pandas as pd
    
    df = pd.read_csv(data_path)
    X, y = df.drop("target", axis=1), df["target"]
    
    model = RandomForestClassifier(max_depth=10)
    model.fit(X, y)
    
    model_path = "/tmp/model.pkl"
    joblib.dump(model, model_path)
    return model_path

@dsl.component
def evaluate_model(model_path: str, test_data: str) -> float:
    import joblib
    model = joblib.load(model_path)
    # ... evaluate and return accuracy
    return 0.95
```

### Building the Pipeline

```python
@dsl.pipeline(name="ml-training-pipeline")
def ml_pipeline(input_path: str, learning_rate: float = 0.01):
    # Step 1: Preprocess
    preprocess_task = preprocess_data(input_path=input_path)
    
    # Step 2: Train (depends on preprocess output)
    train_task = train_model(
        data_path=preprocess_task.output,
        learning_rate=learning_rate
    )
    
    # Step 3: Evaluate (depends on train output)
    eval_task = evaluate_model(
        model_path=train_task.output,
        test_data=preprocess_task.output
    )
```

### Key Benefits

| Benefit | Description |
|---|---|
| **Reproducibility** | Every run uses exact same container images |
| **Scalability** | Kubernetes auto-scales compute (CPU, GPU) |
| **Portability** | Runs on any cloud: AWS, GCP, Azure, on-prem |
| **Versioning** | Every pipeline run is tracked with parameters & artifacts |
| **Caching** | Unchanged steps are skipped on re-runs |
| **Parallel Execution** | Independent steps run simultaneously |""",

    "Pipeline Definition": """## Connecting the Dots — Building ML Pipeline DAGs

A **Pipeline** in Kubeflow Pipelines connects multiple components into a **Directed Acyclic Graph (DAG)** — where the output of one component flows into the input of the next. This creates a complete, end-to-end ML workflow that can be scheduled, monitored, and reproduced with a single command.

### What is a Pipeline DAG?

```
DAG = Directed Acyclic Graph

Directed: Data flows in one direction (preprocess → train → evaluate)
Acyclic:  No loops (evaluate can't flow back to preprocess)
Graph:    Components are nodes, data flow is edges

┌────────────┐     ┌──────────┐     ┌──────────┐
│ Preprocess │ ──→ │  Train   │ ──→ │ Evaluate │
└────────────┘     └──────────┘     └──────────┘
      ↓                                   ↓
┌────────────┐                     ┌──────────┐
│  Validate  │                     │  Deploy  │
└────────────┘                     └──────────┘

Components run in dependency order.
Parallel branches execute simultaneously.
```

### Connecting Components with .output

The key mechanism is the `.output` property — it captures the return value of one component and passes it as input to the next:

```python
from kfp import dsl

@dsl.component
def preprocess(raw_data: str) -> str:
    # Clean the data, return path to cleaned file
    clean_path = f"/tmp/clean_{raw_data}"
    # ... processing logic ...
    return clean_path

@dsl.component
def train(clean_data: str, epochs: int) -> str:
    # Train a model using the clean data
    model_path = "/tmp/model.pkl"
    # ... training logic ...
    return model_path

@dsl.component
def evaluate(model_path: str, test_data: str) -> float:
    # Evaluate the model, return accuracy
    return 0.95

@dsl.component
def deploy(model_path: str, accuracy: float) -> str:
    if accuracy > 0.90:
        return f"Deployed {model_path} with accuracy {accuracy}"
    return f"Model accuracy {accuracy} too low. Not deploying."

# ─── The Pipeline Definition ────────────────────────
@dsl.pipeline(name="full-ml-pipeline")
def ml_pipeline(raw_data: str = "dataset.csv", epochs: int = 10):
    # Step 1: Preprocess
    preprocess_task = preprocess(raw_data=raw_data)
    
    # Step 2: Train (uses output from preprocess)
    train_task = train(
        clean_data=preprocess_task.output,  # ← Connection!
        epochs=epochs
    )
    
    # Step 3: Evaluate (uses outputs from both train and preprocess)
    eval_task = evaluate(
        model_path=train_task.output,       # ← Connection!
        test_data=preprocess_task.output     # ← Connection!
    )
    
    # Step 4: Deploy (conditional on accuracy)
    deploy_task = deploy(
        model_path=train_task.output,       # ← Connection!
        accuracy=eval_task.output            # ← Connection!
    )
```

### How .output Works

```
preprocess(raw_data="dataset.csv")
  → Returns: "/tmp/clean_dataset.csv"
  → preprocess_task.output = "/tmp/clean_dataset.csv"

train(clean_data=preprocess_task.output, epochs=10)
  → Receives: clean_data="/tmp/clean_dataset.csv"
  → Returns: "/tmp/model.pkl"
  → train_task.output = "/tmp/model.pkl"

evaluate(model_path=train_task.output, test_data=preprocess_task.output)
  → Receives: model_path="/tmp/model.pkl", test_data="/tmp/clean_dataset.csv"
  → Returns: 0.95
  → eval_task.output = 0.95
```

### Advanced Pipeline Patterns

```python
# Parallel execution — independent steps run simultaneously
@dsl.pipeline(name="parallel-pipeline")
def parallel_pipeline():
    data_task = load_data()
    
    # These two run IN PARALLEL (no dependency between them):
    model_a = train_model_a(data=data_task.output)
    model_b = train_model_b(data=data_task.output)
    
    # This waits for BOTH to complete:
    compare = compare_models(
        model_a=model_a.output,
        model_b=model_b.output
    )

# Conditional execution
@dsl.pipeline(name="conditional-pipeline")  
def conditional_pipeline():
    eval_task = evaluate_model()
    
    with dsl.Condition(eval_task.output > 0.90):
        deploy_task = deploy_to_production()
    
    with dsl.Condition(eval_task.output <= 0.90):
        retrain_task = retrain_model()
```

### Compiling and Running

```python
from kfp import compiler

# Compile pipeline to YAML
compiler.Compiler().compile(
    pipeline_func=ml_pipeline,
    package_path="pipeline.yaml"
)

# Submit to Kubeflow
from kfp.client import Client
client = Client(host="http://kubeflow-endpoint")
client.create_run_from_pipeline_func(
    ml_pipeline,
    arguments={"raw_data": "s3://bucket/data.csv", "epochs": 20}
)
```

The `.output` property is the glue that connects your ML steps into a cohesive, automated pipeline. Data flows from step to step without manual file management — Kubeflow handles data passing, scheduling, and retry logic automatically.""",

    "Hadoop vs Apache Spark": """## The Big Data Revolution — From Hadoop to Spark

When datasets grow beyond what any single machine can handle — terabytes or petabytes — you need **distributed computing**. **Hadoop MapReduce** was the first practical system for processing massive datasets across clusters of commodity hardware. **Apache Spark** succeeded it by solving Hadoop's biggest weakness: speed. Understanding this evolution is essential for any data engineer.

### The Hadoop Era (2006-2015)

Hadoop was Google's MapReduce paper brought to life as open-source software. It introduced a revolutionary idea: instead of buying one supercomputer, distribute your data across hundreds of cheap machines.

```
Hadoop's Two Components:
  1. HDFS (Hadoop Distributed File System)
     - Splits files into 128MB blocks
     - Replicates each block across 3 machines
     - If a machine dies, data is safe on 2 other machines

  2. MapReduce (Processing Engine)
     - MAP: Apply a function to every record in parallel
     - REDUCE: Aggregate the results
     - Each step reads from and writes to DISK
```

### Why Hadoop Was Slow

```
Hadoop MapReduce — a 3-step job:

Step 1 (Map):
  Read data from HDFS (disk) → Process → Write results to disk
  ↕ DISK I/O ↕                            ↕ DISK I/O ↕

Step 2 (Shuffle):
  Read from disk → Send across network → Write to disk
  ↕ DISK I/O ↕                            ↕ DISK I/O ↕

Step 3 (Reduce):
  Read from disk → Aggregate → Write final results to disk
  ↕ DISK I/O ↕                            ↕ DISK I/O ↕

Every intermediate result hits the disk.
Disk is ~100x slower than RAM.
For iterative ML algorithms (100+ iterations), this is devastating.
```

### Apache Spark — The In-Memory Revolution (2014+)

Spark's key insight: **keep intermediate data in RAM** instead of writing to disk at every step.

```
Apache Spark — the same 3-step job:

Step 1 (Map):
  Read data from storage → Process → Keep results IN MEMORY
                                      ↕ RAM (fast!) ↕

Step 2 (Shuffle):
  Read from RAM → Send across network → Keep IN MEMORY
  ↕ RAM (fast!) ↕                      ↕ RAM (fast!) ↕

Step 3 (Reduce):
  Read from RAM → Aggregate → Write only FINAL results to disk
  ↕ RAM (fast!) ↕

Only the first read and final write touch the disk.
Everything in between stays in RAM.
Up to 100x faster for iterative workloads!
```

### Performance Comparison

| Metric | Hadoop MapReduce | Apache Spark |
|---|---|---|
| **Intermediate storage** | Disk | RAM |
| **Speed (batch)** | Baseline | 10-100x faster |
| **Speed (iterative ML)** | Very slow | 100x faster |
| **Real-time streaming** | Not supported | Spark Structured Streaming |
| **Ease of use** | Java/verbose | Python/Scala/SQL/simple |
| **ML support** | Mahout (limited) | MLlib (comprehensive) |
| **Interactive queries** | No | Yes (Spark SQL) |
| **Fault tolerance** | Disk replication | RDD lineage recomputation |

### The Modern Data Stack

```
2006-2014: Hadoop era
  HDFS + MapReduce → Slow but revolutionary

2014-2020: Spark era  
  Spark on HDFS/S3 → Fast, versatile, became the standard

2020+: Cloud-native era
  Spark on Databricks/EMR/Dataproc + Delta Lake
  → Managed, serverless, Lakehouse architecture
```

Hadoop's HDFS is still widely used for distributed storage, but MapReduce has been almost entirely replaced by Spark for processing. When someone says "big data processing" today, they almost always mean Spark.""",

    "Resilient Distributed Datasets (RDDs)": """## RDDs — Spark's Foundational Data Structure

A **Resilient Distributed Dataset (RDD)** is the core abstraction in Apache Spark. It represents an immutable, partitioned collection of records that is distributed across a cluster and processed in parallel. While modern Spark code primarily uses DataFrames, understanding RDDs is essential because they're the foundation everything else is built upon.

### The Three Properties of RDDs

The name says it all:

```
R — Resilient (Fault-tolerant)
    If a node crashes and a partition is lost,
    Spark recomputes it using the "lineage" (recipe) of transformations.
    No data loss, no manual recovery needed.

D — Distributed
    Data is split into "partitions" spread across cluster nodes.
    Each partition is processed independently, in parallel.

D — Dataset
    A collection of records (rows of data).
    Can hold any Python/Java/Scala object.
```

### How RDDs are Distributed

```
Original data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Partitioned across 3 nodes:
  Node 1: Partition 0 → [1, 2, 3, 4]
  Node 2: Partition 1 → [5, 6, 7, 8]
  Node 3: Partition 2 → [9, 10, 11, 12]

When you call rdd.map(lambda x: x * 2):
  Node 1 processes: [2, 4, 6, 8]
  Node 2 processes: [10, 12, 14, 16]
  Node 3 processes: [18, 20, 22, 24]

  All three compute in PARALLEL. 3x speedup!
```

### RDD Operations: Transformations vs Actions

```python
from pyspark import SparkContext
sc = SparkContext("local", "RDD Demo")

# Create an RDD from a list
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# ─── TRANSFORMATIONS (lazy — not executed yet!) ─────────
squared = rdd.map(lambda x: x ** 2)         # [1, 4, 9, 16, ...]
evens = rdd.filter(lambda x: x % 2 == 0)    # [2, 4, 6, 8, 10]
pairs = rdd.map(lambda x: (x % 3, x))       # [(1,1), (2,2), (0,3), ...]
# Nothing has actually been computed yet!

# ─── ACTIONS (trigger computation!) ─────────────────────
print(squared.collect())    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(evens.count())        # 5
print(rdd.reduce(lambda a, b: a + b))  # 55
```

### Lineage — How Fault Tolerance Works

Instead of replicating data (expensive), Spark remembers the **recipe** (lineage) used to create each RDD:

```
Lineage Graph:
  raw_rdd = sc.textFile("hdfs://data.csv")
      ↓ map(parse_line)
  parsed_rdd
      ↓ filter(lambda x: x.age > 25)
  filtered_rdd
      ↓ map(lambda x: (x.city, x.salary))
  city_salary_rdd
      ↓ reduceByKey(lambda a, b: a + b)
  result_rdd

If Node 2 crashes and loses Partition 1 of filtered_rdd:
  Spark doesn't panic!
  1. Looks at the lineage graph
  2. Re-reads Partition 1 of raw_rdd from HDFS
  3. Re-applies parse_line
  4. Re-applies the filter
  5. Partition is reconstructed. No data lost!
```

### RDDs vs DataFrames

| Feature | RDD | DataFrame |
|---|---|---|
| **API Level** | Low-level | High-level (SQL-like) |
| **Optimization** | None (you optimize manually) | Catalyst optimizer (automatic) |
| **Schema** | No schema (untyped) | Has schema (typed columns) |
| **Performance** | Slower (no optimization) | Faster (optimized execution plan) |
| **Use Case** | Custom transformations, unstructured data | Structured data, SQL queries |

**Modern recommendation:** Use DataFrames for 95% of tasks. Use RDDs only when you need fine-grained control over partitioning or are working with non-tabular data.""",

    "Spark DataFrames and Catalyst": """## The Catalyst Optimizer — Spark's Secret Weapon

While RDDs give you raw power, Spark **DataFrames** provide a higher-level, SQL-like API that's both easier to use AND faster. The secret sauce is the **Catalyst Optimizer** — an automatic query optimization engine that analyzes your DataFrame code and generates the most efficient execution plan, just like a SQL database optimizer.

### Why DataFrames are Faster than RDDs

```python
# RDD approach (no optimization):
rdd = sc.textFile("data.csv")
result = (rdd
    .map(lambda line: line.split(","))
    .filter(lambda row: int(row[2]) > 25)
    .map(lambda row: (row[1], float(row[3])))
    .reduceByKey(lambda a, b: a + b)
)
# Spark runs EXACTLY what you wrote. No optimization.
# If your code is inefficient, Spark doesn't help.

# DataFrame approach (Catalyst optimized):
df = spark.read.csv("data.csv", header=True, inferSchema=True)
result = (df
    .filter(df.age > 25)
    .groupBy("city")
    .agg({"salary": "sum"})
)
# Catalyst analyzes this and generates an optimal plan:
# - Pushes filter BEFORE groupBy (processes fewer rows)
# - Chooses the most efficient join algorithm
# - Optimizes memory layout
# - Generates optimized JVM bytecode
```

### How Catalyst Works — The Four Phases

```
Your DataFrame Code
       ↓
1. ANALYSIS
   - Resolve column names and types
   - Verify that operations are valid
   - "Does column 'age' exist? Is it numeric?"
       ↓
2. LOGICAL OPTIMIZATION
   - Rewrite the plan using optimization rules
   - Push filters down (filter early, process less)
   - Prune unused columns (don't read what you don't need)
   - Constant folding (compute 2+3=5 at compile time)
       ↓
3. PHYSICAL PLANNING
   - Choose execution strategies
   - Sort-Merge Join vs Broadcast Hash Join?
   - How many partitions?
   - Which nodes run which tasks?
       ↓
4. CODE GENERATION (Tungsten)
   - Generate optimized Java bytecode
   - Operate on raw memory (off-heap)
   - Avoid JVM garbage collection overhead
       ↓
Optimized Execution!
```

### Catalyst Optimization Example

```python
# Your code:
df.filter(df.age > 25).select("name", "age").filter(df.age < 50)

# Without optimization, Spark would:
# 1. Read ALL columns from disk
# 2. Filter age > 25
# 3. Select name, age
# 4. Filter age < 50

# Catalyst optimizes to:
# 1. Read ONLY name and age columns (column pruning)
# 2. Filter age > 25 AND age < 50 in ONE pass (predicate pushdown)
# → Reads less data, applies fewer operations!
```

### The explain() Method

You can see Catalyst's optimization plan:

```python
df.filter(df.age > 25).groupBy("city").count().explain(True)

# == Parsed Logical Plan ==
# Aggregate [city], [city, count(1) AS count]
# +- Filter (age > 25)
#    +- Relation [name, age, city, salary]
#
# == Optimized Logical Plan ==
# Aggregate [city], [city, count(1) AS count]
# +- Project [city]                          ← Only reads 'city' column!
#    +- Filter (age > 25)
#       +- Relation [name, age, city, salary]
#
# == Physical Plan ==
# HashAggregate(keys=[city], functions=[count(1)])
# +- Exchange hashpartitioning(city, 200)     ← Shuffle by city
#    +- HashAggregate(keys=[city], functions=[partial_count(1)])
#       +- Project [city]
#          +- Filter (age > 25)
#             +- FileScan parquet [age, city]  ← Reads only 2 columns!
```

### Key Optimization Techniques

| Technique | Description | Example |
|---|---|---|
| **Predicate Pushdown** | Move filters as early as possible | Filter before join, not after |
| **Column Pruning** | Only read needed columns | `SELECT name, age` doesn't read salary |
| **Constant Folding** | Pre-compute constant expressions | `2 + 3` becomes `5` at compile time |
| **Join Reordering** | Optimize multi-table join order | Join smallest tables first |
| **Broadcast Join** | Send small table to all nodes | Avoids expensive shuffle for small tables |

The bottom line: use DataFrames over RDDs whenever possible. Catalyst's automatic optimization means your code runs faster without you having to think about it.""",

    "Lazy Evaluation": """## Do Nothing Until Absolutely Necessary — Spark's Lazy Evaluation

**Lazy Evaluation** is Spark's execution strategy where **transformations** (like `map`, `filter`, `select`) don't actually execute when called — they're just recorded as a plan. Spark only runs the computation when an **action** (like `count`, `collect`, `show`) explicitly requests a result. This laziness isn't procrastination — it's a powerful optimization strategy.

### Why Be Lazy?

```
Eager Evaluation (like Pandas — runs immediately):
  Step 1: df.filter(age > 25)     → Scans ALL data, creates filtered copy
  Step 2: df.select("name")       → Scans filtered data, creates new copy
  Step 3: df.filter(age < 50)     → Scans again, creates another copy
  
  3 full scans of the data. 3 intermediate copies in memory.

Lazy Evaluation (Spark — waits, then optimizes):
  Step 1: df.filter(age > 25)     → Records: "filter age > 25"
  Step 2: df.select("name")       → Records: "select name column"
  Step 3: df.filter(age < 50)     → Records: "filter age < 50"
  
  Nothing executed yet! When you finally call .count():
  
  Spark sees the full plan and OPTIMIZES:
  → Combine filters: age > 25 AND age < 50 (one pass!)
  → Read only "name" and "age" columns (skip salary, city, etc.)
  → Single scan. Zero intermediate copies. Much faster!
```

### Transformations vs Actions

```python
# ─── TRANSFORMATIONS (lazy — builds the plan) ──────────
df2 = df.filter(df.age > 25)           # No computation
df3 = df2.select("name", "salary")     # No computation
df4 = df3.groupBy("name")              # No computation
df5 = df4.agg({"salary": "avg"})       # No computation

# The plan is built but NOTHING has executed!
# No data has been read. No CPU cycles used.

# ─── ACTIONS (trigger — execute the plan) ───────────────
df5.count()       # NOW everything executes! Spark reads data,
                  # filters, selects, groups, and counts.

df5.show()        # Triggers execution and displays results
df5.collect()     # Triggers execution and returns Python list
df5.write.csv()   # Triggers execution and writes to file
```

### Common Transformations and Actions

| Transformations (Lazy) | Actions (Trigger Execution) |
|---|---|
| `filter()` / `where()` | `count()` |
| `select()` | `show()` |
| `groupBy()` | `collect()` |
| `join()` | `first()` / `head()` |
| `map()` / `flatMap()` | `take(n)` |
| `orderBy()` / `sort()` | `reduce()` |
| `withColumn()` | `write.csv()` / `write.parquet()` |
| `distinct()` | `foreach()` |
| `union()` | `toPandas()` |

### Visualizing the Plan

```python
# Build a lazy plan
result = (spark.read.parquet("s3://data/orders/")
    .filter("amount > 100")
    .groupBy("category")
    .agg({"amount": "sum"})
    .orderBy("sum(amount)", ascending=False)
)

# See the plan WITHOUT executing it:
result.explain()
# == Physical Plan ==
# Sort [sum(amount) DESC]
#   +- HashAggregate [category], [sum(amount)]
#     +- Exchange hashpartitioning(category, 200)
#       +- HashAggregate [category], [partial_sum(amount)]
#         +- Filter (amount > 100)
#           +- FileScan parquet [category, amount]  ← Only reads 2 columns!

# Now trigger execution:
result.show()  # Spark runs the optimized plan
```

### The Key Insight

Lazy evaluation allows Spark to see your **entire computation** before running any of it. This global view enables optimizations that would be impossible with eager execution:

- **Combine filters** into a single pass
- **Skip unused columns** entirely
- **Reorder operations** for efficiency
- **Avoid creating intermediate datasets**

This is why a Spark pipeline with 10 transformations can be faster than a Pandas pipeline with 3 — Spark optimizes the whole thing into the minimum possible work.""",

    "Partitioning and Shuffling": """## The Most Expensive Operation in Spark — Understanding Shuffles

In distributed computing, data is split across multiple machines in units called **partitions**. Most operations (filter, map, select) work within each partition independently — no communication needed between machines. But some operations — like `groupBy`, `join`, and `orderBy` — require data to be **redistributed across the network**. This massive data movement is called a **Shuffle**, and it's the single biggest performance bottleneck in Spark.

### Why Shuffles are Expensive

```
BEFORE shuffle (data is partitioned by row):
  Node 1: [{Alice, NYC, $100}, {Bob, LA, $200}]
  Node 2: [{Carol, NYC, $150}, {Dave, LA, $300}]
  Node 3: [{Eve, NYC, $250},   {Frank, LA, $175}]

OPERATION: groupBy("city").sum("amount")

Spark needs all NYC data on one node and all LA data on another.

SHUFFLE (data moves across the network):
  Node 1 sends NYC data to Node A, LA data to Node B
  Node 2 sends NYC data to Node A, LA data to Node B
  Node 3 sends NYC data to Node A, LA data to Node B

  Network transfer: 6 data packets sent between machines!

AFTER shuffle:
  Node A: [{Alice, NYC, $100}, {Carol, NYC, $150}, {Eve, NYC, $250}]
  Node B: [{Bob, LA, $200}, {Dave, LA, $300}, {Frank, LA, $175}]

Now each node can aggregate independently:
  Node A: NYC → $500
  Node B: LA  → $675
```

### Operations That Trigger Shuffles

| Triggers Shuffle | Doesn't Trigger Shuffle |
|---|---|
| `groupBy()` + aggregation | `filter()` / `where()` |
| `join()` (most types) | `select()` / `withColumn()` |
| `orderBy()` / `sort()` | `map()` / `flatMap()` |
| `repartition()` | `union()` |
| `distinct()` | `coalesce()` (reduce partitions) |
| `reduceByKey()` | `mapPartitions()` |

### The Cost of a Shuffle

```
A shuffle involves:
  1. WRITE  — Each node writes its data to local disk (serialized)
  2. TRANSFER — Data is sent across the network to other nodes
  3. READ   — Receiving nodes read the data from network buffers
  4. SORT   — Data is sorted/grouped on the receiving side

For 1TB of data:
  - Disk I/O: Read + Write = ~2TB of disk operations
  - Network: Up to 1TB transferred across the cluster
  - Time: Minutes to hours depending on cluster size

This is why shuffle-heavy operations are 10-100x slower
than partition-local operations!
```

### Strategies to Minimize Shuffles

```python
# Strategy 1: FILTER EARLY — reduce data before shuffle
# Bad: groupBy first, then filter
df.groupBy("city").sum("amount").filter("sum(amount) > 1000")
# Shuffles ALL data, then filters

# Good: filter first, then groupBy
df.filter(df.amount > 10).groupBy("city").sum("amount")
# Filters out small amounts BEFORE shuffling — much less data to move!

# Strategy 2: BROADCAST JOIN — avoid shuffle for small tables
from pyspark.sql.functions import broadcast
# If one table is small (< 10MB), broadcast it to all nodes
result = big_df.join(broadcast(small_df), "key")
# No shuffle! Small table is copied to every node.

# Strategy 3: PRE-PARTITION — partition data by the join key
# Write data partitioned by the groupBy key
df.write.partitionBy("city").parquet("s3://data/orders/")
# Future groupBy("city") operations won't need a shuffle!

# Strategy 4: COALESCE — reduce partitions without a full shuffle
df.coalesce(10)  # Reduces from 200 to 10 partitions (no shuffle)
df.repartition(10)  # Also reduces, but DOES trigger a shuffle
```

### Monitoring Shuffles in the Spark UI

The Spark Web UI shows shuffle metrics for every job:
- **Shuffle Read**: Data received from other nodes
- **Shuffle Write**: Data sent to other nodes
- **Shuffle Spill (Memory)**: Data that overflowed RAM to disk
- **Shuffle Spill (Disk)**: Actual disk space used for spill

If you see large shuffle spill values, you need more memory or better partitioning.""",

    "Broadcast Variables": """## Broadcast Variables — Eliminating Shuffles for Small Data

A **Broadcast Variable** is a read-only variable that Spark sends to every worker node in the cluster exactly once, keeping it cached in memory for efficient lookups. This is the primary technique for optimizing joins between a **large dataset** and a **small lookup table** — eliminating the expensive shuffle that would otherwise move terabytes of data across the network.

### The Problem: Shuffle Joins are Expensive

```
Without broadcast (standard shuffle join):

  Large table (1TB, 100 partitions across 50 nodes)
  Small lookup table (10MB)

  Standard join:
  1. Spark shuffles BOTH tables by the join key
  2. 1TB of data moves across the network  ← EXPENSIVE!
  3. 10MB also moves across the network
  4. Matching rows are joined

  Network transfer: ~1TB. Time: potentially hours.

With broadcast:

  1. Spark sends the 10MB table to ALL 50 nodes (broadcast)
  2. Each node joins its local partition with the local copy
  3. NO shuffle needed for the large table!

  Network transfer: ~500MB (10MB × 50 nodes). Time: minutes.
  1TB of data NEVER moves!
```

### How to Use Broadcast Variables

```python
from pyspark.sql.functions import broadcast

# Large dataset: 1 billion rows of transactions
transactions = spark.read.parquet("s3://data/transactions/")

# Small lookup table: 500 rows of product categories
categories = spark.read.csv("product_categories.csv", header=True)

# ─── BAD: Standard join (triggers shuffle of both tables) ──
result = transactions.join(categories, "product_id")
# Spark shuffles 1 billion rows across the network! 💥

# ─── GOOD: Broadcast join (no shuffle for large table) ──
result = transactions.join(broadcast(categories), "product_id")
# Spark broadcasts the small 500-row table to every node.
# Each node joins locally. No shuffle needed!
```

### When to Broadcast

```python
# Spark auto-broadcasts tables smaller than this threshold:
spark.conf.get("spark.sql.autoBroadcastJoinThreshold")
# Default: 10MB (10485760 bytes)

# You can adjust it:
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 50 * 1024 * 1024)  # 50MB

# Or disable auto-broadcast:
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)

# Or force broadcast for a specific join:
result = big_df.join(broadcast(small_df), "key")
```

### Broadcast Variables (Low-Level RDD API)

```python
# For non-join use cases, you can broadcast any variable:
zip_to_state = {
    "10001": "NY", "90210": "CA", "60601": "IL",
    # ... thousands of zip codes
}

# Broadcast the dictionary to all nodes
broadcast_zips = sc.broadcast(zip_to_state)

# Each node has a local copy — no network calls during map!
def enrich_with_state(row):
    zip_code = row["zip"]
    state = broadcast_zips.value.get(zip_code, "Unknown")
    return {**row, "state": state}

enriched_rdd = transactions_rdd.map(enrich_with_state)
```

### Common Broadcast Use Cases

| Use Case | Large Table | Small Broadcast Table |
|---|---|---|
| **Enrichment** | Customer transactions (1B rows) | Product catalog (10K rows) |
| **Geocoding** | GPS coordinates (100M rows) | Zip code lookup (40K rows) |
| **Feature engineering** | User events (5B rows) | Country metadata (200 rows) |
| **Filtering** | Log entries (50B rows) | Blocklist of IPs (5K entries) |
| **Currency conversion** | Sales records (1B rows) | Exchange rates (150 rows) |

### Rules of Thumb

- **Broadcast if < 100MB** — Safe and fast
- **Be cautious 100MB-1GB** — Monitor driver memory
- **Never broadcast > 1GB** — Will crash the driver node
- **Check with `.explain()`** — Verify Spark is using BroadcastHashJoin

```python
result.explain()
# Look for: BroadcastHashJoin (good!)
# Not: SortMergeJoin (means broadcast wasn't applied)
```""",

    "PySpark SQL": """## SQL on Big Data — Querying Terabytes with PySpark SQL

One of Spark's most powerful features is the ability to run **standard ANSI SQL queries** directly against massive distributed datasets. You don't need to learn the DataFrame API — if you know SQL, you can immediately query terabytes of data using `spark.sql()`. Behind the scenes, Spark's Catalyst optimizer transforms your SQL into an optimized distributed execution plan.

### From SQL to Spark

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SQL Demo").getOrCreate()

# Read data (could be billions of rows across thousands of files)
orders = spark.read.parquet("s3://data-lake/orders/")
customers = spark.read.parquet("s3://data-lake/customers/")

# Register DataFrames as temporary SQL views
orders.createOrReplaceTempView("orders")
customers.createOrReplaceTempView("customers")

# Now write standard SQL!
result = spark.sql(\"\"\"
    SELECT 
        c.name,
        c.city,
        COUNT(o.order_id) AS total_orders,
        SUM(o.amount) AS total_spent,
        AVG(o.amount) AS avg_order_value
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_date >= '2024-01-01'
    GROUP BY c.name, c.city
    HAVING total_spent > 1000
    ORDER BY total_spent DESC
    LIMIT 100
\"\"\")

result.show()
```

### Why Use SQL Instead of the DataFrame API?

```python
# DataFrame API (Pythonic but verbose):
result = (orders
    .join(customers, orders.customer_id == customers.customer_id)
    .filter(orders.order_date >= "2024-01-01")
    .groupBy(customers.name, customers.city)
    .agg(
        count("order_id").alias("total_orders"),
        sum("amount").alias("total_spent"),
        avg("amount").alias("avg_order_value")
    )
    .filter(col("total_spent") > 1000)
    .orderBy(desc("total_spent"))
    .limit(100)
)

# SQL (familiar to every analyst):
result = spark.sql(\"\"\"
    SELECT c.name, c.city, COUNT(*) as total_orders,
           SUM(o.amount) as total_spent
    FROM orders o JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_date >= '2024-01-01'
    GROUP BY c.name, c.city
    HAVING SUM(o.amount) > 1000
    ORDER BY total_spent DESC LIMIT 100
\"\"\")

# BOTH produce the EXACT SAME optimized execution plan!
# Catalyst optimizer treats them identically.
```

### SQL Features Available in Spark SQL

```sql
-- All standard SQL works:
SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT
JOIN (INNER, LEFT, RIGHT, FULL, CROSS)
UNION, UNION ALL, INTERSECT, EXCEPT

-- Window functions:
SELECT name, salary,
       RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rank
FROM employees

-- Subqueries:
SELECT * FROM orders
WHERE customer_id IN (SELECT id FROM customers WHERE city = 'NYC')

-- CTEs (Common Table Expressions):
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) as month, SUM(amount) as total
    FROM orders GROUP BY 1
)
SELECT month, total,
       LAG(total) OVER (ORDER BY month) as prev_month
FROM monthly_sales

-- Spark-specific functions:
SELECT explode(array_column) FROM nested_data
SELECT from_json(json_string, 'struct<name:string, age:int>') FROM raw
```

### Permanent vs Temporary Views

```python
# Temporary view — exists only in current Spark session
df.createOrReplaceTempView("orders")          # Session-scoped
df.createOrReplaceGlobalTempView("orders")    # Application-scoped

# Permanent table — persisted in Hive Metastore/catalog
df.write.saveAsTable("production.orders")     # Permanent
spark.sql("SELECT * FROM production.orders")  # Always available
```

### Performance Tips

| Tip | Why |
|---|---|
| Use `EXPLAIN` to see the plan | Verify Catalyst is optimizing correctly |
| Partition your data by query columns | Enables partition pruning (skips irrelevant files) |
| Use Parquet format | Column pruning reads only needed columns |
| Cache frequently queried data | `spark.sql("CACHE TABLE orders")` keeps it in RAM |
| Broadcast small tables in joins | Avoids expensive shuffles |""",

    "Structured Streaming": """## Real-Time Data Processing — Spark Structured Streaming

**Structured Streaming** is Spark's engine for processing real-time data streams using the exact same DataFrame/SQL API you use for batch processing. The revolutionary idea: treat a live data stream as an **infinitely growing table** — every new event appends a new row. This means if you know how to write Spark batch queries, you already know how to write streaming queries.

### The Key Abstraction: Unbounded Table

```
Traditional streaming (complex):
  - Define event handlers for each message
  - Manage state manually
  - Handle time windows with custom code
  - Different API from batch processing

Structured Streaming (simple):
  A stream is just a table that grows forever.
  New events = new rows appended to the table.
  Your query runs continuously on this growing table.

Time     │  The "Input Table" (growing)
─────────┼──────────────────────────────────
10:00:01 │  {user: Alice, action: click, page: home}
10:00:02 │  {user: Bob,   action: view,  page: product}
10:00:03 │  {user: Alice, action: buy,   page: cart}
10:00:04 │  {user: Carol, action: click, page: home}
   ...   │  ... new rows keep arriving ...
```

### Batch vs Streaming — Same Code!

```python
# ─── BATCH (process all data at once) ─────────────────
batch_df = spark.read.parquet("s3://data/events/")
result = batch_df.groupBy("page").count()
result.write.parquet("s3://output/page_counts/")

# ─── STREAMING (process data as it arrives) ───────────
stream_df = (spark.readStream
    .format("kafka")
    .option("subscribe", "page-events")
    .load()
)

# Same transformation code!
result = stream_df.groupBy("page").count()

# Write results continuously
result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start() \
    .awaitTermination()
```

### Reading from Different Sources

```python
# Read from Kafka
stream = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "user-events")
    .load()
)

# Read from a directory of files (new files = new data)
stream = (spark.readStream
    .format("csv")
    .option("path", "s3://data/incoming/")
    .schema(my_schema)
    .load()
)

# Read from a socket (for testing)
stream = (spark.readStream
    .format("socket")
    .option("host", "localhost")
    .option("port", 9999)
    .load()
)
```

### Output Modes

| Mode | Description | Use Case |
|---|---|---|
| **Append** | Only new rows are written | Simple transformations, no aggregations |
| **Complete** | Entire result table is rewritten | Aggregations (groupBy + count) |
| **Update** | Only changed rows are written | Aggregations where only some groups change |

### Windowed Aggregations

For time-based analytics (e.g., "clicks per minute"), use **windowed aggregations**:

```python
from pyspark.sql.functions import window, col

# Count events per 5-minute window
windowed = (stream_df
    .groupBy(
        window(col("event_time"), "5 minutes"),
        col("page")
    )
    .count()
)

# This produces results like:
# +------------------------------------------+------+-----+
# | window                                   | page | count|
# +------------------------------------------+------+-----+
# | {2024-01-15 10:00:00, 2024-01-15 10:05:00}| home |  142|
# | {2024-01-15 10:00:00, 2024-01-15 10:05:00}| cart |   38|
# | {2024-01-15 10:05:00, 2024-01-15 10:10:00}| home |  156|
# +------------------------------------------+------+-----+
```

### The Power of Unification

```
Before Structured Streaming:
  - Batch pipeline: Spark + custom code (Python/Scala)
  - Stream pipeline: Apache Storm or Flink (completely different API!)
  - Two separate systems, two sets of logic, twice the maintenance

After Structured Streaming:
  - Batch and stream use the SAME DataFrame/SQL API
  - Write business logic ONCE
  - Run it in batch mode OR streaming mode
  - Test with batch data, deploy as a stream
```

This unification of batch and streaming is why Structured Streaming has become the dominant choice for organizations already using Spark for batch processing — no need to learn a separate streaming framework."""
}

# Apply patches
patched = 0
for course_name, course_data in data.items():
    for lesson in course_data.get("lessons", []):
        title = lesson["title"]
        if title in theories:
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories[title]
            new_len = len(lesson["theory"])
            print(f"  OK {title}: {old_len} -> {new_len} chars")
            patched += 1

with open("curriculum/tracks/data_engineering_mlops.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nPatched {patched} lessons in data_engineering_mlops.json")
