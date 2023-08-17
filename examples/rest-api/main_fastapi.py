from api.v1 import fastapi_app as fastapi_app_v1
from fastapi import FastAPI
from infrastructure.sqlalchemy_postgresql.database import setup_database

setup_database()

app = FastAPI()

app.mount("/v1", fastapi_app_v1.get_app())
