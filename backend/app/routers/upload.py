import os
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.nlp.extractor import analyze_resume
from app.parser.resume_parser import extract_text_from_pdf
from app.analyzers.ats_score import calculate_ats_score

router = APIRouter(tags=["Resume Upload"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a resume PDF, extract text and analyze it.
    """

    try:
        # Allow only PDF
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        # Save uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text
        text = extract_text_from_pdf(file_path)

        # Analyze
        analysis = analyze_resume(text)

        ats_result = calculate_ats_score(analysis)

        # Debug
        print("=" * 60)
        print("UPLOAD API HIT")
        print(analysis)
        print("=" * 60)

        return {
    "success": True,
    "filename": file.filename,
    "analysis": analysis,
    "ats_score": ats_result
}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )