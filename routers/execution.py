from fastapi import APIRouter
from schemas import CodeSubmission
import subprocess

router = APIRouter(tags=["Code Execution"])

@router.post("/run-python/")
def execute_python_code(submission: CodeSubmission):
    try:
        # 1. Run the code inside an isolated Docker container via stdin
        result = subprocess.run(
            [
                "docker", "run", "--rm", "-i", 
                "--net", "none",
                "--memory", "128m", 
                "--cpus", "0.5", 
                "python:3.9-slim", 
                "python", "-"
            ],
            input=submission.code,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # 2. Grab the output
        output = result.stdout
        error_output = result.stderr
        exit_code = result.returncode
        
        final_output = output if exit_code == 0 else error_output
        
        return {
            "output": final_output,
            "exit_code": exit_code
        }
            
    except subprocess.TimeoutExpired:
        return {"output": "Error: Code took too long to run (Infinite Loop?).", "exit_code": 1}
    except Exception as e:
        return {"output": f"Server Error: {str(e)}", "exit_code": 1}
