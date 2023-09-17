from fastapi import FastAPI, Response, status

from fastapi_users import FastAPIUsers

from src.utils.tools import create_set_access_refresh_tokens, delete_access_refresh_tokens, refresh_tokens
from src.utils.services import UserService
from src.user.dependencies import UserManagerDep, JwtAuthCredentials, UOWDep
from src.user.managers import get_user_manager
from src.user.managers import auth_backend
from src.user.schemas import UserRead, UserCreate, Login


fastapi_users = FastAPIUsers(get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)


app = FastAPI()


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
    )


@app.post('/auth/login', tags=['auth'])
async def login(response: Response, user_login: Login, uow: UOWDep, user_manager: UserManagerDep):
    user = await user_manager.authenticate(user_login)
    subject = {'username': user.email, 'id': user.id}
    access_token, refresh_token = create_set_access_refresh_tokens(response, subject)
    await UserService().create(uow, subject, refresh_token)
    return {'refresh_token': refresh_token, 'access_token': access_token}


@app.post('/auth/logout', tags=['auth'])
async def logout(response: Response, uow: UOWDep, credintials: JwtAuthCredentials):
    delete_access_refresh_tokens(response)
    await UserService().delete(uow, credintials.subject)
    return {'logout': 'ok'}


@app.post('/auth/refresh', tags=['auth'])
async def refresh(refresh_token: str, response: Response, uow: UOWDep):
    user_service = UserService(refresh_token)
    await user_service.check_refresh_token(uow, refresh_token)
    new_access_token, new_refresh_token = refresh_tokens(response, refresh_token)
    await user_service.update(uow, new_refresh_token)
    return {'refresh_token': new_refresh_token, 'access_token': new_access_token}


@app.get('/auth/protected-route')
async def protected_route(credintials: JwtAuthCredentials):
    return Response(status_code=status.HTTP_200_OK)