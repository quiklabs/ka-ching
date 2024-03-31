from os import getenv

from dotenv import load_dotenv

load_dotenv()

MONGODB_URI: str = getenv("MONGODB_URI")
MONGODB_DB_NAME: str = getenv("MONGODB_DB_NAME")
SESSION_SECRET: str = getenv("SESSION_SECRET")
AUTH_TOKEN = getenv("AUTH_TOKEN")
ADMIN_EMAIL: str = getenv("ADMIN_EMAIL")
ADMIN_PASSWORD: str = getenv("ADMIN_PASSWORD")
REDIS_URL: str = getenv("REDIS_URL")
ENC_KEY: str = getenv("ENC_KEY")

print("[Initialized] Environment Variables")
