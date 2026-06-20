from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from database import engine
from models import Base

# Import all routers
import routers.users
import routers.students
import routers.teachers
import routers.courses
import routers.ai_tutor
import routers.execution


# 2. Initialize the web server
app = FastAPI(title="Mabel Academy API", description="Digital Era Backend", version="2.0")

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Include all routers to modularize the application
app.include_router(routers.users.router)
app.include_router(routers.students.router)
app.include_router(routers.teachers.router)
app.include_router(routers.courses.router)
app.include_router(routers.ai_tutor.router)
app.include_router(routers.execution.router)

# 4. Root / Static File Endpoints
# Mount the entire React app build directory
if os.path.isdir("frontend/dist"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/{catchall:path}")
def serve_frontend(catchall: str):
    # Catchall serves the React app, letting React Router handle the URL
    if os.path.exists("frontend/dist/index.html"):
        return FileResponse("frontend/dist/index.html")
    return {"message": "Frontend build not found. Run npm run build."}