from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


def get_current_datetime() -> datetime:
    return datetime.now(UTC).replace(tzinfo=None)


class UuidPkMixin:
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        server_default=func.gen_random_uuid(),
        comment='Уникальный идентификатор записи в таблице.',
    )


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        comment='Дата и время создания записи в таблице в формате RFC3339(YYYY-MM-DDTHH:mm:ssZ)',
        default=get_current_datetime,
        server_default=func.now(),
        index=True,
    )
