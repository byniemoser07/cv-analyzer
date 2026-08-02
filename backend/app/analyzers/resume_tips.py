def generate_resume_tips(resume_analysis, job_match, github):

    tips = []

    # Missing job skills
    missing = job_match["keyword_match"]["missing_skills"]

    if missing:
        tips.append(
            f"Learn these skills: {', '.join(missing)}."
        )

    # GitHub improvement
    if github["profile"]["public_repositories"] < 5:
        tips.append("Add more public GitHub repositories.")

    # README suggestion
    tips.append("Add README files to every GitHub project.")

    # Resume formatting
    tips.append("Quantify achievements using numbers whenever possible.")

    # ATS suggestion
    tips.append("Customize your resume for every job application.")

    return tips