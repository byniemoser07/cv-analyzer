from typing import Optional
from fastapi import APIRouter, UploadFile, File, Form
import os
import shutil

from app.parser.resume_parser import extract_text_from_pdf
from app.nlp.extractor import analyze_resume

from app.analyzers.ats_score import calculate_ats_score
from app.analyzers.job_match import match_resume_to_job
from app.analyzers.summary import generate_summary
from app.analyzers.career import recommend_roles
from app.analyzers.roadmap import generate_learning_roadmap
from app.analyzers.resume_feedback import generate_resume_feedback
from app.analyzers.strength_meter import generate_strength_meter
from app.analyzers.dashboard_stats import generate_dashboard_stats
from app.analyzers.skill_gap import skill_gap
from app.analyzers.grade import resume_grade
from app.analyzers.hiring import hiring_recommendation
from app.analyzers.priorities import prioritize_skills
from app.analyzers.salary import predict_salary
from app.github.github_api import get_github_profile
from app.analyzers.completeness import resume_completeness
from app.analyzers.ranking import candidate_rank
from app.analyzers.interview import (
    generate_interview_questions,
    interview_readiness,
)
from app.analyzers.resume_tips import generate_resume_tips

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/analyze-profile")
async def analyze_profile(
    file: UploadFile = File(...),
    job_description: Optional[str] = Form(""),
    github_username: str = Form(...)
):

    # -----------------------------
    # Save Resume
    # -----------------------------
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # -----------------------------
    # Extract Resume Text
    # -----------------------------
    resume_text = extract_text_from_pdf(file_path)

    # -----------------------------
    # Resume Analysis
    # -----------------------------
    resume_analysis = analyze_resume(resume_text)
    print("Resume analysis completed")

    # -----------------------------
    # ATS Score
    # -----------------------------
    ats = calculate_ats_score(resume_analysis)
    print("ATS completed")

    # -----------------------------
    # Job Match
    # -----------------------------
    job_match = match_resume_to_job(
        resume_analysis,
        resume_text,
        job_description
    )
    print("Job match completed")

    # -----------------------------
    # GitHub Analysis
    # -----------------------------
    github = get_github_profile(github_username)
    print("GitHub completed")

    # -----------------------------
    # Overall Score
    # -----------------------------
    overall = round(
        (
            ats["overall_score"]
            + job_match["overall_match"]
            + github.get("github_score", 0)
        ) / 3,
        2
    )

    # -----------------------------
    # Derived Results
    # -----------------------------
    summary = generate_summary(
        resume_analysis,
        job_match
    )

    roles = recommend_roles(resume_analysis)

    roadmap = generate_learning_roadmap(job_match)

    feedback = generate_resume_feedback(
        ats,
        job_match,
        github
    )

    resume_tips = generate_resume_tips(
        resume_analysis,
        job_match,
        github
    )

    strength_meter = generate_strength_meter(
        resume_analysis
    )

    dashboard = generate_dashboard_stats(
        resume_analysis,
        github
    )

    gap = skill_gap(job_match)

    prioritized = prioritize_skills(
        job_match["keyword_match"]["missing_skills"]
    )

    interview_questions = generate_interview_questions(
        resume_analysis,
        job_match
    )

    grade = resume_grade(overall)

    hiring = hiring_recommendation(overall)

    salary = predict_salary(overall)

    interview = interview_readiness(overall)

    completeness = resume_completeness(resume_analysis)

    ranking = candidate_rank(overall)

    # -----------------------------
    # Final Response
    # -----------------------------
    return {

        "candidate": resume_analysis,

        "ats": ats,

        "job_match": job_match,

        "github": github,

        "overall_score": overall,

        "grade": grade,

        "hiring_recommendation": hiring,

        "skill_gap": gap,

        "summary": summary,

        "recommended_roles": roles,

        "learning_roadmap": roadmap,

        "resume_feedback": feedback,

        "strength_meter": strength_meter,

        "dashboard": dashboard,

        "missing_skills_priority": prioritized,

        "salary_prediction": salary,

        "interview_readiness": interview,

        "resume_completeness": completeness,

        "candidate_ranking": ranking,

        "interview_questions": interview_questions,

        "resume_tips": resume_tips

    } 