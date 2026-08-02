def generate_recommendations(analysis, job_match):

    recommendations = []

    if len(job_match["missing_skills"]) > 0:
        recommendations.append(
            "Learn these missing skills: "
            + ", ".join(job_match["missing_skills"])
        )

    if len(analysis["projects"]) < 2:
        recommendations.append(
            "Add more technical projects to strengthen your portfolio."
        )

    if len(analysis["experience"]) == 0:
        recommendations.append(
            "Include internship or work experience."
        )

    if len(analysis["skills"]) < 10:
        recommendations.append(
            "Expand the technical skills section."
        )

    if not recommendations:
        recommendations.append(
            "Excellent resume! Only minor improvements recommended."
        )

    return recommendations