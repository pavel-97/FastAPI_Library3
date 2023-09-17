from typing import Final

from environs import Env


env = Env()
env.read_env()


SERVICE_AUTHOR_URL: Final = env.str('SERVICE_AUTHOR_URL')
SERVICE_BOOK_URL: Final = env.str('SERVICE_BOOK_URL')
SERVICE_USER_URL: Final = env.str('SERVICE_USER_URL')
