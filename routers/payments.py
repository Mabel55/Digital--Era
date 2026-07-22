"""
Payments Router — Paystack Integration for Digital Era Subscriptions
Handles: Checkout creation, webhook processing, subscription status
"""
import os
import hmac
import hashlib
import httpx
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

# ─── Paystack Configuration ───
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")
PAYSTACK_PLAN_MONTHLY = os.getenv("PAYSTACK_PLAN_MONTHLY", "")
PAYSTACK_PLAN_YEARLY = os.getenv("PAYSTACK_PLAN_YEARLY", "")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

router = APIRouter(prefix="/payments", tags=["Payments & Subscriptions"])


# ─── Helper: Get or Create Subscription Record ───
def get_or_create_subscription(db: Session, user: models.User) -> models.Subscription:
    """Ensure every user has a subscription record (defaults to free)."""
    sub = db.query(models.Subscription).filter(
        models.Subscription.user_id == user.id
    ).first()
    if not sub:
        sub = models.Subscription(user_id=user.id, plan="free", status="active")
        db.add(sub)
        db.commit()
        db.refresh(sub)
    return sub


# ─── Helper: Check if User is Pro ───
def require_pro(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """FastAPI dependency that raises 403 if user is not a Pro subscriber."""
    sub = get_or_create_subscription(db, current_user)
    if not sub.is_pro:
        raise HTTPException(
            status_code=403,
            detail="This feature requires a Pro subscription. Upgrade at /pricing"
        )
    return current_user


# ─── 1. Get Subscription Status ───
@router.get("/subscription", response_model=schemas.SubscriptionResponse)
def get_subscription_status(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Returns the current user's subscription plan and status."""
    sub = get_or_create_subscription(db, current_user)
    return schemas.SubscriptionResponse(
        plan=sub.plan,
        status=sub.status,
        is_pro=sub.is_pro,
        current_period_end=sub.current_period_end
    )


# ─── 2. Create Paystack Checkout Session ───
@router.post("/create-checkout")
async def create_checkout_session(
    plan: str = "pro_monthly",
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Initializes a Paystack transaction for the user to subscribe."""
    if not PAYSTACK_SECRET_KEY or PAYSTACK_SECRET_KEY == "sk_test_REPLACE_ME":
        raise HTTPException(
            status_code=503,
            detail="Payment system is not configured yet. Please contact support."
        )

    if plan == "pro_yearly":
        plan_code = PAYSTACK_PLAN_YEARLY
        amount = 999900 # $99.99 in kobo/cents equivalent
    else:
        plan_code = PAYSTACK_PLAN_MONTHLY
        amount = 99900 # $9.99 in kobo/cents equivalent

    if not plan_code or plan_code == "PLN_REPLACE_ME":
        raise HTTPException(status_code=503, detail="Pricing not configured. Contact support.")

    sub = get_or_create_subscription(db, current_user)

    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "email": current_user.email,
        "amount": amount,
        "plan": plan_code,
        "callback_url": f"{FRONTEND_URL}/dashboard?payment=success",
        "metadata": {
            "user_id": str(current_user.id),
            "plan": plan
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.paystack.co/transaction/initialize",
            headers=headers,
            json=payload
        )

        data = response.json()
        if not data.get("status"):
            raise HTTPException(status_code=400, detail=f"Paystack Error: {data.get('message')}")
        
        return {
            "checkout_url": data["data"]["authorization_url"],
            "reference": data["data"]["reference"]
        }


# ─── 3. Paystack Webhook Handler ───
@router.post("/webhook")
async def paystack_webhook(request: Request, db: Session = Depends(get_db)):
    """Handles Paystack webhook events for subscription lifecycle management."""
    payload = await request.body()
    sig_header = request.headers.get("x-paystack-signature", "")

    # Verify signature
    hash = hmac.new(
        PAYSTACK_SECRET_KEY.encode('utf-8'),
        payload,
        hashlib.sha512
    ).hexdigest()

    if hash != sig_header:
        # Check if we're in dev mode bypassing verification
        if PAYSTACK_SECRET_KEY != "sk_test_REPLACE_ME":
            raise HTTPException(status_code=400, detail="Invalid signature")

    import json
    event = json.loads(payload)
    event_type = event.get("event")
    data = event.get("data", {})

    if event_type == "subscription.create":
        customer = data.get("customer", {})
        customer_code = customer.get("customer_code")
        email = customer.get("email")
        
        user = db.query(models.User).filter(models.User.email == email).first()
        if user:
            sub = get_or_create_subscription(db, user)
            sub.paystack_customer_code = customer_code
            sub.paystack_subscription_code = data.get("subscription_code")
            sub.plan = "pro_monthly" if "monthly" in str(data.get("plan", {}).get("name", "")).lower() else "pro_yearly"
            sub.status = "active"
            
            # Add 1 month/year roughly for current_period_end
            import datetime as dt
            if "monthly" in sub.plan:
                sub.current_period_end = dt.datetime.utcnow() + dt.timedelta(days=30)
            else:
                sub.current_period_end = dt.datetime.utcnow() + dt.timedelta(days=365)
                
            db.commit()

    elif event_type == "charge.success":
        # Fallback if subscription.create doesn't trigger immediately, handle initial charge
        metadata = data.get("metadata", {})
        user_id = metadata.get("user_id")
        plan = metadata.get("plan")
        
        if user_id:
            user = db.query(models.User).filter(models.User.id == int(user_id)).first()
            if user:
                sub = get_or_create_subscription(db, user)
                sub.plan = plan or "pro_monthly"
                sub.status = "active"
                db.commit()

    elif event_type in ["subscription.disable", "subscription.not_renew"]:
        # Handle cancellations
        sub_code = data.get("subscription_code")
        if sub_code:
            sub = db.query(models.Subscription).filter(models.Subscription.paystack_subscription_code == sub_code).first()
            if sub:
                sub.status = "canceled"
                db.commit()

    return {"status": "success"}
