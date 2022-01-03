import os
import pytest
from faker import Faker
from models import User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from orm import metadata, start_mappers


@pytest.fixture
def sqlite_db():
    sqlite_db_filepath = "db.sqlite"
    if os.path.exists(sqlite_db_filepath):
        os.remove(sqlite_db_filepath)
    engine = create_engine(f"sqlite:///{sqlite_db_filepath}")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_session(sqlite_db):
    start_mappers()
    yield sessionmaker(bind=sqlite_db, autocommit=True)()
    clear_mappers()


@pytest.fixture
def fake_users():
    faker = Faker()
    return [User(name=faker.name(), email=faker.email()) for _ in range(10)]

