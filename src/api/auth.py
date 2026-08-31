from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.password import hash_password, verify_password
from core.security import create_access_token
from database.db import database

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(request: RegisterRequest):
    if not request.username.strip() or len(request.password) < 6:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    backend = database.connect()
    existing = backend.execute(
        "SELECT id FROM users WHERE username = ?",
        (request.username.strip(),),
    ).fetchone()
    if existing:
        raise HTTPException(status_code=409, detail="Username already exists")

    cursor = backend.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (request.username.strip(), hash_password(request.password)),
    )
    return {"id": cursor.lastrowid, "username": request.username.strip()}


@router.post("/login")
def login(request: LoginRequest):
    backend = database.connect()
    user = backend.execute(
        "SELECT id, username, password_hash, is_active FROM users WHERE username = ?",
        (request.username.strip(),),
    ).fetchone()

    if not user or not user["is_active"] or not verify_password(
        request.password, user["password_hash"]
    ):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "access_token": create_access_token(user["username"]),
        "token_type": "bearer",
        "user_id": user["id"],
        "username": user["username"],
    }
