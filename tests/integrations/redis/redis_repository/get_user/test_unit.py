from fakeredis.aioredis import FakeRedis

from app.integrations.redis.redis_repository import RedisRepository


async def test_empty_cache(
    fake_redis_repository: RedisRepository,
) -> None:
    assert await fake_redis_repository.get_user(1) is None


async def test_happy_path(
    fake_redis_repository: RedisRepository,
    fake_redis: FakeRedis,
) -> None:
    user_id = 1
    data = 'test'
    await fake_redis.set(f'user:{user_id}', data)
    assert await fake_redis_repository.get_user(user_id) == data
