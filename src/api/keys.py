from fastapi import APIRouter
import secrets

router = APIRouter()

_keys = []


@router.post('/create')
async def create_key(username: str):
    key = 'zen_' + secrets.token_hex(16)
    _keys.append({
        'username': username,
        'key': key
    })
    return {'api_key': key}


@router.get('/list')
async def list_keys():
    return _keys


@router.delete('/{key}')
async def delete_key(key: str):
    global _keys
    _keys = [x for x in _keys if x['key'] != key]
    return {'deleted': True}
