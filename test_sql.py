from sqlalchemy import text
from sqlalchemy.dialects import postgresql
stmt = text("ALTER TABLE users ADD COLUMN IF NOT EXISTS progress JSON DEFAULT '{{}}'::json")
print(str(stmt.compile(dialect=postgresql.dialect())))
