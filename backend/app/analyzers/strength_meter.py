from app.data.skills import SKILLS

BACKEND = {
    "Python", "Node.js", "Express.js", "FastAPI",
    "Flask", "SQL", "PostgreSQL", "MongoDB", "MySQL"
}

FRONTEND = {
    "HTML", "CSS", "JavaScript", "React"
}

ML = {
    "Machine Learning", "Deep Learning",
    "NLP", "Scikit-learn", "NumPy", "Pandas"
}

DEVOPS = {
    "Docker", "Git", "GitHub", "Kubernetes",
    "AWS", "Azure", "GCP"
}


def score(category, skills):
    matched = len(category & skills)
    return round((matched / len(category)) * 100)


def generate_strength_meter(resume_analysis):
    skills = set(resume_analysis["skills"])

    return {
        "Backend": score(BACKEND, skills),
        "Frontend": score(FRONTEND, skills),
        "Machine Learning": score(ML, skills),
        "DevOps & Cloud": score(DEVOPS, skills)
    }