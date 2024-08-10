from fastapi import APIRouter, HTTPException
from app.services import fetch_github_profile, generate_pdf_report

router = APIRouter()

@router.post("/generate-report/")
async def generate_report(github_url: str):
    profile_data = fetch_github_profile(github_url)
    if not profile_data:
        raise HTTPException(status_code=404, detail="GitHub profile not found")
    pdf_path = generate_pdf_report(profile_data)
    return {"pdf_url": pdf_path}
