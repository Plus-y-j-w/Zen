import os


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Zen")
    JWT_SECRET = os.getenv("JWT_SECRET", "zen-secret-key")


settings = Settings()
