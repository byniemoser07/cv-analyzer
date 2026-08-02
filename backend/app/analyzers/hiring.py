def hiring_recommendation(score):

    if score >= 85:
        return "Strong Hire"

    if score >= 70:
        return "Hire"

    if score >= 55:
        return "Consider"

    return "Not Recommended"