from fakeredis.aioredis import FakeRedis

from app.integrations.redis.redis_repository import RedisRepository


async def test_happy_path(
    fake_redis_repository: RedisRepository,
    fake_redis: FakeRedis,
) -> None:
    user_id = 1
    data = 'test'
    assert await fake_redis.get(f'user:{user_id}') is None
    await fake_redis_repository.set_user(user_id=user_id, full_name=data)
    assert (await fake_redis.get(f'user:{user_id}')).decode('utf-8') == data
