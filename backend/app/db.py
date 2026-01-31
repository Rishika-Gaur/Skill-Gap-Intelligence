from pymongo import MongoClient
from app.utils.config import settings

client: MongoClient | None = None
db = None


def connect_db():
    global client, db

    if not settings.MONGO_URI:
        print("⚠️ MONGO_URI not set. Skipping MongoDB connection.")
        return

    client = MongoClient(settings.MONGO_URI)
    db = client.get_database()

    print("✅ MongoDB connected")


def close_db():
    global client

    if client:
        client.close()
        print("🔌 MongoDB connection closed")
