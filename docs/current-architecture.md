# Digital Era — Current Architecture Report

> **Generated**: 2026-09-29
> **Purpose**: Document the existing system before making any architectural changes.
> **Status**: Phase 0 — Inspect Before Changing

---

## 1. High-Level Architecture Overview

Digital Era is a full-stack AI-powered learning platform.

```
+-------------------------------------------------------------+
|                     React / Vite Frontend                    |
|  (SPA, PWA, Lazy-loaded routes, Monaco Editor, i18n)         |
+----------------------------+--------------------------------+
                             | HTTP / JSON
+----------------------------v--------------------------------+
|                     FastAPI Backend (main.py)                |
|  14 router modules, CORS, GZip, Rate Limiting               |
+--------------+--------------+---------------+---------------+
|  PostgreSQL  |  FAISS       |  Gemini       |  Docker       |
|  (SQLAlchemy)|  Vector DB   |  (LangChain)  |  Sandbox      |
+--------------+--------------+---------------+---------------+
```

**Deployment**: Docker multi-stage build -> Azure App Service
**Domain**: `digital-era.live`

---

## 2. Frontend Architecture

### 2.1 Technology Stack
| Component | Technology | Version |
|-----------|-----------|---------|
| Framework | React | 19.2.6 |
| Build Tool | Vite | 8.0.12 |
| Routing | react-router-dom | 7.18.0 |
| State | React Context + React Query | 5.101.4 |
| Code Editor | Monaco Editor (@monaco-editor/react) | 4.7.0 |
| Markdown | react-markdown + marked + DOMPurify | Latest |
| Charts | Recharts | 3.10.0 |
| Animations | framer-motion | 12.42.0 |
| Icons | lucide-react | 1.21.0 |
| i18n | i18next + react-i18next | 26.3.3 |
| PWA | vite-plugin-pwa (Workbox) | 1.3.0 |
| SEO | react-helmet-async | 3.0.0 |

### 2.2 File Structure
```
frontend/src/
├── App.jsx                    # Root component with routing
├── AuthContext.jsx             # Auth provider (token, user, login/signup/logout)
├── DataSaverContext.jsx        # Data saver mode toggle
├── ErrorBoundary.jsx           # Global error boundary
├── i18n.js                     # Internationalization (9 languages)
├── index.css                   # ~39KB global styles
├── main.jsx                    # React DOM entry
├── components/
│   ├── Assessment.jsx          # AI-generated quizzes
│   ├── CareerTracks.jsx        # Learning track browser
│   ├── CertificateModal.jsx    # Certificate display
│   ├── CourseCatalog.jsx       # Public course catalog
│   ├── CustomerSupportChat.jsx # Support chatbot widget
│   ├── DBWorkspace.jsx         # Database course workspace
│   ├── DailyChallenge.jsx      # Daily coding challenge
│   ├── Dashboard.jsx           # Main user dashboard (~38KB)
│   ├── DataSaverToggle.jsx     # Data saver UI toggle
│   ├── DownloadManager.jsx     # Offline course downloads
│   ├── Forum.jsx               # Community discussions
│   ├── GitHubExportModal.jsx   # Export code to GitHub
│   ├── LandingPage.jsx         # Public landing page (~38KB)
│   ├── Leaderboard.jsx         # XP leaderboard
│   ├── LessonDiscussion.jsx    # Per-lesson forum threads
│   ├── NotFound.jsx            # 404 page
│   ├── NotificationCenter.jsx  # In-app notifications
│   ├── OfflineBanner.jsx       # Offline status indicator
│   ├── Onboarding.jsx          # Signup/login with onboarding flow
│   ├── PWAInstallPrompt.jsx    # PWA install prompt
│   ├── PricingPage.jsx         # Subscription pricing (~28KB)
│   ├── Profile.jsx             # User profile + settings
│   ├── ProjectWorkspace.jsx    # Capstone project workspace
│   ├── PublicNavbar.jsx        # Public navigation bar
│   ├── ResetPassword.jsx       # Password reset flow
│   ├── Sandbox.jsx             # Free-form code playground
│   ├── TeacherDashboard.jsx    # Admin/teacher panel
│   ├── Workspace.jsx           # Main lesson workspace (~34KB)
│   ├── dashboard/CourseCard.jsx
│   └── workspace/
│       ├── AIChatSidebar.jsx   # AI tutor sidebar
│       ├── CodeEditorArea.jsx  # Monaco code editor wrapper
│       └── LessonViewer.jsx    # Markdown lesson renderer
├── data/
│   ├── courses.js              # Static curriculum (~2.2MB)
│   └── projects.js             # Capstone project definitions
├── hooks/
│   ├── useCurriculum.js        # React Query for curriculum.json
│   └── useOfflineSync.js       # Offline progress sync
├── lib/
│   └── offlineDB.js            # IndexedDB wrapper
└── utils/
    └── access.js               # Access control (free vs pro)
```

