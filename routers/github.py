import json
import urllib.request
import urllib.error
import base64
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["GitHub Export"])

class GithubExportRequest(BaseModel):
    token: str
    repo_name: str
    code: str
    language: str

@router.post("/github/export")
def export_to_github(req: GithubExportRequest):
    # 1. Create Repo
    repo_url = "https://api.github.com/user/repos"
    repo_data = json.dumps({
        "name": req.repo_name,
        "description": "Capstone Project exported from Digital Era",
        "private": False,
        "auto_init": False
    }).encode('utf-8')
    
    headers = {
        "Authorization": f"token {req.token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Digital-Era-App"
    }
    
    try:
        request = urllib.request.Request(repo_url, data=repo_data, headers=headers, method="POST")
        with urllib.request.urlopen(request) as response:
            repo_info = json.loads(response.read().decode('utf-8'))
            owner = repo_info["owner"]["login"]
            repo = repo_info["name"]
            html_url = repo_info["html_url"]
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        try:
            err_json = json.loads(err_msg)
            if "errors" in err_json and any(err.get("message") == "name already exists on this account" for err in err_json["errors"]):
                raise HTTPException(status_code=400, detail="Repository name already exists on your GitHub account. Please choose a different name.")
        except:
            pass
        raise HTTPException(status_code=400, detail=f"Failed to create repository. Check your token.")
        
    # 2. Push Code File
    file_ext = "js" if req.language == "javascript" else ("py" if req.language == "python" else "txt")
    filename = f"main.{file_ext}"
    
    code_content_b64 = base64.b64encode(req.code.encode('utf-8')).decode('utf-8')
    
    file_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{filename}"
    file_data = json.dumps({
        "message": "Initial commit from Digital Era",
        "content": code_content_b64
    }).encode('utf-8')
    
    try:
        request2 = urllib.request.Request(file_url, data=file_data, headers=headers, method="PUT")
        urllib.request.urlopen(request2)
    except urllib.error.HTTPError as e:
        raise HTTPException(status_code=400, detail="Failed to upload code file")
        
    # 3. Push README.md
    readme_content = f"""# {req.repo_name}

This project was built and exported from **[Digital Era](https://digital-era.live)**, an interactive learning platform for AI, Data, and Code.

## About
This is a Capstone project demonstrating skills learned in the {req.language.capitalize()} track.
"""
    readme_b64 = base64.b64encode(readme_content.encode('utf-8')).decode('utf-8')
    readme_url = f"https://api.github.com/repos/{owner}/{repo}/contents/README.md"
    readme_data = json.dumps({
        "message": "Add README.md",
        "content": readme_b64
    }).encode('utf-8')
    
    try:
        request3 = urllib.request.Request(readme_url, data=readme_data, headers=headers, method="PUT")
        urllib.request.urlopen(request3)
    except urllib.error.HTTPError:
        pass # Optional, ignore if it fails
        
    return {"url": html_url}
