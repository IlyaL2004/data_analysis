# services/visit_service.py
from app.repositories.visits_repositories import VisitRepository

class VisitService:
    def __init__(self, repository: VisitRepository):
        self.repository = repository

    async def get_first_visit(self):
        visits = await self.repository.get_all_visits()
        if not visits:
            return None
        return visits[0]

    async def create_visit(self, visit_data: dict):
        return await self.repository.create_visit(visit_data)