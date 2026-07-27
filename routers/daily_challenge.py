"""
Daily Challenge Router — DataCamp's #1 Retention Feature
Generates AI-powered daily coding challenges and tracks submissions.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from auth import get_current_user
from ai_brain import ask_gemini
from datetime import date, datetime
import json

router = APIRouter(prefix="/daily-challenge", tags=["Daily Challenge"])


def _get_or_generate_challenge(db: Session) -> models.DailyChallenge:
    """Get today's challenge or generate a new one via AI."""
    today = date.today()
    
    challenge = db.query(models.DailyChallenge).filter(
        models.DailyChallenge.challenge_date == today
    ).first()
    
    if challenge:
        return challenge
    
    # Generate new challenge via AI
    difficulties = ["Beginner", "Intermediate", "Advanced"]
    day_of_week = today.weekday()
    difficulty = difficulties[day_of_week % 3]
    
    prompt = f"""Generate a Python coding challenge for {difficulty} level.
Return STRICTLY as raw JSON (no markdown, no ```json) with these keys:
- "title": short descriptive title (max 60 chars)
- "description": clear problem statement with examples (2-3 paragraphs)
- "starter_code": Python starter code with function signature and docstring
- "hint": a helpful hint without giving the solution
- "solution": the complete working solution
- "test_cases": array of objects with "input" and "expected" keys (3-5 test cases)
- "xp_reward": integer between 15 and 50 based on difficulty

Make the challenge practical and fun. Include real-world context."""

    try:
        raw = ask_gemini("Generate the challenge JSON now.", system_prompt_override=prompt)
        raw = raw.strip()
        if raw.startswith("```json"):
            raw = raw[7:]
        if raw.startswith("```"):
            raw = raw[3:]
        if raw.endswith("```"):
            raw = raw[:-3]
        
        data = json.loads(raw.strip())
        
        challenge = models.DailyChallenge(
            challenge_date=today,
            title=data.get("title", f"Daily Challenge - {today.strftime('%B %d')}"),
            description=data.get("description", "Solve this coding challenge!"),
            difficulty=difficulty,
            language="python",
            starter_code=data.get("starter_code", "# Write your solution here\n"),
            solution=data.get("solution"),
            hint=data.get("hint"),
            test_cases=data.get("test_cases"),
            xp_reward=data.get("xp_reward", 25)
        )
        db.add(challenge)
        db.commit()
        db.refresh(challenge)
        return challenge
        
    except Exception as e:
        print(f"AI Challenge generation failed: {e}")
        # Fallback challenge
        challenge = models.DailyChallenge(
            challenge_date=today,
            title=f"Daily Python Challenge - {today.strftime('%B %d')}",
            description="Write a function that takes a list of numbers and returns the sum of all even numbers in the list.\n\nExample:\n- Input: [1, 2, 3, 4, 5, 6] → Output: 12\n- Input: [7, 11, 13] → Output: 0",
            difficulty="Beginner",
            language="python",
            starter_code="def sum_even(numbers):\n    # Your code here\n    pass\n\n# Test it\nprint(sum_even([1, 2, 3, 4, 5, 6]))\n",
            hint="Use a loop or list comprehension with the modulo operator (%) to check if a number is even.",
            solution="def sum_even(numbers):\n    return sum(n for n in numbers if n % 2 == 0)\n\nprint(sum_even([1, 2, 3, 4, 5, 6]))\n",
            test_cases=[{"input": "[1,2,3,4,5,6]", "expected": "12"}, {"input": "[7,11,13]", "expected": "0"}],
            xp_reward=25
        )
        db.add(challenge)
        db.commit()
        db.refresh(challenge)
        return challenge


@router.get("/", response_model=schemas.DailyChallengeResponse)
def get_daily_challenge(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Get today's coding challenge."""
    challenge = _get_or_generate_challenge(db)
    
    # Check if user already completed it
    submission = db.query(models.DailyChallengeSubmission).filter(
        models.DailyChallengeSubmission.user_id == current_user.id,
        models.DailyChallengeSubmission.challenge_id == challenge.id,
        models.DailyChallengeSubmission.passed == True
    ).first()
    
    response = schemas.DailyChallengeResponse(
        id=challenge.id,
        challenge_date=challenge.challenge_date,
        title=challenge.title,
        description=challenge.description,
        difficulty=challenge.difficulty,
        language=challenge.language,
        starter_code=challenge.starter_code,
        hint=challenge.hint,
        xp_reward=challenge.xp_reward,
        already_completed=submission is not None
    )
    return response


@router.post("/submit")
def submit_challenge(
    payload: schemas.DailyChallengeSubmit,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Submit a solution for today's challenge."""
    challenge = db.query(models.DailyChallenge).filter(
        models.DailyChallenge.id == payload.challenge_id
    ).first()
    
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    # Check if already passed
    existing = db.query(models.DailyChallengeSubmission).filter(
        models.DailyChallengeSubmission.user_id == current_user.id,
        models.DailyChallengeSubmission.challenge_id == challenge.id,
        models.DailyChallengeSubmission.passed == True
    ).first()
    
    if existing:
        return {"passed": True, "message": "You already completed this challenge!", "xp_gained": 0}
    
    # Use AI to evaluate the submission
    eval_prompt = f"""You are an automated code grader. Evaluate this Python code submission.

Challenge: {challenge.title}
Description: {challenge.description}
Expected solution approach: {challenge.solution or 'N/A'}

Student's code:
```python
{payload.code}
```

Reply STRICTLY in JSON (no markdown):
{{"passed": true/false, "feedback": "Brief encouraging feedback"}}"""

    try:
        result_raw = ask_gemini("Evaluate now.", system_prompt_override=eval_prompt)
        result_raw = result_raw.strip()
        if "```json" in result_raw:
            result_raw = result_raw.split("```json")[1].split("```")[0].strip()
        elif "```" in result_raw:
            result_raw = result_raw.split("```")[1].strip()
        
        result = json.loads(result_raw)
        passed = result.get("passed", False)
        feedback = result.get("feedback", "Code evaluated.")
    except Exception:
        # If AI fails, be generous
        passed = True
        feedback = "Great effort! Your solution has been accepted."
    
    # Save submission
    submission = models.DailyChallengeSubmission(
        user_id=current_user.id,
        challenge_id=challenge.id,
        submitted_code=payload.code,
        passed=passed
    )
    db.add(submission)
    
    xp_gained = 0
    if passed:
        xp_gained = challenge.xp_reward
        current_user.xp += xp_gained
        current_user.level = models.calculate_level(current_user.xp)
        
        # Track activity
        today = date.today()
        activity = db.query(models.UserActivity).filter(
            models.UserActivity.user_id == current_user.id,
            models.UserActivity.activity_date == today
        ).first()
        if not activity:
            activity = models.UserActivity(user_id=current_user.id, activity_date=today)
            db.add(activity)
        activity.xp_earned += xp_gained
        activity.challenges_completed += 1
    
    db.commit()
    
    return {
        "passed": passed,
        "feedback": feedback,
        "xp_gained": xp_gained,
        "total_xp": current_user.xp,
        "new_level": current_user.level
    }
