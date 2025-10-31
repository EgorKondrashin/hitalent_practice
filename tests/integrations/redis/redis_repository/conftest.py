from fakeredis.aioredis import FakeRedis
import pytest

from app.integrations.redis.redis_repository import RedisRepository


@pytest.fixture
def fake_redis_repository(fake_redis: FakeRedis) -> RedisRepository:
    return RedisRepository(redis=fake_redis)


@pytest.fixture
def fake_redis() -> FakeRedis:
    return FakeRedis()
