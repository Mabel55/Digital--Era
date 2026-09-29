# Digital Era AI 2.0 — Proposed Architecture

> **Generated**: 2026-09-29
> **Status**: AWAITING APPROVAL — Do not implement until explicitly approved
> **Prerequisite**: Read `docs/current-architecture.md` first

---

## 1. Design Principles

1. **Preserve working features** — Do not rewrite what already works
2. **Incremental evolution** — Each phase leaves the application in a working state
3. **Measurable improvement** — Every capability must be testable and evaluable
4. **Modular services** — Components can be improved independently
5. **Simple architecture** — Prefer simplicity that can evolve over premature abstraction
6. **Secure defaults** — Defense in depth from the start
7. **Data-informed decisions** — Use actual learning data to drive improvements

---

## 2. Proposed System Architecture

```
+---------------------------------------------------------------+
|                    React / Vite Frontend                        |
|  (Existing: preserved, enhanced incrementally)                  |
+----------------------------+----------------------------------+
                             | HTTP / JSON / WebSocket
+----------------------------v----------------------------------+
|                     FastAPI API Layer                           |
|  (Existing routers preserved, new routers added modularly)     |
+---+--------+--------+--------+--------+--------+--------+----+
    |        |        |        |        |        |        |
    v        v        v        v        v        v        v
+------+ +------+ +------+ +------+ +------+ +------+ +------+
| Auth | | AI   | |Memory| | RAG  | | Tool | | Eval | |Course|
|  &   | |Orch- | |System| |Engine| | Reg- | |uation| |Intel-|
| RBAC | |estr- | |      | |      | |istry | |      | |igence|
|      | |ator  | |      | |      | |      | |      | |Engine|
+--+---+ +--+---+ +--+---+ +--+---+ +--+---+ +--+---+ +--+---+
   |        |        |        |        |        |        |
   +--------+--------+--------+--------+--------+--------+
                             |
            +----------------+----------------+
            |                                 |
    +-------v-------+              +----------v----------+
    |  PostgreSQL    |              |  pgvector            |
    | (Structured)   |              | (Vector retrieval)   |
    +----------------+              +----------------------+
```

---

## 3. Component Architecture

### 3.1 API Layer (Enhanced existing FastAPI)

**What changes**: Add new routers alongside existing ones. Do not remove working endpoints.

New routers to add:
- `routers/ai_orchestrator.py` — Intelligent request routing
- `routers/memory.py` — Memory CRUD and retrieval
- `routers/content_intelligence.py` — Course content engine API
- `routers/evaluator.py` — AI evaluation endpoints
- `routers/research.py` — Experiment framework API
- `routers/tools.py` — Tool registry and execution

**Refactoring** (not rewriting):
- Extract service layer from `users.py` (split into `services/user_service.py`, `services/progress_service.py`, `services/notification_service.py`)
- Extract `services/ai_service.py` from `ai_brain.py`
- Consolidate `_is_admin()` into a single `services/auth_service.py`

### 3.2 AI Orchestrator

```
User Request
  |
  v
[Understand Task] -- What type of request is this?
  |                  (question, code help, assessment, content request)
  v
[Retrieve Memory] -- What do we know about this student?
  |                  (skills, weaknesses, history, current lesson)
  v
[Retrieve Knowledge] -- What relevant content do we have?
  |                     (course materials, documentation)
  v
[Plan] -- Does this need multi-step reasoning?
  |       (simple answer vs. complex problem-solving)
  v
[Select Tools] -- Do we need to execute code? Search? Generate?
  |
  v
[Execute] -- Generate response with appropriate context
  |
  v
[Verify] -- Is this response correct and helpful?
  |          (evaluator checks quality)
  v
[Learn] -- Store useful information from this interaction
  |         (update student model, log metrics)
  v
[Respond] -- Deliver final response to student
```

**Implementation**: Python service class, not a framework. The orchestrator is a configurable pipeline, not an opaque black box.

