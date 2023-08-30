from pydantic import BaseModel


class Author(BaseModel):
    id: int
    first_name: str
    last_name: str


class CreateAuthor(BaseModel):
    first_name: str
    last_name: str


class UpdateAuthor(BaseModel):
    first_name: str | None
    last_name: str | None
    