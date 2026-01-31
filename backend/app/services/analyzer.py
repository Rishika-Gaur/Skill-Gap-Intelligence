from app.services.ml_similarity import ml_similarity
from app.services.ml_extractor import extract_skills_ml


def analyze_resume_vs_jd(resume_text: str, jd_text: str):
    # -------- ML Skill Extraction --------
    resume_skills = set(extract_skills_ml(resume_text))
    jd_skills = set(extract_skills_ml(jd_text))

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills

    # -------- ML Similarity --------
    similarity_score = ml_similarity(resume_text, jd_text)

    return {
        "final_match_percentage": similarity_score,
        "matched_skills": sorted(list(matched_skills)),
        "skill_gaps": sorted(list(missing_skills)),
        "resume_skills_extracted": sorted(list(resume_skills)),
        "jd_skills_extracted": sorted(list(jd_skills)),
    }
