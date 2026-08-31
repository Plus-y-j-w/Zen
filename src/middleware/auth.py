from fastapi import Header, HTTPException
from jose import jwt, JWTError

from src.core.config import settings


async def verify_token(
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail='Missing token'
        )

    token = authorization.replace('Bearer ', '')

    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=['HS256']
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid token'
        )
