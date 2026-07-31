from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.gzip import GZipMiddleware
import os
from database import engine
from models import Base
from sqlalchemy import text
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from limiter import limiter
import models
from routers.users import get_current_user, _is_admin

# 1. Initialize Database & Run Migrations
# Removed Base.metadata.create_all(bind=engine) from startup to prevent Azure deadlocks/timeouts.
# We now use the /api/admin/setup-db-tables endpoint below to safely run migrations.
try:
    print("Skipping auto DB setup to prevent deadlocks.")
except Exception as e:
    print(f"WARNING: Exception: {e}")

# Auto-migrate db safely, one column at a time so a single failure doesn't roll back the others
# MIGRATIONS REMOVED: Running ALTER TABLE on every startup can cause database deadlocks
# if the container restarts abruptly. All schema updates should be handled offline.

# Import all routers
import routers.users
import routers.students
import routers.teachers
import routers.courses
import routers.ai_tutor
import routers.execution
import routers.assessments
import routers.forum
import routers.payments
import routers.daily_challenge
import routers.translation


# 2. Initialize the web server
app = FastAPI(title="Digital Era API", description="International E-Learning Platform Backend", version="3.0")

# GZIP compression for faster responses
app.add_middleware(GZipMiddleware, minimum_size=500)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://digital-era.live",
        "https://www.digital-era.live",
        "http://localhost:5173",   # Vite dev server
        "http://127.0.0.1:5173",
    ],
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
app.include_router(routers.assessments.router)
app.include_router(routers.forum.router)
app.include_router(routers.payments.router)
app.include_router(routers.translation.router)

@app.get("/api/admin/setup-db-tables")
def setup_db_tables(current_user: models.User = Depends(get_current_user)):
    """Manual trigger to create database tables without causing startup deadlocks."""
    if not _is_admin(current_user):
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Not authorized")
    try:
        Base.metadata.create_all(bind=engine)
        return {"message": "Database tables created successfully!"}
    except Exception as e:
        return {"error": str(e)}

# 4. Root / Static File Endpoints
# Mount the entire React app build directory
if os.path.isdir("frontend/dist"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/{catchall:path}")
def serve_frontend(catchall: str):
    # Serve root-level static files (like sitemap.xml, favicon.svg, robots.txt)
    # instead of serving the React app for them.
    valid_extensions = (".xml", ".svg", ".png", ".ico", ".txt", ".webmanifest", ".js", ".json")
    if catchall and any(catchall.endswith(ext) for ext in valid_extensions):
        file_path = os.path.join("frontend/dist", catchall)
        # Prevent path traversal vulnerabilities
        if ".." not in catchall and os.path.isfile(file_path):
            return FileResponse(file_path)

    # Catchall serves the React app, letting React Router handle the URL
    if os.path.exists("frontend/dist/index.html"):
        return FileResponse("frontend/dist/index.html")
    return {"message": "Frontend build not found. Run npm run build."}