### 2.3 Routing (18 routes)
- 8 public routes (landing, catalog, community, pricing, onboarding, etc.)
- 10 protected routes (dashboard, workspace, profile, sandbox, etc.)
- All routes lazy-loaded with `React.lazy()` for code splitting

### 2.4 Key Frontend Features
- **Code Splitting**: All routes lazy-loaded
- **PWA**: Full offline support with Workbox (Pyodide, Monaco, curriculum cached)
- **Offline-First**: IndexedDB stores progress queue, saved code, curriculum cache
- **Data Saver Mode**: Reduces bandwidth for users on expensive mobile data
- **Internationalization**: 9 languages (en, es, fr, ig, yo, ha, sw, ar, pcm)
- **Access Control**: Client-side `hasAccess()` checks course level vs subscription

---

## 3. Backend Architecture

### 3.1 Technology Stack
| Component | Technology |
|-----------|-----------|
| Framework | FastAPI 0.136.1 |
| ORM | SQLAlchemy (declarative_base) |
| Migration | Alembic 1.18.4 |
| Auth | JWT (python-jose) + bcrypt |
| AI Model | Gemini 2.5 Flash via LangChain |
| Embeddings | Google Gemini Embedding 001 |
| Vector Store | FAISS (faiss-cpu 1.13.2) |
| Rate Limiting | slowapi |
| Payments | Paystack API (httpx) |
| Email | smtplib (Gmail SMTP) |
| Code Execution | Docker containers (Python 3.9, Node 18) |

### 3.2 API Routers (14 modules)
| Router | Prefix | Description |
|--------|--------|-------------|
| `users.py` | `/users` | Auth, profiles, progress, goals, notifications, reviews, search, admin (791 lines) |
| `students.py` | `/students` | Basic student CRUD (legacy) |
| `teachers.py` | `/teachers` | Basic teacher CRUD (legacy) |
| `courses.py` | — | Course/lesson CRUD, code submission grading |
| `ai_tutor.py` | — | Chat, ask-ai, code review, AI usage |
| `execution.py` | — | Docker-sandboxed code execution |
| `assessments.py` | `/assessments` | AI-generated assessments |
| `forum.py` | `/forum` | Forum threads and comments |
| `payments.py` | `/payments` | Paystack checkout, webhook, subscriptions |
| `daily_challenge.py` | `/daily-challenge` | AI-generated daily challenges |
| `translation.py` | `/translate` | AI-powered lesson translation |
| `support.py` | `/api/support` | Customer support chatbot |
| `github.py` | — | Export code to GitHub |

### 3.3 AI Brain (`ai_brain.py`)
1. **`ask_gemini()`** — LLM inference with system prompts, context, chat history, semantic caching
2. **`build_ai_brain()`** — Builds FAISS index from PostgreSQL lessons (incremental sync)
3. **`query_ai_brain()`** — RAG: vector search -> context -> Gemini answer
4. **`add_pdf_to_vector_db()`** — PDF ingestion into FAISS
5. **`build_support_brain()` / `query_support_brain()`** — Separate support RAG

