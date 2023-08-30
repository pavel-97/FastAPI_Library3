from src.schemas import Book

from .tools import make_get_request


class GetAuthorMixin:
    async def get_books_with_authors(self, books):
        books_with_authors = list()
        for book in books:
            author = await make_get_request(f'http://author_app:8000/author/{book.author_id}')
            books_with_authors.append(Book(id=book.id, title=book.title, author=author))
        return books_with_authors
    
    async def get_book_with_authors(self, book):
        author = await make_get_request(f'http://author_app:8000/author/{book.author_id}')
        return Book(id=book.id, title=book.title, author=author)