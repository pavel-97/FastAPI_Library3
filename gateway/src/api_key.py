import aiohttp

from fastapi.security import APIKeyCookie
from fastapi.exceptions import HTTPException

from starlette.requests import Request
from starlette.status import HTTP_200_OK

from .conf import SERVICE_USER_URL


class CustomAPIKey(APIKeyCookie):
    async def __call__(self, request: Request) -> str | None:
        key = await super().__call__(request)
        async with aiohttp.ClientSession(cookies={'access_token_cookie': key}) as session:
            async with session.get(f'{SERVICE_USER_URL}/auth/protected-route') as response:
                if response.status == HTTP_200_OK:
                    return key
        raise HTTPException(status_code=response.status)