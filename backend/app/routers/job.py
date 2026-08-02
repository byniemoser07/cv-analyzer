from fastapi import APIRouter
from pydantic import BaseModel

from app.nlp.extractor import analyze_resume
from app.analyzers.job_match import match_resume_to_job
from app.analyzers.semantic_match import semantic_match
from app.analyzers.recommendations import generate_recommendations

router = APIRouter()


class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/match-job")
def match_job(request: JobMatchRequest):

    analysis = analyze_resume(request.resume_text)

    result = match_resume_to_job(
        analysis,
        request.job_description
    )
    
    semantic_result = semantic_match(
    request.resume_text,
    request.job_description
)
    recommendations = generate_recommendations(
    analysis,
    result
)
    keyword_score = result["match_score"]
    semantic_score = semantic_result["semantic_score"]

    overall_score = round(
    (keyword_score + semantic_score) / 2,
    2
)
    return {
    "analysis": analysis,
    "keyword_match": result,
    "semantic_match": semantic_result,
    "overall_match": overall_score,
    "recommendations": recommendations
}