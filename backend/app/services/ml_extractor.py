import spacy

# Transformer-based NLP model
nlp = spacy.load("en_core_web_trf")

# Common labels that often include skills
SKILL_LIKE_ENTITIES = {"ORG", "PRODUCT", "WORK_OF_ART", "LANGUAGE"}

def extract_skills_ml(text: str) -> list[str]:
    doc = nlp(text)

    skills = set()
    for ent in doc.ents:
        if ent.label_ in SKILL_LIKE_ENTITIES:
            skills.add(ent.text.lower())

    return sorted(list(skills))
