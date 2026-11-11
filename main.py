from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.gzip import GZipMiddleware
import os
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base
from sqlalchemy import text
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from limiter import limiter
import models
from routers.users import get_current_user, _is_admin

# 1. Initialize Database & Run Safe Non-Blocking Migrations
def safe_init_db():
    try:
        from sqlalchemy import inspect, text
        # Create missing tables (e.g. course_completions, daily_challenges)
        Base.metadata.create_all(bind=engine)
        
        # Self-heal missing columns on existing tables
        insp = inspect(engine)
        tables = insp.get_table_names()
        if 'users' in tables:
            cols = [c['name'] for c in insp.get_columns('users')]
            with engine.connect() as conn:
                if 'created_at' not in cols:
                    try:
                        conn.execute(text("ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"))
                        conn.commit()
                        print("[Migration] Added created_at to users table.")
                    except Exception as col_err:
                        print(f"[Migration Info] created_at check: {col_err}")
    except Exception as e:
        print(f"[Safe DB Init Info] {e}")

safe_init_db()

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
import routers.support
import routers.github

# AI 2.0 routers (Phase 2+)
import routers.memory
import routers.ai_orchestrator
import routers.tools
import routers.evaluator


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
app.include_router(routers.support.router)
app.include_router(routers.github.router)

# AI 2.0 routers (Phase 2+)
app.include_router(routers.memory.router)
app.include_router(routers.ai_orchestrator.router)
app.include_router(routers.tools.router)
app.include_router(routers.evaluator.router)

@app.get("/api/admin/setup-db-tables")
def setup_db_tables(current_user: models.User = Depends(get_current_user)):
    """Manual trigger to create database tables without causing startup deadlocks."""
    if not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized")
    try:
        Base.metadata.create_all(bind=engine)
        return {"message": "Database tables created successfully!"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/migrate-db")
def migrate_db(key: str = ""):
    """
    Run safe ALTER TABLE migrations to add missing columns.
    Secured by a secret key (no auth needed since auth may be broken).
    Usage: GET /api/migrate-db?key=mabel-digital-era-2026
    """
    if key != "mabel-digital-era-2026":
        raise HTTPException(status_code=403, detail="Invalid key")
    
    results = []
    try:
        Base.metadata.create_all(bind=engine)
        results.append("Base.metadata.create_all executed successfully (all tables ensured)")
    except Exception as e:
        results.append(f"create_all note: {str(e)}")

    with engine.connect() as conn:
        # List of (table, column, sql_type, default) migrations to run
        migrations = [
            ("subscriptions", "access_grants", "TEXT", "'{}'"),
        ]
        for table, column, col_type, default in migrations:
            try:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type} DEFAULT {default}"))
                conn.commit()
                results.append(f"Added {table}.{column}")
            except Exception as e:
                conn.rollback()
                if "already exists" in str(e).lower() or "duplicate column" in str(e).lower():
                    results.append(f"{table}.{column} already exists (OK)")
                else:
                    results.append(f"Error on {table}.{column}: {str(e)}")
    
    return {"message": "Migration complete", "results": results}

@app.get("/api/admin/promote")
def promote_admin(email: str = "", key: str = "", db: Session = Depends(get_db)):
    """
    Promote an account to admin role using the secure admin key.
    Usage: GET /api/admin/promote?email=your_email@gmail.com&key=mabel-digital-era-2026
    """
    if key != "mabel-digital-era-2026":
        raise HTTPException(status_code=403, detail="Invalid key")
    if not email:
        raise HTTPException(status_code=400, detail="Email parameter is required")
        
    user = db.query(models.User).filter(models.User.email.ilike(email.strip())).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User '{email}' not found")
        
    user.role = "admin"
    db.commit()
    return {"message": f"Successfully promoted {user.email} (ID: {user.id}) to admin role!"}

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