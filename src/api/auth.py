from fastapi import APIRouter

from src.core.security import create_access_token

router = APIRouter()


@router.post('/login')
async def login(username: str, password: str):
    # Demo authentication placeholder.
    # Replace with database verification in production.
    if username and password:
        return {
            'access_token': create_access_token(username),
            'token_type': 'bearer'
        }

    return {
        'error': 'invalid credentials'
    }
