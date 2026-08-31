from fastapi import FastAPI
from workers import asgi

from api.auth import router as auth_router
from database.schema import init_db

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


@app.on_event("startup")
async def startup():
    # SQLite is initialized for local development. Cloudflare D1 can use
    # its own migrations/bindings without requiring a local SQLite file.
    init_db()


@app.get("/")
async def root():
    return {"name": "Zen", "status": "running"}


@app.get("/health")
async def health():
    return {"healthy": True}


# Cloudflare Python Workers ASGI entrypoint.
Default = asgi.entrypoint(app)
