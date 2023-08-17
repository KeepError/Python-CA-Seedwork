from abc import ABC

from ca_seedwork.repositories import IRepository
from .entities import User


class IUserRepository(IRepository, ABC):
    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError
