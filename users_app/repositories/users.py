from repositories.base_repository import AbstractRepository
from sqlalchemy import select
from models.users import User
from passlib.context import CryptContext
from db.database import SessionLocal


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserRepository(AbstractRepository):
    session = SessionLocal
    model = User

    async def create_user(self, data: dict):
        with self.session() as session:
            user_model = self.model(
                email=data['email'],
                username=data['username'],
                hashed_password=bcrypt_context.hash(data['password'])
            )
            session.add(user_model)
            session.commit()
        return user_model

    async def authenticate_user(self,
                                username: str,
                                password: str):
        with self.session() as session:
            query = select(self.model).where(self.model.username == username)
            user = session.execute(query)
            user = user.scalar_one()
        if not user:
            return False
        if not bcrypt_context.verify(password, user.hashed_password):
            return False
        return user
