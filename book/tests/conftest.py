import pytest

import asyncio

from httpx import AsyncClient

from src.main import app
from src.db import Base
from src.utils.unitofworks import UnitOfWork

from .db import async_engine
from .utils.unitofworks import TestUnitOfWork


Base.metadata.bind = async_engine

app.dependency_overrides[UnitOfWork] = TestUnitOfWork


@pytest.fixture(scope='session', autouse=True)
async def prepare_db():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()



@pytest.fixture(scope='session')
async def async_client():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


