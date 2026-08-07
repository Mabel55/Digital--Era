import json

with open("curriculum/tracks/data_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

theories = {
    ("Data Analysis & Excel Concepts", "What is Data Analysis?"): """## Finding the Story in the Numbers

We live in the Information Age. Every time you swipe a credit card, click a button on a website, or walk into a grocery store with a loyalty card, data is generated. 
Companies collect terabytes of this raw data, but raw data is completely useless on its own. 

**Data Analysis** is the process of inspecting, cleaning, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making.

### The Core Objective

The ultimate goal of a Data Analyst is to **answer business questions**.
- *Marketing*: "Which advertising campaign brought in the most profitable customers?"
- *Operations*: "Why did shipping times increase by 15% last month?"
- *Finance*: "Are we on track to hit our Q3 revenue targets?"

### Descriptive vs Predictive

Data Analysis generally falls into a few categories:
1. **Descriptive Analytics**: What happened? (e.g., "Sales dropped 10% in July.")
2. **Diagnostic Analytics**: Why did it happen? (e.g., "Sales dropped because a major competitor launched a massive discount campaign in July.")
3. **Predictive Analytics**: What will happen next? (e.g., "Based on historical trends, sales will likely rebound by 5% in August.")
4. **Prescriptive Analytics**: What should we do about it? (e.g., "We should increase our ad spend by 20% in August to accelerate the rebound.")

As a Data Analyst, you will spend most of your time on Descriptive and Diagnostic analytics, building dashboards and reports to help executives understand the current state of the business.""",

    ("Data Analysis & Excel Concepts", "The Data Lifecycle"): """## From Raw Data to Actionable Insights

Data Analysis is not just opening Excel and making a chart. It is a rigorous, structured process known as the **Data Lifecycle**. 
Skipping steps in this lifecycle is the fastest way to generate wildly inaccurate conclusions.

### The 5 Phases

**1. Collection (Extraction)**
Where does the data live? Is it in a SQL database, a messy CSV file sent by a client, or hidden behind an API? You must first acquire the raw data.

**2. Cleaning (Wrangling/Munging)**
This is where analysts spend 80% of their time. Real-world data is disastrously messy. 
- You might have a column for "Age" where someone entered `"twenty-five"` instead of `25`. 
- You might have missing values (Nulls/NaNs) because a sensor went offline.
- You might have duplicate records.
If you do not clean the data, your final charts will be fundamentally flawed. ("Garbage In, Garbage Out").

**3. Exploration (EDA)**
Before answering the specific business question, you must understand the "shape" of your data. You look for correlations, outliers, and general distributions. 
*Example: "Wow, 90% of our revenue comes from just 5% of our users. I didn't expect that."*

**4. Modeling & Analysis**
This is where you apply statistical formulas, write complex SQL queries, or use Python to aggregate the data to answer the specific question.

**5. Communication (Visualization)**
The most brilliant analysis is useless if the CEO cannot understand it. You must build clear, intuitive Dashboards (using Tableau, PowerBI, or Matplotlib) that tell a compelling story, stripping away the complexity so the business can make a decision.""",

    ("Data Analysis & Excel Concepts", "Rows vs Columns"): """## The Anatomy of Tabular Data

Whether you are using Excel, a SQL database, or Pandas in Python, almost all data analysis is performed on **Tabular Data** (data arranged in a table). 
Understanding the structural difference between Rows and Columns is foundational.

### Columns (Variables / Features)

A **Column** runs vertically. It represents a single specific **Attribute** (or Variable) across the entire dataset.
- Examples: `First_Name`, `Age`, `Purchase_Date`, `Total_Spent`.
- **The Golden Rule**: Every single piece of data in a column MUST be the exact same data type. You cannot have a column named `Age` where the first cell is `25` (an integer) and the second cell is `"New York"` (a string). 

### Rows (Observations / Records)

A **Row** runs horizontally. It represents a single, unique **Observation** or Event.
- Example: A single row might represent one specific customer (`Alice, 28, 2023-10-15, $150.00`).
- Unlike columns, a row contains a mix of different data types (String, Integer, Date, Float).

### The Intersection (The Cell)

The intersection of a Row and a Column is a **Cell**. It contains a single data point.

**Why this structure matters:**
When a Data Analyst writes code or formulas, they usually perform operations on *Columns*, not Rows. 
- You calculate the Average (Mean) of the entire `Total_Spent` column. 
- You don't calculate the Average of a Row, because taking the average of `Alice + 28 + $150` makes zero mathematical sense!

**Tidy Data:**
In a well-structured dataset (known as "Tidy Data"):
1. Each variable forms a column.
2. Each observation forms a row.
3. Each type of observational unit forms a table.""",

    ("Data Analysis & Excel Concepts", "Basic Excel Formulas"): """## The Calculator of the Business World

Microsoft Excel (and Google Sheets) remains the most widely used data analysis tool on Earth. While SQL and Python handle massive datasets, Excel is unbeatable for quick, ad-hoc calculations on smaller files.

### The Equals Sign `=`

The most important rule in Excel: If you type `10 + 10` into a cell and press Enter, Excel just displays the text "10 + 10". 
To tell Excel you want it to perform a calculation, you MUST start the cell with an equals sign: `=10 + 10` (Excel will display `20`).

### Cell References

Instead of hardcoding numbers, you reference other cells by their Column Letter and Row Number (e.g., `A1`, `C5`).
`=A1 + B1`
If the data in `A1` changes, the formula automatically recalculates. This is the core magic of spreadsheets.

### Essential Aggregation Functions

Functions are pre-built formulas that take a range of cells as arguments.

- **`=SUM(A1:A10)`**: Adds all numbers from A1 to A10.
- **`=AVERAGE(B1:B50)`**: Calculates the mean of the range.
- **`=COUNT(C1:C100)`**: Counts how many cells in the range contain *numbers*.
- **`=COUNTA(C1:C100)`**: Counts how many cells are *not empty* (useful for counting text).
- **`=MAX(D1:D10)`** & **`=MIN(D1:D10)`**: Finds the highest/lowest number in the range.

### Relative vs Absolute References

When you copy a formula like `=A1*B1` down a column, Excel automatically shifts the references (`=A2*B2`, `=A3*B3`). This is a **Relative Reference**.

Sometimes, you want to multiply every row by a single fixed tax rate in cell `Z1`. If you drag `=A1*Z1` down, it becomes `=A2*Z2`, which is wrong! 
To lock a cell reference, you use the Dollar Sign `$` to create an **Absolute Reference**: `=A1*$Z$1`.""",

    ("Data Analysis & Excel Concepts", "Sorting and Filtering Data"): """## Organizing the Chaos

When you open a dataset with 50,000 rows of sales data, it is impossible to read. The first step in exploring tabular data is usually Sorting and Filtering to find exactly what you care about.

### Sorting Data

**Sorting** changes the *order* of the rows based on the values in a specific column, without hiding any data.

- **Alphabetical (A to Z / Z to A)**: Useful for finding a specific customer by Last Name.
- **Numerical (Smallest to Largest / Largest to Smallest)**: Crucial for finding the Top 10 most expensive products, or the 5 worst-performing sales reps.
- **Chronological (Oldest to Newest / Newest to Oldest)**: Essential for time-series data to see the most recent transactions first.

*Danger in Excel*: If you highlight only one column (e.g., `Last_Name`) and click "Sort", Excel will sort *only* the names, leaving the `Age` and `Address` columns in their original positions. You have just permanently scrambled your dataset, mixing Alice's name with Bob's address! Always ensure you expand the selection to sort the entire table.

### Filtering Data

**Filtering** temporarily *hides* rows that do not meet a specific criteria. The data isn't deleted, it's just removed from view.

- **Text Filters**: Show only rows where `Country` equals "Canada", or where `Email` contains "@gmail.com".
- **Number Filters**: Show only rows where `Revenue` is greater than `$10,000`, or between 50 and 100.
- **Date Filters**: Show only rows where `Purchase_Date` was "Last Month" or "Year to Date".

Filtering allows you to instantly answer questions like: *"Show me all the orders from Canada that were placed last week and had a value over $500."*""",

    ("Data Analysis & Excel Concepts", "Pivot Table Concepts"): """## The Ultimate Aggregation Tool

If you have a dataset of 100,000 individual sales transactions, and your manager asks: *"What was the total revenue for each product category in each region?"*

You cannot answer this with basic filtering or SUM formulas. You need a **Pivot Table**.
A Pivot Table allows you to summarize and reorganize massive datasets instantly, without writing a single complex formula.

### The 4 Quadrants of a Pivot Table

When you create a Pivot Table in Excel, you drag and drop your columns into four distinct areas:

**1. Values (The "What")**
This is the data you want to calculate. Usually, this is a numeric column like `Revenue`. The Pivot Table will aggregate it (e.g., Sum of Revenue, or Average of Revenue).

**2. Rows (The "How to group it")**
This dictates how the data is grouped vertically. If you drag the `Region` column into Rows, the Pivot Table will create one row for "North", one for "South", etc., and calculate the total Revenue for each.

**3. Columns (The "Sub-group")**
This breaks the data down further horizontally. If you drag `Product_Category` into Columns, the table will now show a grid: Regions on the left, Categories across the top, and the Revenue at the intersection.

**4. Filters (The "Exclusions")**
If you drag `Year` into Filters, you can easily restrict the entire Pivot Table to only show data for "2023".

### The Magic of Pivoting

The term "Pivot" comes from how easily you can change your mind. 
If the manager suddenly says, *"Actually, I want to see the total revenue by Sales Rep, not Region,"* you simply drag `Region` out of the Rows box, and drag `Sales_Rep` in. The entire table instantly recalculates in milliseconds.

Understanding how to group and aggregate data conceptually via Pivot Tables is the exact same logic you will use later when learning `GROUP BY` in SQL or `groupby()` in Pandas.""",

    ("Intro to Databases", "Relational Databases Explained"): """## The Backbone of Modern Software

While Excel is great for analyzing static files, it is completely unsuited for running a live application like Facebook or Amazon. Spreadsheets max out at about 1 million rows, and if 100 people try to edit an Excel file simultaneously, it will crash or corrupt.

Live applications store their data in a **Database**. 
The most common type of database in the world is the **Relational Database Management System (RDBMS)** (e.g., PostgreSQL, MySQL, SQLite, SQL Server).

### What makes it "Relational"?

Imagine you run an E-commerce store. You have a customer named Alice who has placed 5 orders.
If you used a flat spreadsheet, every time Alice places an order, you have to type her Name, Email, and Shipping Address into the new row. If Alice moves to a new house, you have to find and update all 5 of her past orders!

A Relational Database solves this by splitting data into separate, specialized tables that **relate** to each other.

1. **The Users Table**: Stores Alice's Name, Email, and Address exactly *once*.
2. **The Orders Table**: Stores the Order Date and Amount. Instead of duplicating Alice's email, the Orders table just contains a reference ID pointing back to Alice in the Users table.

### Why Relational Databases Rule

1. **Data Integrity (ACID)**: Relational databases guarantee that transactions are processed reliably. If a bank transfer deducts $100 from you but the server crashes before adding it to your friend, the database automatically rolls back the entire transaction. No money is lost.
2. **Efficiency**: By eliminating duplicate data (a process called Normalization), the database saves massive amounts of hard drive space.
3. **Concurrency**: Thousands of users can read and write to the database at the exact same millisecond without corrupting the data.

To ask questions of a Relational Database, Data Analysts use a special language called **SQL**.""",

    ("Intro to Databases", "Tables and Schemas"): """## The Blueprint of Data

In a Relational Database, data is organized into **Tables**. A table is conceptually identical to a single tab in an Excel workbook: it has rows and columns.

However, unlike Excel, where you can type a word into a column meant for numbers, Database Tables are strictly enforced by a **Schema**.

### The Schema

A Schema is the structural blueprint of the database. It defines exactly what tables exist, what columns are in those tables, and crucially, what **Data Type** is allowed in each column.

If a developer tries to insert the string `"Twenty"` into a column that the Schema defined as an `INTEGER`, the database will throw a fatal error and reject the insertion. This strictness is what makes databases so reliable for analysis.

### Common SQL Data Types

When building a schema, you must choose the correct type for each column:

- **INT / INTEGER**: Whole numbers (e.g., `Age: 25`, `Quantity: 100`).
- **FLOAT / DECIMAL**: Numbers with decimals (e.g., `Price: 19.99`). `DECIMAL` is used for precise financial data to avoid floating-point math errors.
- **VARCHAR(n)**: Variable-length character string. The `n` specifies the maximum length (e.g., `Email: VARCHAR(255)`).
- **TEXT**: Extremely long strings (e.g., `Blog_Post_Content: TEXT`).
- **DATE**: A calendar date without time (e.g., `2023-10-15`).
- **TIMESTAMP / DATETIME**: A date and an exact time (e.g., `2023-10-15 14:30:00`).
- **BOOLEAN**: True or False (`1` or `0`).

### The CREATE TABLE Command

Database Administrators (and sometimes Analysts) use SQL to define this schema:

```sql
CREATE TABLE employees (
    id INT,
    first_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE,
    is_active BOOLEAN
);
```
Once this table is created, the database guarantees that every single row inserted into `employees` will perfectly conform to this structure.""",

    ("Intro to Databases", "Primary Keys"): """## The Unique Identifier

In a database table holding 50 million users, it is highly likely that two users will have the exact same name (e.g., "John Smith"). They might even live in the same city. 

How does the database distinguish between them? How can you guarantee that you are deleting the *correct* John Smith's account?

Every table in a relational database must have a **Primary Key (PK)**.

### The Rules of a Primary Key

A Primary Key is a specific column (or a combination of columns) that uniquely identifies every single row in the table. 

1. **It must be UNIQUE**: No two rows can ever have the same Primary Key value. If you try to insert a row with a duplicate key, the database will throw an error.
2. **It cannot be NULL**: Every single row MUST have a value in the Primary Key column. You cannot have an empty identifier.
3. **It should be IMMUTABLE**: A Primary Key should ideally never change. If it changes, it breaks the links to other tables.

### Types of Primary Keys

**1. Surrogate Keys (Auto-Incrementing IDs)**
This is the most common approach. The database automatically generates a meaningless, sequential integer for every new row (`1`, `2`, `3`...).
- *Example*: An `employee_id` column.
- *Pros*: Extremely fast for the database to index and search.

**2. Natural Keys**
Using a piece of actual real-world data that is guaranteed to be unique.
- *Example*: A `social_security_number` or an `email_address`.
- *Cons*: Real-world data is messy. People change their email addresses, which violates the immutability rule!

### Defining a Primary Key in SQL

```sql
CREATE TABLE users (
    -- The database will automatically assign 1, 2, 3...
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    
    first_name VARCHAR(50),
    email VARCHAR(255)
);
```""",

    ("Intro to Databases", "Foreign Keys"): """## Connecting the Tables

If Relational Databases split data into multiple tables to avoid duplication, how do we connect the data back together? 

We use **Foreign Keys (FK)**.

A Foreign Key is a column in one table that contains a value pointing directly to the **Primary Key** of another table.

### The Relationship Example

Imagine two tables: `Users` and `Orders`.

**Users Table:**
| user_id (PK) | name | email |
|---|---|---|
| 1 | Alice | alice@test.com |
| 2 | Bob | bob@test.com |

**Orders Table:**
| order_id (PK) | amount | user_id (FK) |
|---|---|---|
| 101 | $50.00 | 1 |
| 102 | $25.00 | 2 |
| 103 | $90.00 | 1 |

In the `Orders` table, the `user_id` column is a **Foreign Key**. 
Looking at Order 103, we see the `user_id` is `1`. To find out who placed the order, the database simply looks up `user_id = 1` in the `Users` table and finds Alice!

### Referential Integrity

The magic of Foreign Keys isn't just linking data; it's enforcing strict rules called **Referential Integrity**.

If you declare a column as a Foreign Key, the database will actively prevent you from doing stupid things:
1. **Invalid Inserts**: If you try to insert an order into the `Orders` table with `user_id = 99` (and user 99 doesn't exist), the database will reject the order! You cannot have an "orphan" order.
2. **Dangerous Deletes**: If you try to delete Alice from the `Users` table, the database will block you, because she still has linked orders in the `Orders` table. (You must either delete her orders first, or configure a "Cascade Delete").

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    amount DECIMAL(10,2),
    user_id INT,
    
    -- This enforces the strict relationship!
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```""",

    ("Intro to Databases", "Database Normalization"): """## Designing Efficient Schemas

**Normalization** is the process of organizing data in a database to reduce redundancy (duplicate data) and improve data integrity. 

When a database is poorly designed, it suffers from "Data Anomalies":
- *Update Anomaly*: If a supplier's phone number changes, you have to update it in 5,000 different rows.
- *Delete Anomaly*: If you delete a product, you accidentally delete the supplier's contact info because it was stored in the same row.

### The Normal Forms

Database architects follow rules called "Normal Forms" to achieve a clean design.

**1. First Normal Form (1NF): Atomic Values**
Every cell must contain a single, indivisible value. 
*Bad*: A column named `Skills` containing `"Python, SQL, Excel"`. 
*Fix*: You must split these into separate rows or a separate mapping table, so you can easily query "How many people know SQL?".

**2. Second Normal Form (2NF): No Partial Dependencies**
This applies to tables with composite primary keys (keys made of two columns). Every non-key column must depend on the *entire* primary key, not just part of it.
*Fix*: Split the data into separate tables.

**3. Third Normal Form (3NF): No Transitive Dependencies**
Every non-key column must depend ONLY on the Primary Key, and not on another non-key column.
*Bad*: An `Orders` table containing `Order_ID (PK)`, `Customer_ID`, and `Customer_Email`. The email depends on the Customer, not the Order.
*Fix*: Move `Customer_Email` to the `Customers` table. The `Orders` table should only hold the `Customer_ID` Foreign Key.

### The Trade-off: Joins

Normalization is beautiful for data integrity and saving storage space. 
However, there is a major performance trade-off. Because the data is scattered across 10 different tables, a Data Analyst must use complex SQL `JOIN` statements to stitch the data back together to answer a simple question. Highly normalized databases (OLTP) are great for applications, but can be slow for analytics. Data Warehouses (OLAP) often intentionally *de-normalize* data to make querying faster!""",

    ("SQL Essentials", "The SELECT Statement"): """## Asking the Database a Question

SQL (Structured Query Language) is the standard language for communicating with relational databases. 
As a Data Analyst, 95% of your SQL code will be dedicated to reading data, not writing it. You do this using the `SELECT` statement.

A `SELECT` statement is a query. It asks the database a question, and the database returns a virtual table called a "Result Set".

### The Basic Syntax

Every query requires two mandatory clauses:
1. **`SELECT`**: What columns do you want to see?
2. **`FROM`**: Which table holds these columns?

```sql
-- Select specific columns
SELECT first_name, last_name, email 
FROM employees;
```

### The Wildcard Asterisk (*)

If you want to view every single column in the table, you use the asterisk `*` symbol, which means "All".

```sql
SELECT * 
FROM employees;
```
*Note for Analysts: While `SELECT *` is great for a quick glance to see what the table looks like, you should never use it in production reports or dashboards. If a table has 100 columns and you only need 2, `SELECT *` forces the database to transfer massive amounts of useless data over the network, drastically slowing down performance.*

### Formatting Best Practices

SQL is entirely case-insensitive and ignores whitespace. 
`select * from employees;` works exactly the same as `SELECT * FROM employees;`.

However, the industry standard is to:
1. Write SQL keywords in **UPPERCASE** (`SELECT`, `FROM`, `WHERE`).
2. Write table and column names in **lowercase**.
3. Put each major clause on a new line for readability.
4. Always end a query with a semicolon `;` (though some modern engines forgive you if you forget it).""",

    ("SQL Essentials", "Filtering with WHERE"): """## Finding the Needle in the Haystack

If an `orders` table has 50 million rows, running `SELECT * FROM orders` is useless. You need to restrict the Result Set to only the specific rows you care about.

You do this using the **`WHERE`** clause. The `WHERE` clause evaluates a condition for every single row in the table. If the condition is True, the row is included in the results. If False, it is hidden.

### Basic Operators

**1. Equals (`=`)**
```sql
SELECT first_name, department
FROM employees
WHERE department = 'Sales';
```
*(Note: In SQL, strings must be enclosed in single quotes `'Sales'`, not double quotes).*

**2. Not Equals (`!=` or `<>`)**
```sql
SELECT product_name, category
FROM products
WHERE category != 'Electronics';
```

**3. Greater Than / Less Than (`>`, `<`, `>=`, `<=`)**
Perfect for numerical data or dates.
```sql
SELECT order_id, total_amount
FROM orders
WHERE total_amount >= 500.00;

-- SQL understands date math!
SELECT user_id, signup_date
FROM users
WHERE signup_date > '2023-01-01';
```

### Filtering NULL values

In SQL, a missing value is represented by `NULL`. 
You cannot use the equals sign to find NULLs (`WHERE phone = NULL` will fail). Why? Because NULL means "unknown", and mathematically, "unknown" does not equal "unknown".

Instead, you must use the special `IS NULL` or `IS NOT NULL` operators.

```sql
-- Find users who forgot to provide a phone number
SELECT first_name, email
FROM users
WHERE phone_number IS NULL;
```""",

    ("SQL Essentials", "Using AND / OR"): """## Combining Conditions

Rarely will a business question require only a single filter. 
*"Show me all the customers from California who purchased a Premium subscription."*

To combine multiple conditions in the `WHERE` clause, we use Logical Operators: **`AND`** and **`OR`**.

### The AND Operator

`AND` requires that **both** conditions must be True for the row to be included. It narrows down the results.

```sql
SELECT customer_name, state, subscription_plan
FROM customers
WHERE state = 'CA' 
  AND subscription_plan = 'Premium';
```

### The OR Operator

`OR` requires that **at least one** of the conditions must be True. It expands the results.

```sql
-- Find customers in either California or New York
SELECT customer_name, state
FROM customers
WHERE state = 'CA' 
   OR state = 'NY';
```

### The Danger of Mixing AND & OR (Parentheses)

What happens if a manager asks: *"Find all Premium users who live in either California or New York"*?

If you write this query without parentheses, it will return the wrong data:
```sql
-- DANGEROUS / BUGGY QUERY
SELECT * FROM customers
WHERE subscription_plan = 'Premium' AND state = 'CA' OR state = 'NY';
```
Why is it buggy? Because in SQL, **`AND` is evaluated before `OR`** (just like multiplication before addition in math). 
This query actually asks: *(Premium AND CA)* OR *(Anyone in NY, regardless of their subscription!)*.

**The Fix:** Always use parentheses to explicitly group your logic.

```sql
-- CORRECT QUERY
SELECT * FROM customers
WHERE subscription_plan = 'Premium' 
  AND (state = 'CA' OR state = 'NY');
```""",

    ("SQL Essentials", "Sorting with ORDER BY"): """## Organizing the Result Set

By default, SQL does not guarantee the order of the rows it returns. They might appear in the order they were inserted, or they might appear completely randomized based on how the database engine processed the query.

To guarantee a specific order, you must use the **`ORDER BY`** clause. It is always written at the end of your query.

### Basic Sorting

```sql
SELECT employee_name, salary
FROM employees
WHERE department = 'Engineering'
ORDER BY salary;
```
By default, `ORDER BY` sorts in **Ascending (ASC)** order.
- Numbers: Smallest to Largest.
- Text: A to Z.
- Dates: Oldest to Newest.

### Descending Order (DESC)

If you want to see the highest paid employees first, or the most recent orders first, you must append the `DESC` keyword.

```sql
SELECT order_id, order_date
FROM orders
ORDER BY order_date DESC;
```

### Multi-Column Sorting

You can sort by multiple columns by separating them with commas. The database will sort by the first column, and if there is a "tie", it uses the second column as a tie-breaker.

*"Sort the employees alphabetically by Department. Within each department, sort them by Salary from highest to lowest."*

```sql
SELECT department, employee_name, salary
FROM employees
ORDER BY department ASC, salary DESC;
```
*(Note: Adding `ASC` is optional since it is the default, but often written for clarity).*""",

    ("SQL Essentials", "Limiting Results"): """## Fetching Top N Records

Sometimes you don't want to see all the data. 
- *"Who are our Top 5 highest paying customers?"*
- *"Show me the 10 most recent error logs."*
- Or simply: *"Show me 3 rows just so I can see what this table looks like without crashing my computer."*

To restrict the total number of rows returned, we use the Limit clause.

### The LIMIT / TOP Syntax

The exact keyword depends on which SQL Database you are using, but the concept is identical.

**In PostgreSQL, MySQL, and SQLite (LIMIT):**
This clause goes at the very end of the query, after `ORDER BY`.

```sql
-- Find the 5 most expensive products
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 5;
```

**In Microsoft SQL Server (TOP):**
This clause goes at the very beginning, immediately after `SELECT`.

```sql
SELECT TOP 5 product_name, price
FROM products
ORDER BY price DESC;
```

### Pagination (OFFSET)

LIMIT is frequently combined with `OFFSET` to build Pagination in web applications (e.g., clicking "Page 2" on a list of products).

`OFFSET` tells the database how many rows to skip before it starts returning data.

```sql
-- Give me 10 products, but skip the first 20. 
-- (This effectively returns Page 3 of the results!)
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 10 OFFSET 20;
```""",

    ("SQL Essentials", "Using LIKE for Patterns"): """## Fuzzy Text Searching

The `=` operator requires an exact, perfect match. If you search for `WHERE email = 'gmail.com'`, it will only find rows where the entire email address is literally exactly "gmail.com", which is useless.

To search for patterns within text, SQL provides the **`LIKE`** operator, combined with Wildcard characters.

### The Wildcards

**1. The Percent Sign `%`**
Matches **zero or more** characters.
- `'A%'` : Matches any string starting with 'A' (Apple, Art, A).
- `'%A'` : Matches any string ending with 'A' (Banana, Pizza).
- `'%A%'` : Matches any string containing 'A' anywhere inside it (Cat, Banana).

**2. The Underscore `_`**
Matches exactly **one single** character.
- `'B_b'` : Matches Bob, Bub, Bib, but NOT Boob (too many letters).

### Examples

*"Find all customers using a Gmail account:"*
```sql
SELECT first_name, email
FROM customers
WHERE email LIKE '%@gmail.com';
```

*"Find all employees whose last name starts with 'S':"*
```sql
SELECT last_name
FROM employees
WHERE last_name LIKE 'S%';
```

### Case Sensitivity

In many databases (like PostgreSQL), `LIKE` is strictly case-sensitive. Searching for `LIKE '%smith%'` will NOT find "Smith". 
To perform a case-insensitive search in PostgreSQL, use **`ILIKE`**.
*(Note: MySQL and SQLite's `LIKE` are usually case-insensitive by default).*

### Performance Warning
Putting a wildcard at the *beginning* of a string (`LIKE '%smith'`) is disastrous for database performance on large tables. It completely bypasses database Indexes, forcing the engine to scan every single row one by one (a Full Table Scan). Use it with caution on massive datasets.""",

    ("SQL Essentials", "The IN Operator"): """## Simplifying Multiple OR Conditions

Imagine a manager asks: *"Find all employees who work in Sales, Marketing, or IT."*

Using the tools we know so far, you would have to write a very tedious `WHERE` clause using multiple `OR` statements:

```sql
-- Tedious and hard to read
SELECT first_name, department
FROM employees
WHERE department = 'Sales' 
   OR department = 'Marketing' 
   OR department = 'IT';
```
If the manager asked for 15 different departments, the query would become massive and unreadable.

### The IN Operator

The **`IN`** operator allows you to check if a value exists within a specific list of values. It is syntactic sugar for a chain of `OR` statements, making the code much cleaner and easier to maintain.

```sql
-- Clean and readable
SELECT first_name, department
FROM employees
WHERE department IN ('Sales', 'Marketing', 'IT');
```

### The NOT IN Operator

You can invert the logic to exclude a list of values.
*"Show me all employees EXCEPT those in HR and Legal."*

```sql
SELECT first_name, department
FROM employees
WHERE department NOT IN ('HR', 'Legal');
```

### Combining IN with Subqueries

The true power of the `IN` operator is unlocked when the list isn't hardcoded by you, but generated dynamically by another query (a Subquery).

*"Find all customers who bought our most expensive product."*
```sql
SELECT customer_name 
FROM customers
WHERE product_id IN (
    -- The Subquery dynamically generates the list of IDs
    SELECT product_id 
    FROM products 
    WHERE price > 1000
);
```""",

    ("SQL Essentials", "Aliasing with AS"): """## Renaming Columns and Tables

When querying a database, the column names returned in the Result Set match the column names exactly as they are defined in the schema.
Sometimes schema names are ugly (e.g., `usr_frst_nm`), or sometimes you perform a calculation and the database gives it a terrible default name (e.g., `SUM(price * tax_rate)`).

You can temporarily rename a column or table in your query results using the **`AS`** keyword. This is called **Aliasing**.

### Aliasing Columns

This is crucial for making your final reports and dashboards readable for business stakeholders.

```sql
SELECT 
    first_name AS "First Name",
    salary * 12 AS "Annual Salary"
FROM employees;
```
*Note: If your alias contains spaces (like "First Name"), you MUST wrap it in double quotes. If it is a single word (like `Annual_Salary`), the quotes are optional.*

### Aliasing Tables

Aliasing tables is even more important, but for a different reason: it saves you from typing long table names over and over again when performing complex `JOIN` operations.

```sql
-- 'e' is a temporary alias for the 'employees' table
SELECT e.first_name, e.department
FROM employees AS e
WHERE e.salary > 50000;
```
*Note: The `AS` keyword is entirely optional in most SQL dialects. You can just put a space: `FROM employees e`.*

### The Scope of an Alias

An alias only exists for the duration of the query. It does not permanently rename the column in the actual database.
Furthermore, because of the strict order of operations in SQL execution, you cannot use a Column Alias in the `WHERE` clause! 

```sql
-- THIS WILL THROW AN ERROR!
SELECT salary * 12 AS annual_salary
FROM employees
WHERE annual_salary > 100000; -- The WHERE clause evaluates BEFORE the SELECT clause!
```""",

    ("Filtering & Aggregating", "Counting Rows"): """## Summarizing the Data

Filtering data with `WHERE` is useful for finding specific records. However, Data Analysis is primarily about **Aggregation**—taking thousands of rows of detailed data and summarizing it into a single number.

The most fundamental aggregation function is **`COUNT()`**.

### COUNT(*) vs COUNT(column)

There are two ways to use `COUNT()`, and they behave differently regarding `NULL` (missing) values.

**1. `COUNT(*)`**
This counts the total number of physical rows in the table (or the result set), completely ignoring what data is inside them. It includes rows even if every column is NULL.

*"How many total users are in our database?"*
```sql
SELECT COUNT(*) AS total_users
FROM users;
```

**2. `COUNT(column_name)`**
This counts the number of rows where the specific column is **NOT NULL**.

*"How many users actually provided a phone number?"*
```sql
SELECT COUNT(phone_number) AS users_with_phones
FROM users;
```

### COUNT(DISTINCT column)

Often, a manager will ask: *"How many UNIQUE countries do our customers live in?"*
If you have 10,000 customers, `COUNT(country)` will return 10,000. 

To remove duplicates before counting, you use the `DISTINCT` keyword inside the parentheses.

```sql
SELECT COUNT(DISTINCT country) AS unique_countries
FROM customers;
```

### Combining COUNT with WHERE

Aggregation functions respect the `WHERE` clause. The database filters the rows *first*, and then counts whatever is left.

*"How many active users do we have in California?"*
```sql
SELECT COUNT(*) AS active_ca_users
FROM users
WHERE status = 'Active' AND state = 'CA';
```""",

    ("Filtering & Aggregating", "SUM and AVG"): """## Calculating Totals and Averages

While `COUNT()` counts the number of rows, **`SUM()`** and **`AVG()`** perform mathematical calculations on the actual numeric values inside those rows.

### The SUM() Function

`SUM()` adds up all the values in a specific numeric column.

*"What is the total revenue we made from all orders in 2023?"*
```sql
SELECT SUM(order_amount) AS total_revenue
FROM orders
WHERE order_date >= '2023-01-01' 
  AND order_date <= '2023-12-31';
```

### The AVG() Function

`AVG()` calculates the mean (average) of a numeric column.

*"What is the average salary of an engineer at our company?"*
```sql
SELECT AVG(salary) AS avg_engineer_salary
FROM employees
WHERE department = 'Engineering';
```

### The Danger of NULLs in Math

How do `SUM` and `AVG` handle `NULL` (missing) values?
**They silently ignore them.**

Imagine a table of 3 employees:
- Alice: $100,000
- Bob: $50,000
- Charlie: NULL (Salary not entered yet)

If you run `AVG(salary)`, SQL does NOT calculate `(100k + 50k + 0) / 3 = $50k`.
It calculates `(100k + 50k) / 2 = $75k`. 
It pretends Charlie doesn't exist. This can drastically skew your analysis if you aren't aware of missing data!

To treat NULLs as zero, you must use a function like `COALESCE()`, which replaces NULLs with a default value before doing the math:
```sql
-- Treats Charlie's salary as 0, average becomes $50k
SELECT AVG(COALESCE(salary, 0)) AS true_average
FROM employees;
```""",

    ("Filtering & Aggregating", "MIN and MAX"): """## Finding the Extremes

The final core aggregation functions are **`MIN()`** and **`MAX()`**. They find the smallest and largest values in a column, respectively.

Unlike `SUM()` and `AVG()`, which only work on numbers, `MIN` and `MAX` work on almost any data type!

### Numerical Data

*"What is the cheapest and most expensive product we sell?"*
```sql
SELECT 
    MIN(price) AS lowest_price,
    MAX(price) AS highest_price
FROM products;
```

### Date Data

When applied to dates, `MIN` finds the oldest (earliest) date, and `MAX` finds the newest (most recent) date.

*"When did our very first customer sign up, and when did our latest customer sign up?"*
```sql
SELECT 
    MIN(signup_date) AS first_customer_date,
    MAX(signup_date) AS newest_customer_date
FROM customers;
```

### Text Data

When applied to strings, `MIN` and `MAX` use alphabetical ordering (A to Z).
- `MIN` finds the word closest to 'A'.
- `MAX` finds the word closest to 'Z'.

```sql
SELECT 
    MIN(last_name) AS first_alphabetically,
    MAX(last_name) AS last_alphabetically
FROM employees;
```

### Important Restriction of Aggregations

A very common mistake beginners make is trying to find *who* has the maximum salary by writing:
```sql
-- THIS WILL THROW AN ERROR!
SELECT first_name, MAX(salary)
FROM employees;
```
SQL will reject this. `MAX(salary)` collapses the entire table into a single row (e.g., `$150k`). But `first_name` still has 500 rows! SQL doesn't know how to display 500 names next to 1 aggregated salary.

To find the name of the person with the highest salary, you must use a Subquery or an `ORDER BY` with `LIMIT 1`.""",

    ("Filtering & Aggregating", "Grouping Data (GROUP BY)"): """## The Most Important Clause in Data Analysis

Up until now, our aggregation functions (`SUM`, `COUNT`, `AVG`) have collapsed the *entire* table into a single grand total. 

But business questions are rarely about grand totals. A manager won't ask "What is our total revenue?" They will ask: *"What is our total revenue **broken down by Region**?"*

To calculate aggregations for different sub-groups, we use the **`GROUP BY`** clause. It is the SQL equivalent of an Excel Pivot Table.

### How GROUP BY Works

1. SQL identifies all the unique values in the column you are grouping by (e.g., North, South, East, West).
2. It splits the massive table into smaller, invisible "buckets" based on those regions.
3. It runs your aggregation function (like `SUM`) independently on each bucket.
4. It returns one row per bucket.

### The Syntax

```sql
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region;
```

**Result:**
| region | total_revenue |
|---|---|
| North | $50,000 |
| South | $75,000 |
| East | $30,000 |

### Grouping by Multiple Columns

You can group by multiple categories to create deeper pivot tables.
*"Show me the total revenue broken down by Region, and then by Product Category."*

```sql
SELECT region, category, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region, category
ORDER BY region;
```

### The Golden Rule of GROUP BY

This is the most common error in all of SQL:
**If you use `GROUP BY`, every single column in your `SELECT` statement MUST either be inside the `GROUP BY` clause, or wrapped in an Aggregation Function (`SUM`, `COUNT`, etc.).**

```sql
-- FATAL ERROR: What is 'sales_rep_name' supposed to be? 
-- There are 50 sales reps in the 'North' region, which one should SQL print next to the total?
SELECT region, sales_rep_name, SUM(revenue)
FROM sales
GROUP BY region;
```""",

    ("Filtering & Aggregating", "Filtering Groups (HAVING)"): """## Filtering After Aggregation

We know that `WHERE` is used to filter rows.
But what if we want to filter the *groups* created by `GROUP BY`?

Imagine a manager asks: *"Show me the total sales by region, **but only for regions that made more than $100,000 total**."*

### The Trap: Using WHERE

Your first instinct might be to write this:
```sql
-- THIS WILL THROW AN ERROR!
SELECT region, SUM(revenue) AS total_revenue
FROM sales
WHERE SUM(revenue) > 100000
GROUP BY region;
```
**Why does this fail?**
Because of the SQL Order of Execution.
1. `FROM` runs first.
2. `WHERE` runs second (filtering individual raw rows).
3. `GROUP BY` runs third (creating the buckets and calculating the `SUM`).

You cannot use `SUM(revenue)` in the `WHERE` clause because at the time the `WHERE` clause runs, the database hasn't grouped the data or calculated the sums yet!

### The Solution: HAVING

To filter *after* the aggregations have been calculated, SQL provides the **`HAVING`** clause. It acts exactly like `WHERE`, but it operates exclusively on aggregated groups.

```sql
-- CORRECT APPROACH
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
HAVING SUM(revenue) > 100000;
```

### Combining WHERE and HAVING

You will frequently use both in the same query.
- Use `WHERE` to filter raw rows *before* grouping (improves performance).
- Use `HAVING` to filter the aggregated results *after* grouping.

*"Show me the total 2023 revenue by region, but only for regions that made over $100k."*
```sql
SELECT region, SUM(revenue) AS total_revenue
FROM sales
WHERE sale_year = 2023    -- Filters raw rows BEFORE math happens
GROUP BY region
HAVING SUM(revenue) > 100000; -- Filters the final totals AFTER math happens
```""",

    ("Filtering & Aggregating", "Basic Subqueries"): """## Queries Inside Queries

Sometimes, answering a question requires multiple steps. 
*"Which employees earn more than the company average?"*

You cannot write `WHERE salary > AVG(salary)` because aggregation functions aren't allowed in the `WHERE` clause.
Historically, an analyst would run two separate queries:
1. `SELECT AVG(salary) FROM employees;` (Result: $60,000)
2. `SELECT first_name FROM employees WHERE salary > 60000;`

A **Subquery** (or Inner Query) allows you to combine these steps. You place a query inside parentheses, and the database runs the inner query first, using its result to filter the outer query.

### Single-Value Subqueries

If the inner query returns exactly one row and one column (a single value), you can use it with standard operators (`=`, `>`, `<`).

```sql
SELECT first_name, salary
FROM employees
WHERE salary > (
    -- This inner query runs first and resolves to a single number
    SELECT AVG(salary) 
    FROM employees
);
```

### Multi-Value Subqueries (IN)

If the inner query returns a list of values (a single column, but multiple rows), you cannot use `=` or `>`. You must use the `IN` operator.

*"Find the names of all customers who placed an order in the last 7 days."*

```sql
SELECT customer_name 
FROM customers
WHERE customer_id IN (
    -- This inner query resolves to a list of IDs: (10, 45, 92)
    SELECT DISTINCT customer_id 
    FROM orders
    WHERE order_date >= CURRENT_DATE - 7
);
```

### The Cost of Subqueries

While subqueries are logically intuitive, they can sometimes be slow on massive datasets because the database has to execute multiple separate queries. In modern data analysis, subqueries are often replaced by `JOIN`s or Common Table Expressions (CTEs) for better readability and performance.""",

    ("Advanced SQL Analytics", "INNER JOIN"): """## Connecting the Data

Because Relational Databases use Normalization (splitting data into separate tables), Data Analysts must constantly stitch data back together. 
If the CEO wants a report showing "Customer Name and Order Amount", you cannot find both in one table. Name is in `Customers`, Amount is in `Orders`.

The **`JOIN`** clause is the mechanism used to combine columns from two or more tables based on a related column between them (usually a Primary Key to Foreign Key relationship).

### The INNER JOIN

The `INNER JOIN` is the default and most common type of join. 
**It returns ONLY the rows that have a match in BOTH tables.**

Imagine a Venn Diagram. The `INNER JOIN` is the overlapping center. If a Customer has never placed an Order, they will NOT appear in the final result. If an Order somehow has an invalid Customer ID, it will NOT appear.

### The Syntax

You specify the two tables, and use the `ON` keyword to define exactly which columns link them together.

```sql
SELECT 
    customers.first_name, 
    orders.order_date, 
    orders.total_amount
FROM customers
INNER JOIN orders 
    ON customers.customer_id = orders.customer_id;
```

### Using Aliases for Cleanliness

Typing `customers.customer_id` repeatedly is tedious. Analysts always use Table Aliases (temporarily renaming tables to single letters) when performing JOINs.

```sql
SELECT c.first_name, o.order_date, o.total_amount
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id;
```

### Joining Multiple Tables

You can chain as many JOINs as you need to build a massive dataset.
*"Show Customer Name, Order Amount, and the Product Name they bought."*

```sql
SELECT c.first_name, o.total_amount, p.product_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN products p ON o.product_id = p.product_id;
```""",

    ("Advanced SQL Analytics", "LEFT JOIN"): """## Keeping the Unmatched Data

The `INNER JOIN` is strict: it requires a match in *both* tables. 
But what if the Marketing team asks: *"Show me a list of ALL our customers, and if they have placed an order, show the order amount. If they haven't placed an order, leave the amount blank."*

If you use an `INNER JOIN`, customers who haven't ordered yet are deleted from the results! 
To solve this, we use a **`LEFT JOIN`** (also known as a Left Outer Join).

### How LEFT JOIN Works

In a `LEFT JOIN`, the database looks at the "Left" table (the one written first, immediately after `FROM`). 
**It guarantees that EVERY row from the Left table will be included in the final result**, regardless of whether it finds a match in the Right table.

If it finds a match in the Right table, it pulls the data.
If it does NOT find a match, it fills the Right table's columns with `NULL`.

### The Syntax

```sql
-- 'customers' is the LEFT table. 'orders' is the RIGHT table.
SELECT c.first_name, o.total_amount
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id;
```

**Result:**
| first_name | total_amount |
|---|---|
| Alice | $50.00 |
| Bob | $100.00 |
| Charlie | **NULL** | *(Charlie exists in the database, but hasn't bought anything!)*

### Finding Missing Data

A brilliant use case for `LEFT JOIN` is finding "Orphans" (data that has no match). 
*"Find all users who registered but have NEVER placed an order."*

You use a `LEFT JOIN` to grab everyone, and then use the `WHERE` clause to filter for the ones that generated a `NULL` on the right side!

```sql
SELECT c.first_name, c.email
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL; -- The magic filter!
```""",

    ("Advanced SQL Analytics", "RIGHT JOIN"): """## The Inverse of Left Join

If a `LEFT JOIN` guarantees that every row from the Left table (Table A) is returned, a **`RIGHT JOIN`** guarantees that every row from the Right table (Table B) is returned, filling missing Left data with `NULL`.

### The Syntax

```sql
-- 'customers' is the LEFT table. 'orders' is the RIGHT table.
SELECT c.first_name, o.total_amount
FROM customers c
RIGHT JOIN orders o 
    ON c.customer_id = o.customer_id;
```

**Result:**
If there is an Order in the database with an invalid `customer_id` of 99, this query will return the Order Amount, but the `first_name` will be `NULL`.

### Why Data Analysts Rarely Use RIGHT JOIN

In practice, you will almost never write a `RIGHT JOIN`. Why? Because it is cognitively harder to read. 

Humans read English from top to bottom, left to right. When structuring queries, we naturally put the "Primary" or "Most Important" table first (in the `FROM` clause), and then attach secondary data to it. 

Any `RIGHT JOIN` can be instantly rewritten as a `LEFT JOIN` simply by swapping the order of the tables.

```sql
-- These two queries produce the exact same data!

-- The confusing way:
SELECT c.first_name, o.total_amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- The standard, readable way:
SELECT c.first_name, o.total_amount
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id;
```
For consistency and readability, most engineering teams enforce a strict style guide: **Always use `LEFT JOIN` and order your tables logically.**""",

    ("Advanced SQL Analytics", "FULL OUTER JOIN"): """## The Complete Picture

We know that `INNER JOIN` requires matches in both tables, `LEFT JOIN` keeps everything from Table A, and `RIGHT JOIN` keeps everything from Table B.

What if you want to keep **EVERYTHING** from both tables? You want all matched rows, plus all unmatched rows from Table A (filled with nulls on the right), plus all unmatched rows from Table B (filled with nulls on the left).

You use a **`FULL OUTER JOIN`** (often just written as `FULL JOIN`).

### The Use Case

`FULL OUTER JOIN` is incredibly rare in standard web application databases because Foreign Key constraints usually prevent "orphan" records on the right side. 

However, it is heavily used by Data Analysts when reconciling two completely different datasets from outside sources.

Imagine merging a list of Employees from the internal HR database, with a list of Employees from the external Payroll software, matching them by Email.
- You want to find employees who exist in HR but not in Payroll (maybe they haven't been onboarded yet).
- You want to find employees who exist in Payroll but not in HR (maybe a fired employee is accidentally still getting paid!).

### The Syntax

```sql
SELECT 
    hr.employee_name AS hr_name, 
    pay.employee_name AS payroll_name,
    hr.email
FROM hr_database hr
FULL OUTER JOIN payroll_database pay 
    ON hr.email = pay.email;
```

**Result:**
| hr_name | payroll_name | email |
|---|---|---|
| Alice | Alice | alice@test.com | *(Perfect match)* |
| Bob | **NULL** | bob@test.com | *(In HR, missing from Payroll)* |
| **NULL** | Charlie | charlie@test.com | *(In Payroll, missing from HR. Red Alert!)* |

*(Note: MySQL does not natively support `FULL OUTER JOIN`. To achieve this in MySQL, analysts must perform a `LEFT JOIN`, perform a `RIGHT JOIN`, and stitch them together using `UNION`).*""",

    ("Advanced SQL Analytics", "UNION and UNION ALL"): """## Stacking Data Vertically

`JOIN`s are used to combine data **horizontally** (adding new columns to your result set by linking tables).

But what if you have two tables with the exact same structure (e.g., `sales_2022` and `sales_2023`), and you want to combine them **vertically** into one massive list? 
You use the **`UNION`** operator.

### The Rules of UNION

To successfully stack two queries on top of each other, they must follow strict rules:
1. Both queries must return the exact same **number** of columns.
2. The columns must be in the exact same **order**.
3. The columns must have compatible **data types** (you cannot stack an Integer column on top of a Date column).

### UNION vs UNION ALL

**`UNION` (Removes Duplicates)**
If Alice is in the first table and also in the second table, standard `UNION` will perform a complex deduplication process and only return Alice once. Because it has to search the entire dataset to find duplicates, `UNION` is computationally expensive and slow.

**`UNION ALL` (Keeps Everything)**
This simply glues the second table to the bottom of the first table instantly. It is vastly faster. **Unless you explicitly need to remove duplicates, always use `UNION ALL`.**

### The Syntax

```sql
-- Query 1
SELECT first_name, email, 'Customer' AS role
FROM customers

UNION ALL

-- Query 2 (Notice the columns align perfectly!)
SELECT first_name, email, 'Employee' AS role
FROM employees;
```
*(Pro-tip: Notice how we hardcoded a string `'Customer'` and `'Employee'` as a new column in the `SELECT` statements? This is a common analyst trick so that when the data is combined, you still know which table each row came from!)*""",

    ("Advanced SQL Analytics", "Common Table Expressions (CTEs)"): """## Refactoring SQL for Humans

As business questions get harder, SQL queries get longer. 
Imagine a manager asks: *"Find the total revenue per department, but only for departments where the average employee salary is above $80,000."*

Historically, analysts wrote complex, deeply nested **Subqueries** to solve this. Subqueries are read from the inside-out, making 100-line SQL scripts an absolute nightmare to read and debug.

**Common Table Expressions (CTEs)** solve this. They allow you to write temporary, named result sets that exist only for the duration of the query. They allow you to write SQL from top-to-bottom, like reading a book.

### The WITH Keyword

You define a CTE using the `WITH` keyword at the very top of your file. You can define multiple CTEs, and later CTEs can even refer to earlier ones!

```sql
-- 1. Define the first temporary table (CTE)
WITH HighPaidDepartments AS (
    SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) > 80000
),

-- 2. Define a second CTE (optional)
DepartmentRevenue AS (
    SELECT department_id, SUM(amount) as total_rev
    FROM sales
    GROUP BY department_id
)

-- 3. The Final Query!
-- Now we simply JOIN our beautiful, clean temporary tables together.
SELECT d.department_name, rev.total_rev
FROM departments d
INNER JOIN HighPaidDepartments hp ON d.department_id = hp.department_id
INNER JOIN DepartmentRevenue rev ON d.department_id = rev.department_id;
```

### Why CTEs are the Industry Standard

1. **Readability**: The logic flows sequentially downward.
2. **Reusability**: If you need the `HighPaidDepartments` data twice in the final query, you can reference the CTE twice, instead of copy-pasting an ugly subquery twice.
3. **Debugging**: If the final query looks wrong, you can easily highlight and execute just the CTE block to test if the intermediate math is correct.""",

    ("Advanced SQL Analytics", "The CASE WHEN Statement"): """## If-Then Logic in SQL

Often, you need to create custom categories or clean up messy data directly inside your SQL query. 

For example, a table might have an `age` column, but the Marketing team wants a report grouped by "Age Brackets" (e.g., Youth, Adult, Senior). 
You cannot achieve this with standard filters. You need conditional `IF-THEN-ELSE` logic. 

In SQL, this is done using the **`CASE WHEN`** statement. It allows you to evaluate conditions row by row and output a specific value.

### The Syntax

The `CASE` statement acts as a single column in your `SELECT` clause. It evaluates conditions in order from top to bottom. As soon as a condition is True, it returns the result and skips the rest. If nothing is True, it returns the `ELSE` value.

```sql
SELECT 
    first_name,
    age,
    -- The CASE statement creates a brand new, virtual column
    CASE 
        WHEN age < 18 THEN 'Youth'
        WHEN age >= 18 AND age <= 64 THEN 'Adult'
        ELSE 'Senior' 
    END AS age_bracket
FROM customers;
```

### Advanced Use Case: Custom Aggregation (Pivot)

`CASE WHEN` is frequently combined with `SUM()` or `COUNT()` to pivot data horizontally without relying on Excel.

*"Show me the total number of orders, but broken down by status in separate columns."*

```sql
SELECT 
    customer_id,
    
    -- If status is Pending, count it as 1, else 0. Then SUM the 1s!
    SUM(CASE WHEN status = 'Pending' THEN 1 ELSE 0 END) AS pending_orders,
    
    SUM(CASE WHEN status = 'Shipped' THEN 1 ELSE 0 END) AS shipped_orders,
    
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders
    
FROM orders
GROUP BY customer_id;
```
This incredibly powerful technique (called "Conditional Aggregation") allows analysts to reshape rows into columns directly inside the database, ready for dashboarding.""",

    ("SQL Window Functions", "Introduction to OVER()"): """## The Pinnacle of SQL Analytics

Imagine a manager asks: *"Show me a list of all employees, their salary, and the average salary of their entire department next to it, so we can see who is underpaid."*

If you use `GROUP BY department` to get the average, SQL collapses the table into one row per department, and you lose the individual employee names!
If you don't use `GROUP BY`, you keep the names, but you can't calculate the department average!

Historically, this required complex self-joins. Today, we use **Window Functions**.

### What is a Window Function?

A Window Function performs calculations across a set of table rows (a "Window") that are related to the current row, **but it does NOT collapse the rows together.** It retains all original rows while adding a new column with the aggregated math.

### The OVER() Clause

The presence of the `OVER()` keyword tells SQL that the preceding function (like `SUM` or `AVG`) should act as a Window Function, not a standard `GROUP BY` aggregation.

```sql
SELECT 
    first_name, 
    department, 
    salary,
    -- Calculate the average, but partitioned (grouped) by department!
    AVG(salary) OVER(PARTITION BY department) AS dept_avg_salary
FROM employees;
```

### The PARTITION BY Keyword

Inside `OVER()`, the `PARTITION BY` acts exactly like `GROUP BY`. It defines the boundaries of the "Window". 
In the query above:
1. SQL looks at Alice in the Sales department.
2. It looks through the "Window" of all other Sales employees to calculate the average ($60k).
3. It prints Alice, her salary, and $60k.
4. It moves to Bob in the IT department. The "Window" shifts to IT, calculates the IT average, and prints Bob.

Every single employee is listed, but the math adapts perfectly to their specific department!""",

    ("SQL Window Functions", "RANK() vs DENSE_RANK()"): """## Creating Leaderboards

Ranking data is a daily task in Data Analysis.
*"Who are the top 3 salespeople in each region?"*
*"What are the 5 most viewed videos in every category?"*

You can't solve this with `ORDER BY` and `LIMIT`, because `LIMIT 3` only returns 3 rows for the *entire* table, not 3 rows *per region*.

To calculate a rank for each row within its specific group, we use the **`RANK()`** Window Function.

### The Syntax

Because `RANK()` is a Window Function, it requires the `OVER()` clause. 
Inside `OVER()`, we must use **`ORDER BY`** to tell the function *how* to determine the rank (e.g., highest sales gets Rank 1).

```sql
SELECT 
    sales_rep,
    region,
    total_sales,
    -- Partition resets the rank to 1 for every new region!
    RANK() OVER(
        PARTITION BY region 
        ORDER BY total_sales DESC
    ) AS regional_rank
FROM regional_sales;
```

### The Tie-Breaker Problem

What happens if Alice and Bob both have $10,000 in sales, tying for 2nd place? How is the 4th person (Charlie with $8,000) ranked?

There are two different ranking functions to handle ties:

**1. `RANK()` (Skips numbers)**
If Alice and Bob tie for 2nd, they both get Rank 2. Charlie gets **Rank 4**. (Rank 3 is skipped entirely). 
This matches Olympic medal rules.

**2. `DENSE_RANK()` (Never skips)**
If Alice and Bob tie for 2nd, they both get Rank 2. Charlie gets **Rank 3**.
This is often preferred in business analytics to ensure no ranks are missing.

### Filtering by Rank

Because Window Functions execute at the very end of the SQL query, you cannot put `WHERE regional_rank <= 3` in the main query. You must wrap the ranking query in a CTE (Common Table Expression), and filter the CTE!""",

    ("SQL Window Functions", "ROW_NUMBER()"): """## Generating Unique IDs

While `RANK()` and `DENSE_RANK()` assign identical numbers to tied values, sometimes you absolutely must have a strict, sequentially increasing number (1, 2, 3, 4...) with no duplicates, regardless of ties.

You use the **`ROW_NUMBER()`** Window Function.

### Removing Duplicates (Deduplication)

`ROW_NUMBER()` is the ultimate tool for cleaning dirty data in SQL.
Imagine a buggy tracking system accidentally logged three identical page views for a user at the exact same millisecond. You need to delete the duplicates and keep only one.

**The Strategy:**
1. You use `ROW_NUMBER()` partitioned by the User ID.
2. You order by the timestamp.
3. The first event gets row number 1, the duplicate gets 2, the third gets 3.
4. You filter the results to only keep `row_number = 1`.

```sql
WITH RankedEvents AS (
    SELECT 
        user_id, 
        event_time,
        event_type,
        -- Assigns 1, 2, 3 to identical events
        ROW_NUMBER() OVER(
            PARTITION BY user_id, event_type 
            ORDER BY event_time ASC
        ) as rn
    FROM tracking_logs
)

-- Now, keep only the first occurrence!
SELECT user_id, event_time, event_type
FROM RankedEvents
WHERE rn = 1;
```

### Finding the "Most Recent" Record

A classic interview question: *"We have a history table of employee salaries. Write a query to find the CURRENT salary of every employee."*

You partition by the `employee_id`, order by the `effective_date DESC` (so the newest date gets row number 1), and then filter for `rn = 1`.

```sql
WITH SalaryHistory AS (
    SELECT 
        employee_id, 
        salary,
        ROW_NUMBER() OVER(
            PARTITION BY employee_id 
            ORDER BY effective_date DESC
        ) as recent_rank
    FROM salaries
)
SELECT employee_id, salary FROM SalaryHistory WHERE recent_rank = 1;
```""",

    ("SQL Window Functions", "LEAD() Function"): """## Looking into the Future

In traditional SQL, every row is evaluated in complete isolation. Row 5 has no idea what data exists in Row 6. 

But time-series analysis often requires comparing a row to the row *after* it. 
*"How many days passed between a customer's first purchase and their second purchase?"*

To pull data from the "next" row into the "current" row, we use the **`LEAD()`** Window Function.

### How LEAD Works

`LEAD(column_name, offset)` looks ahead a specific number of rows and grabs a value.
- `LEAD(purchase_date, 1)` pulls the date from the very next row.
- `LEAD(purchase_date, 2)` pulls the date from two rows ahead.

### Calculating Time Between Events

To calculate the time between purchases, we partition the data by customer, order it chronologically, use `LEAD` to grab their *next* purchase date, and do math on the same line!

```sql
SELECT 
    customer_id,
    order_date AS current_purchase,
    
    -- Grab the date of this specific customer's NEXT order
    LEAD(order_date, 1) OVER(
        PARTITION BY customer_id 
        ORDER BY order_date ASC
    ) AS next_purchase_date
    
FROM orders;
```

**Result:**
| customer_id | current_purchase | next_purchase_date |
|---|---|---|
| 1 | 2023-01-01 | 2023-01-15 |
| 1 | 2023-01-15 | 2023-03-01 |
| 1 | 2023-03-01 | **NULL** | *(There is no next order!)* |

Now that both dates are on the exact same row, an analyst can simply wrap the query in a CTE and calculate `DATEDIFF(next_purchase_date, current_purchase)` to find the days between orders. This is the foundation of Customer Retention analysis.""",

    ("SQL Window Functions", "LAG() Function"): """## Looking into the Past

If `LEAD()` looks forward to the next row, **`LAG()`** looks backwards to the previous row. 
It is the most frequently used Window Function in business analytics, primarily used for calculating **Month-Over-Month (MoM) Growth**.

### Calculating Revenue Growth

If the CEO asks: *"What was our percentage revenue growth each month this year?"*

The formula for growth is: `(Current Month - Previous Month) / Previous Month`.
To do this in SQL, you must get the Current Month's revenue and the Previous Month's revenue onto the exact same row.

```sql
WITH MonthlySales AS (
    -- Step 1: Standard Group By to get total sales per month
    SELECT 
        month, 
        SUM(revenue) AS current_revenue
    FROM sales
    GROUP BY month
)
SELECT 
    month,
    current_revenue,
    
    -- Step 2: Use LAG to pull last month's revenue down to this row
    LAG(current_revenue, 1) OVER(
        ORDER BY month ASC
    ) AS previous_revenue
    
FROM MonthlySales;
```

**Result:**
| month | current_revenue | previous_revenue |
|---|---|---|
| Jan | $10,000 | **NULL** | *(No previous month exists!)* |
| Feb | $12,000 | $10,000 |
| Mar | $9,000 | $12,000 |

### Completing the Math

Now that `current_revenue` and `previous_revenue` are side-by-side on the March row, you can easily calculate the drop.

```sql
-- (9000 - 12000) / 12000 = -0.25 (-25% growth)
(current_revenue - previous_revenue) / previous_revenue AS growth_rate
```
*(Note: Always be careful when dividing by `previous_revenue`. If `previous_revenue` is 0 or NULL, the database will throw a "Divide by Zero" error. You must handle this using `CASE WHEN` or `NULLIF`).*""",

    ("SQL Window Functions", "Running Totals"): """## Cumulative Sums

A classic dashboard chart shows a line graph starting at zero in January and climbing up and to the right, showing "Total Revenue Year-To-Date". 

To plot this, you need a **Running Total** (or Cumulative Sum). 
- Jan: $10k
- Feb: $15k (Jan + Feb)
- Mar: $22k (Jan + Feb + Mar)

You calculate this using the standard `SUM()` function, but modified by a special Window Function `OVER()` clause that includes an **`ORDER BY`**.

### The Magic of ORDER BY inside OVER()

When you put an `ORDER BY` inside an `OVER()` clause with an aggregation function like `SUM`, SQL changes its behavior. Instead of summing the entire partition at once, it calculates the sum from the *start of the partition up to the current row*.

```sql
SELECT 
    date,
    daily_revenue,
    
    -- The Running Total!
    SUM(daily_revenue) OVER(
        ORDER BY date ASC
    ) AS cumulative_revenue
    
FROM daily_sales;
```

**Result:**
| date | daily_revenue | cumulative_revenue |
|---|---|---|
| Jan 1 | $100 | $100 |
| Jan 2 | $50 | $150 |
| Jan 3 | $200 | $350 |

### Partitioned Running Totals

What if you want a running total for 2022, and then you want the running total to reset back to zero on January 1st, 2023?

You simply add `PARTITION BY year` into the `OVER()` clause.

```sql
SELECT 
    date,
    year,
    daily_revenue,
    
    -- Resets the running total every time the year changes!
    SUM(daily_revenue) OVER(
        PARTITION BY year 
        ORDER BY date ASC
    ) AS ytd_revenue
    
FROM daily_sales;
```
This is the pinnacle of SQL reporting. Understanding how `PARTITION BY` (the boundary) and `ORDER BY` (the sequence) work together unlocks almost any complex analytical query.""",

    ("Python for Data Analysts", "Variables and Types"): """## The Foundation of Python

While SQL is the language for extracting data from databases, Python is the language for manipulating, cleaning, and visualizing that data. It is the undisputed king of Data Science.

### Variables

In Python, you do not need to explicitly declare the type of a variable (like you do in C or Java). You just assign a value to a name.

```python
# A variable holding an integer
age = 25 

# A variable holding a string
name = "Alice" 

# Reassignment is allowed
age = 26 
```

### Core Data Types for Analysis

Understanding data types is critical. You cannot multiply a string by a string.

1. **Integer (`int`)**: Whole numbers. `sales = 150`
2. **Float (`float`)**: Decimal numbers. `price = 19.99`
3. **String (`str`)**: Text, enclosed in single or double quotes. `category = "Electronics"`
4. **Boolean (`bool`)**: True or False (must be capitalized in Python). `is_active = True`

### Type Conversion (Casting)

Data from CSV files often imports as text, even if it looks like numbers. A common error is trying to do math on strings.

```python
revenue = "5000"
tax = "200"

print(revenue + tax) 
# Output: "5000200" (String concatenation!)

# You must cast (convert) the strings to integers first
real_revenue = int(revenue)
real_tax = int(tax)
print(real_revenue + real_tax) 
# Output: 5200
```

To check the type of a variable when debugging, use the `type()` function:
`print(type(revenue))` -> `<class 'str'>`""",

    ("Python for Data Analysts", "Lists and Indexing"): """## Working with Sequences

A Data Analyst rarely works with a single number. You work with thousands of numbers. The most basic way to store a sequence of items in Python is a **List**.

A List is an ordered, mutable (changeable) collection of items, enclosed in square brackets `[]`.

```python
# A list of integers
sales = [100, 250, 50, 400]

# A mixed list (allowed, but generally bad practice in data analysis)
mixed = [1, "Alice", True, 45.5]
```

### Zero-Based Indexing

To extract a specific item from a list, you use its Index. 
**Crucial Rule: Python is zero-indexed.** The first item is at index 0, not 1.

```python
fruits = ["Apple", "Banana", "Cherry", "Date"]

print(fruits[0]) # "Apple"
print(fruits[2]) # "Cherry"
```

### Negative Indexing

Python allows you to count backward from the end of the list using negative numbers. `-1` is always the last item. This is incredibly useful when you don't know how long the list is.

```python
print(fruits[-1]) # "Date"
print(fruits[-2]) # "Cherry"
```

### Slicing Lists

You can extract a sub-section of a list using a Slice: `list[start:stop]`.
- The `start` index is **inclusive**.
- The `stop` index is **exclusive** (it stops *before* this index).

```python
# Grab index 1 and 2, stop before 3
print(fruits[1:3]) # ["Banana", "Cherry"]

# If you omit the start, it defaults to 0
print(fruits[:2])  # ["Apple", "Banana"]

# If you omit the end, it goes to the end of the list
print(fruits[2:])  # ["Cherry", "Date"]
```""",

    ("Python for Data Analysts", "Dictionaries"): """## Key-Value Pairs

If Lists are good for an ordered sequence of similar items (like a single column of data), **Dictionaries** are good for representing a single entity with multiple attributes (like a single row of data).

A Dictionary is an unordered collection of Key-Value pairs, enclosed in curly braces `{}`. It is identical in structure to JSON.

### Creating and Accessing

```python
customer = {
    "id": 101,
    "name": "Alice",
    "email": "alice@test.com",
    "is_premium": True
}

# Access data using the Key in square brackets
print(customer["name"]) # "Alice"
```

### Modifying Dictionaries

Dictionaries are mutable. You can change existing values or add brand new Key-Value pairs dynamically.

```python
# Update an existing key
customer["is_premium"] = False

# Add a brand new key
customer["total_spent"] = 250.50
```

### Handling Missing Keys

A very common error in data processing is trying to access a key that doesn't exist, which instantly crashes your Python script.

```python
# ERROR! KeyError: 'phone'
print(customer["phone"]) 
```

To prevent this, use the `.get()` method. If the key exists, it returns the value. If the key doesn't exist, it gracefully returns `None` (or a default value of your choosing) instead of crashing.

```python
# Returns None
print(customer.get("phone")) 

# Returns "Unknown" if phone doesn't exist
print(customer.get("phone", "Unknown")) 
```

### Lists of Dictionaries

The most common way raw JSON data from an API is structured in Python is a List containing thousands of Dictionaries (essentially representing a database table).

```python
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# Get Bob's age
print(users[1]["age"]) # 30
```""",

    ("Python for Data Analysts", "For Loops in Data"): """## Automating Repetition

If you have a list of 10,000 sales figures and need to calculate the 10% tax on each, you cannot write 10,000 lines of code. You use a **For Loop** to automate the iteration.

A For Loop allows you to execute a block of code once for every item in a collection (like a List).

### The Basic Loop

```python
sales = [100, 200, 300]

# 'amount' is a temporary variable that takes the value 
# of the current item in the list for each iteration.
for amount in sales:
    tax = amount * 0.10
    print(f"Tax is: {tax}")
```

### Accumulator Pattern

The most common pattern in base Python data analysis is the Accumulator. You define an empty variable outside the loop, and update it inside the loop to calculate a total.

*"What is the total revenue in the list?"*
```python
sales = [100, 200, 300]
total_revenue = 0

for amount in sales:
    total_revenue = total_revenue + amount

print(total_revenue) # 600
```

### Filtering with If Statements inside Loops

You frequently combine Loops with `if` statements to filter data.

*"Create a new list containing only sales over 150."*
```python
sales = [100, 200, 50, 300]
high_sales = [] # Empty list to hold our results

for amount in sales:
    if amount > 150:
        high_sales.append(amount) # Add it to the new list

print(high_sales) # [200, 300]
```
*(Note: While base Python loops are foundational, when analyzing millions of rows later, we will use the Pandas library to avoid writing raw loops, as native Python loops are too slow for massive datasets).*""",

    ("Python for Data Analysts", "Functions for Reusability"): """## Writing Clean Code

If you write a complex block of code to clean a phone number (removing dashes, parentheses, and country codes), and you need to do this in 5 different places in your script, you should not copy and paste the code 5 times. 
If you find a bug later, you'd have to fix it in 5 places.

You should wrap the code in a **Function**. A function is a named, reusable block of code.

### Defining a Function

You define a function using the `def` keyword, followed by the name, parentheses for inputs (Arguments), and a colon. 

```python
def clean_phone_number(raw_phone):
    # This block is indented, so it belongs to the function
    cleaned = raw_phone.replace("-", "")
    cleaned = cleaned.replace("(", "")
    cleaned = cleaned.replace(")", "")
    cleaned = cleaned.replace(" ", "")
    
    # Return passes the final value back to whoever called it
    return cleaned
```

### Calling the Function

Defining the function doesn't execute the code. It just saves it in memory. To execute it, you "call" it by its name.

```python
user_input = "(555) 123-4567"
perfect_number = clean_phone_number(user_input)

print(perfect_number) # "5551234567"
```

### Multiple Arguments and Defaults

Functions can take multiple arguments, and you can provide default values so the user doesn't have to provide them every time.

```python
def calculate_tax(amount, tax_rate=0.05):
    return amount * tax_rate

# Uses the default 0.05
print(calculate_tax(100)) # 5.0

# Overrides the default with 0.10
print(calculate_tax(100, 0.10)) # 10.0
```""",

    ("Python for Data Analysts", "List Comprehensions"): """## The Pythonic Way

In the previous lessons, we used the Accumulator Pattern to filter and transform lists using a `for` loop, an `if` statement, and the `.append()` method.

```python
# The standard, bulky way
sales = [100, 200, 50, 300]
high_sales = []
for amount in sales:
    if amount > 150:
        high_sales.append(amount * 2)
```

Python provides a unique, elegant, and highly optimized syntactic sugar for this exact operation called a **List Comprehension**. It collapses the entire 4-line operation into a single, readable line of code.

### The Syntax

The syntax maps directly to the standard loop, but written inside square brackets:
`[ expression  for item in list  if condition ]`

```python
sales = [100, 200, 50, 300]

# The Pythonic Way
high_sales = [amount * 2 for amount in sales if amount > 150]

print(high_sales) # [400, 600]
```

### Breaking it down

1. **`for amount in sales`**: This is the exact same loop declaration. It iterates through the list.
2. **`if amount > 150`**: (Optional). This acts as a filter. If the condition is false, the item is skipped.
3. **`amount * 2`**: The Expression. This is what is actually appended to the new list. 

### Why Use Them?

1. **Readability**: Once you get used to the syntax, it reads much closer to English ("Give me the amount times two, for every amount in sales, if the amount is greater than 150").
2. **Performance**: Under the hood, Python executes List Comprehensions in C, making them significantly faster than writing a standard `for` loop in native Python. This matters when processing lists of 100,000 items.""",

    ("Pandas Masterclass", "Importing Pandas"): """## The Engine of Data Science

Raw Python is not built for Data Analysis. Lists and Dictionaries are too slow and lack built-in math functions. 
To do real Data Analysis in Python, the global industry standard is **Pandas**. 

Pandas is an open-source library that provides high-performance data structures (specifically, the DataFrame) and data analysis tools. It is essentially "SQL and Excel on steroids, controlled by Python."

### Installation

Pandas does not come with Python. You must install it using the package manager in your terminal:
`pip install pandas`

### The Standard Import Convention

In Python, you can import a library and give it an alias (a nickname) to save typing. 
The universal standard in the Data Science community is to import Pandas as `pd`. **Do not use any other alias.**

```python
import pandas as pd
```

### The Two Core Objects

Pandas introduces two fundamental data structures that you will use constantly:

1. **The Series**: A 1-Dimensional array. You can think of a Series as a single column of data (like a single column in Excel). It holds data of a single type (e.g., a Series of integers, or a Series of strings).

2. **The DataFrame**: A 2-Dimensional table made up of a collection of Series. It has rows and columns. It is the exact equivalent of an Excel spreadsheet or a SQL table. 99% of your work in Pandas revolves around manipulating DataFrames.

```python
import pandas as pd

# Creating a Series manually
ages = pd.Series([25, 30, 35])
print(ages)
```""",

    ("Pandas Masterclass", "Creating DataFrames"): """## Building the Table

A **DataFrame** is the core object in Pandas. It is a 2-dimensional labeled data structure with columns of potentially different types.

While you usually create DataFrames by loading external files (like CSVs), you can also create them manually from standard Python dictionaries. This is very common when creating small test datasets or converting JSON API responses into tabular data.

### From a Dictionary of Lists

The most intuitive way to build a DataFrame is using a Dictionary where the Keys are the Column Names, and the Values are Lists of data.

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

print(df)
```
**Output:**
```text
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
```

### The Index

Notice the `0, 1, 2` on the far left of the output? That is the **Index**.
Pandas automatically generates a row number for every row. 
Unlike SQL, where rows have no guaranteed order, a Pandas DataFrame is strictly ordered by its Index. You can actually replace these numbers with strings (like using the Customer's Name as the Index), which allows for incredibly fast data retrieval.

### Inspecting the DataFrame

Once created, you need to understand its structure.

```python
# Returns a tuple of (rows, columns) e.g., (3, 3)
print(df.shape) 

# Prints the data types of each column (Age is int64, Name is object/string)
print(df.dtypes) 
```""",

    ("Pandas Masterclass", "Reading CSVs"): """## Ingesting Real Data

Data Analysts rarely type data manually. Data lives in files. The most ubiquitous file format in data analysis is the **CSV (Comma-Separated Values)** file. 
It is a simple text file where each line is a row, and each column is separated by a comma.

### pd.read_csv()

Pandas provides a highly optimized, incredibly powerful function to read CSV files directly into a DataFrame.

```python
import pandas as pd

# Load the file into a DataFrame named 'df'
df = pd.read_csv("sales_data.csv")
```
That single line of code can load a 5-million-row CSV file into memory in seconds. It automatically detects the column headers and infers the correct data types (integers, floats, strings) for each column.

### Exploring the Data

If you just `print(df)` on a 5-million-row dataset, Python will truncate it, but it's still overwhelming. Analysts use specific methods to peek at the data.

```python
# Show only the first 5 rows (great for verifying the columns)
df.head()

# Show the last 5 rows
df.tail()

# Show a random sample of 10 rows
df.sample(10)
```

### High-Level Summaries

Before analyzing, you must understand the data quality.

```python
# Prints a technical summary: total rows, column names, 
# non-null counts, and memory usage.
df.info()

# Prints a statistical summary ONLY for numeric columns: 
# count, mean, standard deviation, min, max, and percentiles.
df.describe()
```
`df.describe()` is often the very first command an analyst runs to spot massive outliers (e.g., if the `Max` age in the dataset is 999, you know you have dirty data to clean!).""",

    ("Pandas Masterclass", "Selecting Columns"): """## Slicing the DataFrame

Once your data is loaded into a DataFrame `df`, you need to manipulate specific parts of it. 
Extracting columns in Pandas is very similar to extracting values from a Python Dictionary.

### Selecting a Single Column

To extract a single column, use square brackets `[]` and pass the column name as a string.

```python
# Extracts the 'Age' column
ages = df['Age']

print(type(ages)) # <class 'pandas.core.series.Series'>
```
Notice that extracting a single column returns a **Series**, not a DataFrame. A Series is just a 1D array.

*(Note: You can also use dot notation `df.Age`, but this is highly discouraged because it fails if the column name has a space, like `df.First Name`, or conflicts with a built-in Pandas method like `df.count`).*

### Selecting Multiple Columns

To extract multiple columns, you must pass a **List of strings** inside the square brackets. This means you will use double brackets `[[]]`.

```python
# The inner [] creates the list, the outer [] does the selection
subset_df = df[['Name', 'City']]

print(type(subset_df)) # <class 'pandas.core.frame.DataFrame'>
```
Extracting multiple columns returns a new **DataFrame**.

### Creating New Columns (Feature Engineering)

You can easily create a new column by assigning data to a column name that doesn't exist yet. Pandas performs "Vectorized Operations," meaning if you add two columns together, it automatically adds them row-by-row instantly, without you needing to write a `for` loop!

```python
# Create a new column 'Revenue' by multiplying 'Price' and 'Quantity'
df['Revenue'] = df['Price'] * df['Quantity']

# Create a fixed-value column
df['Tax_Rate'] = 0.05
```""",

    ("Pandas Masterclass", "Filtering Rows with loc"): """## The Pandas WHERE Clause

In SQL, we filter rows using `WHERE age > 30`. 
In Pandas, we use **Boolean Masking** and the `.loc[]` accessor.

### Boolean Masks

If you apply a condition to a column, Pandas doesn't return the filtered data immediately. It returns a Series of `True` and `False` values (a Mask) indicating whether each row passed the test.

```python
# Returns: 0: False, 1: True, 2: False...
mask = df['Age'] > 30 
```

### Applying the Mask with .loc[]

To actually filter the DataFrame, you pass this True/False mask into the `.loc[]` accessor. `.loc` stands for "Location based on Labels/Conditions".

```python
# This returns a new DataFrame containing ONLY the rows where Age > 30
older_staff = df.loc[df['Age'] > 30]
```
*(Note: `df[df['Age'] > 30]` also works, but `.loc` is the preferred, explicit standard in Pandas).*

### Multiple Conditions

You can combine conditions using `&` (AND) and `|` (OR). 
**CRITICAL RULE**: You MUST wrap each condition in parentheses, otherwise Python's order of operations will crash the code.

```python
# Find people over 30 who live in London
# Note the required ( ) around each condition!
london_seniors = df.loc[(df['Age'] > 30) & (df['City'] == 'London')]
```

### Filtering with .isin()

Just like the `IN` operator in SQL, Pandas has `.isin()` to filter based on a list of values.

```python
target_cities = ['London', 'Paris', 'Berlin']

# Find anyone who lives in one of the target cities
euro_staff = df.loc[df['City'].isin(target_cities)]
```""",

    ("Pandas Masterclass", "Using iloc"): """## Filtering by Absolute Position

We learned that `.loc[]` selects data based on *Labels* (e.g., column names like 'Age') or *Conditions* (Boolean masks).

But what if you just want to grab the 5th row and the 2nd column, regardless of what they are named? 
For absolute, integer-based positioning, you use **`.iloc[]`** (Integer Location).

### The Syntax of iloc

`.iloc` takes two arguments separated by a comma: `[row_indices, column_indices]`. 
It uses standard Python zero-based indexing and slicing (just like Lists).

```python
# Grab the very first row (Index 0), and all columns ( : )
first_row = df.iloc[0, :]

# Grab the first 5 rows, and the first 3 columns
subset = df.iloc[0:5, 0:3]

# Grab the last row using negative indexing
last_row = df.iloc[-1, :]
```

### The Difference Between loc and iloc

This is the most common point of confusion for beginners.

Imagine a DataFrame where you deleted the first 3 rows. The Index of the DataFrame now starts at `3, 4, 5...`.

- `df.loc[3]` will look for the row where the literal Index Label is the name '3'. (It will return the very first row in this truncated dataset).
- `df.iloc[3]` ignores the Index Labels entirely. It counts down from the top of memory and returns the 4th physical row in the dataset (which would be Index Label '6').

**Rule of Thumb:**
- Use `.loc[]` 95% of the time (Filtering by conditions, selecting by column names).
- Use `.iloc[]` only when you specifically need to slice data based on geometric position (e.g., slicing the matrix for Machine Learning algorithms).""",

    ("Pandas Masterclass", "Merging DataFrames"): """## The Pandas INNER JOIN

Data analysis often requires combining data from multiple CSV files. 
- File 1: `customers.csv` (Customer_ID, Name, Email)
- File 2: `orders.csv` (Order_ID, Customer_ID, Amount)

In SQL, we use `JOIN`. In Pandas, we use **`pd.merge()`**.

### The pd.merge() Function

You pass the two DataFrames into `pd.merge()`, specify which column links them (`on`), and specify the type of join (`how`).

```python
import pandas as pd

customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')

# INNER JOIN (Default)
# Keeps only rows where the Customer_ID exists in BOTH dataframes
merged_df = pd.merge(
    left=customers, 
    right=orders, 
    on='Customer_ID', 
    how='inner'
)
```

### Different Join Types

The `how` parameter accepts the standard SQL join types:
- `how='inner'`: Intersection (Matches only).
- `how='left'`: Keeps all rows from the Left DataFrame, fills missing Right data with `NaN` (Pandas' version of NULL).
- `how='right'`: Keeps all rows from the Right DataFrame.
- `how='outer'`: Keeps all rows from both DataFrames (FULL OUTER JOIN).

```python
# LEFT JOIN
# Keeps all customers. If they have no orders, their 'Amount' will be NaN.
all_customers_orders = pd.merge(
    customers, 
    orders, 
    on='Customer_ID', 
    how='left'
)
```

### Merging on Different Column Names

What if the customers table calls it `Customer_ID`, but the orders table calls it `Cust_ID`? 
You cannot use `on`. You must use `left_on` and `right_on`.

```python
merged = pd.merge(
    customers, 
    orders, 
    left_on='Customer_ID', 
    right_on='Cust_ID', 
    how='inner'
)
```""",

    ("Pandas Masterclass", "Groupby in Pandas"): """## The Pandas GROUP BY

Just like SQL, aggregating data by categories is the core of data analysis in Pandas. We use the `.groupby()` method.

The flow in Pandas is exactly the same as SQL:
1. **Split**: Split the data into buckets based on a column.
2. **Apply**: Apply an aggregation function (sum, mean, count) to a target column.
3. **Combine**: Combine the results back into a new DataFrame.

### Basic Grouping

*"What is the total revenue for each Region?"*

```python
import pandas as pd
df = pd.read_csv('sales.csv')

# 1. Group by Region
# 2. Select the Revenue column
# 3. Apply the sum() function
regional_revenue = df.groupby('Region')['Revenue'].sum()

print(regional_revenue)
# North    50000
# South    75000
```
*(Note: The result is a Series, where the 'Region' has become the Index).*

### Multiple Aggregations ( .agg() )

What if you want the Total Revenue AND the Average Revenue for each Region?
You use the `.agg()` method, passing a list of functions.

```python
# Returns a DataFrame with two columns: 'sum' and 'mean'
metrics = df.groupby('Region')['Revenue'].agg(['sum', 'mean'])
```

### Grouping by Multiple Columns

Just like SQL, you can group by multiple categories to create hierarchical data by passing a list to `.groupby()`.

```python
# Total revenue by Region, and then by Product Category
complex_group = df.groupby(['Region', 'Category'])['Revenue'].sum()
```

### Resetting the Index

`.groupby()` moves the grouped columns into the DataFrame's Index. This makes the data hard to manipulate further. 
Analysts almost always chain `.reset_index()` at the end of a groupby operation to push the Index back into standard columns, restoring the data to a flat, SQL-like table.

```python
# The industry standard workflow
final_df = df.groupby('Region')['Revenue'].sum().reset_index()
```""",

    ("Data Cleaning & Wrangling", "Identifying Missing Data"): """## The Reality of Real-World Data

In academic tutorials, datasets are perfect. In the real world, datasets are broken. Sensors fail to record, users skip optional form fields, and databases drop connections. 

Missing data in Pandas is represented as **`NaN`** (Not a Number) for numeric data, or `None` for objects.

Before you can run any machine learning algorithm or build a dashboard, you must find and deal with these missing values.

### Finding NaNs

The `.isna()` (or `.isnull()`) method returns a DataFrame of the exact same size, but filled with `True` (if it is missing) and `False` (if the data is present).
But looking at a 10,000-row grid of True/False is useless.

We chain `.sum()` to it! Because in Python `True` is treated as `1` and `False` as `0`, summing the columns instantly tells you exactly how many NaNs exist in each column.

```python
import pandas as pd
df = pd.read_csv('messy_data.csv')

# Prints the count of missing values per column
print(df.isna().sum())
```
**Output:**
```text
Customer_ID      0
Age             45
Income        1200
Email            0
dtype: int64
```
Here, we see `Customer_ID` is perfect, `Age` is missing 45 values, and `Income` is missing a massive 1200 values.

### Visualizing the Missing Data

To investigate *which* rows are missing data, we use the mask inside `.loc[]`:

```python
# Show me only the rows where Age is missing
missing_age_rows = df.loc[df['Age'].isna()]
```
Once you identify the missing data, you have three choices: Ignore it, Drop it, or Fill it (Imputation).""",

    ("Data Cleaning & Wrangling", "Dropping NaNs"): """## The Nuclear Option

If you have a dataset of 100,000 rows, and 5 rows are missing the `Age` value, the easiest and safest solution is simply to delete those 5 rows. Losing 5 rows out of 100,000 will not statistically alter your analysis.

We do this using the **`.dropna()`** method.

### Dropping Rows (Default)

By default, `.dropna()` will delete **any row** that contains at least one `NaN` in *any* column.

```python
# Drops the rows, but returns a new DataFrame. 
# It does NOT modify the original 'df' in place!
clean_df = df.dropna()

# To modify the original dataframe directly, use inplace=True
df.dropna(inplace=True) 
```

### Targeted Dropping (Subset)

Imagine your dataset has 10,000 rows. The `Income` column is missing 5,000 values, but the `Age` column is missing only 5 values.
If you run `df.dropna()`, it will delete 5,000 rows! You just destroyed half your dataset because of the `Income` column, even if your analysis is only about `Age`.

To safely drop rows only if they are missing data in a *specific* column, use the `subset` parameter.

```python
# Only deletes rows if 'Age' is missing. 
# Keeps rows where 'Income' is missing!
df.dropna(subset=['Age'], inplace=True)
```

### Dropping Columns

If a column is entirely useless (e.g., 99% of the values are `NaN`), you shouldn't drop the rows, you should drop the entire column! 
You change the `axis` parameter (0 = Rows, 1 = Columns).

```python
# Deletes the entire 'Income' column from the DataFrame
df.dropna(axis=1, thresh=5000, inplace=True) 
```
*(The `thresh=5000` means: Only keep columns that have at least 5000 non-NaN values).*""",

    ("Data Cleaning & Wrangling", "Filling Missing Values"): """## Data Imputation

Dropping rows is dangerous if you have a small dataset. If you have 100 rows and drop 20, you have destroyed 20% of your statistical power.

Instead of deleting the data, Data Scientists use **Imputation**: guessing the missing value based on the other data in the dataset.

We do this using the **`.fillna()`** method.

### 1. Filling with a Constant

If a column `Has_Premium_Subscription` is missing, you might logically assume the user does not have it. You can fill the `NaN`s with a hardcoded value like `False` or `0`.

```python
# Fills all NaNs in the 'Has_Premium' column with False
df['Has_Premium'].fillna(False, inplace=True)

# Fill text columns with a placeholder
df['City'].fillna("Unknown", inplace=True)
```

### 2. Filling with Statistical Measures (Mean/Median)

If the `Age` column is missing data, you cannot fill it with `0` (a 0-year-old customer ruins your demographics). 
The standard scientific approach is to fill the missing values with the **Mean** (Average) or **Median** of that specific column.

```python
# Calculate the average age of the known data
avg_age = df['Age'].mean()

# Fill the missing ages with the average
df['Age'].fillna(avg_age, inplace=True)
```
*Why use Median?* If your dataset includes Bill Gates, the Mean income will be $500 million. Filling a missing customer's income with $500 million destroys your analysis. The Median (the exact middle value) is immune to extreme outliers.

### 3. Forward Fill / Backward Fill

In Time-Series data (like a daily stock price), if Tuesday's data is missing, it is highly likely that Tuesday's price is very close to Monday's price.

You can use `method='ffill'` (Forward Fill) to tell Pandas to take the last known valid value and copy it forward into the missing slots.

```python
# If Monday is $100 and Tuesday is NaN, Tuesday becomes $100
df['Stock_Price'].fillna(method='ffill', inplace=True)
```""",

    ("Data Cleaning & Wrangling", "Removing Duplicates"): """## Fixing Double Entries

A very common data corruption issue is Duplicate Rows. 
- A user clicked "Submit Order" twice quickly on the frontend.
- A SQL `JOIN` was written poorly and multiplied the rows (a Cartesian explosion).

If you sum the revenue of a dataset with duplicates, you will falsely report inflated earnings to the CFO.

### Identifying Duplicates

The `.duplicated()` method returns a Boolean Mask (`True` if the row is an exact duplicate of an earlier row).

```python
# Count how many exact duplicate rows exist
duplicate_count = df.duplicated().sum()
print(f"Found {duplicate_count} duplicates!")

# View the actual duplicate rows to investigate WHY they exist
duplicates_df = df.loc[df.duplicated()]
```

### Removing Duplicates

The **`.drop_duplicates()`** method safely removes them. By default, it keeps the *first* occurrence of the row and deletes all subsequent identical rows.

```python
df.drop_duplicates(inplace=True)
```

### Targeted Deduplication (Subset)

By default, `.drop_duplicates()` only drops a row if **every single column** matches perfectly.

What if your dataset tracks `Customer_Logins`? 
- Row 1: `Alice | alice@test.com | 2023-10-01 10:00:00`
- Row 2: `Alice | alice@test.com | 2023-10-01 10:05:00`

Because the timestamps are different, Pandas will say these are NOT duplicates. But your business logic might dictate: *"We only care about unique users, not how many times they logged in."*

You use the `subset` parameter to tell Pandas to only look at specific columns when identifying duplicates.

```python
# Drops Row 2, keeping only the first time Alice appeared!
df.drop_duplicates(subset=['Email'], inplace=True)
```
*(You can use `keep='last'` to keep the most recent login instead!)*""",

    ("Data Cleaning & Wrangling", "Converting Data Types"): """## Fixing Bad Imports

When Pandas reads a CSV file, it attempts to guess the data type of each column. Usually, it gets it right. 
However, if a `Revenue` column contains 9,999 numbers, but a single cell contains the string `"100 Dollars"`, Pandas will panic and convert the *entire* column into strings (labeled as `object` in Pandas).

If you try to run `df['Revenue'].sum()`, it will concatenate the strings instead of doing math!

### Identifying Bad Types

Always check the types after loading data.

```python
print(df.dtypes)
# Age        int64
# Revenue    object  <-- RED FLAG! This should be a float!
# Date       object  <-- RED FLAG! This should be a datetime!
```

### The .astype() Method

If the data is clean but simply categorized wrong (e.g., a column of `1` and `0` loaded as integers, but you want them as Booleans), you use `.astype()`.

```python
# Convert 1/0 to True/False
df['Is_Active'] = df['Is_Active'].astype(bool)
```

### Fixing Dirty Numbers (pd.to_numeric)

If the column is a string because of dirty data (like `"100 Dollars"`), `.astype(float)` will crash, because Python doesn't know how to convert "Dollars" to a number.

You must use **`pd.to_numeric()`** combined with `errors='coerce'`. 
`coerce` is a magical parameter: it forces valid numbers into floats, and if it encounters un-convertible text (like "100 Dollars"), it safely replaces it with `NaN` instead of crashing!

```python
# Forces conversion, destroying text into NaNs
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

# Now you can safely use .fillna() and .sum()!
```

### Fixing Dates (pd.to_datetime)

Dates imported from CSVs are always strings. You cannot extract the "Month" from a string. You must convert it to a Pandas DateTime object.

```python
df['Date'] = pd.to_datetime(df['Date'])

# Now you have access to the magical .dt accessor!
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
```""",

    ("Data Cleaning & Wrangling", "String Manipulation"): """## Taming Text Data

While numeric data is the core of analysis, text data (Strings) is often the messiest. 
- You might have `Country` entered as `" USA"`, `"U.S.A"`, and `"united states"`.
- You might have full names that need to be split into First and Last names.

Pandas provides the **`.str`** accessor, allowing you to run standard Python string methods on an entire column simultaneously (vectorized).

### Standardizing Text

The easiest way to clean text is to standardize the capitalization and strip invisible whitespace (spaces at the beginning or end of the string).

```python
# Convert everything to lowercase
df['Country'] = df['Country'].str.lower()

# Remove leading/trailing spaces (e.g., " USA " becomes "USA")
df['Country'] = df['Country'].str.strip()
```

### Replacing Text

If you need to standardize variations (like replacing "U.S.A" with "usa"), use `.str.replace()`.

```python
df['Country'] = df['Country'].str.replace('u.s.a', 'usa')
```

### Splitting Columns

A very common requirement is splitting a single column into two based on a delimiter (like a comma or a space).

Imagine a column `Full_Name` containing `"Smith, John"`.

```python
# split() creates a List: ["Smith", "John"]
# expand=True forces the List to expand into two new DataFrame columns!
df[['Last_Name', 'First_Name']] = df['Full_Name'].str.split(', ', expand=True)
```

### Filtering by Substring

Just like SQL's `LIKE '%gmail%'`, you can use `.str.contains()` to create a Boolean mask for filtering.

```python
# Find all users with a gmail address
gmail_users = df.loc[df['Email'].str.contains('@gmail.com')]
```""",

    ("Exploratory Data Analysis & Viz", "Identifying Outliers"): """## Finding the Anomalies

An **Outlier** is a data point that differs significantly from other observations. 

If you are analyzing the average salary of a neighborhood, and Elon Musk moves in, the Mean salary will skyrocket to $100 Million. If you present this Mean to your boss, you are technically correct, but analytically wrong. Elon Musk is an outlier skewing the data.

### Identifying Outliers Mathematically

A standard way to find outliers is using the **Interquartile Range (IQR)**.
1. Sort the data from lowest to highest.
2. Find the 25th percentile (Q1) and 75th percentile (Q3).
3. The IQR is the distance between them (Q3 - Q1). The IQR represents the "middle 50%" of your normal data.
4. An outlier is defined as any value that is **1.5x IQR below Q1 or above Q3**.

```python
# Calculate Q1 and Q3
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

# Define the acceptable bounds
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Filter the DataFrame to show only the Outliers
outliers = df.loc[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
```

### Visualizing Outliers (Boxplots)

Math is good, but visuals are better. The **Boxplot** is a statistical chart specifically designed to show the IQR and flag outliers.

Using the Seaborn visualization library:
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Creates a Boxplot. 
# The "box" is the IQR. The "whiskers" are the bounds.
# Any data points drawn as individual dots outside the whiskers are Outliers!
sns.boxplot(x=df['Salary'])
plt.show()
```

Once identified, you must use domain knowledge to decide whether to drop the outlier (if it was a data entry error, like age = 999) or keep it (if it's a legitimate, rare event, like a massive Black Friday purchase).""",

    ("Exploratory Data Analysis & Viz", "Correlation Matrices"): """## Discovering Relationships

Exploratory Data Analysis (EDA) isn't just about looking at individual columns. It's about finding hidden relationships *between* columns.

- *"Does a higher Marketing Spend correlate with higher Revenue?"*
- *"Does a higher Age correlate with a lower Default Rate on a loan?"*

We measure this using the **Correlation Coefficient (Pearson's r)**, which ranges from -1 to 1.

- **1.0**: Perfect Positive Correlation (As X goes up, Y goes up exactly proportionately).
- **0.0**: No Correlation (The variables have absolutely nothing to do with each other).
- **-1.0**: Perfect Negative Correlation (As X goes up, Y goes down).

*Rule of thumb: A correlation above 0.7 (or below -0.7) is considered a strong relationship.*

### The df.corr() Method

Pandas can instantly calculate the correlation coefficient between every single numeric column in your DataFrame against every other numeric column, producing a matrix.

```python
import pandas as pd
df = pd.read_csv('housing_data.csv')

# Calculates the matrix
corr_matrix = df.corr()
print(corr_matrix)
```
**Output Example:**
```text
               Square_Feet  Price     Crime_Rate
Square_Feet    1.000        0.850     -0.100
Price          0.850        1.000     -0.650
Crime_Rate    -0.100       -0.650      1.000
```
*Insight*: Price and Square Feet are highly correlated (0.85). Price and Crime Rate are strongly negatively correlated (-0.65).

### Visualizing with a Heatmap

Looking at a grid of numbers is difficult for humans. Analysts use Seaborn to turn this matrix into a color-coded **Heatmap**.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Dark red = strong positive correlation
# Dark blue = strong negative correlation
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```
**CRITICAL WARNING:** *Correlation does not imply causation!* Just because Ice Cream Sales and Shark Attacks have a 0.9 correlation does not mean ice cream causes shark attacks. They are both caused by a third, hidden variable: Summer heat.""",

    ("Exploratory Data Analysis & Viz", "Intro to Matplotlib"): """## The Foundation of Python Visualization

Data is useless if you can't communicate it. While dashboards in Tableau are great for executives, Data Analysts use Python libraries to visualize data *while* they are exploring it.

The grandfather of all Python visualization libraries is **Matplotlib**. It is powerful, infinitely customizable, and admittedly, a bit clunky. (Modern libraries like Seaborn are actually built *on top* of Matplotlib).

### The Pyplot Interface

You interact with Matplotlib through its `pyplot` module, universally imported as `plt`.

```python
import matplotlib.pyplot as plt

# 1. Define the data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 25, 30]

# 2. Plot the data (creates a line chart in memory)
plt.plot(x_values, y_values)

# 3. Render the chart to the screen
plt.show()
```

### Formatting the Chart

A chart without labels is a cardinal sin in Data Analysis. You must use Matplotlib's functions to add context before calling `plt.show()`.

```python
plt.plot(x_values, y_values, color='blue', marker='o')

# Add Labels
plt.title("Revenue Growth Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# Add a grid for readability
plt.grid(True)

plt.show()
```

### The Object-Oriented Interface (Advanced)

While `plt.plot()` is easy, professional data scientists use Matplotlib's Object-Oriented interface. This creates a Figure (the blank canvas) and Axes (the actual chart), allowing you to draw multiple sub-plots on the same canvas.

```python
# Creates a canvas (fig) with one chart (ax)
fig, ax = plt.subplots(figsize=(10, 6))

# Call methods on the specific chart object
ax.plot(x_values, y_values)
ax.set_title("Professional Chart")

plt.show()
```""",

    ("Exploratory Data Analysis & Viz", "Bar and Line Charts"): """## Choosing the Right Chart

The biggest mistake junior analysts make is choosing a chart because it looks cool (like a 3D Pie Chart), rather than choosing a chart that clearly communicates the data.

### 1. Line Charts (Trends over Time)

Line charts should be used almost exclusively for **Time Series** data. If the X-axis is a date or a time period, use a line chart. The continuous line implies a passage of time from one point to the next.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('monthly_sales.csv')

plt.plot(df['Month'], df['Revenue'])
plt.title("Monthly Revenue Trend")
plt.show()
```
*Never use a line chart if the X-axis is categorical (like "Regions"). A line connecting "North America" to "Europe" implies a chronological relationship that doesn't exist.*

### 2. Bar Charts (Comparing Categories)

Bar charts are the workhorse of Data Analysis. They are used to compare aggregated metrics across discrete **Categories**.
- X-axis: Categorical buckets (Regions, Product Types, User Segments).
- Y-axis: A numeric aggregation (Sum, Average, Count).

```python
# First, use Pandas to group the data!
category_sales = df.groupby('Category')['Revenue'].sum()

# Plot the grouped data using a Bar Chart
plt.bar(category_sales.index, category_sales.values, color='green')
plt.title("Total Revenue by Product Category")
plt.ylabel("Total Revenue")
plt.show()
```

### Horizontal Bar Charts

If your category names on the X-axis are very long (e.g., "Enterprise Software Solutions"), they will overlap and become unreadable.
The professional solution is to flip the chart horizontally using `plt.barh()`. Now the long text runs horizontally along the Y-axis and is perfectly readable.""",

    ("Exploratory Data Analysis & Viz", "Scatter Plots"): """## Visualizing Correlation

If you want to understand the relationship between two continuous numerical variables, you cannot use a Bar Chart or a Line Chart. You must use a **Scatter Plot**.

A Scatter Plot renders every single row in your dataset as an individual dot. The dot's position is determined by its value on the X-axis (Variable 1) and Y-axis (Variable 2).

### Building a Scatter Plot

*"Does spending more money on advertising result in higher sales?"*

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('marketing_data.csv')

# x = Ad_Spend (The independent variable we control)
# y = Revenue (The dependent variable we are measuring)
plt.scatter(df['Ad_Spend'], df['Revenue'], alpha=0.5)

plt.title("Ad Spend vs Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.show()
```
*(Pro-Tip: The `alpha=0.5` makes the dots 50% transparent. When you plot 10,000 dots, they overlap. Transparency allows you to see the density of overlapping dots).*

### Reading a Scatter Plot

When you look at the cloud of dots, you are looking for a trend:
1. **Positive Correlation**: The cloud moves from the bottom-left to the top-right (More Ad Spend = More Revenue).
2. **Negative Correlation**: The cloud moves from top-left to bottom-right (Higher Car Mileage = Lower Sale Price).
3. **No Correlation**: The dots look like a random shotgun blast. (No relationship).

### Adding a Third Dimension

You can pack more data into a 2D Scatter Plot by changing the color or size of the dots based on a third categorical variable.
Using Seaborn makes this incredibly easy:

```python
import seaborn as sns

# hue='Region' automatically colors the dots based on their region!
sns.scatterplot(
    data=df, 
    x='Ad_Spend', 
    y='Revenue', 
    hue='Region'
)
plt.show()
```""",

    ("Exploratory Data Analysis & Viz", "Seaborn Heatmaps"): """## Visualizing Density

Matplotlib is powerful, but writing the code is tedious. **Seaborn** is a statistical visualization library built on top of Matplotlib that makes complex charts beautiful with a single line of code.

One of the most powerful tools in an analyst's toolkit is the **Heatmap**. It is used to visualize data density in a 2D grid using color intensity.

### The Correlation Heatmap

We saw this briefly earlier. It is the absolute fastest way to find relationships in a massive dataset.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Calculate the correlation matrix in Pandas
corr_matrix = df.corr()

# 2. Pass the matrix directly into Seaborn
# annot=True prints the decimal numbers inside the colored boxes
# cmap='coolwarm' uses Blue for negative, Red for positive correlation
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```

### Pivot Table Heatmaps (Cohort Analysis)

Heatmaps are brilliant for visualizing **Cohort Analysis** (e.g., User Retention over time).
Imagine you have a Pandas Pivot Table showing "Month User Signed Up" on the Y-axis, "Month since Signup" on the X-axis, and the percentage of users still active as the value.

Reading a grid of 100 percentages is exhausting. If you pass that Pivot Table into a Heatmap, the high retention months turn dark blue, and the low retention months turn pale white. The human eye instantly detects the trend: *"Ah, users who signed up in July dropped off massively by Month 3."*

```python
# Create a pivot table counting total sales by Day and Hour
pivot_data = df.pivot_table(
    index='DayOfWeek', 
    columns='HourOfDay', 
    values='Sales', 
    aggfunc='sum'
)

# Visualize peak shopping hours instantly!
sns.heatmap(pivot_data, cmap='YlGnBu')
plt.title("Sales Density by Day and Hour")
plt.show()
```""",

    ("BI Dashboards & DAX", "Tableau: Dimensions vs Measures"): """## The Philosophy of BI Tools

While Python (Pandas/Matplotlib) is incredible for exploratory analysis, business executives don't want to run Python scripts. They want interactive, click-and-drag **Dashboards** that update daily.

The two industry titans of Business Intelligence (BI) are **Tableau** and **Microsoft Power BI**. 

To use either tool effectively, you must understand a fundamental concept they both share: the strict division of data into **Dimensions** and **Measures**.

### Measures (The "What")

Measures (often colored Green in Tableau) are **quantitative, numerical values** that can be mathematically aggregated (Summed, Averaged, Counted).

- Examples: `Revenue`, `Profit`, `Quantity_Sold`, `Discount_Rate`.
- Test: Does it make logical sense to calculate an Average of this column? If yes, it's a Measure.

### Dimensions (The "How")

Dimensions (often colored Blue in Tableau) are **qualitative, categorical fields** used to slice, group, or filter the Measures.

- Examples: `Region`, `Product_Category`, `Customer_Name`, `Order_Date`.
- Test: You cannot calculate the "Average" of a Region. But you *can* use a Region to group the Revenue.

### The Drag-and-Drop Magic

When you build a chart in Tableau:
1. You drag a **Measure** (`Revenue`) into the view. Tableau instantly calculates a single grand total (`SUM(Revenue)`).
2. You drag a **Dimension** (`Region`) into the view. Tableau instantly splits that single grand total into individual bars for North, South, East, and West.

This is exactly the same concept as `GROUP BY` in SQL. The Dimension is the `GROUP BY` column, and the Measure is the `SUM()` aggregation.

*Warning:* Sometimes a numeric column is actually a Dimension! For example, `Customer_ID = 1005`. Tableau might assume it's a Measure and try to `SUM(Customer_ID)`. Summing IDs makes zero sense. You must manually right-click the field in Tableau and convert it to a Dimension!""",

    ("BI Dashboards & DAX", "Tableau: Calculated Fields"): """## Extending the Data

When you connect Tableau to a SQL database or Excel file, you are given a specific set of Dimensions and Measures.
But what if the database has `Revenue` and `Cost`, but lacks a column for `Profit`?

You do not need to go back to the database or Python to create it. You create a **Calculated Field** directly inside Tableau.

### Row-Level Calculations

A row-level calculation executes logic on every single individual row in the dataset *before* any aggregation happens.

**Creating Profit:**
You open the Calculated Field editor in Tableau and write:
`[Revenue] - [Cost]`

Tableau creates a new Measure called "Profit". If you drag it into a chart grouped by Region, Tableau will calculate the profit for every row, and then `SUM` those profits by Region.

### Aggregate Calculations

This is where beginners make fatal errors.
What if you want to calculate the `Profit Margin` (Profit / Revenue)?

**The Wrong Way (Row-Level):**
`[Profit] / [Revenue]`
If you do this, Tableau will calculate the margin for Row 1 (10%), Row 2 (20%), and Row 3 (15%). When you drag it into the view, Tableau will try to `SUM` them together (10% + 20% + 15% = 45% Margin). This is mathematically completely invalid! You cannot sum ratios.

**The Right Way (Aggregated):**
You must tell Tableau to aggregate the totals *first*, and then divide the grand totals.
`SUM([Profit]) / SUM([Revenue])`

### Conditional Logic (IF-THEN)

Calculated fields support logic identical to SQL's `CASE WHEN`. This is incredibly useful for creating custom Dimensions for dashboard filtering.

```sql
// Create a new Dimension called "Order Size"
IF [Revenue] > 1000 THEN "High Value"
ELSEIF [Revenue] > 100 THEN "Medium Value"
ELSE "Low Value"
END
```
You can now drag this new "Order Size" field into a pie chart!""",

    ("BI Dashboards & DAX", "Power BI: Data Modeling"): """## The Star Schema

While Tableau thrives on visualizing single, massive "flat" tables of data, **Microsoft Power BI** thrives on building complex, relational data models (like a mini SQL database running in memory).

When you import 5 different CSV files into Power BI (Sales, Customers, Products, Dates), Power BI doesn't merge them into one giant table. It creates a **Data Model** using relationships.

### The Star Schema Architecture

The industry standard way to model data in Power BI is the **Star Schema**. It dictates that your tables must be split into two types: Fact Tables and Dimension Tables.

**1. Fact Table (The Center of the Star)**
This table holds the quantitative, transactional data (The Measures). It is massive, containing millions of rows, but very few columns. It primarily contains Foreign Keys and numbers.
- Example: `Sales_Table` (`Date_ID`, `Product_ID`, `Customer_ID`, `Quantity`, `Revenue`).

**2. Dimension Tables (The Points of the Star)**
These tables hold the descriptive attributes (The Dimensions) used to filter the Fact Table. They are small, containing unique Primary Keys.
- Example: `Products_Table` (`Product_ID`, `Product_Name`, `Category`, `Supplier`).
- Example: `Customers_Table` (`Customer_ID`, `Name`, `State`, `Age_Group`).

### Creating the Relationships

In the "Model View" of Power BI, you drag a line connecting the Primary Key (`Product_ID` in the Products table) to the Foreign Key (`Product_ID` in the Sales table).

This creates a **One-to-Many (1:*)** relationship. One product exists in the Dimension table, but it can appear Many times in the Sales Fact table.

### Why the Star Schema?

1. **Performance**: Power BI's underlying VertiPaq engine is heavily optimized for Star Schemas. It compresses the data massively, allowing sub-second filtering on 100 million rows.
2. **Filter Propagation**: When a user clicks "Electronics" on a dashboard filter (from the Products table), Power BI follows the relationship arrow down into the Sales table and instantly filters the billions of sales rows to only show Electronics revenue.""",

    ("BI Dashboards & DAX", "DAX: Introduction"): """## The Brain of Power BI

If you want to perform complex calculations in Power BI, you cannot use Python or standard SQL. You must use **DAX (Data Analysis Expressions)**.

DAX looks deceptively similar to Excel formulas, but it operates entirely differently. Excel formulas calculate on physical *Cells* (e.g., `A1 + B1`). DAX operates on entire *Columns* and *Tables*, heavily relying on the underlying Star Schema relationships.

### Calculated Columns vs Measures

There are two primary ways to write DAX. Choosing the wrong one will destroy your dashboard's performance.

**1. Calculated Columns (Avoid when possible)**
A Calculated Column evaluates row-by-row and physically saves the result into the database, increasing your file size.
```dax
-- Evaluates for every single row in the Sales table
Profit_Column = Sales[Revenue] - Sales[Cost]
```
Use this ONLY if you need to use the result as a Dashboard Filter/Slicer (e.g., creating an "Age Bracket" category).

**2. Measures (The Gold Standard)**
A Measure does NOT save data to the table. It is a formula that is calculated **on the fly, in RAM, at the exact moment a user clicks a chart.**
```dax
Total_Revenue = SUM(Sales[Revenue])
```
Because Measures are calculated dynamically, their result changes instantly based on whatever Filters the user has clicked on the dashboard!

### Filter Context

The most important concept in DAX is **Filter Context**. 

If you write `Total_Revenue = SUM(Sales[Revenue])` and drag it onto a Bar Chart grouped by `Region`:
1. Power BI looks at the "North" bar.
2. It applies a hidden Filter Context: `Region = "North"`.
3. The Measure executes `SUM(Sales[Revenue])`, but only on the filtered rows.
4. It repeats this for the "South" bar.

Understanding that every DAX Measure executes under an invisible, dynamic Filter Context dictated by the user's clicks is the key to mastering Power BI.""",

    ("BI Dashboards & DAX", "DAX: CALCULATE"): """## The Most Powerful Function in DAX

By default, a DAX Measure calculates its result based on the filters currently selected on the dashboard (the Filter Context). 

But what if you need a Measure to *ignore* the dashboard filters, or apply its own hidden filters? 

*"The dashboard is currently filtered to show 2023 Revenue. But I want a card next to it showing 2022 Revenue for comparison, regardless of the filter!"*

You use the **`CALCULATE()`** function. It is the only function in DAX that can modify the Filter Context.

### The Syntax

`CALCULATE( <Expression>, <Filter 1>, <Filter 2>... )`

```dax
-- 1. Create a base Measure
Total_Revenue = SUM(Sales[Revenue])

-- 2. Create a modified Measure using CALCULATE
Revenue_2022 = CALCULATE(
    [Total_Revenue],       -- The math to perform
    Dates[Year] = 2022     -- The forced filter!
)
```

### Overriding the Dashboard

If a user clicks a slicer setting the dashboard to `Year = 2023`:
- `[Total_Revenue]` will return the sum for 2023.
- `[Revenue_2022]` intercepts the context. It deletes the user's `2023` filter, forcibly applies its own `2022` filter, and returns the 2022 sum!

### Complex Conditional Logic

`CALCULATE` replaces the need for complex `IF` statements. You can chain multiple filters together.

*"Calculate the total revenue, but only for Premium customers in Canada."*

```dax
Premium_Canada_Rev = CALCULATE(
    [Total_Revenue],
    Customers[Tier] = "Premium",
    Customers[Country] = "Canada"
)
```
If you master `CALCULATE`, you have mastered 80% of the complexity of Power BI development.""",

    ("BI Dashboards & DAX", "DAX: SUMX"): """## Iterating Row by Row

We know that DAX Measures like `SUM(Sales[Revenue])` aggregate an entire column at once. 

But what if your Fact Table doesn't have a `Revenue` column? What if it only has `Quantity` and `Unit_Price`?
If you try to write a Measure like `Total_Revenue = SUM(Sales[Quantity] * Sales[Unit_Price])`, Power BI will throw an error. The standard `SUM()` function can only accept a single column as an argument; it cannot do math across two columns.

To do row-by-row math and *then* sum the result, you must use an **Iterator Function**: **`SUMX()`**.

### The X Functions

Any DAX function ending in "X" (`SUMX`, `AVERAGEX`, `MINX`) is an Iterator. It requires two arguments: a Table to iterate over, and the Expression to evaluate for every row.

### The Syntax

```dax
Total_Revenue = SUMX(
    Sales,                                 -- The table to iterate through
    Sales[Quantity] * Sales[Unit_Price]    -- The row-level math
)
```

### How SUMX Works Under the Hood

1. `SUMX` creates a temporary, invisible memory space.
2. It looks at Row 1 of the `Sales` table. It multiplies Quantity (2) * Price ($10). It saves $20 in memory.
3. It moves to Row 2. Quantity (1) * Price ($50). It saves $50 in memory.
4. It iterates through all 10 million rows.
5. Finally, it sums up all the temporary numbers in memory (20 + 50...) and returns the Grand Total.

### Performance Warning

`SUMX` forces Power BI to evaluate math row-by-row. On massive datasets, complex iterators can slow down your dashboard rendering. 

If the calculation is static and simple (like Quantity * Price), it is often better to create a physical Calculated Column in the database for `Revenue`, and then use a fast, standard `SUM()` Measure on it.""",

    ("BI Dashboards & DAX", "DAX: FILTER"): """## Advanced Context Manipulation

We learned that `CALCULATE()` can apply simple filters: `CALCULATE([Revenue], Country = "Canada")`.

However, the simple filter argument (`Country = "Canada"`) has a strict limitation in DAX: it cannot reference a Measure. 
You CANNOT write: `CALCULATE([Revenue], [Total_Sales] > 1000)`. Power BI will throw a syntax error.

To filter a calculation based on complex logic or another Measure, you must use the **`FILTER()`** function inside your `CALCULATE()`.

### The FILTER() Function

`FILTER(<table>, <condition>)` is an Iterator function. It scans an entire table row-by-row, evaluates a complex condition, and returns a smaller, invisible virtual table containing only the rows that passed.

### Using FILTER inside CALCULATE

*"Calculate the total revenue, but ONLY from customers who have a lifetime total spend of over $10,000."*

```dax
High_Value_Revenue = CALCULATE(
    [Total_Revenue],
    
    -- We pass a virtual, filtered table into CALCULATE
    FILTER(
        Customers,                      -- Iterate through the Customers table
        [Total_Revenue] > 10000         -- Evaluate this complex Measure for each customer
    )
)
```

### Why this is powerful

The `FILTER()` function allows you to use full DAX power inside your conditions. You can use `OR` statements, compare columns from different tables, or rely on dynamic Measures.

**Performance Warning:** 
Because `FILTER()` is an iterator, writing `FILTER(Sales, ...)` will force Power BI to scan the 100-million-row Fact Table row-by-row every time a user clicks the dashboard. This will crash the visual.

*Pro-Tip*: Always try to use `FILTER()` on small Dimension tables (like the `Customers` table, which only has 50,000 rows), and let the Star Schema relationship naturally filter the massive Sales table down the line!""",

    ("Statistical Analysis & A/B Testing", "Mean, Median, and Mode"): """## Measures of Central Tendency

Descriptive statistics summarize massive datasets into single numbers that describe the "center" of the data. The three most common are Mean, Median, and Mode.

### 1. The Mean (Average)

Calculated by adding all values together and dividing by the total number of values.
- **Formula**: `(Sum of all values) / N`
- **Use Case**: Great for normally distributed data (like the height of adult men).
- **The Flaw**: It is highly sensitive to **Outliers**. If 9 people earn $50k, and 1 CEO earns $5 Million, the Mean salary is $545k. This number completely misrepresents the group.

### 2. The Median (The Middle)

If you sort all values from lowest to highest, the Median is the exact middle number. (If there is an even number of values, it is the average of the two middle numbers).
- **Use Case**: This is the absolute standard for skewed data (Income, House Prices, Time spent on a webpage).
- **The Benefit**: It is completely immune to outliers. In the example above, the Median salary remains exactly $50k, correctly representing the group.

### 3. The Mode (The Most Frequent)

The value that appears most often in the dataset.
- **Use Case**: Crucial for categorical data. You cannot calculate the Mean of "Eye Color" or "Car Brand". The Mode tells you the most popular category (e.g., "The Mode car color is Silver").

### Python Implementation

```python
import pandas as pd

df = pd.DataFrame({'Salary': [50, 50, 50, 50, 5000]})

print("Mean:", df['Salary'].mean())     # Mean: 1040
print("Median:", df['Salary'].median()) # Median: 50
print("Mode:", df['Salary'].mode()[0])  # Mode: 50
```
*Analytical Rule: Whenever a dataset involves money or time, report the Median, not the Mean.*""",

    ("Statistical Analysis & A/B Testing", "Variance and Standard Deviation"): """## Measuring the Spread

Knowing the center of the data (Mean) is only half the story. You must also know how spread out the data is.

Imagine two delivery companies claiming their average delivery time is 3 days.
- **Company A**: Deliveries take exactly 3 days, every single time.
- **Company B**: Deliveries take 1 day half the time, and 5 days the other half. The average is 3, but the experience is wildly unpredictable!

We measure this unpredictability (the spread) using **Variance** and **Standard Deviation**.

### Variance

Variance measures how far, on average, each data point is from the Mean.
1. Find the Mean.
2. Subtract the Mean from every single data point to find the "deviation".
3. Square each deviation (to make negative numbers positive).
4. Find the average of those squared numbers.

*The problem with Variance*: Because we squared the numbers, the unit of measurement is squared (e.g., "Dollars Squared"), which is unreadable to humans.

### Standard Deviation (σ)

To fix the unit problem, we simply take the **Square Root of the Variance**. 
This is the **Standard Deviation**. It brings the metric back to the original unit (e.g., "Dollars" or "Days").

A high standard deviation means the data is widely spread out (Company B). A low standard deviation means the data is tightly clustered around the mean (Company A).

### Python Implementation

```python
import pandas as pd

company_a = pd.Series([3, 3, 3, 3, 3])
company_b = pd.Series([1, 1, 3, 5, 5])

print("A Mean:", company_a.mean(), "| Std Dev:", company_a.std()) 
# A Mean: 3.0 | Std Dev: 0.0

print("B Mean:", company_b.mean(), "| Std Dev:", company_b.std()) 
# B Mean: 3.0 | Std Dev: 2.0
```
*Insight*: Company B's standard deviation of 2.0 tells us that most deliveries fluctuate by 2 days away from the average.""",

    ("Statistical Analysis & A/B Testing", "Normal Distributions"): """## The Bell Curve

When you plot the frequency of naturally occurring continuous data (like human heights, IQ scores, or shoe sizes) on a histogram, it almost always forms a symmetrical bell shape.

This is the **Normal Distribution**. It is the foundation of modern statistics.

### Properties of the Normal Curve

1. It is perfectly symmetrical around the center.
2. The Mean, Median, and Mode are all exactly the same number (the peak of the bell).
3. The tails get closer and closer to zero, but technically stretch to infinity.

### The Empirical Rule (68-95-99.7)

If you know a dataset is Normally Distributed, and you know its Mean (average) and Standard Deviation (spread), you can instantly predict the distribution of the entire dataset using the Empirical Rule:

- **68%** of all data points fall within **1 Standard Deviation** of the mean.
- **95%** of all data points fall within **2 Standard Deviations** of the mean.
- **99.7%** of all data points fall within **3 Standard Deviations** of the mean.

### Real-World Example

Imagine the average score on a Math Test is **70** (Mean), with a Standard Deviation of **10**.

1. 68% of students scored between 60 and 80. `(70 ± 10)`
2. 95% of students scored between 50 and 90. `(70 ± 20)`
3. 99.7% of students scored between 40 and 100. `(70 ± 30)`

If a student scores a 95 on this test, they are more than 2 standard deviations above the mean. You instantly know they scored in the top ~2.5% of the class.

In Data Analysis, recognizing if your data is Normally Distributed is critical, because most advanced statistical tests (like t-tests and ANOVAs) mathematically assume your data follows this bell curve!""",

    ("Statistical Analysis & A/B Testing", "Understanding P-Values"): """## The Metric of Statistical Significance

You run an A/B test changing a website button from Blue to Red. 
- Blue Button (Control): 5.0% Conversion Rate
- Red Button (Variant): 5.2% Conversion Rate

The Red button won! You should change the website, right?
**Wrong.** What if you only tested 100 people? The 0.2% difference could just be random luck (variance).

To prove the result is real and not just luck, Data Scientists calculate a **p-value**.

### What is a P-Value?

A p-value (Probability Value) ranges from 0.0 to 1.0. 
It answers a very specific, backwards question: **"Assuming the Red button and Blue button are actually identical, what is the probability of seeing a 0.2% difference just by pure random chance?"**

- If the p-value is **0.40**: There is a 40% chance this result is just random noise. Do NOT change the website.
- If the p-value is **0.03**: There is only a 3% chance this is random noise. The result is likely real!

### The Alpha Threshold (0.05)

Before running a test, scientists agree on a threshold of strictness, called Alpha (α). 
The global scientific standard is **α = 0.05**.

- If **p < 0.05**: The result is "Statistically Significant". You reject the Null Hypothesis (the assumption that there is no difference) and declare the Red button the winner.
- If **p >= 0.05**: The result is not statistically significant. You fail to reject the Null Hypothesis. The test is inconclusive.

### The Danger of P-Hacking

P-values are notoriously misunderstood and abused.
If you run 20 different A/B tests on random things (button color, font size, image alignment) that actually have zero impact, pure probability dictates that at least 1 of them will randomly generate a p-value < 0.05. 

Unethical analysts will hide the 19 failed tests, and present the 1 "Significant" test to the CEO. This is called **P-Hacking**, and it destroys business value.""",

    ("Statistical Analysis & A/B Testing", "A/B Testing Basics"): """## Scientific Method for Business

An **A/B Test** (or Split Test) is a randomized controlled experiment used to determine if a change to a product actually improves a business metric. 

If Amazon wants to redesign their checkout page, they don't just launch it and see if revenue goes up next month (because Christmas might naturally cause revenue to go up, skewing the result). They run an A/B test.

### The Core Architecture

1. **The Hypothesis**: "Changing the Checkout button from 'Buy' to 'Secure Checkout' will increase the conversion rate."
2. **Randomization**: As users arrive at the website, an algorithm flips a digital coin. 
   - 50% are assigned to Group A (The Control - they see the old 'Buy' button).
   - 50% are assigned to Group B (The Variant - they see the new 'Secure Checkout' button).
3. **The Metric**: You strictly define the success metric beforehand (e.g., Conversion Rate).

### Crucial Best Practices

**1. Test ONLY one thing at a time**
If Group B gets a new button color AND a new headline, and conversions increase by 10%, which change caused it? You will never know. A/B testing isolates variables.

**2. Ensure Random Assignment**
If you test the old button on Mondays, and the new button on Tuesdays, your test is invalid. Tuesday shoppers might naturally spend more money than Monday shoppers. Randomization ensures that demographic differences (Age, Income, Device Type) are perfectly balanced between both groups.

**3. Determine Sample Size First**
You cannot run a test, check the p-value every day, and stop the test the second the p-value dips below 0.05. This is a massive statistical error called "Peeking" and leads to False Positives. 
You must use a statistical calculator beforehand to determine: *"I need exactly 10,000 users in each group to detect a 5% change."* You run the test until you hit 10,000, and only then do you look at the results.""",

    ("Statistical Analysis & A/B Testing", "Evaluating an A/B Test"): """## Making the Final Decision

The A/B test has finished running. You have gathered the data. Now, you must act as the Data Analyst and make a recommendation to the Product team.

### Step 1: Calculate Statistical Significance

You use Python (the `scipy.stats` library) to run a statistical test (usually a Two-Proportion Z-Test for conversion rates, or a T-Test for revenue).

```python
from statsmodels.stats.proportion import proportions_ztest

# Successes (Conversions) and Trials (Total Users)
successes = [500, 560]      # Group A: 500, Group B: 560
trials = [10000, 10000]     # 10k users in each group

# Run the Z-Test
stat, p_value = proportions_ztest(successes, trials)

print(f"P-Value: {p_value}") # P-Value: 0.041
```
Because the p-value (0.041) is less than 0.05, the result is **Statistically Significant**. Group B's higher conversion rate is real.

### Step 2: Practical Significance

Just because a result is mathematically real does NOT mean you should implement it. 
Imagine you run a test on 10 million users. Group B increases revenue by 0.001%, and the p-value is 0.01 (Highly Significant). 

But rewriting the entire website codebase to implement Group B will cost $50,000 in engineering time. The tiny 0.001% revenue increase will only generate $500 a year. 
This result is Statistically Significant, but lacks **Practical Significance**. Do not ship it.

### Step 3: Guardrail Metrics

Before launching Group B, you must check your "Guardrail" (Do No Harm) metrics.
Perhaps Group B increased Checkout Conversion by 5% (Great!). But what if it also increased the Customer Support ticket volume by 200% because the new design was confusing? 

A good analyst looks at the holistic impact of the test on the entire company before recommending a launch."""
}

patched = 0
for category_name, category_data in data.items():
    for lesson in category_data.get("lessons", []):
        title = lesson["title"]
        key = (category_name, title)
        if key in theories and theories[key] is not None:
            old_len = len(lesson.get("theory", ""))
            lesson["theory"] = theories[key]
            new_len = len(lesson["theory"])
            print(f"  OK [{category_name}] {title}: {old_len} -> {new_len} chars")
            patched += 1

with open("curriculum/tracks/data_analysis.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nPatched {patched} lessons in data_analysis.json")
