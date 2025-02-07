from redis.asyncio import Redis

class CacheRepository:
    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def get_item_from_cache(self, item_id: str) -> str:
        return await self.redis_client.get(item_id)

    async def save_item_to_cache(self, item_id: str, value: str, ttl: int = 60):
        await self.redis_client.set(item_id, value, ex=ttl)
