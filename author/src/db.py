from typing import Final

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.conf import env


POSTGRES_USER: Final = env.str('POSTGRES_USER')
POSTGRES_PASSWORD: Final = env.str('POSTGRES_PASSWORD')
POSTGRES_DB: Final = env.str('POSTGRES_DB_AUTHOR')


DB_URL: Final = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db_author/{POSTGRES_DB}'

async_angine = create_async_engine(DB_URL)

async_session_maker = async_sessionmaker(async_angine, expire_on_commit=False)


class Base(DeclarativeBase):
    ...
    