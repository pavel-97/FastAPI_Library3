from abc import ABC, abstractmethod

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import BaseModel

from src.models import Book
from src.utils.decorators import check_author_service


class AbstactRepository(ABC):

    @abstractmethod
    async def all(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def create(self, *args, **kwrgs):
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, *args, **kwrgs):
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstactRepository):
    model: DeclarativeBase

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        result = [row[0].read_model() for row in result.all()]
        return result
    
    @check_author_service
    async def create(self, schema: BaseModel):
        stml = insert(self.model).values(**schema.dict()).returning(self.model.id)
        result = await self.session.execute(stml)
        return result.scalar_one()
    
    async def get(self, id: int):
        obj = await self.session.get(self.model, id)
        return obj.read_model()

    async def update(self, id: int, data: BaseModel):
        book = await self.session.get(self.model, id)
        book.update(data)
        return book


class BookRepository(SQLAlchemyRepository):
    model = Book