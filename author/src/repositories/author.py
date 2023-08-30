from src.utils.repositories import SQLAlchemyRepository

from src.author.models import Author


class AuthorRepository(SQLAlchemyRepository):
    model = Author