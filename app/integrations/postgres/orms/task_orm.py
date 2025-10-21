from enum import Enum as PyEnum
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum as SQLAlchemyEnum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.integrations.postgres.orms.base_orm import BaseORM
from app.integrations.postgres.orms.mixins.mixins import CreatedAtMixin, UuidPkMixin

if TYPE_CHECKING:
    from app.integrations.postgres.orms.user_orm import UserORM


class TaskStatusEnum(PyEnum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class TaskORM(
    BaseORM,
    UuidPkMixin,
    CreatedAtMixin,
):
    __tablename__ = 'tasks'
    title: Mapped[str] = mapped_column(
        String(255),
        comment='Название задачи.',
    )
    description: Mapped[str] = mapped_column(
        Text,
        comment='Описание задачи.',
    )
    status: Mapped[TaskStatusEnum] = mapped_column(
        SQLAlchemyEnum(
            TaskStatusEnum,
            name='task_status',
        ),
        default=TaskStatusEnum.TODO,
        server_default='TODO',
    )
    author_id: Mapped[UUID] = mapped_column(
        ForeignKey('users.id'),
        comment='Внешний ключ с таблицей users. (Автор задачи)',
        index=True,
    )
    assignee_id: Mapped[UUID | None] = mapped_column(
        ForeignKey('users.id'),
        comment='Внешний ключ с таблицей users. (Ответственный за выполнение задачи)',
        index=True,
    )
    column_id: Mapped[UUID | None] = mapped_column(
        ForeignKey('columns.id'),
        comment='Внешний ключ с таблицей columns.',
        index=True,
    )
    sprint_id: Mapped[UUID | None] = mapped_column(
        ForeignKey('sprints.id'),
        comment='Внешний ключ с таблицей sprints.',
        index=True,
    )
    board_id: Mapped[UUID | None] = mapped_column(
        ForeignKey('boards.id'),
        comment='Внешний ключ с таблицей boards.',
        index=True,
    )
    group_id: Mapped[UUID | None] = mapped_column(
        ForeignKey('groups.id'),
        comment='Внешний ключ с таблицей groups.',
        index=True,
    )
    watchers: Mapped[list['UserORM']] = relationship(
        secondary='task_watchers',
        back_populates='task_watching',
    )
    executors: Mapped[list['UserORM']] = relationship(
        secondary='task_executors',
        back_populates='task_executoring',
    )
