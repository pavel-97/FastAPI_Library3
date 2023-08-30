from abc import ABC, abstractmethod

from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException

from pydantic import BaseModel

from src.db import Base


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def all(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):

    model: Optional[Base] = None
    
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def create(self, schema: BaseModel):
        stml = insert(self.model).values(**schema.dict()).returning(self.model.id)
        result = await self.session.execute(stml)
        return result.scalar_one()
    
    async def update(self, id: int, schema: BaseModel):
        obj = await self.session.get(self.model, id)
        obj.update(schema)
        return obj.__dict__


    async def all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        result = [row[0].__dict__ for row in result.all()]
        return result

    async def get(self, id: int):
        result = await self.session.get(self.model, id)
        if result is None:
            raise HTTPException(status_code=404, detail='Not Found')
        return result.__dict__