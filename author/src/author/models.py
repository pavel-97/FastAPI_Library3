from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from pydantic import BaseModel

from src.db import Base


class Author(Base):
    __tablename__ = 'Author'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(128))
    last_name: Mapped[str] = mapped_column(String(128))

    def __str__(self) -> str:
        return f'{self.id}'
    
    def set_first_name(self, new_first_name: str):
        if new_first_name:
            self.first_name = new_first_name

    def set_last_name(self, new_last_name: str):
        if new_last_name:
            self.last_name = new_last_name

    def update(self, data: BaseModel):
        self.set_first_name(data.first_name)
        self.set_last_name(data.last_name)
    