```python
# services/ai_orchestrator.py
class AIOrchestrator:
    def __init__(self, memory: MemoryService, rag: RAGService,
                 planner: PlannerService, tools: ToolRegistry,
                 evaluator: EvaluatorService):
        self.memory = memory
        self.rag = rag
        self.planner = planner
        self.tools = tools
        self.evaluator = evaluator

    async def process(self, request: StudentRequest) -> OrchestratorResponse:
        # 1. Understand
        task = self.classify_task(request)
        # 2. Retrieve memory
        student_context = await self.memory.get_student_context(request.user_id)
        # 3. Retrieve knowledge
        knowledge = await self.rag.retrieve(request.message, request.course_context)
        # 4. Plan
        plan = await self.planner.plan(task, student_context, knowledge)
        # 5. Execute tools if needed
        tool_results = await self.tools.execute_plan(plan)
        # 6. Generate response
        response = await self.generate(task, student_context, knowledge, tool_results)
        # 7. Verify
        evaluation = await self.evaluator.check(response, task)
        # 8. Learn
        await self.memory.record_interaction(request, response, evaluation)
        return response
```

### 3.3 Memory System

```
+-------------------+  +-------------------+  +-------------------+
| Short-term Memory |  | Episodic Memory   |  | Semantic Memory   |
| (Current session) |  | (Past events)     |  | (Stable facts)    |
| - Conversation    |  | - "Student failed |  | - "Knows Python   |
|   context         |  |   loops 3 times"  |  |   basics"         |
| - Current lesson  |  | - "Asked about    |  | - "Goal: become   |
| - Recent errors   |  |   recursion"      |  |   data scientist"  |
+-------------------+  +-------------------+  +-------------------+
         |                      |                      |
         +----------------------+----------------------+
                                |
                    +-----------v-----------+
                    |    Student Model      |
                    | - Skills inventory    |
                    | - Strengths/weaknesses|
                    | - Learning history    |
                    | - Difficulty level    |
                    | - Topics for revision |
                    +-----------------------+
```

#### Database Schema (New tables, additive to existing)

```sql
-- Episodic Memory: Important past interactions
CREATE TABLE episodic_memories (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    memory_type VARCHAR(50) NOT NULL,  -- 'struggle', 'breakthrough', 'misconception', 'preference'
    topic VARCHAR(255),
    summary TEXT NOT NULL,
    importance FLOAT DEFAULT 0.5,      -- 0.0 to 1.0, for retrieval ranking
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    last_accessed TIMESTAMP DEFAULT NOW()
);

-- Semantic Memory: Stable facts about the learner
CREATE TABLE semantic_memories (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    fact_type VARCHAR(50) NOT NULL,    -- 'skill', 'strength', 'weakness', 'goal', 'preference'
    key VARCHAR(255) NOT NULL,
    value TEXT NOT NULL,
    confidence FLOAT DEFAULT 0.5,
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, fact_type, key)
);

-- Student Skill Model
CREATE TABLE student_skills (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    skill_name VARCHAR(255) NOT NULL,
    proficiency FLOAT DEFAULT 0.0,     -- 0.0 to 1.0
    assessment_count INTEGER DEFAULT 0,
    last_assessed TIMESTAMP,
    needs_revision BOOLEAN DEFAULT FALSE,
    UNIQUE(user_id, skill_name)
);

-- Procedural Memory: Useful procedures the AI has used successfully
CREATE TABLE procedural_memories (
    id SERIAL PRIMARY KEY,
    procedure_type VARCHAR(100) NOT NULL,  -- 'explanation_strategy', 'debugging_approach'
    topic VARCHAR(255),
    procedure TEXT NOT NULL,
    success_count INTEGER DEFAULT 0,
    failure_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
```

**What stays in PostgreSQL**: All structured data above.
**What uses vector retrieval (pgvector)**: Course content embeddings, episodic memory search when exact match isn't sufficient.

### 3.4 Improved RAG Pipeline

