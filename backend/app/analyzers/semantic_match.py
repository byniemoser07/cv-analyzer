from difflib import SequenceMatcher


def semantic_match(resume_text, job_description):

    similarity = SequenceMatcher(
        None,
        resume_text.lower(),
        job_description.lower()
    ).ratio()

    return {
        "semantic_score": round(similarity * 100, 2)
    }