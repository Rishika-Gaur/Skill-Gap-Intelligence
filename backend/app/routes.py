from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr

from app.services.parser import extract_text
from app.services.analyzer import analyze_resume_vs_jd
from app.services.pdf import generate_report
from app.services.email import send_email_with_attachment

router = APIRouter()

@router.post("/analyze")
async def analyze(
    resume_file: UploadFile = File(None),
    resume_text: str = Form(None),
    jd_file: UploadFile = File(None),
    jd_text: str = Form(None),
):
    resume = extract_text(resume_file, resume_text)
    jd = extract_text(jd_file, jd_text)

    result = analyze_resume_vs_jd(resume, jd)
    pdf_path = generate_report(result)

    return {
        "analysis": result,
        "pdf_report": pdf_path
    }


@router.get("/download/{file_name}")
def download_report(file_name: str):
    return FileResponse(
        path=file_name,
        filename=file_name,
        media_type="application/pdf",
    )

class EmailRequest(BaseModel):
    email: EmailStr
    pdf_path: str
#make diff file for validators and models

@router.post("/send")
def send_report_email(payload: EmailRequest):
    send_email_with_attachment(
        to_email=payload.email,
        subject="Your Skill Gap Analysis Report",
        body="Please find attached your resume vs job description analysis report.",
        pdf_path=payload.pdf_path,
    )

    return {
        "status": "sent",
        "email": payload.email
    }

