from ca_seedwork_sqlalchemy_postgresql.models import PostgresModel
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from ..database import Base


class UserModel(Base, PostgresModel):
    __tablename__ = "users"
    username: Mapped[str] = Column(String, nullable=False, unique=True)
    email: Mapped[str] = Column(String, nullable=False, unique=True)
