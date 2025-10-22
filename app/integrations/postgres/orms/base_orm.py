from sqlalchemy.orm import DeclarativeBase


class BaseORM(DeclarativeBase):
    __abstract__ = True
