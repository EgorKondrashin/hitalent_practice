from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import UuidPkMixin


class SprintORM(
    BaseORM,
    UuidPkMixin,
):
    __tablename__ = 'sprints'
    name: Mapped[str] = mapped_column(
        String(100),
        comment='Название спринта.',
    )
    start_date: Mapped[date] = mapped_column(
        comment='Дата начала спринта.',
    )
    end_date: Mapped[date] = mapped_column(
        comment='Дата окончания спринта.',
    )
