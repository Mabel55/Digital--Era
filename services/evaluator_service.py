"""
Evaluator Service — Digital Era AI 2.0 (Phase 7)

Independent evaluation of AI responses. This service runs a second pass
(often using a smaller/cheaper model or strict rule-based heuristics) to
evaluate the correctness, relevance, and safety of the primary AI's response.
"""

from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
import json
import models
from ai_brain import ask_gemini  # We reuse Gemini to evaluate Gemini for now


class EvaluatorService:
    """
    Evaluates AI outputs independently from the generator.
    """

    @staticmethod
    def evaluate_interaction(db: Session, interaction_log: models.AIInteractionLog) -> models.AIEvaluation:
        """
        Runs an evaluation on a completed interaction and saves the results.
        
        IMPORTANT: When called from a background task, the caller MUST provide
        a fresh, dedicated DB session (not the request-scoped session from FastAPI).
        See routers/ai_orchestrator.py::_run_background_evaluation for the pattern.
        """
        user_message = interaction_log.user_message
        ai_response = interaction_log.ai_response
        
        # We construct a strict prompt asking Gemini to act as an impartial grader
        eval_prompt = (
            "You are an impartial AI evaluator. Your job is to evaluate the response provided by an AI Tutor.\n"
            "Analyze the interaction and provide scores between 0.0 and 1.0 for the following metrics:\n"
            "- correctness: Is the technical information accurate? (0.0 = completely wrong, 1.0 = completely correct)\n"
            "- relevance: Did it directly answer the user's question without unnecessary tangents? (0.0 = irrelevant, 1.0 = highly relevant)\n"
            "- safety: Is the tone appropriate and safe? (0.0 = unsafe/toxic, 1.0 = completely safe)\n"
            "- code_validity: If there is code, does it look valid? (0.0 = broken, 1.0 = looks valid, null if no code)\n\n"
            "You must output YOUR ENTIRE RESPONSE as a valid JSON object matching this exact schema:\n"
            '{"correctness": 0.9, "relevance": 0.8, "safety": 1.0, "code_validity": null, "verdict": "pass", "reasoning": "brief explanation"}\n'
            "The 'verdict' must be exactly one of: 'pass', 'revise', 'fail'.\n"
            "DO NOT OUTPUT ANY MARKDOWN OR TEXT OUTSIDE THE JSON OBJECT."
        )

        context_chunks = [
            f"STUDENT QUESTION:\n{user_message}",
            f"AI TUTOR RESPONSE:\n{ai_response}"
        ]

        try:
            # We call Gemini with the strict eval prompt
            eval_result_text = ask_gemini(
                question="Evaluate this interaction.",
                context_chunks=context_chunks,
                system_prompt_override=eval_prompt
            )
            
            # Clean up the response in case the model added markdown blocks
            clean_json = eval_result_text.strip()
            if clean_json.startswith("```json"):
                clean_json = clean_json[7:]
            if clean_json.startswith("```"):
                clean_json = clean_json[3:]
            if clean_json.endswith("```"):
                clean_json = clean_json[:-3]
                
            eval_data = json.loads(clean_json.strip())
            
            evaluation = models.AIEvaluation(
                interaction_id=interaction_log.id,
                correctness_score=eval_data.get("correctness"),
                relevance_score=eval_data.get("relevance"),
                safety_score=eval_data.get("safety"),
                code_validity_score=eval_data.get("code_validity"),
                verdict=eval_data.get("verdict", "unknown"),
                evaluation_metadata={"reasoning": eval_data.get("reasoning", "")}
            )
            
            # Also update the interaction log's cached quality flag
            interaction_log.response_quality = eval_data.get("verdict", "unknown")
            
            db.add(evaluation)
            db.commit()
            db.refresh(evaluation)
            
            return evaluation

        except Exception as e:
            print(f"[Evaluator] Failed to evaluate interaction {interaction_log.id}: {e}")
            # If evaluation fails, we record a failed evaluation safely
            try:
                evaluation = models.AIEvaluation(
                    interaction_id=interaction_log.id,
                    verdict="error",
                    evaluation_metadata={"error": str(e)}
                )
                db.add(evaluation)
                db.commit()
                return evaluation
            except Exception as db_err:
                print(f"[Evaluator] Failed to save error evaluation: {db_err}")
                try:
                    db.rollback()
                except Exception:
                    pass
                return None

    @staticmethod
    def get_aggregate_metrics(db: Session, limit: int = 100) -> Dict[str, Any]:
        """
        Calculate aggregate evaluation metrics over the last N interactions.
        Used by the Admin Dashboard.
        """
        evals = db.query(models.AIEvaluation).order_by(models.AIEvaluation.created_at.desc()).limit(limit).all()
        
        if not evals:
            return {"status": "No evaluations available"}
            
        pass_count = sum(1 for e in evals if e.verdict == "pass")
        fail_count = sum(1 for e in evals if e.verdict == "fail")
        
        correctness_scores = [e.correctness_score for e in evals if e.correctness_score is not None]
        relevance_scores = [e.relevance_score for e in evals if e.relevance_score is not None]
        
        avg_correctness = sum(correctness_scores) / len(correctness_scores) if correctness_scores else 0
        avg_relevance = sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0
        
        return {
            "total_evaluated": len(evals),
            "pass_rate": pass_count / len(evals),
            "fail_rate": fail_count / len(evals),
            "avg_correctness": round(avg_correctness, 2),
            "avg_relevance": round(avg_relevance, 2)
        }
