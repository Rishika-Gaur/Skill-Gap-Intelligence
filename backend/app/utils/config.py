import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENV: str = os.getenv("ENV")
    MONGO_URI: str | None = os.getenv("MONGO_URI")
    HOST: str = os.getenv("HOST")
    PORT: int = int(os.getenv("PORT"))
    DB_NAME: str = os.getenv("DB_NAME")

settings = Settings()