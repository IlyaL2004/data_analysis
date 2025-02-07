from app.core.config import settings
import redis.asyncio as redis

redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

async def get_redis_client() -> redis.Redis:
    yield redis_client
