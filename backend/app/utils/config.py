import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI: str | None = os.getenv("MONGO_URI")
    ENV: str = os.getenv("ENV", "development")

settings = Settings()
