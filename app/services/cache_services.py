import asyncio
from app.repositories.cache_repositories import CacheRepository

class CacheService:
    def __init__(self, cache_repository: CacheRepository):
        self.cache_repository = cache_repository

    async def get_item(self, item_id: str) -> dict:
        cached_value = await self.cache_repository.get_item_from_cache(item_id)
        if cached_value:
            return {"item_id": item_id, "value": cached_value, "source": "cache"}
        await asyncio.sleep(3)
        computed_value = f"Value for {item_id}"
        await self.cache_repository.save_item_to_cache(item_id, computed_value)
        return {"item_id": item_id, "value": computed_value, "source": "computed"}
