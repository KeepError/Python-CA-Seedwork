from pydantic_settings import BaseSettings


class Config(BaseSettings):
    POSTGRES_CONNECTION_STRING: str = (
        "postgresql+psycopg2://postgres:postgres@localhost:5432/rest_api"
    )


config = Config()
