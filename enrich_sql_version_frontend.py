"""
enrich_sql_version_frontend.py
Manually patches rich, detailed theory for:
- sql_databases.json (32 lessons)
- version_control.json (21 lessons)  
- frontend.json (20 lessons)
"""
import json, os

def patch_track(track_file, theory_dict):
    print(f"\n{'='*60}")
    print(f"Loading {track_file}...")
    with open(track_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    patched = 0
    still_short = 0

    for topic, topic_data in data.items():
        for lesson in topic_data.get("lessons", []):
            title = lesson.get("title", "")
            if title in theory_dict:
                old_len = len(lesson.get("theory", ""))
                lesson["theory"] = theory_dict[title]
                new_len = len(lesson["theory"])
                print(f"  [OK] {title!r}: {old_len} -> {new_len} chars")
                patched += 1
            elif lesson.get("type") != "quiz" and len(lesson.get("theory", "")) <= 800:
                still_short += 1
                print(f"  [??] Still short: {title!r}")

    print(f"\nPatched: {patched} | Still short: {still_short}")
    with open(track_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved.")


# ════════════════════════════════════════════════
# SQL DATABASES
# ════════════════════════════════════════════════
SQL_THEORY = {

"Basic SELECT Queries": """## Reading Data from a Database

SQL (Structured Query Language) is the universal language for talking to relational databases. The `SELECT` statement is how you ask the database: "give me this data." Every SQL journey starts here.

### Basic Syntax

```sql
-- Basic template:
SELECT column1, column2, column3
FROM table_name;

-- Select ALL columns:
SELECT *
FROM students;
-- Returns every row and every column in the students table

-- Select specific columns:
SELECT name, email, gpa
FROM students;
-- Returns only those three columns for every student
```

### Understanding the Result Set

When you run a SELECT, the database returns a **result set** — a virtual table of matching rows. It doesn't change any data; it only reads.

```sql
-- The students table has: id, name, email, gpa, city, enrolled_date

SELECT name, gpa
FROM students;

-- Result:
-- name    | gpa
-- --------|-----
-- Alice   | 3.8
-- Bob     | 3.2
-- Carol   | 3.9
```

### Column Aliases — Renaming in Results

```sql
-- Use AS to give a column a friendlier name in the result:
SELECT
    name AS student_name,
    gpa  AS grade_point_average
FROM students;

-- Result:
-- student_name | grade_point_average
-- -------------|--------------------
-- Alice        | 3.8
```

### Selecting Expressions

You're not limited to column names — you can select computed expressions:

```sql
SELECT
    name,
    gpa,
    gpa * 25 AS score_out_of_100   -- Computed column!
FROM students;

-- Result:
-- name  | gpa | score_out_of_100
-- ------|-----|----------------
-- Alice | 3.8 | 95.0
-- Bob   | 3.2 | 80.0
```

### Selecting Text Literals

```sql
SELECT
    'Student:' AS label,
    name
FROM students;

-- Adds a constant text column to every row
```

### SQL Style Guide

- SQL keywords (`SELECT`, `FROM`, `WHERE`) are conventionally written in UPPERCASE
- Table and column names in lowercase or snake_case
- Each clause on a new line for readability
- End statements with a semicolon `;`
- `--` starts a single-line comment""",

# ────────────────────────────────────────────────

"WHERE Clause": """## Filtering Rows with WHERE

The `WHERE` clause filters which rows are returned. Without it, you get every row. With it, you get only rows that match your condition.

### Basic Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

### Comparison Operators

```sql
-- Equal to:
SELECT * FROM students WHERE gpa = 4.0;

-- Not equal to:
SELECT * FROM students WHERE city != 'Lagos';
SELECT * FROM students WHERE city <> 'Lagos';   -- Same thing

-- Greater than / Less than:
SELECT * FROM students WHERE gpa > 3.5;
SELECT * FROM students WHERE age < 25;
SELECT * FROM students WHERE gpa >= 3.0;
SELECT * FROM students WHERE gpa <= 2.0;
```

### String Comparisons

```sql
-- Exact match (case-sensitive in most databases):
SELECT * FROM students WHERE name = 'Alice';

-- LIKE for pattern matching:
SELECT * FROM students WHERE name LIKE 'A%';    -- Starts with A
SELECT * FROM students WHERE email LIKE '%@gmail.com'; -- Gmail addresses
SELECT * FROM students WHERE city LIKE '%buj%'; -- Contains 'buj'
```

### Working with NULL

`NULL` means "no value" / "unknown". You cannot use `= NULL` to check for NULL — use `IS NULL`:

```sql
-- Find students with no email:
SELECT * FROM students WHERE email IS NULL;

-- Find students who DO have an email:
SELECT * FROM students WHERE email IS NOT NULL;
```

### Combining Conditions with AND/OR/NOT

```sql
-- AND — both conditions must be true:
SELECT * FROM students
WHERE gpa >= 3.5 AND city = 'Lagos';

-- OR — at least one must be true:
SELECT * FROM students
WHERE city = 'Lagos' OR city = 'Abuja';

-- NOT — reverses the condition:
SELECT * FROM students
WHERE NOT city = 'Kano';

-- Combining — use parentheses to control order:
SELECT * FROM students
WHERE (city = 'Lagos' OR city = 'Abuja')
  AND gpa >= 3.0;
```

### IN — Match Against a List

```sql
-- Instead of: WHERE city = 'Lagos' OR city = 'Abuja' OR city = 'Kano'
SELECT * FROM students
WHERE city IN ('Lagos', 'Abuja', 'Kano');

-- Opposite:
SELECT * FROM students
WHERE city NOT IN ('Lagos', 'Abuja');
```

### BETWEEN — Range Checks

```sql
SELECT * FROM students
WHERE gpa BETWEEN 3.0 AND 3.5;  -- Inclusive on both ends

SELECT * FROM orders
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```""",

# ────────────────────────────────────────────────

"ORDER BY & LIMIT": """## Sorting and Limiting Results

Raw query results have no guaranteed order. `ORDER BY` lets you sort them, and `LIMIT` lets you control how many rows are returned.

### ORDER BY — Sorting Results

```sql
-- Sort by a single column (ascending by default):
SELECT name, gpa FROM students
ORDER BY gpa;
-- Alice 3.8, Bob 3.2, Carol 3.9 — NO! Ascending means lowest first
-- Actually: Bob 3.2, Alice 3.8, Carol 3.9

-- Descending order (highest first):
SELECT name, gpa FROM students
ORDER BY gpa DESC;
-- Carol 3.9, Alice 3.8, Bob 3.2
```

### Multiple Sort Columns

If two rows have the same value in the first sort column, the second column breaks the tie:

```sql
SELECT name, city, gpa FROM students
ORDER BY city ASC, gpa DESC;
-- First sorts by city alphabetically
-- Within same city, sorts by gpa from highest to lowest
```

### LIMIT — Cap the Number of Results

```sql
-- Get only the first 5 rows:
SELECT * FROM products
ORDER BY price DESC
LIMIT 5;
-- Returns the 5 most expensive products

-- Get the single most recent order:
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 1;
```

### OFFSET — Pagination

`OFFSET` skips a number of rows — essential for pagination:

```sql
-- Page 1: rows 1-10
SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 0;

-- Page 2: rows 11-20
SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 10;

-- Page 3: rows 21-30
SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 20;

-- Formula: OFFSET = (page_number - 1) * page_size
```

### TOP 5 Pattern — Getting the Best/Worst

```sql
-- Top 5 students by GPA:
SELECT name, gpa
FROM students
ORDER BY gpa DESC
LIMIT 5;

-- 5 cheapest products:
SELECT name, price
FROM products
ORDER BY price ASC
LIMIT 5;

-- Most recent 10 orders:
SELECT id, customer_name, total
FROM orders
ORDER BY created_at DESC
LIMIT 10;
```

### Combining Everything

```sql
-- Find students in Lagos with GPA above 3.0,
-- sorted by GPA highest first,
-- show only top 3:
SELECT name, gpa, city
FROM students
WHERE city = 'Lagos'
  AND gpa > 3.0
ORDER BY gpa DESC
LIMIT 3;
```

### SQL Clause Order (Must Be in This Order)

```sql
SELECT ...
FROM ...
WHERE ...
ORDER BY ...
LIMIT ...;
```""",

# ────────────────────────────────────────────────

"DISTINCT & COUNT": """## Removing Duplicates and Counting Rows

`DISTINCT` eliminates duplicate values from results. `COUNT` tells you how many rows match.

### DISTINCT — Unique Values Only

```sql
-- Without DISTINCT — shows every city (with repeats):
SELECT city FROM students;
-- Lagos, Abuja, Lagos, Kano, Lagos, Abuja

-- With DISTINCT — each city only once:
SELECT DISTINCT city FROM students;
-- Lagos, Abuja, Kano

-- DISTINCT across multiple columns:
SELECT DISTINCT city, level FROM students;
-- Shows unique combinations of city + level
```

### COUNT — How Many Rows?

```sql
-- Count all rows:
SELECT COUNT(*) FROM students;
-- Returns: 150 (or however many students there are)

-- Count rows that match a condition:
SELECT COUNT(*) FROM students WHERE gpa >= 3.5;
-- Returns: 42

-- Count non-NULL values in a specific column:
SELECT COUNT(email) FROM students;
-- Skips NULL values — only counts students who HAVE an email

-- Combine COUNT with DISTINCT:
SELECT COUNT(DISTINCT city) FROM students;
-- How many unique cities do students come from?
```

### Aggregate Functions (Related to COUNT)

These summarize multiple rows into a single value:

```sql
SELECT
    COUNT(*)          AS total_students,
    AVG(gpa)          AS average_gpa,
    MAX(gpa)          AS highest_gpa,
    MIN(gpa)          AS lowest_gpa,
    SUM(tuition_paid) AS total_revenue
FROM students;
```

### COUNT + GROUP BY — Counting per Category

This is extremely powerful — how many students are in each city?

```sql
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city
ORDER BY student_count DESC;

-- Result:
-- city   | student_count
-- -------|-------------
-- Lagos  | 45
-- Abuja  | 32
-- Kano   | 28
-- ...
```

### Practical Examples

```sql
-- How many products in each category?
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;

-- How many orders per customer?
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC
LIMIT 10;  -- Top 10 most active customers
```""",

# ────────────────────────────────────────────────

"Aliases & Expressions": """## Column Aliases and Calculated Fields

SQL lets you rename columns and compute new values directly in your queries.

### Column Aliases with AS

```sql
-- Basic alias — rename a column in the result:
SELECT
    name       AS student_name,
    gpa        AS grade_point,
    created_at AS enrollment_date
FROM students;

-- The original column names are unchanged in the database.
-- AS is optional — you can just put the alias after a space:
SELECT name "Student Name", gpa "Grade Point"   -- Some DBs support this
FROM students;
```

### Table Aliases — Shortening Table Names

Essential when joining multiple tables:

```sql
-- Without alias — verbose:
SELECT students.name, students.gpa
FROM students;

-- With alias — concise:
SELECT s.name, s.gpa
FROM students AS s;
```

### Computed Expressions

```sql
-- Math operations:
SELECT
    name,
    price,
    price * 1.075 AS price_with_tax,  -- Add 7.5% tax
    price * 0.9   AS discounted_price  -- 10% off
FROM products;

-- String operations:
SELECT
    first_name || ' ' || last_name AS full_name,  -- PostgreSQL concatenation
    CONCAT(first_name, ' ', last_name) AS full_name,  -- MySQL/SQL Server
    UPPER(name) AS name_uppercase,
    LOWER(email) AS email_lowercase,
    LENGTH(name) AS name_length
FROM users;

-- Date operations:
SELECT
    name,
    enrolled_at,
    CURRENT_DATE - enrolled_at AS days_enrolled,
    EXTRACT(YEAR FROM enrolled_at) AS enrollment_year
FROM students;
```

### CASE WHEN — Conditional Columns

Like an if/else statement inside SQL:

```sql
SELECT
    name,
    gpa,
    CASE
        WHEN gpa >= 3.7 THEN 'A - Distinction'
        WHEN gpa >= 3.3 THEN 'B - Merit'
        WHEN gpa >= 2.7 THEN 'C - Pass'
        ELSE                 'F - Fail'
    END AS grade_category
FROM students;

-- Result:
-- name  | gpa | grade_category
-- ------|-----|---------------
-- Alice | 3.8 | A - Distinction
-- Bob   | 3.2 | C - Pass

-- CASE as a column:
SELECT
    name,
    CASE WHEN is_active = 1 THEN 'Active' ELSE 'Inactive' END AS status
FROM users;
```""",

# ────────────────────────────────────────────────

"AND, OR, NOT": """## Combining Multiple Conditions

The `AND`, `OR`, and `NOT` logical operators let you build complex filter conditions in `WHERE` clauses.

### AND — Both Must Be True

```sql
-- Returns rows where ALL conditions are true:
SELECT * FROM students
WHERE city = 'Lagos'
  AND gpa >= 3.5
  AND is_active = 1;
-- Only students from Lagos, with high GPA, who are active

-- As many conditions as needed:
SELECT * FROM products
WHERE category = 'Electronics'
  AND price < 50000
  AND stock_count > 0
  AND is_available = 1;
```

### OR — At Least One Must Be True

```sql
-- Returns rows where ANY condition is true:
SELECT * FROM students
WHERE city = 'Lagos'
   OR city = 'Abuja'
   OR city = 'Kano';

-- Equivalent (cleaner) with IN:
SELECT * FROM students
WHERE city IN ('Lagos', 'Abuja', 'Kano');
```

### NOT — Reverses the Condition

```sql
-- Not equal (these are equivalent):
SELECT * FROM students WHERE NOT city = 'Kano';
SELECT * FROM students WHERE city != 'Kano';
SELECT * FROM students WHERE city <> 'Kano';

-- NOT IN:
SELECT * FROM products
WHERE category NOT IN ('Accessories', 'Clearance');

-- NOT LIKE:
SELECT * FROM users
WHERE email NOT LIKE '%@gmail.com';
```

### Combining AND and OR — Be Careful with Precedence!

`AND` has higher precedence than `OR` (like multiplication vs addition). Always use parentheses to be explicit:

```sql
-- WRONG — may not do what you expect:
SELECT * FROM students
WHERE city = 'Lagos' OR city = 'Abuja' AND gpa >= 3.5;
-- Parsed as: Lagos OR (Abuja AND gpa >= 3.5)
-- Gets ALL Lagos students, PLUS Abuja students with high GPA

-- CORRECT — use parentheses:
SELECT * FROM students
WHERE (city = 'Lagos' OR city = 'Abuja') AND gpa >= 3.5;
-- Gets only high-GPA students from EITHER city
```

### Real-World Example

```sql
-- Find high-value customers who haven't ordered recently:
SELECT name, email, total_spent, last_order_date
FROM customers
WHERE total_spent > 100000                        -- High spenders
  AND (
      last_order_date < '2024-01-01'             -- Haven't ordered in 2024
      OR last_order_date IS NULL                  -- Or never ordered!
  )
  AND is_subscribed = 1                           -- Still subscribed
  AND NOT account_status IN ('blocked', 'deleted') -- Active accounts
ORDER BY total_spent DESC;
```""",

# ────────────────────────────────────────────────

"IN & BETWEEN": """## Efficient Range and Set Filtering

`IN` checks if a value matches any in a list. `BETWEEN` checks if a value is within a range. Both are cleaner alternatives to multiple OR conditions.

### IN — Match Against a Set of Values

```sql
-- Without IN:
SELECT * FROM students
WHERE city = 'Lagos' OR city = 'Abuja' OR city = 'Kano' OR city = 'Port Harcourt';

-- With IN (much cleaner):
SELECT * FROM students
WHERE city IN ('Lagos', 'Abuja', 'Kano', 'Port Harcourt');

-- NOT IN — exclude these values:
SELECT * FROM products
WHERE category NOT IN ('Draft', 'Archived', 'Deleted');

-- IN with numbers:
SELECT * FROM orders
WHERE status_code IN (200, 201, 202);   -- Successful orders only
```

### IN with a Subquery

`IN` can also check against the results of another query:

```sql
-- Get students who have submitted assignments:
SELECT name FROM students
WHERE id IN (
    SELECT DISTINCT student_id FROM assignments
    WHERE submitted = 1
);
```

### BETWEEN — Range Checking

`BETWEEN low AND high` is inclusive on both ends (includes the boundary values):

```sql
-- Numbers in a range:
SELECT * FROM students
WHERE gpa BETWEEN 3.0 AND 3.5;
-- Same as: WHERE gpa >= 3.0 AND gpa <= 3.5

SELECT * FROM products
WHERE price BETWEEN 5000 AND 50000;

-- Dates in a range:
SELECT * FROM orders
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';

-- Text range (alphabetical):
SELECT * FROM students
WHERE name BETWEEN 'A' AND 'M';  -- Names starting A through M
```

### NOT BETWEEN

```sql
SELECT * FROM products
WHERE price NOT BETWEEN 0 AND 1000;
-- Gets products that cost more than 1000 OR are negative (shouldn't exist)
-- More practically:
SELECT * FROM products
WHERE price > 1000;
```

### Combining IN and BETWEEN

```sql
SELECT
    name,
    city,
    gpa,
    age
FROM students
WHERE city IN ('Lagos', 'Abuja')           -- From specific cities
  AND gpa BETWEEN 3.0 AND 4.0             -- Passing GPA range
  AND age BETWEEN 18 AND 25               -- Traditional college age
ORDER BY gpa DESC;
```""",

# ────────────────────────────────────────────────

"LIKE Pattern Matching": """## Searching Text with Patterns

`LIKE` lets you search for text that matches a pattern, rather than an exact value. It's essential for searching, autocomplete, and finding data with partial matches.

### The Two Wildcard Characters

- **`%`** — matches any sequence of zero or more characters (like `*` in file searches)
- **`_`** — matches exactly one character

### Basic LIKE Patterns

```sql
-- Starts with 'Al':
SELECT * FROM students WHERE name LIKE 'Al%';
-- Matches: Alice, Albert, Alexandra

-- Ends with '.com':
SELECT * FROM students WHERE email LIKE '%.com';
-- Matches: alice@gmail.com, bob@yahoo.com

-- Contains 'buj' anywhere:
SELECT * FROM students WHERE city LIKE '%buj%';
-- Matches: Abuja, Obuje

-- Exactly 5 characters:
SELECT * FROM students WHERE name LIKE '_____';
-- Matches: Alice, Carol (5 letters each)

-- Second character is 'l':
SELECT * FROM students WHERE name LIKE '_l%';
-- Matches: Alice, Albert (second char is 'l')

-- Starts with 'A' and has exactly 4 more characters:
SELECT * FROM students WHERE name LIKE 'A____';
-- Matches: Alice, Abdul (5 total)
```

### NOT LIKE

```sql
-- Emails NOT from Gmail:
SELECT * FROM users WHERE email NOT LIKE '%@gmail.com';

-- Cities that don't contain spaces:
SELECT DISTINCT city FROM students WHERE city NOT LIKE '% %';
```

### Case Sensitivity

LIKE behavior varies by database:
- **MySQL**: case-insensitive by default
- **PostgreSQL**: case-sensitive; use `ILIKE` for case-insensitive
- **SQLite**: case-insensitive for ASCII by default

```sql
-- PostgreSQL case-insensitive search:
SELECT * FROM students WHERE name ILIKE 'alice';  -- Finds 'Alice', 'ALICE', etc.

-- Standard solution — convert to same case:
SELECT * FROM students WHERE LOWER(name) LIKE LOWER('alice');
```

### Building a Search Feature

```sql
-- User searches for 'python' — search across multiple columns:
SELECT title, description
FROM courses
WHERE title       LIKE '%python%'
   OR description LIKE '%python%'
   OR tags        LIKE '%python%'
ORDER BY
    CASE
        WHEN title LIKE 'python%' THEN 1   -- Exact start gets priority
        WHEN title LIKE '%python%' THEN 2   -- In title gets second
        ELSE 3                              -- In description gets third
    END;
```

### Performance Note

`LIKE '%pattern%'` (leading wildcard) cannot use a standard index — it scans the entire table. For production full-text search, use:
- PostgreSQL: `tsvector` / `FULL TEXT SEARCH`
- MySQL: `FULLTEXT` indexes
- Elasticsearch or Algolia for large-scale search""",

# ────────────────────────────────────────────────

"NULL Handling": """## Working with Missing Data

`NULL` represents the absence of a value — it means "unknown" or "not applicable." NULL is NOT zero, NOT an empty string, NOT false. It's the absence of any value. This has important implications for how you query and handle data.

### The Golden Rule: Use IS NULL, Not = NULL

```sql
-- WRONG — this never returns any rows:
SELECT * FROM students WHERE email = NULL;    -- Always false!
SELECT * FROM students WHERE email != NULL;   -- Also always false!

-- CORRECT:
SELECT * FROM students WHERE email IS NULL;      -- No email recorded
SELECT * FROM students WHERE email IS NOT NULL;  -- Has an email
```

Why? Because NULL = NULL evaluates to NULL (unknown), not TRUE. SQL treats any comparison with NULL as "I don't know."

### NULL in Arithmetic

```sql
-- Any arithmetic with NULL gives NULL:
SELECT 5 + NULL;    -- NULL
SELECT 100 * NULL;  -- NULL
SELECT NULL / 2;    -- NULL

-- This matters! If bonus is NULL, total_comp will also be NULL:
SELECT name, salary + bonus AS total_comp FROM employees;
-- Use COALESCE to handle this:
SELECT name, salary + COALESCE(bonus, 0) AS total_comp FROM employees;
```

### COALESCE — Return the First Non-NULL Value

```sql
-- COALESCE returns the first non-NULL argument:
SELECT COALESCE(NULL, NULL, 'default');  -- Returns 'default'
SELECT COALESCE(NULL, 42, 100);          -- Returns 42

-- Practical: Show 'Not provided' when phone is NULL:
SELECT
    name,
    COALESCE(phone, 'Not provided') AS phone_display
FROM users;

-- Pick the first available contact:
SELECT
    name,
    COALESCE(mobile_phone, work_phone, home_phone, 'No contact') AS best_phone
FROM employees;
```

### NULLIF — Return NULL if Two Values Are Equal

```sql
-- Prevent division by zero:
SELECT total_sales / NULLIF(num_transactions, 0) AS avg_transaction_value
FROM sales_report;
-- If num_transactions is 0, NULLIF returns NULL instead of causing division-by-zero error

-- Treat empty strings as NULL:
SELECT NULLIF(city, '') AS city FROM users;
```

### NULL in COUNT

```sql
-- COUNT(*) counts all rows (including NULL rows):
SELECT COUNT(*) FROM students;          -- All 150 rows

-- COUNT(column) skips NULL values:
SELECT COUNT(email) FROM students;      -- Only the 120 who have emails
SELECT COUNT(phone) FROM students;      -- Only the 90 who have phones
```

### Checking for NULL in GROUP BY

```sql
-- NULL values form their own group in GROUP BY:
SELECT city, COUNT(*) FROM students
GROUP BY city;
-- NULL cities will appear as a separate group (or be excluded from aggregates)
```""",

# ────────────────────────────────────────────────

"Complex Filters": """## Advanced WHERE Clause Patterns

Real-world queries often combine multiple conditions, subqueries, and functions. This lesson shows patterns used in production systems.

### Nested Conditions

```sql
-- Find premium customers who either:
-- 1. Are from major cities and spent > 100k, OR
-- 2. Have loyalty_points > 5000 regardless of city
SELECT customer_id, name, city, total_spent, loyalty_points
FROM customers
WHERE is_active = 1
  AND (
      (city IN ('Lagos', 'Abuja', 'Port Harcourt') AND total_spent > 100000)
      OR loyalty_points > 5000
  )
ORDER BY total_spent DESC;
```

### EXISTS — Check if a Related Record Exists

```sql
-- Find customers who have at least one order:
SELECT c.name, c.email
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.id
);

-- Find products that have NEVER been ordered:
SELECT p.name, p.price
FROM products p
WHERE NOT EXISTS (
    SELECT 1 FROM order_items oi
    WHERE oi.product_id = p.id
);
```

### Filtering with Aggregates in Subqueries

```sql
-- Find students with GPA above the average:
SELECT name, gpa
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students)
ORDER BY gpa DESC;

-- Find the city that has the most students:
SELECT name, city FROM students
WHERE city = (
    SELECT city FROM students
    GROUP BY city
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
```

### Date Filtering Patterns

```sql
-- Orders from the last 30 days:
SELECT * FROM orders
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days';  -- PostgreSQL
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY);   -- MySQL

-- Orders from the current month:
SELECT * FROM orders
WHERE EXTRACT(YEAR FROM created_at) = EXTRACT(YEAR FROM CURRENT_DATE)
  AND EXTRACT(MONTH FROM created_at) = EXTRACT(MONTH FROM CURRENT_DATE);

-- Records created this week:
SELECT * FROM logs
WHERE created_at >= DATE_TRUNC('week', CURRENT_DATE);  -- PostgreSQL
```

### Combining CASE in WHERE (Anti-pattern — Use Carefully)

```sql
-- Avoid this — hard to optimize:
SELECT * FROM orders
WHERE
    CASE
        WHEN status = 'active' THEN total > 1000
        WHEN status = 'vip'    THEN total > 500
        ELSE total > 5000
    END;

-- Better with OR:
SELECT * FROM orders
WHERE (status = 'active' AND total > 1000)
   OR (status = 'vip'    AND total > 500)
   OR (status NOT IN ('active', 'vip') AND total > 5000);
```""",

# ────────────────────────────────────────────────

"INNER JOIN": """## Combining Data from Two Tables

A **JOIN** combines rows from two or more tables based on a related column. This is the heart of relational databases — instead of duplicating data, you store it in separate tables and JOIN them when needed.

### The Setup

```sql
-- Table 1: students
-- id | name  | city_id
-- ---|-------|--------
-- 1  | Alice | 2
-- 2  | Bob   | 1
-- 3  | Carol | 2

-- Table 2: cities
-- id | name   | country
-- ---|--------|--------
-- 1  | Lagos  | Nigeria
-- 2  | Abuja  | Nigeria
-- 3  | Kano   | Nigeria
```

### INNER JOIN — Only Matching Rows

`INNER JOIN` (or just `JOIN`) returns rows where there is a match in BOTH tables:

```sql
SELECT
    students.name AS student_name,
    cities.name   AS city_name,
    cities.country
FROM students
INNER JOIN cities ON students.city_id = cities.id;

-- Result: Only students who have a matching city (all 3 in this example)
-- student_name | city_name | country
-- -------------|-----------|--------
-- Alice        | Abuja     | Nigeria
-- Bob          | Lagos     | Nigeria
-- Carol        | Abuja     | Nigeria
```

### Using Aliases (Standard Practice)

```sql
SELECT
    s.name  AS student,
    c.name  AS city,
    c.country
FROM students s
JOIN cities c ON s.city_id = c.id;  -- JOIN is shorthand for INNER JOIN
```

### Joining Three Tables

```sql
-- students join enrollments join courses:
SELECT
    s.name  AS student,
    c.title AS course,
    e.grade
FROM students s
JOIN enrollments e ON e.student_id = s.id
JOIN courses c     ON e.course_id = c.id
WHERE e.grade >= 70
ORDER BY s.name, c.title;
```

### When INNER JOIN Excludes Rows

Rows without a match in the other table are EXCLUDED:

```sql
-- If a student has city_id = NULL, they won't appear in an INNER JOIN result
-- If a city has no students, it won't appear either
-- Use LEFT JOIN to keep all rows from one side
```

### Filtering After JOIN

```sql
SELECT
    s.name,
    c.title AS course,
    e.grade
FROM students s
JOIN enrollments e ON e.student_id = s.id
JOIN courses c     ON e.course_id = c.id
WHERE c.category = 'Programming'   -- Filter on joined table
  AND e.grade >= 80                 -- Filter on join table
  AND s.city_id = 2                 -- Filter on original table
ORDER BY e.grade DESC;
```""",

# ────────────────────────────────────────────────

"LEFT JOIN": """## Keeping All Rows from the Left Table

`LEFT JOIN` (also `LEFT OUTER JOIN`) returns ALL rows from the left table, plus any matching rows from the right table. If there's no match, the right-side columns show NULL.

### LEFT JOIN vs INNER JOIN

```sql
-- Setup:
-- students: Alice (no orders), Bob (has orders), Carol (has orders)

-- INNER JOIN — excludes Alice (no matching orders):
SELECT s.name, o.total
FROM students s
JOIN orders o ON o.student_id = s.id;
-- Bob | 5000
-- Carol | 3500

-- LEFT JOIN — keeps ALL students:
SELECT s.name, o.total
FROM students s
LEFT JOIN orders o ON o.student_id = s.id;
-- Alice | NULL   (no orders — kept with NULLs on right side)
-- Bob   | 5000
-- Carol | 3500
```

### Finding Rows With No Match — The Anti-Join Pattern

This is one of the most useful LEFT JOIN techniques:

```sql
-- Find students who have NEVER placed an order:
SELECT s.name, s.email
FROM students s
LEFT JOIN orders o ON o.student_id = s.id
WHERE o.id IS NULL;    -- NULL means no matching row was found!

-- Find products never ordered:
SELECT p.name, p.price
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
WHERE oi.id IS NULL;
```

### Counting with LEFT JOIN

```sql
-- Count orders per student (including students with 0 orders):
SELECT
    s.name,
    COUNT(o.id) AS order_count,   -- COUNT(column) returns 0 when NULL!
    COALESCE(SUM(o.total), 0) AS total_spent
FROM students s
LEFT JOIN orders o ON o.student_id = s.id
GROUP BY s.id, s.name
ORDER BY total_spent DESC;

-- Includes students with order_count=0 (unlike INNER JOIN approach)
```

### RIGHT JOIN — The Opposite

`RIGHT JOIN` keeps all rows from the RIGHT table. In practice, you can always rewrite a `RIGHT JOIN` as a `LEFT JOIN` by swapping the tables — so most developers just use `LEFT JOIN` exclusively.

```sql
-- These are equivalent:
SELECT * FROM a LEFT JOIN b ON a.id = b.a_id;
SELECT * FROM b RIGHT JOIN a ON a.id = b.a_id;
```""",

# ────────────────────────────────────────────────

"Multiple Joins": """## Joining Three or More Tables

Real applications need data from many tables at once. You can chain as many JOINs as needed.

### Basic Three-Table Join

```sql
-- Tables: students, enrollments, courses
-- students: id, name, email
-- enrollments: id, student_id, course_id, grade, enrolled_date
-- courses: id, title, instructor_id, category

SELECT
    s.name    AS student,
    c.title   AS course,
    e.grade,
    e.enrolled_date
FROM students s
JOIN enrollments e ON e.student_id = s.id
JOIN courses c     ON c.id = e.course_id
ORDER BY s.name, c.title;
```

### Four Tables — Including the Instructor

```sql
-- Adding: instructors: id, name, specialty

SELECT
    s.name         AS student,
    c.title        AS course,
    i.name         AS instructor,
    e.grade,
    e.enrolled_date
FROM students s
JOIN enrollments e  ON e.student_id = s.id
JOIN courses c      ON c.id = e.course_id
JOIN instructors i  ON i.id = c.instructor_id
WHERE e.grade >= 70
ORDER BY s.name;
```

### Mixing LEFT and INNER JOINs

```sql
-- Get all courses, their enrollment counts, and optionally their category details:
SELECT
    c.title,
    COUNT(e.id)        AS enrolled_students,
    cat.name           AS category_name,     -- May be NULL if category is missing
    cat.description
FROM courses c
LEFT JOIN enrollments e  ON e.course_id = c.id     -- Keep courses with 0 enrollments
LEFT JOIN categories cat ON cat.id = c.category_id -- Keep even if no category
GROUP BY c.id, c.title, cat.name, cat.description
ORDER BY enrolled_students DESC;
```

### Self-Join — Joining a Table to Itself

```sql
-- Find pairs of students in the same city:
SELECT
    a.name AS student_a,
    b.name AS student_b,
    a.city
FROM students a
JOIN students b ON a.city = b.city
               AND a.id < b.id    -- Avoid duplicates (A,B) and (B,A)
ORDER BY a.city, a.name;

-- Find employee-manager relationships:
SELECT
    e.name   AS employee,
    m.name   AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;
```""",

# ────────────────────────────────────────────────

"Self Joins": """## A Table Joining Itself

A **self-join** is when a table is joined to itself. This is used when rows in the same table have relationships with other rows in the same table — like employees who have managers (both in the same `employees` table), or categories that have parent categories.

### Employee-Manager Hierarchy

```sql
-- employees table:
-- id | name    | manager_id | department
-- ---|---------|------------|----------
-- 1  | Alice   | NULL       | CEO
-- 2  | Bob     | 1          | Engineering
-- 3  | Carol   | 2          | Engineering
-- 4  | Dave    | 2          | Engineering
-- 5  | Eve     | 1          | HR

-- Find each employee and their manager:
SELECT
    e.name         AS employee,
    e.department,
    COALESCE(m.name, 'No Manager') AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;

-- Result:
-- Alice | CEO         | No Manager
-- Bob   | Engineering | Alice
-- Carol | Engineering | Bob
-- Dave  | Engineering | Bob
-- Eve   | HR          | Alice
```

### Finding Coworkers

```sql
-- Find pairs of employees who share the same manager:
SELECT
    a.name AS employee1,
    b.name AS employee2,
    a.manager_id
FROM employees a
JOIN employees b ON a.manager_id = b.manager_id
               AND a.id < b.id   -- Avoid (Alice, Bob) AND (Bob, Alice) — get each pair once
WHERE a.manager_id IS NOT NULL;
```

### Category Hierarchy

```sql
-- categories table:
-- id | name        | parent_id
-- ---|-------------|----------
-- 1  | Programming | NULL
-- 2  | Python      | 1
-- 3  | Django      | 2
-- 4  | Design      | NULL
-- 5  | UI          | 4

-- Show each category with its parent:
SELECT
    c.name     AS category,
    COALESCE(p.name, '(root)') AS parent
FROM categories c
LEFT JOIN categories p ON p.id = c.parent_id;
```

### Product Comparison

```sql
-- Find products in the same category with different prices:
SELECT
    a.name  AS product_a,
    b.name  AS product_b,
    a.category,
    a.price AS price_a,
    b.price AS price_b,
    ABS(a.price - b.price) AS price_difference
FROM products a
JOIN products b ON a.category = b.category
               AND a.id < b.id
               AND ABS(a.price - b.price) < 1000  -- Within N1000 of each other
ORDER BY a.category, price_difference;
```""",

# ────────────────────────────────────────────────

"CROSS JOIN & UNION": """## Cartesian Products and Combining Result Sets

### CROSS JOIN — Every Combination

A `CROSS JOIN` returns every possible combination of rows from two tables — the **Cartesian product**. If table A has 5 rows and table B has 3 rows, a CROSS JOIN produces 5 × 3 = 15 rows.

```sql
-- colors: Red, Green, Blue (3 rows)
-- sizes: Small, Medium, Large, XL (4 rows)

SELECT
    c.name AS color,
    s.name AS size
FROM colors c
CROSS JOIN sizes s;

-- Result: 12 rows — every color/size combination:
-- Red   | Small
-- Red   | Medium
-- Red   | Large
-- Red   | XL
-- Green | Small
-- ... (12 total)
```

**Practical Use:** Generating a complete schedule (every day × every room), creating a full product variant matrix.

### UNION — Stacking Results

`UNION` combines the result sets of two or more SELECT statements, **removing duplicates**. `UNION ALL` keeps all rows including duplicates (faster).

**Rules:**
1. Both queries must have the same number of columns
2. Corresponding columns must have compatible data types

```sql
-- Get all contact emails from two different tables:
SELECT email, 'student' AS source FROM students
UNION
SELECT email, 'teacher' AS source FROM teachers
ORDER BY email;
-- Removes any emails that appear in both tables

-- UNION ALL — keep ALL rows (including duplicates):
SELECT email FROM students
UNION ALL
SELECT email FROM teachers;
-- May have duplicates if same email is in both tables

-- Count unique people across both tables:
SELECT COUNT(*) FROM (
    SELECT email FROM students
    UNION            -- UNION deduplicates
    SELECT email FROM teachers
) AS all_contacts;
```

### INTERSECT — Rows in Both Queries

```sql
-- Find emails that appear in BOTH students AND teachers:
SELECT email FROM students
INTERSECT
SELECT email FROM teachers;
```

### EXCEPT — Rows in First But Not Second

```sql
-- Find students who are NOT also teachers:
SELECT email FROM students
EXCEPT
SELECT email FROM teachers;
```""",

# ────────────────────────────────────────────────

"GROUP BY": """## Aggregating Data by Category

`GROUP BY` divides rows into groups and applies aggregate functions (COUNT, SUM, AVG, MAX, MIN) to each group separately. Instead of one aggregate for the whole table, you get one per group.

### Basic Concept

```sql
-- Without GROUP BY — one result for the whole table:
SELECT COUNT(*) FROM students;   -- 150

-- With GROUP BY — one result per city:
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city;

-- Result:
-- city    | student_count
-- --------|-------------
-- Lagos   | 45
-- Abuja   | 32
-- Kano    | 28
-- Ibadan  | 20
-- (others)
```

### Multiple Aggregate Functions

```sql
SELECT
    city,
    COUNT(*)     AS total_students,
    AVG(gpa)     AS avg_gpa,
    MAX(gpa)     AS top_gpa,
    MIN(gpa)     AS lowest_gpa,
    SUM(tuition) AS total_tuition
FROM students
GROUP BY city
ORDER BY total_students DESC;
```

### Grouping by Multiple Columns

```sql
-- Count students per city per year:
SELECT
    city,
    EXTRACT(YEAR FROM enrolled_at) AS year,
    COUNT(*) AS student_count
FROM students
GROUP BY city, EXTRACT(YEAR FROM enrolled_at)
ORDER BY city, year;
```

### The Golden Rule: SELECT Columns Must Be in GROUP BY

Any column in `SELECT` that is NOT an aggregate function MUST appear in `GROUP BY`:

```sql
-- WRONG — name is not in GROUP BY:
SELECT name, city, COUNT(*)   -- ❌ What name to show for 45 Lagos students?
FROM students
GROUP BY city;

-- CORRECT — everything in SELECT is either aggregated or grouped:
SELECT city, COUNT(*) AS count
FROM students
GROUP BY city;
```

### HAVING — Filter Groups

`HAVING` filters the groups created by `GROUP BY`, just like `WHERE` filters rows. Key difference:
- `WHERE` filters individual rows **before** grouping
- `HAVING` filters groups **after** aggregation

```sql
-- Cities with more than 30 students:
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city
HAVING COUNT(*) > 30;

-- Courses with average grade above 75:
SELECT course_id, AVG(grade) AS avg_grade
FROM enrollments
GROUP BY course_id
HAVING AVG(grade) > 75
ORDER BY avg_grade DESC;
```

### WHERE + GROUP BY + HAVING

```sql
-- Among active students (WHERE),
-- grouped by city (GROUP BY),
-- show only cities with high average GPA (HAVING):
SELECT city, AVG(gpa) AS avg_gpa, COUNT(*) AS count
FROM students
WHERE is_active = 1                  -- Filter rows first
GROUP BY city                         -- Then group
HAVING AVG(gpa) >= 3.0               -- Then filter groups
   AND COUNT(*) >= 5                  -- At least 5 students
ORDER BY avg_gpa DESC;
```""",

# ────────────────────────────────────────────────

"HAVING Clause": """## Filtering Groups After Aggregation

`HAVING` works like `WHERE` but applies to groups created by `GROUP BY`. It's the only way to filter based on aggregate values.

### WHERE vs HAVING — The Key Distinction

```sql
-- WHERE filters BEFORE grouping (individual rows):
SELECT city, COUNT(*) AS count
FROM students
WHERE gpa >= 3.0           -- Keep only high-GPA students first
GROUP BY city;

-- HAVING filters AFTER grouping (groups):
SELECT city, COUNT(*) AS count, AVG(gpa) AS avg_gpa
FROM students
GROUP BY city
HAVING AVG(gpa) >= 3.0;   -- Keep only cities where the AVERAGE is high

-- Combining both:
SELECT city, COUNT(*) AS count, AVG(gpa) AS avg_gpa
FROM students
WHERE is_active = 1         -- WHERE: only active students
GROUP BY city
HAVING COUNT(*) > 10        -- HAVING: only cities with more than 10 students
   AND AVG(gpa) >= 3.0;    -- HAVING: with a high average GPA
```

### HAVING Without GROUP BY

Technically you can use HAVING without GROUP BY (treats entire table as one group), but it's unusual:

```sql
SELECT AVG(gpa) FROM students
HAVING AVG(gpa) >= 3.0;   -- Returns the average only if >= 3.0, otherwise no rows
```

### Practical Examples

```sql
-- Products that have been ordered more than 100 times:
SELECT
    p.name,
    COUNT(oi.id) AS times_ordered,
    SUM(oi.quantity) AS units_sold
FROM products p
JOIN order_items oi ON oi.product_id = p.id
GROUP BY p.id, p.name
HAVING COUNT(oi.id) > 100
ORDER BY units_sold DESC;

-- Instructors whose students average above 80:
SELECT
    i.name AS instructor,
    COUNT(DISTINCT e.student_id) AS students,
    AVG(e.grade) AS avg_student_grade
FROM instructors i
JOIN courses c ON c.instructor_id = i.id
JOIN enrollments e ON e.course_id = c.id
GROUP BY i.id, i.name
HAVING AVG(e.grade) >= 80
   AND COUNT(DISTINCT e.student_id) >= 10  -- At least 10 students
ORDER BY avg_student_grade DESC;

-- Customers who spent between 50,000 and 500,000:
SELECT
    customer_id,
    COUNT(*) AS orders,
    SUM(total) AS lifetime_value
FROM orders
GROUP BY customer_id
HAVING SUM(total) BETWEEN 50000 AND 500000
ORDER BY lifetime_value DESC;
```""",

# ────────────────────────────────────────────────

"Queries inside Queries": """## Subqueries — SQL within SQL

A **subquery** (or subselect, nested query) is a SELECT statement nested inside another SQL statement. The inner query runs first, and its result is used by the outer query.

### Scalar Subquery — Returns One Value

```sql
-- Find students with GPA above the overall average:
SELECT name, gpa
FROM students
WHERE gpa > (
    SELECT AVG(gpa)    -- Inner query returns one number
    FROM students
)
ORDER BY gpa DESC;

-- Find the most expensive product:
SELECT * FROM products
WHERE price = (
    SELECT MAX(price) FROM products
);
```

### Row Subquery — Returns One Row

```sql
-- Find the student with the highest GPA:
SELECT name, gpa, city
FROM students
WHERE (gpa, city) = (
    SELECT MAX(gpa), city
    FROM students
    WHERE city = 'Lagos'
    LIMIT 1
);
```

### Table Subquery — Returns Multiple Rows (IN)

```sql
-- Find students enrolled in any Python course:
SELECT DISTINCT s.name, s.email
FROM students s
WHERE s.id IN (
    SELECT e.student_id
    FROM enrollments e
    JOIN courses c ON c.id = e.course_id
    WHERE c.title LIKE '%Python%'
);

-- Find products never ordered:
SELECT name, price FROM products
WHERE id NOT IN (
    SELECT DISTINCT product_id
    FROM order_items
    WHERE product_id IS NOT NULL  -- Important: NOT IN breaks with NULLs!
);
```

### Derived Table (FROM Subquery)

```sql
-- Subquery in FROM — creates a temporary table:
SELECT
    city_stats.city,
    city_stats.avg_gpa,
    city_stats.student_count
FROM (
    SELECT
        city,
        AVG(gpa) AS avg_gpa,
        COUNT(*) AS student_count
    FROM students
    GROUP BY city
) AS city_stats               -- Must give it an alias!
WHERE city_stats.student_count >= 10
ORDER BY city_stats.avg_gpa DESC;
```

### Correlated Subquery — References the Outer Query

```sql
-- For each student, find their rank within their city:
SELECT
    s1.name,
    s1.city,
    s1.gpa,
    (SELECT COUNT(*) + 1
     FROM students s2
     WHERE s2.city = s1.city      -- Correlated: references outer query's s1
       AND s2.gpa > s1.gpa) AS rank_in_city
FROM students s1
ORDER BY s1.city, rank_in_city;
```""",

# ────────────────────────────────────────────────

"Entity-Relationship (ER)": """## Designing Your Database Before Writing It

An **Entity-Relationship (ER) diagram** is a blueprint for your database. It shows what data you're storing (**entities**), what properties they have (**attributes**), and how they relate to each other (**relationships**). Good database design prevents data problems later.

### Core Concepts

- **Entity** — A thing you want to store data about (Student, Course, Order)
- **Attribute** — A property of an entity (Student has: name, email, gpa)
- **Relationship** — How entities are connected (Students ENROLL IN Courses)
- **Primary Key** — A unique identifier for each row (usually `id`)
- **Foreign Key** — A column that references another table's primary key

### Types of Relationships

**One-to-Many (1:N)** — The most common. One customer has many orders.
```sql
CREATE TABLE customers (
    id      INTEGER PRIMARY KEY,
    name    TEXT NOT NULL,
    email   TEXT UNIQUE NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),  -- Foreign key!
    total       DECIMAL(10, 2),
    created_at  TIMESTAMP DEFAULT NOW()
);
-- One customer → many orders
-- Many orders → one customer each
```

**Many-to-Many (M:N)** — Requires a junction/bridge table.
```sql
-- Students can enroll in many courses
-- Courses can have many students

CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE courses  (id INTEGER PRIMARY KEY, title TEXT);

-- Junction table — bridges students and courses:
CREATE TABLE enrollments (
    student_id INTEGER REFERENCES students(id),
    course_id  INTEGER REFERENCES courses(id),
    enrolled_at TIMESTAMP DEFAULT NOW(),
    grade       DECIMAL(5, 2),
    PRIMARY KEY (student_id, course_id)  -- Composite primary key
);
```

**One-to-One (1:1)** — Rare. Used to split a large table.
```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);
CREATE TABLE user_profiles (
    user_id     INTEGER PRIMARY KEY REFERENCES users(id),  -- 1:1 relationship
    bio         TEXT,
    avatar_url  TEXT,
    social_links JSONB
);
```

### Normalization — Avoiding Redundancy

The goal of normalization is to store each fact exactly once:

❌ **Bad design:**
```
orders: id | customer_name | customer_email | product_name | product_price | quantity
```
- Customer data duplicated in every order
- If customer email changes, must update many rows

✅ **Good design — normalized:**
```
customers: id | name | email
products:  id | name | price
orders:    id | customer_id | created_at
order_items: id | order_id | product_id | quantity | price_at_time
```""",

# ────────────────────────────────────────────────

"Database Speed": """## Indexes — Making Queries Fast

An **index** is a separate data structure that the database maintains to speed up lookups. Without an index, every query must scan every row in the table (a "full table scan"). With an index, the database can jump directly to the relevant rows.

### The Problem Without Indexes

```sql
-- With 10 million rows, this scans all 10M rows every time:
SELECT * FROM orders WHERE customer_id = 12345;
-- Takes seconds. With an index: milliseconds.
```

### Creating Indexes

```sql
-- Basic index on a single column:
CREATE INDEX idx_orders_customer_id ON orders(customer_id);

-- Now this query uses the index — extremely fast:
SELECT * FROM orders WHERE customer_id = 12345;

-- Unique index — also enforces uniqueness:
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Composite index (covers queries filtering on multiple columns):
CREATE INDEX idx_orders_status_created ON orders(status, created_at);
-- Helps queries like:
SELECT * FROM orders WHERE status = 'pending' ORDER BY created_at;
```

### When to Add an Index

✅ **Add an index when:**
- You frequently query `WHERE column = value`
- The column is used in `JOIN ON` conditions
- The column is frequently used in `ORDER BY`
- The table has many rows (> 10,000) and queries are slow

❌ **Don't add an index when:**
- The table is small (full scan is fast enough)
- The column has very few distinct values (e.g., a boolean — only 2 values)
- The table has many writes — each index slows down INSERT/UPDATE/DELETE

### Checking if an Index is Being Used

```sql
-- PostgreSQL:
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 12345;
-- Look for "Index Scan" — means the index is used
-- "Seq Scan" (Sequential Scan) means a full table scan — may need an index

-- MySQL:
EXPLAIN SELECT * FROM orders WHERE customer_id = 12345;
-- Look at the 'key' column — shows which index was used
```

### Primary Key Index

Every primary key automatically gets a unique index — that's why `SELECT * FROM table WHERE id = 5` is always fast.

### Index Types

```sql
-- B-Tree index (default) — good for <, >, =, BETWEEN, LIKE 'prefix%':
CREATE INDEX idx_gpa ON students(gpa);

-- GIN index — good for arrays, JSON, full-text search:
CREATE INDEX idx_tags ON products USING gin(tags);

-- GiST index — good for geographic data, geometric shapes:
CREATE INDEX idx_location ON places USING gist(geom);
```""",

# ────────────────────────────────────────────────

"Code in the Database": """## Stored Procedures — Reusable SQL Logic

A **stored procedure** is a named, reusable block of SQL code stored directly in the database. Instead of sending complex SQL from your application every time, you call the procedure by name, and the database executes it.

### Why Use Stored Procedures?

- **Performance** — Pre-compiled by the database, faster for complex operations
- **Security** — Grant access to the procedure without granting direct table access
- **Code Reuse** — Complex logic defined once, called from many places
- **Reduced Network Traffic** — One call instead of many queries

### PostgreSQL Stored Procedure

```sql
-- Create a procedure to enroll a student in a course:
CREATE OR REPLACE PROCEDURE enroll_student(
    p_student_id INTEGER,
    p_course_id  INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if already enrolled:
    IF EXISTS (
        SELECT 1 FROM enrollments
        WHERE student_id = p_student_id AND course_id = p_course_id
    ) THEN
        RAISE EXCEPTION 'Student % is already enrolled in course %',
            p_student_id, p_course_id;
    END IF;
    
    -- Check if course has capacity:
    IF (SELECT enrolled_count FROM courses WHERE id = p_course_id)
       >= (SELECT max_capacity FROM courses WHERE id = p_course_id) THEN
        RAISE EXCEPTION 'Course % is full', p_course_id;
    END IF;
    
    -- Enroll the student:
    INSERT INTO enrollments (student_id, course_id, enrolled_at)
    VALUES (p_student_id, p_course_id, NOW());
    
    -- Update enrolled count:
    UPDATE courses SET enrolled_count = enrolled_count + 1
    WHERE id = p_course_id;
    
    COMMIT;
END;
$$;

-- Call the procedure:
CALL enroll_student(42, 7);
```

### SQL Functions (Return a Value)

```sql
-- A function that calculates a student's letter grade:
CREATE OR REPLACE FUNCTION get_grade_letter(p_score DECIMAL)
RETURNS TEXT
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_score >= 70 THEN RETURN 'A';
    ELSIF p_score >= 60 THEN RETURN 'B';
    ELSIF p_score >= 50 THEN RETURN 'C';
    ELSIF p_score >= 45 THEN RETURN 'D';
    ELSE RETURN 'F';
    END IF;
END;
$$;

-- Use in a query like any built-in function:
SELECT student_id, grade, get_grade_letter(grade) AS letter_grade
FROM enrollments;
```""",

# ────────────────────────────────────────────────

"EXPLAIN": """## Understanding Query Performance with EXPLAIN

`EXPLAIN` (and `EXPLAIN ANALYZE`) shows you the **query execution plan** — exactly how the database decided to retrieve your data. It's the essential tool for diagnosing slow queries.

### Basic EXPLAIN

```sql
-- Shows the PLAN without actually running the query:
EXPLAIN SELECT * FROM students WHERE gpa > 3.5;

-- Sample output (PostgreSQL):
-- Seq Scan on students  (cost=0.00..25.00 rows=500 width=200)
--   Filter: (gpa > 3.5)

-- "Seq Scan" = sequential scan = reading every row = NO index used
```

### EXPLAIN ANALYZE — Run It and Measure

```sql
-- Actually runs the query and shows real timing:
EXPLAIN ANALYZE SELECT * FROM students WHERE gpa > 3.5;

-- Output:
-- Seq Scan on students (cost=0.00..25.00 rows=500 width=200)
--                      (actual time=0.042..12.345 rows=478 loops=1)
--   Filter: (gpa > 3.5)
--   Rows Removed by Filter: 22
-- Planning Time: 0.15 ms
-- Execution Time: 12.89 ms  ← Actual time!
```

### Reading the Output

| Term | Meaning |
|---|---|
| `Seq Scan` | Full table scan — no index used |
| `Index Scan` | Used an index — fast! |
| `Index Only Scan` | Data found entirely in the index — fastest! |
| `Bitmap Index Scan` | Used index then fetched rows in bulk |
| `Hash Join` | Join using a hash table |
| `Nested Loop` | Join by looping — fast for small tables |
| `Merge Join` | Join on pre-sorted data |
| `cost=X..Y` | Estimated startup..total cost |
| `rows=N` | Estimated number of rows |
| `actual time=X..Y` | Actual startup..total time in ms |

### Comparing With and Without Index

```sql
-- Before adding index:
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 12345;
-- Seq Scan  → Execution Time: 456.78 ms  (slow!)

CREATE INDEX idx_orders_customer ON orders(customer_id);

-- After adding index:
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 12345;
-- Index Scan → Execution Time: 0.12 ms  (3800x faster!)
```

### Common Performance Problems

```sql
-- 1. Missing index — use CREATE INDEX
-- 2. Unused index — the planner chose Seq Scan anyway (too many matching rows)

-- 3. Inefficient function use — can't use index:
EXPLAIN SELECT * FROM students WHERE LOWER(email) = 'alice@x.com';
-- Creates an expression index to fix this:
CREATE INDEX idx_email_lower ON students(LOWER(email));

-- 4. N+1 problem — use JOINs instead of queries in loops
```""",

# ────────────────────────────────────────────────

"Document Databases": """## NoSQL — A Different Way to Store Data

While SQL databases store data in structured tables with strict schemas, **NoSQL** databases use flexible formats. **Document databases** (like MongoDB) store data as JSON-like documents — each record can have different fields.

### SQL vs Document Database

```
SQL (structured, fixed schema):
┌─────────────────────────────────────┐
│ id | name  | age | city  | phone   │
│ 1  | Alice | 25  | Lagos | NULL    │
│ 2  | Bob   | 30  | Abuja | 0812... │
└─────────────────────────────────────┘

MongoDB (flexible documents):
{ "_id": 1, "name": "Alice", "age": 25, "city": "Lagos" }
{ "_id": 2, "name": "Bob", "age": 30, "phone": "0812...", "tags": ["vip", "active"] }
```

Each document can have completely different fields. No schema migration needed when you add new fields.

### MongoDB Basics

```javascript
// MongoDB uses JavaScript-like syntax

// Insert one document:
db.students.insertOne({
    name: "Alice",
    age: 25,
    gpa: 3.8,
    courses: ["Python", "SQL", "ML"],  // Arrays natively supported!
    address: {                          // Nested documents!
        city: "Lagos",
        state: "Lagos State"
    }
})

// Insert many:
db.students.insertMany([
    { name: "Bob",   gpa: 3.2 },
    { name: "Carol", gpa: 3.9 }
])
```

### When to Use Document Databases

✅ **Good for:**
- Data with varying structure (user profiles with optional fields)
- Hierarchical data (a document with nested addresses, tags, items)
- Rapidly evolving schemas (startup with changing requirements)
- High-volume read/write operations with simpler queries
- Content management systems, catalogs, logs

❌ **Not ideal for:**
- Complex relationships between entities (use SQL)
- Transactions across multiple documents (SQL does this better)
- Heavy aggregation and reporting workloads""",

# ────────────────────────────────────────────────

"Finding Documents": """## Querying MongoDB

MongoDB's `find()` is like SQL's SELECT WHERE. Instead of SQL syntax, you pass a JSON filter object.

### Basic Find

```javascript
// Find all documents:
db.students.find()               // Like: SELECT * FROM students

// Find with a filter:
db.students.find({ city: "Lagos" })   // WHERE city = 'Lagos'

// Find one document:
db.students.findOne({ name: "Alice" })

// Projection — select specific fields (1=include, 0=exclude):
db.students.find(
    { city: "Lagos" },      // Filter
    { name: 1, gpa: 1 }     // Projection — only name and gpa
)
// Like: SELECT name, gpa FROM students WHERE city = 'Lagos'
```

### Comparison Operators

```javascript
// Greater than, less than:
db.students.find({ gpa: { $gt: 3.5 } })    // gpa > 3.5
db.students.find({ gpa: { $gte: 3.0 } })   // gpa >= 3.0
db.students.find({ gpa: { $lt: 2.0 } })    // gpa < 2.0
db.students.find({ age: { $ne: 25 } })     // age != 25

// IN — match any value in a list:
db.students.find({ city: { $in: ["Lagos", "Abuja", "Kano"] } })

// BETWEEN equivalent:
db.students.find({ gpa: { $gte: 3.0, $lte: 3.5 } })
```

### Logical Operators

```javascript
// AND (implicit when multiple conditions):
db.students.find({ city: "Lagos", gpa: { $gte: 3.5 } })

// Explicit AND:
db.students.find({
    $and: [
        { city: "Lagos" },
        { gpa: { $gte: 3.5 } }
    ]
})

// OR:
db.students.find({
    $or: [
        { city: "Lagos" },
        { gpa: { $gte: 3.8 } }
    ]
})
```

### Sorting and Limiting

```javascript
// Sort by GPA descending, limit to top 5:
db.students.find()
           .sort({ gpa: -1 })    // -1 = descending, 1 = ascending
           .limit(5)

// Pagination:
db.students.find()
           .sort({ name: 1 })
           .skip(20)     // Skip 20 (page 3 if limit=10)
           .limit(10)
```

### Querying Nested Fields and Arrays

```javascript
// Nested field (dot notation):
db.students.find({ "address.city": "Lagos" })

// Array contains a value:
db.students.find({ courses: "Python" })   // students enrolled in Python

// Array with all values:
db.students.find({ tags: { $all: ["vip", "active"] } })
```""",

# ────────────────────────────────────────────────

"FULL OUTER JOIN": """## Including Unmatched Rows from Both Tables

A `FULL OUTER JOIN` (or `FULL JOIN`) returns all rows from both tables, with NULLs where there's no match on either side. It's the combination of LEFT JOIN and RIGHT JOIN.

### Comparison of Join Types

```
Table A:          Table B:          Result:
Alice (1)         (1) Django        LEFT JOIN: Alice+Django, Bob+NULL
Bob   (2)         (3) React         RIGHT JOIN: Alice+Django, NULL+React
                                    INNER JOIN: Alice+Django
                                    FULL JOIN: Alice+Django, Bob+NULL, NULL+React
```

### FULL OUTER JOIN Syntax

```sql
SELECT
    s.name  AS student,
    c.title AS course
FROM students s
FULL OUTER JOIN courses c ON c.student_id = s.id;

-- Returns:
-- All students (even with no courses) — NULLs on right
-- All courses (even with no students) — NULLs on left
```

### Practical Use Case: Finding Gaps in Both Directions

```sql
-- Find all students with no courses AND all courses with no students:
SELECT
    s.name                               AS student,
    c.title                              AS course,
    CASE
        WHEN s.id IS NULL THEN 'Course has no students'
        WHEN c.id IS NULL THEN 'Student has no courses'
        ELSE 'Enrolled'
    END AS status
FROM students s
FULL OUTER JOIN enrollments e ON e.student_id = s.id
FULL OUTER JOIN courses c ON c.id = e.course_id
WHERE s.id IS NULL OR c.id IS NULL;  -- Only show the gaps
```

### Emulating FULL JOIN in MySQL

MySQL doesn't support FULL OUTER JOIN — use UNION:

```sql
-- MySQL equivalent:
SELECT s.name, c.title
FROM students s
LEFT JOIN courses c ON c.student_id = s.id

UNION

SELECT s.name, c.title
FROM students s
RIGHT JOIN courses c ON c.student_id = s.id;
```""",

# ────────────────────────────────────────────────

"Window Functions": """## Analytics Without Losing Individual Rows

**Window functions** perform calculations across a set of rows **related to the current row**, without collapsing them into groups like `GROUP BY` does. They're incredibly powerful for ranking, running totals, and moving averages.

### Window Function Syntax

```sql
function_name() OVER (
    PARTITION BY column   -- Like GROUP BY but doesn't collapse rows
    ORDER BY column       -- How to order within each partition
    ROWS/RANGE ...        -- Optional: which rows to include
)
```

### ROW_NUMBER, RANK, DENSE_RANK

```sql
-- Rank students by GPA within each city:
SELECT
    name,
    city,
    gpa,
    ROW_NUMBER()  OVER (PARTITION BY city ORDER BY gpa DESC) AS row_num,
    RANK()        OVER (PARTITION BY city ORDER BY gpa DESC) AS rank,
    DENSE_RANK()  OVER (PARTITION BY city ORDER BY gpa DESC) AS dense_rank
FROM students;

-- Difference with ties (both scored 3.8):
-- ROW_NUMBER: 1, 2, 3    (no ties — arbitrary order within)
-- RANK:       1, 1, 3    (skip 2 after tie)
-- DENSE_RANK: 1, 1, 2    (no gaps after tie)
```

### Running Totals

```sql
-- Running total of sales by date:
SELECT
    sale_date,
    daily_amount,
    SUM(daily_amount) OVER (ORDER BY sale_date) AS running_total
FROM daily_sales;

-- Running total within each product category:
SELECT
    product_id,
    category,
    sale_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY category
        ORDER BY sale_date
    ) AS category_running_total
FROM sales;
```

### LAG and LEAD — Comparing to Adjacent Rows

```sql
-- Compare each day's sales to the previous day:
SELECT
    sale_date,
    daily_amount,
    LAG(daily_amount, 1) OVER (ORDER BY sale_date) AS yesterday_amount,
    daily_amount - LAG(daily_amount, 1) OVER (ORDER BY sale_date) AS change
FROM daily_sales;

-- Compare to next day:
SELECT
    sale_date,
    daily_amount,
    LEAD(daily_amount, 1) OVER (ORDER BY sale_date) AS tomorrow_amount
FROM daily_sales;
```

### Top N Per Group — Classic Window Function Use

```sql
-- Top 3 students per city:
SELECT * FROM (
    SELECT
        name, city, gpa,
        RANK() OVER (PARTITION BY city ORDER BY gpa DESC) AS rank_in_city
    FROM students
) ranked
WHERE rank_in_city <= 3;
```""",

# ────────────────────────────────────────────────

"BEGIN and COMMIT": """## Transactions — All or Nothing

A **transaction** is a sequence of SQL operations that are treated as a single unit of work. Either ALL of them succeed, or NONE of them are applied. This is essential for maintaining data integrity.

### The Problem Without Transactions

```sql
-- Bank transfer: debit Alice, credit Bob
UPDATE accounts SET balance = balance - 500 WHERE name = 'Alice';
-- Server crashes here!
UPDATE accounts SET balance = balance + 500 WHERE name = 'Bob';

-- Alice lost 500, Bob never got it. Money disappeared!
```

### With Transactions

```sql
BEGIN;   -- Start the transaction

UPDATE accounts SET balance = balance - 500 WHERE name = 'Alice';
UPDATE accounts SET balance = balance + 500 WHERE name = 'Bob';

COMMIT;  -- Make both changes permanent (only if both succeed)

-- If anything fails between BEGIN and COMMIT, use ROLLBACK to undo everything:
```

### COMMIT — Making Changes Permanent

```sql
BEGIN;

INSERT INTO orders (customer_id, total) VALUES (42, 5000);
INSERT INTO order_items (order_id, product_id, quantity) VALUES (LASTVAL(), 7, 2);
UPDATE products SET stock = stock - 2 WHERE id = 7;

COMMIT;   -- All three changes written to disk permanently
```

### ROLLBACK — Undoing Everything

```sql
BEGIN;

UPDATE accounts SET balance = balance - 1000 WHERE id = 1;

-- Oops! Something went wrong:
ROLLBACK;   -- balance reverts to original — no change made

-- In application code:
BEGIN;
-- ...SQL operations...
-- If any fails:
ROLLBACK;
-- If all succeed:
COMMIT;
```

### ACID Properties

| Property | Meaning |
|---|---|
| **A**tomicity | All or nothing — partial changes never persist |
| **C**onsistency | Transaction brings DB from valid state to valid state |
| **I**solation | Concurrent transactions don't interfere with each other |
| **D**urability | Committed changes survive crashes/restarts |

### Savepoints — Partial Rollback

```sql
BEGIN;

INSERT INTO orders VALUES (...);
SAVEPOINT order_created;   -- Checkpoint

INSERT INTO payments VALUES (...);
-- If payment fails:
ROLLBACK TO SAVEPOINT order_created;  -- Only undo payment, keep order

COMMIT;   -- Order is saved, no payment recorded
```""",

# ────────────────────────────────────────────────

"ROLLBACK": """## Undoing Changes When Things Go Wrong

`ROLLBACK` cancels all changes made in the current transaction, reverting the database to its state before `BEGIN`. It's your safety net when something goes wrong.

### When to Use ROLLBACK

```sql
-- Explicit rollback when you detect an error:
BEGIN;

UPDATE inventory SET quantity = quantity - 10 WHERE product_id = 5;

-- Check if we went negative:
SELECT quantity FROM inventory WHERE product_id = 5;
-- If quantity is now -3 (we didn't have 10):

ROLLBACK;   -- Undo the deduction — quantity restored to original value
```

### ROLLBACK in Application Code (Python/SQLAlchemy)

```python
from sqlalchemy.orm import Session

def transfer_funds(db: Session, from_id: int, to_id: int, amount: float):
    try:
        # Debit
        sender = db.query(Account).filter_by(id=from_id).first()
        if sender.balance < amount:
            raise ValueError('Insufficient funds')
        sender.balance -= amount
        
        # Credit
        receiver = db.query(Account).filter_by(id=to_id).first()
        receiver.balance += amount
        
        db.commit()   # All good — make it permanent
        print(f'Transferred {amount} successfully')
        
    except Exception as e:
        db.rollback()   # Something failed — undo everything!
        print(f'Transfer failed: {e}')
        raise
```

### Automatic Rollback on Error

Most databases automatically roll back if an error occurs mid-transaction:

```sql
BEGIN;

INSERT INTO orders VALUES (1, 42, 5000);   -- Success

INSERT INTO order_items VALUES (1, 999, 2);
-- ERROR: Foreign key constraint — product 999 doesn't exist!
-- Database automatically rolls back the entire transaction!
-- The order INSERT is also undone.
```

### When NOT to Use ROLLBACK

Once you've done `COMMIT`, you cannot ROLLBACK that commit. Committed data is permanent. If you need to undo it, you must do a new UPDATE/DELETE to reverse the changes.

### TRUNCATE vs DELETE in Transactions

```sql
-- DELETE is transactional — can be rolled back:
BEGIN;
DELETE FROM test_data;
ROLLBACK;   -- All rows restored!

-- TRUNCATE in PostgreSQL IS transactional too:
BEGIN;
TRUNCATE test_data;
ROLLBACK;   -- Rows restored (PostgreSQL specific)

-- In MySQL, TRUNCATE auto-commits — cannot be rolled back!
```""",

# ────────────────────────────────────────────────

"JSONB Columns": """## Storing JSON in PostgreSQL

PostgreSQL's `JSONB` type stores JSON data in a binary format that supports indexing and efficient querying. It's the best of both worlds — the flexibility of NoSQL within a relational database.

### Creating a JSONB Column

```sql
CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    price       DECIMAL(10, 2),
    metadata    JSONB           -- Flexible attributes stored as JSON
);

-- Insert with JSON data:
INSERT INTO products (name, price, metadata) VALUES
('Laptop Pro X', 899.99, '{
    "brand": "TechCo",
    "specs": {
        "ram_gb": 16,
        "storage_gb": 512,
        "display": "15.6 inch"
    },
    "tags": ["electronics", "computers", "featured"],
    "in_stock": true
}'),
('Wireless Headphones', 149.99, '{
    "brand": "AudioMax",
    "color_options": ["black", "white", "blue"],
    "wireless": true,
    "battery_hours": 40
}');
```

### Querying JSONB

```sql
-- Access a field with -> (returns JSON) or ->> (returns text):
SELECT name, metadata->>'brand' AS brand FROM products;
SELECT name, metadata->'specs'->>'ram_gb' AS ram FROM products;

-- Filter by a JSONB field:
SELECT * FROM products
WHERE metadata->>'brand' = 'TechCo';

-- Filter by a nested value:
SELECT * FROM products
WHERE (metadata->'specs'->>'ram_gb')::int >= 16;

-- Check if key exists:
SELECT * FROM products WHERE metadata ? 'wireless';

-- Check if value is in an array:
SELECT * FROM products
WHERE metadata->'tags' ? 'featured';

-- Check if object contains another:
SELECT * FROM products
WHERE metadata @> '{"brand": "TechCo"}';
```

### Indexing JSONB

```sql
-- GIN index for efficient JSON queries:
CREATE INDEX idx_products_metadata ON products USING gin(metadata);

-- This makes @>, ?, ?|, ?& operators fast!
```

### Updating JSONB

```sql
-- Update a specific key using jsonb_set:
UPDATE products
SET metadata = jsonb_set(metadata, '{in_stock}', 'false')
WHERE id = 1;

-- Add a new key:
UPDATE products
SET metadata = metadata || '{"warranty_years": 2}'::jsonb
WHERE id = 1;

-- Remove a key:
UPDATE products
SET metadata = metadata - 'old_field'
WHERE id = 1;
```""",

# ────────────────────────────────────────────────

"Roles and Permissions": """## Database Security with Roles

Database roles control who can do what. Proper permissions prevent unauthorized access, accidental data deletion, and security breaches.

### Creating Users and Roles

```sql
-- Create a new database user:
CREATE USER alice WITH PASSWORD 'SecurePass123!';

-- Create a role (like a group — users can be assigned to roles):
CREATE ROLE read_only;
CREATE ROLE app_user;
CREATE ROLE admin_role;
```

### Granting Permissions

```sql
-- GRANT privilege ON object TO user/role:

-- Read-only access to a specific table:
GRANT SELECT ON students TO read_only;

-- Full access to one table:
GRANT SELECT, INSERT, UPDATE, DELETE ON orders TO app_user;

-- Access to all tables in a schema:
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only;

-- Execute a stored procedure:
GRANT EXECUTE ON PROCEDURE enroll_student TO app_user;

-- Assign a role to a user:
GRANT read_only TO alice;
GRANT app_user TO app_service_account;
```

### Revoking Permissions

```sql
-- Remove specific privileges:
REVOKE DELETE ON students FROM app_user;

-- Remove all privileges:
REVOKE ALL ON students FROM alice;

-- Remove role membership:
REVOKE read_only FROM alice;
```

### Principle of Least Privilege

Always grant the minimum necessary permissions:

```sql
-- Application database user (for your FastAPI/Django app):
CREATE USER app_service WITH PASSWORD 'StrongPassword!';
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO app_service;
-- Note: NOT DELETE — prevent accidental data loss from app bugs

-- Read-only analytics user:
CREATE USER analyst WITH PASSWORD 'AnalystPass!';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;

-- Admin (for DBA only — not the application):
CREATE USER dba_admin WITH PASSWORD 'SuperSecurePass!';
GRANT ALL PRIVILEGES ON DATABASE myapp TO dba_admin;
```

### Row-Level Security (RLS) — Advanced

```sql
-- Enable RLS on a table:
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Customers can only see their own orders:
CREATE POLICY customer_orders ON orders
    FOR SELECT
    USING (customer_id = current_setting('app.current_user_id')::int);
```""",

# ────────────────────────────────────────────────

"Star Schema": """## Data Warehouse Design with Star Schema

A **star schema** is the standard design pattern for analytical databases (data warehouses). Unlike OLTP (transaction processing) databases which are normalized, star schemas are intentionally denormalized for fast analytical queries.

### Star Schema Components

- **Fact Table** — The center of the star. Contains measurable events (sales, page views, orders). Has many rows. Contains numeric measures and foreign keys to dimension tables.
- **Dimension Tables** — The points of the star. Describe the "who, what, when, where" of the facts (customers, products, dates, locations).

### Example: Sales Data Warehouse

```sql
-- FACT TABLE: one row per sale event
CREATE TABLE fact_sales (
    sale_id         BIGINT PRIMARY KEY,
    date_id         INTEGER REFERENCES dim_date(date_id),
    customer_id     INTEGER REFERENCES dim_customer(customer_id),
    product_id      INTEGER REFERENCES dim_product(product_id),
    store_id        INTEGER REFERENCES dim_store(store_id),
    -- Measures (the numbers we analyze):
    quantity_sold   INTEGER,
    sale_amount     DECIMAL(12, 2),
    discount_amount DECIMAL(12, 2),
    profit          DECIMAL(12, 2)
);

-- DIMENSION: Date (allows filtering/grouping by any date part)
CREATE TABLE dim_date (
    date_id     INTEGER PRIMARY KEY,
    full_date   DATE,
    year        INTEGER,
    quarter     INTEGER,
    month       INTEGER,
    month_name  TEXT,
    week        INTEGER,
    day_of_week TEXT,
    is_weekend  BOOLEAN,
    is_holiday  BOOLEAN
);

-- DIMENSION: Product
CREATE TABLE dim_product (
    product_id  INTEGER PRIMARY KEY,
    product_name TEXT,
    category    TEXT,
    subcategory TEXT,
    brand       TEXT,
    unit_cost   DECIMAL(10, 2)
);
```

### Querying a Star Schema

```sql
-- Monthly sales by product category:
SELECT
    d.year,
    d.month_name,
    p.category,
    SUM(f.sale_amount) AS total_sales,
    SUM(f.profit)      AS total_profit,
    COUNT(DISTINCT f.customer_id) AS unique_customers
FROM fact_sales f
JOIN dim_date     d ON d.date_id     = f.date_id
JOIN dim_product  p ON p.product_id  = f.product_id
WHERE d.year = 2024
GROUP BY d.year, d.month, d.month_name, p.category
ORDER BY d.month, total_sales DESC;
```""",

# ────────────────────────────────────────────────

"Materialized Views": """## Caching Query Results as Tables

A **materialized view** is a pre-computed query whose results are stored as a real table. Unlike a regular view (which runs the query every time you query it), a materialized view stores the results and only refreshes them on demand. Excellent for expensive analytical queries.

### Regular View vs Materialized View

```sql
-- Regular VIEW — query runs every time:
CREATE VIEW student_stats AS
SELECT city, COUNT(*) AS count, AVG(gpa) AS avg_gpa
FROM students
GROUP BY city;

SELECT * FROM student_stats;   -- Runs the GROUP BY query NOW

-- MATERIALIZED VIEW — stored results, refreshed manually:
CREATE MATERIALIZED VIEW student_stats_mat AS
SELECT city, COUNT(*) AS count, AVG(gpa) AS avg_gpa
FROM students
GROUP BY city;
-- The query runs ONCE during creation, results are stored.

SELECT * FROM student_stats_mat;   -- Reads from stored table — FAST!
```

### Creating and Refreshing

```sql
-- Create the materialized view:
CREATE MATERIALIZED VIEW monthly_sales_summary AS
SELECT
    EXTRACT(YEAR FROM o.created_at)  AS year,
    EXTRACT(MONTH FROM o.created_at) AS month,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    COUNT(DISTINCT o.customer_id)    AS unique_buyers
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
JOIN products p     ON p.id = oi.product_id
GROUP BY 1, 2, 3;

-- Add an index to make queries on it fast:
CREATE INDEX ON monthly_sales_summary (year, month, category);

-- Query it instantly (even if underlying data has millions of rows):
SELECT * FROM monthly_sales_summary
WHERE year = 2024 AND month = 6
ORDER BY total_revenue DESC;

-- Refresh when underlying data changes:
REFRESH MATERIALIZED VIEW monthly_sales_summary;
-- You can run this via a cron job (e.g., nightly at 2am)

-- Refresh without locking (allows reads during refresh):
REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales_summary;
-- Requires a UNIQUE index to use CONCURRENTLY
```

### When to Use Materialized Views

✅ **Use when:**
- A query takes seconds or minutes to run
- Results don't need to be real-time (okay if slightly stale)
- Query is run frequently (dashboard that refreshes every minute)

❌ **Avoid when:**
- Data must always be completely current
- The underlying data changes very frequently
- The query is already fast""",

}

# ════════════════════════════════════════════════
# VERSION CONTROL
# ════════════════════════════════════════════════
GIT_THEORY = {

"What is Git?": """## The World's Most Popular Version Control System

**Git** is a distributed version control system (VCS) — a tool that tracks every change to your code over time, allowing you to see what changed, when, and who changed it. More importantly, it lets you experiment freely because you can always roll back to any previous state.

### The Problem Git Solves

Without version control:
- You rename files to `project_v1.py`, `project_v2.py`, `project_FINAL.py`, `project_REALLY_FINAL.py`
- You accidentally delete working code with no way to get it back
- You can't collaborate — two people editing the same file causes conflicts

With Git:
- Every state of your code is saved permanently
- You can try risky changes in a "branch" without breaking the main code
- Multiple people can work on the same project simultaneously

### Core Concepts

| Concept | What It Is |
|---|---|
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | A saved snapshot of your code at a point in time |
| **Branch** | An independent line of development |
| **Merge** | Combining changes from two branches |
| **Clone** | Making a copy of a repository |
| **Remote** | A copy of the repo on a server (e.g., GitHub) |

### Installing and Setting Up

```bash
# Check if Git is installed:
git --version

# Set your identity (used in every commit you make):
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Set your default editor (optional):
git config --global core.editor "code --wait"  # VS Code

# View all config:
git config --list
```

### Creating Your First Repository

```bash
# Create a new project:
mkdir my-project
cd my-project
git init          # Creates a hidden .git folder — your repo is born!

# Or clone an existing repo from GitHub:
git clone https://github.com/username/repo-name.git
cd repo-name
```

### The Three States of Git

```
Working Directory → Staging Area → Repository (commits)

You edit files    You stage files  You commit files
(untracked,       (git add)        (git commit)
modified)
```

Every file in a Git repo is in one of these states. Understanding this flow is the key to understanding Git.""",

# ────────────────────────────────────────────────

"Staging & Committing": """## Saving Your Work — The Add/Commit Cycle

In Git, saving your work is a two-step process: **staging** (choosing what to include) and **committing** (permanently recording it). This two-step process lets you carefully control exactly what goes into each commit.

### The Workflow

```bash
# 1. Check status — see what's changed:
git status
# Shows: untracked files, modified files, staged files

# 2. Stage files — move changes to the staging area:
git add filename.py         # Stage one specific file
git add folder/             # Stage all files in a folder
git add .                   # Stage ALL changes in current directory
git add -p                  # Interactive staging — choose specific changes

# 3. Commit — permanently save the snapshot:
git commit -m "Add user authentication feature"

# Shortcut — stage all tracked files AND commit:
git commit -am "Fix login bug"   # Only works for already-tracked files
```

### Understanding `git status` Output

```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:   ← Staged (in staging area)
  (use "git restore --staged <file>..." to unstage)
    new file: auth.py
    modified: database.py

Changes not staged for commit:  ← Modified but NOT staged
  (use "git add <file>..." to update what will be committed)
    modified: main.py

Untracked files:   ← New files Git doesn't know about yet
  (use "git add <file>..." to include in what will be committed)
    tests/test_auth.py
```

### What Makes a Good Commit?

A commit is a permanent record. Future you (and your teammates) will read these.

```bash
# ❌ Bad commit messages:
git commit -m "fix"
git commit -m "changes"
git commit -m "WIP"
git commit -m "asdfgh"

# ✅ Good commit messages — describe WHAT and WHY:
git commit -m "Add email validation to registration form"
git commit -m "Fix crash when user has no profile picture"
git commit -m "Refactor database connection to use connection pool"
git commit -m "Update dependencies to fix security vulnerability"
```

### Unstaging Files

```bash
# Oops, staged the wrong file:
git restore --staged filename.py    # Unstage (keep changes in working dir)
git restore filename.py             # Discard changes entirely (DESTRUCTIVE!)
```

### Viewing Commit History

```bash
git log                      # Full history
git log --oneline            # Compact — one line per commit
git log --oneline --graph    # With branch visualization
git log -5                   # Last 5 commits
git log --author="Alice"     # Commits by Alice
```""",

# ────────────────────────────────────────────────

"Git Diff": """## Seeing Exactly What Changed

`git diff` shows the exact line-by-line differences between versions of your files. It's how you review your changes before committing.

### Basic diff Commands

```bash
# See changes NOT yet staged (working dir vs staging):
git diff

# See changes that ARE staged (staging vs last commit):
git diff --staged
git diff --cached    # Same thing

# See all changes since last commit (staged + unstaged):
git diff HEAD

# Compare two commits:
git diff abc1234..def5678

# Compare two branches:
git diff main..feature-branch

# Compare a specific file:
git diff main..feature-branch -- README.md
```

### Reading the Diff Output

```diff
diff --git a/auth.py b/auth.py
index 3a2c4f1..9b8e2f3 100644
--- a/auth.py          ← Old version (a)
+++ b/auth.py          ← New version (b)
@@ -10,7 +10,10 @@   ← Line numbers: old 10-16, new 10-19
 def login(email, password):
-    user = db.get_user(email)      ← Red/minus: REMOVED line
-    if user.password == password:   ← Red/minus: REMOVED line
+    user = db.query(User).filter_by(email=email).first()  ← Green/plus: ADDED
+    if not user:                    ← Green/plus: ADDED
+        return None                 ← Green/plus: ADDED
+    if user.check_password(password):   ← Green/plus: ADDED
         return create_session(user)
```

### Diffing Specific Things

```bash
# What changed in the last commit?
git diff HEAD~1 HEAD          # HEAD~1 = one commit before HEAD

# What changed in the last 3 commits?
git diff HEAD~3 HEAD

# Did a specific file change between branches?
git diff main feature-branch -- models.py

# See only which files changed (not the content):
git diff --name-only HEAD~1 HEAD
git diff --stat HEAD~1 HEAD   # Also shows how many lines changed
```

### Visual Diff Tools

```bash
# Configure a graphical diff tool:
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'

# Launch the visual diff:
git difftool
```""",

# ────────────────────────────────────────────────

"Ignoring Files": """## Telling Git What NOT to Track

Not everything in your project folder should be committed to Git. The `.gitignore` file tells Git which files and directories to ignore completely.

### What to Ignore

- **Virtual environments** — `venv/`, `.env/`, `node_modules/`
- **Compiled files** — `*.pyc`, `__pycache__/`, `*.class`, `dist/`
- **Sensitive data** — `.env` (API keys, passwords), `secrets.json`
- **IDE/editor files** — `.vscode/`, `.idea/`, `*.swp`
- **OS files** — `.DS_Store` (macOS), `Thumbs.db` (Windows)
- **Build outputs** — `build/`, `dist/`, `*.egg-info/`
- **Logs** — `*.log`, `logs/`
- **Database files** — `*.db`, `*.sqlite3` (for development DBs)

### Creating a .gitignore File

```bash
# Create in your project root:
touch .gitignore
```

```gitignore
# Python project .gitignore

# Virtual environments
venv/
.venv/
env/

# Python compiled files
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
*.so

# Environment variables / Secrets — NEVER commit these!
.env
.env.local
.env.production
secrets.json

# Database
*.db
*.sqlite3

# IDE
.vscode/
.idea/
*.swp
*~

# OS files
.DS_Store
Thumbs.db

# Test coverage
.coverage
htmlcov/
.pytest_cache/

# Build
dist/
build/
*.egg-info/
```

### Pattern Syntax

```gitignore
# Exact filename:
.env

# All files with extension:
*.log

# Specific directory:
node_modules/

# Files in any subdirectory:
**/secrets.json

# Exception — track this despite the above rule:
!important.log

# Ignore everything in a folder but keep the folder itself:
uploads/*
!uploads/.gitkeep
```

### Checking if a File is Ignored

```bash
git check-ignore -v filename    # Shows WHY a file is ignored

# See all ignored files:
git status --ignored
```

### Untracking Already-Committed Files

If you accidentally committed something that should be ignored:

```bash
# Remove from Git tracking (keep the local file):
git rm --cached .env
echo ".env" >> .gitignore
git commit -m "Stop tracking .env file"
```""",

# ────────────────────────────────────────────────

"Git Config": """## Customizing Your Git Experience

`git config` stores settings at three levels: system (all users), global (your user), and local (the current repo). Most of your personal settings live in `~/.gitconfig` (global).

### The Three Config Levels

```bash
# System — affects all users on the machine:
git config --system ...

# Global — affects all your repositories:
git config --global ...

# Local — affects only the current repository:
git config --local ...

# Local overrides global, which overrides system
```

### Essential Configuration

```bash
# Your identity (required for commits):
git config --global user.name "Alice Johnson"
git config --global user.email "alice@digitalera.com"

# Default branch name (use 'main' instead of 'master'):
git config --global init.defaultBranch main

# Default editor for commit messages:
git config --global core.editor "code --wait"   # VS Code
git config --global core.editor "vim"           # Vim
git config --global core.editor "nano"          # Nano

# Line endings (important for cross-platform teams):
# On Windows:
git config --global core.autocrlf true
# On Mac/Linux:
git config --global core.autocrlf input

# Colorful output:
git config --global color.ui auto
```

### Aliases — Shortcuts for Common Commands

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm "commit -m"
git config --global alias.unstage "restore --staged"
git config --global alias.last "log -1 HEAD"
git config --global alias.lg "log --oneline --graph --all"

# Now you can use:
git st          # Instead of: git status
git co main     # Instead of: git checkout main
git lg          # Beautiful branch graph
```

### Viewing and Editing Config

```bash
# View all settings:
git config --list

# View a specific setting:
git config user.email

# View the raw config file:
cat ~/.gitconfig

# Edit the config file directly:
git config --global --edit
```

### A Well-Configured ~/.gitconfig

```ini
[user]
    name = Alice Johnson
    email = alice@digitalera.com

[init]
    defaultBranch = main

[core]
    editor = code --wait
    autocrlf = input

[color]
    ui = auto

[alias]
    st = status
    co = checkout
    lg = log --oneline --graph --all --decorate
    undo = reset HEAD~1 --mixed

[pull]
    rebase = false  # Use merge strategy for pulls
```""",

# ────────────────────────────────────────────────

"Writing Good Commits": """## The Art of Meaningful Commit Messages

A commit message is a permanent note to your future self and your teammates. A year from now, when you're debugging a weird bug, a good commit message is the difference between "Ah, this is why!" and "What on earth was I thinking?!"

### The 7 Rules of Great Commit Messages

1. Separate subject from body with a blank line
2. Limit the subject to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject ("Add feature", not "Added feature")
6. Wrap the body at 72 characters
7. Use the body to explain WHAT and WHY, not HOW

### Commit Message Format

```
Short summary (max 50 chars)
[blank line]
More detailed explanation if needed. Wrap at 72 characters.
Explain the problem this commit is solving.
Explain WHY you chose this solution.
Note any side effects or important changes.

Closes #123
Related to #456
```

### Examples

```bash
# ❌ Bad — describes nothing:
git commit -m "fix bug"
git commit -m "changes to auth"
git commit -m "WIP"

# ✅ Good — one clear change:
git commit -m "Fix crash when user has no profile picture"

# ✅ Good — with body explaining why:
git commit -m "Increase session timeout from 30min to 2hrs

Users were frequently losing their work when sessions expired
during long editing sessions. 2 hours matches our competitors
and should significantly reduce support tickets.

Closes #234"

# ✅ Good — clear action verbs:
git commit -m "Add rate limiting to login endpoint"
git commit -m "Remove deprecated payment_v1 API endpoint"
git commit -m "Refactor user service to use repository pattern"
git commit -m "Update dependencies: Django 4.1 → 4.2"
git commit -m "Fix typo in welcome email subject line"
```

### Conventional Commits Standard

Many teams use this structured format:

```
type(scope): description

feat(auth): add Google OAuth login
fix(api): handle null values in user search
docs(readme): update installation instructions
style(ui): fix button alignment on mobile
refactor(db): extract query builder to separate class
test(auth): add unit tests for token expiry
chore(deps): bump requests from 2.28 to 2.31
perf(search): add index to speed up product search
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`""",

# ────────────────────────────────────────────────

"Git Log": """## Exploring Project History

`git log` is your window into the entire history of the project. Learning to read and filter it efficiently is a crucial Git skill.

### Basic Log Commands

```bash
# Full log (press q to quit):
git log

# Compact — one line per commit:
git log --oneline

# Beautiful graph showing branches:
git log --oneline --graph --all --decorate

# Last N commits:
git log -5
git log --oneline -10

# With file changes:
git log --stat            # Shows which files changed + line counts
git log --patch           # Full diff of every commit (very verbose)
git log --patch -2        # Full diff of last 2 commits
```

### Filtering Log

```bash
# By author:
git log --author="Alice"
git log --author="alice@example.com"

# By date:
git log --since="2024-01-01"
git log --until="2024-12-31"
git log --since="2 weeks ago"
git log --after="yesterday"

# By commit message (contains text):
git log --grep="login"
git log --grep="fix" --oneline

# By file — history of a specific file:
git log -- auth.py
git log --oneline -- src/models/user.py

# Commits that changed a specific line/function:
git log -S "def login"   # Commits that added/removed "def login"
git log -G "password"    # Commits where diff matches this regex
```

### Viewing a Specific Commit

```bash
# Show full details of a commit:
git show abc1234

# Show just the changes to one file in a commit:
git show abc1234:src/auth.py

# Show what a file looked like at a specific commit:
git show abc1234:filename.py

# Show the commit that last changed each line:
git blame filename.py    # Shows commit hash + author for each line
```

### Useful Log Aliases

```bash
# Add these to your ~/.gitconfig:
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.lp "log --oneline --patch"
git config --global alias.ls "log --stat --oneline"

# Usage:
git lg    # Beautiful branch graph
git ls    # What files changed in each commit
```""",

# ────────────────────────────────────────────────

"Amending Commits": """## Fixing Your Most Recent Commit

`git commit --amend` lets you modify the most recent commit — change the message, add forgotten files, or remove accidentally staged files.

### Amending the Commit Message

```bash
# You just committed with a typo in the message:
git commit -m "Aad user authentication"

# Fix it immediately:
git commit --amend -m "Add user authentication"

# Or open your editor to edit it:
git commit --amend
# Your editor opens with the current message — edit and save to update
```

### Adding Forgotten Files

```bash
# You committed, then realized you forgot to include a file:

git add forgotten_file.py
git commit --amend --no-edit    # --no-edit keeps the same commit message
# The forgotten_file.py is now part of the original commit

# Or stage and amend in one step:
git add forgotten_file.py && git commit --amend --no-edit
```

### ⚠️ The Golden Rule of Amending

**NEVER amend a commit that has already been pushed to a shared remote!**

`--amend` rewrites history — it creates a NEW commit with a different hash and replaces the old one. If others have pulled the old commit, their history diverges from yours. This causes major problems.

```bash
# ✅ SAFE — amend commits that are ONLY local (not yet pushed):
git commit -m "some commit"
git commit --amend -m "better message"
git push origin main    # Now push the corrected commit

# ❌ DANGEROUS — amend commits that are already on the remote:
git push origin main
git commit --amend -m "better message"    # This changes history!
git push origin main --force              # NEVER do this on shared branches!
```

### Amending Older Commits — Interactive Rebase

For commits older than the most recent, use `git rebase -i`:

```bash
git rebase -i HEAD~3   # Open interactive rebase for last 3 commits

# In the editor, change 'pick' to 'reword' for commits to rename:
pick abc123 Old message 1
reword def456 Old message 2    ← Will prompt for new message
pick ghi789 Old message 3
```""",

# ────────────────────────────────────────────────

"Cherry-pick": """## Applying Specific Commits to Another Branch

`git cherry-pick` copies a specific commit (or range of commits) from one branch and applies it to your current branch. It's like saying "I want exactly that one change from that branch."

### When to Use Cherry-pick

- A bug fix was committed to a feature branch but you need it on `main` right now
- A specific improvement exists on a long-running branch you don't want to merge yet
- You accidentally committed something to the wrong branch

### Basic Cherry-pick

```bash
# First, find the commit hash you want:
git log --oneline feature-branch
# 9a3b2c1 Fix critical login vulnerability
# 8f2e1d0 Add new dashboard feature
# 7c1d0e5 Refactor database connection

# Switch to the branch you want to add the commit to:
git checkout main

# Apply that specific commit:
git cherry-pick 9a3b2c1
# Git applies the changes from that commit to main
# A new commit is created on main with the same changes but a NEW hash
```

### Cherry-picking a Range

```bash
# Apply commits from abc to def (inclusive):
git cherry-pick abc..def

# Apply multiple specific commits:
git cherry-pick abc123 def456 ghi789
```

### Cherry-pick with Conflicts

```bash
# If there are merge conflicts:
git cherry-pick 9a3b2c1
# CONFLICT: merge conflict in auth.py

# Fix the conflicts in your editor, then:
git add auth.py
git cherry-pick --continue    # Finalize the cherry-pick

# Or abort if it's too messy:
git cherry-pick --abort       # Restores the branch to its previous state
```

### Important: Use Sparingly

Cherry-pick creates duplicate commits (same changes, different hash) in your history. If you later merge the original branch, Git may apply the changes twice or cause conflicts.

Prefer:
- `git merge` for regularly merging feature branches
- `git rebase` for keeping a linear history
- Cherry-pick only for specific urgent situations (hotfixes)""",

# ────────────────────────────────────────────────

"Stashing Changes": """## Temporarily Saving Uncommitted Work

`git stash` is like a clipboard for your uncommitted changes. When you need to switch context quickly (e.g., urgent bug to fix) without committing half-finished work, stash saves your changes so you can return to them later.

### Basic Stash

```bash
# You're halfway through a feature and need to switch branches:
git status
# modified: feature.py
# modified: utils.py

# Save everything to the stash (like a clipboard):
git stash
git stash push -m "WIP: half-done user profile feature"   # With a message

# Now your working directory is clean:
git status
# nothing to commit, working tree clean

# Switch to fix the urgent bug:
git checkout main
git checkout -b hotfix/login-crash
# ...fix the bug, commit it...

# Return to your feature work:
git checkout feature/user-profile

# Retrieve your stashed changes:
git stash pop          # Apply and REMOVE from stash (most common)
# or:
git stash apply        # Apply but KEEP in stash (for multiple use)
```

### Managing Multiple Stashes

```bash
# View all stashes:
git stash list
# stash@{0}: WIP on feature: abc1234 Add profile photo
# stash@{1}: WIP on hotfix: def5678 Fix login crash

# Apply a specific stash:
git stash apply stash@{1}

# Show what's in a stash:
git stash show stash@{0}
git stash show -p stash@{0}    # Full diff

# Delete a specific stash:
git stash drop stash@{1}

# Clear ALL stashes:
git stash clear
```

### Stashing Specific Files

```bash
# Stash only specific files:
git stash push -m "Save only utils" utils.py helpers.py

# Stash untracked files too (new files):
git stash -u
git stash --include-untracked

# Stash everything including ignored files:
git stash -a
git stash --all
```

### Creating a Branch from a Stash

```bash
# Create a new branch and apply the stash to it:
git stash branch new-branch stash@{0}
# Checks out the commit where the stash was created,
# applies the stash, and drops it on success
```""",

# ────────────────────────────────────────────────

"Creating Branches": """## Working in Parallel with Branches

A **branch** is an independent line of development. The default branch is usually `main` (or `master`). You create new branches to work on features, fixes, or experiments without touching the main code — and merge them back when ready.

### Why Branch?

- `main` always stays stable and deployable
- Each feature/fix gets its own isolated workspace
- Multiple developers can work in parallel without interfering
- Experiments can be discarded without affecting the main codebase

### Creating and Switching Branches

```bash
# See all branches (current branch has *):
git branch
# * main
#   feature/user-profile
#   hotfix/login-crash

# Create a new branch:
git branch feature/user-auth

# Switch to it:
git checkout feature/user-auth

# Create AND switch in one command (most common):
git checkout -b feature/user-auth
# or (modern syntax):
git switch -c feature/user-auth

# Switch back to main:
git checkout main
git switch main
```

### Branch Naming Conventions

```bash
# Descriptive, lowercase, hyphenated:
git checkout -b feature/add-email-verification
git checkout -b fix/login-crash-on-mobile
git checkout -b chore/update-dependencies
git checkout -b hotfix/sql-injection-vulnerability
git checkout -b release/v2.0.0

# Common prefixes:
# feature/ — new functionality
# fix/     — bug fixes
# hotfix/  — urgent production fixes
# chore/   — maintenance (deps, cleanup)
# docs/    — documentation only
# refactor/— code improvement, no new features
# test/    — adding tests
```

### Deleting Branches

```bash
# Delete a branch (after merging):
git branch -d feature/user-auth       # Safe — only deletes if merged
git branch -D feature/user-auth       # Force delete (even if not merged)

# Delete a remote branch:
git push origin --delete feature/user-auth
```

### Listing Remote Branches

```bash
git branch -r           # Remote branches only
git branch -a           # All branches (local + remote)
git branch -v           # Verbose — show last commit on each branch
```""",

# ────────────────────────────────────────────────

"Branch Strategies": """## Organizing Your Team's Development Workflow

A **branching strategy** is a set of rules about what branches to create, what they're for, and how they flow together. It keeps collaborative development organized.

### GitHub Flow — Simple, Recommended for Most Teams

```
main ──────●─────●──────────────●──────●──→
           ↑     ↑              ↑      ↑
           │     │              │      │
feature-a  └─●─●─┘              │      │
feature-b          └─●─●─●─●─●─┘      │
hotfix                                 └─●─┘
```

**Rules:**
1. `main` is always deployable — never break it
2. All work happens on feature branches
3. Open a Pull Request when ready
4. Get code review before merging
5. Merge to main and deploy immediately

```bash
# GitHub Flow workflow:
git checkout main
git pull origin main                           # Get latest

git checkout -b feature/add-search             # New feature branch
# ...work, commit, commit, commit...
git push origin feature/add-search             # Push to remote

# Open Pull Request on GitHub/GitLab
# Get code review
# CI/CD passes
# Merge to main
# Deploy
```

### Git Flow — For Projects with Scheduled Releases

```
main     ──●────────────────────●────────────────●──→
           │                    ↑                ↑
develop  ──●────●────●────●────●────●────●────●──→
           │    ↑    ↑         ↑              ↑
feature-a  └─●─●┘   │         │              │
feature-b            └─●─●─●──┘              │
release                                      ●─●─→
```

**Branches:**
- `main` — production-ready code only
- `develop` — integration branch for features
- `feature/*` — individual features (branch from develop)
- `release/*` — release preparation (branch from develop)
- `hotfix/*` — urgent production fixes (branch from main)

### Trunk-Based Development — For Advanced CI/CD Teams

All developers commit directly to `main` (or very short-lived branches):
- Feature flags control which features are "on" for users
- Requires excellent test coverage and CI/CD
- Used by Google, Facebook, Netflix""",

# ────────────────────────────────────────────────

"Switching Context": """## Moving Between Branches Safely

Switching branches changes the files in your working directory to match the state of that branch. Git is smart about it, but you need to handle uncommitted changes before switching.

### Basic Context Switching

```bash
# See what branch you're on:
git status
git branch

# Switch to an existing branch:
git checkout feature/user-auth
git switch feature/user-auth      # Modern syntax (Git 2.23+)

# Create and switch in one step:
git checkout -b new-feature
git switch -c new-feature          # Modern syntax
```

### Handling Uncommitted Changes When Switching

If you have uncommitted changes and try to switch branches, Git will:

1. **Allow the switch** — if the changes don't conflict with the target branch
2. **Block the switch** — if there would be conflicts and it might lose your work

```bash
# Option 1: Commit your changes before switching:
git add .
git commit -m "WIP: half-done feature"
git checkout main

# Option 2: Stash your changes:
git stash
git checkout main
# ...do other work...
git checkout feature/user-auth
git stash pop

# Option 3: Discard changes (DESTRUCTIVE!):
git restore .        # Discard all modifications
git checkout main
```

### Switching to a Remote Branch

```bash
# A colleague pushed a branch — how do you switch to it?

# First, fetch all remote branches:
git fetch origin

# Then checkout (Git creates a local tracking branch automatically):
git checkout feature/colleague-work
# or:
git switch feature/colleague-work

# Check which remote branch you're tracking:
git branch -vv
```

### The Detached HEAD State

```bash
# You can checkout a specific commit (not a branch):
git checkout abc1234

# Now you're in "detached HEAD" state — not on any branch!
# Changes made here are easily lost.
# To save work from here, create a branch:
git checkout -b new-branch-from-commit

# Or just go back to a branch:
git checkout main
```""",

# ────────────────────────────────────────────────

"Remote Branches": """## Collaborating via Remote Repositories

A **remote** is a copy of your repository on a server (like GitHub, GitLab, or Bitbucket). `origin` is the conventional name for the primary remote (the one you cloned from).

### Pushing to Remote

```bash
# Push your branch to the remote for the first time:
git push origin feature/user-auth

# Push (if tracking is already set up — after first push):
git push

# Force push (DANGER — overwrites remote history):
git push --force                    # Dangerous
git push --force-with-lease         # Safer — fails if remote has new commits

# Set default remote for current branch:
git push -u origin feature/user-auth    # -u sets up tracking
# After this, just 'git push' works
```

### Fetching and Pulling

```bash
# fetch — download remote changes WITHOUT merging:
git fetch origin
# Remote branches are updated but your local branches are untouched
# Lets you inspect before merging

# pull — fetch AND merge into current branch:
git pull origin main
git pull        # If tracking is set up

# pull with rebase (cleaner history):
git pull --rebase origin main
```

### Tracking Remote Branches

```bash
# See which remote branch each local branch tracks:
git branch -vv
# * feature/auth     abc1234 [origin/feature/auth: ahead 2] Add OAuth
#   main             def5678 [origin/main] Update README

# 'ahead 2' means you have 2 commits not pushed yet
# 'behind 3' means remote has 3 commits you haven't pulled

# Set tracking for an existing branch:
git branch -u origin/main main
```

### Viewing and Managing Remotes

```bash
# List remotes:
git remote -v
# origin  https://github.com/you/repo.git (fetch)
# origin  https://github.com/you/repo.git (push)

# Add a remote:
git remote add upstream https://github.com/original/repo.git

# Remove a remote:
git remote remove old-remote

# Change remote URL:
git remote set-url origin https://github.com/new-url/repo.git
```

### Syncing with the Original Repository (Forks)

```bash
# When you've forked a repo and want to stay up to date:
git remote add upstream https://github.com/original-author/repo.git
git fetch upstream
git merge upstream/main    # or: git rebase upstream/main
```""",

# ────────────────────────────────────────────────

"Branch Cleanup": """## Keeping Your Repository Tidy

Over time, repositories accumulate old branches that have been merged or abandoned. Regular cleanup keeps the repo manageable and confusing lists of branches from cluttering your work.

### Deleting Local Branches

```bash
# Delete a merged branch (safe — fails if not merged):
git branch -d feature/user-auth

# Force delete (even if not merged):
git branch -D feature/abandoned-experiment

# List branches that have been merged into main:
git branch --merged main
# These are safe to delete

# Delete all locally merged branches:
git branch --merged main | grep -v "\* main" | xargs git branch -d
```

### Deleting Remote Branches

```bash
# Delete a branch on the remote:
git push origin --delete feature/old-feature
git push origin :feature/old-feature    # Old syntax (same effect)

# If GitHub shows branches as "deleted" but they still show locally:
git fetch --prune    # Remove local references to deleted remote branches
git fetch -p         # Short form
```

### Pruning Stale Remote-Tracking Branches

```bash
# Remote branch was deleted but your local still shows it:
git branch -r                        # Shows remote tracking branches
# origin/feature/deleted-branch   ← Still showing despite being deleted!

git fetch --prune                    # Clean up stale references

# Configure to prune automatically on fetch:
git config --global fetch.prune true
```

### Finding Old Branches

```bash
# Branches not recently committed to:
git branch -v                        # See last commit on each branch

# Sort branches by last commit date:
git for-each-ref --sort=-committerdate refs/heads/ \
  --format='%(refname:short) %(committerdate:short)'

# Find branches merged into main more than X days ago:
git branch --merged main | while read b; do
    last=$(git log -1 --format="%ci" $b)
    echo "$b: $last"
done
```

### Keeping main Clean

```bash
# After merging a Pull Request on GitHub, immediately delete the branch there.
# Then locally:
git checkout main
git pull origin main    # Get the merged commit
git branch -d feature/completed-feature    # Delete the local branch
```""",

# ────────────────────────────────────────────────

"Git Merge": """## Bringing Changes Together

`git merge` integrates changes from one branch into another. When a feature is ready, you merge it into `main`. Understanding the types of merges and how conflicts work is essential for collaborative development.

### Types of Merge

**Fast-Forward Merge** — When the target branch hasn't changed since you branched off, Git simply moves the pointer forward:

```
Before:  main ──●──●──● 
                         ↘ feature ──●──●
                
After ff: main ──●──●──●──●──●   (just moved the pointer)
```

```bash
git checkout main
git merge feature/simple-change
# Fast-forward: no merge commit created, history stays linear
```

**Three-Way Merge (Merge Commit)** — When both branches have diverged, Git creates a new "merge commit" that has two parents:

```
Before: main    ──●──●──●──●
                      ↘
        feature        ──●──●──●

After:  main ──●──●──●──●──●──M   (M = merge commit with 2 parents)
                      ↗     ↗
        feature  ──●──●──●
```

```bash
git checkout main
git merge feature/new-feature
# Creates a merge commit (message: "Merge branch 'feature/new-feature'")
```

### Merge Conflicts

When the same lines were changed in both branches, Git can't decide which version to keep — it creates a conflict that you must resolve manually:

```
<<<<<<< HEAD (your current branch — main)
def login(email, password):
    user = db.get(email)
=======
def login(email, password, remember_me=False):
    user = db.find_by_email(email)
>>>>>>> feature/login-improvements
```

```bash
# When you see conflict markers:
# 1. Open the file and edit it to be correct
# 2. Remove the <<<<<<, =======, >>>>>>> markers
# 3. Stage the resolved file:
git add auth.py

# 4. Complete the merge:
git commit    # Git pre-fills the merge commit message

# Or abort entirely and go back to before the merge:
git merge --abort
```

### Merge Strategies

```bash
# Always create a merge commit even for fast-forwards:
git merge --no-ff feature/user-auth
# Creates a merge commit, preserving that the feature existed as a branch

# Squash all commits into one before merging:
git merge --squash feature/messy-commits
git commit -m "Add user authentication"
# The feature's 20 commits become ONE clean commit on main
```""",

# ────────────────────────────────────────────────

"Code Review": """## Pull Requests and the Review Process

A **Pull Request** (PR) — called a **Merge Request** (MR) in GitLab — is a proposal to merge your branch into another. It's the standard mechanism for code review, quality control, and team discussion before code reaches main.

### The Pull Request Workflow

```bash
# 1. Create a feature branch and do your work:
git checkout -b feature/add-email-verification
# ...commit your changes...
git push origin feature/add-email-verification

# 2. Open a Pull Request on GitHub/GitLab via the web interface
# 3. Fill out the PR description
# 4. Request reviewers
# 5. Address review comments
# 6. Merge when approved + CI passes
```

### Writing a Good PR Description

```markdown
## Summary
Adds email verification to the registration flow. Users must verify 
their email before they can log in for the first time.

## Changes Made
- Add email verification token model
- Send verification email on registration
- Add /verify-email/<token> endpoint
- Redirect unverified users to resend page

## How to Test
1. Register a new account
2. Check the email inbox (use Mailtrap for testing)
3. Click the verification link
4. Confirm you can log in

## Screenshots
[Screenshot of verification email]
[Screenshot of success page]

## Related Issues
Closes #123
Partially addresses #145
```

### Code Review Best Practices

**As a reviewer:**
- Understand WHAT the code is trying to do before criticizing HOW
- Ask questions instead of making demands ("What if..." instead of "You must...")
- Comment on code, not the person
- Distinguish between must-fix issues and suggestions
- Approve when it's good enough, not perfect

**As an author:**
- Keep PRs small (< 400 lines of changes) — large PRs get poor reviews
- Add comments to explain non-obvious decisions
- Respond to all comments
- Don't take feedback personally

### Reviewing the Changes

```bash
# Fetch and review the PR locally:
git fetch origin
git checkout feature/colleague-work
git log main..HEAD --oneline   # Commits not yet in main
git diff main..HEAD             # All the changes
```""",

# ────────────────────────────────────────────────

"CI/CD Workflows": """## Automating with GitHub Actions

**GitHub Actions** automates tasks triggered by repository events. Every time you push code, open a PR, or tag a release, Actions can automatically run tests, check code quality, build Docker images, and deploy to production.

### Basic Workflow Structure

Workflows live in `.github/workflows/*.yml`:

```yaml
# .github/workflows/ci.yml

name: CI                          # Name shown in GitHub UI

on:                               # Triggers
  push:
    branches: [main, develop]     # Run on pushes to these branches
  pull_request:
    branches: [main]              # Run on PRs targeting main

jobs:
  test:                           # Job name
    runs-on: ubuntu-latest        # Runner environment
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4  # Official action to checkout repo
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        run: pytest --tb=short
      
      - name: Check code style
        run: flake8 . --max-line-length 100
```

### FastAPI/Python CI Example

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:                   # Spin up a PostgreSQL service
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
        ports: ['5432:5432']
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
    
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: pip               # Cache pip packages for speed
      
      - run: pip install -r requirements.txt
      
      - name: Run pytest
        env:
          DATABASE_URL: postgresql://postgres:test@localhost/testdb
        run: pytest --cov=app --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### CD — Deploying on Push to Main

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /app
            git pull origin main
            pip install -r requirements.txt
            systemctl restart myapp
```""",

# ────────────────────────────────────────────────

"Rewriting History": """## git rebase — A Cleaner Alternative to Merge

**Rebasing** moves or replays your commits onto a different base commit. Instead of creating a merge commit, it makes it appear that your feature was developed from the current tip of the base branch — resulting in a clean, linear history.

### Merge vs Rebase

```
Merge:          main ──●──●──●──M
                           ↗  ↗
                feature  ●──●

Rebase:         main ──●──●──●──●'──●'
                                    ↑
                    feature's commits replayed on top
```

```bash
# Rebase feature branch onto current main:
git checkout feature/my-feature
git rebase main

# Git replays each feature commit on top of main's current tip
```

### Interactive Rebase — Editing History

`git rebase -i` is a powerful tool for cleaning up your commit history before merging:

```bash
# Rewrite the last 4 commits interactively:
git rebase -i HEAD~4

# Editor opens:
pick abc1234 Add user model
pick def5678 Add user model (forgot migration)    # Can squash this!
pick ghi9012 Fix typo in model
pick jkl3456 Add login endpoint

# Change 'pick' to:
# 's' (squash) — merge into previous commit
# 'r' (reword) — edit the commit message
# 'd' (drop)   — delete this commit entirely
# 'e' (edit)   — stop and amend this commit
# 'f' (fixup)  — squash, discard this commit's message

# After saving:
pick abc1234 Add user model
squash def5678 Add user model (forgot migration)   # Merged into abc1234!
squash ghi9012 Fix typo in model                   # Also merged!
pick jkl3456 Add login endpoint
```

### ⚠️ The Rebase Golden Rule

**Never rebase commits that have been pushed to a shared remote branch!**

Rebase rewrites commit history (new hashes). If others have pulled those commits, their history diverges from yours. This causes serious team problems.

```bash
# ✅ Safe: Rebase your local feature branch onto main (before pushing):
git checkout feature/my-feature
git rebase main
git push origin feature/my-feature    # First push — safe!

# ❌ Unsafe: Rebase a branch others have already pulled:
git push origin feature/my-feature   # Alice already pulled this!
git rebase main
git push --force origin feature/my-feature   # BREAKS Alice's history!
```""",

# ────────────────────────────────────────────────

"Pre-Commit Checks": """## Automating Code Quality with Git Hooks

**Git hooks** are scripts that run automatically at specific points in the Git workflow. **Pre-commit hooks** run before every commit, letting you automatically check code quality, run tests, and enforce standards.

### How Hooks Work

Hooks are shell scripts in `.git/hooks/`. The `pre-commit` hook runs when you run `git commit` — if it exits with a non-zero code, the commit is rejected.

```bash
# Create a basic pre-commit hook:
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

echo "Running pre-commit checks..."

# Run Python tests:
python -m pytest tests/ -q
if [ $? -ne 0 ]; then
    echo "Tests failed! Commit rejected."
    exit 1
fi

echo "All checks passed!"
exit 0
EOF

chmod +x .git/hooks/pre-commit
```

### The `pre-commit` Framework (Recommended)

Managing hooks manually is tedious. The `pre-commit` framework lets you configure hooks in a shareable config file:

```bash
pip install pre-commit
```

```yaml
# .pre-commit-config.yaml (in your project root)

repos:
  # Python code formatting:
  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black

  # Import sorting:
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  # Linting:
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8

  # Type checking:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy

  # General checks:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace     # Remove trailing spaces
      - id: end-of-file-fixer       # Ensure newline at end of file
      - id: check-yaml              # Validate YAML syntax
      - id: check-json              # Validate JSON syntax
      - id: check-merge-conflict    # Catch unresolved merge conflicts
      - id: no-commit-to-branch     # Prevent direct commits to main
        args: [--branch, main]
```

```bash
# Install hooks into .git/hooks/:
pre-commit install

# Run all hooks on all files manually:
pre-commit run --all-files

# Skip hooks for one commit (emergency!):
git commit -m "hotfix" --no-verify
```""",

# ────────────────────────────────────────────────

"One Repo to Rule Them All": """## Monorepo — Managing Multiple Projects in One Repository

A **monorepo** (monolithic repository) stores multiple related projects in a single Git repository. Companies like Google, Facebook, Twitter, and Uber use monorepos for their entire codebase.

### Monorepo vs Multi-repo

```
Multi-repo (separate repos):         Monorepo (one repo):
├── /frontend-app                    my-company/
├── /backend-api                     ├── apps/
├── /mobile-app                      │   ├── frontend/
└── /shared-utils                    │   ├── backend/
                                     │   └── mobile/
                                     ├── packages/
                                     │   └── shared-utils/
                                     └── tools/
```

### Advantages

✅ **Single source of truth** — One place to see everything  
✅ **Atomic changes** — Update frontend AND backend in one commit  
✅ **Code sharing** — Shared utilities without publishing packages  
✅ **Consistent tooling** — Same linting, testing, CI for everything  
✅ **Easy refactoring** — Rename a function and update all callers at once

### Disadvantages

❌ Longer CI times (build/test everything)  
❌ Repository becomes very large over time  
❌ Access control is harder (everyone sees everything)  
❌ Requires specialized tooling

### Monorepo Tools

**Nx** (JavaScript/TypeScript):
```bash
npx create-nx-workspace@latest my-monorepo
# Manages build, test, lint with dependency graph
# Only rebuilds what changed!
```

**Turborepo** (JavaScript):
```json
// turbo.json
{
  "pipeline": {
    "build": { "dependsOn": ["^build"] },
    "test": { "dependsOn": ["build"] },
    "lint": {}
  }
}
```

**Python monorepo structure:**
```
my-company/
├── services/
│   ├── auth-service/
│   │   ├── pyproject.toml
│   │   └── src/auth/
│   └── api-service/
│       ├── pyproject.toml
│       └── src/api/
├── packages/
│   └── shared-models/
│       ├── pyproject.toml
│       └── src/models/
└── Makefile   # Build commands for all services
```

### Git Sparse Checkout — Only Clone Part of a Monorepo

```bash
git clone --no-checkout https://github.com/company/monorepo.git
cd monorepo
git sparse-checkout init --cone
git sparse-checkout set services/auth-service packages/shared-models
git checkout main
# Only downloads the files you need!
```""",

}

# ════════════════════════════════════════════════
# FRONTEND
# ════════════════════════════════════════════════
FRONTEND_THEORY = {

"HTML Document Structure": """## The Blueprint of Every Web Page

Every web page is built on HTML (HyperText Markup Language). HTML uses **tags** to structure content, telling the browser what each piece of content is — a heading, paragraph, link, image, form, etc.

### The Basic HTML Document

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Head section — metadata, not visible on the page -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A learning platform for tech skills">
    <title>Digital Era Academy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Body section — everything visible on the page -->
    
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/courses">Courses</a>
        </nav>
    </header>
    
    <main>
        <h1>Welcome to Digital Era</h1>
        <p>Learn to code with Nigeria's best platform.</p>
    </main>
    
    <footer>
        <p>&copy; 2024 Digital Era Academy</p>
    </footer>

    <script src="app.js"></script>
</body>
</html>
```

### Understanding Each Tag

```html
<!DOCTYPE html>     <!-- Tells browser this is HTML5 (not optional!) -->
<html lang="en">    <!-- Root element; lang= improves accessibility -->

<!-- HEAD section -->
<head>
  <meta charset="UTF-8">  <!-- Character encoding — always include this -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- ↑ Makes the page mobile-responsive (CRITICAL) -->
  
  <title>Page Title</title>  <!-- Shows in browser tab and search results -->
  <link rel="stylesheet" href="styles.css">  <!-- Connect CSS file -->
</head>

<!-- BODY section — everything users see -->
<body>
  <header>   <!-- Semantic: site header/branding/navigation -->
  <nav>      <!-- Semantic: navigation links -->
  <main>     <!-- Semantic: the main content of the page (only one per page!) -->
  <article>  <!-- Semantic: self-contained content (blog post, product card) -->
  <section>  <!-- Semantic: a thematic grouping of content -->
  <aside>    <!-- Semantic: sidebar or supplementary content -->
  <footer>   <!-- Semantic: site footer (copyright, links) -->
</body>
```

### Semantic vs Non-Semantic HTML

```html
<!-- Non-semantic — no meaning: -->
<div class="header">
  <div class="nav">...</div>
</div>

<!-- Semantic — tells browser AND screen readers what this IS: -->
<header>
  <nav>...</nav>
</header>
```

Semantic HTML improves: **accessibility** (screen readers), **SEO** (search engines understand structure), **maintainability** (easier to read code).""",

# ────────────────────────────────────────────────

"Links & Images": """## Connecting Pages and Displaying Images

Links and images are the two most fundamental interactive elements in HTML.

### Links — `<a>` Tags

The `<a>` (anchor) element creates clickable links. The `href` attribute specifies where it goes.

```html
<!-- External link (use https://) -->
<a href="https://google.com">Visit Google</a>

<!-- Opens in a new tab -->
<a href="https://github.com" target="_blank" rel="noopener noreferrer">
    GitHub
</a>
<!-- rel="noopener noreferrer" is a security best practice with target="_blank" -->

<!-- Internal links (relative paths) -->
<a href="/courses">Courses</a>
<a href="/about.html">About Us</a>
<a href="../index.html">Back to Home</a>  <!-- Go up one folder -->

<!-- Anchor to a section on the same page -->
<a href="#contact">Jump to Contact Section</a>
<section id="contact">Contact us here...</section>

<!-- Email link -->
<a href="mailto:hello@digitalera.com">Email Us</a>

<!-- Phone link -->
<a href="tel:+2348012345678">Call Us</a>

<!-- Download a file -->
<a href="/files/syllabus.pdf" download>Download Syllabus (PDF)</a>
```

### Images — `<img>` Tags

```html
<!-- Basic image — src and alt are required -->
<img src="hero.jpg" alt="A student coding at a laptop">

<!-- alt text is crucial for:
     - Screen readers (accessibility)
     - When image fails to load
     - SEO -->

<!-- With width and height (prevents layout shift while loading) -->
<img 
    src="profile.jpg" 
    alt="Alice Johnson, Python instructor"
    width="200" 
    height="200"
>

<!-- Responsive images -->
<img 
    src="course-thumb.jpg" 
    alt="Python course thumbnail"
    style="max-width: 100%; height: auto;"
>

<!-- Lazy loading (only loads when user scrolls to it) -->
<img src="below-fold.jpg" alt="..." loading="lazy">

<!-- Images from another server -->
<img src="https://cdn.example.com/images/logo.png" alt="Company logo">
```

### Linking Images

```html
<!-- An image that IS a link: -->
<a href="/courses/python">
    <img src="python-course.jpg" alt="Python for Beginners course">
</a>
```

### Figures with Captions

```html
<figure>
    <img src="graph.png" alt="Revenue growth graph showing 150% increase">
    <figcaption>Fig. 1: Revenue growth from 2022 to 2024</figcaption>
</figure>
```""",

# ────────────────────────────────────────────────

"Forms & Inputs": """## Collecting User Input

HTML forms are how users send data to servers — login, registration, search, checkout. The `<form>` element wraps all input fields.

### Basic Form Structure

```html
<form action="/submit" method="POST">
    <!-- action: where to send data -->
    <!-- method: GET (visible in URL) or POST (hidden in body) -->
    
    <!-- Text input -->
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" placeholder="Alice Johnson" required>
    
    <!-- Email input (validates email format automatically!) -->
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>
    
    <!-- Password input (hides characters) -->
    <label for="password">Password</label>
    <input type="password" id="password" name="password" minlength="8" required>
    
    <button type="submit">Create Account</button>
</form>
```

### All Input Types

```html
<!-- Text types -->
<input type="text">         <!-- Single-line text -->
<input type="email">        <!-- Email (validates format) -->
<input type="password">     <!-- Hides typed characters -->
<input type="tel">          <!-- Phone number (shows phone keyboard on mobile) -->
<input type="url">          <!-- URL (validates format) -->
<input type="search">       <!-- Search box (with X to clear) -->
<textarea rows="5"></textarea>  <!-- Multi-line text -->

<!-- Numbers -->
<input type="number" min="0" max="100" step="1">
<input type="range" min="0" max="100" value="50">  <!-- Slider -->

<!-- Date/Time -->
<input type="date">         <!-- Date picker -->
<input type="time">         <!-- Time picker -->
<input type="datetime-local">

<!-- Selection -->
<input type="checkbox" name="terms" value="agreed">  <!-- Tick box -->
<input type="radio" name="gender" value="male">       <!-- One of group -->

<!-- File -->
<input type="file" accept=".jpg,.png,.pdf">   <!-- File upload -->
<input type="file" multiple>                  <!-- Multiple files -->

<!-- Hidden (sent with form, not shown) -->
<input type="hidden" name="csrf_token" value="abc123">

<!-- Buttons -->
<button type="submit">Submit</button>
<button type="reset">Clear Form</button>
<button type="button" onclick="doSomething()">Click Me</button>
```

### Dropdown and Selection

```html
<!-- Dropdown select: -->
<label for="course">Select Course</label>
<select id="course" name="course">
    <option value="">-- Choose a course --</option>
    <option value="python">Python for Beginners</option>
    <option value="sql">SQL Fundamentals</option>
    <option value="ml" selected>Machine Learning</option>
</select>

<!-- Multiple selection: -->
<select name="skills" multiple size="4">
    <option value="python">Python</option>
    <option value="js">JavaScript</option>
    <option value="sql">SQL</option>
    <option value="ml">Machine Learning</option>
</select>
```

### Form Validation Attributes

```html
<input 
    type="text" 
    required          <!-- Must be filled in -->
    minlength="2"     <!-- Minimum characters -->
    maxlength="50"    <!-- Maximum characters -->
    pattern="[A-Za-z ]+"  <!-- Regex pattern -->
    placeholder="Your full name"
>
```""",

# ────────────────────────────────────────────────

"Selectors & Properties": """## How CSS Finds and Styles Elements

CSS (Cascading Style Sheets) controls the visual presentation of HTML. A CSS **rule** consists of a **selector** (which elements to style) and **declarations** (what styles to apply).

### Basic Syntax

```css
selector {
    property: value;
    another-property: another-value;
}

/* Example: */
h1 {
    color: #1a1a2e;
    font-size: 2.5rem;
    font-weight: 700;
}
```

### Types of Selectors

```css
/* ──────────── BASIC SELECTORS ──────────── */

/* Element selector — all <p> tags */
p { color: #333; }

/* Class selector — all elements with class="card" */
.card { background: white; border-radius: 8px; }

/* ID selector — the element with id="hero" (unique, use sparingly) */
#hero { height: 100vh; }

/* Universal selector — every element */
* { box-sizing: border-box; margin: 0; padding: 0; }

/* ──────────── COMBINING SELECTORS ──────────── */

/* Descendant — <a> inside <nav> (any depth) */
nav a { color: white; text-decoration: none; }

/* Child — direct children only */
ul > li { list-style: none; }

/* Adjacent sibling — <p> immediately after <h2> */
h2 + p { font-size: 1.1rem; }

/* General sibling — all <p> after <h2> */
h2 ~ p { margin-top: 1rem; }

/* Multiple selectors — apply same styles to both */
h1, h2, h3 { font-family: 'Inter', sans-serif; }

/* ──────────── ATTRIBUTE SELECTORS ──────────── */
a[target="_blank"] { /* Links that open in new tab */
    padding-right: 1.2em;
}
input[type="email"] { border-color: blue; }

/* ──────────── PSEUDO-CLASSES ──────────── */
a:hover { color: #e94560; }            /* On mouse hover */
button:focus { outline: 2px solid blue; }  /* When focused */
li:first-child { font-weight: bold; }  /* First child element */
li:last-child { border-bottom: none; } /* Last child element */
li:nth-child(2n) { background: #f5f5f5; }  /* Every even row */
input:required { border-left: 3px solid red; }

/* ──────────── PSEUDO-ELEMENTS ──────────── */
p::first-line { font-weight: bold; }
li::before { content: "→ "; color: blue; }   /* Add content before */
.card::after { content: ""; display: block; } /* Clearfix pattern */
```

### CSS Specificity (Which Rule Wins?)

When multiple rules target the same element:
- `!important` > Inline style > ID > Class > Element

```css
/* Specificity: 0,0,1 — lowest */
p { color: black; }

/* Specificity: 0,1,0 */
.highlight { color: yellow; }

/* Specificity: 1,0,0 — highest */
#special { color: red; }
```""",

# ────────────────────────────────────────────────

"Flexbox Layout": """## The Modern Way to Build Layouts

**Flexbox** (Flexible Box Layout) is a CSS layout system that makes it easy to align and distribute space among items in a container, even when their sizes are unknown or dynamic.

### Flexbox Concepts

```
Flex Container: the parent element with display: flex
Flex Items: the direct children

Main Axis ────────────────────────────────→
│ ┌────────┐ ┌────────┐ ┌────────┐       │
│ │ Item 1 │ │ Item 2 │ │ Item 3 │       │
│ └────────┘ └────────┘ └────────┘       │
Cross Axis ↕
```

### Container Properties

```css
.container {
    display: flex;                     /* Activate flexbox! */
    
    /* Direction of the main axis: */
    flex-direction: row;               /* → default: left to right */
    flex-direction: row-reverse;       /* ← right to left */
    flex-direction: column;            /* ↓ top to bottom */
    flex-direction: column-reverse;    /* ↑ bottom to top */
    
    /* Wrapping: */
    flex-wrap: nowrap;   /* Default: items stay on one line */
    flex-wrap: wrap;     /* Items wrap to next line when needed */
    
    /* Alignment on main axis: */
    justify-content: flex-start;      /* Items at start (default) */
    justify-content: flex-end;        /* Items at end */
    justify-content: center;          /* Items centered */
    justify-content: space-between;   /* Equal gaps between items */
    justify-content: space-around;    /* Equal space around items */
    justify-content: space-evenly;    /* Truly equal spacing */
    
    /* Alignment on cross axis: */
    align-items: stretch;   /* Items fill cross axis (default) */
    align-items: flex-start; /* Items at top */
    align-items: flex-end;   /* Items at bottom */
    align-items: center;     /* Items centered vertically */
    align-items: baseline;   /* Aligned on text baseline */
    
    gap: 1rem;              /* Gap between items (rows and columns) */
    gap: 1rem 2rem;         /* row-gap col-gap */
}
```

### Common Layouts with Flexbox

```css
/* Perfect centering — the holy grail: */
.center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Navigation bar: */
.navbar {
    display: flex;
    justify-content: space-between;   /* Logo left, links right */
    align-items: center;
    padding: 1rem 2rem;
}

/* Card row: */
.cards {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.card {
    flex: 1 1 300px;   /* Grow, shrink, basis 300px */
}
```

### Item Properties

```css
.item {
    flex-grow: 1;     /* How much to grow (0 = don't grow) */
    flex-shrink: 1;   /* How much to shrink (0 = don't shrink) */
    flex-basis: auto; /* Starting size before growing/shrinking */
    
    /* Shorthand: */
    flex: 1;          /* flex-grow: 1, flex-shrink: 1, flex-basis: 0 */
    flex: 0 0 200px;  /* Fixed 200px — don't grow or shrink */
    
    /* Override align-items for just this item: */
    align-self: center;
    
    /* Change order (default is 0): */
    order: -1;        /* Move to front */
}
```""",

# ────────────────────────────────────────────────

"CSS Grid": """## Two-Dimensional Layout

**CSS Grid** is a 2D layout system — it lets you control both rows AND columns simultaneously, making complex layouts straightforward.

### Grid vs Flexbox

- **Flexbox** is 1D — great for rows OR columns, like navigation bars, card rows
- **Grid** is 2D — great for page layouts, dashboards with rows AND columns

### Basic Grid

```css
.container {
    display: grid;
    
    /* Define columns: */
    grid-template-columns: 200px 1fr 300px;      /* Fixed, flexible, fixed */
    grid-template-columns: repeat(3, 1fr);        /* 3 equal columns */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));  /* Responsive! */
    
    /* Define rows: */
    grid-template-rows: auto 1fr auto;            /* header, content, footer */
    
    /* Gaps: */
    gap: 1rem;
    row-gap: 1rem;
    column-gap: 2rem;
}
```

### The `fr` Unit — Fractional Space

```css
/* 3 equal columns: */
grid-template-columns: 1fr 1fr 1fr;
/* Same as: */
grid-template-columns: repeat(3, 1fr);

/* Sidebar layout: 250px sidebar, rest for content: */
grid-template-columns: 250px 1fr;

/* 2/3 content, 1/3 sidebar: */
grid-template-columns: 2fr 1fr;
```

### Placing Items

```css
.item {
    /* Place by line numbers (1-indexed): */
    grid-column: 1 / 3;    /* Start at line 1, end at line 3 (spans 2 columns) */
    grid-row: 1 / 2;       /* First row only */
    
    /* Span syntax (clearer): */
    grid-column: span 2;   /* Take up 2 columns */
    grid-row: span 3;      /* Take up 3 rows */
}
```

### Named Grid Areas

```css
.layout {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar main main"
        "footer footer footer";
    grid-template-columns: 250px 1fr 1fr;
    grid-template-rows: 80px 1fr 60px;
    min-height: 100vh;
}

header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
main    { grid-area: main; }
footer  { grid-area: footer; }
```

### Responsive Grid (No Media Queries!)

```css
.cards {
    display: grid;
    /* auto-fill: create as many columns as fit */
    /* minmax(280px, 1fr): each is min 280px, max 1 fraction */
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
}
/* Automatically shows 1 column on small screens, 4 on large! */
```""",

# ────────────────────────────────────────────────

"Variables & Console": """## JavaScript Fundamentals: Data and Output

JavaScript (JS) is the programming language of the web. It makes pages interactive — handling button clicks, fetching data, updating the UI, and more.

### Declaring Variables

Modern JavaScript has three ways to declare variables:

```javascript
// const — for values that never change (PREFERRED):
const name = 'Alice';
const MAX_RETRIES = 3;
const API_URL = 'https://api.digitalera.com';

// let — for values that will change:
let count = 0;
let currentUser = null;
let isLoggedIn = false;

// var — OLD (avoid in modern JS — has confusing scoping rules):
var oldWay = 'deprecated';
```

### Data Types

```javascript
// String:
const name = 'Alice';
const greeting = "Hello, World!";
const template = `Hello, ${name}!`;   // Template literal — can embed expressions

// Number (JavaScript has only ONE number type):
const age = 25;
const price = 9.99;
const negative = -10;

// Boolean:
const isActive = true;
const hasAccount = false;

// Null — explicitly no value:
const noValue = null;

// Undefined — declared but not assigned:
let unassigned;
console.log(unassigned);   // undefined

// Array:
const colors = ['red', 'green', 'blue'];
const mixed = [1, 'hello', true, null];

// Object:
const user = {
    name: 'Alice',
    age: 25,
    email: 'alice@example.com',
    isActive: true
};
```

### The Console — Your Debugging Tool

```javascript
// console.log — most common (prints to browser developer console):
console.log('Hello, World!');
console.log(name, age, isActive);   // Multiple values
console.log(`User: ${user.name}, Age: ${user.age}`);

// Other console methods:
console.error('Something went wrong!');    // Red error
console.warn('This might be a problem');   // Yellow warning
console.info('For information only');       // Info icon

// Debug complex data:
const students = [{ name: 'Alice', gpa: 3.8 }, { name: 'Bob', gpa: 3.2 }];
console.log(students);          // Expandable object in browser
console.table(students);        // Shows as a neat table!
console.dir(document.body);    // Explore DOM element properties

// Timing:
console.time('loop');
for (let i = 0; i < 1000000; i++) {}
console.timeEnd('loop');        // loop: 12.345ms

// Grouping:
console.group('User Details');
console.log('Name:', user.name);
console.log('Age:', user.age);
console.groupEnd();
```""",

# ────────────────────────────────────────────────

"Functions & Arrow Functions": """## Defining Reusable Actions in JavaScript

Functions are reusable blocks of code. JavaScript has multiple ways to define them — understanding each is essential.

### Function Declaration

```javascript
// Traditional function declaration — "hoisted" (can be called before defined):
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet('Alice'));   // Hello, Alice!
```

### Function Expression

```javascript
// Assigned to a variable — NOT hoisted:
const greet = function(name) {
    return `Hello, ${name}!`;
};

// Anonymous function used immediately (IIFE):
(function() {
    console.log('This runs immediately!');
})();
```

### Arrow Functions — Modern, Concise Syntax

```javascript
// Traditional:
function square(x) { return x * x; }

// Arrow function:
const square = (x) => { return x * x; };

// Implicit return (for single expressions, no braces or return needed):
const square = x => x * x;     // Single param: parens optional

const add = (a, b) => a + b;   // Multiple params: parens required

const getUser = () => ({ name: 'Alice', age: 25 });   // Returning an object: wrap in ()
```

### Default Parameters

```javascript
function greet(name = 'World', punctuation = '!') {
    return `Hello, ${name}${punctuation}`;
}

greet();              // Hello, World!
greet('Alice');       // Hello, Alice!
greet('Bob', '.');    // Hello, Bob.
```

### Rest Parameters and Spread

```javascript
// ...rest — collect remaining args into an array:
function sum(...numbers) {
    return numbers.reduce((total, n) => total + n, 0);
}
sum(1, 2, 3, 4, 5);   // 15

// ...spread — expand an array into individual args:
const nums = [1, 2, 3, 4, 5];
console.log(Math.max(...nums));   // 5
```

### Arrow Functions: Key Differences from Regular Functions

```javascript
// Arrow functions do NOT have their own 'this':
const timer = {
    seconds: 0,
    start() {
        // Arrow function inherits 'this' from start():
        setInterval(() => {
            this.seconds++;   // 'this' correctly refers to timer object
        }, 1000);
    }
};

// Regular function would need .bind(this) or const self = this
```""",

# ────────────────────────────────────────────────

"Arrays & Methods": """## Working with Collections in JavaScript

JavaScript arrays are ordered, dynamic lists that hold any data types. They come with powerful built-in methods.

### Creating Arrays

```javascript
const fruits = ['apple', 'banana', 'cherry'];
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, 'hello', true, { name: 'Alice' }, [1, 2]];
const empty = [];
const initialized = new Array(5).fill(0);   // [0, 0, 0, 0, 0]
```

### Basic Operations

```javascript
const arr = ['a', 'b', 'c', 'd'];

// Access:
console.log(arr[0]);        // 'a'
console.log(arr.at(-1));    // 'd' (last element — new syntax!)

// Modify:
arr.push('e');              // Add to end: ['a', 'b', 'c', 'd', 'e']
arr.pop();                  // Remove from end: ['a', 'b', 'c', 'd']
arr.unshift('z');           // Add to start: ['z', 'a', 'b', 'c', 'd']
arr.shift();                // Remove from start: ['a', 'b', 'c', 'd']

// Information:
console.log(arr.length);    // 4
console.log(arr.includes('b'));  // true
console.log(arr.indexOf('c'));   // 2
```

### The Essential Higher-Order Methods

These methods accept a function (callback) and apply it to each element:

```javascript
const students = [
    { name: 'Alice', gpa: 3.8, city: 'Lagos' },
    { name: 'Bob',   gpa: 2.5, city: 'Abuja' },
    { name: 'Carol', gpa: 3.9, city: 'Lagos' },
    { name: 'Dave',  gpa: 3.1, city: 'Kano'  },
];

// .map() — transform every element:
const names = students.map(s => s.name);
// ['Alice', 'Bob', 'Carol', 'Dave']

const upperNames = students.map(s => s.name.toUpperCase());

// .filter() — keep only matching elements:
const passing = students.filter(s => s.gpa >= 3.0);
// Alice, Carol, Dave

const lagosStudents = students.filter(s => s.city === 'Lagos');

// .find() — get the FIRST matching element:
const topStudent = students.find(s => s.gpa >= 3.8);
// { name: 'Alice', ... }

// .some() — does AT LEAST ONE match?
const anyHighGPA = students.some(s => s.gpa >= 3.9);   // true

// .every() — do ALL match?
const allPassing = students.every(s => s.gpa >= 2.0);  // true

// .reduce() — fold into a single value:
const totalGPA = students.reduce((sum, s) => sum + s.gpa, 0);
const avgGPA = totalGPA / students.length;

// Chaining methods:
const topLagosNames = students
    .filter(s => s.city === 'Lagos')    // Keep Lagos students
    .filter(s => s.gpa >= 3.5)          // With high GPA
    .map(s => s.name);                  // Get their names
// ['Alice', 'Carol']
```""",

# ────────────────────────────────────────────────

"Global State": """## Managing Data Across Your Application

**State** is any data your application stores that can change over time — the currently logged-in user, the contents of a shopping cart, which tab is active, what items are in a search result. As apps grow, managing where this data lives and how it flows between components becomes critical.

### Local State vs Global State

```javascript
// Local state — only needed in one component:
function Counter() {
    const [count, setCount] = useState(0);   // Stays inside Counter
    return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

// Global state — needed by many components across the app:
// - Currently logged-in user
// - Shopping cart
// - Theme (dark/light mode)
// - Language selection
```

### Context API — React's Built-in Global State

```javascript
import { createContext, useContext, useState } from 'react';

// 1. Create a context:
const AuthContext = createContext(null);

// 2. Create a provider component:
export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    
    const login = (userData) => {
        setUser(userData);
        setIsLoggedIn(true);
    };
    
    const logout = () => {
        setUser(null);
        setIsLoggedIn(false);
    };
    
    return (
        <AuthContext.Provider value={{ user, isLoggedIn, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

// 3. Wrap your app:
function App() {
    return (
        <AuthProvider>
            <Router>
                <Navbar />     {/* Can access user without props! */}
                <Dashboard />
            </Router>
        </AuthProvider>
    );
}

// 4. Use in any component:
function Navbar() {
    const { user, isLoggedIn, logout } = useContext(AuthContext);
    
    return (
        <nav>
            {isLoggedIn ? (
                <>
                    <span>Welcome, {user.name}</span>
                    <button onClick={logout}>Logout</button>
                </>
            ) : (
                <a href="/login">Login</a>
            )}
        </nav>
    );
}
```

### When to Use Global State

✅ **Use global state for:**
- Authentication (user, role, token)
- Shopping cart
- Theme preferences
- Notifications

❌ **Keep local state for:**
- Form input values
- UI state (is dropdown open?)
- Data only one component uses""",

# ────────────────────────────────────────────────

"Modern Layouts": """## CSS Grid and Flexbox Together

Modern web layouts combine Grid for the overall page structure and Flexbox for component-level alignment. Understanding when to use each is the key skill.

### The Modern CSS Layout Approach

```css
/* Reset — prevents browser default style inconsistencies */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Page Layout — Grid handles the macro structure */
.page {
    display: grid;
    grid-template-rows: auto 1fr auto;   /* header, main, footer */
    min-height: 100vh;
}

/* Dashboard Layout — Grid for the sidebar + content */
.dashboard {
    display: grid;
    grid-template-columns: 260px 1fr;
    grid-template-areas:
        "sidebar header"
        "sidebar main";
    min-height: calc(100vh - 60px);
}

/* Navigation Bar — Flexbox for inline alignment */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: #1a1a2e;
    height: 60px;
}

.nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
}

/* Card Grid — Responsive without media queries */
.course-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    padding: 2rem;
}

/* Card — Flexbox for internal layout */
.course-card {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    transition: transform 0.2s, box-shadow 0.2s;
}

.course-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.course-card__body {
    flex: 1;   /* Takes up remaining space — pushes button to bottom */
    padding: 1.5rem;
}

.course-card__footer {
    padding: 1rem 1.5rem;
    background: #f8f9fa;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

### Responsive Layout with Media Queries

```css
/* Mobile-first approach — start with mobile layout, add breakpoints */

/* Mobile (default — no media query needed): */
.dashboard {
    grid-template-columns: 1fr;   /* Sidebar hides or goes to top */
}

/* Tablet and above: */
@media (min-width: 768px) {
    .dashboard {
        grid-template-columns: 240px 1fr;
    }
}

/* Desktop: */
@media (min-width: 1200px) {
    .dashboard {
        grid-template-columns: 280px 1fr;
    }
    
    .course-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```""",

# ────────────────────────────────────────────────

"Lazy Loading": """## Only Load What the User Actually Sees

**Lazy loading** defers the loading of resources (images, components, scripts) until they're actually needed — typically when they enter the user's viewport. This dramatically improves initial page load time and saves bandwidth.

### Native Image Lazy Loading (HTML)

```html
<!-- Just add loading="lazy" — browser handles the rest! -->
<img 
    src="course-thumbnail.jpg" 
    alt="Python course thumbnail"
    loading="lazy"
    width="400" 
    height="300"
>

<!-- Always eager-load above-the-fold images: -->
<img src="hero-image.jpg" alt="Hero" loading="eager">

<!-- Below the fold — lazy load: -->
<img src="testimonial.jpg" alt="Student review" loading="lazy">
```

### React Lazy Loading — Code Splitting

Split your JavaScript bundle so users only download the code for the current page:

```javascript
import { lazy, Suspense } from 'react';

// Instead of:
// import Dashboard from './Dashboard';

// Lazy load — only downloaded when user navigates to it:
const Dashboard = lazy(() => import('./Dashboard'));
const AdminPanel = lazy(() => import('./AdminPanel'));
const CourseEditor = lazy(() => import('./CourseEditor'));

function App() {
    return (
        <Router>
            <Suspense fallback={<div>Loading...</div>}>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/admin" element={<AdminPanel />} />
                </Routes>
            </Suspense>
        </Router>
    );
}
```

### Intersection Observer — Custom Lazy Loading

```javascript
// Load high-resolution images only when they enter the viewport:
const lazyImages = document.querySelectorAll('img[data-src]');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;       // Swap in the real image
            img.removeAttribute('data-src');  // Clean up
            observer.unobserve(img);          // Stop observing
        }
    });
}, {
    rootMargin: '200px',    // Start loading 200px before entering viewport
    threshold: 0            // Trigger as soon as any part is visible
});

lazyImages.forEach(img => observer.observe(img));
```

```html
<!-- HTML for custom lazy loading: -->
<img 
    src="placeholder-blur.jpg"   <!-- Low-quality placeholder shown immediately -->
    data-src="full-quality.jpg"  <!-- Real image loaded on demand -->
    alt="Course banner"
    class="lazy"
>
```""",

# ────────────────────────────────────────────────

"Semantic HTML": """## Writing HTML That Means Something

**Semantic HTML** uses elements that convey meaning about the content, not just its appearance. `<article>` tells you it's a self-contained piece of content; `<div>` tells you nothing.

### Why Semantics Matter

1. **Accessibility** — Screen readers use semantic tags to navigate. A blind user navigating by headings needs proper `<h1>`-`<h6>` hierarchy.
2. **SEO** — Search engines understand semantic structure and rank well-structured pages higher.
3. **Maintainability** — Code is easier to read and maintain.
4. **Browser defaults** — Browsers apply useful default styling and behavior to semantic elements.

### The Main Semantic Elements

```html
<!-- Page structure: -->
<header>    <!-- Site/article header — branding, navigation, hero -->
<nav>       <!-- Navigation links (main menu, breadcrumbs, pagination) -->
<main>      <!-- Primary content — ONLY ONE per page! -->
<article>   <!-- Self-contained content that makes sense on its own -->
<section>   <!-- Thematic grouping of related content -->
<aside>     <!-- Sidebar, call-to-action, related links -->
<footer>    <!-- Site/article footer — contact, copyright, links -->

<!-- Content:  -->
<h1>–<h6>   <!-- Heading hierarchy — NEVER skip levels! -->
<p>         <!-- A paragraph of text -->
<figure>    <!-- An image, diagram, code block with optional caption -->
<figcaption><!-- Caption for a <figure> -->
<time datetime="2024-01-15">January 15, 2024</time>  <!-- Date/time -->
<address>   <!-- Contact information -->
<blockquote cite="https://source.com">  <!-- Quotation -->
<mark>      <!-- Highlighted text -->
<strong>    <!-- Important text (bold by default) -->
<em>        <!-- Stressed emphasis (italic by default) -->
<abbr title="Cascading Style Sheets">CSS</abbr>  <!-- Abbreviation -->
<code>      <!-- Inline code -->
<pre>       <!-- Preformatted text block -->

<!-- Lists: -->
<ul>        <!-- Unordered list (bullets) -->
<ol>        <!-- Ordered list (numbers) -->
<dl>        <!-- Description list — term/definition pairs -->
<dt>        <!-- Description term -->
<dd>        <!-- Description definition -->
```

### Before vs After Example

```html
<!-- ❌ Non-semantic (divs everywhere): -->
<div class="header">
    <div class="logo">Digital Era</div>
    <div class="menu">
        <div class="menu-item"><a href="/">Home</a></div>
    </div>
</div>
<div class="content">
    <div class="blog-post">
        <div class="post-title">How to Learn Python</div>
        <div class="post-text">...</div>
    </div>
</div>

<!-- ✅ Semantic: -->
<header>
    <h1 class="logo">Digital Era</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
        </ul>
    </nav>
</header>
<main>
    <article>
        <h2>How to Learn Python</h2>
        <p>...</p>
    </article>
</main>
```""",

# ────────────────────────────────────────────────

"Utility-First CSS": """## Tailwind CSS — A Different Way to Style

**Tailwind CSS** is a utility-first CSS framework. Instead of writing custom CSS classes with styles inside, you apply many small, single-purpose utility classes directly in your HTML.

### Traditional CSS vs Tailwind

```html
<!-- Traditional approach: -->
<style>
.card {
    background: white;
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    max-width: 400px;
}
</style>
<div class="card">...</div>

<!-- Tailwind approach — no CSS file needed: -->
<div class="bg-white rounded-lg p-6 shadow-md max-w-sm">...</div>
```

### Common Utility Classes

```html
<!-- Spacing: p=padding, m=margin, t/r/b/l/x/y = sides -->
<div class="p-4">          <!-- padding: 1rem -->
<div class="px-6 py-3">    <!-- padding: 0.75rem 1.5rem -->
<div class="mt-4 mb-8">    <!-- margin-top: 1rem; margin-bottom: 2rem -->

<!-- Typography: -->
<h1 class="text-4xl font-bold text-gray-900">         <!-- 36px, bold, dark gray -->
<p class="text-base text-gray-600 leading-relaxed">   <!-- body text -->
<span class="text-sm font-medium text-blue-600">      <!-- small, blue -->

<!-- Colors: -->
<div class="bg-blue-500 text-white">        <!-- Blue background, white text -->
<div class="bg-gradient-to-r from-purple-500 to-pink-500">

<!-- Layout: -->
<div class="flex items-center justify-between gap-4">
<div class="grid grid-cols-3 gap-6">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">

<!-- Sizing: -->
<div class="w-full max-w-lg h-64">
<img class="w-full h-48 object-cover">

<!-- Borders: -->
<div class="border border-gray-200 rounded-xl">

<!-- States: -->
<button class="bg-blue-500 hover:bg-blue-600 active:bg-blue-700 
               transition-colors duration-200">
```

### Responsive Prefixes

```html
<!-- Format: breakpoint:utility -->
<!-- sm: 640px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1536px -->

<div class="text-sm md:text-base lg:text-lg">           <!-- Responsive text -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4"> <!-- Responsive grid -->
<div class="hidden md:block">                           <!-- Hidden on mobile -->
<div class="block md:hidden">                           <!-- Show only on mobile -->
```""",

# ────────────────────────────────────────────────

"Responsive Design": """## Tailwind's Responsive System

Tailwind's responsive design is built on **breakpoints** — screen width thresholds where the layout changes. Every utility can be prefixed with a breakpoint to apply only at that size and above (mobile-first).

### Tailwind Breakpoints

| Prefix | Min Width | Typical Device |
|--------|-----------|----------------|
| (none) | 0px | Mobile (default) |
| `sm:` | 640px | Large mobile |
| `md:` | 768px | Tablet |
| `lg:` | 1024px | Laptop |
| `xl:` | 1280px | Desktop |
| `2xl:` | 1536px | Wide desktop |

### Mobile-First Pattern

Always design for mobile first, then add modifications for larger screens:

```html
<!-- 1 column on mobile, 2 on tablet, 4 on desktop: -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="bg-white rounded-lg p-4 shadow">Card 1</div>
    <div class="bg-white rounded-lg p-4 shadow">Card 2</div>
    <div class="bg-white rounded-lg p-4 shadow">Card 3</div>
    <div class="bg-white rounded-lg p-4 shadow">Card 4</div>
</div>

<!-- Text that grows with screen size: -->
<h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold">
    Welcome to Digital Era
</h1>

<!-- Padding that increases with screen size: -->
<section class="px-4 sm:px-8 md:px-12 lg:px-24">
    Content here
</section>

<!-- Navbar: hamburger on mobile, full menu on desktop: -->
<nav class="flex items-center justify-between p-4">
    <div class="font-bold text-xl">Digital Era</div>
    
    <!-- Hide on mobile, show on desktop: -->
    <ul class="hidden md:flex gap-8 list-none">
        <li><a href="/">Home</a></li>
        <li><a href="/courses">Courses</a></li>
    </ul>
    
    <!-- Show on mobile, hide on desktop: -->
    <button class="md:hidden" id="menu-toggle">☰</button>
</nav>
```

### Responsive Images

```html
<!-- Full width on mobile, fixed width on desktop: -->
<img 
    class="w-full md:w-96 rounded-xl shadow-lg" 
    src="course-banner.jpg" 
    alt="Python Course"
>

<!-- Object-fit for consistent image display: -->
<img class="w-full h-48 object-cover rounded-t-xl" src="thumb.jpg" alt="...">
```""",

# ────────────────────────────────────────────────

"Declarative Rendering": """## Vue.js — Rendering Based on Data

**Vue.js** is a progressive JavaScript framework for building user interfaces. Its core idea is **declarative rendering** — you describe what the UI should look like based on your data, and Vue automatically updates the DOM when the data changes.

### The Core Vue 3 Pattern

```javascript
// In a Vue Single File Component (.vue):
<template>
    <!-- HTML template — rendered declaratively based on data -->
    <div>
        <h1>Hello, {{ name }}!</h1>
        <p>You have {{ courses.length }} courses.</p>
        <ul>
            <li v-for="course in courses" :key="course.id">
                {{ course.title }}
            </li>
        </ul>
        <button @click="addCourse">Add Course</button>
    </div>
</template>

<script setup>
// Composition API (Vue 3 — modern approach)
import { ref, computed } from 'vue'

// Reactive data:
const name = ref('Alice')
const courses = ref([
    { id: 1, title: 'Python Basics' },
    { id: 2, title: 'SQL Fundamentals' },
])

// Computed values (automatically re-computed when deps change):
const courseCount = computed(() => courses.value.length)

// Methods:
function addCourse() {
    courses.value.push({ 
        id: Date.now(), 
        title: 'New Course' 
    })
}
</script>
```

### Vue Directives

```html
<!-- v-bind (or :) — bind an attribute to data: -->
<img :src="user.avatarUrl" :alt="user.name">
<input :value="searchQuery" :disabled="isLoading">

<!-- v-model — two-way data binding: -->
<input v-model="searchQuery" placeholder="Search...">
<textarea v-model="description"></textarea>
<select v-model="selectedCategory">...</select>

<!-- v-if / v-else — conditional rendering: -->
<div v-if="isLoggedIn">Welcome, {{ user.name }}!</div>
<div v-else>Please log in.</div>
<div v-else-if="isPending">Loading...</div>

<!-- v-show — toggles CSS display (element stays in DOM): -->
<div v-show="isMenuOpen">Menu content...</div>

<!-- v-for — list rendering: -->
<li v-for="(item, index) in items" :key="item.id">
    {{ index + 1 }}. {{ item.name }}
</li>

<!-- @click (v-on:click) — event handling: -->
<button @click="handleSubmit">Submit</button>
<button @click.prevent="handleSubmit">Submit (prevent default)</button>
<input @keyup.enter="handleSearch">
```""",

# ────────────────────────────────────────────────

"Typing Props": """## TypeScript with React — Type-Safe Components

**TypeScript** adds static types to JavaScript. When used with React, it catches prop type errors at compile time instead of runtime, provides autocomplete in your editor, and makes refactoring safer.

### Typing Component Props

```typescript
// Define prop types with an interface:
interface CourseCardProps {
    id: number;
    title: string;
    description: string;
    instructor: string;
    price: number;
    imageUrl: string;
    isFeatured?: boolean;        // Optional — may be undefined
    onEnroll: (id: number) => void;  // Function prop
}

// Use the interface in the component:
function CourseCard({
    id,
    title,
    description,
    instructor,
    price,
    imageUrl,
    isFeatured = false,     // Default value for optional prop
    onEnroll,
}: CourseCardProps) {
    return (
        <div className={`card ${isFeatured ? 'card--featured' : ''}`}>
            <img src={imageUrl} alt={title} />
            <h3>{title}</h3>
            <p>{description}</p>
            <p className="instructor">{instructor}</p>
            <p className="price">₦{price.toLocaleString()}</p>
            <button onClick={() => onEnroll(id)}>Enroll Now</button>
        </div>
    );
}

// TypeScript catches errors at compile time:
<CourseCard
    id={1}
    title="Python Basics"
    description="Learn Python from scratch"
    instructor="Alice Johnson"
    price={15000}
    imageUrl="/python.jpg"
    onEnroll={(id) => console.log(`Enrolling in ${id}`)}
/>

// ❌ TypeScript would catch this: price should be a number, not a string
<CourseCard price="free" />   // Error: Type 'string' is not assignable to type 'number'
```

### useState with Types

```typescript
import { useState } from 'react';

interface User {
    id: number;
    name: string;
    email: string;
    role: 'student' | 'instructor' | 'admin';   // Union type
}

// TypeScript infers the type from the initial value:
const [count, setCount] = useState(0);           // number
const [name, setName] = useState('');            // string

// Or specify explicitly for complex types:
const [user, setUser] = useState<User | null>(null);
const [courses, setCourses] = useState<Course[]>([]);

// Now TypeScript knows what setUser expects:
setUser({ id: 1, name: 'Alice', email: 'a@b.com', role: 'student' });
// setUser({ id: 1 });   // ❌ Error: missing required fields
```""",

# ────────────────────────────────────────────────

"CSS Keyframes": """## Animating with CSS Keyframes

CSS animations let you create smooth, GPU-accelerated animations without JavaScript. They're defined with `@keyframes` and applied with the `animation` property.

### Basic Keyframe Animation

```css
/* 1. Define the animation: */
@keyframes fade-in {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* 2. Apply it to an element: */
.hero-text {
    animation: fade-in 0.6s ease-out forwards;
    /*         name    duration timing  fill-mode */
}
```

### Animation Properties

```css
.animated-element {
    animation-name: fade-in;           /* Which @keyframes to use */
    animation-duration: 0.6s;          /* How long */
    animation-timing-function: ease-out;  /* Speed curve */
    animation-delay: 0.2s;             /* Wait before starting */
    animation-iteration-count: 1;      /* How many times (or 'infinite') */
    animation-direction: normal;       /* normal, reverse, alternate */
    animation-fill-mode: forwards;     /* What state to hold after */
    
    /* Shorthand (most common): */
    animation: fade-in 0.6s ease-out 0.2s forwards;
}
```

### Multiple Keyframe Stops

```css
@keyframes pulse {
    0%   { transform: scale(1); box-shadow: 0 0 0 0 rgba(66, 153, 225, 0.4); }
    50%  { transform: scale(1.05); }
    70%  { box-shadow: 0 0 0 10px rgba(66, 153, 225, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(66, 153, 225, 0); }
}

/* Bouncing loader: */
@keyframes bounce {
    0%, 100% { transform: translateY(0); animation-timing-function: ease-out; }
    50%       { transform: translateY(-30px); animation-timing-function: ease-in; }
}

/* Spinning loader: */
@keyframes spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

.spinner {
    animation: spin 1s linear infinite;
}

/* Gradient shift: */
@keyframes gradient-shift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient-shift 8s ease infinite;
}
```

### Performance Best Practices

Only animate these properties for smooth 60fps (GPU-accelerated):
- `transform` (scale, rotate, translate)
- `opacity`

Avoid animating: `width`, `height`, `top`, `left`, `padding`, `margin` — these cause layout recalculation (expensive).""",

# ────────────────────────────────────────────────

"React Testing Library": """## Testing React Components the Right Way

**React Testing Library** tests components from the user's perspective — it interacts with elements the way a user would, not by checking internal implementation details.

### Installation

```bash
npm install --save-dev @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

### Your First Test

```javascript
// CourseCard.test.jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import CourseCard from './CourseCard';

const mockCourse = {
    id: 1,
    title: 'Python Basics',
    instructor: 'Alice Johnson',
    price: 15000,
    enrolledCount: 142,
};

test('renders course title and instructor', () => {
    render(<CourseCard course={mockCourse} />);
    
    // Find elements as users would see them:
    expect(screen.getByText('Python Basics')).toBeInTheDocument();
    expect(screen.getByText('Alice Johnson')).toBeInTheDocument();
    expect(screen.getByText(/₦15,000/)).toBeInTheDocument();
});

test('calls onEnroll when button is clicked', async () => {
    const mockEnroll = jest.fn();
    const user = userEvent.setup();
    
    render(<CourseCard course={mockCourse} onEnroll={mockEnroll} />);
    
    const enrollButton = screen.getByRole('button', { name: /enroll/i });
    await user.click(enrollButton);
    
    expect(mockEnroll).toHaveBeenCalledWith(1);   // Called with the course ID
    expect(mockEnroll).toHaveBeenCalledTimes(1);
});

test('shows loading state while enrolling', async () => {
    const user = userEvent.setup();
    render(<CourseCard course={mockCourse} onEnroll={jest.fn()} />);
    
    await user.click(screen.getByRole('button', { name: /enroll/i }));
    
    // After click, button should show loading state:
    expect(screen.getByRole('button', { name: /enrolling/i })).toBeDisabled();
});
```

### Key Querying Methods

```javascript
// Preferred — accessible queries (like real users find things):
screen.getByRole('button', { name: 'Submit' })
screen.getByRole('heading', { name: 'Python Basics' })
screen.getByLabelText('Email Address')
screen.getByPlaceholderText('Search courses...')
screen.getByText('Welcome back')

// All queries: getBy (throws if not found), queryBy (returns null), findBy (async)
screen.queryByText('Error message')   // Returns null if not found
await screen.findByText('Loaded data')  // Waits for element to appear
```""",

# ────────────────────────────────────────────────

"useState Basics": """## Managing Component State with useState

`useState` is React's primary hook for adding state to functional components. When state changes, React automatically re-renders the component with the new values.

### Basic useState

```javascript
import { useState } from 'react';

function Counter() {
    // Destructure: [currentValue, setterFunction] = useState(initialValue)
    const [count, setCount] = useState(0);
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>+1</button>
            <button onClick={() => setCount(count - 1)}>-1</button>
            <button onClick={() => setCount(0)}>Reset</button>
        </div>
    );
}
```

### Multiple State Variables

```javascript
function RegistrationForm() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [error, setError] = useState(null);
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        setError(null);
        
        try {
            await registerUser({ name, email, password });
        } catch (err) {
            setError(err.message);
        } finally {
            setIsSubmitting(false);
        }
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input value={name} onChange={e => setName(e.target.value)} />
            <input value={email} onChange={e => setEmail(e.target.value)} />
            <input value={password} type="password" onChange={e => setPassword(e.target.value)} />
            {error && <p className="error">{error}</p>}
            <button type="submit" disabled={isSubmitting}>
                {isSubmitting ? 'Creating account...' : 'Register'}
            </button>
        </form>
    );
}
```

### State with Objects and Arrays

```javascript
// Object state — spread to update:
const [user, setUser] = useState({ name: '', email: '', role: 'student' });

// ❌ Wrong — mutates state directly:
user.name = 'Alice';
setUser(user);   // React won't re-render!

// ✅ Correct — create a new object:
setUser({ ...user, name: 'Alice' });
setUser(prev => ({ ...prev, name: 'Alice' }));

// Array state:
const [items, setItems] = useState([]);

// Add:
setItems(prev => [...prev, newItem]);

// Remove:
setItems(prev => prev.filter(item => item.id !== idToRemove));

// Update:
setItems(prev => prev.map(item =>
    item.id === targetId ? { ...item, done: true } : item
));
```""",

}

# ════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════
if __name__ == "__main__":
    base = "curriculum/tracks"
    patch_track(os.path.join(base, "sql_databases.json"), SQL_THEORY)
    patch_track(os.path.join(base, "version_control.json"), GIT_THEORY)
    patch_track(os.path.join(base, "frontend.json"), FRONTEND_THEORY)
    print("\n\nAll three tracks complete!")
