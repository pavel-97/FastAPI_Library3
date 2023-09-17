from typing import Final

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from .conf import env


POSTGRES_USER: Final = env.str('POSTGRES_USER')
POSTGRES_PASSWORD: Final = env.str('POSTGRES_PASSWORD')
POSTGRES_DB: Final = env.str('POSTGRES_DB')


DB_URL: Final = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db_user/{POSTGRES_DB}'

async_engin = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(async_engin, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    ...
