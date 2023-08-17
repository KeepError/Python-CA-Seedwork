from ca_seedwork_sqlalchemy_postgresql.data_mappers import PostgresDataMapper
from ca_seedwork_sqlalchemy_postgresql.repositories import PostgresRepository, PostgresRepositoryMeta
from domain.user.entities import User
from domain.user.repositories import IUserRepository

from .models import UserModel


class UserDataMapper(PostgresDataMapper):
    @staticmethod
    def model_to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            username=model.username,
            email=model.email,
        )

    @staticmethod
    def entity_to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            username=entity.username,
            email=entity.email,
        )


class UserRepository(IUserRepository, PostgresRepository, metaclass=PostgresRepositoryMeta):
    class Meta:
        model = UserModel
        data_mapper = UserDataMapper

    def get_by_email(self, email: str) -> Meta.model | None:
        model = self.session.query(self.Meta.model).filter_by(email=email).one_or_none()
        if model:
            return self.Meta.data_mapper.model_to_entity(model)
        return None
