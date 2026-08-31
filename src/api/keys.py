import hashlib
import secrets

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database.db import database

router = APIRouter()


class CreateKeyRequest(BaseModel):
    user_id: int
    name: str = "default"


def _hash_key(key: str) -> str:
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


@router.post("/create")
def create_key(request: CreateKeyRequest):
    backend = database.connect()
    user = backend.execute(
        "SELECT id FROM users WHERE id = ? AND is_active = 1",
        (request.user_id,),
    ).fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    key = "zen_" + secrets.token_urlsafe(32)
    backend.execute(
        "INSERT INTO api_keys (user_id, name, key_hash, key_prefix) VALUES (?, ?, ?, ?)",
        (request.user_id, request.name.strip() or "default", _hash_key(key), key[:12]),
    )

    # The plaintext key is returned only once and is never stored.
    return {"api_key": key, "name": request.name.strip() or "default"}


@router.get("/list/{user_id}")
def list_keys(user_id: int):
    backend = database.connect()
    rows = backend.execute(
        "SELECT id, name, key_prefix, is_active, created_at, last_used_at "
        "FROM api_keys WHERE user_id = ? ORDER BY id DESC",
        (user_id,),
    ).fetchall()
    return [dict(row) for row in rows]


@router.delete("/{key_id}")
def delete_key(key_id: int):
    backend = database.connect()
    cursor = backend.execute(
        "UPDATE api_keys SET is_active = 0 WHERE id = ?",
        (key_id,),
    )
    return {"deleted": cursor.rowcount > 0}
