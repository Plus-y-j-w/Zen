from pathlib import Path
import sqlite3


class SQLiteDatabase:
    """Local SQLite adapter used by the FastAPI development server."""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.connection: sqlite3.Connection | None = None

    def _path(self) -> str:
        path = Path(self.database_url).expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        path.parent.mkdir(parents=True, exist_ok=True)
        return str(path)

    def connect(self) -> sqlite3.Connection:
        if self.connection is None:
            self.connection = sqlite3.connect(
                self._path(),
                check_same_thread=False,
            )
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def execute(self, query: str, params=()):
        connection = self.connect()
        cursor = connection.execute(query, params)
        connection.commit()
        return cursor

    def executescript(self, script: str):
        connection = self.connect()
        connection.executescript(script)
        connection.commit()

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
