from dataclasses import dataclass

from ca_seedwork.entities import Entity


@dataclass
class User(Entity):
    username: str
    email: str
