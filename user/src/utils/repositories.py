from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.user.models import User


class SQLAlchemyRepository():
    model: DeclarativeBase = User

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: int, refresh_token: str):
        query = select(self.model).where(self.model.id == id, self.model.refresh_token == refresh_token)
        result = await self.session.execute(query)
        user = result.scalar_one()
        return user

    async def create(self, id: int, refresh_token: str):
        query = select(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        user = result.scalar_one()
        user.refresh_token = refresh_token
        return user
    
    async def delete(self, id: int):
        query = select(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        user = result.scalar_one()
        user.refresh_token = None
        return user
    
    async def update(self, id: int, new_refresh_token: str):
        query = select(self.model).where(self.model.id == id)
        result = await self.session.execute(query)
        user = result.scalar_one()
        user.refresh_token = new_refresh_token
        return user