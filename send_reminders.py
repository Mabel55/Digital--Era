import os
import json
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_streak_email(to_email: str, name: str, streak: int):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    base_url = os.getenv("BASE_URL", "https://digital-era.live")

    if not all([smtp_server, smtp_username, smtp_password]):
        print(f"DEBUG: Missing SMTP credentials. Would have sent email to: {to_email}")
        return

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = f"Don't lose your {streak}-day streak, {name}!"
    
    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>Keep your streak alive! 🔥</h2>
        <p>Hi {name},</p>
        <p>We noticed you haven't logged in to Digital Era for a few days.</p>
        <p>You have a <strong>{streak}-day streak</strong> on the line!</p>
        <p>Come back and complete a quick lesson to keep it alive.</p>
        <p><a href="{base_url}/dashboard" style="background-color: #00e5a0; color: #0d0f14; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Continue Learning</a></p>
        <br/>
        <p>Keep building,<br/>The Digital Era Team</p>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print(f"Successfully sent streak reminder email to {to_email}")
    except Exception as e:
        print(f"Failed to send streak reminder email to {to_email}: {e}")

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
            send_streak_email(
                to_email=user.email,
                name=user.full_name.split(" ")[0] if user.full_name else "Student",
                streak=user.streak
            )
            
    except Exception as e:
        print(f"Error processing reminders: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    process_reminders()
