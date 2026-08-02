def generate_learning_roadmap(job_match):

    missing = job_match["keyword_match"]["missing_skills"]

    roadmap = []

    for index, skill in enumerate(missing, start=1):

        roadmap.append({

            "step": index,

            "skill": skill,

            "status": "Recommended"

        })

    return roadmap