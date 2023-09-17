from fastapi_users.db import SQLAlchemyBaseUserTable

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from src.db import Base


class User(SQLAlchemyBaseUserTable, Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    refresh_token: Mapped[str] = mapped_column(String, unique=True, nullable=True)

    def __str__(self) -> str:
        return f'{self.id}: {self.email}'
