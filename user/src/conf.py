from typing import Final

from environs import Env

from datetime import timedelta

from fastapi_jwt import JwtAccessCookie, JwtRefreshCookie


env = Env()
env.read_env()


SECRET: Final = 'SECRET'

RABBITMQ_LOGIN: Final = env.str('RABBITMQ_DEFAULT_USER')
RABBITMQ_PASSWORD: Final = env.str('RABBITMQ_DEFAULT_PASS')

EMAIL: Final = env.str('EMAIL')
EMAIL_PASSWORD: Final = env.str('EMAIL_PASSWORD')


access_security = JwtAccessCookie(secret_key=SECRET, auto_error=True, access_expires_delta=timedelta(minutes=5))
refresh_security = JwtRefreshCookie(secret_key=SECRET, auto_error=True, refresh_expires_delta=timedelta(minutes=30))
