import re
import spacy
from app.data.skills import SKILLS
nlp = spacy.load("en_core_web_sm")

DEGREES = [
    "Bachelor",
    "Master",
    "B.Tech",
    "M.Tech",
    "B.E",
    "M.E",
    "BCA",
    "MCA",
    "MBA",
    "PhD",
    "Diploma",
]

EXPERIENCE_KEYWORDS = [
    "Engineer",
    "Developer",
    "Analyst",
    "Scientist",
    "Manager",
    "Intern",
    "Consultant",
    "Researcher",
]


def extract_email(text):
    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text,
    )
    return match.group() if match else None


def extract_phone(text):
    match = re.search(r"(\+?\d[\d\s\-]{8,15})", text)
    return match.group() if match else None


def extract_name(text):
    lines = text.split("\n")

    for line in lines[:5]:
        line = line.strip()

        if (
            line
            and "@" not in line
            and len(line.split()) <= 4
            and not any(char.isdigit() for char in line)
        ):
            return line

    return None


def extract_skills(text):

    found = []

    text_lower = text.lower()

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found.append(skill)

    return sorted(set(found))


def extract_education(text):
    found = []
    lower = text.lower()

    for degree in DEGREES:
        if degree.lower() in lower:
            found.append(degree)

    return sorted(set(found))


def extract_experience(text):

    experience = []

    inside = False

    for line in text.split("\n"):

        if "WORK EXPERIENCE" in line.upper():
            inside = True
            continue

        if inside:

            if line.strip() == "":
                continue

            if line.upper() == "CERTIFICATIONS":
                break

            experience.append(line.strip())

    return experience


def extract_projects(text):

    projects = []

    inside = False

    for line in text.split("\n"):

        if "PROJECTS" in line.upper():
            inside = True
            continue

        if inside:

            if line.strip() == "":
                continue

            if "CERTIFICATION" in line.upper():
                break

            if "—" in line or "-" in line:
                projects.append(line.strip())

    return projects


def analyze_resume(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "projects": extract_projects(text),
    }