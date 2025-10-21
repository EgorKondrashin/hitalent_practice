from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import UuidPkMixin


class TaskWatcher(
    BaseORM,
    UuidPkMixin,
):
    __tablename__ = 'task_watchers'
    __table_args__ = (
        UniqueConstraint(
            'task_id',
            'user_id',
            name='idx_unique_task_user_watcher',
        ),
    )

    task_id: Mapped[UUID] = mapped_column(
        ForeignKey('tasks.id'),
        comment='Внешний ключ с таблицей tasks.',
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey('users.id'),
        comment='Внешний ключ с таблицей users.',
    )
