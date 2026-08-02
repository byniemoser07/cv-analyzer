def candidate_rank(score):

    if score >= 90:
        return "Top 1%"

    elif score >= 80:
        return "Top 10%"

    elif score >= 70:
        return "Top 25%"

    elif score >= 60:
        return "Top 50%"

    return "Average"