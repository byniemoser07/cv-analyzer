def calculate_ats_score(analysis):

    score = 0

    breakdown = {}

    explanation = []

    # Contact
    contact_score = 0

    if analysis["name"]:
        contact_score += 3
        explanation.append("✔ Name detected")

    if analysis["email"]:
        contact_score += 4
        explanation.append("✔ Email detected")

    if analysis["phone"]:
        contact_score += 3
        explanation.append("✔ Phone number detected")

    breakdown["contact"] = contact_score
    score += contact_score

    # Skills
    skill_count = len(analysis["skills"])

    skill_score = min(skill_count, 25)

    breakdown["skills"] = skill_score
    score += skill_score

    explanation.append(f"✔ {skill_count} technical skills identified")

    # Education
    education_score = 10 if analysis["education"] else 0

    breakdown["education"] = education_score
    score += education_score

    if education_score:
        explanation.append("✔ Education section found")
    else:
        explanation.append("✘ Education section missing")

    # Experience
    experience_score = 25 if analysis["experience"] else 0

    breakdown["experience"] = experience_score
    score += experience_score

    if experience_score:
        explanation.append("✔ Experience section found")
    else:
        explanation.append("✘ Experience section missing")

    # Projects
    project_score = 20 if analysis["projects"] else 0

    breakdown["projects"] = project_score
    score += project_score

    if project_score:
        explanation.append("✔ Projects section found")
    else:
        explanation.append("✘ Projects section missing")

    # ATS Keywords
    keyword_score = 10 if skill_count >= 15 else 4

    breakdown["keywords"] = keyword_score
    score += keyword_score

    if skill_count >= 15:
        explanation.append("✔ Strong ATS keyword coverage")
    else:
        explanation.append("✘ Add more ATS keywords")

    score = min(score, 100)

    recommendations = []

    if skill_count < 15:
        recommendations.append(
            "Include more technical skills."
        )

    if not analysis["projects"]:
        recommendations.append(
            "Add at least one project."
        )

    if not analysis["experience"]:
        recommendations.append(
            "Include internship or work experience."
        )

    return {

        "overall_score": score,

        "breakdown": breakdown,

        "explanation": explanation,

        "recommendations": recommendations

    }