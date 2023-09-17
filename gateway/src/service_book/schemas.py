from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author_id: int


class UpdateBook(BaseModel):
    title: str|None
    author_id: int|None