from core.config import settings
from database.sqlite import SQLiteDatabase


class Database:
    """Database facade.

    Local development uses SQLite. Cloudflare Workers can use the existing
    D1 adapter without changing API-layer code.
    """

    def __init__(self):
        self.backend = None

    def connect(self):
        if self.backend is None:
            if settings.DATABASE_TYPE.lower() == "sqlite":
                self.backend = SQLiteDatabase(settings.DATABASE_URL)
                self.backend.connect()
            else:
                from database.d1 import d1
                self.backend = d1
        return self.backend

    def close(self):
        if self.backend is not None and hasattr(self.backend, "close"):
            self.backend.close()
            self.backend = None


# Shared database facade for the application.
database = Database()
