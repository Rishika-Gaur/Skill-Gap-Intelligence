from fastapi import UploadFile
import pdfplumber

def extract_text(file: UploadFile | None, text: str | None) -> str:
    if text:
        return text.strip()

    if not file:
        raise ValueError("No resume or text provided")

    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join(
                page.extract_text() or "" for page in pdf.pages
            )

    raise ValueError("Unsupported file type")
