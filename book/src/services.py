from src.utils.unitofworks import UnitOfWork
from src.utils.mixins import GetAuthorMixin

from .schemas import CreateBook, UpdateBook


class BookService(GetAuthorMixin):
    async def create(self, uow: UnitOfWork, obj: CreateBook):
        async with uow:
            new_book = await uow.repository.create(obj)
            await uow.commit()
            return new_book
        
    async def update(self, uow: UnitOfWork, id: int, data: UpdateBook):
        async with uow:
            book = await uow.repository.update(id, data)
            await uow.commit()
            return book
        
    async def all(self, uow: UnitOfWork):
        async with uow:
            books = await uow.repository.all()
            return await self.get_books_with_authors(books)
        
    async def get(self, uow: UnitOfWork, id: int):
        async with uow:
            book = await uow.repository.get(id)
            return await self.get_book_with_authors(book)
        