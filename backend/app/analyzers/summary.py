def generate_summary(analysis, job_match):

    name = analysis.get("name", "Candidate")

    skills = analysis.get("skills", [])

    experience = analysis.get("experience", [])

    missing = job_match["keyword_match"]["missing_skills"]

    summary = (
        f"{name} has "
        f"{len(skills)} technical skills, "
        f"{len(experience)} experience entries and "
        f"demonstrates strong knowledge in "
        f"{', '.join(skills[:5])}."
    )

    if missing:
        summary += (
            " To become a stronger candidate, "
            f"consider learning {', '.join(missing)}."
        )

    return summary