```
User Question
  |
  v
[Query Understanding]     -- Rephrase, extract intent, identify topic
  |
  v
[Memory Retrieval]        -- Check student model for relevant context
  |
  v
[Course/Document Search]  -- pgvector similarity search (replaces FAISS)
  |
  v
[Reranking]               -- Score and filter results by relevance
  |
  v
[Context Construction]    -- Build optimized prompt with selected chunks
  |
  v
[AI Response]             -- Generate answer
  |
  v
[Evaluation]              -- Check quality, relevance, accuracy
```

**Migration from FAISS to pgvector**:
- pgvector is already in the docker-compose file
- Eliminates file-based index problem for multi-instance deployment
- SQL-native filtering (by course_id, topic, difficulty) alongside vector search
- Transactions and ACID guarantees

```sql
-- Course content embeddings (replaces FAISS index)
CREATE TABLE content_embeddings (
    id SERIAL PRIMARY KEY,
    source_type VARCHAR(50) NOT NULL,  -- 'lesson', 'documentation', 'support'
    source_id INTEGER,                 -- lesson_id if source_type='lesson'
    chunk_index INTEGER DEFAULT 0,
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}',
    embedding VECTOR(768),             -- Gemini embedding dimension
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX ON content_embeddings USING ivfflat (embedding vector_cosine_ops);
```

### 3.5 Tool Registry

```python
# services/tool_registry.py
class ToolRegistry:
    """Controlled registry of tools the AI can use."""

    tools = {
        "calculator": CalculatorTool(),
        "python_executor": PythonExecutorTool(sandboxed=True),
        "code_analyzer": CodeAnalyzerTool(),
        "course_search": CourseSearchTool(),
        "memory_search": MemorySearchTool(),
        "quiz_generator": QuizGeneratorTool(),
        "content_analyzer": ContentAnalyzerTool(),
    }

    # Permission matrix
    permissions = {
        "calculator": {"requires_auth": False, "max_per_minute": 60},
        "python_executor": {"requires_auth": True, "max_per_minute": 20},
        "code_analyzer": {"requires_auth": True, "max_per_minute": 30},
        "course_search": {"requires_auth": False, "max_per_minute": 60},
        "memory_search": {"requires_auth": True, "max_per_minute": 30},
        "quiz_generator": {"requires_auth": True, "max_per_minute": 10},
        "content_analyzer": {"requires_auth": True, "max_per_minute": 10, "requires_admin": True},
    }
```

**Security invariants**:
- No tool can access production databases directly
- No tool can access server shell
- No tool can access secrets or credentials
- Code execution always sandboxed via existing Docker infrastructure
- All tool invocations logged with user_id and timestamp

### 3.6 Reasoning and Planning

```python
# services/planner.py
class PlannerService:
    """Generates structured plans for complex tasks."""

    async def plan(self, task: Task, context: StudentContext,
                   knowledge: list[RetrievedChunk]) -> Plan:
        """
        For simple questions: returns a single-step plan.
        For complex tasks: decomposes into steps.
        """
        # Metadata stored, not exposed to user
        return Plan(
            task=task.description,
            steps=[PlanStep(action="...", tool="...", params={})],
            reasoning_metadata={
                "task_complexity": "simple|moderate|complex",
                "plan_steps": [...],
                "tools_selected": [...],
                "confidence": 0.85,
            }
        )
```

**Chain-of-thought**: Internal only. Users see the final answer, not the reasoning steps. Structured metadata is stored for evaluation and debugging.

### 3.7 Evaluation System

```python
# services/evaluator.py
class EvaluatorService:
    """Evaluates AI outputs independently from the generator."""

    async def check(self, response: AIResponse, task: Task) -> Evaluation:
        return Evaluation(
            correctness=self.check_correctness(response, task),
            relevance=self.check_relevance(response, task),
            code_validity=self.check_code(response) if response.has_code else None,
            hallucination_risk=self.check_hallucination(response),
            safety=self.check_safety(response),
            verdict="pass" | "revise" | "fail",
        )
```

**Metrics tracked**:
| Metric | How Measured |
|--------|-------------|
| Correctness | Independent evaluator LLM check |
| Code correctness | Sandbox execution + test cases |
| Relevance | Evaluator scoring against task |
| Hallucination rate | Fact-checking against course material |
| Task completion | Did the student's problem get solved? |
| Student improvement | Assessment score changes over time |
| Lesson quality | Student pass rates, time-on-task |
| Latency | Response time tracking |
| Token efficiency | Token count per response |

