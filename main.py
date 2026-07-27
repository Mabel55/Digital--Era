from fastapi import FastAPI
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

# 1. Initialize Database & Run Migrations
try:
    Base.metadata.create_all(bind=engine)
    print("Database tables created/verified successfully.")
except Exception as e:
    print(f"WARNING: Could not connect to database on startup: {e}")
    print("Server will start anyway. Database-dependent routes will fail until DB is available.")

# Auto-migrate db safely, one column at a time so a single failure doesn't roll back the others
migrations = [
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS xp INTEGER DEFAULT 0",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS level VARCHAR DEFAULT 'Beginner'",
    # Fix: If level was accidentally created as INTEGER, we must drop the old default first
    "ALTER TABLE users ALTER COLUMN level DROP DEFAULT",
    "ALTER TABLE users ALTER COLUMN level TYPE VARCHAR USING level::varchar",
    "ALTER TABLE users ALTER COLUMN level SET DEFAULT 'Beginner'",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS streak INTEGER DEFAULT 0",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS last_login TIMESTAMP",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS progress JSON",
    # New profile fields for international competitiveness
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS longest_streak INTEGER DEFAULT 0",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT NOW()",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS avatar_url VARCHAR",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS bio TEXT",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS github_url VARCHAR",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS linkedin_url VARCHAR",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS country VARCHAR",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS preferred_language VARCHAR DEFAULT 'en'",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS goal VARCHAR",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS weekly_goal_days INTEGER DEFAULT 5",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS last_active_course VARCHAR",
    "ALTER TABLE users ADD COLUMN IF NOT EXISTS last_active_lesson_idx INTEGER DEFAULT 0",
    # Course enhancements
    "ALTER TABLE courses ADD COLUMN IF NOT EXISTS estimated_hours FLOAT DEFAULT 2.0",
    "ALTER TABLE lessons ADD COLUMN IF NOT EXISTS order_index INTEGER DEFAULT 0",
]

try:
    for migration in migrations:
        try:
            with engine.begin() as conn:
                conn.execute(text(migration))
            print(f"Migration OK: {migration[:60]}")
        except Exception as e:
            print(f"Migration SKIPPED: {migration[:60]} -> {e}")
except Exception as e:
    print(f"WARNING: Could not run migrations (DB may be unavailable): {e}")

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
app.include_router(routers.daily_challenge.router)

# 4. Root / Static File Endpoints
# Mount the entire React app build directory
if os.path.isdir("frontend/dist"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/{catchall:path}")
def serve_frontend(catchall: str):
    # Serve root-level static files (like sitemap.xml, favicon.svg, robots.txt)
    # instead of serving the React app for them.
    valid_extensions = (".xml", ".svg", ".png", ".ico", ".txt", ".webmanifest", ".js")
    if catchall and any(catchall.endswith(ext) for ext in valid_extensions):
        file_path = os.path.join("frontend/dist", catchall)
        # Prevent path traversal vulnerabilities
        if ".." not in catchall and os.path.isfile(file_path):
            return FileResponse(file_path)

    # Catchall serves the React app, letting React Router handle the URL
    if os.path.exists("frontend/dist/index.html"):
        return FileResponse("frontend/dist/index.html")
    return {"message": "Frontend build not found. Run npm run build."}