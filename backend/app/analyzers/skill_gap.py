def skill_gap(job_match):

    keyword = job_match["keyword_match"]

    matched = len(keyword["matched_skills"])
    missing = len(keyword["missing_skills"])

    total = matched + missing

    if total == 0:
        percentage = 0
    else:
        percentage = round((missing / total) * 100)

    return {
        "matched": matched,
        "missing": missing,
        "gap_percentage": percentage
    }