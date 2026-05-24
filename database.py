from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This URL uses the exact credentials we just set up in Docker!
# Format: postgresql://user:password@server_address:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@localhost:5432/digital_era_db"

# The engine is what actually connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# The session is what we use to query the database (like adding or searching for a student)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All of our database tables will inherit from this Base class
Base = declarative_base()

# 👉 Paste this at the bottom of database.py
def get_db():
    """Generates an independent database session for each request."""
    db = SessionLocal() # Make sure SessionLocal matches the variable name above it!
    try:
        yield db
    finally:
        db.close()