from fastapi import APIRouter

from pydantic import BaseModel

from app.github.github_api import get_github_profile

router = APIRouter()


class GithubRequest(BaseModel):

    username: str


@router.post("/github")

def github(request: GithubRequest):

    return get_github_profile(
        request.username
    )