"""
Tools Router — Digital Era AI 2.0 (Phase 5)

API endpoints for discovering and executing tools securely.
Allows the AI frontend to trigger specific tools (like code execution)
with full auditing.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from pydantic import BaseModel

from database import get_db
import models
from auth import get_current_user
from services.tool_registry import ToolRegistry, ToolExecutionError

router = APIRouter(prefix="/api/v2/tools", tags=["AI 2.0 — Tool Registry"])


class ToolExecutionRequest(BaseModel):
    params: Dict[str, Any]


@router.get("")
def list_tools():
    """List all available tools and their required parameters."""
    return {"tools": ToolRegistry.get_available_tools()}


@router.post("/{tool_name}/run")
def execute_tool(
    tool_name: str,
    request: ToolExecutionRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Execute a specific tool with the provided parameters.
    Execution is sandboxed and logged to the database.
    """
    try:
        result = ToolRegistry.execute_tool(
            db=db,
            tool_name=tool_name,
            params=request.params,
            user=current_user
        )
        return {"success": True, "result": result}
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except ToolExecutionError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tool Execution Failed: {str(e)}")
