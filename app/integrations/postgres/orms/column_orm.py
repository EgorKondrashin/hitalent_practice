from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import UuidPkMixin


class ColumnORM(
    BaseORM,
    UuidPkMixin,
):
    __tablename__ = 'columns'
    name: Mapped[str] = mapped_column(
        String(100),
        comment='Название столбца.',
    )
    board_id: Mapped[UUID] = mapped_column(
        ForeignKey('boards.id'),
        comment='Внешний ключ с таблицей boards.',
    )
