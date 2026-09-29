"""
Tool Registry Service — Digital Era AI 2.0 (Phase 5)

A controlled registry of tools that the AI (or users) can execute.
Enforces permissions, handles sandboxed execution, and provides
comprehensive audit logging.
"""

from typing import Dict, Any, Callable, Optional, Tuple
import time
from sqlalchemy.orm import Session
import models

# Import existing code execution functions safely
# We reuse the existing sandboxed Docker infrastructure
from routers.execution import run_docker, run_sqlite

class ToolExecutionError(Exception):
    pass

class BaseTool:
    """Base class for all tools."""
    name: str = ""
    description: str = ""
    requires_auth: bool = True
    max_per_minute: int = 60

    def execute(self, params: Dict[str, Any], user: models.User, db: Session) -> Any:
        raise NotImplementedError()


class PythonExecutorTool(BaseTool):
    name = "python_executor"
    description = "Execute Python 3.9 code in a secure Docker sandbox."
    requires_auth = True
    max_per_minute = 20

    def execute(self, params: Dict[str, Any], user: models.User, db: Session) -> Any:
        code = params.get("code")
        if not code:
            raise ToolExecutionError("Missing 'code' parameter")
        
        files = params.get("files", None)
        entrypoint = params.get("entrypoint", "-")

        # Reuse existing robust docker sandbox
        result = run_docker("python:3.9-slim", ["python", entrypoint if files else "-"], code, files)
        
        if result.get("exit_code", 1) != 0:
            raise ToolExecutionError(result.get("output", "Unknown execution error"))
            
        return result


class SqlExecutorTool(BaseTool):
    name = "sql_executor"
    description = "Execute SQL queries in an isolated in-memory SQLite database."
    requires_auth = True
    max_per_minute = 30

    def execute(self, params: Dict[str, Any], user: models.User, db: Session) -> Any:
        code = params.get("code")
        if not code:
            raise ToolExecutionError("Missing 'code' parameter")

        result = run_sqlite(code)
        
        if result.get("exit_code", 1) != 0:
            raise ToolExecutionError(result.get("output", "Unknown execution error"))
            
        return result


class CourseSearchTool(BaseTool):
    name = "course_search"
    description = "Search the course catalog and curriculum."
    requires_auth = False
    
    def execute(self, params: Dict[str, Any], user: models.User, db: Session) -> Any:
        query = params.get("query")
        if not query:
            raise ToolExecutionError("Missing 'query' parameter")
            
        # Import here to avoid circular dependencies
        from services.rag_service import rag_service
        
        results = rag_service.retrieve(db, query, top_k=5, source_type="lesson")
        return [
            {
                "title": r["metadata"].get("title"),
                "content_snippet": r["content"][:200] + "..."
            }
            for r in results
        ]


class ToolRegistry:
    """Registry managing available tools and execution logging."""
    
    _tools: Dict[str, BaseTool] = {
        "python_executor": PythonExecutorTool(),
        "sql_executor": SqlExecutorTool(),
        "course_search": CourseSearchTool(),
    }

    @classmethod
    def get_available_tools(cls) -> list[dict]:
        """Return a schema of all available tools."""
        return [
            {
                "name": tool.name,
                "description": tool.description,
                "requires_auth": tool.requires_auth
            }
            for tool in cls._tools.values()
        ]

    @classmethod
    def execute_tool(
        cls, 
        db: Session, 
        tool_name: str, 
        params: Dict[str, Any], 
        user: models.User
    ) -> Any:
        """
        Execute a tool safely, enforcing permissions and logging the result.
        """
        if tool_name not in cls._tools:
            raise ValueError(f"Tool '{tool_name}' not found.")
            
        tool = cls._tools[tool_name]
        
        if tool.requires_auth and not user:
            raise PermissionError(f"Tool '{tool_name}' requires authentication.")

        start_time = time.time()
        is_success = True
        output_data = {}
        error_message = None

        try:
            # Execute the actual tool
            result = tool.execute(params, user, db)
            output_data = result if isinstance(result, (dict, list)) else {"result": result}
            return result
            
        except ToolExecutionError as e:
            is_success = False
            error_message = str(e)
            output_data = {"error": error_message}
            raise e
            
        except Exception as e:
            is_success = False
            error_message = f"Internal Tool Error: {str(e)}"
            output_data = {"error": error_message}
            raise e
            
        finally:
            # Always log the execution, regardless of success/failure
            latency_ms = int((time.time() - start_time) * 1000)
            
            try:
                log = models.ToolInvocationLog(
                    user_id=user.id if user else 0, # 0 for system/unauth
                    tool_name=tool_name,
                    input_data=params,
                    output_data=output_data,
                    is_success=is_success,
                    error_message=error_message,
                    latency_ms=latency_ms
                )
                db.add(log)
                db.commit()
            except Exception as log_e:
                print(f"[ToolRegistry] Failed to log tool invocation: {log_e}")
