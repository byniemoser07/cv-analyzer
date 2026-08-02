import requests
from collections import Counter


def get_github_profile(username):

    profile_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    profile_response = requests.get(profile_url)

    # -------------------------------------
    # User not found / Invalid username
    # -------------------------------------
    if profile_response.status_code != 200:

        return {

            "github_score": 0,

            "profile": {

                "username": username,

                "name": "GitHub User Not Found",

                "followers": 0,

                "following": 0,

                "public_repositories": 0,

                "profile_url": "",

                "avatar": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

            },

            "top_languages": [],

            "repositories": [],

            "recommendations": [

                "GitHub username not found. Please check the username."

            ]

        }

    repo_response = requests.get(repos_url)

    profile = profile_response.json()
    repos = repo_response.json()

    language_counter = Counter()

    total_stars = 0

    repo_list = []

    for repo in repos:

        if repo.get("language"):

            language_counter[repo["language"]] += 1

        total_stars += repo.get("stargazers_count", 0)

        repo_list.append({

            "name": repo.get("name", ""),

            "stars": repo.get("stargazers_count", 0),

            "language": repo.get("language")

        })

    top_languages = [

        lang

        for lang, count in language_counter.most_common(5)

    ]

    github_score = 50

    github_score += min(profile.get("public_repos", 0), 20)

    github_score += min(profile.get("followers", 0), 20)

    github_score += min(total_stars, 10)

    github_score = min(github_score, 100)

    recommendations = []

    if profile.get("public_repos", 0) < 5:

        recommendations.append(
            "Create more public repositories."
        )

    if total_stars == 0:

        recommendations.append(
            "Improve project quality to gain stars."
        )

    if len(top_languages) < 3:

        recommendations.append(
            "Diversify your technology stack."
        )

    return {

        "github_score": github_score,

        "profile": {

            "username": profile.get("login", ""),

            "name": profile.get("name", ""),

            "followers": profile.get("followers", 0),

            "following": profile.get("following", 0),

            "public_repositories": profile.get("public_repos", 0),

            "profile_url": profile.get("html_url", ""),

            "avatar": profile.get("avatar_url", "")

        },

        "top_languages": top_languages,

        "repositories": repo_list,

        "recommendations": recommendations

    }