### 3.8 Student / Learning Model

```python
# services/student_model.py
class StudentModelService:
    """Tracks and adapts to individual student capabilities."""

    async def get_profile(self, user_id: int) -> StudentProfile:
        """Aggregates all knowledge about a student."""
        return StudentProfile(
            skills=await self.get_skills(user_id),
            strengths=await self.get_strengths(user_id),
            weaknesses=await self.get_weaknesses(user_id),
            goals=await self.get_goals(user_id),
            learning_history=await self.get_history(user_id),
            difficulty_level=await self.calculate_difficulty(user_id),
            topics_needing_revision=await self.get_revision_topics(user_id),
        )

    async def update_after_interaction(self, user_id: int,
                                        interaction: Interaction):
        """Update student model based on new interaction data."""
        # E.g., student struggled with loops -> update skill, flag for revision
```

### 3.9 Course Content Intelligence Engine

This is a **backend service** + **admin interface**, NOT an auto-publisher.

```
+--------------------------------------------------+
|         Course Content Intelligence Engine        |
+--------------------------------------------------+
|                                                    |
|  Curriculum Auditor                                |
|  - Prerequisite detection                          |
|  - Difficulty progression analysis                 |
|  - Duplicate content detection                     |
|  - Gap detection                                   |
|  - Outdated content flagging                       |
|                                                    |
|  Lesson Analyzer                                   |
|  - Quality scoring (internal QA)                   |
|  - Accuracy checking (code validation)             |
|  - Learning objective validation                   |
|  - Concept sequencing analysis                     |
|                                                    |
|  Content Generator (DRAFT ONLY)                    |
|  - Lesson drafts following standard structure      |
|  - Quiz generation                                 |
|  - Exercise generation                             |
|  - Code example generation + validation            |
|                                                    |
|  Student Feedback Analyzer                         |
|  - Failure rate analysis per lesson                |
|  - Common misconception detection                  |
|  - Exercise difficulty calibration                 |
|                                                    |
|  HUMAN REVIEW GATE                                 |
|  - All AI-generated content requires approval      |
|  - Admin dashboard for review queue                |
|  - Version tracking for content changes            |
|                                                    |
+--------------------------------------------------+
```

**Standard Lesson Structure** (used as a template, not forced):
1. What You Will Learn
2. Learning Objectives
3. Prerequisites
4. Introduction
5. Simple Explanation
6. Detailed Concept Explanation
7. Why It Matters
8. Syntax/Rules/Principles
9. Worked Examples
10. Real-world Examples
11. Guided Practice
12. Independent Practice
13. Common Mistakes
14. Troubleshooting
15. Mini Quiz
16. Practical Task/Project
17. Lesson Summary
18. Further Practice
19. Assessment

### 3.10 Adaptive Learning

```
Student opens lesson on "Python Loops"
  |
  v
[Check Student Model] --> Student has failed loops quiz twice
  |
  v
[Detect Weakness] --> Missing prerequisite: "Variables & Data Types"
  |
  v
[Adapt] --> Suggest prerequisite lesson first
         --> Provide simpler explanation with more examples
         --> Give targeted practice exercises
  |
  v
[Reassess] --> After practice, re-quiz on loops
  |
  v
[Progress] --> Demonstrated understanding -> increase difficulty
```

### 3.11 Research / Experiment Framework

```python
# services/research.py
class ExperimentService:
    """Framework for testing AI capabilities."""

    async def run_experiment(self, config: ExperimentConfig) -> ExperimentResult:
        return ExperimentResult(
            hypothesis=config.hypothesis,
            model=config.model_version,
            prompt_version=config.prompt_version,
            dataset=config.dataset,
            metrics=await self.evaluate(config),
            conclusion=None,  # Human fills this in
        )
```

Stored in `docs/research/` and in a `experiments` database table.

---

## 4. Proposed Database Changes (Additive)

