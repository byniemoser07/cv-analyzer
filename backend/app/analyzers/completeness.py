def resume_completeness(resume):

    sections = [
        "skills",
        "education",
        "experience",
        "projects"
    ]

    completed = 0

    for s in sections:
        if resume.get(s):
            completed += 1

    score = round((completed / len(sections)) * 100)

    return {
        "completed_sections": completed,
        "total_sections": len(sections),
        "completion_score": score
    }