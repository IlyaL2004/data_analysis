from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

AsyncSessionFactory = async_sessionmaker(async_engine)

async def get_async_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session

class Base(DeclarativeBase):
    pass



