# repositories/visit_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.visits_models import Visits
from sqlalchemy import select

class VisitRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_visits(self):
        result = await self.session.execute(select(Visits))
        return result.scalars().all()

    async def create_visit(self, visit_data: dict):
        new_visit = Visits(**visit_data)
        self.session.add(new_visit)
        await self.session.commit()
        await self.session.refresh(new_visit)
        return new_visit