from fastapi import APIRouter
from schemas import CodeSubmission
import subprocess
import sqlite3
import pandas as pd

router = APIRouter(tags=["Code Execution"])

@router.post("/run-code/")
def execute_code(submission: CodeSubmission):
    language = submission.language.lower()
    code = submission.code

    try:
        if language == "python":
            return run_docker("python:3.9-slim", ["python", "-"], code)
        
        elif language == "javascript" or language == "js":
            return run_docker("node:18-slim", ["node", "-e", code], "") # Pass code to -e or via stdin. Stdin is safer.
            
        elif language == "sql":
            return run_sqlite(code)
            
        else:
            return {"output": f"Error: Unsupported language '{language}'", "exit_code": 1}
            
    except subprocess.TimeoutExpired:
        return {"output": "Error: Code took too long to run (Infinite Loop?).", "exit_code": 1}
    except Exception as e:
        return {"output": f"Server Error: {str(e)}", "exit_code": 1}


def run_docker(image: str, command: list, stdin_input: str):
    # Adjust for node stdin
    if "node" in image:
        command = ["node", "-"]
        stdin_input = stdin_input
        
    result = subprocess.run(
        [
            "docker", "run", "--rm", "-i", 
            "--net", "none",
            "--memory", "128m", 
            "--cpus", "0.5", 
            image
        ] + command[1:],
        input=stdin_input,
        capture_output=True,
        text=True,
        timeout=10
    )
    
    output = result.stdout
    error_output = result.stderr
    exit_code = result.returncode
    
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
