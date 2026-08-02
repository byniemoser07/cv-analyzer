HIGH_PRIORITY = {
    "AWS",
    "Docker",
    "Kubernetes",
    "FastAPI"
}

MEDIUM_PRIORITY = {
    "React",
    "Node.js",
    "Express.js",
    "MongoDB",
    "PostgreSQL",
    "SQL"
}


def prioritize_skills(missing_skills):

    prioritized = []

    for skill in missing_skills:

        if skill in HIGH_PRIORITY:
            priority = "High"

        elif skill in MEDIUM_PRIORITY:
            priority = "Medium"

        else:
            priority = "Low"

        prioritized.append({
            "skill": skill,
            "priority": priority
        })

    return prioritized