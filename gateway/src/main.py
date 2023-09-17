from fastapi import FastAPI, Depends
from fastapi import Request, Response
from fastapi.security import APIKeyCookie
from fastapi.exceptions import HTTPException
from fastapi import status

from fastapi_gateway import route

from src.service_author.schemas import Author, UpdateAuthor
from src.service_book.schemas import Book, UpdateBook
from src.service_user.schemas import UserLogin

from .api_key import CustomAPIKey
from .conf import SERVICE_AUTHOR_URL, SERVICE_BOOK_URL, SERVICE_USER_URL


app = FastAPI(title='API Gateway', debug=True)

api_key_cookie = CustomAPIKey(name='access_token_cookie', auto_error=False)


def check_api_key(key: str = Depends(api_key_cookie)):
    if key:
        return key
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@route(
    request_method=app.post,
    service_url=SERVICE_USER_URL,
    service_path='/auth/login',
    gateway_path='/login',
    body_params=['login_user', ],
)
async def login(login_user: UserLogin, request: Request, response: Response):
    pass
    

@route(
    request_method=app.post,
    service_url=SERVICE_USER_URL, 
    service_path='/auth/logout',
    gateway_path='/logout',
    dependencies=[Depends(check_api_key)],
)
async def logout(request: Request, response: Response):
    pass


@route(
        request_method=app.post,
        service_url=SERVICE_USER_URL,
        service_path='/auth/refresh',
        gateway_path='/refresh',
        query_params=['refresh_token',]
)
async def refresh_token(refresh_token: str, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    service_url=SERVICE_AUTHOR_URL,
    service_path='/author/',
    gateway_path='/author/',
    dependencies=[Depends(check_api_key)],
)
async def get_authors(request: Request, response: Response):
    pass



@route(
    request_method=app.get,
    service_url=SERVICE_AUTHOR_URL,
    service_path='/author/{id}',
    gateway_path='/author/{id}',
    query_params=['id', ],
    dependencies=[Depends(check_api_key)],
)
async def get_author(id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.post,
    service_url=SERVICE_AUTHOR_URL,
    service_path='/author/',
    gateway_path='/author/',
    body_params=['author', ],
    dependencies=[Depends(check_api_key)],
)
async def create_author(author: Author, request: Request, response: Response):
    pass


@route(
    request_method=app.put,
    service_url=SERVICE_AUTHOR_URL,
    service_path='/author/{id}',
    gateway_path='/author/{id}',
    query_params=['id'],
    body_params=['author', ],
    dependencies=[Depends(check_api_key)],
)
async def update_author(id: int, author: UpdateAuthor, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    service_url=SERVICE_BOOK_URL,
    service_path='/book/',
    gateway_path='/book/',
    dependencies=[Depends(check_api_key)]
)
async def get_books(request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    service_url=SERVICE_BOOK_URL,
    service_path='/book/{id}',
    gateway_path='/book/{id}',
    dependencies=[Depends(check_api_key)]
)
async def get_book(id: int, request: Request, response: Response):
    pass


@route(
    request_method=app.post,
    service_url=SERVICE_BOOK_URL,
    service_path='/book/',
    gateway_path='/book/',
    body_params=['book', ],
    dependencies=[Depends(check_api_key)]
)
async def create_book(book: Book, request: Request, response: Response):
    pass


@route(
    request_method=app.put,
    service_url=SERVICE_BOOK_URL,
    service_path='/book/{id}',
    gateway_path='/book/{id}',
    query_params=['id', ],
    body_params=['book', ],
    dependencies=[Depends(check_api_key)]
)
async def update_book(id: int, book: UpdateBook, request: Request, response: Response):
    pass

