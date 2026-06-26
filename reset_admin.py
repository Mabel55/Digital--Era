import os
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Manually setup DB since we are running standalone
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password123@localhost:5432/digital_era_db")
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# 2. Hash new password
password_bytes = "password123".encode('utf-8')
salt = bcrypt.gensalt()
hashed_pw = bcrypt.hashpw(password_bytes, salt).decode('utf-8')

# 3. Update the user
from models import User
admin_email = "nasaadanna@gmail.com"
user = db.query(User).filter(User.email == admin_email).first()
if user:
    user.hashed_password = hashed_pw
    db.commit()
    print(f"Password reset for {admin_email} to 'password123'")
else:
    print(f"User {admin_email} not found.")
db.close()
