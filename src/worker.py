from main import app
from workers import asgi

# Expose the FastAPI application through Cloudflare's native ASGI adapter.
Default = asgi.entrypoint(app)