### 3.4 Security Features
- JWT auth with 7-day token expiry
- bcrypt password hashing
- CORS restricted to production + localhost
- Rate limiting on code execution (20/min)
- AI usage limits (3/day free, 30/day pro)
- Docker sandbox: `--net none`, `--memory 128m`, `--cpus 0.5`, 10s timeout
- Paystack webhook signature verification
- Admin role checks on destructive endpoints

---

## 4. Database and Models (19 tables)

### 4.1 Configuration
- **Production**: PostgreSQL via `DATABASE_URL` with TCP keepalives
- **Development**: SQLite (`sql_app.db`)
- **Docker Compose**: pgvector image
- **Migrations**: Alembic (manual trigger only)

### 4.2 Models
| Model | Purpose |
|-------|---------|
| `User` | Primary user: auth, XP, streaks, progress (JSON), profile |
| `Course` | Course metadata (name, level, track, hours) |
| `Lesson` | Lesson content (markdown), expected output, ordering |
| `ChatMessage` | AI tutor conversation history per user |
| `Subscription` | Plan, status, Paystack codes, access_grants (JSON) |
| `Certificate` | Verification codes for completed courses |
| `AIUsage` | Daily AI message count per user |
| `UserActivity` | Daily XP/lessons/challenges/time tracking |
| `CourseCompletion` | Course completion records |
| `DailyChallenge` | AI-generated daily challenges |
| `DailyChallengeSubmission` | Challenge submissions |
| `Notification` | In-app notifications |
| `CourseReview` | Course ratings/reviews |
| `LearningGoal` | Weekly learning goals |
| `AssessmentResult` | Quiz/assessment history |
| `ForumThread` / `ForumComment` | Discussion forum |
| `PasswordResetToken` | Token-based password reset |
| `LessonTranslationCache` | Cached AI translations |
| `AITutorCache` | Cached AI tutor responses |
| `Student` / `Teacher` | Legacy entity models (not actively used) |

---

## 5. Course and Curriculum System

### 5.1 Dual Content Architecture
1. **Static Curriculum** (`public/curriculum.json` — 2.2MB): ~20 tracks, ~200+ courses, ~1500+ lessons. Loaded client-side, cached offline.
2. **Dynamic DB Lessons** (`courses` + `lessons` tables): PostgreSQL-backed, created via API/admin.

### 5.2 Curriculum Scope (from `curriculum/index.json`)
20 tracks: Python Core, Frontend, Backend, SQL & Databases, Data Science, AI Engineering, AI Automation, Version Control, Mobile Development, Systems Programming, Cloud Native & Go, Cloud & DevOps, System Design & Architecture, Agentic AI & MCP, Computer Vision & Deep Learning, Data Engineering & MLOps, C Programming, Data Structures & Algorithms, UI/UX Design, Tech Entrepreneurship, Generative AI (Theory)

### 5.3 Content Pipeline
- 64+ batch scripts for content generation (in root directory)
- Basic audit scripts for content validation
- No automated quality checks on content accuracy

---

## 6. Gamification and Engagement

| Feature | Implementation |
|---------|---------------|
| XP System | 10 XP/lesson, variable for challenges/assessments |
| Level System | Beginner -> Intermediate -> Advanced -> Master -> Expert -> Grandmaster |
| Streaks | Login-based, milestone notifications |
| Leaderboard | XP-ranked, filterable by time period |
| Certificates | Unique verification codes on completion |
| Notifications | Streaks, XP milestones, referrals, achievements |
| Daily Challenges | AI-generated coding challenges |
| Learning Goals | Weekly targets (days + XP) |
| Course Reviews | 1-5 star ratings |

---

## 7. Monetization

| Tier | Price | Features |
|------|-------|----------|
| Free | $0 | Beginner courses, 3 AI messages/day |
| Pro Monthly | N10,000/mo | All courses, unlimited AI, certificates |
| Pro Yearly | N100,000/yr | All Pro + exclusive webinars |
| Free Trial | 7 days | Full Pro access |
| Referral | 30 days free | Both referrer and referee |

