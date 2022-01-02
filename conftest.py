import os
import pytest

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
