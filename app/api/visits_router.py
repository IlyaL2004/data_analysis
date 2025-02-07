from fastapi import APIRouter, HTTPException, Depends
from app.repositories.cache_repositories import CacheRepository
from app.repositories.visits_repositories import VisitRepository
from app.schemas.visits_schemas import VisitCreate, VisitСheck
from app.core.datagase import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.cache_services import CacheService
from app.services.visits_services import VisitService
from redis.asyncio import Redis
from app.core.database_redis import get_redis_client

visits_router = APIRouter(tags=["Visits"])  # Добавляем тег для документации

"""@visits_router.get("/get", response_model=VisitСheck, summary="Главная страница визитов")
async def read_visits_root( session: AsyncSession = Depends(get_async_session)):
    try:
        result = await session.execute(select(Visits))
        visits = result.scalars().all()
        if not visits:
            raise HTTPException(status_code=404, detail="No visits available")
        return visits[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")"""

@visits_router.get("/get", response_model=VisitСheck, summary="Главная страница визитов")
async def read_visits_root(
    session: AsyncSession = Depends(get_async_session)
):
    try:
        repository = VisitRepository(session)
        service = VisitService(repository)
        first_visit = await service.get_first_visit()
        if not first_visit:
            raise HTTPException(status_code=404, detail="No visits available")
        return first_visit
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

"""@visits_router.post("/create", response_model=VisitCreate, summary="Добавить новый визит")
async def create_visit(visit: VisitCreate,session: AsyncSession = Depends(get_async_session)):
    try:
        new_visit = Visits(
            user_email=visit.user_email,
            site_id=visit.site_id,
            date=visit.date,
            admin_name=visit.admin_name
        )
        session.add(new_visit)
        await session.commit()
        await session.refresh(new_visit)
        return new_visit

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating visit: {str(e)}")"""

@visits_router.post("/create", response_model=VisitCreate, summary="Добавить новый визит")
async def create_visit(visit: VisitCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        repository = VisitRepository(session)
        service = VisitService(repository)
        new_visit = await service.create_visit(visit.dict())
        return new_visit
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating visit: {str(e)}")


"""@visits_router.get("/items/{item_id}")
async def read_item(item_id: str, redis_client: Redis = Depends(get_redis_client)):
    cached_value = await redis_client.get(item_id)
    if cached_value:
        return {"item_id": item_id, "value": cached_value, "source": "cache"}
    await asyncio.sleep(3)
    computed_value = f"Value for {item_id}"
    await redis_client.set(item_id, computed_value, ex=60)
    return {"item_id": item_id, "value": computed_value, "source": "computed"}"""


@visits_router.get("/items/{item_id}")
async def read_item(item_id: str, redis_client: Redis = Depends(get_redis_client)):
    try:
        item_repository = CacheRepository(redis_client)
        item_service = CacheService(item_repository)
        result = await item_service.get_item(item_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cache error: {str(e)}")







