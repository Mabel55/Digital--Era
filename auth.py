import bcrypt
from datetime import datetime, timedelta
from jose import jwt

# 🔑 Setup JWT Token Secrets
SECRET_KEY = "super_secret_noun_academy_key_change_this_later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 

def hash_password(password: str) -> str:
    """
    Encodes the string password to raw bytes and hashes it securely.
    Decodes the final hash to a clean string string to store safely in PostgreSQL.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    return hashed_bytes.decode('utf-8') 

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Converts inputs to bytes and securely cross-checks them natively 
    to bypass the unmaintained passlib wrapper bug completely.
    """
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def create_access_token(data: dict):
    """Generates a secure JWT token for user authentication sessions."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt