from typing import Final, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, Response
from fastapi import Request

from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, CookieTransport
from fastapi_users import BaseUserManager
from fastapi_users import IntegerIDMixin

from src.db import get_async_session

from .models import User


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


cookie_transport = CookieTransport(cookie_name='jwt', cookie_max_age=3600)

SECRET: Final = 'SECRET'


def get_jwt_strategy():
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


class UserMnager(IntegerIDMixin, BaseUserManager):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    
    async def on_after_register(self, user: User, request: Optional[Request] = None) -> None:
        print(f'User {user.id} has registred')

    async def on_after_login(self, user: User, request: Optional[Request] = None, response: Optional[Response] = None) -> None:
        print(f'User {user.id} login')

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserMnager(user_db)
