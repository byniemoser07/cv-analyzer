import re

from app.data.skills import SKILLS
from app.analyzers.semantic_match import semantic_match


def extract_job_skills(job_description):

    found = []

    job_lower = job_description.lower()

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, job_lower):
            found.append(skill)

    return sorted(set(found))


def match_resume_to_job(resume_analysis, resume_text, job_description):

    resume_skills = set(resume_analysis["skills"])

    job_skills = set(extract_job_skills(job_description))

    matched = sorted(resume_skills & job_skills)

    missing = sorted(job_skills - resume_skills)

    keyword_score = 0

    if len(job_skills) > 0:
        keyword_score = round(
            (len(matched) / len(job_skills)) * 100
        )

    semantic = semantic_match(
        resume_text,
        job_description
    )

    overall = round(
        (
            keyword_score +
            semantic["semantic_score"]
        ) / 2,
        2
    )

    recommendations = []

    if missing:
        recommendations.append(
            "Learn these missing skills: " +
            ", ".join(missing)
        )

    if len(resume_analysis["projects"]) < 2:
        recommendations.append(
            "Add more technical projects."
        )

    if len(resume_analysis["experience"]) == 0:
        recommendations.append(
            "Include internship or work experience."
        )

    return {

        "keyword_match": {

            "match_score": keyword_score,

            "matched_skills": matched,

            "missing_skills": missing

        },

        "semantic_match": semantic,

        "overall_match": overall,

        "recommendations": recommendations

    }