from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "zen-secret-key"
ALGORITHM = "HS256"


def create_access_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
