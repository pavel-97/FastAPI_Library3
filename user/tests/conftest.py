import pytest
import asyncio

from typing import Final

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from httpx import AsyncClient

from src.main import app
from src.db import Base, get_async_session
from src.utils.unitofworks import UnitOfWork

from .conf import env


POSTGRES_DB_TEST: Final = env.str('POSTGRES_DB_TEST')
POSTGRES_USER_TEST: Final = env.str('POSTGRES_USER_TEST')
POSTGRES_PASSWORD_TEST: Final = env.str('POSTGRES_PASSWORD_TEST')


DB_URL: Final = f'postgresql+asyncpg://{POSTGRES_USER_TEST}:{POSTGRES_PASSWORD_TEST}@db_test/{POSTGRES_DB_TEST}'


async_engine = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


Base.metadata.bind = async_engine


async def get_override_async_session():
    async with async_session_maker() as session:
        yield session


class TestUnitOfWork(UnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker


app.dependency_overrides[get_async_session] = get_override_async_session
app.dependency_overrides[UnitOfWork] = TestUnitOfWork


@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def async_client():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
