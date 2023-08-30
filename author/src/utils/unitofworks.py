from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from src.db import async_session_maker

from .repositories import SQLAlchemyRepository


class AbstractUnitOfWork(ABC):
    repository: SQLAlchemyRepository

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    async def commit(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def rollback(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def __aenter__(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def __aexit__(self, *args, **kwargs):
        raise NotImplementedError
    

class UnitOfWork(AbstractUnitOfWork):

    def __init__(self):
        self.session_factory = async_session_maker

    def __call__(self, repository: SQLAlchemyRepository) -> Any:
        self.repository = repository
        return self
        

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        self.repository = self.repository(self.session)

    async def __aexit__(self, *args, **kwargs):
        await self.rollback()
        await self.session.close()

    async def commit(self, *args, **kwargs):
        await self.session.commit(*args, **kwargs)

    async def rollback(self):
        await self.session.rollback()