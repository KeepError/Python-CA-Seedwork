import uuid

from ca_seedwork.usecases import UseCase

from .entities import User
from .repositories import IUserRepository
from .errors import UserNotFoundError


class UserUseCase(UseCase):
    user_repository: IUserRepository

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def get(self, user_id: uuid.UUID) -> User:
        user = self.user_repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError()
        return user

    def create(self, username: str, email: str) -> User:
        user = User(
            id=self.user_repository.next_id(),
            email=email,
            username=username,
        )
        self.user_repository.add(user)
        return user
