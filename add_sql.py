"""
Phase 5: Add 39 new unique lessons to SQL track.
"""
import json

TRACK_FILE = "curriculum/tracks/sql_databases.json"

NEW_LESSONS = {
    "SQL Fundamentals": [
        {
            "title": "Data Definition Language (DDL)",
            "theory": "## DDL Commands\nDDL (Data Definition Language) is used to define database structures. Commands include `CREATE`, `ALTER`, and `DROP`.",
            "instructions": "## Task: Create a Table\n1. Write a SQL command to `CREATE TABLE` named `employees`.\n2. Add an `id` integer column that is the `PRIMARY KEY`.\n3. Add a `name` varchar(50) column.",
            "starterCode": "___ ___ employees (\n    id ___ ___ ___,\n    name ___(50)\n);",
            "solution": "CREATE TABLE employees (\n    id INT PRIMARY KEY,\n    name VARCHAR(50)\n);",
            "hint": "Use CREATE TABLE, INT PRIMARY KEY, and VARCHAR.",
            "rubric": "DDL statement correctly creates the requested table."
        },
        {
            "title": "Data Manipulation Language (DML)",
            "theory": "## DML Commands\nDML (Data Manipulation Language) is used for managing data within schema objects. Commands include `INSERT`, `UPDATE`, and `DELETE`.",
            "instructions": "## Task: Insert Data\n1. Write a SQL command to `INSERT INTO` the `employees` table.\n2. Provide values for `id` (1) and `name` ('Alice').",
            "starterCode": "___ ___ employees (id, name)\n___ (1, 'Alice');",
            "solution": "INSERT INTO employees (id, name)\nVALUES (1, 'Alice');",
            "hint": "Use INSERT INTO and VALUES keywords.",
            "rubric": "DML statement correctly inserts the requested data."
        },
        {
            "title": "Selecting Data",
            "theory": "## SELECT Statement\nThe `SELECT` statement is used to select data from a database. Use `*` to select all columns.",
            "instructions": "## Task: Select All Columns\n1. Write a SQL query to select all columns from the `employees` table.",
            "starterCode": "___ * ___ employees;",
            "solution": "SELECT * FROM employees;",
            "hint": "Use SELECT and FROM.",
            "rubric": "SQL query correctly selects all data from the table."
        }
    ],
    "Filtering & Sorting": [
        {
            "title": "The WHERE Clause",
            "theory": "## Filtering\nThe `WHERE` clause is used to extract only those records that fulfill a specified condition.",
            "instructions": "## Task: Filter Employees\n1. Select all columns from `employees`.\n2. Only include employees where `department_id` is 5.",
            "starterCode": "SELECT * FROM employees\n___ department_id = ___;",
            "solution": "SELECT * FROM employees\nWHERE department_id = 5;",
            "hint": "Use the WHERE clause.",
            "rubric": "Query successfully filters data based on condition."
        },
        {
            "title": "Sorting Results",
            "theory": "## ORDER BY\nThe `ORDER BY` keyword is used to sort the result-set in ascending or descending order.",
            "instructions": "## Task: Sort by Salary\n1. Select all columns from `employees`.\n2. Sort the results by `salary` in descending order.",
            "starterCode": "SELECT * FROM employees\n___ ___ salary ___;",
            "solution": "SELECT * FROM employees\nORDER BY salary DESC;",
            "hint": "Use ORDER BY column DESC.",
            "rubric": "Data is correctly sorted in descending order."
        },
        {
            "title": "Pattern Matching with LIKE",
            "theory": "## LIKE Operator\nThe `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column using `%` and `_` wildcards.",
            "instructions": "## Task: Find Names\n1. Select all from `employees`.\n2. Filter where `name` starts with 'A'.",
            "starterCode": "SELECT * FROM employees\nWHERE name ___ '___%';",
            "solution": "SELECT * FROM employees\nWHERE name LIKE 'A%';",
            "hint": "Use LIKE 'A%'.",
            "rubric": "Query utilizes LIKE with wildcard to filter string patterns."
        }
    ],
    "Joins & Relationships": [
        {
            "title": "Inner Joins",
            "theory": "## INNER JOIN\nThe `INNER JOIN` keyword selects records that have matching values in both tables.",
            "instructions": "## Task: Join Employees and Departments\n1. Select employee `name` and department `name`.\n2. Join `employees` (e) and `departments` (d) on `department_id`.",
            "starterCode": "SELECT e.name, d.name\nFROM employees e\n___ ___ departments d\n___ e.department_id = d.id;",
            "solution": "SELECT e.name, d.name\nFROM employees e\nINNER JOIN departments d\nON e.department_id = d.id;",
            "hint": "Use INNER JOIN and ON.",
            "rubric": "Inner join properly links the two tables."
        },
        {
            "title": "Left Joins",
            "theory": "## LEFT JOIN\nThe `LEFT JOIN` keyword returns all records from the left table, and the matched records from the right table.",
            "instructions": "## Task: All Employees and Their Departments\n1. Write a `LEFT JOIN` to get all employees, even if they have no department.",
            "starterCode": "SELECT e.name, d.name\nFROM employees e\n___ ___ departments d\nON e.department_id = d.id;",
            "solution": "SELECT e.name, d.name\nFROM employees e\nLEFT JOIN departments d\nON e.department_id = d.id;",
            "hint": "Use LEFT JOIN.",
            "rubric": "Left join correctly implemented to preserve left table records."
        },
        {
            "title": "Cross Joins",
            "theory": "## CROSS JOIN\nThe `CROSS JOIN` keyword returns the Cartesian product of the sets of records from the two joined tables.",
            "instructions": "## Task: Create a Matrix\n1. Use a `CROSS JOIN` to combine all `colors` with all `sizes`.",
            "starterCode": "SELECT c.color, s.size\nFROM colors c\n___ ___ sizes s;",
            "solution": "SELECT c.color, s.size\nFROM colors c\nCROSS JOIN sizes s;",
            "hint": "Use CROSS JOIN.",
            "rubric": "Cross join successfully creates a Cartesian product."
        }
    ],
    "Aggregations & Grouping": [
        {
            "title": "Basic Aggregations",
            "theory": "## Aggregate Functions\nFunctions like `COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()` perform a calculation on a set of values and return a single value.",
            "instructions": "## Task: Calculate Total Salary\n1. Select the sum of all salaries from the `employees` table.",
            "starterCode": "SELECT ___(___) FROM employees;",
            "solution": "SELECT SUM(salary) FROM employees;",
            "hint": "Use the SUM() function.",
            "rubric": "Correct aggregate function applied."
        },
        {
            "title": "Grouping Data",
            "theory": "## GROUP BY\nThe `GROUP BY` statement groups rows that have the same values into summary rows.",
            "instructions": "## Task: Count Employees by Department\n1. Select `department_id` and the count of employees.\n2. Group the results by `department_id`.",
            "starterCode": "SELECT department_id, ___(id)\nFROM employees\n___ ___ department_id;",
            "solution": "SELECT department_id, COUNT(id)\nFROM employees\nGROUP BY department_id;",
            "hint": "Use COUNT() and GROUP BY.",
            "rubric": "Data successfully aggregated using GROUP BY."
        },
        {
            "title": "Filtering Grouped Data",
            "theory": "## HAVING Clause\nThe `HAVING` clause was added to SQL because the `WHERE` keyword cannot be used with aggregate functions.",
            "instructions": "## Task: Departments with Many Employees\n1. Select `department_id` and count of employees.\n2. Group by `department_id`.\n3. Filter to only show departments with more than 5 employees.",
            "starterCode": "SELECT department_id, COUNT(id)\nFROM employees\nGROUP BY department_id\n___ COUNT(id) > 5;",
            "solution": "SELECT department_id, COUNT(id)\nFROM employees\nGROUP BY department_id\nHAVING COUNT(id) > 5;",
            "hint": "Use HAVING after GROUP BY.",
            "rubric": "HAVING clause correctly filters aggregated data."
        }
    ],
    "Subqueries": [
        {
            "title": "Scalar Subqueries",
            "theory": "## Scalar Subquery\nA subquery that returns exactly one row and one column. It can be used anywhere a single value is expected.",
            "instructions": "## Task: Compare to Average\n1. Select employees whose salary is greater than the average salary of all employees.",
            "starterCode": "SELECT name, salary \nFROM employees \nWHERE salary > (\n    SELECT ___(salary) FROM ___\n);",
            "solution": "SELECT name, salary \nFROM employees \nWHERE salary > (\n    SELECT AVG(salary) FROM employees\n);",
            "hint": "Subquery should SELECT AVG(salary) FROM employees.",
            "rubric": "Scalar subquery successfully implemented in the WHERE clause."
        },
        {
            "title": "IN with Subqueries",
            "theory": "## IN Clause\nA subquery can return a column of values. The `IN` operator checks if a value matches any value in that list.",
            "instructions": "## Task: Find Managers\n1. Select names of employees whose `id` is present in the `manager_id` column of the `departments` table.",
            "starterCode": "SELECT name \nFROM employees \nWHERE id ___ (\n    SELECT manager_id FROM departments\n);",
            "solution": "SELECT name \nFROM employees \nWHERE id IN (\n    SELECT manager_id FROM departments\n);",
            "hint": "Use the IN operator.",
            "rubric": "Subquery with IN operator used correctly."
        },
        {
            "title": "Correlated Subqueries",
            "theory": "## Correlated Subqueries\nA correlated subquery uses values from the outer query, meaning it must be evaluated once for each row processed by the outer query.",
            "instructions": "## Task: Highest Paid per Department\n1. Select employee names who have the highest salary within their specific department.",
            "starterCode": "SELECT e1.name\nFROM employees e1\nWHERE e1.salary = (\n    SELECT MAX(e2.salary)\n    FROM employees e2\n    WHERE e1.___ = e2.___\n);",
            "solution": "SELECT e1.name\nFROM employees e1\nWHERE e1.salary = (\n    SELECT MAX(e2.salary)\n    FROM employees e2\n    WHERE e1.department_id = e2.department_id\n);",
            "hint": "Link e1.department_id to e2.department_id.",
            "rubric": "Correlated subquery correctly joins inner and outer tables."
        }
    ],
    "Indexes & Performance": [
        {
            "title": "Creating Indexes",
            "theory": "## Indexes\nIndexes are used to retrieve data from the database more quickly. They are created on columns that are frequently searched.",
            "instructions": "## Task: Index an Email Column\n1. Create an index named `idx_email` on the `email` column of the `users` table.",
            "starterCode": "___ ___ idx_email \n___ users (___);",
            "solution": "CREATE INDEX idx_email \nON users (email);",
            "hint": "Use CREATE INDEX ... ON table_name (column_name).",
            "rubric": "Index creation statement is properly formed."
        },
        {
            "title": "Unique Indexes",
            "theory": "## Unique Indexes\nA unique index ensures that the indexed columns do not contain duplicate values.",
            "instructions": "## Task: Unique Username Index\n1. Create a unique index named `idx_username` on the `username` column of the `accounts` table.",
            "starterCode": "CREATE ___ INDEX idx_username \nON accounts (___);",
            "solution": "CREATE UNIQUE INDEX idx_username \nON accounts (username);",
            "hint": "Use CREATE UNIQUE INDEX.",
            "rubric": "Unique index creation statement is correctly written."
        },
        {
            "title": "EXPLAIN Command",
            "theory": "## Query Execution Plans\nThe `EXPLAIN` keyword in PostgreSQL/MySQL shows the execution plan of a statement, indicating if indexes are being used.",
            "instructions": "## Task: Explain a Query\n1. Prepend the `EXPLAIN` keyword to a query fetching a user by email to see its plan.",
            "starterCode": "___ \nSELECT * FROM users WHERE email = 'test@example.com';",
            "solution": "EXPLAIN \nSELECT * FROM users WHERE email = 'test@example.com';",
            "hint": "Just use EXPLAIN.",
            "rubric": "EXPLAIN command utilized correctly."
        }
    ],
    "Stored Procedures": [
        {
            "title": "Basic Stored Procedure",
            "theory": "## Stored Procedures\nA stored procedure is a prepared SQL code that you can save, so the code can be reused.",
            "instructions": "## Task: Create a Procedure (PostgreSQL)\n1. Create a procedure `add_user` that takes a `p_name` VARCHAR.\n2. Inside, insert the name into the `users` table.",
            "starterCode": "CREATE OR REPLACE ___ add_user(p_name VARCHAR)\nLANGUAGE plpgsql\nAS $$\nBEGIN\n    INSERT INTO users (name) VALUES (___);\nEND;\n$$;",
            "solution": "CREATE OR REPLACE PROCEDURE add_user(p_name VARCHAR)\nLANGUAGE plpgsql\nAS $$\nBEGIN\n    INSERT INTO users (name) VALUES (p_name);\nEND;\n$$;",
            "hint": "Use PROCEDURE and the variable p_name.",
            "rubric": "Stored procedure definition is syntactically valid."
        },
        {
            "title": "Calling a Procedure",
            "theory": "## Calling Procedures\nOnce created, you must invoke the procedure using the `CALL` statement (or `EXEC` in SQL Server).",
            "instructions": "## Task: Invoke Procedure\n1. Call the `add_user` procedure passing the string 'Bob'.",
            "starterCode": "___ add_user('___');",
            "solution": "CALL add_user('Bob');",
            "hint": "Use CALL procedure_name().",
            "rubric": "Procedure invocation statement is correct."
        },
        {
            "title": "Functions vs Procedures",
            "theory": "## Functions\nUnlike procedures, SQL functions must return a value and can be used directly in `SELECT` statements.",
            "instructions": "## Task: Create a Function\n1. Create a function `get_count` returning an `INTEGER`.\n2. Return the count of rows in the `users` table.",
            "starterCode": "CREATE OR REPLACE ___ get_count() \nRETURNS ___\nLANGUAGE plpgsql\nAS $$\nDECLARE \n    c INT;\nBEGIN\n    SELECT COUNT(*) INTO c FROM users;\n    ___ c;\nEND;\n$$;",
            "solution": "CREATE OR REPLACE FUNCTION get_count() \nRETURNS INTEGER\nLANGUAGE plpgsql\nAS $$\nDECLARE \n    c INT;\nBEGIN\n    SELECT COUNT(*) INTO c FROM users;\n    RETURN c;\nEND;\n$$;",
            "hint": "Use FUNCTION, RETURNS INTEGER, and RETURN c.",
            "rubric": "Function definition successfully returns a value."
        }
    ],
    "Transactions & ACID": [
        {
            "title": "Beginning and Committing",
            "theory": "## Transactions\nTransactions bundle multiple steps into a single, all-or-nothing operation. Use `BEGIN` to start and `COMMIT` to save.",
            "instructions": "## Task: Safe Transfer\n1. Start a transaction.\n2. Deduct $100 from account 1.\n3. Add $100 to account 2.\n4. Commit.",
            "starterCode": "___;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\n___;",
            "solution": "BEGIN;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;",
            "hint": "Use BEGIN and COMMIT.",
            "rubric": "Transaction block is correctly opened and closed."
        },
        {
            "title": "Rolling Back",
            "theory": "## Rollback\nIf an error occurs during a transaction, `ROLLBACK` undoes all changes made since `BEGIN`.",
            "instructions": "## Task: Undo Changes\n1. Start a transaction, do an update, and then undo it using `ROLLBACK`.",
            "starterCode": "BEGIN;\nUPDATE users SET status = 'active';\n___; -- Wait, mistake!",
            "solution": "BEGIN;\nUPDATE users SET status = 'active';\nROLLBACK; -- Wait, mistake!",
            "hint": "Use ROLLBACK.",
            "rubric": "Rollback command correctly utilized."
        },
        {
            "title": "Isolation Levels",
            "theory": "## Isolation\nIsolation levels control how transaction changes are visible to other concurrent transactions (e.g., Read Committed, Serializable).",
            "instructions": "## Task: Set Isolation Level\n1. Start a transaction.\n2. Set the transaction isolation level to `SERIALIZABLE`.",
            "starterCode": "BEGIN;\nSET TRANSACTION ISOLATION LEVEL ___;\nCOMMIT;",
            "solution": "BEGIN;\nSET TRANSACTION ISOLATION LEVEL SERIALIZABLE;\nCOMMIT;",
            "hint": "Use SERIALIZABLE.",
            "rubric": "Transaction isolation level successfully set."
        }
    ],
    "Views & CTEs": [
        {
            "title": "Creating Views",
            "theory": "## Views\nA view is a virtual table based on the result-set of an SQL statement. It simplifies complex queries.",
            "instructions": "## Task: Active Users View\n1. Create a view named `active_users`.\n2. The view should select all users where `status` is 'active'.",
            "starterCode": "___ ___ active_users ___ \nSELECT * FROM users WHERE status = 'active';",
            "solution": "CREATE VIEW active_users AS \nSELECT * FROM users WHERE status = 'active';",
            "hint": "Use CREATE VIEW view_name AS.",
            "rubric": "View creation syntax correctly formulated."
        },
        {
            "title": "Common Table Expressions",
            "theory": "## CTEs\nThe `WITH` clause (CTE) defines a temporary result set that you can reference within another query.",
            "instructions": "## Task: Basic CTE\n1. Create a CTE named `TopSpenders` selecting user_ids spending > 100.\n2. Select all from `TopSpenders`.",
            "starterCode": "___ TopSpenders AS (\n    SELECT user_id FROM orders GROUP BY user_id HAVING SUM(amount) > 100\n)\nSELECT * FROM ___;",
            "solution": "WITH TopSpenders AS (\n    SELECT user_id FROM orders GROUP BY user_id HAVING SUM(amount) > 100\n)\nSELECT * FROM TopSpenders;",
            "hint": "Use WITH TopSpenders AS (...) and SELECT * FROM TopSpenders.",
            "rubric": "CTE correctly defined using WITH and referenced in main query."
        },
        {
            "title": "Recursive CTEs",
            "theory": "## Recursion\nRecursive CTEs reference themselves, useful for hierarchical data like organizational charts.",
            "instructions": "## Task: Number Generator\n1. Create a recursive CTE to generate numbers 1 to 5.",
            "starterCode": "WITH ___ numbers AS (\n    SELECT 1 AS n\n    UNION ALL\n    SELECT n + 1 FROM numbers WHERE n < ___\n)\nSELECT * FROM numbers;",
            "solution": "WITH RECURSIVE numbers AS (\n    SELECT 1 AS n\n    UNION ALL\n    SELECT n + 1 FROM numbers WHERE n < 5\n)\nSELECT * FROM numbers;",
            "hint": "Use RECURSIVE and end condition n < 5.",
            "rubric": "Recursive CTE syntax implemented properly."
        }
    ],
    "PostgreSQL Deep Dive": [
        {
            "title": "JSONB Data Type",
            "theory": "## JSON in Postgres\nPostgreSQL's `JSONB` type stores JSON data in a decomposed binary format, allowing indexing and fast querying.",
            "instructions": "## Task: Query JSONB\n1. Select rows from `logs` where the `details` JSONB column contains a key `status` with value `\"error\"`.",
            "starterCode": "SELECT * FROM logs \nWHERE details ___ '{\"status\": \"error\"}';",
            "solution": "SELECT * FROM logs \nWHERE details @> '{\"status\": \"error\"}';",
            "hint": "Use the @> containment operator.",
            "rubric": "JSONB containment operator applied correctly."
        },
        {
            "title": "Window Functions",
            "theory": "## OVER Clause\nWindow functions perform calculations across a set of table rows related to the current row, without grouping them into a single row.",
            "instructions": "## Task: Running Total\n1. Select the `amount` and a running total of the amount ordered by `id` using `SUM() OVER()`.",
            "starterCode": "SELECT amount, \n       SUM(amount) ___(ORDER BY id) as running_total\nFROM sales;",
            "solution": "SELECT amount, \n       SUM(amount) OVER(ORDER BY id) as running_total\nFROM sales;",
            "hint": "Use OVER(ORDER BY id).",
            "rubric": "Window function OVER clause used correctly for running totals."
        }
    ],
    "Query Optimization": [
        {
            "title": "Avoiding SELECT *",
            "theory": "## Column Selection\nUsing `SELECT *` fetches unnecessary data, increasing I/O and network overhead. Always specify columns.",
            "instructions": "## Task: Optimize Selection\n1. Rewrite the query to only fetch the `id` and `email` columns instead of `*`.",
            "starterCode": "-- Before: SELECT * FROM users;\nSELECT ___, ___ FROM users;",
            "solution": "-- Before: SELECT * FROM users;\nSELECT id, email FROM users;",
            "hint": "Replace * with id, email.",
            "rubric": "Query optimized to fetch specific columns."
        },
        {
            "title": "Using LIMIT",
            "theory": "## Limiting Results\nWhen you only need a subset of results, use `LIMIT` to prevent the database from processing the entire dataset.",
            "instructions": "## Task: Top 3 Earners\n1. Select the `name` and `salary` from `employees`.\n2. Order by salary descending.\n3. Limit to 3 rows.",
            "starterCode": "SELECT name, salary FROM employees\nORDER BY salary DESC\n___ 3;",
            "solution": "SELECT name, salary FROM employees\nORDER BY salary DESC\nLIMIT 3;",
            "hint": "Use LIMIT.",
            "rubric": "LIMIT clause correctly applied to restrict result set."
        }
    ],
    "Database Design Patterns": [
        {
            "title": "Normalization",
            "theory": "## Normal Forms\nNormalization eliminates redundant data and ensures data dependencies make sense (e.g., 1NF, 2NF, 3NF).",
            "instructions": "## Task: Create a Lookup Table\n1. To normalize a table containing repeated department names, create a `departments` table with an `id` and `name`.",
            "starterCode": "CREATE TABLE departments (\n    id SERIAL ___ ___,\n    name VARCHAR(50) UNIQUE\n);",
            "solution": "CREATE TABLE departments (\n    id SERIAL PRIMARY KEY,\n    name VARCHAR(50) UNIQUE\n);",
            "hint": "Use PRIMARY KEY.",
            "rubric": "Lookup table created correctly establishing a primary key."
        },
        {
            "title": "Foreign Keys",
            "theory": "## Referential Integrity\nForeign keys link tables together and enforce referential integrity, ensuring relationships remain valid.",
            "instructions": "## Task: Add Foreign Key\n1. In the `employees` table, define `department_id` as a foreign key referencing `departments(id)`.",
            "starterCode": "CREATE TABLE employees (\n    id INT PRIMARY KEY,\n    department_id INT,\n    ___ KEY (department_id) ___ departments(id)\n);",
            "solution": "CREATE TABLE employees (\n    id INT PRIMARY KEY,\n    department_id INT,\n    FOREIGN KEY (department_id) REFERENCES departments(id)\n);",
            "hint": "Use FOREIGN KEY and REFERENCES.",
            "rubric": "Foreign key constraint correctly formulated."
        }
    ],
    "NoSQL with MongoDB": [
        {
            "title": "Document Structure",
            "theory": "## BSON Documents\nMongoDB stores data in flexible, JSON-like documents called BSON, where fields can vary from document to document.",
            "instructions": "## Task: Insert Document\n1. Write a MongoDB shell command to insert a document with `name: \"Alice\"` into the `users` collection.",
            "starterCode": "db.users.___({ name: \"Alice\" });",
            "solution": "db.users.insertOne({ name: \"Alice\" });",
            "hint": "Use insertOne or insert.",
            "rubric": "MongoDB insertion command accurately written."
        },
        {
            "title": "Querying Documents",
            "theory": "## find()\nUse `db.collection.find(query)` to retrieve documents matching criteria.",
            "instructions": "## Task: Find by Age\n1. Query the `users` collection for documents where `age` is exactly 30.",
            "starterCode": "db.users.___({ ___: 30 });",
            "solution": "db.users.find({ age: 30 });",
            "hint": "Use find().",
            "rubric": "MongoDB find command correctly queries by property."
        }
    ],
    "ORMs with SQLAlchemy": [
        {
            "title": "Defining Models",
            "theory": "## SQLAlchemy Classes\nModels inherit from a declarative base to map Python attributes to database columns.",
            "instructions": "## Task: Create User Model\n1. Define `User` inheriting from `Base`.\n2. Set `__tablename__` to 'users'.\n3. Add `id` as an Integer primary key.",
            "starterCode": "class User(___):\n    __tablename__ = '___'\n    id = Column(Integer, ___=True)",
            "solution": "class User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)",
            "hint": "Inherit from Base, tablename is 'users', primary_key=True.",
            "rubric": "SQLAlchemy model defined correctly with primary key."
        },
        {
            "title": "Adding Data via ORM",
            "theory": "## Sessions\nChanges are staged in a Session and pushed to the DB using `session.commit()`.",
            "instructions": "## Task: Add a User\n1. Create a `User` instance.\n2. Add it to the session.\n3. Commit the session.",
            "starterCode": "new_user = User(name='Bob')\nsession.___(new_user)\nsession.___()",
            "solution": "new_user = User(name='Bob')\nsession.add(new_user)\nsession.commit()",
            "hint": "Use session.add() and session.commit().",
            "rubric": "ORM insertion and commit cycle works."
        }
    ],
    "Sharding & Replication": [
        {
            "title": "Read Replicas",
            "theory": "## High Availability\nRead replicas are copies of the primary database used to handle read-only queries, reducing load on the primary.",
            "instructions": "## Task: Route Query\n1. In a hypothetical load balancer logic, route a `SELECT` query to a replica and an `UPDATE` to the primary.",
            "starterCode": "function routeQuery(query) {\n    if (query.startsWith(\"___\")) return \"replica\";\n    return \"___\";\n}",
            "solution": "function routeQuery(query) {\n    if (query.startsWith(\"SELECT\")) return \"replica\";\n    return \"primary\";\n}",
            "hint": "SELECT goes to replica, others to primary.",
            "rubric": "Routing logic correctly differentiates read and write traffic."
        },
        {
            "title": "Sharding Keys",
            "theory": "## Horizontal Partitioning\nSharding distributes data across multiple databases using a shard key.",
            "instructions": "## Task: Choose Shard\n1. Given a user ID, implement a simple modulo sharding strategy across 3 shards.",
            "starterCode": "function getShard(userId) {\n    return userId % ___;\n}",
            "solution": "function getShard(userId) {\n    return userId % 3;\n}",
            "hint": "Modulo by 3.",
            "rubric": "Basic modulo sharding algorithm correctly applied."
        }
    ]
}

def add_new_lessons():
    with open(TRACK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    added = 0
    for course_name, new_lessons in NEW_LESSONS.items():
        if course_name in data:
            data[course_name]["lessons"].extend(new_lessons)
            added += len(new_lessons)
            print(f"[OK] {course_name}: +{len(new_lessons)} lessons")
        else:
            print(f"[WARN] Course not found: {course_name}")
    
    with open(TRACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\nDone! Added {added} new lessons to sql_databases.json")

if __name__ == "__main__":
    add_new_lessons()
