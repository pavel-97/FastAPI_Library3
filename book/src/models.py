from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

from .db import Base
from .schemas import BookForModelDB


class Book(Base):
    __tablename__ = 'Book'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(128), unique=True)
    author_id: Mapped[int] = mapped_column(Integer)

    def __str__(self):
        return self.title
    
    def set_title(self, new_title):
        if new_title:
            self.title = new_title

    def set_author_id(self, new_author_id):
        if new_author_id:
            self.author_id = new_author_id

    def update(self, data):
        self.set_title(data.title)
        self.set_author_id(data.author_id)
    
    def read_model(self):
        return BookForModelDB(**self.__dict__)