### New Tables
| Table | Purpose | Phase |
|-------|---------|-------|
| `episodic_memories` | Important past interactions | 2 |
| `semantic_memories` | Stable facts about learners | 2 |
| `student_skills` | Skill proficiency tracking | 2 |
| `procedural_memories` | Successful teaching procedures | 2 |
| `content_embeddings` | pgvector course content (replaces FAISS) | 3 |
| `tool_invocations` | Audit log of tool usage | 5 |
| `ai_evaluations` | AI response evaluations | 7 |
| `experiments` | Research experiment records | 10 |
| `experiment_results` | Experiment metrics | 10 |
| `content_drafts` | AI-generated content awaiting review | 9 |
| `content_reviews` | Human review decisions | 9 |
| `content_versions` | Content change history | 9 |
| `student_lesson_analytics` | Per-lesson student performance | 8 |

### Existing Table Modifications
| Table | Change | Phase |
|-------|--------|-------|
| `users` | Add `difficulty_level VARCHAR(20)` | 2 |
| `lessons` | Add `quality_score FLOAT`, `last_audited TIMESTAMP` | 9 |
| `lessons` | Add `version INTEGER DEFAULT 1` | 9 |

### Tables NOT Changed
All existing tables remain as-is. New functionality is additive.

---

## 5. Proposed API Changes

### New Endpoints (Additive)

**Phase 2 — Memory**
```
POST   /api/v2/memory/episodic          # Record episodic memory
GET    /api/v2/memory/student/{id}      # Get student context
PUT    /api/v2/memory/skills/{id}       # Update student skills
```

**Phase 3 — RAG**
```
POST   /api/v2/rag/query               # Enhanced RAG query
POST   /api/v2/rag/index               # Index content into pgvector
```

**Phase 4 — Orchestrator**
```
POST   /api/v2/ai/chat                 # Orchestrated AI chat (replaces /chat)
POST   /api/v2/ai/explain              # Explain a concept adaptively
```

**Phase 5 — Tools**
```
GET    /api/v2/tools                    # List available tools
POST   /api/v2/tools/{tool_name}/run   # Execute a tool
```

**Phase 7 — Evaluation**
```
GET    /api/v2/eval/metrics             # Get evaluation metrics
POST   /api/v2/eval/report             # Generate evaluation report
```

**Phase 9 — Content Intelligence**
```
POST   /api/v2/content/audit/{course}  # Audit a course
POST   /api/v2/content/generate        # Generate draft content
GET    /api/v2/content/review-queue    # Get content awaiting review
POST   /api/v2/content/approve/{id}   # Approve/reject content
```

**Phase 10 — Research**
```
POST   /api/v2/research/experiment     # Create experiment
GET    /api/v2/research/results        # Get experiment results
```

### Existing Endpoints: PRESERVED
All existing endpoints (`/chat`, `/ask-ai/`, `/run-code/`, etc.) continue to work unchanged. New `/api/v2/` endpoints run in parallel.

---

## 6. Implementation Phases

### Phase 1: Architecture & Documentation (This document)
- Document existing architecture ✓
- Propose new architecture ✓
- Get approval
- Set up `docs/research/` directory
- **Complexity**: Low
- **Risk**: None
- **Duration**: 1-2 days

### Phase 2: Memory + Student Model
- Create memory tables (Alembic migrations)
- Implement `MemoryService` and `StudentModelService`
- Begin recording episodic events from existing interactions
- Build student skill tracking from assessment results
- **Complexity**: Medium
- **Risk**: Low — purely additive, no existing features changed
- **Duration**: 1-2 weeks

### Phase 3: Improved RAG
- Add pgvector extension to PostgreSQL
- Create `content_embeddings` table
- Implement migration script from FAISS to pgvector
- Build improved retrieval pipeline with reranking
- Keep FAISS as fallback during migration
- **Complexity**: Medium
- **Risk**: Medium — RAG is critical path, need fallback
- **Duration**: 1-2 weeks

