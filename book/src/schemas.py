from pydantic import BaseModel


class Author(BaseModel):
    id: int|None
    first_name: str
    last_name: str


class Book(BaseModel):
    id: str
    title: str
    author: Author


class CreateBook(BaseModel):
    title: str
    author_id: int


class UpdateBook(BaseModel):
    title: str|None
    author_id: int|None


class BookForModelDB(BaseModel):
    id: int
    title: str
    author_id: int