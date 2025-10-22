from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import UuidPkMixin


class BoardORM(
    BaseORM,
    UuidPkMixin,
):
    __tablename__ = 'boards'
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        comment='Название доски.',
    )
