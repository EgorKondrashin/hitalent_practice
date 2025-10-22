from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import UuidPkMixin


class GroupORM(
    BaseORM,
    UuidPkMixin,
):
    __tablename__ = 'groups'
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        comment='Название группы.',
    )
