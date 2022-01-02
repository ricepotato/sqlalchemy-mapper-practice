from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper

import models

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("email", String(50)),
)


def start_mappers():
    _ = mapper(models.User, user)
