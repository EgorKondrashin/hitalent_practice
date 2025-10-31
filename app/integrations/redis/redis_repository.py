from redis.asyncio import Redis


class RedisRepository:
    def __init__(
        self,
        redis: Redis,
    ) -> None:
        self._redis = redis

    async def get_user(
        self,
        user_id: int,
    ) -> str | None:
        key = self._get_key(user_id)
        result = await self._redis.get(key)
        if result is not None:
            return result.decode('utf-8') if isinstance(result, bytes) else result
        return None

    async def set_user(
        self,
        user_id: int,
        full_name: str,
    ) -> None:
        key = self._get_key(user_id)
        await self._redis.set(
            key,
            full_name,
            ex=60,
        )

    async def delete_user(
        self,
        user_id: int,
    ) -> None:
        key = self._get_key(user_id)
        await self._redis.delete(key)

    @staticmethod
    def _get_key(
        user_id: int,
    ) -> str:
        return f'user:{user_id}'
