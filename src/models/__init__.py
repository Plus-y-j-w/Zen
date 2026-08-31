from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    api_key: str | None = None
