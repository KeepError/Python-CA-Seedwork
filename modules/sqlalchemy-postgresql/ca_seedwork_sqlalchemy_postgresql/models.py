import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped


class PostgresModel:
    id: Mapped[uuid.UUID] = Column(UUID(as_uuid=True), primary_key=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
