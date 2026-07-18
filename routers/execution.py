from fastapi import APIRouter
from schemas import CodeSubmission
import subprocess
import sqlite3
import pandas as pd
import tempfile
import shutil
import os
from fastapi import Request
from limiter import limiter

router = APIRouter(tags=["Code Execution"])

@router.post("/run-code/")
@limiter.limit("20/minute")
def execute_code(request: Request, submission: CodeSubmission):
    language = submission.language.lower()
    code = submission.code
    files = submission.files
    entrypoint = submission.entrypoint

    try:
        if language == "python":
            return run_docker("python:3.9-slim", ["python", entrypoint if files else "-"], code, files)
        
        elif language == "javascript" or language == "js":
            return run_docker("node:18-slim", ["node", entrypoint if files else "-"], code, files)
            
        elif language == "sql":
            return run_sqlite(code)
            
        else:
            return {"output": f"Error: Unsupported language '{language}'", "exit_code": 1}
            
    except subprocess.TimeoutExpired:
        return {"output": "Error: Code took too long to run (Infinite Loop?).", "exit_code": 1}
    except Exception as e:
        return {"output": f"Server Error: {str(e)}", "exit_code": 1}


def run_docker(image: str, command: list, stdin_input: str, files: dict = None):
    temp_dir = None
    mount_args = []
    
    if files:
        temp_dir = tempfile.mkdtemp()
        for filename, content in files.items():
            safe_name = os.path.basename(filename)
            file_path = os.path.join(temp_dir, safe_name)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        mount_args = ["-v", f"{temp_dir}:/app", "-w", "/app"]
        stdin_input = ""
    
    docker_cmd = [
        "docker", "run", "--rm", "-i", 
        "--net", "none",
        "--memory", "128m", 
        "--cpus", "0.5"
    ] + mount_args + [image] + (command if files else command[1:])
    
    try:
        # 1. Try Docker first
        result = subprocess.run(
            docker_cmd,
            input=stdin_input,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # 2. If Docker daemon is off, fallback to native execution
        if result.returncode != 0 and "Cannot connect to the Docker daemon" in result.stderr:
            native_cmd = command.copy()
            if not files:
                native_cmd = [command[0], "-c", stdin_input] if "python" in command[0] else [command[0], "-e", stdin_input]
                
            native_result = subprocess.run(
                native_cmd,
                cwd=temp_dir if files else None,
                capture_output=True,
                text=True,
                timeout=10
            )
            return {
                "output": native_result.stdout if native_result.returncode == 0 else native_result.stderr,
                "exit_code": native_result.returncode
            }
            
        output = result.stdout
        error_output = result.stderr
        exit_code = result.returncode
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
    
    final_output = output if exit_code == 0 else error_output
    
    return {
        "output": final_output,
        "exit_code": exit_code
    }


def run_sqlite(sql_code: str):
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        # We might have multiple statements.
        statements = sql_code.split(';')
        
        output_lines = []
        for stmt in statements:
            stmt = stmt.strip()
            if not stmt:
                continue
                
            cursor.execute(stmt)
            if stmt.upper().startswith("SELECT"):
                rows = cursor.fetchall()
                if rows:
                    # Format as simple table
                    cols = [description[0] for description in cursor.description]
                    df = pd.DataFrame(rows, columns=cols)
                    output_lines.append(df.to_string(index=False))
                else:
                    output_lines.append("(0 rows returned)")
            else:
                output_lines.append(f"Successfully executed: {stmt[:30]}...")
                
        conn.commit()
        conn.close()
        
        return {
            "output": "\n\n".join(output_lines),
            "exit_code": 0
        }
    except Exception as e:
        return {
            "output": f"SQL Error: {str(e)}",
            "exit_code": 1
        }
