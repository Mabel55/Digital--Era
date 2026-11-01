"""
Helper script to quickly grant Pro access to any student from the command line.
Usage:
    python grant_student_pro.py <student_email> [duration_months]

Examples:
    python grant_student_pro.py student@example.com          # Lifetime Pro
    python grant_student_pro.py student@example.com 3        # 3 Months Pro
"""

import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from database import SessionLocal
import models


def grant_pro(email: str, duration_months: int = None):
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.email.ilike(email.strip())).first()
        if not user:
            print(f"[ERROR] User with email '{email}' not found in database.")
            return

        sub = db.query(models.Subscription).filter(models.Subscription.user_id == user.id).first()
        if not sub:
            sub = models.Subscription(user_id=user.id)
            db.add(sub)

        expiration = None
        if duration_months:
            expiration = datetime.utcnow() + relativedelta(months=duration_months)
            sub.plan = "pro_monthly"
        else:
            sub.plan = "pro_lifetime"

        sub.status = "active"
        sub.current_period_end = expiration
        db.commit()

        dur_text = f"{duration_months} month(s) (until {expiration.strftime('%Y-%m-%d')})" if duration_months else "Lifetime (Permanent)"
        print(f"[SUCCESS] Granted {dur_text} Pro access to {user.full_name or user.email} (User ID: {user.id})")
    except Exception as e:
        print(f"[ERROR] Failed to grant pro: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python grant_student_pro.py <student_email> [duration_months]")
        print("Example: python grant_student_pro.py student@example.com")
        print("Example: python grant_student_pro.py student@example.com 6")
    else:
        target_email = sys.argv[1]
        target_months = int(sys.argv[2]) if len(sys.argv) > 2 else None
        grant_pro(target_email, target_months)
