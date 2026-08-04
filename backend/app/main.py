from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.upload import router as upload_router
from app.routers.job import router as job_router
from app.routers.github import router as github_router
from app.routers.analyze import router as analyze_router

app = FastAPI(
    title="AI CV Analyzer",
    version="1.0.0"
)

# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Routers
# ---------------------------------------------------

app.include_router(upload_router)
app.include_router(job_router)
app.include_router(github_router)
app.include_router(analyze_router)

# ---------------------------------------------------
# Home
# ---------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API",
        "version": "2.0",
        "status": "Running"
    }


# ---------------------------------------------------
# About
# ---------------------------------------------------

@app.get("/about")
def about():
    return {
        "project": "AI Resume Analyzer",
        "developer": "Akarshit Singh",
        "version": "2.0",
        "features": [
            "Resume Parsing",
            "ATS Score",
            "Keyword Matching",
            "Semantic Matching",
            "GitHub Analysis",
            "Overall Candidate Score",
            "Summary Generator",
            "Recommended Roles",
            "Learning Roadmap",
            "Resume Feedback",
            "Strength Meter",
            "Dashboard Statistics",
            "Skill Gap Analysis",
            "Resume Grade",
            "Hiring Recommendation",
            "Missing Skills Priority",
            "Salary Prediction",
            "Interview Readiness",
            "Resume Completeness",
            "Candidate Ranking",
            "Interview Questions",
            "Resume Tips"
        ]
    }