### Phase 4: AI Orchestrator
- Implement `AIOrchestrator` service class
- Wire up memory, RAG, and existing AI (Gemini) through orchestrator
- Create `/api/v2/ai/chat` endpoint
- Keep existing `/chat` endpoint unchanged
- **Complexity**: High
- **Risk**: Medium — new endpoint runs in parallel, doesn't break existing
- **Duration**: 2-3 weeks

### Phase 5: Tool Registry + Sandboxed Execution
- Create tool registry with permission system
- Wrap existing code execution in tool interface
- Add calculator, code analyzer, course search tools
- Audit logging for all tool invocations
- **Complexity**: Medium
- **Risk**: Low — builds on existing Docker sandbox
- **Duration**: 1-2 weeks

### Phase 6: Reasoning + Planning
- Implement `PlannerService` for task decomposition
- Add structured reasoning metadata storage
- Multi-step problem solving for complex questions
- **Complexity**: High
- **Risk**: Low — enhances orchestrator, doesn't change existing behavior
- **Duration**: 2-3 weeks

### Phase 7: Evaluation
- Implement `EvaluatorService`
- Add independent correctness checking
- Track metrics (correctness, relevance, hallucination, latency)
- Create evaluation dashboard for admin
- **Complexity**: Medium
- **Risk**: Low — purely observational, no production impact
- **Duration**: 1-2 weeks

### Phase 8: Adaptive Learning
- Use student model to adapt lesson delivery
- Prerequisite detection and recommendation
- Difficulty adjustment based on demonstrated understanding
- Targeted practice generation
- **Complexity**: High
- **Risk**: Medium — affects learning experience, needs A/B testing
- **Duration**: 2-3 weeks

### Phase 9: Course Content Intelligence Engine
- Curriculum auditing tools
- Lesson quality scoring
- AI content draft generation (with human review gate)
- Code example validation via sandboxed execution
- Student feedback analysis
- Content versioning
- **Complexity**: Very High
- **Risk**: Medium — content changes need careful review
- **Duration**: 3-4 weeks

### Phase 10: Research / Experiment Framework
- Experiment configuration and execution
- A/B testing infrastructure
- Metrics collection and comparison
- `docs/research/` documentation
- **Complexity**: Medium
- **Risk**: Low — infrastructure for testing, not production changes
- **Duration**: 1-2 weeks

### Phase 11: Multi-Agent Capabilities (Future)
- Specialized agents (code tutor, concept explainer, debugger)
- Agent collaboration protocols
- **Complexity**: Very High
- **Risk**: High — requires all previous phases to be stable
- **Duration**: 4+ weeks

---

## 7. Course Migration Strategy

### Step-by-Step Approach (Do NOT rewrite everything)

1. **Inventory** all 20 tracks, ~200+ courses, ~1500+ lessons
2. **Define quality standard** based on lesson structure template
3. **Audit 5 pilot lessons** manually using the standard
4. **Build automated quality checker** (code syntax validation, prerequisite detection)
5. **Score all lessons** programmatically
6. **Identify bottom 10%** — lessons with lowest quality scores
7. **Generate improved drafts** for bottom 10% using Content Intelligence Engine
8. **Human review and approve** improved versions
9. **Measure impact** on student performance
10. **Progressively migrate** remaining content based on measured improvement

### Content Migration Report (to be created before mass changes)
```
docs/content-migration-report.md
- Total courses: X
- Total lessons: X
- Quality score distribution
- Lessons flagged for improvement
- Missing prerequisites identified
- Duplicate content found
- Outdated material flagged
```

---

## 8. Security Model

### Authentication & Authorization
- **Existing**: JWT + bcrypt (PRESERVED)
- **Enhanced**: Add RBAC with explicit permissions (admin, teacher, student)
- **New**: Consolidate `_is_admin()` into single service

### Input Validation
- **Existing**: Pydantic schemas (PRESERVED)
- **Enhanced**: Add input length limits, SQL injection checks on search

### Rate Limiting
- **Existing**: slowapi on code execution (PRESERVED)
- **Enhanced**: Apply rate limits to all AI endpoints

### Audit Logging
- **New**: Log all admin actions, tool invocations, content changes

