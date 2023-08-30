from typing import Final

from environs import Env

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


env = Env()
env.read_env()


POSTGRES_USER_TEST: Final = env.str('POSTGRES_USER_TEST')
POSTGRES_PASSWORD_TEST: Final = env.str('POSTGRES_PASSWORD_TEST')
POSTGRES_DB_TEST: Final = env.str('POSTGRES_DB_TEST')


DB_URL_TEST: Final = f'postgresql+asyncpg://{POSTGRES_USER_TEST}:{POSTGRES_PASSWORD_TEST}@db_test/{POSTGRES_DB_TEST}'

async_engine = create_async_engine(DB_URL_TEST)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)