"""
Payments Router — Stripe Integration for Digital Era Subscriptions
Handles: Checkout creation, webhook processing, subscription status, customer portal
"""
import os
import stripe
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Request, Header
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user

# ─── Stripe Configuration ───
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
STRIPE_PRICE_ID_MONTHLY = os.getenv("STRIPE_PRICE_ID_MONTHLY", "")
STRIPE_PRICE_ID_YEARLY = os.getenv("STRIPE_PRICE_ID_YEARLY", "")
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://digital-era.live")

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


# ─── 2. Create Stripe Checkout Session ───
@router.post("/create-checkout")
def create_checkout_session(
    plan: str = "pro_monthly",
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Creates a Stripe Checkout session for the user to subscribe."""
    if not stripe.api_key or stripe.api_key == "sk_test_REPLACE_ME":
        raise HTTPException(
            status_code=503,
            detail="Payment system is not configured yet. Please contact support."
        )

    # Pick the correct price ID
    if plan == "pro_yearly":
        price_id = STRIPE_PRICE_ID_YEARLY
    else:
        price_id = STRIPE_PRICE_ID_MONTHLY

    if not price_id or price_id == "price_REPLACE_ME":
        raise HTTPException(status_code=503, detail="Pricing not configured. Contact support.")

    # Get or create the user's subscription record
    sub = get_or_create_subscription(db, current_user)

    try:
        # Create or reuse Stripe customer
        if not sub.stripe_customer_id:
            customer = stripe.Customer.create(
                email=current_user.email,
                name=current_user.full_name or "",
                metadata={"user_id": str(current_user.id)}
            )
            sub.stripe_customer_id = customer.id
            db.commit()

        # Create checkout session
        session = stripe.checkout.Session.create(
            customer=sub.stripe_customer_id,
            payment_method_types=["card"],
            line_items=[{"price": price_id, "quantity": 1}],
            mode="subscription",
            success_url=f"{FRONTEND_URL}/dashboard?payment=success",
            cancel_url=f"{FRONTEND_URL}/pricing?payment=canceled",
            metadata={
                "user_id": str(current_user.id),
                "plan": plan
            }
        )

        return {"checkout_url": session.url, "session_id": session.id}

    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Stripe Error: {str(e)}")


# ─── 3. Stripe Webhook Handler ───
@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    """Handles Stripe webhook events for subscription lifecycle management."""
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    try:
        if STRIPE_WEBHOOK_SECRET and STRIPE_WEBHOOK_SECRET != "whsec_REPLACE_ME":
            event = stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
        else:
            # In development, parse without verification
            import json
            event = stripe.Event.construct_from(
                json.loads(payload), stripe.api_key
            )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    event_type = event["type"]
    data = event["data"]["object"]

    if event_type == "checkout.session.completed":
        # User just completed checkout — activate their subscription
        _handle_checkout_completed(db, data)

    elif event_type == "customer.subscription.updated":
        _handle_subscription_updated(db, data)

    elif event_type == "customer.subscription.deleted":
        _handle_subscription_deleted(db, data)

    elif event_type == "invoice.payment_failed":
        _handle_payment_failed(db, data)

    return {"status": "ok"}


def _handle_checkout_completed(db: Session, session_data: dict):
    """Activate subscription after successful checkout."""
    customer_id = session_data.get("customer")
    subscription_id = session_data.get("subscription")
    plan = session_data.get("metadata", {}).get("plan", "pro_monthly")

    sub = db.query(models.Subscription).filter(
        models.Subscription.stripe_customer_id == customer_id
    ).first()

    if sub:
        sub.plan = plan
        sub.status = "active"
        sub.stripe_subscription_id = subscription_id
        sub.updated_at = datetime.utcnow()
        db.commit()
        print(f"✅ Subscription activated for customer {customer_id}: {plan}")


def _handle_subscription_updated(db: Session, sub_data: dict):
    """Update subscription status and period dates."""
    stripe_sub_id = sub_data.get("id")
    sub = db.query(models.Subscription).filter(
        models.Subscription.stripe_subscription_id == stripe_sub_id
    ).first()

    if sub:
        sub.status = sub_data.get("status", sub.status)
        period = sub_data.get("current_period_end")
        if period:
            sub.current_period_end = datetime.utcfromtimestamp(period)
        period_start = sub_data.get("current_period_start")
        if period_start:
            sub.current_period_start = datetime.utcfromtimestamp(period_start)
        sub.updated_at = datetime.utcnow()
        db.commit()


def _handle_subscription_deleted(db: Session, sub_data: dict):
    """Downgrade user to free when subscription is canceled."""
    stripe_sub_id = sub_data.get("id")
    sub = db.query(models.Subscription).filter(
        models.Subscription.stripe_subscription_id == stripe_sub_id
    ).first()

    if sub:
        sub.plan = "free"
        sub.status = "canceled"
        sub.updated_at = datetime.utcnow()
        db.commit()
        print(f"⚠️ Subscription canceled for user {sub.user_id}")


def _handle_payment_failed(db: Session, invoice_data: dict):
    """Mark subscription as past_due when payment fails."""
    customer_id = invoice_data.get("customer")
    sub = db.query(models.Subscription).filter(
        models.Subscription.stripe_customer_id == customer_id
    ).first()

    if sub:
        sub.status = "past_due"
        sub.updated_at = datetime.utcnow()
        db.commit()


# ─── 4. Customer Portal (Manage Subscription) ───
@router.post("/customer-portal")
def create_customer_portal(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Creates a Stripe Customer Portal session so users can manage their subscription."""
    sub = get_or_create_subscription(db, current_user)

    if not sub.stripe_customer_id:
        raise HTTPException(status_code=400, detail="No active subscription to manage.")

    try:
        session = stripe.billing_portal.Session.create(
            customer=sub.stripe_customer_id,
            return_url=f"{FRONTEND_URL}/dashboard"
        )
        return {"portal_url": session.url}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Stripe Error: {str(e)}")


# ─── 5. Get Available Plans ───
@router.get("/plans")
def get_available_plans():
    """Returns pricing information for the frontend pricing page."""
    return {
        "plans": [
            {
                "id": "free",
                "name": "Free",
                "price": 0,
                "currency": "usd",
                "interval": None,
                "features": [
                    "3 beginner courses",
                    "3 AI tutor messages per day",
                    "Community forum access",
                    "Basic code editor"
                ]
            },
            {
                "id": "pro_monthly",
                "name": "Pro Monthly",
                "price": 9.99,
                "currency": "usd",
                "interval": "month",
                "features": [
                    "All courses & learning paths",
                    "Unlimited AI tutor",
                    "Downloadable certificates",
                    "Guided projects",
                    "Priority support",
                    "Skill assessments"
                ]
            },
            {
                "id": "pro_yearly",
                "name": "Pro Yearly",
                "price": 79.00,
                "currency": "usd",
                "interval": "year",
                "features": [
                    "Everything in Pro Monthly",
                    "Save 34% vs monthly",
                    "Early access to new courses",
                    "LinkedIn badge"
                ]
            }
        ]
    }
