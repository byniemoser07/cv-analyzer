def predict_salary(overall_score):
    if overall_score >= 90:
        return {
            "range": "₹18-35 LPA",
            "level": "Senior"
        }

    elif overall_score >= 75:
        return {
            "range": "₹10-18 LPA",
            "level": "Mid-Level"
        }

    elif overall_score >= 60:
        return {
            "range": "₹6-10 LPA",
            "level": "Junior"
        }

    else:
        return {
            "range": "₹3-6 LPA",
            "level": "Entry"
        }