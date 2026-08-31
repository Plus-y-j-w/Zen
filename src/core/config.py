import os
from pathlib import Path

from dotenv import load_dotenv


# Load .env for local development. Cloudflare Workers can use its own
# environment/bindings and does not require a local .env file.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Zen")
    JWT_SECRET = os.getenv("JWT_SECRET", "zen-secret-key")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRE_HOURS = int(os.getenv("JWT_EXPIRE_HOURS", "24"))

    ZEN_ENV = os.getenv("ZEN_ENV", "development")
    DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlite")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        str(PROJECT_ROOT / "data" / "zen.db"),
    )

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "8000"))


settings = Settings()
