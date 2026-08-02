def generate_interview_questions(resume, job_match):
    questions = []

    keyword_match = job_match.get("keyword_match", {})

    matched = keyword_match.get("matched_skills", [])
    missing = keyword_match.get("missing_skills", [])

    # Questions from matched skills
    for skill in matched:
        questions.append(
            f"Explain a project where you used {skill}."
        )

    # Questions from missing skills
    for skill in missing[:3]:
        questions.append(
            f"What do you know about {skill}, and how would you learn it quickly?"
        )

    # Experience question
    if resume.get("experience"):
        questions.append(
            "Describe the biggest technical challenge you faced during your internship."
        )

    # Project question
    if resume.get("projects"):
        questions.append(
            "Which project are you most proud of and why?"
        )

    return questions


def interview_readiness(score):
    if score >= 85:
        return {
            "status": "Excellent",
            "message": "You are well prepared for technical interviews."
        }

    elif score >= 70:
        return {
            "status": "Good",
            "message": "You are interview ready but should strengthen a few areas."
        }

    elif score >= 55:
        return {
            "status": "Average",
            "message": "Practice core concepts and improve missing skills before interviewing."
        }

    return {
        "status": "Needs Improvement",
        "message": "Focus on your skill gaps and build more projects before applying."
    }