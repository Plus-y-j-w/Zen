from fastapi import FastAPI
from workers import asgi

from src.api.auth import router as auth_router

app = FastAPI(
    title="Zen",
    version="0.1.0",
    description="FastAPI application for Cloudflare Workers",
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)


@app.get("/")
async def root():
    return {
        "name": "Zen",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "healthy": True,
    }


# Cloudflare Python Workers ASGI entrypoint.
Default = asgi.entrypoint(app)
