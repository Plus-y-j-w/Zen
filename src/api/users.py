from fastapi import APIRouter

from src.core.security import create_access_token

router = APIRouter()


_users = []


@router.post('/register')
async def register(username: str, password: str):
    user = {
        'username': username,
        'password': password
    }
    _users.append(user)
    return {'message': 'registered', 'username': username}


@router.post('/login')
async def login(username: str, password: str):
    for user in _users:
        if user['username'] == username and user['password'] == password:
            return {
                'access_token': create_access_token(username),
                'token_type': 'bearer'
            }

    return {'error': 'invalid credentials'}


@router.get('/me')
async def me():
    return {'message': 'user profile'}
