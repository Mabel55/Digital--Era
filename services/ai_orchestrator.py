"""
AI Orchestrator Service — Digital Era AI 2.0 (Phase 4)

This is the central coordinating "brain" for the 2.0 architecture.
It manages the flow of a user request through the entire system:
Understanding -> Memory Retrieval -> RAG -> Generation -> Learning.

Future phases will inject Planning (Phase 6), Tool Execution (Phase 5), 
and Evaluation (Phase 7) into this pipeline.
"""

from typing import Dict, Any, Optional, Tuple
from pydantic import BaseModel
import time
import json
import re
from sqlalchemy.orm import Session
import models

# Import Phase 2 (Memory), Phase 3 (RAG), and Phase 5 (Tools) services
from services.memory_service import MemoryService
from services.student_model_service import StudentModelService
from services.rag_service import rag_service
from services.tool_registry import ToolRegistry

# Import core LLM
from ai_brain import ask_gemini


class OrchestratorRequest(BaseModel):
    user_id: int
    message: str
    course_name: str
    lesson_id: Optional[int] = None
    level: str = "Beginner"
    track: str = "General"
    persona: str = "study_buddy"


class OrchestratorResponse(BaseModel):
    answer: str
    thought_process: Optional[str] = None
    sources: list[dict]
    latency_ms: int
    intent: str


