from database import SessionLocal
from models import User
from datetime import datetime, timedelta

db = SessionLocal()
# Find any user
user = db.query(User).first()
if user:
    # Backdate to exactly 3.5 days ago and give them a streak
    user.last_login = datetime.utcnow() - timedelta(days=3, hours=12)
    user.streak = 5
    db.commit()
    print(f"Updated user {user.email} to have last_login 3.5 days ago with a streak of 5.")
else:
    print("No users found.")
db.close()
