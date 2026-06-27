"""
Batch 35: Expanding SQL & Databases Curriculum (NoSQL, Window Functions, Transactions, PostgreSQL, Data Warehousing)
"""
import json, os

NEW_COURSES_BATCH35 = {
    "NoSQL Basics": {
        "tier": "Beginner",
        "aiRubric": "Assess NoSQL and MongoDB basics",
        "lessons": [
            {"title": "Document Databases", "theory": "## JSON-like Storage\\nNoSQL databases like MongoDB store data in flexible, JSON-like documents. Fields can vary from document to document, unlike strict SQL tables.", "instructions": "## Task: Insert Document\\nWrite a MongoDB query to insert a user document with name 'Alice' and age 25 into the 'users' collection.", "starterCode": "db.users.___({ name: '___', age: ___ })", "solution": "db.users.insertOne({ name: 'Alice', age: 25 })", "hint": "Use insertOne", "rubric": "Correctly uses insertOne with the provided fields."},
            {"title": "Finding Documents", "theory": "## Querying Collections\\nInstead of SELECT, NoSQL databases use methods like `find()` to retrieve documents that match a specific filter object.", "instructions": "## Task: Find Users\\nFind all users in the 'users' collection where the age is greater than 20. Use the `$gt` operator.", "starterCode": "db.users.___({ age: { ___: 20 } })", "solution": "db.users.find({ age: { $gt: 20 } })", "hint": "Use find and $gt", "rubric": "Correctly uses find and the $gt operator."}
        ]
    },
    "Advanced Joins & Window Functions": {
        "tier": "Intermediate",
        "aiRubric": "Assess advanced SQL queries",
        "lessons": [
            {"title": "FULL OUTER JOIN", "theory": "## Combining Everything\\nA FULL OUTER JOIN returns all records when there is a match in either the left or the right table records. Unmatched rows will contain NULLs.", "instructions": "## Task: Full Outer Join\\nJoin `employees` and `departments` on `dept_id` using a FULL OUTER JOIN.", "starterCode": "SELECT e.name, d.dept_name \\nFROM employees e\\n___ ___ JOIN departments d \\nON e.dept_id = d.dept_id;", "solution": "SELECT e.name, d.dept_name \\nFROM employees e\\nFULL OUTER JOIN departments d \\nON e.dept_id = d.dept_id;", "hint": "Use FULL OUTER JOIN", "rubric": "Correctly applies FULL OUTER JOIN syntax."},
            {"title": "Window Functions", "theory": "## OVER Clause\\nWindow functions perform calculations across a set of table rows related to the current row, but unlike GROUP BY, they do not collapse the rows.", "instructions": "## Task: Row Number\\nUse `ROW_NUMBER()` to assign a unique sequential integer to rows, ordered by salary descending.", "starterCode": "SELECT name, salary,\\n  ___() OVER (ORDER BY salary ___) as rank\\nFROM employees;", "solution": "SELECT name, salary,\\n  ROW_NUMBER() OVER (ORDER BY salary DESC) as rank\\nFROM employees;", "hint": "Use ROW_NUMBER() and DESC", "rubric": "Correctly uses ROW_NUMBER and DESC."}
        ]
    },
    "Transactions & ACID": {
        "tier": "Intermediate",
        "aiRubric": "Assess ACID properties and transactions",
        "lessons": [
            {"title": "BEGIN and COMMIT", "theory": "## Atomic Operations\\nA transaction ensures that a series of database operations either all succeed (COMMIT) or all fail (ROLLBACK).", "instructions": "## Task: Safe Transfer\\nWrap the two UPDATE statements in a transaction using BEGIN and COMMIT.", "starterCode": "___;\\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\\n___;", "solution": "BEGIN;\\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\\nCOMMIT;", "hint": "Use BEGIN and COMMIT", "rubric": "Correctly begins and commits the transaction."},
            {"title": "ROLLBACK", "theory": "## Undoing Mistakes\\nIf something goes wrong during a transaction (or if a condition isn't met), you can issue a ROLLBACK to undo all changes since BEGIN.", "instructions": "## Task: Abort Transaction\\nUndo the transaction changes using the appropriate SQL command.", "starterCode": "BEGIN;\\nDELETE FROM important_table;\\n-- Oh no, wait!\\n___;", "solution": "BEGIN;\\nDELETE FROM important_table;\\n-- Oh no, wait!\\nROLLBACK;", "hint": "Use ROLLBACK", "rubric": "Correctly uses ROLLBACK."}
        ]
    },
    "PostgreSQL Administration": {
        "tier": "Advanced",
        "aiRubric": "Assess Postgres administration",
        "lessons": [
            {"title": "JSONB Columns", "theory": "## Semi-Structured Data\\nPostgreSQL allows you to store and query JSON data efficiently using the JSONB data type, giving you the best of both SQL and NoSQL.", "instructions": "## Task: Query JSONB\\nExtract the 'role' key from the `metadata` JSONB column where the user id is 1.", "starterCode": "SELECT metadata___'role' AS role \\nFROM users \\nWHERE id = 1;", "solution": "SELECT metadata->>'role' AS role \\nFROM users \\nWHERE id = 1;", "hint": "Use the ->> operator", "rubric": "Correctly uses the ->> operator to extract text from JSONB."},
            {"title": "Roles and Permissions", "theory": "## Database Security\\nPostgreSQL uses roles to manage database access privileges. You can GRANT specific permissions to roles.", "instructions": "## Task: Grant Select\\nGrant SELECT permission on the `reports` table to the `analyst` role.", "starterCode": "___ SELECT ON reports TO ___;", "solution": "GRANT SELECT ON reports TO analyst;", "hint": "Use GRANT and analyst", "rubric": "Correctly grants select on the table to the role."}
        ]
    },
    "Data Warehousing": {
        "tier": "Advanced",
        "aiRubric": "Assess Data Warehousing concepts",
        "lessons": [
            {"title": "Star Schema", "theory": "## Fact and Dimension Tables\\nIn data warehousing, a Star Schema consists of a central Fact table (events/transactions) connected to multiple Dimension tables (context like time, user, product).", "instructions": "## Task: Fact Table Join\\nJoin the `sales_fact` table to the `date_dim` dimension table.", "starterCode": "SELECT d.year, SUM(s.amount) \\nFROM sales_fact s\\nJOIN ___ d ON s.date_id = d.___ \\nGROUP BY d.year;", "solution": "SELECT d.year, SUM(s.amount) \\nFROM sales_fact s\\nJOIN date_dim d ON s.date_id = d.id \\nGROUP BY d.year;", "hint": "Join date_dim on id", "rubric": "Correctly joins the dimension table."},
            {"title": "Materialized Views", "theory": "## Caching Complex Queries\\nA materialized view saves the result of a complex query physically to the disk, speeding up read access at the cost of requiring periodic refreshes.", "instructions": "## Task: Create Materialized View\\nCreate a materialized view named `daily_sales` from a SELECT query.", "starterCode": "CREATE ___ ___ daily_sales AS \\nSELECT date, sum(amount) FROM sales GROUP BY date;", "solution": "CREATE MATERIALIZED VIEW daily_sales AS \\nSELECT date, sum(amount) FROM sales GROUP BY date;", "hint": "Use MATERIALIZED VIEW", "rubric": "Correctly uses CREATE MATERIALIZED VIEW."}
        ]
    }
}

def apply_lessons(tracks_dir):
    total = 0
    filepath = os.path.join(tracks_dir, 'sql_databases.json')
    
    # 1. Update sql_databases.json
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            track_data = json.load(f)
            
        updated = False
        
        # Add brand new courses
        for new_course_name, course_info in NEW_COURSES_BATCH35.items():
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
        for new_course_name, course_info in NEW_COURSES_BATCH35.items():
            tier = course_info["tier"]
            if "SQL & Databases" in index_data and tier in index_data["SQL & Databases"]:
                if new_course_name not in index_data["SQL & Databases"][tier]:
                    index_data["SQL & Databases"][tier].append(new_course_name)
                    index_updated = True
                    
        if index_updated:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                
    print(f'Batch 35: Added {total} lessons to SQL & Databases track')
    os.system('python build_courses.py')

if __name__ == '__main__':
    apply_lessons(os.path.join('curriculum', 'tracks'))
