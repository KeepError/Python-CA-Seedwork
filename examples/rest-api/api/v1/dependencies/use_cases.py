from typing import Iterator

from domain.user.usecases import UserUseCase
from infrastructure.sqlalchemy_postgresql.database import SessionLocal
from infrastructure.sqlalchemy_postgresql.user.repositories import UserRepository


def get_user_use_case() -> Iterator[UserUseCase]:
    session = SessionLocal()
    try:
        yield UserUseCase(UserRepository(session))
    finally:
        session.close()
