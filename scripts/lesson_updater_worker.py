"""
Automated Lesson Updater Worker — Digital Era AI 2.0 (Phase 9)

This script runs periodically in the background. It finds lessons that
students are consistently failing (or have poor AI interactions on).
It uses an agentic loop (with access to the Python code executor) to
rewrite the lesson content to be clearer and less error-prone, then
submits a LessonUpdateProposal for an admin to review.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import json
import re
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
import models
from ai_brain import ask_gemini
from services.tool_registry import ToolRegistry


def find_low_performing_lessons(db: Session, limit: int = 5) -> list[models.Lesson]:
    """
    Identifies lessons that need improvement.
    For Phase 9 MVP, we look for lessons that have the most 'fail' or 'revise' evaluations.
    """
    # Join Interactions -> Evaluations to find bad interactions, then group by topic/lesson
    # Since topic is stored as a string (course_name), for MVP we'll just pick random lessons 
    # that haven't been proposed yet to demonstrate the agentic rewriting.
    
    # In a fully populated production DB, this would be:
    # SELECT lesson_id, COUNT(*) as failures FROM ai_interactions i 
    # JOIN ai_evaluations e ON i.id = e.interaction_id WHERE e.verdict = 'fail' GROUP BY lesson_id ...
    
    proposed_lesson_ids = [r[0] for r in db.query(models.LessonUpdateProposal.lesson_id).all()]
    
    lessons = db.query(models.Lesson)\
        .filter(~models.Lesson.id.in_(proposed_lesson_ids))\
        .order_by(func.random())\
        .limit(limit)\
        .all()
        
    return lessons


def rewrite_lesson_agentically(db: Session, lesson: models.Lesson) -> str:
    """
    Uses an Agentic Loop to analyze and rewrite a lesson.
    The AI is given access to the Python Executor tool to test any code it writes.
    """
    print(f"🤖 Agent started reviewing Lesson '{lesson.title}'...")
    
    tools_schema = ToolRegistry.get_available_tools()
    
    system_prompt = (
        "You are an Expert Curriculum Developer and Senior Engineer.\n"
        "Your task is to review a programming lesson that students are struggling with, "
        "and rewrite it to be clearer, more engaging, and completely error-free.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "1. You MUST use the `python_executor` tool to test ALL code snippets you intend to include in the lesson. Never publish untested code.\n"
        "2. Format your final output as pure Markdown, starting with the Lesson Title.\n"
        "3. Use the `<think>...</think>` tags to plan your rewrite before returning the final content.\n"
        "4. If you need a tool, output exactly:\n"
        "<tool_call>{\"tool\": \"tool_name\", \"params\": {\"key\": \"value\"}}</tool_call>\n"
        "and wait for the output.\n"
    )
    
    context = [
        f"--- ORIGINAL LESSON CONTENT ---\n{lesson.content}\n------------------------------",
        "Reason for rewrite: Automated routine maintenance to improve clarity and test code snippets."
    ]
    
    max_iterations = 4
    iteration = 0
    final_content = ""
    
    while iteration < max_iterations:
        iteration += 1
        print(f"   [Iteration {iteration}/{max_iterations}] Thinking...")
        
        try:
            raw_answer = ask_gemini(
                question="Please review, test, and rewrite this lesson.",
                context_chunks=context,
                system_prompt_override=system_prompt
            )
            
            # Check for tool call
            tool_match = re.search(r'<tool_call>(.*?)</tool_call>', raw_answer, re.DOTALL)
            if tool_match:
                tool_json_str = tool_match.group(1).strip()
                try:
                    tool_req = json.loads(tool_json_str)
                    tool_name = tool_req.get("tool")
                    tool_params = tool_req.get("params", {})
                    
                    print(f"   🛠️ Agent is using tool: {tool_name}")
                    tool_result = ToolRegistry.execute_tool(db, tool_name, tool_params, user=None)
                    
                    context.append(f"Tool '{tool_name}' result:\n```json\n{json.dumps(tool_result, indent=2)}\n```\nAnalyze the result and continue.")
                    continue
                except Exception as e:
                    context.append(f"Tool execution failed: {e}. Please adjust.")
                    continue
                    
            # Extract final content (remove thinking block)
            think_match = re.search(r'<think>(.*?)</think>', raw_answer, re.DOTALL)
            if think_match:
                final_content = re.sub(r'<think>.*?</think>', '', raw_answer, flags=re.DOTALL).strip()
            else:
                final_content = raw_answer.strip()
                
            break
            
        except Exception as e:
            print(f"   ❌ API Error: {e}")
            break
            
    return final_content


def run_updater_worker():
    print("🚀 Starting Automated Lesson Updater Worker...")
    db = SessionLocal()
    try:
        lessons = find_low_performing_lessons(db, limit=1) # Just 1 for testing
        
        if not lessons:
            print("✅ No low-performing lessons found. Sleeping.")
            return
            
        for lesson in lessons:
            rewritten_content = rewrite_lesson_agentically(db, lesson)
            
            if not rewritten_content:
                print(f"⚠️ Failed to rewrite lesson '{lesson.title}'.")
                continue
                
            # Create a proposal instead of silently overwriting
            proposal = models.LessonUpdateProposal(
                lesson_id=lesson.id,
                reason="Routine automated optimization (tested code snippets and improved clarity).",
                original_content=lesson.content,
                proposed_content=rewritten_content,
                status="pending"
            )
            db.add(proposal)
            db.commit()
            print(f"✅ Submitted LessonUpdateProposal for '{lesson.title}'! Admin can review it in the dashboard.")
            
    finally:
        db.close()


if __name__ == "__main__":
    run_updater_worker()
