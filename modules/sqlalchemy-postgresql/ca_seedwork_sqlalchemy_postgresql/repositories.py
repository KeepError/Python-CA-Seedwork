import uuid
from abc import ABCMeta

from sqlalchemy.orm import Session

from ca_seedwork.repositories import IRepository, TEntity
from .data_mappers import PostgresDataMapper
from .models import PostgresModel


class PostgresRepositoryMeta(ABCMeta):
    def __init__(cls: type["PostgresRepository"], name: str, bases: tuple[type, ...], namespace: dict[str, object]):
        super().__init__(name, bases, namespace)
        if cls.__name__ == "PostgresRepository":
            return
        if not hasattr(cls, "Meta"):
            raise TypeError(f"Class {name} must have Meta class")
        if not hasattr(cls.Meta, "model"):
            raise TypeError(f"Class {name} must have model attribute")
        if not issubclass(cls.Meta.model, PostgresModel):
            raise TypeError(f"Class {name}.Meta.model must be subclass of PostgresModel")
        if not hasattr(cls.Meta, "data_mapper"):
            raise TypeError(f"Class {name} must have data_mapper attribute")
        if not issubclass(cls.Meta.data_mapper, PostgresDataMapper):
            raise TypeError(f"Class {name}.Meta.data_mapper must be subclass of PostgresDataMapper")


class PostgresRepository(IRepository, metaclass=PostgresRepositoryMeta):
    session: Session

    class Meta:
        model: type[PostgresModel]
        data_mapper: type[PostgresDataMapper[TEntity, "model"]]

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, entity_id: uuid.UUID) -> TEntity | None:
        model = self.session.query(self.Meta.model).filter_by(id=entity_id).one_or_none()
        if model:
            return self.Meta.data_mapper.model_to_entity(model)
        return None

    def add(self, entity: TEntity) -> None:
        model = self.Meta.data_mapper.entity_to_model(entity)
        self.session.add(model)

    def remove_by_id(self, entity_id: uuid.UUID) -> None:
        self.session.query(self.Meta.model).filter_by(id=entity_id).delete()

    def next_id(self) -> uuid.UUID:
        return uuid.uuid4()
