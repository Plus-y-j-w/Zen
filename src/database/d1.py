class D1Database:
    """Cloudflare D1 database adapter.

    Compatible abstraction for local SQLite and Cloudflare D1.
    """

    def __init__(self, client=None):
        self.client = client

    async def execute(self, query: str, params=None):
        params = params or []

        if self.client:
            return await self.client.execute(query, params)

        return None


d1 = D1Database()
