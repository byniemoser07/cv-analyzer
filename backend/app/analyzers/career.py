def recommend_roles(analysis):

    skills = [skill.lower() for skill in analysis["skills"]]

    roles = []

    if "python" in skills:
        roles.append("Python Developer")

    if "postgresql" in skills or "mysql" in skills:
        roles.append("Backend Developer")

    if "machine learning" in skills or "deep learning" in skills:
        roles.append("Machine Learning Engineer")

    if "pandas" in skills or "numpy" in skills:
        roles.append("Data Analyst")

    if "react" in skills or "javascript" in skills:
        roles.append("Full Stack Developer")

    return list(set(roles))