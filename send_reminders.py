import os
import json
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

def send_mock_email(email: str, name: str, streak: int):
    print("=" * 50)
    print(f"📧 EMAIL SENT TO: {email}")
    print(f"Subject: Don't lose your {streak}-day streak, {name}!")
    print(f"\nHi {name},\n")
    print(f"We noticed you haven't logged in to Digital Era for a few days.")
    print(f"You have a 🔥 {streak}-day streak on the line!")
    print(f"Come back and complete a quick lesson to keep it alive.\n")
    print("Keep building,\nThe Digital Era Team")
    print("=" * 50)

def process_reminders():
    db: Session = SessionLocal()
    try:
        # Get users who haven't logged in for 3 days or more, but less than 4 days
        # (so we don't spam them every single day after)
        now = datetime.utcnow()
        three_days_ago = now - timedelta(days=3)
        four_days_ago = now - timedelta(days=4)
        
        users_to_remind = db.query(User).filter(
            User.last_login != None,
            User.last_login <= three_days_ago,
            User.last_login > four_days_ago,
            User.streak > 0
        ).all()
        
        print(f"Found {len(users_to_remind)} users to send streak reminders to.")
        
        for user in users_to_remind:
            send_mock_email(
                email=user.email,
                name=user.full_name.split(" ")[0] if user.full_name else "Student",
                streak=user.streak
            )
            
    except Exception as e:
        print(f"Error processing reminders: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    process_reminders()
