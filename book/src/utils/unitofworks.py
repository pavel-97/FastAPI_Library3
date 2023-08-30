from abc import ABC, abstractmethod

from src.db import async_session_maker
from src.utils.repositories import BookRepository


class AbstractUnitOfWork(ABC):
    def __init__(self) -> None:
        ...

    async def aenter(self, *args, **kwargs):
        raise NotImplementedError
    
    async def aexit(self, *args, **kwrgs):
        raise NotImplementedError
    
    async def commit(self):
        raise NotImplementedError
    
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.repository = BookRepository(self.session)
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.rollback()
        await self.session.close()

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()