Payment processor: Paystack (Nigerian payments)

---

## 8. What Is Working Well

1. Rich feature set with impressive breadth
2. PWA with offline-first design for bandwidth-constrained users
3. Data saver mode awareness of target audience
4. Docker-sandboxed code execution with proper isolation
5. Semantic caching to reduce AI API costs
6. Incremental FAISS sync
7. Paystack integration appropriate for Nigerian market
8. Multi-language support including Nigerian languages
9. Gamification for engagement (XP, streaks, levels)
10. Referral system for growth

---

## 9. What Should Be Preserved

1. FastAPI + React/Vite technology stack
2. PostgreSQL as primary database
3. Docker-sandboxed code execution
4. PWA with offline-first capabilities
5. Paystack payment integration
6. i18n infrastructure
7. Data saver mode concept
8. Gamification system
9. FAISS/vector store concept (can migrate to pgvector)
10. Curriculum JSON delivery for offline support

---

## 10. Technical Debt

### Critical
1. **Secrets in `.env` committed to repo** — API keys, SMTP passwords in plaintext
2. **Migration endpoint with hardcoded key** — Security vulnerability
3. **No proper test suite** — Only ad-hoc test scripts
4. **64+ batch scripts** polluting root directory

### High
5. **Dual content system** — Static JSON and PostgreSQL lessons create confusion
6. **Progress stored as JSON column** — Not normalized, hard to query
7. **`users.py` is 791 lines** — Multiple concerns in one file
8. **`datetime.utcnow()` deprecated** in Python 3.12+
9. **No structured logging** — Only `print()` statements
10. **requirements.txt contains unused Django dependencies**

### Medium
11. `courses.js` duplicates `curriculum.json`
12. Legacy `Student`/`Teacher` models not used
13. Course reviews linked by string name
14. No API versioning or pagination
15. AI video generator mixed into main repo

---

## 11. Security Risks

| Risk | Severity |
|------|----------|
| Secrets in source control | CRITICAL |
| Hardcoded migration key | CRITICAL |
| Chat history unbounded (cost/memory) | MEDIUM |
| Admin check inconsistency across files | MEDIUM |
| No audit logging for admin actions | MEDIUM |
| Rate limiting only on code execution | LOW |

---

## 12. Architectural Weaknesses

1. No service layer — business logic in route handlers
2. Monolithic AI module (ai_brain.py does everything)
3. No task queue for long-running operations
4. No caching layer (Redis/memcached)
5. No WebSocket support for streaming AI responses
6. FAISS stored as files on disk (not scalable for multi-instance)
7. No background job scheduler

---

## 13. Reusable Components

### Backend
- `auth.py` — JWT + bcrypt auth system
- `database.py` — SQLAlchemy session management
- `models.py` — Complete data model definitions
- `schemas.py` — Pydantic validation schemas
- `ai_brain.py` — FAISS builder + Gemini integration (needs refactoring)

### Frontend
- `AuthContext.jsx` — Auth state management
- `DataSaverContext.jsx` — Bandwidth awareness
- `offlineDB.js` — IndexedDB abstraction
- `useCurriculum.js` — Curriculum fetching with offline fallback
- `access.js` — Course access control
- All workspace components (CodeEditorArea, LessonViewer, AIChatSidebar)

---

## 14. Components That Should Eventually Be Replaced

| Component | Reason | Replacement |
|-----------|--------|-------------|
| FAISS file-based vector store | Not multi-instance scalable | pgvector (already in docker-compose) |
| JSON progress column on User | Not queryable | Normalized progress tables |
| Hardcoded system prompts | Not configurable | Prompt management system |
| `print()` logging | Not structured | Python logging + structured formatter |
| Ad-hoc migration endpoint | Security risk | Proper Alembic-only migrations |
| Single-file AI brain | Not modular | Separate services |
| Unbounded chat history in LLM | Memory/cost | Sliding window + summarization |
