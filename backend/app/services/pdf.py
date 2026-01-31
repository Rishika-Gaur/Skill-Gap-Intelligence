from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid

def generate_report(data: dict) -> str:
    file_name = f"skill_gap_report_{uuid.uuid4().hex}.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "ML-Based Skill Gap Report")

    c.setFont("Helvetica", 12)
    c.drawString(
        50, 770,
        f"Semantic Match Score: {data['final_match_percentage']}%"
    )

    y = 740
    c.drawString(50, y, "Matched Skills:")
    y -= 20
    for skill in data["matched_skills"][:25]:
        c.drawString(60, y, f"- {skill}")
        y -= 14

    y -= 20
    c.drawString(50, y, "Missing Skills:")
    y -= 20
    for skill in data["skill_gaps"][:25]:
        c.drawString(60, y, f"- {skill}")
        y -= 14

    c.save()
    return file_name
