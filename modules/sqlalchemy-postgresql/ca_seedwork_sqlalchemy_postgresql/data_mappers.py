from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic

from ca_seedwork.entities import Entity
from .models import PostgresModel

TEntity = TypeVar("TEntity", bound=Entity)
TModel = TypeVar("TModel", bound=PostgresModel)


class PostgresDataMapper(Generic[TEntity, TModel], metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def model_to_entity(model: TModel) -> TEntity:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def entity_to_model(entity: TEntity) -> TModel:
        raise NotImplementedError
