from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import CreatedAtMixin, UuidPkMixin

if TYPE_CHECKING:
    from app.integrations.postgres.orms.task_orm import TaskORM


class UserORM(
    BaseORM,
    UuidPkMixin,
    CreatedAtMixin,
):
    __tablename__ = 'users'
    full_name: Mapped[str] = mapped_column(
        String(100),
        comment='Имя и фамилия пользователя.',
    )
    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        comment='Электронная почта пользователя.',
    )
    task_watching: Mapped[list['TaskORM']] = relationship(
        secondary='task_watchers',
        back_populates='watchers',
    )
    task_executoring: Mapped[list['TaskORM']] = relationship(
        secondary='task_executors',
        back_populates='executors',
    )
