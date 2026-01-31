from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import connect_db, close_db
from app.utils.config import settings

from app.routes import router as api_router

app = FastAPI(
    title="Skill Gap Intelligence",
    version="0.1.0",
    description="Analyze resume vs job description and identify skill gaps",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.ENV == "development" else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    connect_db()

@app.on_event("shutdown")
def shutdown_event():
    close_db()

@app.get("/health-check")
def health_check():
    return {
        "status": "ok",
        "service": "Skill Gap Intelligence API",
        "environment": settings.ENV,
    }

app.include_router(api_router, prefix="/api")