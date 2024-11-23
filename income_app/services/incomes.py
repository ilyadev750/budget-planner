from repositories.incomes import IncomeRepository
from models.incomes import TypeIncome, Income
from repositories.base_repository import ModelRepository
from db.database import SessionLocal


class IncomeService:

    def __init__(self,
                 session,
                 model,
                 income_repo):
        self.income_repo = income_repo()
        self.income_repo.session = session
        self.income_repo.model = model

    async def create(self, data: dict):
        result = await self.income_repo.create(data=data)
        return result

    async def get_user_incomes(self, data: dict):
        result = await self.income_repo.get_user_incomes(data=data)
        return result