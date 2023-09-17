from typing import Any

from fastapi.exceptions import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from src.db import async_session_maker

from .repositories import SQLAlchemyRepository


class UnitOfWork():
    def __init__(self):
        self.session_factory = async_session_maker

    def __call__(self, repository: SQLAlchemyRepository) -> Any:
        self.repository = repository
        return self

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        self.repository = self.repository(self.session)

    async def __aexit__(self, type, value, traceback):
        await self.rollback()
        await self.session.close()
        if type:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{value}')

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()
