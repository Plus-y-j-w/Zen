from datetime import datetime, timedelta, timezone

from jose import jwt

from core.config import settings


def create_access_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.now(timezone.utc)
        + timedelta(hours=settings.JWT_EXPIRE_HOURS),
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )
