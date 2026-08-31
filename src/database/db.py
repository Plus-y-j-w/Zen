class Database:
    """Zen database abstraction.

    Later versions will support Cloudflare D1 and SQLite.
    """

    def __init__(self):
        self.connected = False

    async def connect(self):
        self.connected = True

    async def close(self):
        self.connected = False


 database = Database()
