def generate_dashboard_stats(
    resume_analysis,
    github
):

    return {

        "technical_skills": len(resume_analysis["skills"]),

        "education_entries": len(resume_analysis["education"]),

        "experience_entries": len(resume_analysis["experience"]),

        "projects": len(resume_analysis["projects"]),

        "github_repositories": github["profile"]["public_repositories"]

    }