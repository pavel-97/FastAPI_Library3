import aiohttp

from fastapi import HTTPException


def check_author_service(func):
    async def wrapper(*args, **kwargs):
        async with aiohttp.ClientSession() as session:
            author_id = args[1].author_id
            async with session.get(f'http://author_app:8000/author/{author_id}') as response:
                if response.status == 404:
                    raise HTTPException(status_code=404, detail=f'Author with id={author_id} Not Found')
        result = await func(*args, **kwargs)
        return result
    return wrapper