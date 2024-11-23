from .base_repository import ModelRepository
from sqlalchemy import insert, select


class IncomeRepository(ModelRepository):
    session = None
    model = None

    async def create(self, data: dict):
        with self.session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = session.execute(stmt).scalar_one()
            session.commit()
            return res

    async def get_user_incomes(self, data: dict):
        with self.session() as session:
            query = (select(self.model)
                     .where(self.model.created_at >= data['starttime'])
                     .where(self.model.created_at <= data['endtime']))
            res = session.execute(query).scalars().all()
            return res
