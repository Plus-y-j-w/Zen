from src.main import app


async def fetch(request):
    return await app(
        request.scope,
        request.receive,
        request.send
    )
