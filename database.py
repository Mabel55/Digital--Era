from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This URL uses the exact credentials we just set up in Docker!
# Format: postgresql://user:password@server_address:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://mabel:supersecret@localhost:5432/school_db"

# The engine is what actually connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# The session is what we use to query the database (like adding or searching for a student)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All of our database tables will inherit from this Base class
Base = declarative_base()