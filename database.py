import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Grab the DATABASE_URL from Azure. If it's not there (like on your laptop), default to localhost.
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:password123@localhost:5432/digital_era_db"
)

# Crucial Fix: SQLAlchemy crashes if the Neon URL starts with "postgres://" instead of "postgresql://"
# This quick check automatically fixes it so Azure doesn't crash!
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# The engine is what actually connects to the database. 
# We add pool_pre_ping to stop Azure/Neon from dropping idle connections!
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True, 
    pool_recycle=300,
    # If using sqlite locally, these args are needed, but for postgres they are ignored.
    # However, to be safe across both, we omit connect_args.
)
# The session is what we use to query the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All of our database tables will inherit from this Base class
Base = declarative_base()

def get_db():
    """Generates an independent database session for each request."""
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()