### Secret Management
- **New**: Remove secrets from `.env` in repo, use Azure Key Vault or environment-only secrets

### AI-Specific Security
- **Prompt injection defense**: Input sanitization, system prompt separation
- **Tool permissions**: Explicit allow-list per tool
- **Output filtering**: Check AI responses for harmful content
- **Sandboxed execution**: Existing Docker sandbox (PRESERVED)

---

## 9. What Should NOT Be Changed

1. **React/Vite frontend framework** — Modern, works well
2. **FastAPI backend framework** — Fast, typed, well-suited
3. **PostgreSQL database** — Correct choice
4. **Docker-sandboxed code execution** — Security is correct
5. **Paystack integration** — Right for Nigerian market
6. **PWA/offline architecture** — Critical for target users
7. **bcrypt + JWT auth** — Industry standard
8. **Gamification system** — Engagement is working
9. **Existing API endpoint contracts** — Don't break existing clients
10. **i18n infrastructure** — Supports Nigerian languages

---

## 10. Risks

| Risk | Mitigation |
|------|-----------|
| Breaking existing features during refactoring | Every phase must leave app in working state; existing endpoints never removed |
| pgvector migration data loss | Keep FAISS as fallback during migration; verify before cutover |
| AI orchestrator adds latency | Start simple (single LLM call + memory lookup), optimize later |
| Over-engineering memory system | Start with episodic + skills only; add procedural/semantic as needed |
| Content Intelligence Engine auto-publishes bad content | Hard gate: all AI content requires human approval |
| Evaluation system is just another LLM call | Use code execution for code checks; use rubrics not just LLM judgment |
| Scope creep | Each phase has clear deliverables; Phase 11 is explicitly "future" |

---

## 11. Estimated Complexity Summary

| Phase | Description | Complexity | Risk | Estimated Time |
|-------|-------------|:---:|:---:|:---:|
| 1 | Architecture & Documentation | Low | None | 1-2 days |
| 2 | Memory + Student Model | Medium | Low | 1-2 weeks |
| 3 | Improved RAG | Medium | Medium | 1-2 weeks |
| 4 | AI Orchestrator | High | Medium | 2-3 weeks |
| 5 | Tool Registry | Medium | Low | 1-2 weeks |
| 6 | Reasoning + Planning | High | Low | 2-3 weeks |
| 7 | Evaluation | Medium | Low | 1-2 weeks |
| 8 | Adaptive Learning | High | Medium | 2-3 weeks |
| 9 | Content Intelligence | Very High | Medium | 3-4 weeks |
| 10 | Research Framework | Medium | Low | 1-2 weeks |
| 11 | Multi-Agent (Future) | Very High | High | 4+ weeks |

**Total estimated: 16-26 weeks** (phases are sequential, but some can overlap)

---

## 12. Recommended Implementation Order

The phases are ordered by:
1. **Foundation first** — Memory and RAG are prerequisites for everything else
2. **Risk management** — Lower-risk phases before higher-risk
3. **Value delivery** — Each phase delivers usable improvement
4. **Dependency chain** — Orchestrator needs memory and RAG; evaluation needs orchestrator

**Recommended order**: 1 → 2 → 3 → 4 → 5 → 7 → 6 → 8 → 9 → 10 → 11

(Evaluation moved before Reasoning because it's simpler and validates the orchestrator)

---

## 13. Success Metrics

Success is NOT measured by amount of code generated.

| Metric | Target |
|--------|--------|
| Existing features still working after each phase | 100% |
| AI response correctness (evaluator-verified) | >85% |
| Code example validity (sandbox-tested) | >95% |
| Response latency (p95) | <5 seconds |
| Student assessment improvement over 30 days | Measurable increase |
| Lesson quality score (audited) | Continuous improvement |
| Hallucination rate | <5% |
| Test coverage on new code | >80% |
| Zero secrets in source control | Verified |
| All AI-generated content human-reviewed before publish | 100% |

---

> **STOP**: This document requires explicit approval before any implementation begins.
> Review and approve or request modifications before proceeding to Phase 2.
