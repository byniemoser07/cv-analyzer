def generate_resume_feedback(
    ats,
    job_match,
    github
):
    strengths = []
    weaknesses = []
    improvements = []

    # ATS
    if ats["overall_score"] >= 90:
        strengths.append("Excellent ATS score")
    elif ats["overall_score"] >= 75:
        strengths.append("Good ATS compatibility")
    else:
        weaknesses.append("Low ATS score")
        improvements.append("Improve resume formatting and keyword coverage")

    # Job Match
    missing = job_match["keyword_match"]["missing_skills"]

    if missing:
        weaknesses.append(
            f"Missing {len(missing)} important job skills"
        )

        improvements.append(
            "Learn: " + ", ".join(missing)
        )
    else:
        strengths.append(
            "Excellent match with job description"
        )

    # GitHub
    if github["github_score"] >= 80:
        strengths.append("Strong GitHub portfolio")
    else:
        weaknesses.append("GitHub profile needs improvement")

        improvements.append(
            "Create more public repositories"
        )

        improvements.append(
            "Add README files to projects"
        )

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "improvements": improvements
    }