from pydantic import BaseModel

from src.utils.unitofworks import UnitOfWork
from src.repositories.author import AuthorRepository


class AuthorService:

    async def create(self, uow: UnitOfWork, obj: BaseModel):
        async with uow(AuthorRepository):
            author = await uow.repository.create(obj)
            await uow.commit()
            return author
        
    async def update(self, uow: UnitOfWork, id: int, obj: BaseModel):
        async with uow(AuthorRepository):
            author = await uow.repository.update(id, obj)
            await uow.commit()
            return author
        
    async def all(self, uow: UnitOfWork):
        async with uow(AuthorRepository):
            authors = await uow.repository.all()
            return authors
        
    async def get(self, uow: UnitOfWork, id: int):
        async with uow(AuthorRepository):
            author = await uow.repository.get(id)
            return author