class AIOrchestrator:
    """
    Coordinates the entire AI request lifecycle.
    """

    @staticmethod
    def classify_intent(message: str) -> str:
        """
        Classify what the user is trying to do.
        For now (Phase 4), we use fast heuristics. 
        In future phases, we could use a fast LLM pass.
        """
        msg_lower = message.lower()
        if any(w in msg_lower for w in ["help", "stuck", "error", "bug", "doesn't work", "why"]):
            return "troubleshooting"
        elif any(w in msg_lower for w in ["explain", "what is", "how do", "meaning"]):
            return "concept_explanation"
        elif any(w in msg_lower for w in ["review", "feedback", "my code"]):
            return "code_review"
        else:
            return "general_question"

    @staticmethod
    def get_persona_prompt(persona: str) -> str:
        if persona == "code_reviewer":
            return (
                "--- PERSONA: CODE REVIEWER ---\n"
                "Your job is to explicitly grade and review the user's assignment or code. "
                "Point out security flaws, performance bottlenecks, and bad practices. "
                "Do not give them a hint; give them a strict, professional code review.\n"
                "------------------------------\n"
            )
        else: # study_buddy
            return (
                "--- PERSONA: STUDY BUDDY ---\n"
                "Your job is to guide the student towards the answer without ever giving them the exact code. "
                "Provide hints, ask Socratic questions, and help them debug their own code. "
                "NEVER output the full correct code solution.\n"
                "----------------------------\n"
            )

    @staticmethod
    def process_chat(db: Session, request: OrchestratorRequest) -> Tuple[OrchestratorResponse, Optional[models.AIInteractionLog]]:
        """
        The main pipeline for processing a student's chat request.
        """
        start_time = time.time()

        # 1. UNDERSTAND
        # What is the student trying to achieve?
        intent = AIOrchestrator.classify_intent(request.message)

        # 2. MEMORY RETRIEVAL (Phase 2)
        # What do we know about this student that might help?
        student_context_str = ""
        try:
            student_context = StudentModelService.get_context_for_ai(
                db, request.user_id, topic=request.course_name
            )
            student_context_str = student_context if student_context else ""
        except Exception as e:
            print(f"[Orchestrator] Memory retrieval warning: {e}")

        # 3. KNOWLEDGE RETRIEVAL / RAG (Phase 3)
        # What course materials do we need to answer this?
        rag_context_chunks = []
        sources = []
        try:
            # We search the RAG system using the specific lesson if provided, otherwise general course
            results = rag_service.retrieve(
                db=db, 
                query=request.message, 
                top_k=3, 
                source_type="lesson", 
                source_id=request.lesson_id
            )
            
            for r in results:
                rag_context_chunks.append(r["content"])
                sources.append({
                    "title": r["metadata"].get("title"), 
                    "lesson_id": r["metadata"].get("lesson_id")
                })
        except Exception as e:
            print(f"[Orchestrator] RAG retrieval warning: {e}")

        # 4. CONSTRUCT CONTEXT
        # Combine everything for the generator
        final_context = []
        
        # Inject RAG context
        if rag_context_chunks:
            final_context.extend(rag_context_chunks)
            
        # Inject Persona Instructions (Phase 10)
        final_context.append(AIOrchestrator.get_persona_prompt(request.persona))
            
        # Inject Student Memory Context (crucial for personalization)
        if student_context_str:
            final_context.append(student_context_str)
            
        # Inject Available Tools Schema
        tools_schema = ToolRegistry.get_available_tools()
        tools_instruction = (
            "--- AVAILABLE TOOLS ---\n"
            f"{json.dumps(tools_schema, indent=2)}\n"
            "If you need to use a tool (e.g. to test code before answering), output exactly:\n"
            "<tool_call>{\"tool\": \"tool_name\", \"params\": {\"key\": \"value\"}}</tool_call>\n"
            "Do not output anything else if you are calling a tool. Wait for the system to return the result."
            "-----------------------\n"
        )
        final_context.append(tools_instruction)

        # 5. EXECUTE (Agentic Loop)
        thought_process = None
        max_iterations = 3
        iteration = 0
        raw_answer = ""
        
        # Mock user object for tool registry permissions
        from models import User
        mock_user = db.query(User).filter(User.id == request.user_id).first()
        
        while iteration < max_iterations:
            iteration += 1
            try:
                raw_answer = ask_gemini(
                    question=request.message,
                    context_chunks=final_context,
                    chat_history=[], 
                    course_title=request.course_name,
                    student_level=request.level,
                    student_track=request.track
                )
                
                # Check if the AI wants to call a tool
                tool_match = re.search(r'<tool_call>(.*?)</tool_call>', raw_answer, re.DOTALL)
                if tool_match:
                    tool_json_str = tool_match.group(1).strip()
                    try:
                        tool_req = json.loads(tool_json_str)
                        tool_name = tool_req.get("tool")
                        tool_params = tool_req.get("params", {})
                        
                        # Execute the tool
                        tool_result = ToolRegistry.execute_tool(db, tool_name, tool_params, mock_user)
                        
                        # Feed the result back into the context for the next iteration
                        final_context.append(f"Tool '{tool_name}' execution result:\n```json\n{json.dumps(tool_result, indent=2)}\n```\nAnalyze this result and provide your final answer, or call another tool.")
                        continue # Loop again
                        
                    except Exception as tool_e:
                        final_context.append(f"Tool execution failed: {tool_e}. Please adjust your tool call or answer without it.")
                        continue # Loop again

                # Phase 6: Parse out the reasoning block from the final answer
                think_match = re.search(r'<think>(.*?)</think>', raw_answer, re.DOTALL)
                if think_match:
                    thought_process = think_match.group(1).strip()
                    answer = re.sub(r'<think>.*?</think>', '', raw_answer, flags=re.DOTALL).strip()
                else:
                    answer = raw_answer.strip()
                    
                break # We got a final answer, exit the loop
                    
            except Exception as e:
                answer = f"I'm currently experiencing a technical issue connecting to my brain. Please try again in a moment. (Error: {e})"
                break

        latency = int((time.time() - start_time) * 1000)

        # 6. LEARN (Update Memory)
        # Analyze what just happened and update the student model
        interaction_log = None
        try:
            StudentModelService.update_after_chat(
                db=db,
                user_id=request.user_id,
                topic=request.course_name,
                course_name=request.course_name,
                user_message=request.message,
                ai_response=answer
            )
            
            interaction_log = MemoryService.log_interaction(
                db=db,
                user_id=request.user_id,
                interaction_type="orchestrated_chat",
                user_message=request.message,
                ai_response=answer,
                topic=request.course_name,
                course_name=request.course_name,
                latency_ms=latency,
                metadata={"intent": intent}
            )
        except Exception as e:
            print(f"[Orchestrator] Memory learning warning: {e}")

        response = OrchestratorResponse(
            answer=answer,
            thought_process=thought_process,
            sources=sources,
            latency_ms=latency,
            intent=intent
        )
        
        return response, interaction_log
